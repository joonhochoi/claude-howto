<!-- i18n-source: INDEX.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 예제 - 전체 색인

이 문서는 모든 예제 파일을 기능 유형별로 정리한 전체 색인입니다.

## 요약 통계

- **전체 파일**: 100개 이상
- **카테고리**: 10개 기능 카테고리
- **플러그인**: 완성된 플러그인 3개
- **스킬**: 완성된 스킬 6개
- **훅**: 예제 훅 11개
- **바로 사용 가능**: 모든 예제

---

## 01. 슬래시 커맨드 (파일 10개)

일반적인 워크플로를 위한 사용자 호출 단축 명령입니다.

| 파일 | 설명 | 사용 사례 |
|------|------|----------|
| `optimize.md` | 코드 최적화 분석기 | 성능 문제 찾기 |
| `pr.md` | PR 준비 | PR 워크플로 자동화 |
| `generate-api-docs.md` | API 문서 생성기 | API 문서 생성 |
| `commit.md` | 커밋 메시지 도우미 | 커밋 표준화 |
| `setup-ci-cd.md` | CI/CD 파이프라인 설정 | DevOps 자동화 |
| `push-all.md` | 모든 변경사항 푸시 | 빠른 푸시 워크플로 |
| `unit-test-expand.md` | 단위 테스트 커버리지 확장 | 테스트 자동화 |
| `doc-refactor.md` | 문서 리팩터링 | 문서 개선 |
| `pr-slash-command.png` | 스크린샷 예제 | 시각 자료 참고 |
| `README.md` | 문서 | 설치 및 사용 가이드 |

**설치 경로**: `.claude/commands/`

**사용법**: `/optimize`, `/pr`, `/generate-api-docs`, `/commit`, `/setup-ci-cd`, `/push-all`, `/unit-test-expand`, `/doc-refactor`

---

## 02. 메모리 (파일 6개)

지속되는 컨텍스트와 프로젝트 표준입니다.

| 파일 | 설명 | 범위 | 위치 |
|------|------|------|------|
| `project-CLAUDE.md` | 팀 프로젝트 표준 | 프로젝트 전체 | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | API 전용 규칙 | 디렉터리 | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | 개인 선호 설정 | 사용자 | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | 스크린샷: 메모리 저장됨 | - | 시각 자료 참고 |
| `memory-ask-claude.png` | 스크린샷: Claude에게 질문 | - | 시각 자료 참고 |
| `README.md` | 문서 | - | 참고 |

**설치**: 적절한 위치에 복사합니다

**사용법**: Claude가 자동으로 로드합니다

**AGENTS.md**(v2.1.277): 작업 디렉터리 또는 그 상위에 `CLAUDE.md`, `.claude/CLAUDE.md`, `CLAUDE.local.md`가 없으면 프로젝트 지시사항으로 읽습니다 — `02-memory/README.md#agentsmd` 참고

---

## 03. 스킬 (파일 23개)

스크립트와 템플릿을 갖춘, 자동 호출되는 기능입니다.

### 코드 리뷰 스킬 (파일 5개)
```
code-review-specialist/
├── SKILL.md                          # Skill definition
├── scripts/
│   ├── analyze-metrics.py            # Code metrics analyzer
│   └── compare-complexity.py         # Complexity comparison
└── templates/
    ├── review-checklist.md           # Review checklist
    └── finding-template.md           # Finding documentation
```

**목적**: 보안·성능·품질 분석을 아우르는 종합 코드 리뷰

**자동 호출**: 코드를 리뷰할 때

---

### 브랜드 보이스 스킬 (파일 4개)
```
brand-voice/
├── SKILL.md                          # Skill definition
├── templates/
│   ├── email-template.txt            # Email format
│   └── social-post-template.txt      # Social media format
└── tone-examples.md                  # Example messages
```

**목적**: 커뮤니케이션에서 일관된 브랜드 보이스 유지

**자동 호출**: 마케팅 문구를 작성할 때

---

