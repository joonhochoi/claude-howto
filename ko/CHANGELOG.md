<!-- i18n-source: CHANGELOG.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

# 변경 이력

## [v2.1.245] — 2026-08-25

### Claude Code v2.1.245 기준 문서 동기화

Claude Code가 v2.1.235(2026-08-19)에서 **v2.1.245**(2026-08-25)로 이동했습니다 — 릴리스 10건입니다.
이 항목은 해당 동기화를 기록합니다.

> **참고**: 이 변경 이력에는 v2.1.233·v2.1.235 동기화(커밋 `deb7e5c`, `da6e09e`) 항목이 없습니다.
> 두 커밋은 변경 이력 항목 없이 저장소에 반영되었습니다. 이 공백은 재구성한 날짜로 소급
> 작성하지 않고 여기에 기록합니다.

### 수정

- **버전 최신성 주장이 낡았고 서로 모순되었습니다** — 루트
  `README.md`는 한 곳에서 `v2.1.235`, 다른 곳에서 `v2.1.220 (July 2026)`이라고 적었고,
  이 변경 이력의 최상단 항목도 여전히 v2.1.220을 현재
  Claude Code 릴리스로 불렀습니다. 이제 모두 v2.1.245로 표기합니다.
- **훅 기본 타임아웃**을 60초에서 **600**초로 정정했습니다 —
  `command`, `http`, `mcp_tool` 기준이며(`prompt`는 30, `agent`는 60),
  이벤트별 재정의도 문서화했습니다.
- **스킬 우선순위**를 **enterprise > personal > project**로 정정했습니다. 레슨에서는
  project와 personal이 뒤바뀌어 자체 퀴즈와 모순되었습니다.
- **메모리 파일은 덮어쓰지 않고 연결됩니다** — `02-memory/README.md`에 남아 있던
  "루트 CLAUDE.md를 덮어쓴다"는 두 문구를 교체했습니다.
- **`SECURITY.md`**가 더 이상 "1.x 릴리스" 지원을 표방하지 않습니다.
- **`STYLE_GUIDE.md`**가 더 이상 낡은 푸터를 예시로 가르치지 않습니다.
- 채점 자료(`lesson-quiz`, `self-assessment` 스킬)를 채점 대상 레슨과 다시 맞췄습니다:
  훅 이벤트 31개, 훅 유형 5개, 되감기 옵션 6개, 권한 모드 6개, 임포트 깊이 4입니다.

### 추가

- **WebSocket(`ws`) MCP 전송** — 네 번째 전송 방식이며
  `.mcp.json` 또는 `claude mcp add-json`으로 구성합니다.
- **`Concise` 출력 스타일** — 다섯 번째 내장 스타일(v2.1.237)입니다.
- **새 설정 키** — `modelPicker`, `promptCacheTtl`,
  `subagentPromptCacheTtl`, `modelPricing`, `keybindingFlavor`.
- **`ANTHROPIC_DEFAULT_MODEL`** 환경변수(v2.1.236).
- **`/design`** — 디자인 캔버스 연구 프리뷰입니다.
- **`notify_when_idle`** — 세션 간 `SendMessage`에서 지원합니다(v2.1.236).
- **플러그인 매니페스트 필드** — `workflows`, `channels`, `dependencies` 및
  관련 CLI 추가분입니다.

### 변경

- **Remote Control**이 연구 프리뷰를 종료했습니다. 이제
  `claude remote-control`을 실행하는 머신이 Claude 앱에 기기 카드로 표시됩니다.
- **`Ctrl+L`**은 화면을 지우는 대신 다시 그립니다(v2.1.238).
- **플러그인 `commands/`**는 레거시로 표시되었고, `skills/`가 현재 권장 방식입니다.

## [v2.1.220-r2] — 2026-08-04

### Claude Code v2.1.220 기준 정확성 점검 (업스트림 버전 변경 없음)

v2.1.220(2026-07-25)이 여전히 현재 Claude Code 릴리스이므로, 이 항목은 버전 동기화가 아니라
**내부 정정**을 기록합니다. 공식 문서와 대조한 감사에서 업스트림 기능 누락은 발견되지
않았습니다 — v2.1.218~v2.1.220의 모든 기능이 이미 문서화되어 있었습니다. 대신 발견된 것은
깨진 예제 코드, 파일마다 서로 어긋난 개수와 이름, 메타데이터 드리프트였습니다.

### 수정

- **`06-hooks/pre-commit.sh`가 실제로는 커밋을 차단하지 못했습니다** — 스크립트가
  "Commit blocked."를 출력한 뒤 네 곳에서 `exit 1`을 호출했습니다. 이 저장소의 자체
  종료 코드 표(`06-hooks/README.md`)에 따르면 exit 1은 *비차단* 오류이므로 커밋은
  그대로 진행되었고, 차단되는 것은 exit 2뿐입니다. 네 곳 모두 이제 `exit 2`로 끝내고
  사유를 stderr에 기록하는데, Claude Code가 차단 사유를 읽는 곳이 바로 stderr입니다.
- **`06-hooks/dependency-check.sh`가 실행되지 않았습니다** — `$1`에서 대상을 읽었지만
  훅은 stdin으로 JSON을 받으므로 경로가 항상 비어 있었고 스크립트는 즉시 종료되었습니다.
  이제 `format-code.sh`와 동일하게 stdin에서 `file_path`를 파싱합니다.
- **`claude_concepts_guide.md`의 중첩 서브에이전트 깊이가 5로 적혀 있었습니다** — "v2.1.172 기준
  최대 5단계"라고 서술해, 다른 네 파일에 이미 문서화된 깊이 3 기본값(v2.1.219)과
  모순되었습니다. 현재 동작을 먼저 제시하고 `04-subagents/README.md`와 같은 세 시기
  이력 주석을 붙이는 방식으로 다시 썼습니다.
- **훅 이벤트 개수가 다섯 파일에서 29였습니다** — `README.md`, `CATALOG.md`,
  `QUICK_REFERENCE.md`(4곳), `INDEX.md`, `resources.md`가 모두 29라고 적었지만 올바른
  수치는 **31**이며 공식 훅 목록과 이름 단위로 대조해 확인했습니다. 이전 동기화는 두 파일만
  고치고 나머지를 놓쳤습니다. `README.md`의 이벤트 목록은 이름 25개만 나열했고
  `INDEX.md`는 29개만 나열했는데, 이제 둘 다 31개를 모두 나열합니다.
- **`/less-permission-prompts`는 실제 커맨드가 아닙니다** — 내장 커맨드는
  `/fewer-permission-prompts`입니다. `CATALOG.md`는 한 파일에서 *두 이름을 모두* 썼습니다.
- **`/fork`와 `/subtask`가 의미가 뒤바뀐 채 문서화되어 있었습니다** — 두 커맨드는 v2.1.212에서
  역할이 교환되었습니다. 이제 `/fork`는 대화를 새 독립 백그라운드 세션으로 복사하고,
  포크 서브에이전트 동작은 `/subtask`로 옮겨졌는데 이 커맨드는 저장소에 아예 없었습니다.
  네 파일에서 정정하고 추가했습니다.
- **`08-checkpoints/README.md`가 `cleanupPeriodDays`를 유일한 체크포인트 설정이라고 했습니다** —
  `fileCheckpointingEnabled`(기본 `true`)도 존재하며,
  `CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING`과 체크포인트 100개 보존 상한도 있습니다.
  저장소 자체의 `config-examples.json`이 이미 존재하지 않는다고 한 키를 쓰고 있었습니다.
- **`03-skills/refactor/SKILL.md`가 `refactor/`에 있으면서 `name: code-refactor`를 선언했습니다** —
  지난 동기화에서 `doc-generator`에 대해 고친 것과 같은 결함입니다. 영어본에서 이름을 바꾸고
  `ja/`, `zh/`, `uk/`, `vi/`에 미러링했습니다.
- **`03-skills/README.md`가 스킬 우선순위를 모순되게 두 번 적었습니다** — 한 곳에서는
  "enterprise > personal > project", 다른 곳에서는 "기본적으로 project 우선"이었습니다.
  이제 일관되게 **enterprise > project > personal**입니다.
- **`claude-md` 스킬이 AGENTS.md를 잘못 설명했습니다** — 에이전트 정의 형식이라고 불렀습니다.
  AGENTS.md는 도구 간 프로젝트 컨텍스트 파일이며 Claude Code는 이를 **직접 읽지 않습니다**.
  `@AGENTS.md`로 임포트하거나 심볼릭 링크해야 합니다.
- **`02-memory/directory-api-CLAUDE.md`가 루트 CLAUDE.md를 "덮어쓴다"고 했습니다** —
  메모리 파일은 연결될 뿐 절대 덮어쓰지 않습니다.
- **`INDEX.md`가 `auto`와 `dontAsk`를 반대로 설명했습니다** — `dontAsk`를 관대한 모드
  ("위험한 것만 빼고 모두 수락")로 썼지만 이는 가장 제한적인 모드입니다:
  사전 승인되지 않은 것은 자동 거부합니다. 공식 정의에 맞게 정정했습니다.
- **`permissions.mode`는 설정 키가 아닙니다** — `09-advanced-features/README.md`와
  `claude_concepts_guide.md`의 설정 예시 네 개가 이 키를 (이미 대체된 값 `default`와 함께)
  사용했습니다. 이제 모두 `permissions.defaultMode: "manual"`을 씁니다.
- **`09-advanced-features/config-examples.json`에 Opus 5가 없었습니다** — 세 개의 "최고 성능"
  프로필에 여전히 `claude-opus-4-8`을 썼는데, Opus 5는 v2.1.219부터 기본 Opus입니다.
- **`05-mcp/database-mcp.json`이 자격 증명을 하드코딩했습니다** —
  `postgresql://user:***@localhost/mydb`로, 모듈 자체의 "자격 증명을 하드코딩하지 말 것" 규칙과
  모순되었습니다. 이제 `${DATABASE_URL}`입니다.
- **`05-mcp/README.md`가 MCP 스코프는 설명하면서 `--scope` 플래그는 다루지 않았습니다** —
  독자가 스코프를 실제로 선택할 방법이 없었습니다. 예제와 함께 추가했습니다.
- **`/output-style`이 지원 중단으로 표기되어 있었습니다** — 이 커맨드는 v2.1.91에서 *제거*되었습니다.
  출력 스타일은 `/config` 또는 `outputStyle` 설정으로 계속 사용할 수 있습니다.
- **훅 `permissionDecision`에 `defer`가 빠져 있었습니다** — 허용 값은
  `allow`, `deny`, `ask`, `defer`이며 우선순위는 `deny` > `defer` > `ask` > `allow`입니다.
- **컨텍스트 추적 훅이 128k 창을 가정했습니다** — 현재 Claude 모델 중 그런 창을 가진 모델은 없습니다.
  기본값을 1M으로 올리고 Haiku 4.5의 200k를 명시했습니다.
- **`claude_concepts_guide.md`의 로컬 메모리 경로가 틀렸습니다** —
  `.claude/local/CLAUDE.md`를 `./CLAUDE.local.md`로 정정했습니다.
