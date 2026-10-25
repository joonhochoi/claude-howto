<!-- i18n-source: 05-mcp/README.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (Model Context Protocol)

이 폴더에는 Claude Code에서의 MCP 서버 구성과 사용법에 관한 종합 문서와 예제가 포함되어 있습니다.

## 개요

MCP(Model Context Protocol)는 Claude가 외부 도구, API, 실시간 데이터 소스에 접근하는 표준화된 방식입니다. 메모리와 달리 MCP는 변화하는 데이터에 대한 실시간 접근을 제공합니다.

주요 특징:
- 외부 서비스에 대한 실시간 접근
- 실시간 데이터 동기화
- 확장 가능한 아키텍처
- 안전한 인증
- 도구 기반 상호작용

## MCP 아키텍처

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
```

## MCP 생태계

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["Local Files"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Slack Workspace"]
    F -->|Docs| K["Google Drive"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#f3e5f5,stroke:#333,color:#333
    style G fill:#e8f5e9,stroke:#333,color:#333
    style H fill:#e8f5e9,stroke:#333,color:#333
    style I fill:#e8f5e9,stroke:#333,color:#333
    style J fill:#e8f5e9,stroke:#333,color:#333
    style K fill:#e8f5e9,stroke:#333,color:#333
```

## MCP 설치 방법

Claude Code는 MCP 서버 연결을 위해 여러 전송 프로토콜을 지원합니다.

### HTTP 전송 (권장)

```bash
# Basic HTTP connection
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP with authentication header
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### stdio 전송 (로컬)

로컬에서 실행되는 MCP 서버용입니다.

```bash
# Local Node.js server
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# With environment variables
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

#### stdio 서버용 `CLAUDE_PROJECT_DIR` (v2.1.139+)

모든 MCP stdio 서버는 환경에 `CLAUDE_PROJECT_DIR=<저장소 루트의 절대 경로>`가 이미 설정된 상태로 실행됩니다. 훅에서 쓰는 것과 동일한 규칙입니다. 플러그인 및 프로젝트 `.mcp.json` 파일은 `command`, `args`, `env` 값에서 `${CLAUDE_PROJECT_DIR}`를 참조할 수 있으며, 치환은 `execve()` 이전에 이루어집니다.

```json
{
  "mcpServers": {
    "repo-tools": {
      "type": "stdio",
      "command": "node",
      "args": ["${CLAUDE_PROJECT_DIR:-.}/.claude/mcp/repo-tools.js"],
      "env": {
        "REPO_ROOT": "${CLAUDE_PROJECT_DIR:-.}"
      }
    }
  }
}
```

> **참고**: 프로젝트·로컬·사용자 구성에서는 기본값을 붙여 `${CLAUDE_PROJECT_DIR:-.}` 형태로 작성하세요. 이 변수는 Claude Code 자체가 아니라 서버의 환경에 설정되기 때문입니다. `${CLAUDE_PROJECT_DIR}`를 직접 치환하는 것은 플러그인 MCP 구성뿐입니다.

stdio 서버가 Claude Code를 어디서 실행했든 프로젝트 루트를 기준으로 파일을 읽어야 할 때 사용하세요.

stdio MCP 서버는 `CLAUDE_CODE_SESSION_ID`도 함께 받습니다(훅과 Bash에 전달되는 값과 동일). 세션을 `--resume`으로 재개한 경우에도 마찬가지입니다(v2.1.163+).

### SSE 전송 (지원 중단)

Server-Sent Events 전송은 `http`로 대체되어 지원이 중단되었지만 여전히 동작합니다.

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### WebSocket 전송 (`ws`)

WebSocket 서버는 지속적인 양방향 연결을 유지하므로, Claude에 이벤트를 스스로 밀어 넣는 원격 MCP 서버에 적합합니다. 서버가 요청에만 응답한다면 HTTP를 사용하세요. HTTP는 OAuth와 `claude mcp add --transport` 플래그를 지원하지만 WebSocket은 둘 다 지원하지 않습니다.

`--transport`는 `ws`를 받지 않으므로 `.mcp.json`이나 `claude mcp add-json`으로 구성합니다.

```json
{
  "type": "ws",
  "url": "wss://mcp.example.com/socket",
  "headers": {
    "Authorization": "Bearer YOUR_TOKEN"
  }
}
```

`type: "ws"` 항목은 `http`와 동일한 `url`, `headers`, `headersHelper`, `timeout`, `alwaysLoad` 필드를 받습니다. 인증은 **헤더 전용**이며, WebSocket 서버를 위한 OAuth 플로는 없습니다.

> **참고**: v2.1.285부터 `claude mcp list`가 WebSocket(`ws`) 서버를 URL, 상태와 함께 표시합니다(이전 버전에서는 누락되었습니다). `claude mcp get <name>`이나 `/mcp` 패널로도 확인할 수 있습니다.

HTTP, SSE와 마찬가지로 WebSocket 연결은 5분 유휴 창을 사용합니다. stdio와 WebSocket에는 요청별 타이머가 없습니다. `type` 없이 `url` 항목만 두면 오류이며, 이때 유효한 값으로 `"http"`, `"sse"`, `"ws"`가 안내됩니다.

### 세션 작업 디렉터리 (roots/list)

MCP 서버는 세션의 작업 디렉터리를 알 수 있습니다. 실행 디렉터리와 모든 `--add-dir`/`additionalDirectories` 항목이 MCP `roots/list` 요청으로 반환되며, 집합이 바뀔 때마다 `notifications/roots/list_changed` 알림이 전송됩니다(v2.1.203). 이제 유휴 타임아웃이 stdio 서버에도 적용되며(30분), 서버별 `timeout`이 유휴 하한으로 동작합니다(v2.1.203).

### Windows 관련 참고 사항

네이티브 Windows(WSL 아님)에서는 npx 명령에 `cmd /c`를 사용하세요.

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### OAuth 2.0 인증

Claude Code는 OAuth가 필요한 MCP 서버에 대해 OAuth 2.0을 지원합니다. OAuth 지원 서버에 연결할 때 Claude Code가 인증 플로 전체를 처리합니다.

