<!-- i18n-source: QUICK_REFERENCE.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 예제 - 빠른 참조 카드

## 🚀 설치 빠른 명령

### 슬래시 커맨드
```bash
# Install all
cp 01-slash-commands/*.md .claude/commands/

# Install specific
cp 01-slash-commands/optimize.md .claude/commands/
```

### 메모리
```bash
# Project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Personal memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### 스킬
```bash
# Personal skills
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Project skills
cp -r 03-skills/code-review-specialist .claude/skills/
```

### 서브에이전트
```bash
# Install all
cp 04-subagents/*.md .claude/agents/

# Install specific
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# Set credentials
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Install config (project scope)
cp 05-mcp/github-mcp.json .mcp.json

# Or user scope: add to ~/.claude.json
```

### 훅
```bash
# Install hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Configure in settings (~/.claude/settings.json)
```

### 플러그인
```bash
# Install from examples (if published)
claude --plugin-dir ./07-plugins/pr-review
/plugin install devops-automation
/plugin install documentation
```

### 체크포인트
```bash
# Checkpoints are created automatically with every user prompt
# To rewind, press Esc twice or use:
/rewind

# Then choose: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, or Never mind
```

### 고급 기능
```bash
# Configure in settings (.claude/settings.json)
# See 09-advanced-features/config-examples.json

# Planning mode
/plan Task description

# Permission modes (use --permission-mode flag)
# manual         - Ask for approval on every action (config value "default"; "manual" is its alias since v2.1.200)
# acceptEdits    - Auto-accept file edits, ask for others
# plan           - Read-only analysis, no modifications
# auto           - Background classifier decides permissions automatically
# dontAsk        - Only pre-approved tools run; everything else is denied
# bypassPermissions - Accept all actions (--permission-mode bypassPermissions; --dangerously-skip-permissions is equivalent)

# Session management
/resume                # Resume a previous conversation (no args = picker of past sessions)
/rename "name"         # Name the current session
/fork [prompt]         # Copy the conversation into a new background session; keep working here
/subtask <task>        # Spawn a forked subagent that inherits the conversation and reports back
/branch [name]         # Switch into a copy of the conversation, preserving the original
claude -c              # Continue most recent conversation
claude -r "session"    # Resume session by name/ID
```

---

## 📋 기능 치트시트

| 기능 | 설치 경로 | 사용법 |
|---------|-------------|-------|
| **슬래시 커맨드 (60+)** | `.claude/commands/*.md` | `/command-name` |
| **메모리** | `./CLAUDE.md` | 자동 로드됨 |
| **스킬** | `.claude/skills/*/SKILL.md` | 자동 호출됨 |
| **서브에이전트** | `.claude/agents/*.md` | 자동 위임됨 |
| **MCP** | `.mcp.json`(프로젝트) 또는 `~/.claude.json`(사용자) | `/mcp__server__action` |
| **훅 (이벤트 33개)** | `~/.claude/hooks/*.sh` | 이벤트 트리거(유형 5개) |
| **플러그인** | `/plugin install` 경유 | 모든 기능을 묶음 제공 |
| **체크포인트** | 내장 | `Esc+Esc` 또는 `/rewind` |
| **플랜 모드** | 내장 | `/plan <task>` |
| **권한 모드 (6개)** | 내장 | `--allowedTools`, `--permission-mode` |
| **세션** | 내장 | `/resume`, `/rename`, `/branch`, `/fork` |
| **백그라운드 작업** | 내장 | 백그라운드에서 실행 |
| **원격 제어** | 내장 | `claude --remote-control` 또는 `/remote-control` |
| **웹 세션** | 내장 | `claude --cloud "task"` |
| **Git 워크트리** | 내장 | `claude -w <name>` |
| **자동 메모리** | 내장 | `~/.claude/projects/<project>/memory/`에 자동 저장 |
| **작업 목록** | 내장 | `Ctrl+T`(체크리스트), `/tasks`(백그라운드 작업) |
| **내장 스킬** | 내장 | `/batch`, `/claude-api`, `/code-review [low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [pr#\|branch\|path]` *(v2.1.246부터 모든 환경에서 Claude가 스스로 시작할 수도 있습니다. 레벨을 지정하지 않으면 마지막으로 입력한 레벨을 재사용합니다, v2.1.223)*, `/simplify` *(정리 전용 리뷰이며, v2.1.154부터 `/code-review`와 다시 구분됩니다)*, `/debug`, `/fewer-permission-prompts`, `/loop`, `/run` *(v2.1.145+)*, `/run-skill-generator` *(v2.1.145+)*, `/verify` *(v2.1.145+; v2.1.215부터 명시적 호출만 가능하며, Claude가 스스로 트리거하지 않습니다)* |

---

## 🎯 일반적인 사용 사례

### 코드 리뷰
```bash
# Method 1: Slash command
cp 01-slash-commands/optimize.md .claude/commands/
# Use: /optimize

# Method 2: Subagent
cp 04-subagents/code-reviewer.md .claude/agents/
# Use: Auto-delegated

# Method 3: Skill
cp -r 03-skills/code-review-specialist ~/.claude/skills/
# Use: Auto-invoked

# Method 4: Plugin (best)
claude --plugin-dir ./07-plugins/pr-review
# Use: /review-pr
```

### 문서화
```bash
# Slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# Skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Plugin (complete solution)
/plugin install documentation
```

### DevOps
```bash
# Complete plugin
/plugin install devops-automation

# Commands: /deploy, /rollback, /status, /incident
```

### 팀 표준
```bash
# Project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Edit for your team
vim CLAUDE.md
```

### 자동화와 훅
```bash
# Install hooks (33 events, 5 types: command, http, mcp_tool, prompt, agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Examples:
# - Pre-commit tests: pre-commit.sh
# - Auto-format code: format-code.sh
# - Security scanning: security-scan.sh

# Auto Mode for fully autonomous workflows
claude --permission-mode auto -p "Refactor and test the auth module"
# Or cycle modes interactively with Shift+Tab
```

### 안전한 리팩터링
```bash
# Checkpoints are created automatically before each prompt
# Try refactoring
# If it works: continue
# If it fails: press Esc+Esc or use /rewind to go back
```

### 복잡한 구현
```bash
# Use planning mode
/plan Implement user authentication system

# Claude creates detailed plan
# Review and approve
# Claude implements systematically
```

### CI/CD 연동
```bash
# Run in headless mode (non-interactive)
claude -p "Run all tests and generate report"

# With permission mode for CI
claude -p "Run tests" --permission-mode dontAsk

# With Auto Mode for fully autonomous CI tasks
claude --permission-mode auto -p "Run tests and fix failures"

# With hooks for automation
# See 09-advanced-features/README.md
```

### 학습과 실험
```bash
# Use plan mode for safe analysis
claude --permission-mode plan

# Experiment safely - checkpoints are created automatically
# If you need to rewind: press Esc+Esc or use /rewind
```

### 에이전트 팀
```bash
# Enable agent teams
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Or in settings.json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }

# Start with: "Implement feature X using a team approach"
```

### 예약 작업
```bash
# Run a command every 5 minutes
/loop 5m /check-status

# One-time reminder: ask in plain language (/loop repeats until cancelled)
remind me in 30 minutes to check the deploy
```

---

## 📁 파일 위치 참조

```text
Your Project/
├── .claude/
│   ├── commands/              # Slash commands go here
│   ├── agents/                # Subagents go here
│   ├── skills/                # Project skills go here
│   └── settings.json          # Project settings (hooks, etc.)
├── .mcp.json                  # MCP configuration (project scope)
├── CLAUDE.md                  # Project memory
└── src/
    └── api/
        └── CLAUDE.md          # Directory-specific memory

User Home/
├── .claude/
│   ├── commands/              # Personal commands
│   ├── agents/                # Personal agents
│   ├── skills/                # Personal skills
│   ├── hooks/                 # Hook scripts
│   ├── settings.json          # User settings
│   └── CLAUDE.md              # Personal memory
└── .claude.json               # Personal MCP config (user scope)

System directory/              # macOS /Library/Application Support/ClaudeCode/, Linux /etc/claude-code/, Windows C:\Program Files\ClaudeCode\
├── managed-settings.json      # Managed settings (enterprise/org)
└── managed-settings.d/        # Managed settings drop-ins
```

---

## 🔍 예제 찾기

### 카테고리별
- **슬래시 커맨드**: `01-slash-commands/`
- **메모리**: `02-memory/`
- **스킬**: `03-skills/`
- **서브에이전트**: `04-subagents/`
- **MCP**: `05-mcp/`
- **훅**: `06-hooks/`
- **플러그인**: `07-plugins/`
- **체크포인트**: `08-checkpoints/`
- **고급 기능**: `09-advanced-features/`
- **CLI**: `10-cli/`

### 사용 사례별
- **성능**: `01-slash-commands/optimize.md`
- **보안**: `04-subagents/secure-reviewer.md`
- **테스트**: `04-subagents/test-engineer.md`
- **문서**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### 복잡도별
- **단순**: 슬래시 커맨드
- **중간**: 서브에이전트, 메모리
- **고급**: 스킬, 훅
- **완성형**: 플러그인

---

## 🎓 학습 경로

### 1일차
```bash
# Read overview
cat README.md

# Install a command
cp 01-slash-commands/optimize.md .claude/commands/

# Try it
/optimize
```

### 2~3일차
```bash
# Set up memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# Install subagent
cp 04-subagents/code-reviewer.md .claude/agents/
```

### 4~5일차
```bash
# Set up MCP
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# Try MCP commands
/mcp__github__list_prs
```

### 2주차
```bash
# Install skill
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Let it auto-invoke
# Just say: "Review this code for issues"
```

### 3주차 이후
```bash
# Install complete plugin
claude --plugin-dir ./07-plugins/pr-review

# Use bundled features
/review-pr
/check-security
/check-tests
```

---

## 주요 기능

| 기능 | 설명 | 사용법 |
|---------|-------------|-------|
| **오토 모드** | 백그라운드 분류기가 판단하는 완전 자율 동작. v2.1.207부터 Bedrock/Vertex/Foundry에서 기본 제공됩니다 | 모드를 순환하려면 `Shift+Tab`, 또는 `--permission-mode auto` |
| **채널** | Discord·Telegram 연동 | `--channels` 플래그, Discord/Telegram 봇 |
| **음성 받아쓰기** | 명령과 컨텍스트를 말로 Claude에 전달 | `/voice` 커맨드 |
| **출력 스타일** | Claude의 역할, 어조, 기본 응답 형식을 변경 | `/config` → Output style, 또는 `outputStyle` 설정. 내장: Default, Proactive, Explanatory, Learning, Concise |
| **상태 표시줄** | 커맨드로 세션 하단 상태줄을 사용자 정의 | `/statusline`, 또는 `statusLine` 설정. 세션/모델/비용/컨텍스트 JSON을 stdin으로 받습니다 |
| **훅 (이벤트 33개)** | 유형 5개로 확장된 훅 시스템 | command, http, mcp_tool, prompt, agent 훅 유형 |
| **MCP 유도(Elicitation)** | MCP 서버가 실행 중에 사용자 입력을 요청할 수 있음 | 서버가 확인을 필요로 할 때 자동으로 프롬프트됩니다 |
| **플러그인 LSP** | 플러그인의 Language Server Protocol 지원 | `userConfig`, `${CLAUDE_PLUGIN_DATA}` 변수 |
| **원격 제어** | claude.ai 또는 Claude 앱에서 로컬 세션을 조작 | `claude --remote-control`(세션 안에서는 `/remote-control`) |
| **웹 세션** | claude.ai/code의 클라우드 세션 | 터미널에서 시작하려면 `claude --cloud "task"` |
| **데스크톱 앱** | 네이티브 데스크톱 애플리케이션 | claude.ai/download에서 내려받기 |
| **작업 목록** | 백그라운드 작업 관리 | `/tasks`(별칭 `/bashes`) |
| **자동 메모리** | 대화에서 메모리를 자동 저장 | Claude가 `~/.claude/projects/<project>/memory/MEMORY.md`에 노트를 저장하며, `/memory`로 관리합니다 |
| **AGENTS.md** *(v2.1.277)* | 도구 간 프로젝트 컨텍스트 파일로, 작업 디렉터리 또는 그 상위에 `CLAUDE.md`가 없을 때 프로젝트 지시사항으로 읽힙니다 | `/config`의 **Project instructions**에서 모드를 전환합니다. [AGENTS.md](02-memory/README.md#agentsmd) 참고 |
| **Git 워크트리** | 병렬 개발을 위한 격리된 작업 공간 | `claude --worktree <name>`(또는 `-w`) |
| **모델 선택** | Fable 5.1, Fable 5, Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5, Sonnet 4.6, Opus 4.8, Haiku 5.5, Haiku 4.5 사이를 전환 | `/model`(Anthropic API에서는 `sonnet`이 Sonnet 5.5로 해석됩니다, v2.1.284+) — v2.1.153부터 선택한 모델이 새 세션의 기본값으로 저장되며, `s`를 누르면 해당 세션에만 적용됩니다 |
| **에이전트 팀** | 여러 에이전트가 작업을 협업하도록 조정 | `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 환경변수로 활성화(실험적) |
| **동적 워크플로** *(v2.1.154)* | 결정론적 다중 에이전트 오케스트레이션. v2.1.219부터 기본 규모 기준은 medium입니다(에이전트 10개 미만 권장) | `/workflows`로 실행 기록 확인, Claude에게 생성을 요청, `/config`의 **Dynamic workflow size**에서 규모 변경 |
| **예약 작업** | `/loop`로 반복 작업 실행 | `/loop 5m /command` 또는 CronCreate 도구 |
| **Chrome 연동** | 브라우저 자동화 | `--chrome` 플래그 또는 `/chrome` 커맨드 |
| **키보드 사용자 정의** | 사용자 키 바인딩 | `/keybindings` 커맨드 |
| **/usage-credits** | 추가 사용 한도 설정(v2.1.144에서 `/extra-usage`에서 개명되었으며, 이전 이름도 별칭으로 동작합니다) | `/usage-credits` |
| **/run** *(v2.1.145+)* | 이 프로젝트의 앱을 실행해 변경 사항이 동작하는 모습 확인 | `/run` |
| **/verify** *(v2.1.145+)* | 앱을 빌드·실행·관찰해 수정이 실제로 동작하는지 확인(v2.1.215부터 명시적 호출만 가능하며, Claude가 스스로 트리거하지 않습니다) | `/verify` |
| **/run-skill-generator** *(v2.1.145+)* | 특정 프로젝트를 `/run`·`/verify`가 다루는 방법을 학습시킴 | `/run-skill-generator` |
| **서브에이전트 출력 스캔** *(v2.1.210+)* | 서브에이전트 보고서에서 프롬프트 인젝션 패턴을 스캔해 무력화 | 기본 활성화, 해제 불가 |
| **WebSearch 상한과 서브에이전트 팬아웃 한도** *(v2.1.212, v2.1.219 확장)* | 세션당 WebSearch 호출 200회. v2.1.290부터 대화형 세션에서는 시간당 100회씩 보충됩니다. 동시 서브에이전트 상한(기본 20)은 v2.1.217에서 추가되었고, v2.1.219부터 서브에이전트가 **기본 깊이 3**까지 중첩 서브에이전트를 생성할 수 있습니다(v2.1.217에서는 중첩이 비활성화되어 있었습니다). 세션당 서브에이전트 200개 생성 상한은 **v2.1.224에서 제거**되어, 이제 세션당 전체 서브에이전트 수에 제한이 없습니다 | `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`(기본 200, `/clear` 시 초기화), `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR`(대화형 기본 100, `-p` 사용 시 0), `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`(기본 20), `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`(기본 3, 1로 설정하면 비활성화) |
| **화면 판독기 모드** *(v2.1.208)* | 화면 판독기용 평문 렌더링 모드 | `--ax-screen-reader` 플래그, `CLAUDE_AX_SCREEN_READER=1`, 또는 설정의 `"axScreenReader": true` |
| **제한 모드(Restricted Mode)** *(v2.1.248+)* | 명령이나 코드를 실행하는 내장 도구(Bash, PowerShell 등)와 WebFetch를 제거합니다. 단 `--tools`로 개별 지정하면 사용할 수 있습니다(`default` 프리셋으로는 불가). 사용자·프로젝트·로컬 설정을 무시하며(관리형 설정과 `--settings`는 계속 적용), 파일 도구를 작업 디렉터리로 제한하고, `bypassPermissions`와 클라우드 세션을 거부합니다 | `claude --restricted`, 또는 `CLAUDE_CODE_RESTRICTED=1` |
| **서브에이전트 캐시 TTL** *(v2.1.248+)* | `experimental.cacheTtl` 에이전트 프론트매터 필드가 서브에이전트 프롬프트 캐시의 수명을 결정 | 에이전트 프론트매터에 `experimental:`과 `cacheTtl: "5m"`(또는 `"1h"`)을 추가합니다. [서브에이전트](04-subagents/README.md) 참고 |
| **서브에이전트 모델 강제** *(v2.1.257+)* | `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`이면 `CLAUDE_CODE_SUBAGENT_MODEL`이 에이전트 프론트매터를 덮어씁니다. v2.1.251부터는 이 값을 설정하지 않는 한 프론트매터(`model: inherit` 포함)가 우선하여 환경변수가 기본으로 이기지 않습니다 | `CLAUDE_CODE_SUBAGENT_MODEL=sonnet CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1 claude` |

