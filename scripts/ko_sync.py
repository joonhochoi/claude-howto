#!/usr/bin/env python3
"""ko/ 번역 상태·드리프트 점검 도구.

`ko/`의 각 마크다운 머리에 기록된 i18n 헤더를 읽어
1) 번역 진행률(status)과 2) 원문 변경(drift)을 보고한다.

헤더 규약 (ko/TRANSLATION_NOTES.md 참조):
    <!-- i18n-source: README.md -->
    <!-- i18n-source-sha: 188f468 -->
    <!-- i18n-status: translated | source-copy -->
    <!-- i18n-date: 2026-10-26 -->

사용:
    python3 scripts/ko_sync.py status [--verbose] [--json]
    python3 scripts/ko_sync.py diff   ko/01-slash-commands/README.md
    python3 scripts/ko_sync.py stamp  ko/01-slash-commands/README.md [--keep-status]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

HEADER_RE = re.compile(r"^<!-- i18n-(source|source-sha|status|date): (.*?) -->$", re.M)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def git(args: list[str], cwd: Path) -> str:
    out = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 else ""


def read_header(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")[:600]
    return {m.group(1): m.group(2).strip() for m in HEADER_RE.finditer(text)}


def collect(root: Path, lang: str) -> list[dict]:
    base = root / lang
    rows: list[dict] = []
    if not base.exists():
        return rows
    for md in sorted(base.rglob("*.md")):
        h = read_header(md)
        if "source" not in h:
            rows.append(
                {
                    "path": str(md.relative_to(root)),
                    "source": None,
                    "sha": None,
                    "status": "template (헤더 없음)",
                    "changed": False,
                }
            )
            continue
        src = root / h["source"]
        sha = h.get("source-sha", "")
        changed = False
        commits = ""
        if src.exists() and sha:
            commits = git(["log", "--oneline", f"{sha}..HEAD", "--", h["source"]], root)
            changed = bool(commits)
        elif not src.exists():
            commits = "(원문 파일 없음)"
            changed = True
        rows.append(
            {
                "path": str(md.relative_to(root)),
                "source": h["source"],
                "sha": sha,
                "status": h.get("status", "?"),
                "changed": changed,
                "commits": commits,
            }
        )
    return rows


def cmd_status(root: Path, lang: str, verbose: bool, as_json: bool) -> int:
    rows = collect(root, lang)
    translated = [r for r in rows if r["status"] == "translated"]
    copies = [r for r in rows if r["status"] == "source-copy"]
    drift = [r for r in rows if r["changed"] and r["status"] == "translated"]
    pending = [r for r in rows if r["changed"] and r["status"] == "source-copy"]
    head = git(["rev-parse", "--short=7", "HEAD"], root)

    if as_json:
        print(json.dumps({"head": head, "rows": rows}, ensure_ascii=False, indent=2))
        return 0

    print(f"HEAD {head} · {lang}/ 파일 {len(rows)}개")
    print(f"  번역 완료 {len(translated)} · 원문 복사 상태 {len(copies)}")
    print(f"  원문이 바뀐 파일: 번역본 {len(drift)}개 / 미번역 {len(pending)}개")

    if drift:
        print("\n⚠️  번역 후 원문이 변경됨 (재번역 필요)")
        for r in drift:
            print(f"  - {r['path']}  (기록 {r['sha']})")
            if verbose:
                for line in r["commits"].splitlines():
                    print(f"      {line}")
    if pending:
        print("\n📝 아직 번역 전인데 원문이 바뀐 파일")
        for r in pending:
            print(f"  - {r['path']}")
    return 0


def cmd_diff(root: Path, lang: str, target: str) -> int:
    p = Path(target)
    if not p.is_absolute():
        p = root / p
    h = read_header(p)
    if "source" not in h:
        print("i18n 헤더가 없습니다.")
        return 1
    sha = h.get("source-sha", "")
    print(f"원문 {h['source']} · 기록 시점 {sha} → HEAD")
    log = git(["log", "--oneline", f"{sha}..HEAD", "--", h["source"]], root)
    print("\n[커밋]" if log else "\n[커밋] 변경 없음")
    if log:
        print(log)
        diff = git(["diff", f"{sha}..HEAD", "--", h["source"]], root)
        print("\n[변경 내용]")
        print(diff[:8000] if diff else "(diff 없음)")
    return 0


def cmd_stamp(root: Path, lang: str, target: str, keep_status: bool, status: str) -> int:
    p = Path(target)
    if not p.is_absolute():
        p = root / p
    text = p.read_text(encoding="utf-8")
    sha = git(["rev-parse", "--short=7", "HEAD"], root)
    text = re.sub(r"(<!-- i18n-source-sha: ).*?( -->)", rf"\g<1>{sha}\g<2>", text, count=1)
    text = re.sub(r"(<!-- i18n-date: ).*?( -->)", rf"\g<1>{date.today().isoformat()}\g<2>", text, count=1)
    if not keep_status:
        text = re.sub(r"(<!-- i18n-status: ).*?( -->)", rf"\g<1>{status}\g<2>", text, count=1)
    p.write_text(text, encoding="utf-8")
    print(f"{p.relative_to(root)} → sha {sha}, status {status if not keep_status else '유지'}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=None)
    ap.add_argument("--lang", default="ko")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("status", help="진행률·드리프트 요약")
    s.add_argument("--verbose", "-v", action="store_true")
    s.add_argument("--json", action="store_true")

    d = sub.add_parser("diff", help="해당 번역본의 원문 변경 구간 보기")
    d.add_argument("path")

    t = sub.add_parser("stamp", help="번역 완료 표시(sha·날짜 갱신)")
    t.add_argument("path")
    t.add_argument("--keep-status", action="store_true")
    t.add_argument("--status", default="translated", choices=["translated", "source-copy"])

    args = ap.parse_args()
    root = (args.root or repo_root()).resolve()

    if args.cmd == "status":
        return cmd_status(root, args.lang, args.verbose, args.json)
    if args.cmd == "diff":
        return cmd_diff(root, args.lang, args.path)
    if args.cmd == "stamp":
        return cmd_stamp(root, args.lang, args.path, args.keep_status, args.status)
    return 1


if __name__ == "__main__":
    sys.exit(main())