- **`03-skills/doc-generator/SKILL.md`의 깨진 펜스** — 바깥 ```` ```markdown ````
  블록이 일찍 닫히면서 닫히지 않은 펜스가 남아 예제 절반이 실제 마크다운으로 렌더링되었습니다.
  이제 네 개 백틱 바깥 펜스를 씁니다. `check_markdown_rendering.py`가 README 파일만
  검사하기 때문에 어느 검증기도 이를 잡지 못했습니다.
- **커맨드 템플릿 세 개의 스킬 이름이 유효하지 않았습니다** — `Documentation Refactor`,
  `Setup CI/CD Pipeline`, `Expand Unit Tests`는 유효한 `name:` 값(소문자/하이픈만 허용)이 아니어서
  README 안내대로 `.claude/skills/`에 복사하면 실패했을 것입니다. 비표준 `tags:` 필드도 제거했습니다.
- **플러그인 에이전트 아홉 개가 소문자 도구 이름을 썼습니다**(`read, grep, bash`) 반면
  `04-subagents/` 템플릿은 정규 표기 `Read, Grep, Bash`를 썼습니다. 통일했습니다.
- **다섯 파일의 "Claude Code 1.0+" 요구 사항** — 2.1+로 올렸습니다.
- **집계 오류** — `CATALOG.md`의 요약 표가 합이 맞지 않았고 *게다가*
  Examples 개수 세 개가 틀렸습니다(Subagents 11→9, MCP 8→4, Hooks 8→11).
  `INDEX.md`는 Plugins(27→39), Skills(21→23), Hooks(9→12), Subagents(9→10),
  Advanced(3→4)를 과소 집계했고, 훅 스크립트 세 개와 `setup-auto-mode-permissions.py`를
  누락했으며 훅 이벤트 세 개를 잘못 표기했습니다. 모두 파일 트리에서 다시 세었습니다.
- **`CONTRIBUTING.md`가 "검사 네 개"라고 했습니다** — 다섯 개입니다.
- **문서화되지 않은 서브에이전트 템플릿 두 개** — `clean-code-reviewer.md`와
  `performance-optimizer.md`가 디스크에는 있었지만 `04-subagents/README.md`의 예제 목록에도
  파일 트리에도 없었습니다.
- **`resources.md`의 Mermaid 다이어그램이 가이드 밖 팔레트를 썼습니다** — 필수 `stroke`/`color`와
  함께 `STYLE_GUIDE.md`의 다섯 색으로 재매핑했습니다.
- **메타데이터 푸터** — 61개 파일이 레거시 `Last Updated`만 있는 푸터를 쓰거나 아예 없었습니다.
  이제 모두 전체 블록을 갖춥니다. 모듈 README 네 개에는 `Compatible Models` 줄이 빠져 있었고
  `02-memory/README.md`는 ISO 형식 날짜와 함께 v2.1.217에 머물러 있었습니다. 범위 내
  마크다운 87개가 이제 모두 **2.1.220**을 보고합니다.
- **소소한 수정** — `session-end.sh`에 명시적 `exit 0`; (실제 문법이 아닌) `# Hook: Event:Matcher`
  축약 표기를 스크립트 네 개에서 다시 서술; MCP 예시 설정 네 개에 `"type": "stdio"` 추가;
  한 곳에서는 PR 42개, 다른 곳에서는 47개로 보고하던 계산 예제 수정.

## [v2.1.220] — 2026-07-29

### Claude Code v2.1.220 동기화

튜토리얼 커버리지를 v2.1.217 기준선(2026-07-22 동기화)에서 v2.1.220으로 올립니다 —
연속 릴리스 세 건(v2.1.218, v2.1.219, v2.1.220)이며 건너뛴 버전은 없습니다.
이번 동기화의 대부분은 v2.1.219가 이끕니다: Claude Opus 5를 추가했고, 직전 동기화가 막
문서화한 중첩 서브에이전트 기본값을 뒤집었습니다.

### 수정

- **중첩 서브에이전트 기본값이 다시 뒤집혔습니다(v2.1.219)** —
  `04-subagents/README.md`, `CATALOG.md`, `10-cli/README.md`, `QUICK_REFERENCE.md`의 다섯 곳이
  중첩 생성이 기본적으로 비활성이라고 적었습니다. 이는 v2.1.217~v2.1.218에만 맞는 설명이었습니다.
  v2.1.219는 기본값을 **깊이 3**으로 두었고, 이제 `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`은
  중첩을 켜는 것이 아니라 *끕니다*. 다섯 곳 모두 현재 동작을 먼저 제시하고 동일한 세 시기
  이력 주석(v2.1.172~v2.1.216은 기본 중첩 최대 5단계이며 변경 불가, v2.1.217은 깊이 1 옵트인,
  v2.1.219는 기본값 3)을 달아 다음 번 뒤집힘에도 완만하게 대응하도록 했습니다.
- **Opus 4.8을 기본 Opus 모델로 명시** — `10-cli/README.md`는 "Opus 4.8이 Max, Team Premium,
  Enterprise 종량제, Claude API에서 계속 기본"이라고 적었습니다. v2.1.219 기준으로는
  **Claude Opus 5**(`claude-opus-5`, 1M 컨텍스트, 기본 effort `high`)이며, 이 모델은 저장소의
  모든 모델 표에서 빠져 있었습니다. `10-cli`와 `claude_concepts_guide.md` 모델 표, 18개
  `Compatible Models` 푸터 전체, effort 수준 열거 약 20곳에 추가했습니다. Microsoft Foundry는
  여전히 `opus` 별칭을 Opus 4.6으로 해석합니다.
- **패스트 모드 모델 목록** — `/fast`가 이제 **Opus 5와 Opus 4.8**에 적용되고
  Opus 4.7은 제외되었습니다(v2.1.219). `10-cli/README.md`에서 Opus 4.6의 패스트 모드 활성화를
  현재형으로 안내하던 문장도 정정했습니다.
- **오토 모드 자격 자기모순** — `09-advanced-features/README.md`가 "모든 플랜에서 사용 가능"과
  "Team, Enterprise 또는 API" / "Anthropic API 전용"을 함께 적었습니다. 문서화된 네 가지
  요건(플랜/조직/모델/제공자)으로 다시 썼습니다. 오토 모드는 **모든 플랜**에서 사용 가능하며
  Team/Enterprise는 기본 활성이고 관리자가 `permissions.disableAutoMode`로 옵트-*아웃*합니다 —
  이 파일은 앞서 Owner 옵트-*인*으로 설명했습니다.
- **낡은 오토 모드 옵트인 안내** — `CATALOG.md`가 여전히 서드파티 제공자에서
  `CLAUDE_CODE_ENABLE_AUTO_MODE=1`을 설정하라고 했습니다. 이 요건은 v2.1.207에서 제거되었고,
  변수는 호환성을 위해 받아들여질 뿐 효과가 없습니다.
- **훅 이벤트 개수 불일치** — `LEARNING-ROADMAP.md`와 `claude_concepts_guide.md`는 29,
  `06-hooks/README.md`는 30(현재 31)이었습니다. 둘 다 31로 맞췄습니다.
  `claude_concepts_guide.md`의 이벤트 이름 표에는 새 `DirectoryAdded`와 함께
  `MessageDisplay`(v2.1.152부터 있던 기존 누락)도 빠져 있었는데, 이제 이벤트 목록이
  `06-hooks`와 동일합니다.
- **`doc-generator` 스킬 이름 불일치** — `03-skills/doc-generator/SKILL.md`가 `doc-generator/`에
  있으면서 `name: api-documentation-generator`를 선언해 모든 카탈로그·색인 항목과 모순되었습니다.
  영어본에서 이름을 바꾸고 `ja/`, `zh/`, `uk/`에 미러링했습니다.
- **낡은 "New Features (May 2026)" 제목** — 다시 낡을 수 없는 날짜 없는 제목으로
  `CATALOG.md`와 `resources.md`에서 바꾸고, `CATALOG.md`의 탐색 앵커도 그에 맞게 갱신했습니다.
- **레거시 `docs.anthropic.com` 링크** — `01-slash-commands/README.md`, `05-mcp/README.md`,
  `10-cli/README.md` 푸터에 남아 있던 링크 세 개를 `code.claude.com`으로 이전했습니다.
- **내장 기능을 가리는 스킬 예제** — `03-skills/README.md`가 커스텀 스킬 예제로
  `name: deep-research`를 썼는데, 이제 내장 `/deep-research`를 가립니다.
  `topic-research`로 이름을 바꾸고 `vi/`, `ja/`, `uk/`에 미러링했습니다.

### 추가

- **`DirectoryAdded` 훅(v2.1.219)** — `/add-dir` 또는 SDK의
  `register_repo_root` 제어 요청이 세션 중간에 새 작업 디렉터리를 등록한 뒤 발생합니다.
  `06-hooks/README.md` 이벤트 표에 추가했습니다(개수 30 → 31).
- **`/deep-research`는 명시 호출 전용입니다(v2.1.218)** — Claude가 스스로 실행하지 않습니다.
  번들 스킬 표에 추가했습니다.
- **`/code-review`는 백그라운드 서브에이전트로 실행됩니다(v2.1.218)** — 리뷰 작업이
  더 이상 대화를 채우지 않고, 쌓인 슬래시 커맨드가 여전히 리뷰 대상입니다.
  `03-skills/README.md`와 `CATALOG.md`에 문서화했습니다.
- **포크 스킬은 기본적으로 백그라운드에서 실행됩니다(v2.1.218)** — `context: fork` 스킬은
  기본값이 `background: true`이며 `false`로 옵트아웃합니다. `background` 프론트매터 행,
  대응하는 YAML 예시 줄, 기본값에 대한 명시적 서술을 추가해 `background: true`가 백그라운드를
  *강제*하는 `04-subagents`와 모순되어 읽히지 않도록 했습니다.
- **에이전트 프론트매터 훅에는 워크스페이스 신뢰가 필요합니다(v2.1.218)** — 프로젝트 서브에이전트의
  훅은 에이전트 파일이 있는 폴더에 대해 워크스페이스 신뢰가 수락된 뒤에만 실행됩니다.
- **동적 워크플로 크기 가이드라인(v2.1.219)** — 워크플로는 이제 기본적으로 중간 가이드라인
  (에이전트 15개 미만 목표)을 쓰며, `/config`의 **Dynamic workflow size** 또는 새 설정 키
  `workflowSizeGuideline`으로 선택할 수 있습니다.
- **`sandbox.network.strictAllowlist`(v2.1.219)** — 샌드박스 명령에 대해 허용 목록 밖 호스트를
  묻지 않고 거부합니다.
- **MCP 오류 노출(v2.1.219)** — `claude mcp list`와 `/mcp`가 연결 실패 시 HTTP 상태와 오류 텍스트를
  보고하고, 설정 값의 앞뒤 공백이 숨겨져 있으면 경고하며, 헤드리스 실행은 stream-json init
  이벤트에 `mcp_server_errors`를 노출합니다. `05-mcp/README.md`에 문제 해결 안내로 추가했습니다.
- **stream-json의 중첩 서브에이전트 전달(v2.1.219)** — `--forward-subagent-text`가 설정되면
  깊이 2 이상의 서브에이전트도 나타나며, 이를 생성한 `Agent` `tool_use` id로 키가 잡힙니다.
- **프론트매터 불리언이 더 많은 값을 받습니다(v2.1.218)** — `true`/`false` 외에 `yes`/`no`,
  `on`/`off`, `1`/`0`을 대소문자 구분 없이 허용합니다.
- **에이전트 이름에서 `:` 거부(v2.1.218)** — 플러그인 네임스페이스용으로 예약되었습니다.
- **오토·플랜 모드가 분류기에 더 많이 위임합니다(v2.1.218)** — `rm -rf /`와
  `rm -rf ~`(명령·프로세스 치환 내부 포함)는 이제 권한 대화상자를 띄우지 않고 분류기가 판정하며,
  오토가 켜진 플랜 모드는 정적 분석기가 읽기 전용임을 증명할 수 없는 Bash 명령에 대해
  더 이상 묻지 않습니다(`useAutoModeDuringPlan`, 기본 켜짐).
- **Opus 5 안전 분류기 폴백(v2.1.219)** — 사이버보안 플래그가 붙은 요청은 Opus 4.8에서 다시 실행되고,
  생물학 플래그가 붙은 요청은 거부로 끝납니다(Opus 5는 자체 생물학 분류기를 쓰며 폴백이 없음).
  이 저장소의 보안 리뷰 서브에이전트와 플러그인 템플릿을 쓰는 독자에게 해당되며,
  펜테스트/CTF 작업에서 자주 발동합니다.