```bash
# Connect to an OAuth-enabled MCP server (interactive flow)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# Pre-configure OAuth credentials for non-interactive setup
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| 기능 | 설명 |
|---------|-------------|
| **대화형 OAuth** | `/mcp`를 사용해 브라우저 기반 OAuth 플로를 시작합니다 |
| **미리 구성된 OAuth 클라이언트** | Notion, Stripe 등 주요 서비스용 기본 제공 OAuth 클라이언트(v2.1.30+) |
| **미리 구성된 자격 증명** | 자동 설정을 위한 `--client-id`, `--client-secret`, `--callback-port` 플래그 |
| **토큰 저장** | 토큰은 시스템 키체인에 안전하게 저장됩니다 |
| **단계별 인증** | 권한이 필요한 작업에 대해 단계별 인증(step-up authentication)을 지원합니다 |
| **검색 캐싱** | OAuth 검색 메타데이터를 캐시해 재연결 속도를 높입니다 |
| **메타데이터 재정의** | `.mcp.json`의 `oauth.authServerMetadataUrl`로 기본 OAuth 메타데이터 검색을 재정의합니다 |

#### OAuth 메타데이터 검색 재정의

MCP 서버가 표준 OAuth 메타데이터 엔드포인트(`/.well-known/oauth-authorization-server`)에서 오류를 반환하지만 정상 동작하는 OIDC 엔드포인트를 제공한다면, Claude Code가 지정한 URL에서 OAuth 메타데이터를 가져오도록 지시할 수 있습니다. 서버 구성의 `oauth` 객체에 `authServerMetadataUrl`을 설정하세요.

```json
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "authServerMetadataUrl": "https://auth.example.com/.well-known/openid-configuration"
      }
    }
  }
}
```

URL은 `https://`를 사용해야 합니다. 이 옵션은 Claude Code v2.1.64 이상이 필요합니다.

#### 인증 시작 알림과 동적 헤더 갱신 (v2.1.193)

