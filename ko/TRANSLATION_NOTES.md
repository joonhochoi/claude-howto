# 한국어 번역 용어집 · 스타일 가이드

> **중요:** 이 문서는 `claude-howto`를 한국어로 옮길 때의 규칙을 정한다. 작업 전에 반드시 읽는다.
> 원문(영어) 트리가 단일 진실 원천(source of truth)이며, `ko/`는 그 번역본이다.

## 기본 방침

- **문체:** `~합니다`체(정중체). 단, 절차 나열·명령 설명은 `~하세요`로 통일. 경어 섞임 금지.
- **용어 정책:** Claude Code의 기능명은 업계 관행대로 외래어 표기(아래 용어집 고정). 그 외 일반 기술 용어는 국립국어원 외래어 표기법을 따른다.
- **코드 보존:** 펜스 안 코드·명령어·경로·JSON·YAML은 **100% 원문 유지**. 주석·docstring만 번역한다.
- **Mermaid 라벨:** 노드 라벨은 **영어 유지**(빌드 검증기·이미지 렌더 안정성). 설명 문장은 번역.
- **앵커 링크:** 제목을 번역하면 같은 페이지 내 `#앵커`도 **번역된 제목 기준으로 재작성**한다. 파일 간 링크는 상대경로 유지.
- **파일 머리 헤더:** 모든 번역 문서 상단에 아래 4줄을 둔다(템플릿 파일은 프론트매터가 1행이어야 하므로 제외).

```
<!-- i18n-source: <영어 원문 상대경로> -->
<!-- i18n-source-sha: <번역 시점 HEAD 7자리> -->
<!-- i18n-status: translated | source-copy -->
<!-- i18n-date: YYYY-MM-DD -->
```

## 번역하지 않는 것 (실행 자산)

| 대상 | 처리 | 이유 |
|------|------|------|
| `01-slash-commands/*.md` (프론트매터 있는 커맨드) | 원문 그대로 | 내용이 곧 모델 프롬프트. 번역하면 동작이 달라진다 |
| `03-skills/*/SKILL.md`, `04-subagents/*.md`, `07-plugins/**` | 원문 그대로 | 동일 |
| `*.json`(MCP 설정), `*.sh`(훅), `*.py` | 원문 그대로 | 실행 코드. 주석만 번역 허용 |
| `02-memory/*CLAUDE.md` | 원문 그대로 | 사용자가 복사해 쓰는 템플릿 |
| 이미지·PDF | 복사만 | 시각 자료 |

## 기술 용어집

| English | 한국어 | 비고 |
|---------|--------|------|
| slash command | 슬래시 커맨드 | Claude Code 기능명 |
| hook | 훅 | 기능명 |
| skill | 스킬 | 기능명 |
| subagent | 서브에이전트 | 기능명 |
| agent | 에이전트 | 일반 표기 |
| agent team | 에이전트 팀 | 실험 기능명 |
| memory | 메모리 | 기능명(기억 영역) |
| checkpoint | 체크포인트 | 세션 스냅샷 |
| plugin | 플러그인 | 일반 용어 |
| MCP (Model Context Protocol) | MCP | 프로토콜명은 그대로 |
| context window | 컨텍스트 창 | 기능 설명 맥락에서 |
| token | 토큰 | |
| prompt | 프롬프트 | |
| workflow | 워크플로 | |
| repository | 저장소(리포지터리) | 첫 등장만 병기 |
| pull request / PR | PR | |
| commit / branch / merge | 커밋 / 브랜치 / 병합 | |
| issue | 이슈 | |
| release | 릴리스 | |
| frontmatter | 프론트매터 | |
| template | 템플릿 | |
| boilerplate | 상용구 | |
| permission | 권한 | |
| sandbox | 샌드박스 | |
| plan mode | 플랜 모드 | 기능명 |
| auto mode | 오토 모드 | 기능명 |
| headless mode | 헤드리스 모드 | |
| output style | 출력 스타일 | |
| session | 세션 | |
| worktree | 워크트리 | |
| CLI / API / CI-CD | CLI / API / CI-CD | 그대로 |

## 고정 표기 (번역 금지)

`CLAUDE.md` · `.claude/` · `~/.claude/` · 파일 경로 · 명령어(`/clear`, `/compact`, `/model`, `/effort`, `claude -p` 등) · 환경변수(`CLAUDE_CODE_*`) · 모델명(`Opus`/`Sonnet`/`Haiku`) · 제품명(`Claude Code`, `Anthropic`, `GitHub`).

## 용어 일관성 검사

빌드 전에 아래를 확인한다.

```bash
python3 scripts/ko_sync.py status        # 번역 진행률·드리프트
python3 scripts/check_links.py           # 끊긴 링크(ko 포함 전체)
python3 scripts/check_cross_references.py
```

## 링크 규칙 (실측으로 확정)

`ko/`는 문서만 미러하고 `scripts/`, `.github/`, `LICENSE`, 다른 언어판(`ja/` 등)은 복제하지 않는다.
따라서 영어 원문의 `scripts/README.md` 같은 상대 링크는 ko/ 안에서 **깨진다**(`check_cross_references.py`가 잡아낸다).

- ko/ 안에 대상이 있으면 그대로 둔다.
- ko/에 없고 저장소 루트에 있으면 `../`를 붙여 원문 트리를 가리킨다 (`../scripts/README.md`, `../ja/README.md`, `../LICENSE`).
- 이 보정은 손으로 하지 말고 `python3 scripts/ko_fixlinks.py --write`로 일괄 적용한다(멱등).

## 도구

| 명령 | 용도 |
|------|------|
| `python3 scripts/ko_skeleton.py` | ko/에 누락된 파일만 원문에서 채운다(기존 번역은 보존) |
| `python3 scripts/ko_sync.py status [-v]` | 번역 진행률 + 원문 드리프트 목록 |
| `python3 scripts/ko_sync.py diff ko/<경로>.md` | 해당 파일 원문의 변경 커밋·diff 보기 |
| `python3 scripts/ko_sync.py stamp ko/<경로>.md` | 번역 완료 표시(sha·날짜 갱신) |
| `python3 scripts/ko_fixlinks.py --write` | 상대 링크를 ko 트리에 맞게 보정 |

검증 게이트(모두 통과해야 함):

```bash
./.venv/bin/python scripts/check_cross_references.py
./.venv/bin/python scripts/check_links.py
./.venv/bin/python scripts/check_markdown_rendering.py
./.venv/bin/python scripts/build_website.py --lang ko -o /tmp/site-ko
```

## 원문 갱신 추적

- `ko/`의 각 문서는 `i18n-source-sha`에 **번역 시점의 커밋**을 기록한다.
- 원문이 바뀌면 `python3 scripts/ko_sync.py status`가 `drift`로 표시하고, `python3 scripts/ko_sync.py diff <경로>`가 **해당 구간 diff**를 보여준다.
- 갱신 절차: diff 확인 → 해당 문단만 재번역 → `python3 scripts/ko_sync.py stamp <경로>`로 sha 갱신.
