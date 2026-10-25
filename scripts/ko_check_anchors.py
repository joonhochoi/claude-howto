#!/usr/bin/env python3
"""ko/ 문서의 교차 파일 앵커가 실제 제목과 맞는지 검사한다.

`ko/` 번역본은 제목을 번역하므로, 영어 앵커(`#available-managed-settings`)를
그대로 둔 링크는 렌더 후 페이지 내에서 이동하지 않는다.
`check_links.py`/`check_cross_references.py`는 앵커까지 보지 않으므로 별도 검사가 필요하다.

사용:
    python3 scripts/ko_check_anchors.py            # 불일치 목록 출력
    python3 scripts/ko_check_anchors.py --fix      # 가능한 경우 슬러그 치환 제안만(자동 수정 안 함)
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

KO = Path(__file__).resolve().parent.parent / "ko"
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"^(```|~~~)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")


def github_slug(text: str) -> str:
    """GitHub heading 앵커 규칙(근사): 소문자·공백→하이픈·구두점 제거·한글 유지."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_~]", "", text)
    out = []
    for ch in text.lower():
        if ch.isalnum() or ch in "-_":
            out.append(ch)
        elif ch.isspace():
            out.append("-")
        elif unicodedata.category(ch).startswith("L"):
            out.append(ch)
        # 그 외 구두점은 버린다
    slug = "".join(out)
    return slug


def anchors_of(path: Path) -> set[str]:
    seen: dict[str, int] = {}
    inside = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if FENCE_RE.match(line.lstrip()):
            inside = not inside
            continue
        if inside:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        base = github_slug(m.group(2))
        n = seen.get(base, 0)
        seen[base] = n + 1
        yield_name = base if n == 0 else f"{base}-{n}"
        yield yield_name


def collect(path: Path) -> set[str]:
    return set(anchors_of(path))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    cache: dict[Path, set[str]] = {}
    problems: list[tuple[Path, int, str, str]] = []
    checked = 0

    for md in sorted(KO.rglob("*.md")):
        text = md.read_text(encoding="utf-8", errors="replace")
        inside = False
        for lineno, line in enumerate(text.splitlines(), 1):
            if FENCE_RE.match(line.lstrip()):
                inside = not inside
                continue
            if inside:
                continue
            for raw in LINK_RE.findall(line):
                if not raw.startswith("../") or "#" not in raw:
                    continue
                target, _, anchor = raw.partition("#")
                if not anchor:
                    continue
                dst = (md.parent / target).resolve()
                checked += 1
                if not dst.is_file():
                    continue  # 경로 자체는 다른 검사기가 잡는다
                if dst not in cache:
                    cache[dst] = collect(dst)
                if anchor not in cache[dst]:
                    problems.append((md, lineno, raw, dst.name))

    print(f"교차 파일 앵커 검사 {checked}건 · 불일치 {len(problems)}건")
    for md, lineno, raw, name in problems:
        print(f"  {md.relative_to(KO.parent)}:{lineno}  {raw}  (대상 {name})")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