### 문서 생성기 스킬 (파일 2개)
```
doc-generator/
├── SKILL.md                          # Skill definition
└── generate-docs.py                  # Python doc extractor
```

**목적**: 소스 코드에서 종합 API 문서 생성

**자동 호출**: API 문서를 생성하거나 갱신할 때

---

### 리팩터링 스킬 (파일 5개)
```
refactor/
├── SKILL.md                          # Skill definition
├── scripts/
│   ├── analyze-complexity.py         # Complexity analyzer
│   └── detect-smells.py              # Code smell detector
├── references/
│   ├── code-smells.md                # Code smells catalog
│   └── refactoring-catalog.md        # Refactoring patterns
└── templates/
    └── refactoring-plan.md           # Refactoring plan template
```

**목적**: 복잡도 분석을 동반한 체계적 코드 리팩터링

**자동 호출**: 코드를 리팩터링할 때

---

### Claude MD 스킬 (파일 1개)
```
claude-md/
└── SKILL.md                          # Skill definition
```

**목적**: CLAUDE.md 파일 관리 및 최적화

---

### 블로그 초안 스킬 (파일 3개)
```
blog-draft/
├── SKILL.md                          # Skill definition
└── templates/
    ├── draft-template.md             # Blog draft template
    └── outline-template.md           # Blog outline template
```

**목적**: 일관된 구조로 블로그 글 초안 작성

**추가**: `README.md` - 스킬 개요 및 사용 가이드

**설치 경로**: `~/.claude/skills/` 또는 `.claude/skills/`

---

## 04. 서브에이전트 (파일 10개)

사용자 정의 기능을 갖춘 특화 AI 어시스턴트입니다.

| 파일 | 설명 | 도구 | 사용 사례 |
|------|------|------|----------|
| `code-reviewer.md` | 코드 품질 분석 | Read, Grep, Glob, Bash | 종합 리뷰 |
| `test-engineer.md` | 테스트 커버리지 분석 | Read, Write, Bash, Grep | 테스트 자동화 |
| `documentation-writer.md` | 문서 작성 | Read, Write, Grep | 문서 생성 |
| `secure-reviewer.md` | 보안 리뷰(읽기 전용) | Read, Grep | 보안 감사 |
| `implementation-agent.md` | 전체 구현 | Read, Write, Edit, Bash, Grep, Glob | 기능 개발 |
| `debugger.md` | 디버깅 전문가 | Read, Edit, Bash, Grep, Glob | 버그 조사 |
| `data-scientist.md` | 데이터 분석 전문가 | Bash, Read, Write | 데이터 워크플로 |
| `clean-code-reviewer.md` | 클린 코드 표준 | Read, Grep, Glob, Bash | 코드 품질 |
| `performance-optimizer.md` | 성능 병목 분석 | Read, Edit, Bash, Grep, Glob | 최적화 작업 |
| `README.md` | 문서 | - | 설치 및 사용 가이드 |

**설치 경로**: `.claude/agents/`

**사용법**: 메인 에이전트가 자동으로 위임합니다

---

## 05. MCP 프로토콜 (파일 5개)

외부 도구 및 API 연동입니다.

| 파일 | 설명 | 연동 대상 | 사용 사례 |
|------|------|----------|----------|
| `github-mcp.json` | GitHub 연동 | GitHub API | PR/이슈 관리 |
| `database-mcp.json` | 데이터베이스 쿼리 | PostgreSQL/MySQL | 실시간 데이터 조회 |
| `filesystem-mcp.json` | 파일 작업 | 로컬 파일시스템 | 파일 관리 |
| `multi-mcp.json` | 다중 서버 | GitHub + DB + Slack | 전체 통합 |
| `README.md` | 문서 | - | 설치 및 사용 가이드 |

**설치 경로**: `.mcp.json`(프로젝트 범위) 또는 `~/.claude.json`(사용자 범위)

**사용법**: `/mcp__github__list_prs` 등

---

## 06. 훅 (파일 12개)

자동으로 실행되는 이벤트 기반 자동화 스크립트입니다.