## [v2.1.217] — 2026-07-22

### Claude Code v2.1.217 동기화

튜토리얼 커버리지를 v2.1.212 기준선(2026-07-18 동기화)에서 v2.1.217로 올립니다
(v2.1.213은 업스트림에서 건너뛰었습니다 — 변경 이력과 GitHub 릴리스 모두 2.1.212 → 2.1.214로
점프합니다). 저장소 내부 정확성 감사도 함께 반영합니다.

### 수정

- **중첩 서브에이전트 생성 주장이 뒤집혔습니다(v2.1.217)** — `04-subagents/README.md`와
  `CATALOG.md`가 "서브에이전트가 자체 서브에이전트를 최대 5단계까지 중첩 생성할 수 있다"를
  현재 동작으로 적었습니다(v2.1.172~v2.1.216에는 사실). v2.1.217 기준으로 이는 기본 꺼짐이며
  `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`로 옵트인합니다. 두 파일 모두 현재 동작을 먼저 제시하고
  과거 주석을 유지합니다.
- **낡은 `--enable-auto-mode` 플래그** — v2.1.111에서 제거되었고(오토 모드가 기본 `Shift+Tab`
  순환에 포함되었으며, 현재는 `--permission-mode auto`로 시작), `10-cli/README.md`가 여전히
  네 곳에서 이 플래그를 유효한 것처럼 제시했고 `QUICK_REFERENCE.md`는 세 곳에서 사용했습니다.
  일곱 곳 모두 `--permission-mode auto`로 갱신했습니다.
- **임포트 깊이 모순("5단계" vs "4홉")** — 2026-07-18 동기화에서 두 곳을 고친 뒤에도
  `02-memory/README.md`의 모범 사례 영역에 "5단계"가 두 곳 남아 있었습니다. 이제 둘 다
  "4홉"으로 읽히며 파일의 나머지와 일치합니다.
- **Sonnet 5가 빠진 모델 표** — `claude_concepts_guide.md`의 "Models & Reasoning Effort" 표가
  파일 자체 푸터에는 호환 모델로 적혀 있는 Claude Sonnet 5를 누락했습니다.
  Pro/Team Standard/Enterprise의 기본 행으로 추가했습니다.
- **`config-examples.json`의 조작된 스키마** — 예시 설정 11개 모두 실제 설정 스키마에 없는
  필드(`mode: "unrestricted"/"confirm"`, `planning.*`, `extendedThinking.*`, `headless.*`,
  `checkpoints.autoCheckpoint`)와 낡은 `claude-opus-4-7` 모델 ID를 썼습니다.
  실제 `settings.json` 키(`permissions.defaultMode`, `permissions.allow`/`deny`, `env`, `hooks`,
  `fileCheckpointingEnabled`, `sandbox.*`)와 현재 모델 ID를 쓰도록 다시 썼습니다.
- **`brand-voice` 스킬과 README 예제의 불일치** — 실제
  `03-skills/brand-voice/SKILL.md`(`name: brand-voice-consistency`, 사용자 호출 가능)가
  `03-skills/README.md`의 "Example 4" 설명(`name: brand-voice`, `user-invocable: false`)과
  모순되었습니다. 스킬 파일을 README의 배경 지식 구도에 맞췄습니다.
- **CLAUDE.md 길이 지침 충돌** — `03-skills/claude-md/SKILL.md`("<300줄, 이상적으로 <100")와
  `02-memory/README.md`("<500줄")가 어긋났습니다. 두 파일 모두 "몇백 줄 이하로 유지하고
  짧을수록 좋다"로 통일했습니다(공식 구체 한도는 없으며 두 수치 모두 편집상의 판단이었습니다).

### 추가