- **시작 시 인증 알림(v2.1.193+)**: 시작할 때 Claude Code가 아직 인증이 필요한 MCP 서버 목록을 알림으로 표시합니다. 로그인이 필요한 서버가 조용히 동작하지 않는 상태로 남지 않습니다.
- **`headersHelper` 자동 갱신(v2.1.193+)**: `headersHelper`로 사용자 지정 인증을 제공하는 경우, 서버가 HTTP 401 또는 403을 반환하면 헬퍼가 자동으로 다시 호출됩니다. 수동 재연결 없이 자격 증명이 즉시 갱신됩니다. [사용자 지정 인증을 위한 동적 헤더 사용](https://code.claude.com/docs/en/mcp)을 참고하세요.

> **경고**(v2.1.238): 이제 프로젝트 `.mcp.json`의 `headersHelper`와, 프로젝트 또는 `--add-dir` 에이전트 파일에 인라인으로 정의된 MCP 서버는 해당 폴더의 신뢰 대화상자가 승인되어 있어야 합니다. `claude -p`에서도 마찬가지입니다. 또한 이런 헬퍼는 **자격 증명 환경변수를 상속하지 않고** 실행됩니다. 사용자·관리형·claude.ai 스코프의 헬퍼는 대신 Claude 구성 디렉터리에서 실행됩니다. 상속된 자격 증명이나 신뢰되지 않은 실행에 의존하던 프로젝트 구성은 신뢰 대화상자를 승인하고 자격 증명을 다른 방식으로 제공할 때까지 동작하지 않습니다.

### Claude.ai MCP 커넥터

Claude.ai 계정에 구성한 MCP 서버는 Claude Code에서 자동으로 사용할 수 있습니다. 즉, Claude.ai 웹 인터페이스로 설정한 MCP 연결은 추가 구성 없이 접근할 수 있습니다.

Claude.ai MCP 커넥터는 `--print` 모드에서도 사용할 수 있어(v2.1.83+) 비대화형·스크립트 사용이 가능합니다.

> **시작 관련 참고(v2.1.117+)**: 로컬 MCP 서버와 claude.ai MCP 서버가 모두 구성된 경우 동시 연결이 기본값입니다(이전에는 순차). 여러 서버를 사용할 때 시작 지연이 줄어듭니다.

Claude Code에서 Claude.ai MCP 서버를 비활성화하려면 `ENABLE_CLAUDEAI_MCP_SERVERS` 환경변수를 `false`로 설정하세요.

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **참고:** 이 기능은 Claude.ai 계정으로 로그인한 사용자에게만 제공됩니다.

## MCP 설정 과정

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as External Service

    User->>Claude: Type /mcp
    Claude->>Claude: List available MCP servers
    Claude->>User: Show options
    User->>Claude: Select GitHub MCP
    Claude->>Config: Update configuration
    Config->>Claude: Activate connection
    Claude->>Service: Test connection
    Service-->>Claude: Authentication successful
    Claude->>User: ✅ MCP connected!
```

### `/mcp` 명령

세션 안에서 `/mcp`를 입력하면 연결된 서버 목록을 확인하고, OAuth 플로를 시작하고, 연결 상태를 검사할 수 있습니다.

- **v2.1.121**부터 MCP는 일시적 오류 발생 시 초기 연결을 최대 3회 재시도합니다.
- **v2.1.128**부터 `/mcp`가 연결된 각 서버의 **도구 개수**를 표시하고, **도구 0개**를 보고하는 서버를 시각적으로 표시해 잘못 구성된 서버를 한눈에 알아볼 수 있습니다.

## MCP 도구 검색

도구 검색은 기본으로 켜져 있습니다. MCP 도구는 지연되고 필요할 때 검색되므로 도구 정의가 모델 컨텍스트를 채우지 않습니다. `ANTHROPIC_BASE_URL`이 자체 호스팅이 아닌 호스트를 가리키면 Claude Code가 이 기능을 끕니다. 대부분의 프록시가 필요한 블록을 전달하지 않기 때문입니다.

| 설정 | 값 | 설명 |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | (설정 안 함 — 기본값) | 모든 MCP 도구를 지연시키고 필요할 때 로드합니다 |
| `ENABLE_TOOL_SEARCH` | `auto` | 임계값 모드: 도구 정의가 컨텍스트 창의 10%에 도달할 때까지 미리 로드하고, 이후 모두 지연합니다 |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | 사용자 지정 비율(0-100)을 쓰는 임계값 모드 — 예를 들어 5%는 `auto:5`입니다 |
| `ENABLE_TOOL_SEARCH` | `true` | 모든 MCP 도구를 지연합니다 |
| `ENABLE_TOOL_SEARCH` | `false` | 비활성화. 모든 도구 설명을 전부 전송합니다 |

> **참고:** 도구 검색은 `tool_reference` 블록을 지원하는 모델이 필요합니다. Claude Opus 4, Claude Sonnet 4, Claude Haiku 4.5 및 이후 모델(Google Cloud의 Agent Platform에서는 Opus 4.5, Sonnet 4.5, Haiku 4.5 이후)입니다.

### 서버별 도구 검색 우회 (v2.1.121+)

특정 MCP 서버의 도구가 매 턴 필요하다면 해당 구성에 `"alwaysLoad": true`를 지정해 도구 검색 지연을 건너뛰고 도구를 항상 사용 가능한 상태로 유지하세요.

```json
{
  "mcpServers": {
    "always-on-tool": {
      "command": "node",
      "args": ["./tools/always.js"],
      "alwaysLoad": true
    }
  }
}
```

아껴 쓰세요. 항상 로드되는 도구는 모두 컨텍스트를 소비하며, 그 컨텍스트는 도구 검색이 더 관련성 높은 도구를 찾아내는 데 쓰일 수 있었던 몫입니다.

서버의 모든 도구를 도구 검색 뒤에 두려면 해당 서버 항목에 `"alwaysLoad": false`를 설정하세요(v2.1.287+). 여기에는 서버 작성자가 미리 로드하도록 표시한 도구도 포함됩니다. `alwaysLoad`를 비워 두면 표시된 도구는 미리 로드됩니다. 서버 작성자는 개별 도구의 `_meta` 객체에 `"anthropic/alwaysLoad"`를 설정해 도구를 표시하며, 구성의 서버 수준 `alwaysLoad` 설정이 이를 재정의할 수 있습니다.

## 동적 도구 업데이트

Claude Code는 MCP `list_changed` 알림을 지원합니다. MCP 서버가 사용 가능한 도구를 동적으로 추가·제거·수정하면 Claude Code가 업데이트를 받아 도구 목록을 자동으로 조정합니다. 재연결이나 재시작이 필요 없습니다.

## MCP 앱

MCP Apps는 첫 번째 공식 MCP 확장으로, MCP 도구 호출이 채팅 인터페이스에 직접 렌더링되는 대화형 UI 컴포넌트를 반환할 수 있게 합니다. MCP 서버는 일반 텍스트 응답 대신 풍부한 대시보드, 폼, 데이터 시각화, 다단계 워크플로를 제공할 수 있으며, 대화를 떠나지 않고 모두 인라인으로 표시됩니다.

## MCP Elicitation (정보 요청)

MCP 서버는 대화형 대화상자를 통해 사용자에게 구조화된 입력을 요청할 수 있습니다(v2.1.49+). 이를 통해 MCP 서버가 워크플로 중간에 추가 정보를 요청할 수 있습니다. 예를 들어 확인을 요구하거나, 옵션 목록에서 선택하게 하거나, 필수 필드를 채우게 하는 식으로 MCP 서버 상호작용에 상호작용성을 더합니다.

## 도구 설명 및 지침 길이 제한

Claude Code는 장황한 서버가 컨텍스트를 부풀리지 않도록 각 MCP 도구 설명과 각 서버 지침을 잘라냅니다. 기본 한도는 서버 지침과 미리 로드되는 도구 설명의 경우 **4,096자**(v2.1.296. 그 전까지 v2.1.84부터는 2,048자), 도구 검색을 통해 Claude가 로드하는 설명의 경우 **16,384자**입니다(v2.1.295). v2.1.280부터 `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH`가 이를 재정의합니다. 설정한 숫자가 **두 한도를 모두** 대체합니다(`8192`는 짧은 쪽을 올리고 긴 쪽을 내립니다). v2.1.299부터 `api.anthropic.com`의 Anthropic 자사 MCP 서버가 보내는 설명과 지침은 전부 Claude에 도달합니다. 중요한 세부 정보는 설명 앞부분에 두세요.

## 슬래시 커맨드로서의 MCP 프롬프트

MCP 서버는 Claude Code에서 슬래시 커맨드로 표시되는 프롬프트를 노출할 수 있습니다. 프롬프트는 다음 명명 규칙으로 접근합니다.

```
/mcp__<server>__<prompt>
```

예를 들어 `github`라는 서버가 `review`라는 프롬프트를 노출한다면 `/mcp__github__review`로 호출할 수 있습니다.

## 서버 중복 제거

같은 MCP 서버가 여러 스코프(로컬, 프로젝트, 사용자)에 정의되어 있으면 로컬 구성이 우선합니다. 따라서 충돌 없이 프로젝트 수준 또는 사용자 수준 MCP 설정을 로컬 사용자 지정으로 재정의할 수 있습니다.

## 최근 수명 주기 수정 사항 (v2.1.136)

v2.1.136에서 오래된 MCP 수명 주기 버그 두 개가 수정되었습니다. 다중 서버 구성을 사용한다면 업그레이드할 만합니다.

- **MCP 서버가 `/clear` 후에도 유지**: `.mcp.json`, 플러그인, claude.ai 커넥터로 구성한 서버가 VS Code, JetBrains, Agent SDK에서 `/clear` 후 사라지지 않습니다. 이전 버전에서는 조용히 제거되어 재시작이 필요했습니다.
- **OAuth 리프레시 토큰 동시 갱신 수정**: 여러 서버가 동시에 갱신을 시도할 때 다중 서버 OAuth 구성에서 리프레시 토큰을 잃지 않습니다. OAuth로 보호되는 MCP 서버를 여러 개 쓰는 구성에서 나타나던 "매일 아침 다시 인증해야 하는" 패턴이 사라집니다.

## @ 멘션을 통한 MCP 리소스

`@` 멘션 문법으로 프롬프트에서 MCP 리소스를 직접 참조할 수 있습니다.

```
@server-name:protocol://resource/path
```

예를 들어 특정 데이터베이스 리소스를 참조하려면 다음과 같이 합니다.

```
@database:postgres://mydb/users
```

이를 통해 Claude가 MCP 리소스 내용을 대화 컨텍스트의 일부로 인라인으로 가져와 포함할 수 있습니다.

## MCP 스코프

MCP 구성은 공유 수준이 다른 여러 스코프에 저장할 수 있습니다.

| 스코프 | 플래그 | 위치 | 설명 | 공유 대상 | 승인 필요 |
|-------|------|----------|-------------|-------------|------------------|
| **로컬** (기본값) | `--scope local` | `~/.claude.json`(프로젝트 경로 아래) | 현재 사용자, 현재 프로젝트 전용(이전 버전에서는 `project`라고 불렀습니다) | 본인만 | 아니요 |
| **프로젝트** | `--scope project` | `.mcp.json` | git 저장소에 커밋됩니다 | 팀 구성원 | 예(첫 사용 시) |
| **사용자** | `--scope user` | `~/.claude.json` | 모든 프로젝트에서 사용 가능(이전 버전에서는 `global`이라고 불렀습니다) | 본인만 | 아니요 |

서버를 추가할 때 `--scope`(단축형 `-s`)로 스코프를 선택하세요. 생략하면 Claude Code는 `local`을 사용합니다.

```bash
# Project scope — writes to .mcp.json so the team shares it
claude mcp add --scope project --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# User scope — available in every project
claude mcp add --scope user --transport stdio memory -- npx @modelcontextprotocol/server-memory
```

### 프로젝트 스코프 사용

프로젝트별 MCP 구성은 `.mcp.json`에 저장하세요.

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

팀 구성원은 프로젝트 MCP를 처음 사용할 때 승인 프롬프트를 보게 됩니다. 신뢰되지 않은 워크스페이스에서는 저장소가 커밋된 `.claude/settings.json`으로 자체 승인한 서버를 `claude mcp list`/`get`이 **자동으로 실행하지 않습니다**. 신뢰 대화상자를 승인할 때까지 `⏸ Pending approval`로 표시되며, 신뢰되지 않은 폴더에서는 `enableAllProjectMcpServers`가 무시됩니다(v2.1.196).

## MCP 구성 관리

### MCP 서버 추가

```bash
# Add HTTP-based server
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# Add local stdio server
claude mcp add --transport stdio database -- npx @company/db-server

# List all MCP servers
claude mcp list

# Get details on specific server
claude mcp get github

# Remove an MCP server
claude mcp remove github

# Reset project-specific approval choices
claude mcp reset-project-choices

# Authenticate an MCP server from the CLI (v2.1.186+)
claude mcp login github

# Sign out of an MCP server (v2.1.186+)
claude mcp logout github

# Import from Claude Desktop
claude mcp add-from-claude-desktop

# Add a server from a JSON blob (useful for scripted setup)
claude mcp add-json events-server '{"type":"stdio","command":"npx","args":["@modelcontextprotocol/server-events"]}'
```

> **참고**: JSON 구성(`.mcp.json`, `~/.claude.json`, `claude mcp add-json`)에서 `type` 필드는 `http`의 별칭으로 `streamable-http`를 받습니다. MCP 명세는 이 전송을 `streamable-http`라는 이름으로 부르므로, 서버 자체 문서에서 복사한 구성이 수정 없이 동작합니다.

v2.1.238부터 `claude mcp list`와 `claude mcp get`은 비활성화된 서버를 상태 확인을 위해 연결하지 않고 `⊘ Disabled`로 표시합니다.

`claude mcp login <name>` / `claude mcp logout <name>`은 `/mcp` 메뉴의 OAuth 플로에 대한 비대화형 대응입니다. 메뉴를 열지 않고 인증하거나 로그아웃할 수 있습니다. SSH 또는 헤드리스 세션에서 OAuth를 완료하려면 `login`에 `--no-browser`를 추가하세요(플로를 stdin으로 우회합니다).

## 사용 가능한 MCP 서버 표

| MCP 서버 | 용도 | 일반적인 도구 | 인증 | 실시간 |
|------------|---------|--------------|------|-----------|
| **Filesystem** | 파일 작업 | read, write, delete | OS 권한 | ✅ 예 |
| **GitHub** | 저장소 관리 | list_prs, create_issue, push | OAuth | ✅ 예 |
| **Slack** | 팀 커뮤니케이션 | send_message, list_channels | Token | ✅ 예 |
| **Database** | SQL 쿼리 | query, insert, update | 자격 증명 | ✅ 예 |
| **Google Docs** | 문서 접근 | read, write, share | OAuth | ✅ 예 |
| **Asana** | 프로젝트 관리 | create_task, update_status | API Key | ✅ 예 |
| **Stripe** | 결제 데이터 | list_charges, create_invoice | API Key | ✅ 예 |
| **Memory** | 영구 메모리 | store, retrieve, delete | 로컬 | ❌ 아니요 |

## 실전 예제

### 예제 1: GitHub MCP 구성

**파일:** `.mcp.json`(프로젝트 루트)

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

**사용 가능한 GitHub MCP 도구:**

#### PR 관리
- `list_prs` - 저장소의 모든 PR 목록
- `get_pr` - diff를 포함한 PR 세부 정보 조회
- `create_pr` - 새 PR 생성
- `update_pr` - PR 설명/제목 수정
- `merge_pr` - PR을 main 브랜치에 병합
- `review_pr` - 리뷰 코멘트 추가

**예제 요청:**
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### 이슈 관리
- `list_issues` - 모든 이슈 목록
- `get_issue` - 이슈 세부 정보 조회
- `create_issue` - 새 이슈 생성
- `close_issue` - 이슈 닫기
- `add_comment` - 이슈에 코멘트 추가

#### 저장소 정보
- `get_repo_info` - 저장소 세부 정보
- `list_files` - 파일 트리 구조
- `get_file_content` - 파일 내용 읽기
- `search_code` - 코드베이스 전체 검색

#### 커밋 작업
- `list_commits` - 커밋 기록
- `get_commit` - 특정 커밋 세부 정보
- `create_commit` - 새 커밋 생성

**설정**:
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
# Or use the CLI to add directly:
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

### 구성에서의 환경변수 확장

MCP 구성은 기본값 대체가 있는 환경변수 확장을 지원합니다. `${VAR}` 및 `${VAR:-default}` 문법은 `command`, `args`, `env`, `url`, `headers` 필드에서 동작합니다.

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}",
        "X-Custom-Header": "${CUSTOM_HEADER:-default-value}"
      }
    },
    "local-server": {
      "command": "${MCP_BIN_PATH:-npx}",
      "args": ["${MCP_PACKAGE:-@company/mcp-server}"],
      "env": {
        "DB_URL": "${DATABASE_URL:-postgresql://localhost/dev}"
      }
    }
  }
}
```

변수는 런타임에 확장됩니다.
- `${VAR}` - 환경변수를 사용합니다. 설정되지 않았고 기본값도 없으면 서버는 리터럴 `${VAR}` 상태로 로드되며, `claude mcp list`와 `/mcp`가 누락된 변수에 대해 경고합니다
- `${VAR:-default}` - 환경변수를 사용하고, 설정되지 않았으면 기본값으로 대체합니다

### 예제 2: 데이터베이스 MCP 설정

**구성:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--dsn", "${DATABASE_URL}"]
    }
  }
}
```

**사용 예:**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# Using MCP database tool:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Results:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

**설정**:
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
claude mcp add --transport stdio database -- npx -y @bytebase/dbhub \
  --dsn "$DATABASE_URL"
```