---

## 팁과 요령

### 사용자 정의
- 예제를 그대로 시작합니다
- 필요에 맞게 수정합니다
- 팀에 공유하기 전에 테스트합니다
- 설정을 버전 관리합니다

### 권장 사례
- 팀 표준에는 메모리를 사용합니다
- 완성된 워크플로에는 플러그인을 사용합니다
- 복잡한 작업에는 서브에이전트를 사용합니다
- 빠른 작업에는 슬래시 커맨드를 사용합니다

### 문제 해결
```bash
# Check file locations
ls -la .claude/commands/
ls -la .claude/agents/

# Verify YAML syntax
head -20 .claude/agents/code-reviewer.md

# Test MCP connection
echo $GITHUB_PERSONAL_ACCESS_TOKEN
```

---

## 📊 기능 매트릭스

| 필요 | 사용할 것 | 예시 |
|------|----------|---------|
| 빠른 단축 실행 | 슬래시 커맨드 (60+) | `01-slash-commands/optimize.md` |
| 팀 표준 | 메모리 | `02-memory/project-CLAUDE.md` |
| 자동 워크플로 | 스킬 | `03-skills/code-review-specialist/` |
| 특화된 작업 | 서브에이전트 | `04-subagents/code-reviewer.md` |
| 외부 데이터 | MCP (+ 유도) | `05-mcp/github-mcp.json` |
| 이벤트 자동화 | 훅 (이벤트 33개, 유형 5개) | `06-hooks/pre-commit.sh` |
| 완성된 솔루션 | 플러그인 (+ LSP 지원) | `07-plugins/pr-review/` |
| 안전한 실험 | 체크포인트 | `08-checkpoints/checkpoint-examples.md` |
| 완전 자율 동작 | 오토 모드 | `--permission-mode auto` 또는 `Shift+Tab` |
| 채팅 연동 | 채널 | `--channels` (Discord, Telegram) |
| CI/CD 파이프라인 | CLI | `10-cli/README.md` |

