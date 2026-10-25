#!/usr/bin/env python3
"""ko/ 마크다운의 상대 링크를 ko 트리에 맞게 보정한다.

`ko/`는 문서만 미러하고 `scripts/`, `.github/`, 다른 언어판(`ja/` 등)은 복제하지 않는다.
영어 원문에서 `scripts/README.md` 같은 상대 링크는 ko/ 안에서 깨지므로,
대상 파일이 ko/에 없고 저장소 루트에는 있으면 `../`를 붙여 원문 트리를 가리키게 한다.

사용:
    python3 scripts/ko_fixlinks.py            # 검사만 (--dry-run 기본)
    python3 scripts/ko_fixlinks.py --write    # 실제 수정
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# [text](target) 및 ![alt](target) 형태를 잡는다. URL 스킴·앵커·메일은 건드리지 않는다.
LINK_RE = re.compile(r"(\]\(|<img [^>]*src=\")([^)\"\s]+)")


def should_skip(target: str) -> bool:
    return (
        not target
        or target.startswith(("http://", "https://", "mailto:", "#", "//"))
        or target.startswith("../")
        or target.startswith("/")
    )


def split_target(target: str) -> tuple[str, str]:
    """경로와 (앵커/쿼리)를 분리한다."""
    for i, ch in enumerate(target):
        if ch in "#?":
            return target[:i], target[i:]
    return target, ""


def fix_file(md: Path, ko_root: Path, repo_root: Path, write: bool) -> list[tuple[str, str]]:
    text = md.read_text(encoding="utf-8")
    changes: list[tuple[str, str]] = []

    def repl(m: re.Match) -> str:
        prefix, target = m.group(1), m.group(2)
        if should_skip(target):
            return m.group(0)
        path, tail = split_target(target)
        if not path:
            return m.group(0)
        local = (md.parent / path)
        if local.exists():  # ko/ 안에 이미 있으면 그대로
            return m.group(0)
        rel_from_ko = (md.parent.relative_to(ko_root) / path)
        # ko 트리 기준 상대 경로를 루트 기준으로 환산
        depth = len(md.parent.relative_to(ko_root).parts)
        root_target = "../" * depth + str(rel_from_ko) if depth else str(rel_from_ko)
        if (repo_root / root_target).exists():
            new = "../" + target
            changes.append((target, new))
            return prefix + new
        return m.group(0)

    new_text = LINK_RE.sub(repl, text)
    if write and changes and new_text != text:
        md.write_text(new_text, encoding="utf-8")
    return changes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    ap.add_argument("--lang", default="ko")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    repo_root: Path = args.root.resolve()
    ko_root = repo_root / args.lang
    total = 0
    for md in sorted(ko_root.rglob("*.md")):
        changes = fix_file(md, ko_root, repo_root, args.write)
        if changes:
            total += len(changes)
            print(f"{md.relative_to(repo_root)}: {len(changes)}건")
            for a, b in changes[:10]:
                print(f"    {a}  →  {b}")
    mode = "수정" if args.write else "검사(dry-run)"
    print(f"\n{mode}: 대상 링크 {total}건")
    if not args.write and total:
        print("실제 반영은 --write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