> **경고**: 이 설정은 Claude에 쓰기 권한을 부여합니다. DBHub의 `execute_sql` 도구는 읽기 전용 모드를 켜지 않으면 `UPDATE`, `DELETE`, `DROP`을 포함해 받은 모든 SQL을 실행합니다. 로컬 또는 일회용 데이터베이스를 사용하고, 프로덕션은 절대 사용하지 마세요.

**읽기 전용 설정(권장):**

`SELECT`만 실행할 수 있는 데이터베이스 사용자를 만드세요(PostgreSQL 예시).

```sql
CREATE ROLE claude_readonly LOGIN PASSWORD 'change-me';
GRANT CONNECT ON DATABASE mydb TO claude_readonly;
GRANT USAGE ON SCHEMA public TO claude_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO claude_readonly;
```

`dbhub.toml`에서 읽기 전용 모드를 켜세요. 예전 `--readonly` 플래그는 더 이상 동작하지 않습니다. DBHub가 환경에서 `${DATABASE_URL}`을 채우므로 파일에 자격 증명이 들어가지 않습니다.

```toml
[[sources]]
id = "default"
dsn = "${DATABASE_URL}"

[[tools]]
name = "execute_sql"
source = "default"
readonly = true
```

그다음 `--dsn`을 전달하는 대신 DBHub가 이 파일을 가리키게 하세요. Claude Code는 같은 이름의 서버를 두 번째로 추가하지 않으므로, 위에서 추가한 쓰기 권한 `database` 서버를 먼저 제거하세요.