| 파일 | 설명 | 이벤트 | 사용 사례 |
|------|------|--------|----------|
| `format-code.sh` | 코드 자동 포매팅 | PostToolUse (matcher: Write) | 코드 포매팅 |
| `pre-commit.sh` | 커밋 전 테스트 실행 | PreToolUse (matcher: Bash) | 테스트 자동화 |
| `pre-tool-check.sh` | 실행 전 명령 검증 및 감사 | PreToolUse (matcher: Bash) | 가드레일, 감사 로그 |
| `security-scan.sh` | 보안 스캔 | PostToolUse (matcher: Write) | 보안 점검 |
| `dependency-check.sh` | 의존성 매니페스트에서 취약점 스캔 | PostToolUse (matcher: Write) | 공급망 점검 |
| `log-bash.sh` | bash 명령 로깅 | PostToolUse (matcher: Bash) | 명령 로깅 |
| `notify-team.sh` | 알림 전송 | PostToolUse (matcher: Bash) | 팀 알림 |
| `validate-prompt.sh` | 프롬프트 검증 | UserPromptSubmit | 입력 검증 |
| `session-end.sh` | 세션 종료 시 진행 상황 캡처 | SessionEnd | 진행 상황 추적 |
| `context-tracker.py` | 컨텍스트 창 사용량 추적 | UserPromptSubmit, Stop | 컨텍스트 모니터링 |
| `context-tracker-tiktoken.py` | 토큰 기반 컨텍스트 추적 | UserPromptSubmit, Stop | 정밀 토큰 계산 |
| `README.md` | 문서 | - | 설치 및 사용 가이드 |

**설치 경로**: `~/.claude/settings.json`에서 설정합니다

**사용법**: 설정에 구성하면 자동으로 실행됩니다

**훅 유형**(5가지): `command`, `http`, `prompt`, `mcp_tool`, `agent` — 훅이 실행되는 방식입니다.

**훅 이벤트**(33개, 4개 범주) — 실행되는 시점입니다:
- 도구 훅: PreToolUse, PostToolUse, PostToolUseFailure, PostToolBatch, PermissionRequest, PermissionDenied
- 세션 훅: SessionStart, Setup, SessionEnd, Stop, StopFailure, SubagentStart, SubagentStop
- 작업 훅: UserPromptSubmit, UserPromptExpansion, MessageDisplay, TaskCompleted, TaskCreated, TeammateIdle (TaskCompleted/TaskCreated는 투두 도구가 활성화된 경우에만 발생하며, Claude 3.x 모델, Opus 4~4.7, Sonnet 4~4.6, Haiku 4.5에서만 기본 제공됩니다)
- 수명 주기 훅: ConfigChange, CwdChanged, DirectoryAdded, FileChanged, PreCompact, PostCompact, PreModelSwitch, PostModelSwitch, WorktreeCreate, WorktreeRemove, Notification, InstructionsLoaded, Elicitation, ElicitationResult

---

## 07. 플러그인 (완성된 플러그인 3개, 파일 39개)

여러 기능을 묶음으로 제공하는 모음입니다.

### PR 리뷰 플러그인 (파일 10개)
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── review-pr.md                  # Comprehensive review
│   ├── check-security.md             # Security check
│   └── check-tests.md                # Test coverage check
├── agents/
│   ├── security-reviewer.md          # Security specialist
│   ├── test-checker.md               # Test specialist
│   └── performance-analyzer.md       # Performance specialist
├── mcp/
│   └── github-config.json            # GitHub integration
├── hooks/
│   └── pre-review.js                 # Pre-review validation
└── README.md                         # Plugin documentation
```

**기능**: 보안 분석, 테스트 커버리지, 성능 영향

**커맨드**: `/review-pr`, `/check-security`, `/check-tests`

**설치**: `claude --plugin-dir ./07-plugins/pr-review` (저장소 루트에서 실행)

---

### DevOps 자동화 플러그인 (파일 15개)
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── deploy.md                     # Deployment
│   ├── rollback.md                   # Rollback
│   ├── status.md                     # System status
│   └── incident.md                   # Incident response
├── agents/
│   ├── deployment-specialist.md      # Deployment expert
│   ├── incident-commander.md         # Incident coordinator
│   └── alert-analyzer.md             # Alert analyzer
├── mcp/
│   └── kubernetes-config.json        # Kubernetes integration
├── hooks/
│   ├── pre-deploy.js                 # Pre-deployment checks
│   └── post-deploy.js                # Post-deployment tasks
├── scripts/
│   ├── deploy.sh                     # Deployment automation
│   ├── rollback.sh                   # Rollback automation
│   └── health-check.sh               # Health checks
└── README.md                         # Plugin documentation
```