---

## 🔗 빠른 링크

- **기본 가이드**: `README.md`
- **전체 색인**: `INDEX.md`
- **원본 가이드**: `claude_concepts_guide.md`

---

## 📞 자주 묻는 질문

**Q: 어떤 것을 써야 하나요?**
A: 슬래시 커맨드부터 시작하고, 필요에 따라 기능을 추가합니다.

**Q: 기능을 섞어 써도 되나요?**
A: 물론입니다! 기능들은 함께 동작합니다. 메모리 + 커맨드 + MCP = 강력합니다.

**Q: 팀과 어떻게 공유하나요?**
A: `.claude/` 디렉터리를 git에 커밋합니다.

**Q: 비밀 값은 어떻게 하나요?**
A: 환경변수를 사용하고, 절대 하드코딩하지 않습니다.

**Q: 예제를 수정해도 되나요?**
A: 물론입니다! 예제는 사용자 정의용 템플릿입니다.

---

## ✅ 체크리스트

시작하기 체크리스트:

- [ ] `README.md`를 읽습니다
- [ ] 슬래시 커맨드 1개를 설치합니다
- [ ] 그 커맨드를 사용해 봅니다
- [ ] 프로젝트 `CLAUDE.md`를 만듭니다
- [ ] 서브에이전트 1개를 설치합니다
- [ ] MCP 연동 1개를 설정합니다
- [ ] 스킬 1개를 설치합니다
- [ ] 완성된 플러그인을 사용해 봅니다
- [ ] 필요에 맞게 사용자 정의합니다
- [ ] 팀과 공유합니다

---

**빠른 시작**: `cat README.md`

**전체 색인**: `cat INDEX.md`

**이 카드**: 빠른 참조용으로 가까이 두세요!

---

**마지막 업데이트**: 2026년 10월 18일
**Claude Code 버전**: 2.1.302
**출처**:
- https://code.claude.com/docs/en/workflows#set-a-size-guideline
- https://code.claude.com/docs/en/memory#agents-md
- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/cli-reference
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/env-vars
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/memory#storage-location
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/managed-settings
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/code-review-local
**호환 모델**: Claude Fable 5.1, Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
