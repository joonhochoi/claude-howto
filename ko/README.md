<!-- i18n-source: README.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%231%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.302-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

🌐 **Language / Ngôn ngữ / 语言 / Мова / 言語 / 한국어:** [English](../README.md) | [Tiếng Việt](../vi/README.md) | [中文](../zh/README.md) | [Українська](../uk/README.md) | [日本語](../ja/README.md) | [한국어](README.md)

# 주말에 Claude Code 마스터하기

`claude`를 입력하는 단계에서 에이전트·훅·스킬·MCP 서버를 오케스트레이션하는 단계로 넘어갑니다. 시각적 튜토리얼, 복사해 붙여 쓰는 템플릿, 단계별 학습 경로를 함께 제공합니다.

**[15분 만에 시작하기](#15분-만에-시작하기)** | **[내 수준 찾기](#어디서-시작할지-모르겠다면)** | **[기능 카탈로그 보기](CATALOG.md)**

---

## 목차

- [문제](#문제)
- [Claude How To가 해결하는 방법](#claude-how-to가-해결하는-방법)
- [동작 방식](#동작-방식)
- [어디서 시작할지 모르겠다면?](#어디서-시작할지-모르겠다면)
- [15분 만에 시작하기](#15분-만에-시작하기)
- [이것으로 무엇을 만들 수 있나요?](#이것으로-무엇을-만들-수-있나요)
- [FAQ](#faq)
- [기여하기](#기여하기)
- [라이선스](#라이선스)

---

## 문제

Claude Code를 설치했습니다. 프롬프트를 몇 개 실행했습니다. 이제 무엇을 해야 할까요?

- **공식 문서는 기능을 설명할 뿐, 조합하는 방법은 보여 주지 않습니다.** 슬래시 커맨드가 있다는 것은 알지만, 그것을 훅·메모리·서브에이전트와 엮어 실제로 몇 시간을 아껴 주는 워크플로로 만드는 방법은 모릅니다.
- **명확한 학습 경로가 없습니다.** MCP를 훅보다 먼저 배워야 할까요? 스킬을 서브에이전트보다 먼저 배워야 할까요? 결국 모든 것을 훑어보고 아무것도 마스터하지 못합니다.
- **예제가 너무 기초적입니다.** "hello world" 슬래시 커맨드로는 메모리를 활용하고, 전문화된 에이전트에 위임하고, 보안 스캔을 자동 실행하는 프로덕션급 코드 리뷰 파이프라인을 만들 수 없습니다.

Claude Code 성능의 90%를 놀린 채로, 자기 자신이 무엇을 모르는지조차 모르는 상태입니다.

---

## Claude How To가 해결하는 방법

또 하나의 기능 레퍼런스가 아닙니다. 오늘 프로젝트에 그대로 복사해 쓸 수 있는 실전 템플릿과 함께 Claude Code의 모든 기능을 쓰는 법을 가르치는 **구조화된 시각적 예제 중심 가이드**입니다.

| | 공식 문서 | 이 가이드 |
|--|---------------|------------|
| **형식** | 레퍼런스 문서 | Mermaid 다이어그램이 있는 시각적 튜토리얼 |
| **깊이** | 기능 설명 | 내부 동작 원리 |
| **예제** | 기초 스니펫 | 즉시 활용하는 프로덕션급 템플릿 |
| **구조** | 기능별 구성 | 단계적 학습 경로(초급부터 고급까지) |
| **온보딩** | 자기 주도 | 소요 시간이 표시된 가이드 로드맵 |
| **자기 평가** | 없음 | 부족한 점을 찾아 맞춤 경로를 만드는 인터랙티브 퀴즈 |

### 얻을 수 있는 것:

- **10개 튜토리얼 모듈** — 슬래시 커맨드부터 커스텀 에이전트 팀까지 Claude Code의 모든 기능을 다룹니다
- **복사해 쓰는 설정** — 슬래시 커맨드, CLAUDE.md 템플릿, 훅 스크립트, MCP 설정, 서브에이전트 정의, 완전한 플러그인 번들
- **Mermaid 다이어그램** — 각 기능이 내부에서 어떻게 동작하는지 보여 주므로 *어떻게*뿐 아니라 *왜*를 이해하게 됩니다
- **단계별 학습 경로** — 11~13시간에 초급자에서 고급 사용자까지 도달합니다
- **내장 자기 평가** — Claude Code에서 `/self-assessment` 또는 `/lesson-quiz hooks`를 직접 실행해 부족한 부분을 찾습니다

**[학습 경로 시작하기 ->](LEARNING-ROADMAP.md)**

---

## 동작 방식

### 1. 내 수준 찾기

[자기 평가 퀴즈](LEARNING-ROADMAP.md#-find-your-level)를 풀거나 Claude Code에서 `/self-assessment`를 실행하세요. 이미 아는 내용을 기준으로 맞춤 로드맵을 받습니다.

### 2. 가이드 경로 따라가기

10개 모듈을 순서대로 진행하세요. 각 모듈은 앞 모듈 위에 쌓입니다. 배우는 즉시 템플릿을 프로젝트에 복사해 쓰세요.

### 3. 기능을 워크플로로 조합하기

진짜 힘은 기능을 조합하는 데 있습니다. 슬래시 커맨드 + 메모리 + 서브에이전트 + 훅을 코드 리뷰, 배포, 문서 생성을 처리하는 자동화 파이프라인으로 엮는 법을 배우세요.

### 4. 이해도 점검하기

모듈마다 `/lesson-quiz [topic]`을 실행하세요. 퀴즈가 놓친 부분을 짚어 주므로 빠르게 메울 수 있습니다.

**[15분 만에 시작하기](#15분-만에-시작하기)**

---

## 개발자들의 신뢰

- Claude Code를 매일 쓰는 개발자들의 **GitHub 스타**
- 이 가이드를 자기 워크플로에 맞게 고쳐 쓰는 팀들의 **포크**
- **활발한 유지 관리** — 모든 Claude Code 릴리스와 동기화합니다(최신: v2.1.302, 2026년 10월)
- **커뮤니티 주도** — 실제 설정을 공유하는 개발자들의 기여

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## 어디서 시작할지 모르겠다면?

자기 평가를 하거나 수준을 고르세요:

| 수준 | 할 수 있는 것 | 여기서 시작 | 시간 |
|-------|-----------|------------|------|
| **초급** | Claude Code를 실행하고 대화하기 | [슬래시 커맨드](01-slash-commands/) | 약 2.5시간 |
| **중급** | CLAUDE.md와 커스텀 커맨드 사용하기 | [스킬](03-skills/) | 약 3.5시간 |
| **고급** | MCP 서버와 훅 구성하기 | [고급 기능](09-advanced-features/) | 약 5시간 |

**10개 모듈 전체 학습 경로:**

| 순서 | 모듈 | 수준 | 시간 |
|-------|--------|-------|------|
| 1 | [슬래시 커맨드](01-slash-commands/) | 초급 | 30분 |
| 2 | [메모리](02-memory/) | 초급+ | 45분 |
| 3 | [체크포인트](08-checkpoints/) | 중급 | 45분 |
| 4 | [CLI 기초](10-cli/) | 초급+ | 30분 |
| 5 | [스킬](03-skills/) | 중급 | 1시간 |
| 6 | [훅](06-hooks/) | 중급 | 1시간 |
| 7 | [MCP](05-mcp/) | 중급+ | 1시간 |
| 8 | [서브에이전트](04-subagents/) | 중급+ | 1.5시간 |
| 9 | [고급 기능](09-advanced-features/) | 고급 | 2~3시간 |
| 10 | [플러그인](07-plugins/) | 고급 | 2시간 |

**[전체 학습 로드맵 ->](LEARNING-ROADMAP.md)**

---

## 15분 만에 시작하기

> **설치 참고**: v2.1.113부터 Claude Code는 플랫폼별 네이티브 바이너리(macOS/Linux/Windows)로 배포됩니다. 권장 설치 방법은 네이티브 설치 프로그램(`curl -fsSL https://claude.ai/install.sh | bash`)이며, 공식 README에서 npm 설치는 폐기되었습니다. 네이티브 설치 프로그램, Homebrew(`brew install --cask claude-code`), WinGet(`winget install Anthropic.ClaudeCode`)을 우선하세요. 참고로 `npm install -g @anthropic-ai/claude-code`는 설치 시점에 플랫폼별 선택적 의존성을 통해 같은 네이티브 바이너리를 받아옵니다. v2.1.116부터 다운로드는 `https://downloads.claude.ai/claude-code-releases`에서 이루어지므로, 사내 프록시는 이 호스트를 허용 목록에 추가해야 합니다.

```bash
# 1. Clone the guide
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. Copy your first slash command
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. Try it — in Claude Code, type:
# /optimize

# 4. Ready for more? Set up project memory:
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. Install a skill:
cp -r 03-skills/code-review-specialist ~/.claude/skills/
```

전체 설정이 필요하신가요? **1시간 필수 설정**은 다음과 같습니다:

```bash
# Slash commands (15 min)
cp 01-slash-commands/*.md .claude/commands/

# Project memory (15 min)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Install a skill (15 min)
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Weekend goal: add hooks, subagents, MCP, and plugins
# Follow the learning path for guided setup
```

**[전체 설치 레퍼런스 보기](#15분-만에-시작하기)**

---

## 이것으로 무엇을 만들 수 있나요?

| 사용 사례 | 조합할 기능 |
|----------|------------------------|
| **자동 코드 리뷰** | 슬래시 커맨드 + 서브에이전트 + 메모리 + MCP |
| **팀 온보딩** | 메모리 + 슬래시 커맨드 + 플러그인 |
| **CI/CD 자동화** | CLI 레퍼런스 + 훅 + 백그라운드 작업 |
| **문서 생성** | 스킬 + 서브에이전트 + 플러그인 |
| **보안 감사** | 서브에이전트 + 스킬 + 훅(읽기 전용 모드) |
| **DevOps 파이프라인** | 플러그인 + MCP + 훅 + 백그라운드 작업 |
| **복잡한 리팩터링** | 체크포인트 + 플랜 모드 + 훅 |

---

## FAQ

**무료인가요?**
예. MIT 라이선스이며 영구 무료입니다. 라이선스 고지를 포함하는 것 외에 별도 제한 없이 개인 프로젝트, 직장, 팀에서 사용하세요.

**유지 관리되나요?**
적극적으로 유지합니다. 이 가이드는 모든 Claude Code 릴리스와 동기화됩니다. 현재 버전: v2.1.302(2026년 10월), Claude Code 2.1+ 호환.

**공식 문서와 무엇이 다른가요?**
공식 문서는 기능 레퍼런스입니다. 이 가이드는 다이어그램, 프로덕션급 템플릿, 단계적 학습 경로를 갖춘 튜토리얼입니다. 둘은 서로를 보완합니다. 배울 때는 여기서 시작하고, 구체적인 내용이 필요할 때 공식 문서를 참조하세요.

**전부 훑으려면 얼마나 걸리나요?**
전체 경로는 11~13시간입니다. 하지만 15분이면 바로 가치를 얻습니다. 슬래시 커맨드 템플릿 하나를 복사해 써 보세요.

**Claude Sonnet / Haiku / Opus와 함께 쓸 수 있나요?**
예. 모든 템플릿은 Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5와 함께 동작합니다.

**기여할 수 있나요?**
물론입니다. 가이드라인은 [CONTRIBUTING.md](CONTRIBUTING.md)를 보세요. 새로운 예제, 버그 수정, 문서 개선, 커뮤니티 템플릿을 환영합니다.

**오프라인으로 읽을 수 있나요?**
예. `uv run scripts/build_epub.py`를 실행하면 모든 콘텐츠와 렌더링된 다이어그램이 담긴 EPUB 전자책을 생성합니다.

---

## 오늘부터 Claude Code 마스터하기

Claude Code는 이미 설치되어 있습니다. 10배 생산성과 나 사이에 남은 것은 그것을 쓰는 법을 아는 것뿐입니다. 이 가이드가 그곳에 이르는 구조화된 경로, 시각적 설명, 복사해 쓰는 템플릿을 제공합니다.

MIT 라이선스. 영구 무료. 클론하고, 포크하고, 내 것으로 만드세요.

**[학습 경로 시작하기 ->](LEARNING-ROADMAP.md)** | **[기능 카탈로그 보기](CATALOG.md)** | **[15분 만에 시작하기](#15분-만에-시작하기)**

---

<details>
<summary>빠른 탐색 — 전체 기능</summary>

| 기능 | 설명 | 폴더 |
|---------|-------------|--------|
| **기능 카탈로그** | 설치 명령이 포함된 전체 레퍼런스 | [CATALOG.md](CATALOG.md) |
| **슬래시 커맨드** | 사용자가 호출하는 단축 명령 | [01-slash-commands/](01-slash-commands/) |
| **메모리** | 지속되는 컨텍스트 | [02-memory/](02-memory/) |
| **스킬** | 재사용 가능한 기능 | [03-skills/](03-skills/) |
| **서브에이전트** | 전문화된 AI 어시스턴트 | [04-subagents/](04-subagents/) |
| **MCP 프로토콜** | 외부 도구 접근 | [05-mcp/](05-mcp/) |
| **훅** | 이벤트 기반 자동화 | [06-hooks/](06-hooks/) |
| **플러그인** | 묶음으로 제공되는 기능 | [07-plugins/](07-plugins/) |
| **체크포인트** | 세션 스냅샷 및 되감기 | [08-checkpoints/](08-checkpoints/) |
| **고급 기능** | 플랜 모드, 확장 사고, 백그라운드 작업 | [09-advanced-features/](09-advanced-features/) |
| **CLI 레퍼런스** | 명령, 플래그, 옵션 | [10-cli/](10-cli/) |
| **블로그 글** | 실제 사용 예제 | [블로그 글](https://medium.com/@luongnv89) |

</details>

<details>
<summary>기능 비교</summary>

| 기능 | 호출 방식 | 지속성 | 적합한 용도 |
|---------|-----------|------------|----------|
| **슬래시 커맨드** | 수동(`/cmd`) | 세션에만 | 빠른 단축 |
| **메모리** | 자동 로드 | 세션 간 | 장기 학습 |
| **스킬** | 자동 호출 | 파일 시스템 | 자동화된 워크플로 |
| **서브에이전트** | 자동 위임 | 격리된 컨텍스트 | 작업 분산 |
| **MCP 프로토콜** | 자동 조회 | 실시간 | 라이브 데이터 접근 |
| **훅** | 이벤트 트리거 | 설정 기반 | 자동화 및 검증 |
| **플러그인** | 명령 하나 | 모든 기능 | 완전한 솔루션 |
| **체크포인트** | 수동/자동 | 세션 기반 | 안전한 실험 |
| **플랜 모드** | 수동/자동 | 계획 단계 | 복잡한 구현 |
| **백그라운드 작업** | 수동 | 작업 기간 | 장시간 실행 작업 |
| **CLI 레퍼런스** | 터미널 명령 | 세션/스크립트 | 자동화 및 스크립팅 |

</details>

<details>
<summary>설치 빠른 참조</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Plugins (load a local plugin from the repo root)
claude --plugin-dir ./07-plugins/pr-review

# Checkpoints (auto-enabled, configure in settings)
# See 08-checkpoints/README.md

# Advanced Features (configure in settings)
# See 09-advanced-features/config-examples.json

# CLI Reference (no installation needed)
# See 10-cli/README.md for usage examples
```

</details>

<details>
<summary>01. 슬래시 커맨드</summary>

**위치**: [01-slash-commands/](01-slash-commands/)

**무엇**: Markdown 파일로 저장되는 사용자 호출 단축 명령

**예제**:
- `optimize.md` - 코드 최적화 분석
- `pr.md` - PR 준비
- `generate-api-docs.md` - API 문서 생성기

**설치**:
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**사용법**:
```
/optimize
/pr
/generate-api-docs
```

**더 알아보기**: [Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. 메모리</summary>

**위치**: [02-memory/](02-memory/)

**무엇**: 세션 간에 지속되는 컨텍스트

**예제**:
- `project-CLAUDE.md` - 팀 전체 프로젝트 표준
- `directory-api-CLAUDE.md` - 디렉터리별 규칙
- `personal-CLAUDE.md` - 개인 선호 설정

**설치**:
```bash
# Project memory
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# Directory memory
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# Personal memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**사용법**: Claude가 자동으로 로드합니다

</details>

<details>
<summary>03. 스킬</summary>

**위치**: [03-skills/](03-skills/)

**무엇**: 지침과 스크립트를 갖춘, 자동 호출되는 재사용 가능한 기능

**예제**:
- `code-review-specialist/` - 스크립트를 포함한 종합 코드 리뷰
- `brand-voice/` - 브랜드 보이스 일관성 검사기
- `doc-generator/` - API 문서 생성기

**설치**:
```bash
# Personal skills
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Project skills
cp -r 03-skills/code-review-specialist /path/to/project/.claude/skills/
```

**사용법**: 관련 상황에서 자동으로 호출됩니다

</details>

<details>
<summary>04. 서브에이전트</summary>

**위치**: [04-subagents/](04-subagents/)

**무엇**: 격리된 컨텍스트와 커스텀 프롬프트를 갖춘 전문화된 AI 어시스턴트

**예제**:
- `code-reviewer.md` - 종합적인 코드 품질 분석
- `test-engineer.md` - 테스트 전략과 커버리지
- `documentation-writer.md` - 기술 문서 작성
- `secure-reviewer.md` - 보안 중심 리뷰(읽기 전용)
- `implementation-agent.md` - 기능 전체 구현

**설치**:
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**사용법**: 메인 에이전트가 자동으로 위임합니다

</details>

<details>
<summary>05. MCP 프로토콜</summary>

**위치**: [05-mcp/](05-mcp/)

**무엇**: 외부 도구와 API에 접근하기 위한 Model Context Protocol

**예제**:
- `github-mcp.json` - GitHub 통합
- `database-mcp.json` - 데이터베이스 쿼리
- `filesystem-mcp.json` - 파일 작업
- `multi-mcp.json` - 여러 MCP 서버

**설치**:
```bash
# Set environment variables
export DATABASE_URL="postgresql://..."

# Add MCP server via CLI
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# Or add to project .mcp.json manually (see 05-mcp/ for examples)
```

**사용법**: 설정이 끝나면 MCP 도구를 Claude가 자동으로 사용할 수 있습니다

</details>

<details>
<summary>06. 훅</summary>

**위치**: [06-hooks/](06-hooks/)

**무엇**: Claude Code 이벤트에 반응해 자동으로 실행되는 이벤트 기반 셸 명령

**예제**:
- `format-code.sh` - 파일 작성 후 코드 자동 포맷
- `pre-commit.sh` - 커밋 전 테스트 실행
- `security-scan.sh` - 보안 문제 스캔
- `log-bash.sh` - 모든 bash 명령 기록
- `validate-prompt.sh` - 사용자 프롬프트 검증
- `notify-team.sh` - 이벤트 발생 시 알림 전송

**설치**:
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

`~/.claude/settings.json`에서 훅을 설정하세요:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          { "type": "command", "command": "~/.claude/hooks/format-code.sh" },
          { "type": "command", "command": "~/.claude/hooks/security-scan.sh" }
        ]
      }
    ]
  }
}
```

**사용법**: 훅은 이벤트가 발생하면 자동으로 실행됩니다

**훅 타입**(5종): `command`, `http`, `prompt`, `mcp_tool`, `agent` — 훅이 실행되는 방식입니다.

**훅 이벤트**(33종, 4개 범주) — 실행되는 시점입니다:
- **도구 훅**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `PermissionRequest`, `PermissionDenied`
- **세션 훅**: `SessionStart`, `Setup`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
- **작업 훅**: `UserPromptSubmit`, `UserPromptExpansion`, `MessageDisplay`, `TaskCompleted`, `TaskCreated`, `TeammateIdle` — `TaskCompleted`와 `TaskCreated`는 todo 도구가 활성화된 경우에만 발생하며, 기본적으로 Claude 3.x 모델, Opus 4~4.7, Sonnet 4~4.6, Haiku 4.5에서만 사용할 수 있습니다(`CLAUDE_CODE_ENABLE_TODO_TOOLS=1`로 다시 활성화할 수 있습니다)
- **수명 주기 훅**: `ConfigChange`, `CwdChanged`, `DirectoryAdded`, `FileChanged`, `PreCompact`, `PostCompact`, `PreModelSwitch`, `PostModelSwitch`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

</details>

<details>
<summary>07. 플러그인</summary>

**위치**: [07-plugins/](07-plugins/)

**무엇**: 커맨드, 에이전트, MCP, 훅을 묶은 번들 모음

**예제**:
- `pr-review/` - 완전한 PR 리뷰 워크플로
- `devops-automation/` - 배포와 모니터링
- `documentation/` - 문서 생성

**설치**:
```bash
# From the repo root (this repo ships no marketplace, so /plugin install does not apply)
claude --plugin-dir ./07-plugins/pr-review
claude --plugin-dir ./07-plugins/devops-automation
claude --plugin-dir ./07-plugins/documentation
```

**사용법**: 번들로 제공되는 슬래시 커맨드와 기능을 사용합니다

</details>

<details>
<summary>08. 체크포인트와 되감기</summary>

**위치**: [08-checkpoints/](08-checkpoints/)

**무엇**: 대화 상태를 저장하고 이전 지점으로 되감아 다른 접근을 시도합니다

**핵심 개념**:
- **체크포인트**: 대화 상태의 스냅샷
- **되감기**: 이전 체크포인트로 돌아가기
- **분기 지점**: 같은 체크포인트에서 여러 접근을 시도하기

**사용법**:
```
# Checkpoints are created automatically with every user prompt
# To rewind, press Esc twice or use:
/rewind

# Then choose from six options:
# 1. Restore code and conversation
# 2. Restore conversation
# 3. Restore code
# 4. Summarize from here
# 5. Summarize up to here
# 6. Never mind
```

**사용 사례**:
- 다른 구현 방식 시도하기
- 실수에서 복구하기
- 안전한 실험
- 대안 솔루션 비교하기
- 서로 다른 설계 A/B 테스트

</details>

<details>
<summary>09. 고급 기능</summary>

**위치**: [09-advanced-features/](09-advanced-features/)

**무엇**: 복잡한 워크플로와 자동화를 위한 고급 기능

**포함 내용**:
- **플랜 모드** — 코딩 전에 상세한 구현 계획을 작성합니다
- **확장 사고** — 복잡한 문제를 깊이 추론합니다(`Alt+T` / `Option+T`로 전환)
- **백그라운드 작업** — 블로킹 없이 긴 작업을 실행합니다
- **권한 모드** — `manual`(설정 값 `default`), `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`
- **헤드리스 모드** — CI/CD에서 Claude Code를 실행합니다: `claude -p "Run tests and generate report"`
- **세션 관리** — `/resume`, `/rename`, `/fork`, `/branch`, `claude -c`, `claude -r`
- **설정** — `~/.claude/settings.json`에서 동작을 커스터마이즈합니다

전체 설정은 [config-examples.json](09-advanced-features/config-examples.json)을 보세요.

</details>

<details>
<summary>10. CLI 레퍼런스</summary>

**위치**: [10-cli/](10-cli/)

**무엇**: Claude Code의 완전한 커맨드라인 인터페이스 레퍼런스

**빠른 예제**:
```bash
# Interactive mode
claude "explain this project"

# Print mode (non-interactive)
claude -p "review this code"

# Process file content
cat error.log | claude -p "explain this error"

# JSON output for scripts
claude -p --output-format json "list functions"

# Resume session
claude -r "feature-auth" "continue implementation"
```

**사용 사례**: CI/CD 파이프라인 통합, 스크립트 자동화, 배치 처리, 멀티 세션 워크플로, 커스텀 에이전트 구성

</details>

<details>
<summary>예제 워크플로</summary>

### 전체 코드 리뷰 워크플로

```markdown
# Uses: Slash Commands + Subagents + Memory + MCP

User: /review-pr

Claude:
1. Loads project memory (coding standards)
2. Fetches PR via GitHub MCP
3. Delegates to code-reviewer subagent
4. Delegates to test-engineer subagent
5. Synthesizes findings
6. Provides comprehensive review
```

### 자동 문서 생성

```markdown
# Uses: Skills + Subagents + Memory

User: "Generate API documentation for the auth module"

Claude:
1. Loads project memory (doc standards)
2. Detects doc generation request
3. Auto-invokes doc-generator skill
4. Delegates to api-documenter subagent
5. Creates comprehensive docs with examples
```

### DevOps 배포

```markdown
# Uses: Plugins + MCP + Hooks

User: /deploy production

Claude:
1. Runs pre-deploy hook (validates environment)
2. Delegates to deployment-specialist subagent
3. Executes deployment via Kubernetes MCP
4. Monitors progress
5. Runs post-deploy hook (health checks)
6. Reports status
```

</details>

<details>
<summary>디렉터리 구조</summary>

```
├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review-specialist/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md (this file)
```

</details>

<details>
<summary>모범 사례</summary>

### 해야 할 것
- 슬래시 커맨드로 단순하게 시작하세요
- 기능을 점진적으로 추가하세요
- 팀 표준은 메모리에 두세요
- 설정은 먼저 로컬에서 테스트하세요
- 커스텀 구현을 문서화하세요
- 프로젝트 설정을 버전 관리하세요
- 팀과 플러그인을 공유하세요

### 하지 말 것
- 중복 기능을 만들지 마세요
- 자격 증명을 하드코딩하지 마세요
- 문서화를 건너뛰지 마세요
- 단순한 작업을 과도하게 복잡하게 만들지 마세요
- 보안 모범 사례를 무시하지 마세요
- 민감한 데이터를 커밋하지 마세요

</details>

<details>
<summary>문제 해결</summary>

### 기능이 로드되지 않음
1. 파일 위치와 이름을 확인하세요
2. YAML 프론트매터 문법을 검증하세요
3. 파일 권한을 확인하세요
4. Claude Code 버전 호환성을 검토하세요

### MCP 연결 실패
1. 환경 변수를 확인하세요
2. MCP 서버 설치를 점검하세요
3. 자격 증명을 테스트하세요
4. 네트워크 연결을 검토하세요

### 서브에이전트가 위임하지 않음
1. 도구 권한을 확인하세요
2. 에이전트 설명이 명확한지 검증하세요
3. 작업 복잡도를 검토하세요
4. 에이전트를 단독으로 테스트하세요

</details>

<details>
<summary>테스트</summary>

이 프로젝트에는 포괄적인 자동 테스트가 포함되어 있습니다:

- **단위 테스트**: pytest를 사용한 Python 테스트(Python 3.10, 3.11, 3.12)
- **코드 품질**: Ruff를 사용한 린팅과 포매팅
- **보안**: Bandit을 사용한 취약점 스캔
- **타입 검사**: mypy를 사용한 정적 타입 분석
- **빌드 검증**: EPUB 생성 테스트
- **커버리지 추적**: Codecov 통합

```bash
# Install development dependencies
uv pip install -r scripts/requirements-dev.txt

# Run all unit tests
pytest scripts/tests/ -v

# Run tests with coverage report
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Run code quality checks
ruff check scripts/
ruff format --check scripts/

# Run security scan
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/

# Run type checking
mypy scripts/ --ignore-missing-imports
```

테스트는 `main`/`develop`에 대한 모든 push와 `main`으로 향하는 모든 PR에서 자동으로 실행됩니다. 자세한 내용은 [TESTING.md](../.github/TESTING.md)를 보세요.

</details>

<details>
<summary>EPUB 생성</summary>

이 가이드를 오프라인에서 읽고 싶으신가요? EPUB 전자책을 생성하세요:

```bash
uv run scripts/build_epub.py
```

모든 콘텐츠와 렌더링된 Mermaid 다이어그램이 담긴 `claude-howto-guide.epub`가 생성됩니다.

추가 옵션은 [scripts/README.md](../scripts/README.md)를 보세요.

</details>

<details>
<summary>기여하기</summary>

문제를 발견했거나 예제를 기여하고 싶으신가요? 도움을 환영합니다!

**자세한 가이드라인은 [CONTRIBUTING.md](CONTRIBUTING.md)를 읽어 보세요:**
- 기여 유형(예제, 문서, 기능, 버그, 피드백)
- 개발 환경 설정 방법
- 디렉터리 구조와 콘텐츠 추가 방법
- 작성 가이드라인과 모범 사례
- 커밋과 PR 절차

**커뮤니티 표준:**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 서로를 대하는 방식
- [SECURITY.md](SECURITY.md) - 보안 정책과 취약점 신고

### 보안 이슈 신고

보안 취약점을 발견하면 책임 있게 신고해 주세요:

1. **GitHub 비공개 취약점 신고 사용**: https://github.com/luongnv89/claude-howto/security/advisories
2. **또는** 자세한 절차는 [.github/SECURITY_REPORTING.md](../.github/SECURITY_REPORTING.md)를 읽어 보세요
3. 보안 취약점에 대해 **공개 이슈를 열지 마세요**

빠른 시작:
1. 저장소를 포크하고 클론합니다
2. 설명이 담긴 브랜치를 만듭니다(`add/feature-name`, `fix/bug`, `docs/improvement`)
3. 가이드라인에 따라 변경합니다
4. 명확한 설명과 함께 PR을 제출합니다

**도움이 필요하신가요?** 이슈나 토론을 열어 주시면 절차를 안내해 드립니다.

</details>

<details>
<summary>추가 자료</summary>

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) - 바로 쓸 수 있는 스킬 모음
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny's Claude Code Workflow](https://x.com/bcherny/status/2007179832300581177) - Claude Code를 만든 사람이 공개한 체계화된 워크플로: 병렬 에이전트, 공유 CLAUDE.md, 플랜 모드, 슬래시 커맨드, 서브에이전트, 그리고 자율적으로 오래 실행되는 세션을 위한 검증 훅.

</details>

---

## 기여하기

기여를 환영합니다! 시작하는 방법은 [기여 가이드](CONTRIBUTING.md)를 보세요.

---

## 라이선스

MIT 라이선스 - [LICENSE](../LICENSE)를 보세요. 사용, 수정, 배포가 자유롭습니다. 유일한 조건은 라이선스 고지를 포함하는 것입니다.

---

**최종 업데이트**: 2026년 10월 18일
**Claude Code 버전**: 2.1.302
**출처**:
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/permission-modes
- https://platform.claude.com/docs/en/about-claude/models/overview
- https://github.com/anthropics/claude-code/releases
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
- https://code.claude.com/docs/en/model-config
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://github.com/anthropics/claude-code/releases/tag/v2.1.296
- https://code.claude.com/docs/en/setup
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/plugins/install
- https://code.claude.com/docs/en/checkpointing
- https://github.com/anthropics/claude-code
- https://code.claude.com/docs/en/changelog#2-1-302
**호환 모델**: Claude Fable 5.1, Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