**기능**: Kubernetes 배포, 롤백, 모니터링, 장애 대응

**커맨드**: `/deploy`, `/rollback`, `/status`, `/incident`

**설치**: `claude --plugin-dir ./07-plugins/devops-automation` (저장소 루트에서 실행)

---

### 문서 플러그인 (파일 14개)
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── generate-api-docs.md          # API docs generation
│   ├── generate-readme.md            # README creation
│   ├── sync-docs.md                  # Doc synchronization
│   └── validate-docs.md              # Doc validation
├── agents/
│   ├── api-documenter.md             # API doc specialist
│   ├── code-commentator.md           # Code comment specialist
│   └── example-generator.md          # Example creator
├── mcp/
│   └── github-docs-config.json       # GitHub integration
├── templates/
│   ├── api-endpoint.md               # API endpoint template
│   ├── function-docs.md              # Function doc template
│   └── adr-template.md               # ADR template
└── README.md                         # Plugin documentation
```

**기능**: API 문서, README 생성, 문서 동기화, 검증

**커맨드**: `/generate-api-docs`, `/generate-readme`, `/sync-docs`, `/validate-docs`

**설치**: `claude --plugin-dir ./07-plugins/documentation` (저장소 루트에서 실행)

**추가**: `README.md` - 플러그인 개요 및 사용 가이드

---

## 08. 체크포인트와 되감기 (파일 2개)

대화 상태를 저장하고 다른 접근 방식을 탐색합니다.

| 파일 | 설명 | 내용 |
|------|------|------|
| `README.md` | 문서 | 체크포인트 종합 가이드 |
| `checkpoint-examples.md` | 실제 사례 | 데이터베이스 마이그레이션, 성능 최적화, UI 반복, 디버깅 |
| | | |

**핵심 개념**:
- **체크포인트**: 대화 상태의 스냅샷
- **되감기**: 이전 체크포인트로 복귀
- **분기점**: 여러 접근 방식 탐색

**사용법**:
```
# Checkpoints are created automatically with every user prompt
# To rewind, press Esc twice or use:
/rewind
# Then choose: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, Summarize up to here, or Never mind
```

**사용 사례**:
- 서로 다른 구현 방식 시도
- 실수에서 복구
- 안전한 실험
- 해결책 비교
- A/B 테스트

---

## 09. 고급 기능 (파일 4개)

복잡한 워크플로를 위한 고급 기능입니다.

| 파일 | 설명 | 기능 |
|------|------|------|
| `README.md` | 전체 가이드 | 모든 고급 기능 문서 |
| `config-examples.json` | 구성 예제 | 사용 사례별 구성 10개 이상 |
| `planning-mode-examples.md` | 플랜 모드 예제 | REST API, 데이터베이스 마이그레이션, 리팩터링 |
| `setup-auto-mode-permissions.py` | 오토 모드용 `permissions.allow` 초기 설정 | 멱등, `--dry-run` 및 옵트인 플래그 |
| 동적 워크플로 | `/workflows`를 통한 결정적 멀티 에이전트 오케스트레이션 (v2.1.154) | 종합 감사, 마이그레이션, 규모 확장 |
| 예약 작업 | `/loop`와 cron 도구를 사용하는 반복 작업 | 자동화된 반복 워크플로 |
| Chrome 통합 | Claude in Chrome 확장 프로그램을 통한 자체 Chrome 브라우저 자동화 | 웹 테스트 및 스크래핑 |
| 원격 제어(확장) | 연결 방식, 보안, 비교표, 기기 카드 | 원격 세션 관리(더 이상 리서치 프리뷰가 아님) |
| 세션 간 메시징 | `SendMessage` / `ListAgents`, `notify_when_idle` 포함 (v2.1.236) | 동일 머신의 세션 간 협업 |
| 키보드 사용자 정의 | 사용자 정의 키바인딩, 코드(chord) 지원, 컨텍스트 | 개인화된 단축키 |
| 데스크톱 앱(확장) | 커넥터, launch.json, 엔터프라이즈 기능 | 데스크톱 통합 |
| | | |

**다루는 고급 기능**:

### 플랜 모드
- 상세한 구현 계획 수립
- 시간 추정과 위험 평가
- 체계적인 작업 분해

### 확장 사고
- 복잡한 문제에 대한 심층 추론
- 아키텍처 결정 분석
- 트레이드오프 평가

### 백그라운드 작업
- 블로킹 없이 실행되는 장시간 작업
- 병렬 개발 워크플로
- 작업 관리와 모니터링

### 동적 워크플로 (v2.1.154)
- 수십에서 수백 개의 백그라운드 서브에이전트를 결정적으로 오케스트레이션
- 종합적 커버리지를 위한 팬아웃/파이프라인/병렬 단계
- `/workflows`로 실행 내역을 확인합니다. `/effort`의 Ultracode 토글(`/effort ultracode [on|off]`)을 사용하면 effort 레벨을 바꾸지 않고 해당 세션에 한해 켤 수 있고(v2.1.284), `ultracode` 설정을 사용하면 이 상태가 지속됩니다
- v2.1.219 기준 기본 크기 가이드라인은 medium(에이전트 10개 미만 목표)입니다 — `/config`의 **Dynamic workflow size**에서 변경합니다

### 권한 모드
- **manual**: 읽기 외 작업은 모두 확인을 요청합니다(v2.1.200부터 Manual로 표시되며, 설정 값은 여전히 `default`입니다)
- **acceptEdits**: 파일 편집은 자동 수락하고 나머지는 확인합니다
- **plan**: 읽기 전용 분석, 수정 없음
- **auto**: 모든 작업 허용, 백그라운드 안전 점검 수행 — 분류기가 명령과 보호 디렉터리 쓰기를 검토합니다(`autoMode` 설정 객체로 구성)
- **dontAsk**: 사전 승인된 도구만 허용 — 확인을 요구할 호출을 모두 자동 거부합니다. Claude는 `permissions.allow`에 해당하는 호출, 읽기 전용 Bash 명령, `PreToolUse` 훅이 승인한 호출만 실행합니다
- **bypassPermissions**: 모두 수락합니다(`--permission-mode bypassPermissions` 또는 이에 상응하는 `--dangerously-skip-permissions`로 활성화)

### 헤드리스 모드 (`claude -p`)
- CI/CD 통합
- 자동화된 작업 실행
- 배치 처리

### 세션 관리
- 여러 작업 세션
- 세션 전환과 저장
- 세션 지속성

### 대화형 기능
- 키보드 단축키
- 명령 기록
- 탭 자동 완성
- 여러 줄 입력

### 구성
- 종합적인 설정 관리
- 환경별 구성
- 프로젝트별 사용자 정의

### 예약 작업
- `/loop` 명령을 사용하는 반복 작업
- Cron 도구: CronCreate, CronList, CronDelete
- 자동화된 반복 워크플로

### Chrome 통합
- Claude in Chrome 확장 프로그램을 통한 자체 Chrome 브라우저 자동화
- 웹 테스트 및 스크래핑 기능
- 페이지 상호작용과 데이터 추출

### 원격 제어(확장)
- 연결 방식과 프로토콜
- 보안 고려사항과 모범 사례
- 원격 접근 옵션 비교표
- 리서치 프리뷰에서 벗어났습니다 — `claude remote-control`을 실행 중인 머신이 Claude 앱의 Code 탭에 기기 카드로 표시됩니다

### 세션 간 메시징
- 동일 머신의 세션 간 `SendMessage`
- `notify_when_idle` — 상대 세션이 다음에 유휴 상태가 되면 한 번 알림을 주는 옵트인 기능입니다(v2.1.236)
- `ListAgents`는 세션 자신의 이름을 알려주고 활성 팀원을 나열합니다(v2.1.239)

### 키보드 사용자 정의
- 사용자 정의 키바인딩 구성
- 다중 키 단축키를 위한 코드(chord) 지원
- 컨텍스트 인식 키바인딩 활성화

### 데스크톱 앱(확장)
- IDE 연동용 커넥터
- launch.json 구성
- 엔터프라이즈 기능과 배포

---

## 10. CLI 사용법 (파일 1개)

명령줄 인터페이스 사용 패턴과 레퍼런스입니다.

| 파일 | 설명 | 내용 |
|------|------|------|
| `README.md` | CLI 문서 | 플래그, 옵션, 사용 패턴 |

**주요 CLI 기능**:
- `claude` - 대화형 세션 시작
- `claude -p "prompt"` - 헤드리스/비대화형 모드
- `claude --cloud "task"` - 클라우드(웹) 세션 시작
- `claude --model` - 모델 선택 (Opus 5.5, Sonnet 5.5, Opus 5, Sonnet 5, Sonnet 4.6, Opus 4.8, Haiku 5.5, Haiku 4.5)
- `claude --permission-mode` - 권한 모드 설정
- `claude --remote-control` - claude.ai 또는 Claude 앱에서도 제어할 수 있는 세션 시작

---

## 문서 파일 (파일 13개)

| 파일 | 위치 | 설명 |
|------|----------|------|
| `README.md` | `/` | 메인 예제 개요 |
| `INDEX.md` | `/` | 이 전체 색인 |
| `QUICK_REFERENCE.md` | `/` | 빠른 참조 카드 |
| `README.md` | `/01-slash-commands/` | 슬래시 커맨드 가이드 |
| `README.md` | `/02-memory/` | 메모리 가이드 |
| `README.md` | `/03-skills/` | 스킬 가이드 |
| `README.md` | `/04-subagents/` | 서브에이전트 가이드 |
| `README.md` | `/05-mcp/` | MCP 가이드 |
| `README.md` | `/06-hooks/` | 훅 가이드 |
| `README.md` | `/07-plugins/` | 플러그인 가이드 |
| `README.md` | `/08-checkpoints/` | 체크포인트 가이드 |
| `README.md` | `/09-advanced-features/` | 고급 기능 가이드 |
| `README.md` | `/10-cli/` | CLI 가이드 |

---

## 전체 파일 트리

```
claude-howto/
├── README.md                                    # Main overview
├── INDEX.md                                     # This file
├── QUICK_REFERENCE.md                           # Quick reference card
├── claude_concepts_guide.md                     # Original guide
│
├── 01-slash-commands/                           # Slash Commands
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # Memory
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # Skills
│   ├── code-review-specialist/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # Subagents
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # MCP Protocol
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # Hooks
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # Plugins
│   ├── pr-review/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── review-pr.md
│   │   │   ├── check-security.md
│   │   │   └── check-tests.md
│   │   ├── agents/
│   │   │   ├── security-reviewer.md
│   │   │   ├── test-checker.md
│   │   │   └── performance-analyzer.md
│   │   ├── mcp/
│   │   │   └── github-config.json
│   │   ├── hooks/
│   │   │   └── pre-review.js
│   │   └── README.md
│   ├── devops-automation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── deploy.md
│   │   │   ├── rollback.md
│   │   │   ├── status.md
│   │   │   └── incident.md
│   │   ├── agents/
│   │   │   ├── deployment-specialist.md
│   │   │   ├── incident-commander.md
│   │   │   └── alert-analyzer.md
│   │   ├── mcp/
│   │   │   └── kubernetes-config.json
│   │   ├── hooks/
│   │   │   ├── pre-deploy.js
│   │   │   └── post-deploy.js
│   │   ├── scripts/
│   │   │   ├── deploy.sh
│   │   │   ├── rollback.sh
│   │   │   └── health-check.sh
│   │   └── README.md
│   ├── documentation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── generate-api-docs.md
│   │   │   ├── generate-readme.md
│   │   │   ├── sync-docs.md
│   │   │   └── validate-docs.md
│   │   ├── agents/
│   │   │   ├── api-documenter.md
│   │   │   ├── code-commentator.md
│   │   │   └── example-generator.md
│   │   ├── mcp/
│   │   │   └── github-docs-config.json
│   │   ├── templates/
│   │   │   ├── api-endpoint.md
│   │   │   ├── function-docs.md
│   │   │   └── adr-template.md
│   │   └── README.md
│   └── README.md
│
├── 08-checkpoints/                              # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # Advanced Features
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # CLI Usage
    └── README.md
