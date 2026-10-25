<!-- i18n-source: CLAUDE.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

# CLAUDE.md

튜토리얼 저장소입니다. 산출물은 `01-`부터 `10-`까지 번호가 붙은 모듈에 담긴 마크다운이며, 앱이 아닙니다. `scripts/`의 스크립트는 문서 검증과 EPUB 빌드만을 위해 존재합니다.

스택과 명령은 `.claude/CLAUDE.md`를, 레슨 구조는 `STYLE_GUIDE.md`를 참고하세요.

## 핵심 명령

```bash
# Quality gate (also runs on commit via pre-commit hooks)
pre-commit run --all-files

# Tests
pytest scripts/tests/ -v

# EPUB build (renders Mermaid with Pele — needs Node.js >= 20; the pinned bundle downloads once, then works offline)
uv run scripts/build_epub.py

# Python tooling
ruff check scripts/ && ruff format scripts/
mypy scripts/ --ignore-missing-imports
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/
```

pre-commit은 `.md` 변경 시 5가지 문서 검사를 실행합니다: markdown-lint, cross-references, mermaid-syntax, link-check, markdown-rendering. 모두 통과해야 합니다. EPUB 빌드는 pre-commit 훅이 **아니며** CI에서만 실행됩니다(`.github/workflows/test.yml`의 `build-epub` 잡). 전체 책을 빌드하는 느린 작업이기 때문이며, mermaid-syntax 훅이 이미 같은 Pele 번들로 모든 다이어그램을 렌더링합니다.

## 아키텍처 지도

- `01-` … `10-` — 튜토리얼 모듈. **번호 접두사 = 학습 순서**이며 알파벳 순이 아닙니다. 재구성하지 마세요.
- 각 모듈: `README.md` + 복사해 쓰는 템플릿(`.md`, `.json`, `.sh`).
- `scripts/` — 유틸리티(EPUB 빌더, 링크/mermaid/상호 참조 검증기). 제품이 아닙니다.
- `02-memory/*.md` — 사용자가 자기 프로젝트로 복사해 가는 CLAUDE.md 템플릿. 이 파일과 혼동하지 마세요.
- `openspec/` — 명세 기반 변경 제안.

## 하드 룰

- **사용자의 명시적 요청 없이는 커밋하거나 푸시해서는 안 됩니다.**
- **어떤 커밋 메시지에도 `Co-Authored-By: Claude`를 추가해서는 안 됩니다.**
- Python 스크립트를 실행하기 전에 항상 `.venv`를 활성화하세요(`venv/`, `.venv/`, `env/` 확인).
- 내부 링크는 **상대 경로**를 사용하고(예: `01-slash-commands/README.md`), 앵커는 `#heading-name` 형식을 사용합니다.
- 코드 펜스는 **반드시** 언어를 명시해야 합니다(`bash`, `python`, `json`, …). 그렇지 않으면 상호 참조 검사가 실패합니다.
- 외부 URL은 접근 가능하고 안정적이어야 합니다. 일시적인 링크는 안 됩니다.
- Mermaid 다이어그램은 Pele로 렌더링되어야 합니다. pre-commit mermaid 훅은 pre-commit이 제공하는 Node.js 22를 사용하고 엄격 모드로 실행되므로, 건너뛰지 않고 실패합니다. 첫 실행에는 Node.js와 고정된 Pele 번들을 내려받기 위한 네트워크가 필요합니다(오프라인: `SKIP=mermaid,vietnamese-mermaid,japanese-mermaid`). 직접 실행하는 `scripts/check_mermaid.py`는 Node.js >= 20이 없으면 경고만 하고, `--strict` 또는 CI에서는 실패합니다. EPUB 빌드가 깨지는 원인은 대개 잘못된 Mermaid, Node.js >= 20 부재, 번들 다운로드 실패입니다.
- 커밋 형식: `type(scope): subject`이며, `scope`는 모듈 폴더와 일치합니다(예: `feat(slash-commands):`, `docs(memory):`, `fix(README):`).
- `01-`–`10-` 번호를 재구성하지 마세요. 그 순서가 곧 커리큘럼입니다.

## 워크플로 선호

- 레슨을 편집할 때는 구조/명명/다이어그램에 대해 `STYLE_GUIDE.md`를 따르세요.
- 작은 수정 → 최소 diff. 오타 하나 고치려고 섹션을 다시 쓰지 마세요.
- 모듈 페이지를 추가할 때: README + 템플릿을 먼저 만들고, 그다음 루트 `README.md` 색인과 (순서나 일정이 바뀌면) `LEARNING-ROADMAP.md`를 갱신하세요.
- 튜토리얼 > 라이브러리: 재사용 가능한 추상화보다 명확한 설명과 복사해 쓰는 예제를 우선하세요.
- 품질 검사가 실패하면 근본 원인을 고치세요. `--no-verify`로 우회하지 마세요.

## 토큰 효율
- 방금 쓰거나 편집한 파일을 다시 읽지 마세요. 내용을 이미 알고 있습니다.
- 결과가 불확실하지 않았다면 "검증"을 위해 명령을 다시 실행하지 마세요.
- 요청받지 않았다면 코드나 파일 내용을 크게 되풀이해 출력하지 마세요.
- 관련된 편집은 하나의 작업으로 묶으세요. 1번으로 될 일을 5번 하지 마세요.
- "계속하겠습니다..." 같은 확인은 생략하세요. 그냥 하세요.
- 작업에 도구 호출 1번이면 충분하다면 3번 쓰지 마세요. 행동 전에 계획하세요.
- 결과가 모호하거나 추가 입력이 필요하지 않다면 방금 한 일을 요약하지 마세요.
