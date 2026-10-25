<!-- i18n-source: CATALOG.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 기능 카탈로그

> 모든 Claude Code 기능을 한눈에 보는 빠른 참조 가이드: 커맨드, 에이전트, 스킬, 플러그인, 훅.

**탐색**: [커맨드](#슬래시-커맨드) | [권한 모드](#권한-모드) | [서브에이전트](#서브에이전트) | [스킬](#스킬) | [플러그인](#플러그인) | [MCP 서버](#mcp-서버) | [훅](#훅) | [메모리](#메모리-파일) | [새 기능](#새-기능)

---

## 요약

| 기능 | 내장 | 예시 | 합계 | 참조 |
|---------|----------|----------|-------|-----------|
| **슬래시 커맨드** | 60+ | 8 | 68+ | [01-slash-commands/](01-slash-commands/) |
| **서브에이전트** | 6 | 9 | 15 | [04-subagents/](04-subagents/) |
| **스킬** | 번들 20개 | 6 | 26 | [03-skills/](03-skills/) |
| **플러그인** | - | 3 | 3 | [07-plugins/](07-plugins/) |
| **MCP 서버** | - | 4 | 4 | [05-mcp/](05-mcp/) |
| **훅** | 이벤트 33개 | 11 | 44 | [06-hooks/](06-hooks/) |
| **메모리** | 유형 7개 | 3 | 10 | [02-memory/](02-memory/) |
| **합계** | **126** | **44** | **170** | |

---

## 슬래시 커맨드

커맨드는 사용자가 직접 호출하는 단축키로, 특정 작업을 실행합니다.

### 내장 커맨드

| 커맨드 | 설명 | 사용 시점 |
|---------|-------------|-------------|
| `/help` | 도움말 정보 표시 | 시작하기, 커맨드 익히기 |
| `/btw` | 일회성 곁가지 질문 — 메인 컨텍스트를 오염시키지 않습니다 | 빠른 곁가지 질문 |
| `/chrome` | Chrome 통합 구성 | 브라우저 자동화 |
| `/clear` | 대화 기록 지우기 | 새로 시작, 컨텍스트 줄이기 |
| `/diff` | 대화형 diff 뷰어. 전체 화면 TUI(v2.1.260+)에서는 대화 옆에 diff 패널이 열리고, 그 패널은 계속 열린 채로 Claude가 파일을 편집하거나 명령을 실행할 때마다 새로 고쳐집니다. 클래식 렌더러에서는 프롬프트 자리에 뷰어를 엽니다 | 변경 사항 검토 |
| `/config` | 구성 조회·편집 | 동작 사용자 정의 |
| `/status` | 세션 상태 표시 | 현재 상태 확인 |
| `/agents` | 제거됨: 마법사는 v2.1.198에, 커맨드는 v2.1.281에 `/` 메뉴와 `/help`에서 빠졌습니다 — Claude에게 서브에이전트 생성을 요청하거나 `.claude/agents/`를 직접 편집하세요 | Claude에게 요청해 서브에이전트 관리 |
| `/skills` | 사용 가능한 스킬 나열 | 자동 호출 기능 확인 |
| `/hooks` | 구성된 훅 나열 | 자동화 디버깅 |
| `/insights` | 세션 패턴 분석 | 세션 최적화 |
| `/install-slack-app` | Claude Slack 앱 설치 | Slack 통합 |
| `/keybindings` | 키보드 단축키 사용자 정의 | 키 사용자 정의 |
| `/mcp` | MCP 서버 나열 | 외부 통합 확인 |
| `/memory` | 로드된 메모리 파일 보기 | 컨텍스트 로딩 디버깅 |
| `/mobile` | 모바일 QR 코드 생성 | 모바일 접근 |
| `/passes` | 친구에게 Claude Code 1주일 무료 이용권 공유(자격 있는 계정만) | 추천 |
| `/plugin` | 플러그인 관리 | 확장 설치·제거 |
| `/plan` | 플랜 모드 진입 | 복잡한 구현 |
| `/proactive` | `/loop`의 별칭 (v2.1.105) | `/loop`와 동일 |
| `/recap` | 세션으로 돌아올 때 세션 요약 표시 | 자리를 비운 뒤 무엇을 했는지 파악 |
| `/rewind` | 체크포인트로 되감기 | 변경 취소, 대안 탐색 |
| `/checkpoint` | `/rewind`의 별칭 | `/rewind`와 동일 |
| `/cost` | `/usage`의 비용 탭을 여는 단축 별칭 (v2.1.118+) | 지출 모니터링 |
| `/context` | 컨텍스트 창 사용량 표시 | 대화 길이 관리 |
| `/export` | 대화 내보내기 | 참고용으로 저장 |
| `/usage-credits` | 추가 사용 한도 구성 (v2.1.144에서 `/extra-usage`에서 이름이 바뀌었고, 이전 이름도 별칭으로 동작) | 속도 제한 관리 |
| `/feedback` | 피드백 또는 버그 리포트 제출 | 문제 보고 |
| `/login` | Anthropic 인증 | 기능 접근 |
| `/logout` | 로그아웃 | 계정 전환 |
| `/sandbox` | 샌드박스 모드 전환 | 안전한 명령 실행 |
| `/doctor` | 진단 실행 | 문제 해결 |
| `/reload-plugins` | 설치된 플러그인 다시 로드. v2.1.221부터 대부분의 설치가 즉시 활성화되므로 설치 요약에 `Run /reload-plugins to activate.`가 나올 때만 필요합니다. v2.1.260+부터 헤드리스 세션에서도 사용할 수 있어 Claude Code Desktop과 SDK 커맨드 목록에 나타납니다 | 플러그인 관리 |
| `/reload-skills` | 재시작 없이 스킬 디렉터리 다시 스캔 (v2.1.152) | 스킬 관리 |
| `/workflows` | 실행 중·완료된 동적 워크플로 실행 보기 (v2.1.154) | 멀티 에이전트 오케스트레이션 |
| `/release-notes` | 릴리스 노트 표시 | 새 기능 확인 |
| `/remote-control` | 원격 제어 활성화 | 원격 접근 |
| `/permissions` | 권한 관리 | 접근 제어 |
| `/rename` | 현재 세션 이름 변경 | 세션 정리 |
| `/resume` | 이전 세션 재개 | 작업 이어가기 |
| `/tui [default\|fullscreen]` | 터미널 UI 렌더러 설정 (`fullscreen` = 깜빡임 없는 대체 화면). 인자 없이 `/tui`만 쓰면 현재 활성 렌더러를 출력합니다 | 전체 화면·tmux에서 깜빡임 없는 렌더링 |
| `/tasks` | 백그라운드 작업 보기 | 비동기 작업 모니터링 |
| `/copy` | 마지막 응답을 클립보드로 복사 | 출력을 빠르게 공유 |
| `/teleport` (별칭 `/tp`) | 웹의 Claude Code 세션을 이 터미널에서 재개합니다. 선택기가 열립니다. claude.ai 구독 필요 | 원격에서 작업 이어가기 |
| `/desktop` | Claude Desktop 앱 열기 | 데스크톱 인터페이스로 전환 |
| `/theme` | 색상 테마 변경. v2.1.118에서 `~/.claude/themes/<name>.json`을 통한 사용자 지정 이름 테마가 추가되었습니다(플러그인은 `themes/` 디렉터리를 함께 배포할 수 있음) | 모양 사용자 정의 |
| `/usage` | 사용량·비용·통계의 표준 커맨드 — `/cost`와 `/stats`를 하나의 탭 뷰로 병합했습니다(v2.1.118). v2.1.149부터 비용 뷰는 지출을 범주별(스킬, 서브에이전트, 플러그인, MCP 서버별)로 나눕니다. **VSCode 확장**(v2.1.174)의 `/usage`(Account & usage) 대화상자는 24시간·7일 창에 대한 귀속 분석 — 캐시 미스, 장문 컨텍스트 비용, 서브에이전트, 스킬별·에이전트별·플러그인별·MCP별 사용량 — 을 추가로 보여줍니다 | 할당량·비용 모니터링 |
| `/focus` | 포커스 뷰 전환(방해 요소 없는 출력 표시) | 긴 작업 중 시각적 잡음 줄이기 |
| `/fork` | 대화를 새 독립 백그라운드 세션으로 복사 (v2.1.212+) | 대안을 병렬로 탐색 |
| `/subtask` | 대화를 상속하고 결과를 보고하는 포크 서브에이전트 생성 (v2.1.212+) | 하던 작업을 잃지 않고 곁가지 작업 위임 |
| `/stats` | `/usage`의 통계 탭을 여는 단축 별칭 (v2.1.118+) | 세션 지표 검토 |
| `/statusline` | 상태 표시줄 구성 | 상태 표시 사용자 정의 |
| `/stickers` | Claude Code 스티커 주문 | 재미 보상 |
| `/fast` | 빠른 출력 모드 전환. **Opus 5.5**(v2.1.280 이후 기본), **Opus 5, Opus 4.8**에 적용됩니다 | 응답 속도 높이기 |
| `/terminal-setup` | 터미널 통합 구성 | 터미널 기능 설정 |
| `/undo` | `/rewind`의 별칭 (v2.1.108) | `/rewind`와 동일 |
| `/upgrade` | 상위 플랜으로 전환하는 업그레이드 페이지 열기 | 플랜 업그레이드 |
| `/team-onboarding` | 이 프로젝트의 Claude Code 사용 기록에서 팀원 온보딩 가이드 생성 | 새 팀원 온보딩 (v2.1.101) |
| `/code-review ultra` | 현재 변경 사항에 대해 클라우드 멀티 에이전트 코드 리뷰 실행. `/ultrareview`도 별칭으로 남아 있지만 `/code-review ultra`가 권장 호출 방식입니다. Pro·Max에서 3회 무료 실행 후 사용 크레딧이 필요합니다 | 여러 에이전트로 병합 전 심층 리뷰 (v2.1.112) |
| `/fewer-permission-prompts` | 트랜스크립트를 스캔해 흔한 읽기 전용 도구에 대한 우선순위 허용 목록 제안 | 프로젝트에서 반복되는 권한 프롬프트 줄이기 (v2.1.112) |
| `/skill-doctor` | 로드된 스킬 중 사용되지 않는 것과 그것이 컨텍스트에서 차지하는 비용 표시. `/plugin` 관리자의 **Stats** 탭에서 열리며 `-p`에서는 텍스트로 출력됩니다 | 더 이상 필요 없는 스킬 정리 (v2.1.252+) |

### 사용자 정의 커맨드 (예시)

| 커맨드 | 설명 | 사용 시점 | 범위 | 설치 |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | 최적화 관점에서 코드 분석 | 성능 개선 | Project | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | 풀 리퀘스트 준비 | PR 제출 전 | Project | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | API 문서 생성 | API 문서화 | Project | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | 컨텍스트를 담은 git 커밋 생성 | 변경 사항 커밋 | User | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | 스테이징·커밋·푸시 | 빠른 배포 | User | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | 문서 구조 개편 | 문서 개선 | Project | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | CI/CD 파이프라인 설정 | 신규 프로젝트 | Project | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | 테스트 커버리지 확장 | 테스트 개선 | Project | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **범위**: `User` = 개인 워크플로(`~/.claude/commands/`), `Project` = 팀 공유(`.claude/commands/`)

**참조**: [01-slash-commands/](01-slash-commands/) | [공식 문서](https://code.claude.com/docs/en/interactive-mode)

**빠른 설치 (모든 사용자 정의 커맨드)**:
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## 권한 모드

Claude Code는 도구 사용이 어떻게 승인되는지 제어하는 6가지 권한 모드를 지원합니다.

| 모드 | 설명 | 사용 시점 |
|------|-------------|-------------|
| `manual` | 도구 호출마다 프롬프트 표시 | 모든 작업을 직접 검토할 때 (v2.1.200부터 Manual로 표시되며, 구성 값은 여전히 `default`이고 `manual`은 별칭입니다). v2.1.283부터 대화형 터미널·VS Code 세션의 내장 시작 모드는 auto입니다 |
| `acceptEdits` | 파일 편집은 자동 수락하고 나머지는 프롬프트 표시 | 신뢰하는 편집 워크플로 |
| `plan` | 조사 후 계획을 제안하고, 승인 전에는 소스 편집 없음 | 계획 수립과 탐색 |
| `auto` | 모든 작업 허용, 백그라운드 안전 분류기 검사 포함 | 긴 작업, 프롬프트 피로 줄이기 |
| `bypassPermissions` | 모든 권한 검사 건너뛰기 | CI/CD, 헤드리스 환경 |
| `dontAsk` | 권한이 필요한 도구를 건너뛰기 | 비대화형 스크립팅 |

> **참고**: `auto` 모드는 자격을 갖춘 플랜·모델·제공자가 필요합니다 — [09-advanced-features/](09-advanced-features/#오토-모드)를 참조하세요. `bypassPermissions`는 신뢰할 수 있는 샌드박스 환경에서만 사용하세요.

**참조**: [공식 문서](https://code.claude.com/docs/en/permissions)

---

## 서브에이전트

특정 작업을 위해 격리된 컨텍스트를 갖는 전문화된 AI 어시스턴트입니다.

> **중첩 생성은 기본 활성, 깊이 3 (v2.1.219)**: 서브에이전트는 메인 대화 아래 최대 3계층까지 자신의 서브에이전트를 생성할 수 있습니다. 한도를 바꾸려면 `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`를 설정하고, 중첩을 끄려면 `1`로 설정하세요. (이력: v2.1.172–v2.1.216은 변경 수단 없이 최대 5계층까지 기본 중첩이었고, v2.1.217은 중첩을 깊이 1의 옵트인으로 바꿨으며, v2.1.219가 기본값을 3으로 정했습니다.) 특정 서브에이전트가 생성할 수 있는 서브에이전트를 제한하는 `Agent(agent_type)` 문법은 [04-subagents/README.md](04-subagents/README.md#생성-가능한-서브에이전트-제한)를 참조하세요.

### 내장 서브에이전트

| 에이전트 | 설명 | 도구 | 모델 | 사용 시점 |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | 다단계 작업, 조사 | 모든 도구 | 모델 상속 | 복잡한 조사, 다중 파일 작업 |
| **Plan** | 구현 계획 수립 | Read, Glob, Grep, Bash | 모델 상속 | 아키텍처 설계, 계획 수립 |
| **Explore** | 코드베이스 탐색 | Read, Glob, Grep | 상속(Opus로 상한) | 빠른 검색, 코드 이해 |
| **claude** | 더 전문화된 에이전트에 맞지 않는 작업의 포괄 담당 | 모든 도구 | 모델 상속 | 전용 에이전트가 없는 작업, 디스패치된 백그라운드 세션의 기본 에이전트 |
| **statusline-setup** | 상태 표시줄 구성 | Bash, Read, Write | Sonnet | 상태 표시줄 표시 구성 |
| **claude-code-guide** | 도움말과 문서 | Read, Glob, Grep | Haiku | 도움받기, 기능 학습 |

### 서브에이전트 구성 필드

| 필드 | 유형 | 설명 |
|-------|------|-------------|
| `name` | string | 에이전트 식별자 |
| `description` | string | 에이전트가 하는 일 |
| `model` | string | 모델 재정의 (`sonnet`, `opus`, `haiku`, `fable`, 전체 모델 ID, 또는 `inherit`) |
| `tools` | array | 허용 도구 목록 |
| `effort` | string | 노력 수준 (`low`, `medium`, `high`, `xhigh`, `max`, 모델에 따라 다름) |
| `initialPrompt` | string | 에이전트가 메인 세션 에이전트(`--agent`)로 실행될 때 자동 제출되는 첫 사용자 턴 |
| `disallowedTools` | array | 이 에이전트에서 명시적으로 거부되는 도구 |

### 사용자 정의 서브에이전트 (예시)

| 에이전트 | 설명 | 사용 시점 | 범위 | 설치 |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | 포괄적인 코드 품질 검토 | 코드 리뷰 세션 | Project | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `clean-code-reviewer` | 클린 코드 원칙 검토 | 유지보수성 검토 | Project | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | 테스트 전략과 커버리지 | 테스트 계획 | Project | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | 기술 문서 작성 | API 문서, 가이드 | Project | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | 보안 중심 검토 | 보안 감사 | Project | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | 기능 전체 구현 | 기능 개발 | Project | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | 근본 원인 분석 | 버그 조사 | User | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL 쿼리, 데이터 분석 | 데이터 작업 | User | `cp 04-subagents/data-scientist.md .claude/agents/` |
| `performance-optimizer` | 프로파일링과 성능 튜닝 | 병목 조사 | Project | `cp 04-subagents/performance-optimizer.md .claude/agents/` |

> **범위**: `User` = 개인(`~/.claude/agents/`), `Project` = 팀 공유(`.claude/agents/`)

**참조**: [04-subagents/](04-subagents/) | [공식 문서](https://code.claude.com/docs/en/sub-agents)

**빠른 설치 (모든 사용자 정의 에이전트)**:
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## 스킬

지침, 스크립트, 템플릿을 갖춘 자동 호출 기능입니다.

### 예시 스킬

| 스킬 | 설명 | 자동 호출 시점 | 범위 | 설치 |
|-------|-------------|-------------------|-------|--------------|
| `code-review-specialist` | 포괄적인 코드 리뷰 | "Review this code", "Check quality" | Project | `cp -r 03-skills/code-review-specialist .claude/skills/` |
| `brand-voice` | 브랜드 일관성 검사기 | 마케팅 문구 작성 | Project | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | API 문서 생성기 | "Generate docs", "Document API" | Project | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | 체계적인 코드 리팩터링 (Martin Fowler) | "Refactor this", "Clean up code" | User | `cp -r 03-skills/refactor ~/.claude/skills/` |
| `claude-md` | CLAUDE.md 파일 생성·갱신 | "Create CLAUDE.md", "Audit CLAUDE.md" | Project | `cp -r 03-skills/claude-md .claude/skills/` |
| `blog-draft` | 아이디어와 자료로 블로그 글 초안 작성 | "Write a blog post", "Draft an article" | User | `cp -r 03-skills/blog-draft ~/.claude/skills/` |

> **범위**: `User` = 개인(`~/.claude/skills/`), `Project` = 팀 공유(`.claude/skills/`)

### 스킬 구조

```
~/.claude/skills/skill-name/
├── SKILL.md          # Skill definition & instructions
├── scripts/          # Helper scripts
└── templates/        # Output templates
```

### 스킬 프론트매터 필드

스킬은 구성에 `SKILL.md`의 YAML 프론트매터를 지원합니다.

| 필드 | 유형 | 설명 |
|-------|------|-------------|
| `name` | string | 스킬 표시 이름 |
| `description` | string | 스킬이 하는 일 |
| `when_to_use` | string | `description` 뒤에 덧붙는 트리거 문구나 예시 요청 |
| `effort` | string | 노력 수준 (`low`, `medium`, `high`, `xhigh`, `max`, 모델에 따라 다름) |
| `shell` | string | 인라인 `` !`command` `` 블록에 쓸 셸 (`bash` 기본, 또는 `powershell`) |

**참조**: [03-skills/](03-skills/) | [공식 문서](https://code.claude.com/docs/en/skills)

**빠른 설치 (모든 스킬)**:
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### 번들 스킬

| 스킬 | 설명 | 자동 호출 시점 |
|-------|-------------|-------------------|
| `/artifact-capabilities` | 게시된 아티팩트가 사용할 수 있는 런타임 기능(커넥터, 파일 다운로드)에 대한 레퍼런스를 로드 | 해당 기능을 쓰는 아티팩트 페이지를 만들기 전 |
| `/artifact-diagramming` *(v2.1.221+)* | 아티팩트용 다이어그램 지침 로드: 다이어그램이 도움이 되는 때, 무엇을 그릴지, 밝은·어두운 테마 모두에서 읽히는 인라인 SVG | 아티팩트에 다이어그램을 그릴 때 |
| `/batch` | 큰 변경을 5~30개의 독립 단위로 나누고 각 단위를 자체 워크트리의 백그라운드 서브에이전트가 실행 | 대규모 병렬 리팩터링 |
| `/claude-api` | Claude API로 앱 구축 | API 개발 |
| `/claude-in-chrome [task]` | Claude in Chrome을 통해 브라우저에서 작업 수행(페이지 테스트, 폼 작성, 콘솔 로그 읽기). Chrome 통합이 활성화되어 있을 때 사용 가능 | 브라우저 작업 |
| `/dataviz [request]` | 차트·그래프·대시보드 설계 지침: 차트 형식, 역할별 색상, 색각 안전성과 대비를 위한 팔레트 검증 | 차트나 대시보드 제작 |
| `/debug [description]` | 세션의 디버그 로깅을 켜고 세션 디버그 로그로 문제 해결 | Claude Code 자체 디버깅 |
| `/design` *(v2.1.265+)* | 다중 아트보드 디자인 캔버스 생성 — UI 목업, 화면 흐름, 랜딩 페이지, 포스터 — 를 코드 대신 시각적으로 다듬습니다. Pro/Max/Team/Enterprise | HTML보다 손으로 다듬고 싶은 화면이나 페이지 디자인 |
| `/design-sync [hint]` | 저장소의 React 디자인 시스템을 변환해 Claude Design에 업로드하여, 디자인이 실제 컴포넌트를 쓰도록 합니다. Anthropic API 전용. 독립 실행형 Claude Design(claude.ai/design)은 2026년 12월 14일 종료됩니다. | 디자인 시스템을 Claude Design에 동기화 |
| `/design-login` | `/design-sync`를 위한 디자인 시스템 접근 권한 부여 | `/design-sync` 실행 전 |
| `/doctor [prompt-audit [path]]` | 설치, 설정, 확장, `CLAUDE.md` 문제를 진단하고 수정안을 제안하는 설치 점검. 별칭: `/checkup` | 설정 문제 해결 |
| `/fewer-permission-prompts` | 트랜스크립트를 스캔해 우선순위 허용 목록 제안 | 반복 권한 프롬프트 줄이기 |
| `/loop` | 일정 간격으로 프롬프트 실행 | 반복 작업 |
| `/run` *(v2.1.145+)* | 이 프로젝트의 앱을 실행해 변경이 동작하는 모습 확인 | 실제 앱에서 변경 검증 |
| `/run-skill-generator` *(v2.1.145+)* | `/run`·`/verify`가 특정 프로젝트를 다루는 방법을 학습시킴 | `/run`의 최초 프로젝트 설정 |
| `/code-review [low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [pr#\|branch\|path]` | 현재 diff — 또는 PR, 브랜치, 경로 — 를 정확성 버그 관점에서 리뷰. `--fix`는 발견 사항을 적용하고, `--comment`는 PR 인라인 코멘트로 게시합니다. 수준을 생략하면 마지막으로 입력한 수준을 재사용합니다(v2.1.223). v2.1.218에서 낮은 노력 수준이 **백그라운드 서브에이전트**로 옮겨 갔고 v2.1.232에 `high`, `xhigh`, `max`가 뒤따라, 리뷰 출력이 더 이상 대화를 채우지 않습니다 | 코드 작성 후, PR 병합 전 |
| `/slides [brief]` *(v2.1.265+)* | 브리프로 Claude Slides 아티팩트 형식의 새 프레젠테이션 생성. 아티팩트와 Slides 템플릿이 필요합니다 | 슬라이드 덱 제작 |
| `/simplify` *(v2.1.154부터 다시 별개)* | 수정만 적용하는 정리 전용 리뷰(재사용/단순화/효율/추상 수준). 버그를 찾지는 않습니다 | 버그 사냥 없이 코드 정돈 |
| `/update-config [request]` | 설정 변경(명령 허용, 환경변수 지정, 훅 추가)을 설명하면 Claude가 해당 `settings.json`을 편집 | JSON을 직접 고치지 않고 설정 변경 |
| `/verify` *(v2.1.145+)* | 앱을 빌드·실행·관찰해 수정이 동작함을 확인 | 수정 사항을 처음부터 끝까지 검증 |
| `/workflow-authoring` *(v2.1.248+)* | 동적 워크플로 스크립트 작성용 레퍼런스(스크립트 API, 재개, 품질 패턴) 로드. 동적 워크플로가 활성화되어 있을 때 사용 가능 | 워크플로 스크립트 작성·편집 |

---

## 플러그인

커맨드, 에이전트, MCP 서버, 훅을 묶은 번들 모음입니다.

### 예시 플러그인

| 플러그인 | 설명 | 구성 요소 | 사용 시점 | 범위 | 설치 |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | PR 리뷰 워크플로 | 커맨드 3개, 에이전트 3개, GitHub MCP | 코드 리뷰 | Project | `claude --plugin-dir ./07-plugins/pr-review` |
| `devops-automation` | 배포와 모니터링 | 커맨드 4개, 에이전트 3개, K8s MCP | DevOps 작업 | Project | `/plugin install devops-automation` |
| `documentation` | 문서 생성 모음 | 커맨드 4개, 에이전트 3개, 템플릿 | 문서화 | Project | `/plugin install documentation` |

> **범위**: `Project` = 팀 공유, `User` = 개인 워크플로

### 플러그인 구조

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json   # Manifest file (the only file in .claude-plugin/)
├── commands/         # Slash commands
├── agents/           # Subagents
├── skills/           # Skills (<name>/SKILL.md)
├── hooks/
│   └── hooks.json    # Hook configuration
├── .mcp.json         # MCP configurations
├── bin/              # Executables
└── scripts/          # Utility scripts
```

**참조**: [07-plugins/](07-plugins/) | [공식 문서](https://code.claude.com/docs/en/plugins)

**플러그인 관리 커맨드**:
```bash
/plugin list              # List installed plugins
/plugin install <name>    # Install plugin
/plugin uninstall <name>  # Uninstall plugin
claude plugin update <name>   # Update a plugin (CLI; the /plugin update slash form is referenced in prose but not in the command reference)
```

---

## MCP 서버

외부 도구와 API 접근을 위한 Model Context Protocol 서버입니다.

### 일반적인 MCP 서버

| 서버 | 설명 | 사용 시점 | 범위 | 설치 |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | PR 관리, 이슈, 코드 | GitHub 워크플로 | Local | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | SQL 쿼리, 데이터 접근 | 데이터베이스 작업 | Local | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | 고급 파일 작업 | 복잡한 파일 작업 | Local | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | 팀 커뮤니케이션 | 알림, 업데이트 | Project | 설정에서 구성 |
| **Google Docs** | 문서 접근 | 문서 편집, 리뷰 | Project | 설정에서 구성 |
| **Asana** | 프로젝트 관리 | 작업 추적 | Project | 설정에서 구성 |
| **Stripe** | 결제 데이터 | 재무 분석 | Project | 설정에서 구성 |
| **Memory** | 영구 메모리 | 세션 간 회상 | User | 설정에서 구성 |
| **Context7** | 라이브러리 문서 | 최신 문서 조회 | User | 설정에서 구성(서드파티 서버) |

> **범위**: `Local` = `--scope` 없이 `claude mcp add`를 실행할 때의 기본값(본인만, 이 프로젝트만; `~/.claude.json`), `Project` = 팀(`.mcp.json`, `--scope project`), `User` = 개인(`~/.claude.json`, `--scope user`), `Built-in` = 사전 설치됨

### MCP 구성 예시

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**참조**: [05-mcp/](05-mcp/) | [MCP 프로토콜 문서](https://modelcontextprotocol.io)

**빠른 설치 (GitHub MCP)**:
```bash
export GITHUB_TOKEN="your_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## 훅

Claude Code 이벤트에 맞춰 셸 명령을 실행하는 이벤트 기반 자동화입니다.

### 훅 이벤트

| 이벤트 | 설명 | 트리거 시점 | 사용 사례 |
|-------|-------------|----------------|-----------|
| `SessionStart` | 세션 시작·재개 | 세션 초기화 | 준비 작업 |
| `Setup` | 저장소 설정 또는 유지보수 실행 | `--init-only`일 때만, 또는 `-p`와 함께 `--init`/`--maintenance`를 쓸 때 | 도구 프로비저닝, 의존성 설치 |
| `InstructionsLoaded` | 지침 로드됨 | CLAUDE.md 또는 규칙 파일 로드 | 사용자 지정 지침 처리 |
| `UserPromptSubmit` | 프롬프트 처리 전(그리고 v2.1.299부터 스킬이나 사용자 정의 커맨드가 확장되기 전) | 사용자가 메시지 전송 | 입력 검증 |
| `UserPromptExpansion` | 입력된 슬래시 커맨드(스킬, 사용자 정의 커맨드, MCP 프롬프트)가 프롬프트로 확장됨 | `UserPromptSubmit` 이후, 확장된 프롬프트가 Claude에 도달하기 전 | 직접 `/command` 사용 차단, 스킬별 컨텍스트 추가, 커맨드 로깅 |
| `PreToolUse` | 도구 실행 전 | 모든 도구 실행 직전 | 검증, 로깅 |
| `PermissionRequest` | 권한 대화상자 표시 | 민감한 작업 전 | 사용자 지정 승인 흐름 |
| `PermissionDenied` | 사용자가 권한 프롬프트를 거부 | 권한 거부 후 | 로깅, 분석, 정책 적용 |
| `PostToolUse` | 도구 성공 후 | 모든 도구 완료 후 | 포맷팅, 알림 |
| `PostToolUseFailure` | 도구 실행 실패 | 도구 오류 후 | 오류 처리, 로깅 |
| `PostToolBatch` | 도구 사용 묶음이 완료된 후 | 도구 배치 종료 | 집계 보고, 배치 검증 |
| `Notification` | 알림 전송 | Claude가 알림 전송 | 외부 알림 |
| `MessageDisplay` | 어시스턴트 메시지 텍스트 표시 | 메시지 렌더 중 | 표시되는 텍스트 변환·숨김 |
| `SubagentStart` | 서브에이전트 생성 | 서브에이전트 작업 시작 | 서브에이전트 컨텍스트 초기화 |
| `SubagentStop` | 서브에이전트 종료 | 서브에이전트 작업 완료 | 후속 작업 연결 |
| `Stop` | Claude 응답 완료 | 응답 완료 | 정리, 보고 |
| `StopFailure` | API 오류로 턴 종료 | API 오류 발생 | 오류 복구, 로깅 |
| `TeammateIdle` | 팀원 에이전트 유휴 | 에이전트 팀 협업 | 작업 분배 |
| `TaskCompleted` | 작업 완료 표시(할 일 도구가 활성화된 경우에만 발생 — [훅](06-hooks/README.md#훅-이벤트) 참조) | 작업 완료 | 작업 후 처리 |
| `TaskCreated` | TaskCreate로 작업 생성(할 일 도구가 활성화된 경우에만 발생 — [훅](06-hooks/README.md#훅-이벤트) 참조) | 새 작업 생성 | 작업 추적, 로깅 |
| `ConfigChange` | 구성 갱신 | 설정 변경 | 구성 변경에 반응 |
| `CwdChanged` | 작업 디렉터리 변경 | 디렉터리 변경 | 디렉터리별 설정 |
| `DirectoryAdded` | 세션 중 새 작업 디렉터리 등록 | `/add-dir` 또는 SDK `register_repo_root` | 새 디렉터리용 도구 설정 |
| `FileChanged` | 감시 중인 파일 변경 | 파일 수정 | 파일 모니터링, 재빌드 |
| `PreCompact` | 압축 작업 전 | 컨텍스트 압축 | 상태 보존 |
| `PostCompact` | 압축 완료 후 | 압축 완료 | 압축 후 작업 |
| `PreModelSwitch` | 요청된 모델 전환이 적용되기 전 | 모델 전환 요청 | 모델 변경 차단·거부 |
| `PostModelSwitch` | 세션 모델 변경 후 | 모델 전환 완료 | 모델 변경 로깅·반응 |
| `WorktreeCreate` | 워크트리 생성 중 | git 워크트리 생성 | 워크트리 환경 설정 |
| `WorktreeRemove` | 워크트리 제거 중 | git 워크트리 제거 | 워크트리 리소스 정리 |
| `Elicitation` | MCP 서버가 입력 요청 | MCP 일리시테이션 | 입력 검증 |
| `ElicitationResult` | 사용자가 일리시테이션에 응답 | 사용자 응답 | 응답 처리 |
| `SessionEnd` | 세션 종료 | 세션 종료 | 정리, 상태 저장 |

### 예시 훅

| 훅 | 설명 | 이벤트 | 범위 | 설치 |
|------|-------------|-------|-------|--------------|
| `pre-tool-check.sh` | 위험한 Bash 명령 차단·경고 | PreToolUse:Bash | User | `cp 06-hooks/pre-tool-check.sh ~/.claude/hooks/` |
| `security-scan.sh` | 보안 스캔 | PostToolUse:Write | Project | `cp 06-hooks/security-scan.sh .claude/hooks/` |
| `format-code.sh` | 자동 포맷팅 | PostToolUse:Write | User | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.sh` | 프롬프트 검증 | UserPromptSubmit | Project | `cp 06-hooks/validate-prompt.sh .claude/hooks/` |
| `context-tracker.py` | 토큰 사용량 추적 | UserPromptSubmit, Stop | User | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `context-tracker-tiktoken.py` | 토큰 사용량 추적(tiktoken, 정확도 약 90-95%) | UserPromptSubmit, Stop | User | `cp 06-hooks/context-tracker-tiktoken.py ~/.claude/hooks/` |
| `pre-commit.sh` | 커밋 전 검증 | PreToolUse:Bash | Project | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | 명령 로깅 | PostToolUse:Bash | User | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |
| `dependency-check.sh` | 매니페스트 변경 시 취약점 스캔 | PostToolUse:Write | Project | `cp 06-hooks/dependency-check.sh .claude/hooks/` |
| `notify-team.sh` | git push 시 팀 알림 | PostToolUse:Bash | Project | `cp 06-hooks/notify-team.sh .claude/hooks/` |
| `session-end.sh` | 세션 종료 시 진행 상황 기록 | SessionEnd | User | `cp 06-hooks/session-end.sh ~/.claude/hooks/` |

> **범위**: `Project` = 팀(`.claude/settings.json`), `User` = 개인(`~/.claude/settings.json`)

### 훅 구성

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "~/.claude/hooks/pre-tool-check.sh" }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          { "type": "command", "command": "~/.claude/hooks/format-code.sh" }
        ]
      }
    ]
  }
}
```

**참조**: [06-hooks/](06-hooks/) | [공식 문서](https://code.claude.com/docs/en/hooks)

**빠른 설치 (모든 훅)**:
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## 메모리 파일

세션을 넘어 자동으로 로드되는 영구 컨텍스트입니다.

### 메모리 유형

| 유형 | 위치 | 범위 | 사용 시점 |
|------|----------|-------|-------------|
| **Managed Policy** | 조직 관리 정책 | 조직 | 조직 전체 표준 적용 |
| **Project** | `./CLAUDE.md` | 프로젝트(팀) | 팀 표준, 프로젝트 컨텍스트 |
| **Project Rules** | `.claude/rules/` | 프로젝트(팀) | 모듈식 프로젝트 규칙 |
| **User** | `~/.claude/CLAUDE.md` | 사용자(개인) | 개인 선호 |
| **User Rules** | `~/.claude/rules/` | 사용자(개인) | 모듈식 개인 규칙 |
| **Local** | `./CLAUDE.local.md` | 로컬(git 무시) | 머신별 로컬 재정의(gitignore됨). 개발자별 재정의 파일로 https://code.claude.com/docs/en/memory 에 문서화되어 있습니다. |
| **Auto Memory** | 자동 | 세션 | 자동으로 수집되는 통찰과 교정 |

> **범위**: `Organization` = 관리자가 관리, `Project` = git으로 팀과 공유, `User` = 개인 선호, `Local` = 커밋되지 않음, `Session` = 자동 관리

**참조**: [02-memory/](02-memory/) | [공식 문서](https://code.claude.com/docs/en/memory)

**빠른 설치**:
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## 새 기능

| 기능 | 설명 | 사용 방법 |
|---------|-------------|------------|
| **/focus** | 방해 요소 없는 출력 표시를 위한 포커스 뷰 전환 (v2.1.110) | 긴 작업 중 시각적 잡음을 줄이려면 `/focus` 실행 |
| **/proactive** | `/loop`의 별칭 — 반복 작업 동작이 동일 (v2.1.105) | `/loop` 대신 `/proactive`를 같은 의미로 사용 |
| **/recap** | 기존 세션으로 돌아올 때 세션 요약 표시 (v2.1.108) | 자리를 비운 뒤 무엇을 했는지 파악하려면 `/recap` 실행 |
| **/tui** | 터미널 UI 렌더러 설정: 깜빡임 없는 렌더링에는 `/tui fullscreen`, 되돌리려면 `/tui default`. 인자 없는 `/tui`는 활성 렌더러를 출력 (v2.1.110) | 전체 화면 터미널이나 tmux에서 `/tui fullscreen` 사용 |
| **/undo** | `/rewind`의 별칭 (v2.1.108) | `/undo`, `/checkpoint`, `/rewind`를 같은 의미로 사용 |
| **Monitor 도구** | 폴링 대신 백그라운드 명령의 stdout 스트림을 관찰하고 이벤트에 반응 (v2.1.98+) | [고급 기능](09-advanced-features/)에서 Monitor 도구 사용 |
| **출력 스타일** | 시스템 프롬프트를 통해 Claude의 역할, 어조, 기본 응답 형식 변경. 내장: Default, Proactive, Explanatory, Learning, Concise | `/config` → 출력 스타일, `outputStyle` 설정, 또는 `/output-style` 실행(v2.1.91 제거 후 v2.1.269에서 다시 추가). [고급 기능](09-advanced-features/#출력-스타일) 참조 |
| **상태 표시줄** | stdin으로 세션·모델·비용·컨텍스트 JSON을 받는 명령에서 사용자 지정 상태 표시줄 렌더 | `/statusline` 또는 `statusLine` 설정. [고급 기능](09-advanced-features/#상태-표시줄) 참조 |
| **커뮤니티 마켓플레이스** | Anthropic의 자동 검증을 통과한 서드파티 플러그인. 각각 커밋 SHA에 고정됩니다 | `/plugin marketplace add anthropics/claude-plugins-community` 실행 후 `/plugin install <name>@claude-community` |
| **/team-onboarding** | 프로젝트의 Claude Code 설정에서 팀원 온보딩 가이드 자동 생성 (v2.1.101) | 프로젝트에서 `/team-onboarding` 실행 |
| **원격 제어** | API로 Claude Code 세션을 원격 제어. **더 이상 리서치 프리뷰가 아닙니다** — `claude remote-control`을 실행 중인 모든 머신이 Claude 앱의 Code 탭에 기기 카드로 나타나므로, 휴대폰에서 그 머신의 세션을 시작할 수 있습니다 | 머신에서 `claude remote-control`을 실행한 뒤 Claude 앱에서 해당 기기 카드 선택. [고급 기능](09-advanced-features/README.md) 참조 |
| **웹 세션** | 클라우드 세션에서 Claude Code 실행 | `claude --cloud "task"` 또는 claude.ai/code에서 시작 |
| **데스크톱 앱** | Claude Code용 네이티브 데스크톱 애플리케이션 | `/desktop` 사용 또는 Anthropic 웹사이트에서 다운로드 |
| **세션 간 메시징** | 세션끼리 메시지를 주고받을 수 있습니다 — 다른 머신과 클라우드 세션도 포함하며, `ListAgents`로 탐색합니다 (v2.1.224+ macOS/Linux, 네이티브 Windows는 v2.1.234+) | [고급 기능](09-advanced-features/README.md#세션-간-메시징) 참조. 수신은 `crossSessionInbound`로 제어 |
| **셀프 호스팅 러너** | Claude Code 웹·모바일·데스크톱 세션을 자체 머신이나 컨테이너에서 실행 (v2.1.224+, Team/Enterprise) | `claude self-hosted-runner setup`; [CLI](10-cli/README.md) 참조 |
| **`archive` 플러그인 소스** | HTTPS zip에서 플러그인 설치, 선택적으로 `sha256`으로 고정 (v2.1.224+) | [플러그인](07-plugins/README.md#archive-소스-v21224) 참조 |
| **`command` 플러그인 소스** | 로컬에 설치된 도구가 플러그인 디렉터리 경로를 출력 (v2.1.229+) | [플러그인](07-plugins/README.md#command-소스-v21229) 참조 |
| **마켓플레이스 소유자 와일드카드** | `"owner/*"`로 GitHub 소유자 아래의 모든 마켓플레이스 저장소를 허용·차단 — `strictKnownMarketplaces`와 `blockedMarketplaces`에서만 (v2.1.223+) | [플러그인](07-plugins/README.md#마켓플레이스-구성) 참조 |
| **샌드박스 자격 증명 마스킹** | 샌드박스 명령은 센티널을 읽고, 프록시가 송신 시 실제 시크릿으로 치환 (v2.1.221+, Linux/WSL) | [고급 기능](09-advanced-features/README.md#자격-증명-마스킹-v21221-v21224) 참조 |
| **에이전트 팀** | 관련 작업을 함께 수행하는 여러 에이전트 조율 | 협업하고 컨텍스트를 공유하는 팀원 에이전트 구성 |
| **작업 목록** | 백그라운드 작업 관리와 모니터링 | `/tasks`로 백그라운드 작업 조회·관리 |
| **프롬프트 제안** | 컨텍스트 인식 커맨드 제안 | 현재 컨텍스트에 따라 제안이 자동으로 나타남 |
| **Git 워크트리** | 병렬 개발을 위한 격리된 git 워크트리 | 안전한 병렬 브랜치 작업에 워크트리 커맨드 사용 |
| **샌드박싱** | 안전을 위한 격리 실행 환경 | `/sandbox`로 전환하며, 제한된 환경에서 명령 실행 |
| **MCP OAuth** | MCP 서버용 OAuth 인증 | 안전한 접근을 위해 MCP 서버 설정에서 OAuth 자격 증명 구성 |
| **MCP 도구 검색** | MCP 도구를 동적으로 검색·탐색 | 도구 검색으로 연결된 서버의 사용 가능한 MCP 도구 찾기 |
| **예약된 작업** | `/loop`와 cron 도구로 반복 작업 설정 | `/loop 5m /command` 또는 CronCreate 도구 사용 |
| **Chrome 통합** | Claude in Chrome 확장을 통해 본인의 Chrome/Edge(보이는 창, 본인 로그인) 구동 | `--chrome` 플래그 또는 `/chrome` 커맨드 사용 |
| **키보드 사용자 정의** | 코드(chord) 지원을 포함한 키바인딩 사용자 정의 | `/keybindings` 사용 또는 `~/.claude/keybindings.json` 편집 |
| **오토 모드** | 백그라운드 안전 분류기 검사와 함께 완전 자율 동작 | `Shift+Tab`으로 순환하거나 `--permission-mode auto` |
| **채널** | 다중 채널 커뮤니케이션(Telegram, Slack 등) (리서치 프리뷰) | 채널 플러그인 구성; 2026년 3월 |
| **음성 받아쓰기** | 프롬프트 음성 입력 | 마이크 아이콘이나 음성 키바인딩 사용 |
| **에이전트 훅 유형** | 셸 명령 대신 서브에이전트를 생성하는 훅 | 훅 구성에 `"type": "agent"` 설정 |
| **프롬프트 훅 유형** | 단일 턴 평가를 위해 Claude 모델에 프롬프트를 보내는 훅. 모델이 결정을 JSON으로 반환합니다 | 훅 구성에 `"type": "prompt"` 설정 |
| **MCP 일리시테이션** | MCP 서버가 도구 실행 중 사용자 입력을 요청할 수 있음 | `Elicitation`·`ElicitationResult` 훅 이벤트로 처리 |
| **플러그인 LSP 지원** | 플러그인을 통한 Language Server Protocol 통합 | 편집기 기능을 위해 `plugin.json`에 LSP 서버 구성 |
| **관리형 드롭인** | 조직 관리 드롭인 구성 (v2.1.83) | 관리 정책으로 관리자가 구성하며 모든 사용자에게 자동 적용 |
| **`claude plugin init`** | `.claude/skills` 안에 새 플러그인 스캐폴드 생성. 이런 플러그인은 마켓플레이스 없이 자동 로드됩니다 (v2.1.157) | `claude plugin init <name>` 실행 |
| **서드파티 제공자의 오토 모드** | Amazon Bedrock, Google Cloud의 Agent Platform, Microsoft Foundry, 로그인한 Claude 앱 게이트웨이 세션에서 기본 제공됩니다. 지원 모델은 Claude Sonnet 5 이상, Opus 4.7 이상, Haiku 5.5(v2.1.293+), Fable 모델입니다(옵트인 필요 v2.1.158–v2.1.206, v2.1.207에서 제거 — `CLAUDE_CODE_ENABLE_AUTO_MODE`는 여전히 허용되지만 효과 없음) | `Shift+Tab`으로 순환하거나 `--permission-mode auto` |
| **즉시 대화상자 커맨드** | Claude가 작업 중일 때도 `/permissions`를 열 수 있고(규칙 변경은 해당 턴의 나머지에 적용), `/add-dir`, `/autocompact`, `/theme`, `/help`, `/config`, `/advisor` 대화상자는 Claude 응답이 끝날 때까지 대기하지 않고 **전체 화면 TUI**에서 턴 중에 열립니다(v2.1.232부터 `/bug`가 이미 이렇게 동작) (v2.1.234) | Claude가 작업 중일 때 해당 커맨드 중 하나를 실행. [슬래시 커맨드](01-slash-commands/README.md) 참조 |
| **`CLAUDE_CODE_PROJECT_DIR_NAME`** | 프로젝트별 트랜스크립트 디렉터리 이름을 제어하는 환경변수 (v2.1.234) | Claude Code 실행 전 셸/환경에 설정. `CLAUDE_CONFIG_DIR`도 설정된 경우가 아니면 무시됩니다. [CLI](10-cli/README.md) 참조 |
| **목표 체크인 임계값** | `/goal`이 활성인 동안 백그라운드 작업이 30분 이상 진행되지 않으면 조용히 계속하지 않고 상태 업데이트로 체크인합니다. `CLAUDE_CODE_GOAL_CHECKIN_MINUTES`로 조정하고 `0`으로 끌 수 있습니다 (v2.1.234) | 활성 `/goal`과 함께 `CLAUDE_CODE_GOAL_CHECKIN_MINUTES=<n>` 설정. [슬래시 커맨드](01-slash-commands/README.md) 참조 |
| **사용 한도 자동 계속** | claude.ai 사용 한도 때문에 세션이 막혀 있었다면, 한도가 초기화될 때 Claude Code가 세션을 자동으로 계속합니다 (v2.1.234) | 기본 켜짐. `/config` → "Continue automatically at usage limit"에서 끌 수 있습니다. [고급 기능](09-advanced-features/) 참조 |
| **`spellcheck` 설정** | `PATH`에 있는 aspell, hunspell, ispell 중 하나를 사용해 프롬프트 입력의 철자 오류에 밑줄 표시. 기본 꺼짐 (v2.1.235) | 검사기를 설치한 뒤 `~/.claude/settings.json`에 `"spellcheck": { "enabled": true }` 설정. 사용자 설정, `--settings`, 관리형 설정에서만 동작하며 프로젝트 설정에서는 무시됩니다. [고급 기능](09-advanced-features/) 참조 |
| **에이전트 팀 기본 모델** | "Default teammate model" `/config` 설정이 제거되었습니다. 이제 팀원은 생성 호출에서 명시하지 않는 한 팀 리드의 모델을 기본으로 상속합니다 (v2.1.234) | [서브에이전트 — 에이전트 팀](04-subagents/README.md#에이전트-팀-실험적) 참조 |
| **`/design`** | 디자인 캔버스 — 아티팩트 위에 만들고 코드 대신 시각적으로 다듬는 다중 아트보드 시각 디자인(UI 목업, 화면 흐름, 랜딩 페이지, 포스터). v2.1.265+ 필요, Pro/Max/Team/Enterprise | CLI 또는 데스크톱 앱에서 `/design` 실행. [슬래시 커맨드](01-slash-commands/README.md) 참조 |
| **`notify_when_idle`** | 같은 머신의 다른 세션에 다음 유휴 시 알림을 한 번 보내달라고 요청하는 세션 간 `SendMessage` 입력 — 옵트인, 1회성, 폴링 없음 (v2.1.236). 관련: `ListAgents`가 세션 자신의 이름을 보고하고 활성 팀원을 나열하며, Windows에 세션 간 메시징이 추가됨 (v2.1.239) | `SendMessage`에 `notify_when_idle` 전달. [고급 기능](09-advanced-features/README.md#세션-간-메시징) 참조 |
| **플러그인 매니페스트 필드** | `plugin.json`이 `workflows`, `channels`, `dependencies`(semver), `outputStyles`, `keywords`, `metadata`, `lspServers`, `experimental.themes`/`experimental.monitors`를 받습니다. CLI에는 `claude plugin new`, `remove`/`rm`, `prune`/`autoremove`와 `--with`, `-f`/`--force`, `--available`, `--push`, `--dry-run` 플래그가 추가됨 | [플러그인](07-plugins/README.md) 참조 |
| **제한 모드** | 명령이나 코드를 실행하는 내장 도구(Bash, PowerShell 등)와 WebFetch를 제거합니다. `--tools`로 개별 지정한 경우(단, `default` 프리셋 경유는 불가)는 예외입니다. 사용자·프로젝트·로컬 설정을 무시하고(관리형 설정과 `--settings`는 여전히 적용), 파일 도구를 작업 디렉터리로 제한하며, `bypassPermissions`를 거부하고, 클라우드 세션 생성을 거부합니다 (v2.1.248+) | `claude --restricted` 또는 `CLAUDE_CODE_RESTRICTED=1`. [CLI](10-cli/README.md) 참조 |
| **`/advisor` 텍스트 형식** | `/advisor`, `/advisor <model>`, `/advisor off`가 대화상자뿐 아니라 데스크톱 앱, 원격 제어, 기타 헤드리스(`-p`/Agent SDK) 세션에서도 텍스트 커맨드로 동작합니다 (v2.1.260+) | 헤드리스 세션에서 `/advisor off` 입력. [슬래시 커맨드](01-slash-commands/README.md) 참조 |

---

## 빠른 참조 매트릭스

### 기능 선택 가이드

| 필요 | 권장 기능 | 이유 |
|------|---------------------|-----|
| 빠른 단축키 | 슬래시 커맨드 | 수동, 즉시 |
| 지속되는 컨텍스트 | 메모리 | 자동 로드 |
| 복잡한 자동화 | 스킬 | 자동 호출 |
| 전문화된 작업 | 서브에이전트 | 격리된 컨텍스트 |
| 외부 데이터 | MCP 서버 | 실시간 접근 |
| 이벤트 자동화 | 훅 | 이벤트 트리거 |
| 완전한 솔루션 | 플러그인 | 올인원 번들 |

### 설치 우선순위

| 우선순위 | 기능 | 커맨드 |
|----------|---------|---------|
| 1. 필수 | 메모리 | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. 일상 사용 | 슬래시 커맨드 | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. 품질 | 서브에이전트 | `cp 04-subagents/*.md .claude/agents/` |
| 4. 자동화 | 훅 | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. 외부 | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. 고급 | 스킬 | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. 완성 | 플러그인 | `claude --plugin-dir ./07-plugins/pr-review` |

---

## 한 번에 설치하는 전체 명령

이 저장소의 모든 예시를 설치합니다:

```bash
# Create directories
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# Install all features
cp 01-slash-commands/*.md .claude/commands/ && \
cp 02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r 03-skills/* ~/.claude/skills/ && \
cp 04-subagents/*.md .claude/agents/ && \
cp 06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## 추가 자료

- [Claude Code 공식 문서](https://code.claude.com/docs/en/overview)
- [MCP 프로토콜 명세](https://modelcontextprotocol.io)
- [학습 로드맵](LEARNING-ROADMAP.md)
- [메인 README](README.md)

---

**최종 갱신**: 2026년 10월 18일
**Claude Code 버전**: 2.1.302
**출처**:
- https://code.claude.com/docs/en/sub-agents
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/changelog#2-1-172
- https://code.claude.com/docs/en/changelog#2-1-174
- https://github.com/anthropics/claude-code/releases/tag/v2.1.145
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/plugin-marketplaces
- https://code.claude.com/docs/en/discover-plugins
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/slash-commands
- https://code.claude.com/docs/en/fast-mode
- https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/chrome
- https://code.claude.com/docs/en/skills#bundled-skills
- https://code.claude.com/docs/en/plugins/manifest-reference
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/env-vars
- https://code.claude.com/docs/en/cross-session-messaging
- https://support.claude.com/en/articles/17440474-migrate-from-standalone-claude-design-to-claude
**호환 모델**: Claude Fable 5.1, Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