```

---

## 사용 사례별 빠른 시작

### 코드 품질과 리뷰
```bash
# Install slash command
cp 01-slash-commands/optimize.md .claude/commands/

# Install subagent
cp 04-subagents/code-reviewer.md .claude/agents/

# Install skill
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Or install complete plugin
claude --plugin-dir ./07-plugins/pr-review
```

### DevOps와 배포
```bash
# Install plugin (includes everything)
claude --plugin-dir ./07-plugins/devops-automation
```

### 문서화
```bash
# Install slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Install subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# Install skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Or install complete plugin
claude --plugin-dir ./07-plugins/documentation
```

### 팀 표준
```bash
# Set up project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Edit to match your team's standards
```

### 외부 연동
```bash
# Set environment variables
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
export DATABASE_URL="postgresql://..."
export SLACK_BOT_TOKEN="your-slack-bot-token"
export SLACK_TEAM_ID="T0000000000"

# Install MCP config (project scope)
cp 05-mcp/multi-mcp.json .mcp.json
```

### 자동화와 검증
```bash
# Install hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Configure hooks in settings (~/.claude/settings.json)
# See 06-hooks/README.md
```

### 안전한 실험
```bash
# Checkpoints are created automatically with every user prompt
# To rewind: press Esc+Esc or use /rewind
# Then choose what to restore from the rewind menu

