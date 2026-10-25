#!/usr/bin/env python3
"""ko/ 번역 트리 골격 생성기 (멱등).

영어 원문 트리를 ko/ 아래로 미러한다.
- 문서 md(프론트매터 없음): 머리에 i18n 헤더 주석을 붙여 복사 (status=source-copy)
- 템플릿 md(프론트매터 있음): 프론트매터가 첫 줄이어야 하므로 **헤더 없이 원문 그대로** 복사
- 이미지·코드 자산(.png/.svg/.json/.sh/.py): 원문 그대로 복사

이미 ko/에 있는 파일은 건드리지 않는다(번역 내용 보존).

사용:
    python3 scripts/ko_skeleton.py            # 누락분만 채움
    python3 scripts/ko_skeleton.py --dry-run
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

# ko/ 로 복제하지 않는 최상위 경로 (다른 언어판·메타)
EXCLUDE_TOP = {
    "ja", "uk", "vi", "zh", "ko",  # 다른 언어판
    ".git", "site", "site-ko",
    ".claude", ".github",
    "scripts", "slides", "assets", "local-progress",  # 레포 유지보수·발표자료·빌드 자산 (본문 아님)
    ".venv", "venv", "node_modules", "__pycache__",  # 로컬 환경·빌드 캐시
}
# 자산 확장자 (원문 그대로 복사)
ASSET_EXT = {".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp", ".pdf", ".json", ".sh", ".py"}


def head_sha(repo: Path) -> str:
    out = subprocess.run(
        ["git", "rev-parse", "--short=7", "HEAD"], cwd=repo, capture_output=True, text=True, check=True
    )
    return out.stdout.strip()


def has_frontmatter(path: Path) -> bool:
    try:
        return path.read_text(encoding="utf-8", errors="ignore").lstrip().startswith("---")
    except OSError:
        return False


def header(src_rel: str, sha: str, today: str) -> str:
    return (
        f"<!-- i18n-source: {src_rel} -->\n"
        f"<!-- i18n-source-sha: {sha} -->\n"
        f"<!-- i18n-status: source-copy -->\n"
        f"<!-- i18n-date: {today} -->\n\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    ap.add_argument("--lang", default="ko")
    ap.add_argument("--date", default=None, help="i18n-date 값 (기본: 오늘)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="ko/ 기존 파일도 덮어쓴다(위험)")
    args = ap.parse_args()

    root: Path = args.root.resolve()
    ko = root / args.lang
    sha = head_sha(root)
    from datetime import date

    today = args.date or date.today().isoformat()

    created = skipped = 0
    for src in sorted(root.rglob("*")):
        if not src.is_file():
            continue
        rel = src.relative_to(root)
        if rel.parts[0] in EXCLUDE_TOP:
            continue
        if src.name.startswith("."):
            continue
        if src.suffix.lower() not in {".md"} | ASSET_EXT:
            continue
        dst = ko / rel
        if dst.exists() and not args.force:
            skipped += 1
            continue
        if args.dry_run:
            print(f"[dry] {rel}")
            created += 1
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix.lower() == ".md" and not has_frontmatter(src):
            body = src.read_text(encoding="utf-8", errors="ignore")
            dst.write_text(header(str(rel), sha, today) + body, encoding="utf-8")
        else:
            shutil.copy2(src, dst)
        created += 1

    print(f"{args.lang}/ 생성 {created}개 · 기존 유지 {skipped}개 · HEAD {sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