```bash
# Replace the write-access server added above
claude mcp remove database
export DATABASE_URL="postgresql://claude_readonly:change-me@localhost/mydb"
claude mcp add --transport stdio database -- npx -y @bytebase/dbhub \
  --config "$PWD/dbhub.toml"
```

읽기 전용 모드는 SQL 텍스트를 필터링하며 과거에 우회 사례가 있었습니다(DBHub 0.22.6에서 수정). 따라서 실제로 데이터를 보호하는 것은 `SELECT` 전용 사용자입니다. [DBHub 읽기 전용 모드](https://dbhub.ai/tools/execute-sql#read-only-mode)를 참고하세요.

### 예제 3: 다중 MCP 워크플로

**시나리오: 일일 보고서 생성**

```markdown
# Daily Report Workflow using Multiple MCPs

## Setup
1. GitHub MCP - fetch PR metrics
2. Database MCP - query sales data
3. Slack MCP - post report
4. Filesystem MCP - save report

## Workflow

### Step 1: Fetch GitHub Data
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Step 2: Query Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Step 3: Generate Report
Combine data into HTML report

### Step 4: Save to Filesystem
Write report.html to /reports/

### Step 5: Post to Slack
Send summary to #daily-reports channel

Final Output:
✅ Report generated and posted
📊 47 PRs merged this week
💰 $12,450 in daily sales
```

**설정**:
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_BOT_TOKEN="your_slack_bot_token"
export SLACK_TEAM_ID="your_slack_team_id"
# Add each MCP server via the CLI or configure them in .mcp.json
```

### 예제 4: Filesystem MCP 작업

**구성:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    }
  }
}
```

**사용 가능한 작업:**

| 작업 | 명령 | 용도 |
|-----------|---------|---------|
| 파일 목록 | `ls ~/projects` | 디렉터리 내용 표시 |
| 파일 읽기 | `cat src/main.ts` | 파일 내용 읽기 |
| 파일 쓰기 | `create docs/api.md` | 새 파일 생성 |
| 파일 편집 | `edit src/app.ts` | 파일 수정 |
| 검색 | `grep "async function"` | 파일 내 검색 |
| 삭제 | `rm old-file.js` | 파일 삭제 |

**설정**:
```bash
# Use the CLI to add directly:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## MCP vs 메모리: 의사 결정 매트릭스

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

## 요청/응답 패턴

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
    App->>App: Process result
    App->>App: Continue task

    Note over MCP,DB: Real-time access<br/>No caching
```

## 환경변수

민감한 자격 증명은 환경변수에 저장하세요.

```bash
# ~/.bashrc or ~/.zshrc
export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_BOT_TOKEN="your-slack-bot-token"
export SLACK_TEAM_ID="T0000000000"
```

그런 다음 MCP 구성에서 참조합니다.

```json
{
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
  }
}
```

## MCP 서버로서의 Claude (`claude mcp serve`)

Claude Code 자체가 다른 애플리케이션을 위한 MCP 서버 역할을 할 수 있습니다. 이를 통해 외부 도구, 편집기, 자동화 시스템이 표준 MCP 프로토콜로 Claude의 기능을 활용할 수 있습니다.

```bash
# Start Claude Code as an MCP server on stdio
claude mcp serve
```

다른 애플리케이션은 stdio 기반 MCP 서버에 연결하듯 이 서버에 연결할 수 있습니다. 예를 들어 다른 Claude Code 인스턴스에 Claude Code를 MCP 서버로 추가하려면 다음과 같이 합니다.

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

한 Claude 인스턴스가 다른 인스턴스를 조율하는 다중 에이전트 워크플로를 만들 때 유용합니다.

## 관리형 MCP 구성 (엔터프라이즈)

엔터프라이즈 배포에서 IT 관리자는 두 가지 별개 메커니즘으로 MCP 서버 정책을 적용합니다. 하나는 고정된 서버 집합을 독점 제어로 배포하는 `managed-mcp.json` 파일이고, 다른 하나는 구성된 서버 중 어떤 것이 로드될 수 있는지 필터링하는 `allowedMcpServers` / `deniedMcpServers` 설정 키입니다.

**위치:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux 및 WSL: `/etc/claude-code/managed-mcp.json`
- Windows: `C:\Program Files\ClaudeCode\managed-mcp.json`

`managed-mcp.json`은 프로젝트 `.mcp.json`과 같은 형식(최상위 `mcpServers` 맵)을 사용합니다. 이 파일은 서버를 배포하며, 필터링하지는 않습니다.

```json
{
  "mcpServers": {
    "example-remote": {
      "type": "http",
      "url": "https://mcp.example.com/mcp"
    },
    "company-internal": {
      "type": "stdio",
      "command": "/usr/local/bin/company-mcp-server",
      "args": ["--config", "/etc/company/mcp-config.json"]
    }
  }
}
```

머신의 모든 사용자가 이 파일을 읽을 수 있으므로 `env` 블록에 자격 증명을 절대 넣지 마세요. 대신 `${VAR}` 확장, OAuth, `headersHelper`를 사용하세요.

**필터링: 허용 목록과 차단 목록**

`allowedMcpServers`, `deniedMcpServers`, `allowAllClaudeAiMcps`는 **`managed-mcp.json`의 필드가 아니라 설정 키**입니다. 이를 강제하려면 관리형 설정 소스(서버 관리형 설정, `managed-settings.json`, MDM 프로파일, 레지스트리)에 넣어야 합니다.

- `allowedMcpServers` -- 허용되는 서버의 허용 목록입니다. 같은 관리형 소스에서 `allowManagedMcpServersOnly: true`를 함께 설정하세요. 그렇지 않으면 허용 목록이 모든 스코프에서 병합되어 사용자가 여러분의 목록을 넓힐 수 있습니다.
- `deniedMcpServers` -- 차단되는 서버의 차단 목록입니다. 이 목록은 항상 모든 스코프에서 병합됩니다.
- `allowAllClaudeAiMcps` -- 배포된 `managed-mcp.json`과 함께 claude.ai 클라우드 커넥터를 로드합니다(v2.1.149+). 관리자 제어 정책 계층에서만 읽습니다.

각 항목은 **단일** 키를 가진 객체입니다.

| 키 | 일치 대상 |
|-----|---------|
| `serverUrl` | 원격 서버 URL. 정확히 일치하거나 `*` 와일드카드 사용 |
| `serverCommand` | stdio 서버를 시작하는 정확한 명령과 인자의 배열 — 모든 인자를 순서대로 |
| `serverName` | 사용자가 지정한 레이블. **정확히 일치해야 하며 와일드카드는 확장되지 않습니다** |

**구성 예시:**

```json
{
  "allowedMcpServers": [
    { "serverUrl": "https://mcp.example.com/*" },
    { "serverCommand": ["/usr/local/bin/company-mcp-server", "--config", "/etc/company/mcp-config.json"] }
  ],
  "deniedMcpServers": [
    { "serverName": "untrusted-server" },
    { "serverUrl": "http://*" }
  ],
  "allowManagedMcpServersOnly": true
}
```

세 번째 관리형 설정인 `managedMcpServers`(v2.1.259+)는 조직이 모든 사용자에게 HTTP/SSE MCP 서버를 제공할 수 있게 합니다. 항목은 `.mcp.json`과 같은 형태를 사용하며, 실행할 명령을 지정한 항목은 건너뜁니다.

> **참고:** `allowedMcpServers`와 `deniedMcpServers`가 모두 서버에 일치하면 차단 규칙이 우선합니다.

## 플러그인 제공 MCP 서버

플러그인은 자체 MCP 서버를 함께 제공할 수 있으며, 플러그인이 설치되면 자동으로 사용할 수 있습니다. 플러그인 제공 MCP 서버는 두 가지 방식으로 정의할 수 있습니다.

1. **독립 `.mcp.json`** -- 플러그인 루트 디렉터리에 `.mcp.json` 파일을 둡니다
2. **`plugin.json`에 인라인** -- 플러그인 매니페스트 안에 MCP 서버를 직접 정의합니다

`${CLAUDE_PLUGIN_ROOT}` 변수로 플러그인 설치 디렉터리를 기준으로 한 경로를 참조하세요.

```json
{
  "mcpServers": {
    "plugin-tools": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/dist/mcp-server.js"],
      "env": {
        "CONFIG_PATH": "${CLAUDE_PLUGIN_ROOT}/config.json"
      }
    }
  }
}
```

## 서브에이전트 범위 MCP

MCP 서버는 에이전트 프론트매터 안에 `mcpServers:` 키로 인라인 정의할 수 있으며, 프로젝트 전체가 아니라 특정 서브에이전트에 범위가 한정됩니다. 에이전트가 워크플로의 다른 에이전트에게는 필요 없는 특정 MCP 서버에 접근해야 할 때 유용합니다.

```yaml
---
name: my-tool-agent
description: Uses my-tool for specialized operations
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

서브에이전트 범위 MCP 서버는 해당 에이전트의 실행 컨텍스트 안에서만 사용할 수 있으며 상위나 형제 에이전트와 공유되지 않습니다.

## MCP 출력 제한

Claude Code는 컨텍스트 오버플로를 막기 위해 MCP 도구 출력에 제한을 적용합니다.

| 한도 | 임계값 | 동작 |
|-------|-----------|----------|
| **경고** | 10,000 토큰 | 출력이 크다는 경고가 표시됩니다 |
| **기본 최대** | 25,000 토큰 | 더 큰 출력은 파일로 저장되고, 파일 경로가 대화에 대신 들어갑니다 |
| **디스크 지속** | 50,000자 | 50K자를 초과하는 도구 결과는 디스크에 저장됩니다 |

최대 출력 한도는 `MAX_MCP_OUTPUT_TOKENS` 환경변수로 설정할 수 있습니다.

```bash
# Increase the max output to 50,000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

## 장시간 실행 도구 호출 자동 백그라운드 전환 (v2.1.212)

2분을 넘게 실행되는 MCP 도구 호출은 이제 자동으로 백그라운드로 이동하므로, 느린 도구에서 세션이 막히지 않고 계속 사용할 수 있습니다. 임계값은 `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`로 설정할 수 있고, 동작을 조정하거나 비활성화할 수도 있습니다.

```bash
# Change the auto-background threshold to 5 minutes (300,000ms)
export CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS=300000
```

## 코드 실행으로 컨텍스트 비대화 해결

MCP 도입이 확대되면서 수십 개 서버에 수백·수천 개 도구를 연결하는 일이 늘었고, 여기서 **컨텍스트 비대화**라는 큰 문제가 생깁니다. 규모가 커진 MCP에서 가장 큰 문제라 할 만하며, Anthropic 엔지니어링 팀은 직접 도구 호출 대신 코드 실행을 쓰는 우아한 해결책을 제안했습니다.

> **출처**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic Engineering Blog

### 문제: 토큰 낭비의 두 가지 원인

**1. 도구 정의가 컨텍스트 창을 과부하시킵니다**

대부분의 MCP 클라이언트는 모든 도구 정의를 미리 로드합니다. 수천 개 도구에 연결되면 모델은 사용자 요청을 읽기도 전에 수십만 토큰을 처리해야 합니다.

**2. 중간 결과가 추가 토큰을 소비합니다**

모든 중간 도구 결과가 모델 컨텍스트를 거칩니다. Google Drive에서 Salesforce로 회의록을 옮기는 경우를 생각해 보세요. 전체 회의록이 컨텍스트를 **두 번** 통과합니다. 읽을 때 한 번, 대상에 쓸 때 다시 한 번입니다. 2시간짜리 회의록이라면 50,000토큰 이상이 추가로 들 수 있습니다.

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### 해결책: 코드 API로서의 MCP 도구

도구 정의와 결과를 컨텍스트 창으로 전달하는 대신, 에이전트가 MCP 도구를 API로 호출하는 **코드를 작성**합니다. 코드는 샌드박스 실행 환경에서 실행되고 최종 결과만 모델로 돌아옵니다.

```mermaid
graph LR
    A["Model"] -->|"Writes code"| B["Code Execution<br/>Environment"]
    B -->|"Calls tools directly"| C["MCP Servers"]
    C -->|"Data stays in<br/>execution env"| B
    B -->|"Only final result<br/>(minimal tokens)"| A

    style A fill:#c8e6c9,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
```

#### 동작 방식

MCP 도구는 타입이 지정된 함수의 파일 트리로 제시됩니다.

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
└── ...
```

각 도구 파일에는 타입이 지정된 래퍼가 들어 있습니다.

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

export async function getDocument(
  input: GetDocumentInput
): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>(
    'google_drive__get_document', input
  );
}
```

그다음 에이전트가 도구를 조율하는 코드를 작성합니다.

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// Data flows directly between tools — never through the model
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**결과: 토큰 사용량이 약 150,000에서 약 2,000으로 감소 — 98.7% 절감.**

### 주요 이점

| 이점 | 설명 |
|---------|-------------|
| **점진적 공개** | 에이전트가 파일시스템을 탐색해 필요한 도구 정의만 로드합니다. 모든 도구를 미리 로드하지 않습니다 |
| **컨텍스트 효율적 결과** | 모델로 돌아오기 전에 실행 환경에서 데이터를 필터링·변환합니다 |
| **강력한 제어 흐름** | 루프, 조건문, 오류 처리가 모델을 왕복하지 않고 코드에서 실행됩니다 |
| **프라이버시 보존** | 중간 데이터(PII, 민감 레코드)가 실행 환경에 남고 모델 컨텍스트에 들어가지 않습니다 |
| **상태 지속성** | 에이전트가 중간 결과를 파일로 저장하고 재사용 가능한 스킬 함수를 만들 수 있습니다 |

#### 예제: 대용량 데이터셋 필터링

```typescript
// Without code execution — all 10,000 rows flow through context
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> returns 10,000 rows in context

// With code execution — filter in the execution environment
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Only 5 rows reach the model
```

#### 예제: 왕복 없는 루프

```typescript
// Poll for a deployment notification — runs entirely in code
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({
    channel: 'C123456'
  });
  found = messages.some(
    m => m.text.includes('deployment complete')
  );
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

### 고려할 트레이드오프

코드 실행은 그 자체의 복잡성을 도입합니다. 에이전트가 생성한 코드를 실행하려면 다음이 필요합니다.

- 적절한 리소스 한도가 있는 **안전한 샌드박스 실행 환경**
- 실행된 코드에 대한 **모니터링과 로깅**
- 직접 도구 호출 대비 추가 **인프라 오버헤드**

토큰 비용 감소, 지연 감소, 도구 조합 개선 같은 이점은 이런 구현 비용과 견주어 판단해야 합니다. MCP 서버가 몇 개뿐인 에이전트라면 직접 도구 호출이 더 단순할 수 있습니다. 규모가 큰 에이전트(수십 개 서버, 수백 개 도구)에게 코드 실행은 상당한 개선입니다.

### MCPorter: MCP 도구 조합을 위한 런타임

[MCPorter](https://github.com/steipete/mcporter)는 상용구 없이 MCP 서버를 실용적으로 호출할 수 있게 하는 TypeScript 런타임이자 CLI 툴킷이며, 선택적 도구 노출과 타입 래퍼로 컨텍스트 비대화를 줄이는 데 도움을 줍니다.

**해결하는 문제:** 모든 MCP 서버의 모든 도구 정의를 미리 로드하는 대신, MCPorter로 특정 도구를 필요할 때 발견·검사·호출할 수 있어 컨텍스트를 가볍게 유지합니다.

**주요 기능:**

| 기능 | 설명 |
|---------|-------------|
| **무설정 검색** | Cursor, Claude, Codex 또는 로컬 구성에서 MCP 서버를 자동으로 찾습니다 |
| **타입 지정 도구 클라이언트** | `mcporter emit-ts`가 `.d.ts` 인터페이스와 바로 실행 가능한 래퍼를 생성합니다 |
| **조합 가능한 API** | `createServerProxy()`가 도구를 camelCase 메서드로 노출하고 `.text()`, `.json()`, `.markdown()` 헬퍼를 제공합니다 |
| **CLI 생성** | `mcporter generate-cli`가 모든 MCP 서버를 `--include-tools` / `--exclude-tools` 필터링이 있는 독립 CLI로 변환합니다 |
| **매개변수 숨김** | 선택적 매개변수는 기본적으로 숨겨져 스키마 장황함을 줄입니다 |

**설치:**

```bash
npx mcporter list          # No install required — discover servers instantly
pnpm add mcporter          # Add to a project
brew install steipete/tap/mcporter  # macOS via Homebrew
```

**예제 — TypeScript에서 도구 조합:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// Data flows between tools without passing through the model context
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**예제 — CLI 도구 호출:**

```bash
# Call a specific tool directly
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# List available servers and tools
npx mcporter list
```

MCPorter는 MCP 도구를 타입이 지정된 API로 호출하기 위한 런타임 인프라를 제공해 위에서 설명한 코드 실행 접근을 보완합니다. 중간 데이터를 모델 컨텍스트 밖에 두기가 간단해집니다.

## 모범 사례

### 보안 고려 사항

#### 해야 할 것 ✅
- 모든 자격 증명에 환경변수를 사용합니다
- 토큰과 API 키를 정기적으로 교체합니다(월 1회 권장)
- 가능하면 읽기 전용 토큰을 사용합니다
- MCP 서버 접근 범위를 최소 필요로 제한합니다
- MCP 서버 사용량과 접근 로그를 모니터링합니다
- 가능하면 외부 서비스에 OAuth를 사용합니다
- MCP 요청에 속도 제한을 구현합니다
- 프로덕션 사용 전에 MCP 연결을 테스트합니다
- 모든 활성 MCP 연결을 문서화합니다
- MCP 서버 패키지를 최신 상태로 유지합니다

#### 하지 말 것 ❌
- 구성 파일에 자격 증명을 하드코딩하지 마세요
- 토큰이나 비밀을 git에 커밋하지 마세요
- 팀 채팅이나 이메일로 토큰을 공유하지 마세요
- 팀 프로젝트에 개인 토큰을 사용하지 마세요
- 불필요한 권한을 부여하지 마세요
- 인증 오류를 무시하지 마세요
- MCP 엔드포인트를 공개로 노출하지 마세요
- MCP 서버를 root/관리자 권한으로 실행하지 마세요
- 로그에 민감한 데이터를 캐시하지 마세요
- 인증 메커니즘을 비활성화하지 마세요

### 구성 모범 사례

1. **버전 관리**: `.mcp.json`은 git에 두되 비밀은 환경변수로 처리합니다
2. **최소 권한**: MCP 서버마다 필요한 최소 권한만 부여합니다
3. **격리**: 가능하면 MCP 서버를 별도 프로세스로 실행합니다
4. **모니터링**: 감사 추적을 위해 모든 MCP 요청과 오류를 기록합니다
5. **테스트**: 프로덕션 배포 전에 모든 MCP 구성을 테스트합니다

### 성능 팁

- 자주 접근하는 데이터는 애플리케이션 수준에서 캐시하세요
- 데이터 전송을 줄이려면 구체적인 MCP 쿼리를 사용하세요
- MCP 작업의 응답 시간을 모니터링하세요
- 외부 API에 속도 제한을 고려하세요
- 여러 작업을 수행할 때 배치를 사용하세요

## 설치 지침

### 사전 요구 사항
- Node.js와 npm 설치
- Claude Code CLI 설치
- 외부 서비스용 API 토큰/자격 증명

### 단계별 설정

1. **첫 MCP 서버를 추가**하세요. CLI를 사용합니다(예: GitHub).
```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

   또는 프로젝트 루트에 `.mcp.json` 파일을 만드세요.
```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

2. **환경변수를 설정합니다:**
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_personal_access_token"
```

3. **연결을 테스트합니다:**
```bash
claude /mcp
```

4. **MCP 도구를 사용합니다:**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### 특정 서비스별 설치

**GitHub MCP:**
```bash
npm install -g @modelcontextprotocol/server-github
```

**데이터베이스 MCP:**
```bash
npm install -g @bytebase/dbhub
```

**Filesystem MCP:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP (지원 중단된 패키지):**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## 문제 해결

### 오류 출력부터 확인하세요 (v2.1.219+)

서버가 연결되지 않으면 아무것도 바꾸기 전에 `claude mcp list`(또는 세션 안에서 `/mcp`)를 실행하세요. 이제 Claude Code가 실패한 서버 옆에 **HTTP 상태 코드와 서버의 오류 텍스트**를 출력하므로, 일반적인 "failed to connect" 대신 `401 Unauthorized`나 `404 Not Found`를 확인할 수 있습니다.

```bash
# Shows connection status plus HTTP status and error text for failures
claude mcp list
```

상태부터 읽으세요. 어떤 수정이 맞는지 알려 줍니다.

- `401` / `403` → 자격 증명이 잘못되었거나 만료됨. `claude mcp login <name>`으로 다시 인증하세요
- `404` → 잘못된 URL(`/mcp` 또는 `/sse` 경로 접미사 누락이 흔한 원인입니다)
- `5xx` / 타임아웃 → 원격 서버가 다운됨. [연결 타임아웃](#연결-타임아웃)을 참고하세요

### 구성 값의 숨은 공백 (v2.1.219+)

MCP 구성 값에 **앞뒤 공백**이 있으면 Claude Code가 경고합니다. 인증 실패의 흔하고 찾기 어려운 원인입니다. 브라우저나 채팅 메시지에서 복사한 토큰에는 뒤따르는 공백이나 개행이 붙는 경우가 많고, 이것이 `Authorization` 헤더에 그대로 전송되어 유효하지 않은 자격 증명으로 실패합니다.

이 경고가 보이면 `.mcp.json`(또는 그 값이 확장되는 환경변수)의 값을 다시 확인하고 공백을 제거하세요.

```bash
# Reveals hidden leading/trailing whitespace between the delimiters
printf '[%s]\n' "$GITHUB_PERSONAL_ACCESS_TOKEN"
```

### 헤드리스 실행에서 건너뛴 서버 (v2.1.219+)

`--mcp-config`로 전달한 서버 중 구성 검증에 실패한 것은 실행을 중단시키지 않고 **건너뜁니다**. 따라서 헤드리스 스크립트가 도구의 절반을 잃은 채 정상처럼 보일 수 있습니다. 이제 Claude Code가 어떤 항목이 제외되었는지 보고합니다.

- **헤드리스 / `-p` 실행**: stream-json `init` 이벤트의 `mcp_server_errors` 필드에 건너뛴 모든 항목이 나열됩니다. 실행 출력을 신뢰하기 전에 확인하세요.
- **대화형 터미널 실행**: 세션이 시작될 때 같은 문제가 시작 경고로 출력됩니다.

```bash
# Inspect skipped --mcp-config entries in a headless run
claude -p "list my tools" --mcp-config ./servers.json \
  --output-format stream-json --verbose \
  | jq -r 'select(.type == "system" and .subtype == "init") | .mcp_server_errors'
```

### MCP 서버를 찾을 수 없음
```bash
# Verify MCP server is installed
npm list -g @modelcontextprotocol/server-github

# Install if missing
npm install -g @modelcontextprotocol/server-github
```

### 인증 실패
```bash
# Verify environment variable is set
echo $GITHUB_PERSONAL_ACCESS_TOKEN

# Re-export if needed
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"

# Verify token has correct permissions
# Check GitHub token scopes at: https://github.com/settings/tokens
```

### 연결 타임아웃
- 네트워크 연결 확인: `ping api.github.com`
- API 엔드포인트 접근 가능 여부 확인
- API 속도 제한 확인
- 구성에서 타임아웃 늘리기 시도
- 방화벽 또는 프록시 문제 확인

### MCP 서버 충돌
- MCP 서버 로그 확인: `~/.claude/logs/`
- 모든 환경변수가 설정되었는지 확인
- 적절한 파일 권한 확인
- MCP 서버 패키지 재설치 시도
- 같은 포트를 쓰는 충돌 프로세스 확인

## 관련 개념

### 메모리 vs MCP
- **메모리**: 영구적이고 변하지 않는 데이터를 저장합니다(선호도, 컨텍스트, 기록)
- **MCP**: 실시간으로 변하는 데이터에 접근합니다(API, 데이터베이스, 실시간 서비스)

### 각각을 언제 사용할까
- **메모리 사용**: 사용자 선호도, 대화 기록, 학습된 컨텍스트
- **MCP 사용**: 현재 GitHub 이슈, 실시간 데이터베이스 쿼리, 실시간 데이터

### 다른 Claude 기능과의 통합
- 풍부한 컨텍스트를 위해 MCP를 메모리와 결합합니다
- 더 나은 추론을 위해 프롬프트에서 MCP 도구를 사용합니다
- 복잡한 워크플로를 위해 여러 MCP를 활용합니다

## 추가 자료

- [공식 MCP 문서](https://code.claude.com/docs/en/mcp)
- [MCP 프로토콜 명세](https://modelcontextprotocol.io/specification)
- [MCP GitHub 저장소](https://github.com/modelcontextprotocol/servers)
- [사용 가능한 MCP 서버](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — 상용구 없이 MCP 서버를 호출하는 TypeScript 런타임 및 CLI
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — 컨텍스트 비대화 해결을 다룬 Anthropic 엔지니어링 블로그
- [Claude Code CLI 레퍼런스](https://code.claude.com/docs/en/cli-reference)
- [Claude API 문서](https://docs.anthropic.com)

---

**최종 업데이트**: 2026년 10월 18일
**Claude Code 버전**: 2.1.302
**출처**:
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/managed-mcp
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.139
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/mcp#configure-tool-search
- https://code.claude.com/docs/en/env-vars
- https://github.com/anthropics/claude-code/releases/tag/v2.1.285
- https://github.com/anthropics/claude-code/releases/tag/v2.1.296
- https://code.claude.com/docs/en/mcp#tool-search-for-mcp-server-authors
- https://code.claude.com/docs/en/mcp#environment-variable-expansion-in-mcp-json
- https://code.claude.com/docs/en/sub-agents
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