# See 08-checkpoints/README.md for examples
```

### 고급 워크플로
```bash
# Configure advanced features
# See 09-advanced-features/config-examples.json

# Use planning mode
/plan Implement feature X

# Use permission modes
claude --permission-mode plan          # For code review (read-only)
claude --permission-mode acceptEdits   # Auto-accept edits
claude --permission-mode auto          # Auto-approve safe actions

# Run in headless mode for CI/CD
claude -p "Run tests and report results"

# Run background tasks
Run tests in background

# See 09-advanced-features/README.md for complete guide
```

---

## 기능 커버리지 매트릭스

| 카테고리 | 커맨드 | 에이전트 | MCP | 훅 | 스크립트 | 템플릿 | 문서 | 이미지 | 합계 |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **01 슬래시 커맨드** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 메모리** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 스킬** | - | - | - | - | 5 | 7 | 11 | - | **23** |
| **04 서브에이전트** | - | 9 | - | - | - | - | 1 | - | **10** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 훅** | - | - | - | 11 | - | - | 1 | - | **12** |
| **07 플러그인** | 11 | 9 | 3 | 3 | 3 | 3 | 7 | - | **39** |
| **08 체크포인트** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 고급 기능** | - | - | - | - | 1 | 1 | 2 | - | **4** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## 학습 경로

### 초급 (1주차)
1. ✅ `README.md` 읽기
2. ✅ 슬래시 커맨드 1~2개 설치
3. ✅ 프로젝트 메모리 파일 만들기
4. ✅ 기본 명령 사용해 보기

### 중급 (2~3주차)
1. ✅ GitHub MCP 설정
2. ✅ 서브에이전트 설치
3. ✅ 작업 위임 시도
4. ✅ 스킬 설치

### 고급 (4주차 이후)
1. ✅ 완성된 플러그인 설치
2. ✅ 사용자 정의 슬래시 커맨드 만들기
3. ✅ 사용자 정의 서브에이전트 만들기
4. ✅ 사용자 정의 스킬 만들기
5. ✅ 직접 플러그인 제작

### 전문가 (5주차 이후)
1. ✅ 자동화용 훅 설정
2. ✅ 실험을 위한 체크포인트 활용
3. ✅ 플랜 모드 구성
4. ✅ 권한 모드 효과적으로 사용
5. ✅ CI/CD용 헤드리스 모드 설정
6. ✅ 세션 관리 완전 습득

---

## 키워드 검색

### 성능
- `01-slash-commands/optimize.md` - 성능 분석
- `04-subagents/code-reviewer.md` - 성능 리뷰
- `03-skills/code-review-specialist/` - 성능 지표
- `07-plugins/pr-review/agents/performance-analyzer.md` - 성능 전문가

### 보안
- `04-subagents/secure-reviewer.md` - 보안 리뷰
- `03-skills/code-review-specialist/` - 보안 분석
- `07-plugins/pr-review/` - 보안 점검

### 테스트
- `04-subagents/test-engineer.md` - 테스트 엔지니어
- `07-plugins/pr-review/commands/check-tests.md` - 테스트 커버리지

### 문서화
- `01-slash-commands/generate-api-docs.md` - API 문서 커맨드
- `04-subagents/documentation-writer.md` - 문서 작성 에이전트
- `03-skills/doc-generator/` - 문서 생성 스킬
- `07-plugins/documentation/` - 완성된 문서 플러그인

### 배포
- `07-plugins/devops-automation/` - 완성된 DevOps 솔루션

### 자동화
- `06-hooks/` - 이벤트 기반 자동화
- `06-hooks/pre-commit.sh` - 커밋 전 자동화
- `06-hooks/format-code.sh` - 자동 포매팅
- `09-advanced-features/` - CI/CD용 헤드리스 모드

### 검증
- `06-hooks/security-scan.sh` - 보안 검증
- `06-hooks/validate-prompt.sh` - 프롬프트 검증

### 실험
- `08-checkpoints/` - 되감기를 활용한 안전한 실험
- `08-checkpoints/checkpoint-examples.md` - 실제 사례

### 계획
- `09-advanced-features/planning-mode-examples.md` - 플랜 모드 예제
- `09-advanced-features/README.md` - 확장 사고

### 구성
- `09-advanced-features/config-examples.json` - 구성 예제

---

## 참고 사항

- 모든 예제는 바로 사용할 수 있습니다
- 자신의 필요에 맞게 수정하세요
- 예제는 Claude Code 모범 사례를 따릅니다
- 각 카테고리에는 상세한 안내가 담긴 자체 README가 있습니다
- 스크립트에는 적절한 오류 처리가 포함되어 있습니다
- 템플릿은 자유롭게 커스터마이즈할 수 있습니다

---

## 기여하기

예제를 더 추가하고 싶으신가요? 다음 구조를 따르세요.
1. 적절한 하위 디렉터리를 만듭니다
2. 사용법을 담은 README.md를 포함합니다
3. 이름 규칙을 따릅니다
4. 충분히 테스트합니다
5. 이 색인을 갱신합니다

---

**최종 업데이트**: 2026년 10월 18일
**Claude Code 버전**: 2.1.302
**출처**:
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/workflows#set-a-size-guideline
- https://code.claude.com/docs/en/memory#agents-md
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/permission-modes
- https://github.com/anthropics/claude-code/releases/tag/v2.1.153
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/plugins/install
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/chrome
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
**전체 예제**: 100개 이상 파일
**카테고리**: 10개 기능
**훅**: 11개 자동화 스크립트
**구성 예제**: 10개 이상 시나리오
**바로 사용 가능**: 모든 예제