- **새 서브에이전트 상한(v2.1.217)** — 위의 중첩 깊이 제어와 함께 동시 실행 서브에이전트 상한
  (기본 20, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`)이 생겼습니다. `04-subagents/README.md`,
  `10-cli/README.md`, `QUICK_REFERENCE.md`에 문서화했습니다.
- **`--max-budget-usd`가 백그라운드 서브에이전트를 중단시킵니다(v2.1.217)** — 지출 상한이
  이전에는 새 생성만 막았지만, 이제 이미 실행 중인 백그라운드 서브에이전트도 중단합니다.
  `10-cli/README.md`에 문서화했습니다.
- **훅 `if:` 글롭 범위 축소(v2.1.214)** — 단일 세그먼트 `dir/**` 훅 `if:` 조건은 이제
  `<cwd>/dir`에만 일치합니다(임의 깊이는 `**/dir/**` 사용). deny/ask 권한 규칙은 영향받지 않습니다.
  `06-hooks/README.md`에 문서화했습니다.
- **SessionStart `"fork"` 소스(v2.1.214)** — 포크된 세션은 이제 `"resume"` 대신 소스 `"fork"`를
  보고합니다. `06-hooks/README.md`에 문서화했습니다.
- **`sandbox.filesystem.disabled`(v2.1.216)** — 네트워크 이그레스 제어는 유지하면서 파일 시스템
  격리를 건너뜁니다. `09-advanced-features/README.md`와 `10-cli/README.md`에 문서화했습니다.
- **`/rewind` 심볼릭·하드 링크 보호(v2.1.216)** — 추적 경로에서 심볼릭 링크나 하드 링크를 통해
  파일을 복원하거나 삭제하지 않으며, 건너뛴 경로 수를 보고합니다. `08-checkpoints/README.md`에
  문서화했습니다.
- **오토 메모리 `modified` 타임스탬프 + 비차단 `/memory` 편집기** — 메모리 파일 프론트매터의
  ISO `modified` 타임스탬프(v2.1.214)와, GUI 편집기가 열려 있는 동안 세션을 막지 않는
  `/memory`(v2.1.216)입니다. `02-memory/README.md`에 문서화했습니다.
- **CLI·설정 일괄(v2.1.214~v2.1.217)** — `emojiCompletionEnabled`, `FORCE_HYPERLINK=0`,
  `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH`, `--settings` 파일 2 MiB 상한, 권한 강화
  (Docker/Podman 데몬 리디렉션 플래그, `file -m`/`--magic-file`/`-f`/`--files-from`,
  1만 자 이상 명령)를 `10-cli/README.md`에 문서화했습니다. `/context`의 컨텍스트 창 초과 경고와
  `/compact` 실패가 이제 오류로 표시되는 것(v2.1.216)은 `01-slash-commands/README.md`에
  문서화했습니다.
- **`/verify`와 `/code-review`는 명시 호출 전용(v2.1.215)** — `03-skills/README.md`와
  `QUICK_REFERENCE.md`에 보충 설명을 넣었습니다. 저장소는 자동 호출을 주장한 적이 없습니다.

### 참고

- `QUICK_REFERENCE.md`의 `--enable-auto-mode` / `--permission-mode auto` 불일치는
  실제 CLI 레퍼런스에서 전자가 v2.1.111에 제거되었음을 확인한 뒤 후자로 확정했습니다.
- 번역 미러(`vi`/`ja`/`zh`/`uk`)에 대해 위 P0/P1 주장을 점검했습니다. `04-subagents/README.md`와
  `CATALOG.md` 번역본 대부분은 중첩 생성 기능보다 오래되었거나 해당 절을 담고 있지 않아
  미러 수정이 필요 없었습니다. `10-cli/README.md`의 `--max-budget-usd` 설명은 네 언어 모두에
  반영했습니다.

## [v2.1.212] — 2026-07-18

### Claude Code v2.1.212 동기화

튜토리얼 커버리지를 v2.1.206 기준선(2026-07-11 동기화)에서 v2.1.212로 올리고,
버전 델타와 무관하게 드러난 결함을 찾아낸 저장소 내부 정확성 감사도 함께 반영합니다.

### 수정

- **죽은 `#` 메모리 단축키 제거** — `02-memory/README.md`가 `#` 접두 빠른 메모리 추가 패턴을
  두 곳("Method 3"과 "Example 4" 설명)에서 작동하는 기능으로 문서화해, 맨 위 세 줄 아래의
  커맨드 표가 이미 `#`을 **중단됨**으로 표시한 것과 정면으로 모순되었습니다. 두 절 모두 제거하거나
  `/memory`와 대화형 메모리 요청을 가리키도록 다시 썼습니다.
- **Bedrock/Vertex/Foundry에서 오토 모드 옵트인 → 옵트아웃(v2.1.207)** — 오토 모드는 이제
  이들 제공자(및 로그인한 Claude 앱 게이트웨이 세션)에서 Sonnet 5, Opus 4.7/4.8, Fable 5에 대해
  기본 제공됩니다. `CLAUDE_CODE_ENABLE_AUTO_MODE` 옵트인 플래그는 v2.1.207부터 효과가 없습니다.
  `09-advanced-features/README.md`와 `10-cli/README.md`에서 수정했습니다.
- **`auto` 권한 모드를 "Research Preview"로 오표기** — 현재 공식 문서는 `auto`를 GA
  (모든 플랜에서 사용 가능하고 모델·제공자 자격만 조건)로 제시하며 프리뷰 기능이 아닙니다.
  `09-advanced-features/README.md`, `CATALOG.md`, `README.md`에서 정정했고, README의
  권한 모드 요약에는 빠져 있던 `auto` 행도 추가했습니다.
- **`/fork` / `/branch` 이력 정정** — 저장소는 "`/fork`가 v2.1.77에서 `/branch`로 이름이 바뀌었다
  (별칭 유지)"고 주장했습니다. 현재 문서는 이 둘이 서로 다른 현재 커맨드임을 보여줍니다:
  `/fork`는 대화를 상속하는 백그라운드 서브에이전트를 만들고, `/branch`는 제자리에서 복사본으로
  전환합니다. 두 커맨드가 하나의 별칭 커맨드였던 것은 v2.1.77부터 v2.1.161까지입니다.
  `01-slash-commands/README.md`와 `09-advanced-features/README.md`에서 수정했습니다.
- **`effort` 프론트매터 열거 완성** — `04-subagents/README.md`가 4단계
  (`low`/`medium`/`high`/`max`)만 나열해 `xhigh`가 빠졌는데, 이 열거를 문서화한 다른 모든 파일에는
  있습니다.
- **번들 스킬 개수 정합** — `CATALOG.md`의 요약 표는 자체 10행 상세 표와 달리 "bundled 9"라고
  했습니다. 10(총 16)으로 정정했습니다.
- **`INDEX.md` 기능 커버리지 매트릭스 전면 재계산** — 헤더는 "파일 16개", Skills 행은 같은
  범주에 "28"을 주장했지만 둘 다 문서화된 6개 스킬의 실제 파일 21개와 맞지 않았습니다.
  Plugins 행도 합이 36인데 40으로 표시되었습니다. 모든 행을 손으로 다시 세었고, 이제 Skills 행은
  `5 | 9 | 7`(**21**), Plugins 행은 `11 | 9 | 3 | 3 | 3 | 3 | 7`(**39**)로 읽히며 모든 행의
  Total이 자기 셀의 합과 같습니다.
- **낡은 `2.1.160` 푸터 무리 상향** — 다섯 파일(`08-checkpoints/checkpoint-examples.md`,
  `09-advanced-features/planning-mode-examples.md`, `07-plugins/*/README.md` 예제 패키지 파일 세 개)이
  2026년 6월 푸터를 유지하고 있었으나 버전별 내용 드리프트는 없어 2.1.212로 올렸습니다.
- **`QUICK_REFERENCE.md` 전면 재동기화** — `2.1.160`/6월 2일 기준으로 52버전 뒤처져 있었습니다.
  권한 모드 블록을 `manual`(이전 `default`)로 갱신하고, Compatible Models에 Sonnet 5를 추가했으며,
  "New Features (May 2026)" 절의 제목을 바꾸고 내용을 새로 고쳤습니다.
- **`02-memory/README.md` 메모리 계층 절 재작성** — 조작된 8계층 엄격 우선순위 모델을 검증된
  구조로 교체했습니다: CLAUDE.md 파일과 규칙은 컨텍스트에 연결되며(우선순위로 선택되지 않음)
  `managed-settings.d/`는 CLAUDE.md가 아니라 `settings.json` 메커니즘입니다. Memory Architecture
  다이어그램도 정정했습니다 — 이전에는 claude.ai의 24시간 합성 주기와 Claude Code의 연속 오토
  메모리를 혼동했습니다.

### 추가

- **서브에이전트 출력 스캔(v2.1.210)** — Claude Code가 서브에이전트 보고서에서 프롬프트 인젝션
  패턴(가짜 시스템 태그, 조작된 대화 턴, 권한 우회 언급)을 스캔해 무력화합니다.
  `04-subagents/README.md`의 새 하위 절에 문서화했습니다.
- **세션 전역 생성 상한(v2.1.212)** — WebSearch 호출(`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`)과
  서브에이전트 생성(`CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`, `/clear`로 초기화)에 세션당
  기본 200회 상한입니다. `09-advanced-features/README.md`, `04-subagents/README.md`,
  `10-cli/README.md`에 문서화했습니다.
- **MCP 장기 실행 도구 자동 백그라운드 전환(v2.1.212)** — 2분을 넘는 MCP 도구 호출이 세션을
  막지 않고 자동으로 백그라운드로 전환됩니다. `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`로 구성합니다.
  `05-mcp/README.md`에 문서화했습니다.
- **`claude auto-mode reset`과 `/resume` 선택기(v2.1.212)** — 새 CLI 하위 커맨드가 기본 오토 모드
  구성을 복원하고, 인자 없는 `/resume`은 과거 세션(제거된 세션 포함) 선택기를 열어 백그라운드
  세션으로 재개합니다. `09-advanced-features/README.md`, `01-slash-commands/README.md`,
  `10-cli/README.md`에 문서화했습니다.
- **스크린 리더 모드(v2.1.208)** — `--ax-screen-reader`, `CLAUDE_AX_SCREEN_READER=1`,
  `"axScreenReader": true`로 옵트인하는 평문 렌더링입니다. `09-advanced-features/README.md`와
  `10-cli/README.md`에 문서화했습니다.
- **Task 도구 `mode` 매개변수 지원 중단(v2.1.212)** — `04-subagents/README.md`에 명시했습니다:
  서브에이전트는 이제 기본적으로 부모 세션의 권한 모드를 상속하며, Task 도구의 호출별 `mode`
  매개변수는 무시됩니다.

### 알려진 공백 (이번 동기화에서 미수정, 보류)

- `03-skills/.claude/skills/blog-draft/`는 gitignore된 로컬 테스트 스크래치(`03-skills/.gitignore`의
  `# Local skill testing`)이며 `03-skills/blog-draft/`의 추적된 중복이 아닙니다 — 조치 불필요로
  확인했습니다.

## [v2.1.160] — 2026-06-02

### Claude Code v2.1.160 동기화

튜토리얼 커버리지를 Claude Code v2.1.160 릴리스로 올립니다. 중간의 v2.1.156 동기화
(Claude Opus 4.8, #129)는 문서에는 적용되었지만 별도 변경 이력으로 남기지 않았으므로,
이 항목은 그 지점부터 이어 v2.1.157~v2.1.160 델타를 다룹니다. 이 범위에는 파괴적 변경이
없었습니다 — 추가분은 새 CLI/기능 표면 몇 가지와 정기 푸터 상향입니다. 서드파티 제공자의
오토 모드는 **옵트인**이며 새 기본값이 아닙니다.

### 추가

- **`claude plugin init <name>`(v2.1.157)** — `.claude/skills`에 새 플러그인을 직접
  스캐폴딩하며, 그곳에 둔 플러그인은 마켓플레이스 없이 자동 로드됩니다. `10-cli/README.md`,
  `07-plugins/README.md`, `CATALOG.md`에 문서화했습니다.
- **Bedrock / Vertex / Foundry의 오토 모드(v2.1.158)** — 세 서드파티 제공자에서 Opus 4.7/4.8용
  오토 모드를 쓸 수 있으며, `CLAUDE_CODE_ENABLE_AUTO_MODE=1` 환경변수로 **옵트인**합니다.
  `09-advanced-features/README.md`, `10-cli/README.md`, `CATALOG.md`에 문서화했습니다.
- **`EnterWorktree` 세션 중 전환(v2.1.157)** — `EnterWorktree` 도구가 세션 내에서 Claude 관리
  워크트리 사이를 전환할 수 있고, 완료된 워크트리는 잠금이 풀린 채 남아
  `git worktree remove`/`prune`으로 정리할 수 있습니다. `09-advanced-features/README.md`에
  문서화했습니다.

### 동작 변경

- **`acceptEdits` 쓰기 안전 프롬프트(v2.1.160)** — `acceptEdits` 모드에서도 Claude Code는 셸 시작
  파일(`.zshenv`, `.zlogin`, `.bash_login`, `~/.config/git/`)과 코드를 실행하는 빌드 설정
  (`.npmrc`, `.yarnrc*`, `bunfig.toml`, `.bazelrc`, `.pre-commit-config.yaml`, `.devcontainer/`)에
  쓰기 전에 묻습니다. 그렇지 않으면 의도치 않은 명령 실행으로 이어질 수 있습니다.
  `09-advanced-features/README.md`에 문서화했습니다.
- **동적 워크플로 트리거 키워드 `workflow` → `ultracode`(v2.1.160)** — "workflow"라는 단어만으로는
  더 이상 동적 워크플로가 실행되지 않고, 트리거 키워드는 이제 `ultracode`입니다.
  `09-advanced-features/README.md`에 명시했습니다.

### 제거

- **`CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE`는 이제 무효(v2.1.160)** — 환경변수가 제거되어
  효과가 없습니다. `10-cli/README.md`의 환경변수 표 문구를 "removed 2026-06-01"에서
  "Removed (no-op as of v2.1.160)"로 갱신했습니다.

### 문서화

- `README.md`의 내부 모순 버전 문자열 세 개(배지와 FAQ 본문이 `2.1.145` / `v2.1.150`에 멈춰
  있었음)를 고치고 낡은 Sources 링크를 정규화했습니다.
- 일관된 동기화를 위해 모든 영어 문서의 메타데이터 푸터를 **v2.1.160 / June 2, 2026**으로
  올렸습니다.

## [v2.1.150] — 2026-05-25

### Claude Code v2.1.150 동기화

튜토리얼 커버리지를 Claude Code v2.1.145 → v2.1.150(2026년 5월 23일 릴리스)으로 올립니다.
지난 동기화 이후 Anthropic은 패치 다섯 건(v2.1.146~v2.1.150)을 냈습니다. 핵심 변경은
**번들 `/simplify` 스킬의 `/code-review` 개명**(v2.1.146)입니다 — **별칭 없는** 순수 개명이라
옛 이름은 더 이상 동작하지 않습니다. 이 저장소도 자체 로컬 code-review 스킬을 제공하므로,
새 내장 기능을 가리지 않도록 디렉터리를 `code-review-specialist`로 바꿨습니다. 그 밖의
하이라이트: `/usage`의 범주별 비용 분석, `Ctrl+T`로 백그라운드 세션 고정, 마크다운 렌더러의
GFM 작업 목록 체크박스 지원, 새 관리 설정 `allowAllClaudeAiMcps` 추가. 이번 동기화는
v2.1.143에 묶여 있던 모듈 README 네 개(`04-subagents`, `05-mcp`, `07-plugins`,
`09-advanced-features`)도 따라잡습니다.

### 동작 변경

- **`/simplify` → `/code-review` 개명(v2.1.146)**: 번들 리뷰 스킬은 이제 `/code-review`로
  호출하고 선택적 effort 수준을 받습니다(예: `/code-review high`). `--comment`를 넘기면 결과를
  GitHub PR 인라인 코멘트로 남깁니다(v2.1.147). 옛 `/simplify` 이름은 더 이상 동작하지
  않습니다 — 별칭이 없습니다. `01-slash-commands/README.md`, `03-skills/README.md`,
  `CATALOG.md`, `QUICK_REFERENCE.md`, `claude_concepts_guide.md`에서 갱신했습니다.

### 변경

- **저장소의 로컬 `code-review` 스킬을 `code-review-specialist`로 개명** — 새 내장
  `/code-review`와 충돌하지 않도록 했습니다. 디렉터리는 `03-skills/code-review/` →
  `03-skills/code-review-specialist/`이며, 모든 설치 명령·디렉터리 트리·상호 참조를
  `README.md`, `QUICK_REFERENCE.md`, `INDEX.md`, `CATALOG.md`, `LEARNING-ROADMAP.md`,
  `claude_concepts_guide.md`, `03-skills/README.md`에서 갱신했습니다. 충돌 이유와 내장 기능을
  가리지 않는 방법을 설명하는 주석을 추가했습니다.

### 추가

- **`/usage` 범주별 비용 분석(v2.1.149)** — 비용 보기가 이제 지출을 범주별(스킬, 서브에이전트,
  플러그인, MCP 서버별 비용)로 나눕니다. `CATALOG.md`와 `claude_concepts_guide.md`에
  문서화했습니다.
- **백그라운드 세션 고정 — `Ctrl+T`(v2.1.147)** — `claude agents`에서 세션을 고정하면 유휴
  상태에서도 살아 있고, Claude Code 업데이트 적용을 위해 제자리에서 재시작하며, 메모리 압박 시
  고정되지 않은 세션 다음으로 정리됩니다. `10-cli/README.md`에 문서화했습니다.
- **GFM 작업 목록 체크박스 렌더링(v2.1.149)** — 마크다운 렌더러가 `- [ ]` / `- [x]`를
  체크박스로 렌더링합니다. `09-advanced-features/README.md`에 문서화했습니다.
- **`allowAllClaudeAiMcps` 관리 설정(v2.1.149)** — 조직 전체에서 claude.ai 클라우드 MCP 커넥터
  로딩을 허용합니다. `05-mcp/README.md`에 문서화했습니다.

### 제거

- **Stop/SubagentStop 훅 입력 필드 `background_tasks`와 `session_crons`** —
  `06-hooks/README.md`와 `resources.md`에서 제거했습니다. v2.1.145 릴리스 노트를 보고 추가했지만
  공식 훅 레퍼런스 페이지에 열거되어 있지 않아, 문서를 공개 레퍼런스에 맞추기 위해 제거했습니다.

### 문서화

- 모듈 README 네 개를 v2.1.143에서 v2.1.150으로 따라잡았습니다:
  `04-subagents/README.md`, `05-mcp/README.md`, `07-plugins/README.md`,
  `09-advanced-features/README.md`.
- 모든 영어 문서의 메타데이터 푸터를 **v2.1.150 / May 25, 2026**으로 올렸습니다.

## [v2.1.145] — 2026-05-20

### Claude Code v2.1.145 동기화

튜토리얼 커버리지를 Claude Code v2.1.143 → v2.1.145(2026년 5월 19일 릴리스)로 올립니다.
지난 동기화 이후 Anthropic은 패치 두 건(v2.1.144, v2.1.145)을 냈습니다. 하이라이트:
`/extra-usage` → `/usage-credits` 개명, `/model`의 기본 세션 한정화, 새 번들 스킬 세 개
(`/run`, `/verify`, `/run-skill-generator`), Stop/SubagentStop 훅 입력 필드 `background_tasks`와
`session_crons`, 스크립팅용 `claude agents --json`, 그리고 순수 환경변수 Bash 자동 승인 우회를
막는 보안 수정. 이번 동기화는 v2.1.143 동기화에서 놓쳐 여전히 v2.1.138에 묶여 있던 루트 참조
문서 여섯 개(`LEARNING-ROADMAP.md`, `QUICK_REFERENCE.md`, `INDEX.md`, `resources.md`,
`claude_concepts_guide.md`, `STYLE_GUIDE.md`)도 따라잡습니다.

### 추가

- `/usage-credits` 슬래시 커맨드(v2.1.144) — 주 이름으로 `/extra-usage`를 대체하며,
  `/extra-usage`는 별칭으로 계속 동작합니다. `01-slash-commands/README.md`와 `CATALOG.md`에
  문서화했습니다.
- 새 번들 스킬 세 개(v2.1.145) — `/run`(프로젝트 앱을 띄워 변경이 실행되는 모습 확인),
  `/verify`(앱을 빌드·실행·관찰해 수정이 동작함을 확인), `/run-skill-generator`(프로젝트별 스킬을
  생성해 `/run`·`/verify`가 특정 프로젝트를 다루는 법을 가르침). `03-skills/README.md`,
  `CATALOG.md`, `QUICK_REFERENCE.md`에 문서화했습니다. 정규 번들 스킬 개수는 **9**가 됩니다.
- Stop/SubagentStop 훅 입력 필드 `background_tasks`와 `session_crons`(v2.1.145) — 훅 작성자가
  백그라운드 작업이나 예약 작업이 아직 대기 중일 때 정지를 차단할지 판단하는 데 읽을 수 있습니다.
  `06-hooks/README.md`에 문서화했습니다.
- `claude agents --json`(v2.1.145) — 에이전트 목록을 스크립팅용 기계 판독 JSON으로 출력합니다
  (상태 바, 세션 선택기, tmux-resurrect). `10-cli/README.md`에 문서화했습니다.
- 요약 표에서 빠져 있던 훅 이벤트 행 다섯 개 — `Setup`, `UserPromptExpansion`, `PermissionDenied`,
  `PostToolBatch`(서술부는 이미 "이벤트 29개"라고 했지만 `CATALOG.md`,
  `claude_concepts_guide.md`, `INDEX.md`의 요약 표는 25개만 나열했습니다).

### 동작 변경

- **`/model`은 기본적으로 세션 한정(v2.1.144)**: 모델 선택이 이제 현재 세션에만 적용됩니다.
  선택 후 `d`를 누르면 그 선택이 이후 세션의 새 기본값이 됩니다.
  `01-slash-commands/README.md`에 문서화했습니다.
- **Bash 순수 환경변수 자동 승인 차단(v2.1.145 보안 수정)**: `FOO=bar somecommand` 형태의 명령은
  허용 목록에 `FOO=bar`만 있을 때 더 이상 자동 승인되지 않습니다. 전체 명령을 포괄하는
  `Bash(...)` 권한 규칙으로 다시 허용하세요. `06-hooks/README.md`에 문서화했습니다.
- **`context: fork` 무한 루프 수정(v2.1.145)**: `context: fork`를 쓰는 스킬이 드물게 무한
  재호출 루프를 일으킬 수 있었습니다. `03-skills/README.md`에 주석으로 문서화했습니다.

### 문서화

- 루트 참조 문서 여섯 개를 v2.1.138에서 v2.1.145로 따라잡았습니다: `LEARNING-ROADMAP.md`,
  `QUICK_REFERENCE.md`, `INDEX.md`, `resources.md`, `claude_concepts_guide.md`, `STYLE_GUIDE.md`.
- 번들 스킬 불일치 수정 — `CATALOG.md`, `QUICK_REFERENCE.md`, `03-skills/README.md`가 각각 다른
  5개짜리 목록을 제시하고 있었습니다. 정규 9개(`/batch`, `/claude-api`, `/debug`,
  `/fewer-permission-prompts`, `/loop`, `/run`, `/run-skill-generator`, `/simplify`, `/verify`)로
  정합했습니다. `QUICK_REFERENCE.md` 셀은 `/voice`와 `/browse`를 번들 스킬로 잘못 적고
  있었는데 둘 다 번들이 아닙니다.
- `QUICK_REFERENCE.md`와 `resources.md`에서 "New Features (March 2026)" → "New Features (May 2026)"로
  이름을 바꿔 저장소의 나머지와 맞췄습니다.
- `README.md`의 버전 배지를 `2.1.138`에서 `2.1.145`로 올리고 본문의 "latest: v2.1.138" 주장
  두 곳을 갱신했습니다.
- 기여자가 현재 버전을 복사하도록 STYLE_GUIDE 예시 메타데이터 푸터를 `2.1.97`에서 `2.1.145`로
  갱신했습니다.

## [v2.1.143] — 2026-05-19

### Claude Code v2.1.143 동기화

튜토리얼 커버리지를 Claude Code v2.1.138 → v2.1.143(2026년 5월 15일 릴리스)으로 올립니다.
지난 동기화 이후 Anthropic은 패치 다섯 건(v2.1.139~v2.1.143)을 냈습니다. 하이라이트:
`/goal`과 `/scroll-speed` 슬래시 커맨드, 전체 디스패치 플래그 집합을 갖춘 `claude agents`
Agent View(Research Preview), Stop 훅 안전 상한, 훅 exec 형식(`args`), PostToolUse용
`continueOnBlock`, 훅 `terminalSequence` 출력, 패스트 모드 기본값의 Opus 4.7 전환,
Bedrock/Vertex/Foundry에서 Windows의 PowerShell 기본화, `worktree.bgIsolation` 설정.

### 추가

- `/goal <statement>` 슬래시 커맨드(v2.1.139) — 경과 시간, 턴 수, 토큰 사용량을 보여주는 실시간
  오버레이 패널과 함께 세션 수준 완료 조건을 등록합니다. `01-slash-commands/README.md`에
  문서화하고 `10-cli/README.md`에서 상호 링크했습니다.
- `/scroll-speed <±N>` 슬래시 커맨드(v2.1.139) — TUI 실시간 미리보기 스크롤 속도를 조정하며
  머신별로 유지됩니다. `01-slash-commands/README.md`에 문서화했습니다.
- `claude agents` Agent View(Research Preview, v2.1.139)와 디스패치 플래그
  `--cwd`(v2.1.141), `--add-dir`, `--settings`, `--mcp-config`,
  `--plugin-dir`, `--permission-mode`, `--model`, `--effort`,
  `--dangerously-skip-permissions`(v2.1.142). `10-cli/README.md`에 문서화했습니다.
- `claude plugin details <name>`(v2.1.139) — 전체 플러그인 인벤터리와 턴당·호출당 토큰 비용
  추정치를 보여줍니다. v2.1.142에서 상세 창에 LSP 서버가 추가되었습니다.
  `07-plugins/README.md`에 문서화했습니다.
- `/plugin` 브라우즈 창의 마켓플레이스 컨텍스트 비용 예측(v2.1.143). `07-plugins/README.md`에
  문서화했습니다.
- 훅 **exec 형식**(`args: string[]`, v2.1.139) — 셸 파싱 없이 `execve()`로 직접 실행하며,
  셸 형식 `command` 필드와 함께 쓸 수 없습니다. `06-hooks/README.md`에 문서화했습니다.
- PostToolUse의 훅 `continueOnBlock: true` 필드(v2.1.139) — 차단된 도구 결과를 턴을 중단하는
  대신 `tool_result`로 Claude에 되돌려 보여줍니다. `06-hooks/README.md`에 문서화했습니다.
- 훅 `terminalSequence` JSON 출력 필드(v2.1.141) — 데스크톱 알림, 창 제목, 벨용 원시 OSC 이스케이프
  시퀀스를 내보냅니다. `06-hooks/README.md`에 문서화했습니다.
- `worktree.bgIsolation: "none"` 설정(v2.1.143) — 백그라운드 세션이 격리된 워크트리 대신 현재
  작업 사본을 직접 편집합니다. `09-advanced-features/README.md`에 문서화했습니다.
- `CLAUDE_PROJECT_DIR`이 이제 모든 MCP stdio 서버 환경에 전달되며(v2.1.139), 플러그인 및
  프로젝트 `.mcp.json`의 `command`/`args`/`env` 필드에서 `${CLAUDE_PROJECT_DIR}` 치환을
  지원합니다. `05-mcp/README.md`에 문서화했습니다.
- 서브에이전트 OTEL 헤더 `x-claude-code-agent-id`와 `x-claude-code-parent-agent-id`(v2.1.139)로,
  `claude_code.llm_request` OTEL 스팬에 `agent_id` / `parent_agent_id` 속성으로 노출됩니다.
  `04-subagents/README.md`에 문서화했습니다.
- `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1`(v2.1.142) — v2.1.142에서 기본값이 Opus 4.7로
  뒤집힌 뒤 패스트 모드를 Opus 4.6으로 되돌립니다. `10-cli/README.md`에 문서화했습니다.
- `CLAUDE_CODE_USE_POWERSHELL_TOOL=0`과
  `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`(v2.1.143) — 기본 켜짐인 PowerShell 도구를
  끄거나, `-ExecutionPolicy Bypass` 대신 시스템 실행 정책을 따르게 합니다.
  `09-advanced-features/README.md`에 문서화했습니다.
- `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`(v2.1.143) — Stop 훅의 8회 연속 차단 안전 상한을 재정의합니다
  (`0`으로 두면 비활성). `06-hooks/README.md`와 `09-advanced-features/README.md`에 문서화했습니다.
- `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1`(v2.1.141) — SSH 키가 없는 CI 러너를 위해 플러그인 설치 시
  GitHub 플러그인 소스를 HTTPS로 클론하도록 강제합니다. `07-plugins/README.md`에 문서화했습니다.
- `ANTHROPIC_WORKSPACE_ID`(v2.1.141) — 페더레이션 워크로드 아이덴티티 토큰의 범위를 특정
  워크스페이스로 한정합니다. `09-advanced-features/README.md`에 문서화했습니다.
- 루트 수준 `SKILL.md` 플러그인 패턴(v2.1.142) — 최상위 `SKILL.md`만 있고 `skills/` 하위
  디렉터리가 없는 플러그인은 단일 스킬로 노출됩니다. `07-plugins/README.md`에 문서화했습니다.
- `/schedule`의 플러그인 마케팅 명칭 **Routines**(Anthropic 블로그, 2026-05-14) —
  `09-advanced-features/README.md`에 한 줄 주석으로 표시했으며, CLI 표면은 `/schedule` 그대로입니다.

### 동작 변경

- **패스트 모드 기본값이 Opus 4.7로 전환(v2.1.142)**: `/fast`는 이제 기본적으로 Opus 4.7을
  실행합니다(이전 Opus 4.6). `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1`로 되돌릴 수 있습니다.
- **Bedrock/Vertex/Foundry에서 Windows의 PowerShell 도구 기본 활성(v2.1.143)**:
  Claude Code가 `-ExecutionPolicy Bypass`로 PowerShell을 호출합니다.
  `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`(시스템 정책 준수) 또는
  `CLAUDE_CODE_USE_POWERSHELL_TOOL=0`(도구 비활성)으로 옵트아웃합니다.
- **API 키 인증이 설정되면 Remote Control, `/schedule`, claude.ai MCP 커넥터, 알림 설정이 자동
  비활성화(v2.1.139)**: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper` 중 하나를
  설정하면 claude.ai 로그인이 함께 활성이어도 이 네 가지 claude.ai 연동 표면이 모두 꺼집니다.
- **Stop 훅 차단 루프는 연속 8회로 제한(v2.1.143)**: 연속 8회 후에는 경고와 함께 세션이
  종료되어, 버그 있는 Stop 훅이 세션을 영원히 반복시키지 못합니다.
  `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`으로 재정의합니다.
- **`subagent_type` 매칭이 대소문자·구분자 무시로 변경(v2.1.140)**:
  `code-reviewer`, `Code Reviewer`, `code_reviewer`가 모두 같은 에이전트로 해석됩니다.
  `04-subagents/README.md`에 문서화했습니다.

### 변경

- 루트 참조 문서(`README.md`, `CATALOG.md`)를 `28 hook events`에서 `29 hook events`로 갱신했습니다 —
  v2.1.138에서 `Setup` 훅이 들어온 뒤 `06-hooks/README.md`, `LEARNING-ROADMAP.md`와 일치합니다.

### 번역자 참고

- 튜토리얼 번역(`vi/`, `ja/`, `uk/`, `zh/`)은 영어를 따릅니다. 이번 라운드의 델타를 모듈 README와
  위 CHANGELOG에 동기화하세요. 푸터는 `Last Updated: May 19, 2026`와
  `Claude Code Version: 2.1.143`을 반영해야 합니다.

## [v2.1.138] — 2026-05-09

### Claude Code v2.1.138 동기화

튜토리얼 커버리지를 Claude Code v2.1.131 → v2.1.138(2026년 5월 9일 릴리스)로 올립니다.
지난 동기화 이후 Anthropic은 v2.1.132부터 v2.1.138까지 패치 일곱 건을 냈습니다.

### 추가 (영어 문서)

- `worktree.baseRef` 설정(v2.1.133) — `claude --worktree`가 `origin/<default>`(`"fresh"`, 기본)에서
  분기할지 로컬 `HEAD`(`"head"`)에서 분기할지 제어합니다. **동작 변경**: `"fresh"` 기본값은
  v2.1.128 동작을 되돌리므로, v2.1.128 이후 로컬 `HEAD` 분기에 의존한 사용자는 직접 다시
  옵트인해야 합니다. `09-advanced-features/README.md`에 문서화했습니다.
- `autoMode.hard_deny` 관리자 키(v2.1.136) — 추론된 사용자 의도와 무관하게 특정 부류의 동작을
  차단하는 분류기 규칙 배열입니다. 오토 모드에서 절대 실행되면 안 되는 동작
  (예: `rm -rf /`, 보호된 브랜치로의 강제 푸시)에 사용합니다. `soft_deny`와 달리 hard-deny
  규칙은 분류기가 협상할 수 없습니다. `09-advanced-features/README.md`에 문서화했습니다.
- `parentSettingsBehavior` 관리자 키(v2.1.133+, 관리자 등급) — SDK의 `managedSettings`가
  부모 프로세스 설정과 병합되는 방식을 제어합니다. `"first-wins"`는 기존 우선순위를 유지하고
  `"merge"`는 값을 깊은 병합합니다. `09-advanced-features/README.md`에 문서화했습니다.
- `Setup` 훅 이벤트 — 최초 환경 설정(세션당 1회)이며, 도구 프로비저닝이나 의존성 설치에 씁니다.
  문서화된 훅 이벤트 합계가 28에서 29로 늘어납니다. `06-hooks/README.md`에 문서화했습니다.
- 훅 입력 JSON의 `effort.level` 필드(v2.1.133) — 훅에 활성 effort 수준
  (`low`/`medium`/`high`/`xhigh`/`max`)을 노출합니다. `06-hooks/README.md`에 문서화했습니다.
- Bash 하위 프로세스의 `CLAUDE_CODE_SESSION_ID` 환경변수(v2.1.132) — 훅 입력 JSON의
  `session_id` 필드와 일치하는 세션 UUID로, bash 로그와 훅 텔레메트리를 연관시킬 수 있습니다.
  `06-hooks/README.md`에 문서화했습니다.
- Bash 하위 프로세스의 `CLAUDE_EFFORT` 환경변수(v2.1.133) — 활성 effort 수준이며, 훅 입력
  JSON의 `effort.level`과 일치합니다. `06-hooks/README.md`에 문서화했습니다.
- `sandbox.bwrapPath`, `sandbox.socatPath` 설정(v2.1.133+, Linux/WSL) — `bubblewrap`과 `socat`의
  비표준 설치 위치를 지정합니다. 기본은 `$PATH` 조회입니다. `09-advanced-features/README.md`에
  문서화했습니다.
- `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` 환경변수(v2.1.132).
  `09-advanced-features/README.md`에 문서화했습니다.
- `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL` 환경변수(v2.1.136) — OpenTelemetry 데이터를
  수집하는 조직에서 세션 품질 설문을 다시 활성화합니다. OTEL 배포에서는 기본 꺼짐입니다.
  `09-advanced-features/README.md`에 문서화했습니다.

### 변경

- **동작 변경**: 플랜 모드가 이제 모든 파일 쓰기를 무조건 차단합니다(v2.1.136). 일치하는
  `Edit(...)` 규칙이 `permissions.allow`에 있어도 마찬가지입니다. 이전에는 관대한 `Edit(...)`
  규칙이 플랜 모드에서 쓰기를 통과시킬 수 있었으나 그 우회가 막혔습니다. 이전 동작에 의존한
  워크플로는 편집 전에 플랜 모드를 종료(`Shift+Tab`)해야 합니다.
  `09-advanced-features/README.md`에 문서화했습니다.
- 플러그인의 띄어 쓴 슬래시 커맨드(예: `/myplugin review`)가 이제 `/myplugin:review`로
  해석됩니다. 플러그인 `skills` 설정 항목이 더 이상 기본 `skills/` 디렉터리를 가리지 않고
  둘이 병합됩니다. `07-plugins/README.md`에 문서화했습니다.
- MCP 서버가 이제 `/clear`를 넘겨 유지됩니다(v2.1.132+). `05-mcp/README.md`에 문서화했습니다.
- 서브에이전트가 Skill 도구로 프로젝트·사용자·플러그인 스킬을 탐색합니다(v2.1.133).
  `04-subagents/README.md`에 문서화했습니다.
- 플랜 모드 세션을 재개할 때 `--permission-mode`가 이제 반영됩니다(v2.1.132).
  `09-advanced-features/README.md`에 문서화했습니다.
- `CronList` 출력에 이제 한정자와 예약 프롬프트 본문이 포함되어(v2.1.136), 각 cron을 열어 보지
  않고도 무엇이 실행될지 감사할 수 있습니다. `09-advanced-features/README.md`에 문서화했습니다.

### 수정

- OAuth 리프레시 토큰 동시 갱신 경쟁 조건.
- INDEX.md 개수 드리프트: Skills 28 → 16, Plugins 40 → 27, Hooks 스크립트
  8 → 9(마크다운 콘텐츠 트리에서 다시 셈). 새 합계는 빌드 산출물과 설정을 제외하고 튜토리얼
  콘텐츠로 범위를 한정하는 `.md` 전용 산정 방식을 반영합니다.
- `CATALOG.md`(v2.1.118 → v2.1.138)와 `claude_concepts_guide.md`(v2.1.117 → v2.1.138)의 낡은
  소스 URL. 개념 가이드의 중복된 레거시 푸터를 제거했습니다.

### 번역 유지보수자 참고

`vi/`, `zh/`, `uk/`, `ja/` 번역 트리는 커뮤니티가 유지하며 영어 원문보다 뒤처질 수 있습니다.
번역을 동기화하는 기여자는 이번 릴리스에서 갱신된 영어 파일과 diff를 떠 보세요.

## [v2.1.131] — 2026-05-06

### Claude Code v2.1.131 동기화

튜토리얼 커버리지를 Claude Code v2.1.126 → v2.1.131(2026년 5월 6일 릴리스)로 올립니다.
지난 동기화 이후 Anthropic은 v2.1.128, v2.1.129, v2.1.131을 냈으며, v2.1.127과 v2.1.130은
건너뛰어 공개 릴리스되지 않았습니다.

### 추가 (영어 문서)

- `--plugin-url <url>` 플래그(v2.1.129) — URL에서 플러그인 `.zip` 아카이브를 받아 현재 세션에
  적용합니다. 반복 지정할 수 있습니다. `07-plugins/README.md`에 문서화했습니다.
- `CLAUDE_CODE_FORCE_SYNC_OUTPUT` 환경변수(v2.1.129) — 자동 감지가 놓치는 터미널
  (예: Emacs `eat`)에서 동기 출력을 강제합니다. `10-cli/README.md`와
  `09-advanced-features/README.md`에 문서화했습니다.
- `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE` 환경변수(v2.1.129) — Homebrew/WinGet 설치
  (보통 자동 업데이트되지 않음)의 백그라운드 업그레이드를 활성화합니다. `10-cli/README.md`와
  `09-advanced-features/README.md`에 문서화했습니다.
- `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` 환경변수(v2.1.129) — `/v1/models` 게이트웨이
  탐색을 옵트인하는 데 필요합니다(변경 항목 참고). `10-cli/README.md`에 문서화했습니다.
- `disableRemoteControl` 설정(v2.1.128) — 관리자가 관리/정책 스코프로 `claude remote-control`과
  `/remote-control`을 차단할 수 있습니다. `09-advanced-features/README.md`에 문서화했습니다.
- `--plugin-dir`이 `.zip` 아카이브를 받습니다(v2.1.128) — 디렉터리 입력과 함께 지원합니다.
  `07-plugins/README.md`에 문서화했습니다.
- `skillOverrides`가 `"name-only"`와 `"user-invocable-only"`를 받습니다(v2.1.129) — 기존
  `"on"`/`"off"`에 더해 지원합니다. `03-skills/README.md`에 문서화했습니다.

### 변경

- **동작 변경**: 게이트웨이 `/v1/models` 탐색이 이제 **옵트인**입니다(v2.1.129). 이전(v2.1.126)에는
  `ANTHROPIC_BASE_URL`만 설정하면 `/model`이 게이트웨이의 `/v1/models` 엔드포인트에서 자동으로
  채워졌습니다. v2.1.129부터는 `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`을 추가로 설정해야
  하며, 환경변수가 없으면 `/model`은 내장 정적 목록으로 폴백합니다.
  `10-cli/README.md`에 문서화했습니다.
- `/mcp`가 서버별 도구 개수를 보여주고 도구가 0개라고 보고하는 서버를 시각적으로 표시합니다
  (v2.1.128). `05-mcp/README.md`에 문서화했습니다.
- 인자 없는 `/color`가 임의의 세션 색을 고릅니다(v2.1.128). 명시적 `/color <name|hex>`는 계속
  특정 색을 지정합니다. `01-slash-commands/README.md`에 문서화했습니다.
- `--channels` 플래그가 이제 API 키(콘솔) 인증에서도 동작합니다(v2.1.128). 이전 릴리스는
  Pro/Max OAuth를 요구했습니다. `09-advanced-features/README.md`에 문서화했습니다.
- Ctrl+R 기록 선택기가 기본적으로 **모든 프로젝트의 모든 프롬프트**를 보여줍니다(v2.1.129).
  선택기 안에서 Ctrl+S를 누르면 현재 프로젝트로 범위를 좁힙니다.
  `09-advanced-features/README.md`에 문서화했습니다.
- `/context`가 더 이상 ASCII 시각화를 대화에 덤프하지 않습니다(v2.1.129). 시각화는 UI에만
  표시되어 호출당 약 1.6k 토큰 비용이 사라졌습니다. `09-advanced-features/README.md`에
  문서화했습니다.
- 드래그 앤 드롭한 과대 이미지가 자동 축소됩니다(v2.1.128) — 이전 버전은 이미지를 그대로
  거부했습니다.

### 수정

- Windows의 VS Code 확장 활성화(v2.1.131).
- Mantle 엔드포인트 인증(v2.1.131).
- 1시간 프롬프트 캐시 TTL이 더 이상 5분으로 잘리지 않습니다(v2.1.129).
- 10 MB를 넘는 stdin 페이로드에서의 크래시(v2.1.128).

### 번역 유지보수자 참고

`vi/`, `zh/`, `uk/`, `ja/` 번역 트리는 커뮤니티가 유지하며 영어 원문보다 뒤처질 수 있습니다.
번역을 동기화하는 기여자는 이번 릴리스에서 갱신된 영어 파일과 diff를 떠 보세요.

## [v2.1.126] — 2026-05-02

### Claude Code v2.1.126 동기화

튜토리얼 커버리지를 Claude Code v2.1.119 → v2.1.126(2026년 5월 1일 릴리스)으로 올립니다.
v2.1.120은 첫 릴리스 당일(2026-04-24) 롤백되었지만, 보고된 회귀를 수정해 2026-04-28에
정상 재배포되었습니다. v2.1.124와 v2.1.125는 Anthropic이 건너뛰어 릴리스되지 않았습니다.

### 추가 (영어 문서)

- `claude project purge [path]` 하위 커맨드(v2.1.126) — 프로젝트의 Claude Code 상태 전부
  (트랜스크립트, 작업, 디버그 로그, 파일 편집 이력, 프롬프트 기록, `~/.claude.json` 항목)를
  삭제합니다. `--dry-run`, `-y/--yes`, `-i/--interactive`, `--all`을 지원합니다.
  `10-cli/README.md`에 문서화했습니다.
- `claude plugin prune` 하위 커맨드(v2.1.121) — 고아가 된 자동 설치 플러그인 의존성을 제거하며
  `plugin uninstall --prune`이 연쇄 처리합니다. `07-plugins/README.md`에 문서화했습니다.
- `claude ultrareview [target]` 하위 커맨드(v2.1.120) — CI/스크립트에서 `/ultrareview`를
  비대화형으로 실행하고 결과를 stdout에 출력하며 성공/실패에 따라 0/1로 종료합니다.
  `--json`과 `--timeout <minutes>`를 지원합니다. `10-cli/README.md`에 문서화했습니다.
- 스킬 콘텐츠 안에서 쓸 수 있는 `${CLAUDE_EFFORT}` 플레이스홀더(v2.1.120) — 현재 effort 수준으로
  해석됩니다. `03-skills/README.md`에 문서화했습니다.
- `alwaysLoad` MCP 서버 설정 옵션(v2.1.121) — `true`이면 해당 서버의 모든 도구가 도구 검색
  지연을 건너뜁니다. `05-mcp/README.md`에 문서화했습니다.
- `PostToolUse.hookSpecificOutput.updatedToolOutput`이 이제 모든 도구에서 동작합니다(v2.1.121).
  이전에는 MCP 전용이었습니다. `06-hooks/README.md`에 문서화했습니다.
- `ANTHROPIC_BEDROCK_SERVICE_TIER` 환경변수(v2.1.122) — Bedrock 서비스 등급
  (`default`, `flex`, `priority`)을 선택합니다. `10-cli/README.md` 환경변수 표에 문서화했습니다.
- `--dangerously-skip-permissions` 확장 경로 커버리지(v2.1.121, v2.1.126) — 이제
  `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/`, `.git/`, `.vscode/`,
  셸 설정 파일에 대한 쓰기 프롬프트를 우회합니다. 파괴적 삭제 명령(`rm -rf /` 등)은 계속
  프롬프트를 띄웁니다. `09-advanced-features/README.md` 권한 모드 절에 문서화했습니다.
- OAuth 코드 붙여넣기 폴백(v2.1.126) — 브라우저 콜백이 localhost에 닿지 못하는 경우(WSL2, SSH,
  컨테이너) `claude auth login`이 터미널에 붙여넣은 OAuth 코드를 받습니다.
  `10-cli/README.md`에 문서화했습니다.
- 입력 필터형 `/skills` 메뉴(v2.1.121). `03-skills/README.md`에 문서화했습니다.
- `AI_AGENT` 환경변수(v2.1.120) — `gh`가 트래픽을 Claude Code로 귀속시킬 수 있도록 하위
  프로세스에 설정됩니다. `10-cli/README.md` 환경변수 표에 문서화했습니다.

### 변경

- `--from-pr`(v2.1.119)과 `/resume`의 PR URL 검색(v2.1.122)이 이제 모두 GitHub, GitHub
  Enterprise, GitLab, Bitbucket URL을 지원합니다.
- Windows: Git for Windows / Git Bash가 더 이상 필요하지 않습니다(v2.1.120) — Git Bash가 없으면
  Claude Code가 셸 도구로 PowerShell을 씁니다. v2.1.126부터 PowerShell 도구가 활성이면
  PowerShell이 기본 셸입니다. 감지 범위는 Microsoft Store, PATH 없는 MSI,
  `.NET 글로벌 도구`로 설치된 PowerShell 7까지 확장되었습니다.
  `09-advanced-features/README.md` 플랫폼 주석에 문서화했습니다.
- `ANTHROPIC_BASE_URL`이 Anthropic 호환 게이트웨이를 가리키면 `/model` 선택기가 이제 게이트웨이의
  `/v1/models` 엔드포인트에서 모델을 나열합니다(v2.1.126). `10-cli/README.md`에 문서화했습니다.
- `--dangerously-skip-permissions`가 훨씬 넓어진 허용 목록에 대한 쓰기에서 프롬프트를 띄우지
  않습니다(추가 항목 참고). 파괴적 삭제는 계속 프롬프트를 띄웁니다.
- 이미지 붙여넣기 자동 축소(v2.1.126) — 2000px를 넘는 이미지는 붙여넣을 때 축소됩니다.
  기록에 있는 과대 이미지는 자동 제거되고 요청이 재시도됩니다. (튜토리얼 관점에서는
  안전성/UX 주석 수준입니다.)

### 보안

- 상위 우선순위 관리 설정 소스에 `sandbox` 블록이 없을 때 `allowManagedDomainsOnly` /
  `allowManagedReadPathsOnly`가 무시되던 문제를 수정했습니다(v2.1.126).

### 번역 유지보수자 참고

`vi/`, `zh/`, `uk/`, `ja/` 번역 트리는 커뮤니티가 유지하며 영어 원문보다 뒤처질 수 있습니다.
번역을 동기화하는 기여자는 이번 릴리스에서 갱신된 영어 파일과 diff를 떠 보세요.

## [v2.4.0] — 2026-04-27

### Claude Code v2.1.119 동기화

튜토리얼 커버리지를 Claude Code v2.1.112 → v2.1.119(2026년 4월 23일 릴리스)로 올립니다.
v2.1.120은 4월 24일 배포되었다가 회귀 때문에 같은 날 잠시 롤백되었고, 수정을 거쳐 4월 28일에
재배포되어 이제 정상 릴리스 라인의 일부입니다. 이후의 v2.1.126(2026년 5월 1일)이 다음 안정
목표이며 위의 v2.1.126 항목에서 다룹니다.

### 추가 (영어 문서)

- 네이티브 바이너리 패키징 주석(v2.1.113) — CLI가 이제 플랫폼별 네이티브 바이너리를 배포합니다
- 네이티브 macOS/Linux 빌드의 `bfs`/`ugrep` Glob/Grep 대체 각주(v2.1.117)
- `mcp_tool` 훅 유형과 예제(v2.1.118)
- PostToolUse / PostToolUseFailure 입력의 `duration_ms` 필드(v2.1.119)
- `prUrlTemplate` 설정(v2.1.119)과 확장된 `--from-pr` 제공자 목록(GitLab, Bitbucket)
- `cleanupPeriodDays` 범위 확장(체크포인트 + 작업 + 셸 스냅샷 + 백업, v2.1.117)
- 모든 수명 주기 이벤트에서의 플러그인 마켓플레이스 적용(v2.1.117)과 `hostPattern`/`pathPattern`
  정규식(v2.1.119)
- 새 환경변수: `DISABLE_UPDATES`, `CLAUDE_CODE_HIDE_CWD`, `CLAUDE_CODE_FORK_SUBAGENT`,
  `OTEL_LOG_TOOL_DETAILS`, `ENABLE_TOOL_SEARCH` Vertex 옵트인
- 새 슬래시 커맨드: `/btw`, 커스텀 테마를 지원하는 `/theme`
- `/usage` 정규 커맨드(`/cost` + `/stats` 병합, v2.1.118)
- 포크 서브에이전트(`CLAUDE_CODE_FORK_SUBAGENT=1`, v2.1.117)
- 오토 모드 `"$defaults"` 토큰(v2.1.118)
- `wslInheritsWindowsSettings` 관리 정책(v2.1.118)
- Vim 비주얼 / 비주얼 라인 모드(v2.1.118)
- `claude install [version]`과 `claude plugin tag` 하위 커맨드

### 변경

- 문서 호스트 이전: `docs.anthropic.com/en/docs/claude-code/*` → `code.claude.com/docs/en/*`
- Opus 4.7 effort 수준: 2026-04-16 출시 이후 `xhigh`가 Claude Code 기본값이며, Opus 4.7의 네이티브
  컨텍스트 창은 1M로 확인되었습니다(v2.1.117에서 `/context`가 이를 200K로 잘못 세던 문제 수정)
- Opus 4.6 / Sonnet 4.6의 Pro/Max 구독자 기본 effort가 `medium`에서 `high`로 상향(v2.1.117)
- `STYLE_GUIDE.md`의 Source URL을 Claude Apps 문서에서 `code.claude.com/docs/en/changelog`로 갱신

### 지원 중단 (추적 중, 제거 안 함)

- `includeCoAuthoredBy` 설정 → `attribution.commit` / `attribution.pr` 사용
- `voiceEnabled` 설정 → `voice.enabled` 사용

### 번역 유지보수자 참고

`vi/`, `zh/`, `uk/` 번역 트리는 커뮤니티가 유지하며 영어 원문보다 뒤처질 수 있습니다.
번역을 동기화하는 기여자는 이번 릴리스에서 갱신된 영어 파일과 diff를 떠 보세요.

## v2.1.112 — 2026-04-16

### 주요 변경

- 모든 영어 튜토리얼을 Claude Code v2.1.112와 새 Opus 4.7 모델(`claude-opus-4-7`)에 동기화했습니다.
  새 `xhigh` effort 수준(Opus 4.7 기본값, `high`와 `max` 사이), 새 내장 슬래시 커맨드 두 개
  (`/ultrareview`, `/less-permission-prompts`), Opus 4.7의 Max 구독자에게 `--enable-auto-mode`가
  더 이상 필요 없는 오토 모드, Windows의 PowerShell 도구, "Auto (match terminal)" 테마,
  프롬프트 이름을 따르는 플랜 파일을 포함합니다. 영어 문서 푸터 18개를 모두 Claude Code
  v2.1.112로 올렸습니다. @Luong NGUYEN

### 기능

- 모든 모듈, 루트 문서, 예제, 레퍼런스에 우크라이나어(uk) 번역을 추가했습니다 (039dde2) @Evgenij I

### 버그 수정

- pre-tool-check.sh 훅 프로토콜 버그를 수정했습니다 (bce7cf8) @yarlinghe
- CI를 통과하도록 잘못된 mermaid 예제를 텍스트 블록으로 바꿨습니다 (b8a7b1f) @Evgenij I
- 우크라이나어 claude_concepts_guide.md 목차의 CP1251 인코딩을 수정했습니다 (d970cc6) @Evgenij I
- 스텁 우크라이나어 README를 완역본으로 교체하고 깨진 앵커를 고쳤습니다 (f6d73e2) @Evgenij I
- 모든 푸터의 Claude Code 버전을 2.1.97로 정정했습니다 (63a1416) @Luong NGUYEN
- 2026-04-09 문서 정확성 갱신을 적용했습니다 (e015f39) @Luong NGUYEN

### 문서화

- Claude Code v2.1.112에 동기화했습니다(Opus 4.7, `xhigh` effort, `/ultrareview`,
  `/less-permission-prompts`, PowerShell 도구, Auto-match-terminal 테마) @Luong NGUYEN
- Claude Code v2.1.110에 동기화했습니다(TUI, 푸시 알림, 세션 요약) (15f0085) @Luong NGUYEN
- Claude Code v2.1.101에 동기화했습니다(`/team-onboarding`, `/ultraplan`, Monitor 도구) (2deba3a) @Luong NGUYEN
- 베트남어 문서를 영어 원문과 동기화했습니다 (561c6cb) @Thiên Toán
- 모든 파일의 Last Updated 날짜와 Claude Code 버전을 갱신했습니다 (7f2e773) @Luong NGUYEN
- 언어 전환기에 우크라이나어 링크를 추가했습니다 (9c224ff) @Luong NGUYEN
- 기여자 절을 제거했습니다 (f07313d) @Luong NGUYEN
- GitHub 지표를 21,800+ 스타, 2,585+ 포크로 갱신했습니다 (4f55374) @Luong NGUYEN

**전체 변경 이력**: https://github.com/luongnv89/claude-howto/compare/v2.3.0...v2.1.112

---

## v2.3.0 — 2026-04-07

### 기능

- 언어별 EPUB 산출물을 빌드·게시합니다 (90e9c30) @Thiên Toán
- 06-hooks에 빠져 있던 pre-tool-check.sh 훅을 추가했습니다 (b511ed1) @JiayuWang
- zh/ 디렉터리에 중국어 번역을 추가했습니다 (89e89d4) @Luong NGUYEN
- performance-optimizer 서브에이전트와 dependency-check 훅을 추가했습니다 (f53d080) @qk

### 버그 수정

- Windows Git Bash 호환성 + stdin JSON 프로토콜 (2cbb10c) @Luong NGUYEN
- 08-checkpoints의 autoCheckpoint 설정 문서를 정정했습니다 (749c79f) @JiayuWang
- SVG 이미지를 플레이스홀더로 바꾸지 않고 직접 삽입했습니다 (1b16709) @Thiên Toán
- 메모리 README의 중첩 코드 펜스 렌더링 (ce24423) @Zhaoshan Duan
- 스쿼시 병합에서 누락된 리뷰 수정을 적용했습니다 (34259ca) @Luong NGUYEN
- 훅 스크립트가 Windows Git Bash와 호환되도록 하고 stdin JSON 프로토콜을 쓰도록 했습니다 (107153d) @binyu li

### 문서화

- 모든 튜토리얼을 최신 Claude Code 문서(2026년 4월)와 동기화했습니다 (72d3b01) @Luong NGUYEN
- 언어 전환기에 중국어 링크를 추가했습니다 (6cbaa4d) @Luong NGUYEN
- 영어와 베트남어 사이의 언어 전환기를 추가했습니다 (100c45e) @Luong NGUYEN
- GitHub #1 트렌딩 배지를 추가했습니다 (0ca8c37) @Luong NGUYEN
- 컨텍스트 존 모니터링용 cc-context-stats를 도입했습니다 (d41b335) @Luong NGUYEN
- luongnv89/skills 컬렉션과 luongnv89/asm 스킬 매니저를 도입했습니다 (7e3c0b6) @Luong NGUYEN
- 현재 GitHub 지표(5,900+ 스타, 690+ 포크)를 반영하도록 README 통계를 갱신했습니다 (5001525) @Luong NGUYEN
- 현재 GitHub 지표(3,900+ 스타, 460+ 포크)를 반영하도록 README 통계를 갱신했습니다 (9cb92d6) @Luong NGUYEN

### 리팩터링

- Kroki HTTP 의존성을 로컬 mmdc 렌더링으로 교체했습니다 (e76bbe4) @Luong NGUYEN
- 품질 검사를 pre-commit으로 옮기고 CI를 2차 통과로 두었습니다 (6d1e0ae) @Luong NGUYEN
- 오토 모드 권한 기준선을 좁혔습니다 (2790fb2) @Luong NGUYEN
- auto-adapt 훅을 1회성 권한 설정 스크립트로 교체했습니다 (995a5d6) @Luong NGUYEN

### 기타

- 품질 게이트를 앞당겼습니다 — pre-commit에 mypy를 추가하고 CI 실패를 수정했습니다 (699fb39) @Luong NGUYEN
- 베트남어(Tiếng Việt) 번역을 추가했습니다 (a70777e) @Thiên Toán

**전체 변경 이력**: https://github.com/luongnv89/claude-howto/compare/v2.2.0...v2.3.0

---

## v2.2.0 — 2026-03-26

### 문서화

- 모든 튜토리얼과 레퍼런스를 Claude Code v2.1.84에 동기화했습니다 (f78c094) @luongnv89
  - 슬래시 커맨드를 내장 55개 이상 + 번들 스킬 5개로 갱신하고 3개를 지원 중단으로 표시
  - 훅 이벤트를 18개에서 25개로 확장하고 `agent` 훅 유형 추가(이제 4가지 유형)
  - 고급 기능에 Auto Mode, Channels, Voice Dictation 추가
  - `effort`, `shell` 스킬 프론트매터 필드와 `initialPrompt`, `disallowedTools` 에이전트 필드 추가
  - WebSocket MCP 전송, elicitation, 2KB 도구 상한 추가
  - 플러그인 LSP 지원, `userConfig`, `${CLAUDE_PLUGIN_DATA}` 추가
  - 모든 참조 문서(CATALOG, QUICK_REFERENCE, LEARNING-ROADMAP, INDEX) 갱신
- README를 랜딩 페이지 구조의 가이드로 다시 작성했습니다 (32a0776) @luongnv89

### 버그 수정

- CI 준수를 위해 cSpell 단어와 README 절을 보충했습니다 (93f9d51) @luongnv89
- cSpell 사전에 `Sandboxing`을 추가했습니다 (b80ce6f) @luongnv89

**전체 변경 이력**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### 버그 수정

- CI 링크 검사를 실패시키던 죽은 마켓플레이스 링크를 제거했습니다 (3fdf0d6) @luongnv89
- cSpell 사전에 `sandboxed`와 `pycache`를 추가했습니다 (dc64618) @luongnv89

**전체 변경 이력**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### 기능

- 자기 평가와 레슨 퀴즈 스킬을 갖춘 적응형 학습 경로를 추가했습니다 (1ef46cd) @luongnv89
  - `/self-assessment` — 10개 기능 영역에 걸친 대화형 숙련도 퀴즈와 개인화 학습 경로
  - `/lesson-quiz [lesson]` — 레슨별 8~10개 문항으로 구성된 지식 점검

### 버그 수정

- 깨진 URL, 지원 중단 항목, 낡은 참조를 갱신했습니다 (8fe4520) @luongnv89
- resources와 self-assessment 스킬의 깨진 링크를 수정했습니다 (7a05863) @luongnv89
- 개념 가이드의 중첩 코드 블록에 물결 펜스를 사용했습니다 (5f82719) @VikalpP
- cSpell 사전에 빠진 단어를 추가했습니다 (8df7572) @luongnv89

### 문서화

- 5단계 QA — 문서 전반의 일관성, URL, 용어를 수정했습니다 (00bbe4c) @luongnv89
- 3~4단계 완료 — 새 기능 커버리지와 참조 문서 갱신 (132de29) @luongnv89
- MCP 컨텍스트 비대 절에 MCPorter 런타임을 추가했습니다 (ef52705) @luongnv89
- 가이드 6개에 빠진 커맨드, 기능, 설정을 추가했습니다 (4bc8f15) @luongnv89
- 기존 저장소 관례에 기반한 스타일 가이드를 추가했습니다 (84141d0) @luongnv89
- 가이드 비교 표에 self-assessment 행을 추가했습니다 (8fe0c96) @luongnv89
- PR #7 기여자 목록에 VikalpP를 추가했습니다 (d5b4350) @luongnv89
- README와 로드맵에 self-assessment 및 lesson-quiz 스킬 참조를 추가했습니다 (d5a6106) @luongnv89

### 신규 기여자

- @VikalpP가 #7에서 첫 기여를 했습니다

**전체 변경 이력**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### 기능

- 모든 문서를 Claude Code 2026년 2월 기능에 동기화했습니다 (487c96d)
  - 튜토리얼 디렉터리 10개와 참조 문서 7개에 걸쳐 파일 26개를 갱신
  - **Auto Memory** — 프로젝트별 지속 학습 — 문서 추가
  - **Remote Control**, **Web Sessions**, **Desktop App** 문서 추가
  - **Agent Teams**(실험적 멀티 에이전트 협업) 문서 추가
  - **MCP OAuth 2.0**, **Tool Search**, **Claude.ai Connectors** 문서 추가
  - 서브에이전트용 **Persistent Memory**와 **Worktree Isolation** 문서 추가
  - **Background Subagents**, **Task List**, **Prompt Suggestions** 문서 추가
  - **Sandboxing**과 **Managed Settings**(Enterprise) 문서 추가
  - **HTTP Hooks**와 새 훅 이벤트 7개 문서 추가
  - **Plugin Settings**, **LSP Servers**, 마켓플레이스 갱신 문서 추가
  - **Summarize from Checkpoint** 되감기 옵션 문서 추가
  - 새 슬래시 커맨드 17개 문서화(`/fork`, `/desktop`, `/teleport`, `/tasks`, `/fast` 등)
  - 새 CLI 플래그 문서화(`--worktree`, `--from-pr`, `--remote`, `--teleport`, `--teammate-mode` 등)
  - 오토 메모리, effort 수준, 에이전트 팀 등에 대한 새 환경변수 문서화

### 디자인

- 로고를 최소 팔레트의 컴퍼스-브래킷 마크로 재디자인했습니다 (20779db)

### 버그 수정 / 교정

- 모델 이름 갱신: Sonnet 4.5 → **Sonnet 4.6**, Opus 4.5 → **Opus 4.6**
- 권한 모드 이름 수정: 가상의 "Unrestricted/Confirm/Read-only"를 실제 `default`/`acceptEdits`/`plan`/`dontAsk`/`bypassPermissions`로 교체
- 훅 이벤트 수정: 가상의 `PreCommit`/`PostCommit`/`PrePush`를 제거하고 실제 이벤트(`SubagentStart`, `WorktreeCreate`, `ConfigChange` 등) 추가
- CLI 문법 수정: `claude-code --headless`를 `claude -p`(프린트 모드)로 교체
- 체크포인트 커맨드 수정: 가상의 `/checkpoint save/list/rewind/diff`를 실제 `Esc+Esc` / `/rewind` 인터페이스로 교체
- 세션 관리 수정: 가상의 `/session list/new/switch/save`를 실제 `/resume`/`/rename`/`/fork`로 교체
- 플러그인 매니페스트 형식 수정: `plugin.yaml` → `.claude-plugin/plugin.json` 마이그레이션
- MCP 설정 경로 수정: `~/.claude/mcp.json` → `.mcp.json`(프로젝트) / `~/.claude.json`(사용자)
- 문서 URL 수정: `docs.claude.com` → `docs.anthropic.com`, 가상의 `plugins.claude.com` 제거
- 여러 파일에 걸친 가상 구성 필드를 제거했습니다
- 모든 "Last Updated" 날짜를 2026년 2월로 갱신했습니다

**전체 변경 이력**: https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0

---

**최종 갱신**: 2026년 8월 25일
**Claude Code 버전**: 2.1.245
**출처**:
- https://code.claude.com/docs/en/changelog
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
