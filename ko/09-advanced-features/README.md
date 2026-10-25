<!-- i18n-source: 09-advanced-features/README.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# 고급 기능

플랜 모드, 확장 사고, 오토 모드, 백그라운드 작업, 권한 모드, 프린트 모드(비대화형), 세션 관리, 대화형 기능, 채널, 음성 받아쓰기, 원격 제어, 웹 세션, 데스크톱 앱, 작업 목록, 프롬프트 제안, Git 워크트리, 샌드박스, 관리형 설정, 구성을 포함한 Claude Code의 고급 기능에 관한 종합 안내서입니다.

## 목차

1. [개요](#개요)
2. [플랜 모드](#플랜-모드)
3. [확장 사고](#확장-사고)
4. [오토 모드](#오토-모드)
5. [백그라운드 작업](#백그라운드-작업)
6. [Monitor 도구 (이벤트 기반 스트림)](#monitor-도구-이벤트-기반-스트림)
7. [동적 워크플로](#동적-워크플로)
8. [예약된 작업](#예약된-작업)
9. [권한 모드](#권한-모드)
10. [헤드리스 모드](#헤드리스-모드)
11. [세션 관리](#세션-관리)
12. [세션 간 메시징](#세션-간-메시징)
13. [대화형 기능](#대화형-기능)
14. [출력 스타일](#출력-스타일)
15. [상태 표시줄](#상태-표시줄)
16. [TUI 모드 (전체 화면)](#tui-모드-전체-화면)
17. [음성 받아쓰기](#음성-받아쓰기)
18. [채널](#채널)
19. [Chrome 통합](#chrome-통합)
20. [원격 제어](#원격-제어)
21. [웹 세션](#웹-세션)
22. [데스크톱 앱](#데스크톱-앱)
23. [작업 목록](#작업-목록)
24. [프롬프트 제안](#프롬프트-제안)
25. [Git 워크트리](#git-워크트리)
26. [샌드박싱](#샌드박싱)
27. [관리형 설정 (엔터프라이즈)](#관리형-설정-엔터프라이즈)
28. [구성 및 설정](#구성-및-설정)
29. [신뢰 및 권한 범위](#신뢰-및-권한-범위)
30. [에이전트 팀](#에이전트-팀)
31. [모범 사례](#모범-사례)
32. [추가 자료](#추가-자료)

---

## 개요

Claude Code의 고급 기능은 플래닝, 추론, 자동화, 제어 메커니즘으로 핵심 역량을 확장합니다. 이러한 기능을 통해 복잡한 개발 작업, 코드 리뷰, 자동화, 다중 세션 관리에 정교한 워크플로를 구성할 수 있습니다.

**주요 고급 기능은 다음과 같습니다:**
- **플랜 모드**: 코딩 전에 상세한 구현 계획을 수립합니다
- **확장 사고**: 복잡한 문제에 대한 심층 추론을 수행합니다
- **오토 모드**: 백그라운드 안전 분류기가 실행 전에 각 작업을 검토합니다
- **백그라운드 작업**: 대화를 막지 않고 장기 작업을 실행합니다
- **권한 모드**: Claude가 수행할 수 있는 작업을 제어합니다(`manual` — 이전 이름 `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`)
- **프린트 모드**: 자동화와 CI/CD를 위해 Claude Code를 비대화형으로 실행합니다(`claude -p`)
- **세션 관리**: 여러 작업 세션을 관리합니다
- **대화형 기능**: 키보드 단축키, 여러 줄 입력, 명령 기록을 제공합니다
- **음성 받아쓰기**: 20개 언어 STT를 지원하는 누르고 말하기 방식 음성 입력입니다
- **채널**: MCP 서버가 실행 중인 세션으로 메시지를 밀어 넣습니다(Research Preview)
- **원격 제어**: Claude.ai 또는 Claude 앱에서 Claude Code를 제어합니다
- **웹 세션**: claude.ai/code에서 브라우저로 Claude Code를 실행합니다
- **데스크톱 앱**: 시각적 diff 검토와 다중 세션을 제공하는 독립 실행 앱입니다
- **작업 목록**: 컨텍스트 압축을 넘어 지속되는 작업 추적을 제공합니다
- **프롬프트 제안**: 컨텍스트 기반으로 스마트한 명령을 제안합니다
- **Git 워크트리**: 병렬 작업을 위한 격리된 워크트리 브랜치를 제공합니다
- **샌드박싱**: OS 수준의 파일시스템·네트워크 격리를 제공합니다
- **관리형 설정**: plist, 레지스트리, 관리 파일을 통한 엔터프라이즈 배포를 지원합니다
- **구성**: JSON 구성 파일로 동작을 사용자 정의합니다

---

## 플랜 모드

플랜 모드를 사용하면 Claude가 구현 전에 복잡한 작업을 충분히 검토하여, 검토하고 승인할 수 있는 상세한 계획을 작성합니다.

### 플랜 모드란 무엇인가?

플랜 모드는 2단계 접근 방식입니다:
1. **플래닝 단계**: Claude가 작업을 분석하고 상세한 구현 계획을 작성합니다
2. **구현 단계**: 승인 후 Claude가 계획을 실행합니다

### 플랜 모드를 사용할 때

✅ 다음과 같은 경우 플랜 모드를 사용하세요:
- 복잡한 다중 파일 리팩터링
- 신규 기능 구현
- 아키텍처 변경
- 데이터베이스 마이그레이션
- 대규모 API 재설계

❌ 다음과 같은 경우에는 플랜 모드를 사용하지 마세요:
- 단순 버그 수정
- 포맷팅 변경
- 단일 파일 편집
- 간단한 질의

### 플랜 모드 활성화

**슬래시 커맨드**:
```bash
/plan Implement user authentication system
```

**CLI 플래그**:
```bash
claude --permission-mode plan
```

**기본값으로 설정**:
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**키보드 단축키**:
- `Shift + Tab` - 권한 모드 순환(플랜 모드 포함)
- `Alt + M` - 권한 모드 순환(Windows 전용, 런타임이 VT 입력 모드를 활성화하지 않은 경우)

### 플랜 모드의 이점

- **구조화된 구현 접근**: 구현 단계를 상세히 분해합니다
- **검토 및 승인**: 실행 전에 계획을 승인하거나 조정합니다
- **위험 식별**: 구현 전에 잠재적 문제를 파악합니다
- **명확한 단계**: 체계적인 구현 단계와 마일스톤을 제공합니다

### 예제: 기능 구현

```
User: /plan Add a real-time notification system

Claude: I'll create a plan for implementing real-time notifications.

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Install WebSocket libraries (socket.io)
2. Set up WebSocket server
3. Configure connection management

### Phase 2: Backend Implementation
4. Create notification service
5. Implement notification queue
6. Add database schema for notifications
7. Create API endpoints

### Phase 3: Frontend Integration
8. Set up WebSocket client
9. Create notification UI components
10. Implement notification state management
11. Add notification permissions

### Phase 4: Testing & Deployment
12. Write unit tests
13. Write integration tests
14. Update documentation
15. Deploy to staging

Estimated time: 3-4 hours
Files to modify: 12
New files to create: 8

Ready to proceed? (yes/no/modify plan)

User: yes

Claude: [Begins implementation following the plan]
```

### 플랜 수정

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: Updated plan:
[Shows modified plan with queue removed]

User: Looks good, proceed

Claude: [Implements modified plan]
```

### 플랜 모드 구성

플랜 모드는 CLI 플래그 또는 슬래시 커맨드로 활성화합니다:

```bash
# Activate plan mode via CLI
claude --permission-mode plan

# Or use the /plan slash command inside the REPL
/plan Implement user authentication system
```

**플래닝용 모델 별칭**: `opusplan`을 모델 별칭으로 사용하면 플래닝에는 Opus를, 실행에는 Sonnet을 사용합니다:

```bash
claude --model opusplan "design and implement the new API"
```

**외부에서 계획 편집**: `Ctrl+G`를 누르면 현재 계획이 외부 편집기에서 열려 세부적으로 수정할 수 있습니다.

> **v2.1.112 업데이트**: 이제 플랜 파일은 임의의 단어 대신 해당 계획을 만들어낸 프롬프트의 이름을 따서 저장됩니다. 따라서 파일을 찾아보고 재사용하기가 더 쉽습니다.

> **v2.1.136 업데이트 — 플랜 모드의 쓰기 차단은 무조건 적용됩니다**: 이제 플랜 모드는 모든 파일 쓰기를 차단하며, `permissions.allow`에 일치하는 `Edit(...)` 규칙이 있어도 마찬가지입니다. 이전에는 허용적인 `Edit(...)` 규칙이 있으면 플랜 모드에서도 쓰기가 통과될 수 있었으나, 그 우회 경로가 닫혔습니다. 이전 동작에 의존하던 워크플로가 있다면 편집 전에 `Shift+Tab`으로 플랜 모드를 종료하세요.

---

## 확장 사고

확장 사고를 사용하면 Claude가 해결책을 제시하기 전에 복잡한 문제를 더 오래 추론할 수 있습니다.

### 확장 사고란 무엇인가?

확장 사고는 의도적이고 단계적인 추론 과정으로, Claude가 다음을 수행합니다:
- 복잡한 문제를 분해합니다
- 여러 접근 방식을 검토합니다
- 트레이드오프를 평가합니다
- 엣지 케이스를 추론합니다

### 확장 사고 활성화

**키보드 단축키**:
- `Option + T`(macOS) / `Alt + T`(Windows/Linux) - 확장 사고를 토글합니다. Opus 5.5(v2.1.280 이후 기본 모델), Sonnet 5.5, Haiku 5.5, Fable 모델에서는 사고를 끌 수 없습니다. 해당 모델에서는 토글, `alwaysThinkingEnabled`, `MAX_THINKING_TOKENS=0` 모두 효과가 없습니다.

**자동 활성화**:
- 모든 모델에서 기본으로 활성화됩니다(Opus 5, Opus 4.8, Opus 4.7, Sonnet 4.6, Haiku 4.5)
- Opus 5 / Opus 4.8: 노력 수준을 지원하는 적응형 추론입니다: `low`(○), `medium`(◐), `high`(●), `xhigh`, `max`. 기본값은 Opus 5.5(v2.1.280 이후 기본 모델), Sonnet 5.5, Haiku 5.5에서 `medium`, Opus 5(v2.1.219), Sonnet 5, Opus 4.8(v2.1.154), Opus 4.6, Sonnet 4.6에서 `high`, Opus 4.7에서 `xhigh`입니다. `xhigh`는 Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7에서 사용할 수 있습니다(Opus 4.6 / Sonnet 4.6에서는 `high`로 폴백됩니다). `max`는 Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7/4.6 및 Sonnet 4.6에서 동작합니다(세션 한정). Haiku 4.5에는 노력 수준이 없습니다. Opus 5, Opus 4.8, Opus 4.7은 1M 토큰 네이티브 컨텍스트 창을 가집니다(1M 컨텍스트 수정은 v2.1.117에 반영되었으며, 그 이전에는 `/context`가 Opus 4.7을 200K 창 기준으로 잘못 계산하여 조기 자동 압축을 유발했습니다). v2.1.129부터 `/context`는 시각화를 UI 안에서만 표시합니다. ASCII 시각화가 더 이상 대화 컨텍스트로 유출되지 않으므로(호출당 약 1.6k 토큰 절약) `/context`를 부담 없이 호출할 수 있습니다.
- Opus 4.6 / Sonnet 4.6의 Pro/Max 구독자: 기본 노력 수준이 v2.1.117에서 `medium`에서 `high`로 올라갔습니다.
- 기타 모델: 최대 31,999 토큰의 고정 예산

**구성 방법**:
- 토글: `Alt+T` / `Option+T`, 또는 `/config` 사용
- 추론 보기: `Ctrl+O`(상세 모드)
- 노력 수준 설정: `/effort` 명령 또는 `--effort` 플래그

**사용자 지정 예산**:
```bash
export MAX_THINKING_TOKENS=1024
```

**노력 수준**(Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6에서 지원 — Haiku 4.5는 미지원):
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○), medium (◐), high (●), xhigh (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7), or max — default is high on Opus 5 and Opus 4.8
```

**CLI 플래그**:
```bash
claude --effort high "complex architectural review"
```

**슬래시 커맨드**:
```
/effort high
```

> **참고:** 프롬프트에 "ultrathink" 키워드를 넣으면 심층 추론 모드가 활성화됩니다. 노력 수준 `low`, `medium`, `high`, `max`는 Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6에서 지원됩니다(Haiku 4.5는 없음). `xhigh`는 Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7에서 사용할 수 있습니다. 기본 노력 수준은 Opus 5.5, Sonnet 5.5, Haiku 5.5에서 `medium`, Opus 5, Sonnet 5, Opus 4.8(그리고 Opus 4.6 / Sonnet 4.6)에서 `high`, Opus 4.7에서 `xhigh`입니다. 첫 실행 시 기본 노력 수준을 고정하는 Opus 4.8, Opus 4.7과 달리 Opus 5에는 그런 고정이 없어, 이전에 설정한 수준이 그대로 이어집니다. `/effort` 슬라이더에는 **Ultracode** 토글도 있습니다(Tab, 또는 `/effort ultracode [on|off]`). 이것은 모델 노력 수준이 **아니며**, 세션이 동작하는 노력 수준에서 Claude가 동적 워크플로를 오케스트레이션하도록 합니다. v2.1.284부터는 `xhigh`를 강제하지 않고 수준을 변경해도 유지됩니다. `--effort ultracode`와 Agent SDK의 `effortLevel: "ultracode"`는 여전히 `xhigh`를 설정합니다.

### Opus 5의 안전 분류기 폴백

과부하와 사용 불가를 처리하는 [`fallbackModel` 설정](#폴백-모델-fallbackmodel)과는 별개로, Claude Code는 안전 분류기가 요청을 표시하면 **카테고리 기반 폴백**을 적용합니다. Claude Code v2.1.219 이상이 필요합니다.

- **Opus 5**: 사이버보안으로 표시된 요청은 Opus 4.8에서 다시 실행됩니다. 생물학으로 표시된 요청은 대신 거부로 끝납니다. Opus 5는 폴백 모델 없이 자체 생물학 분류기를 운영하기 때문입니다. 이런 거부는 첫 번째로 표시된 요청부터 발생합니다.
- 공격적 보안이나 생물학 영역의 워크로드 — 침투 테스트, Capture the Flag(CTF) 실습, 생물학 인접 코드베이스 — 는 폴백을 자주 유발하며, 대개 첫 요청에서 발생합니다.

이것이 여기서 중요한 이유: Opus 5에서 [보안 리뷰 서브에이전트](../04-subagents/README.md)나 CTF/펜테스트 작업을 실행한다면, 사이버보안 프롬프트는 Opus 4.8로 조용히 재실행되고(노력 상한과 컨텍스트 창이 다름), 생물학 인접 프롬프트는 곧바로 거부될 것으로 예상하세요. 이런 동작이 방해된다면 다른 모델을 명시적으로 고정하세요.

**전환 제어** — `switchModelsOnFlag` 설정(v2.1.170+, 기본값 `true`)은 폴백이 조용히 일어날지 결정합니다. `false`로 설정하면 Claude Code가 대신 일시 정지하여, 모델 전환과 프롬프트 수정 중 하나를 선택할 수 있습니다. `/config`에는 **Switch models when a message is flagged** 항목으로 나타납니다.

```json
{
  "switchModelsOnFlag": false
}
```

### 확장 사고의 이점

- **심층 추론**: 복잡한 문제를 더 오래 사고합니다
- **더 나은 아키텍처 결정**: 포괄적인 평가를 바탕으로 정보에 기반한 선택을 합니다
- **엣지 케이스 고려**: 잠재적 문제와 시나리오를 미리 검토합니다
- **철저한 분석**: 복잡한 문제 해결을 위한 구조화된 접근을 제공합니다

### 예제: 아키텍처 결정

```
User: ultrathink Should we use microservices or a monolith for our e-commerce platform?

Claude: Let me think through this architectural decision carefully...

<extended_thinking>
## Context Analysis
- Team size: 5 developers
- Expected traffic: 10k daily users initially
- Need to scale to 100k+ users
- Limited DevOps resources
- 6-month timeline to MVP

## Approach 1: Microservices
Pros:
+ Independent scaling
+ Technology flexibility
+ Team independence
+ Fault isolation

Cons:
- Operational complexity
- Network overhead
- Distributed tracing needed
- Requires DevOps expertise
- Slower initial development

## Approach 2: Monolith
Pros:
+ Simpler deployment
+ Faster initial development
+ Easier debugging
+ Lower operational overhead
+ Single codebase

Cons:
- Scaling challenges later
- All-or-nothing deployments
- Technology lock-in
- Potential for tight coupling

## Decision Factors
1. Team size (5 devs) → Favors monolith
2. DevOps resources (limited) → Favors monolith
3. Timeline (6 months) → Favors monolith
4. Future scale (100k users) → Achievable with monolith + caching
5. Complexity budget → Limited

## Recommendation
Start with a **modular monolith**:
- Single deployment unit
- Clear module boundaries
- Clean interfaces between modules
- Prepare for future extraction to microservices if needed

This gives you:
✓ Fast initial development
✓ Low operational complexity
✓ Option to extract services later
✓ Clear architecture

Migration path: When you reach 50k+ users or specific modules need independent scaling, extract those modules into microservices.
</extended_thinking>

**Recommendation**: Implement a modular monolith with clean module boundaries.

This approach balances your current constraints (team size, timeline, DevOps resources) with future scalability needs. You can migrate specific modules to microservices later when there's a clear business need.
```

### 확장 사고 구성

확장 사고는 환경 변수, 키보드 단축키, CLI 플래그로 제어합니다:

```bash
# Set thinking token budget
export MAX_THINKING_TOKENS=16000

# Set effort level (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6): low (○), medium (◐), high (●), xhigh (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7), or max — default is high on Opus 5 and Opus 4.8
export CLAUDE_CODE_EFFORT_LEVEL=high
```

세션 중에는 `Alt+T` / `Option+T`로 토글하고, `/effort`로 노력 수준을 설정하며, `/config`로 구성할 수 있습니다.

> **간소화된 시스템 프롬프트(v2.1.154):** 간소화된 시스템 프롬프트가 이제 Haiku 4.5, Sonnet 5, Opus 4.7 및 해당 계열의 이전 모델을 제외한 모든 모델의 **기본값**입니다(Haiku 5.5와 Sonnet 5.5도 사용). Opus 5와 Opus 4.8에서 기준 토큰 오버헤드를 줄여 줍니다.

---

## 오토 모드

오토 모드는 백그라운드 안전 분류기로 실행 전에 각 작업을 검토하는 권한 모드입니다. Claude가 자율적으로 작업하면서 위험한 작업은 차단할 수 있습니다. 모든 플랜에서 사용할 수 있지만, 자격을 갖춘 모델이 필요합니다(Anthropic API 및 AWS의 Claude Platform에서는 Claude Opus 4.6 이상, Sonnet 4.6 이상, Haiku 5.5, Fable 모델. Bedrock, Vertex, Foundry, 로그인한 Claude 앱 게이트웨이 세션에서는 Sonnet 5 이상, Opus 4.7 이상, Haiku 5.5, Fable 모델). Team 및 Enterprise에서는 기본으로 켜져 있으며, 관리자가 관리형 설정에서 조직 전체에 대해 끌 수 있습니다.

### 요구 사항

오토 모드는 계정이 아래 요구 사항을 모두 충족할 때만 사용할 수 있습니다:

- **플랜**: 모든 플랜.
- **조직**: Team 및 Enterprise에서는 오토 모드가 기본으로 제공됩니다. 관리자는 관리형 설정에서 `permissions.disableAutoMode`를 `"disable"`로 설정하여 조직 전체에 대해 끌 수 있습니다.
- **모델**: Anthropic API 및 AWS의 Claude Platform에서는 Claude Opus 4.6 이상, Sonnet 4.6 이상, Haiku 5.5, Fable 모델. Amazon Bedrock, Google Cloud의 Agent Platform(Vertex AI), Microsoft Foundry, 로그인한 Claude 앱 게이트웨이 세션에서는 Claude Sonnet 5 이상, Opus 4.7 이상, Haiku 5.5(v2.1.293+), Fable 모델만 가능합니다. 이전 모델 — Sonnet 4.5, Opus 4.5, Haiku 4.5, claude-3 모델 — 은 어떤 공급자에서도 지원되지 않습니다.
- **공급자**: Anthropic API, AWS의 Claude Platform, Amazon Bedrock, Google Cloud의 Agent Platform(Vertex AI), Microsoft Foundry, 로그인한 Claude 앱 게이트웨이 세션에서 기본으로 제공됩니다. v2.1.158부터 v2.1.206까지는 Anthropic API와 AWS의 Claude Platform을 제외한 모든 곳에서 `CLAUDE_CODE_ENABLE_AUTO_MODE=1`을 설정하기 전까지 오토 모드가 꺼져 있었고, v2.1.207에서 그 요구 사항이 제거되었습니다. 이 변수는 호환성을 위해 여전히 허용되지만 v2.1.207 이후로는 효과가 없습니다.
- **분류기**: 추가 토큰 비용이 발생합니다. 단, Enterprise 플랜과 Claude API 계정에서는 v2.1.278+가 검사를 서버 측에서 무료로 실행합니다

### 오토 모드 활성화

```bash
# Interactive sessions start in auto mode when no permission mode is configured (v2.1.284+)
# To pick it explicitly, for example when your settings default to another mode:
claude --permission-mode auto

# Or cycle to it with Shift+Tab in the REPL
```

> **v2.1.112 업데이트**: 오토 모드에 더 이상 `--enable-auto-mode` 플래그가 필요하지 않습니다. Max 구독자는 Opus 4.7에서 바로 사용할 수 있습니다.

> **v2.1.158 업데이트**: 오토 모드가 Bedrock, Vertex, Foundry의 Opus 4.7/4.8에서 사용 가능해졌으며, `CLAUDE_CODE_ENABLE_AUTO_MODE=1`로 게이트되었습니다.
>
> **v2.1.207 업데이트**: 해당 옵트인 요구 사항이 제거되었습니다. 이제 Bedrock, Vertex AI, Microsoft Foundry, 로그인한 Claude 앱 게이트웨이 세션에서 Claude Sonnet 5, Opus 4.7, Opus 4.8, Fable 5(v2.1.219부터 Opus 5도)에 대해 오토 모드가 기본으로 제공되며, 플래그나 환경 변수가 필요하지 않습니다. 관리자는 관리형 설정의 `disableAutoMode`로 비활성화할 수 있습니다. `CLAUDE_CODE_ENABLE_AUTO_MODE`는 호환성을 위해 여전히 허용되지만 v2.1.207 이후로는 효과가 없습니다.

또는 기본 권한 모드로 설정할 수 있습니다:

```bash
claude --permission-mode auto
```

구성으로 설정:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### 분류기 동작 방식

백그라운드 분류기는 다음 결정 순서로 각 작업을 평가합니다:

1. **허용/거부 규칙** -- 명시적 권한 규칙을 먼저 확인합니다
2. **읽기 전용/편집 자동 승인** -- 파일 읽기와 편집은 자동으로 통과합니다
3. **분류기** -- 백그라운드 분류기가 작업을 검토합니다
4. **폴백** -- 연속 3회 또는 누적 20회 차단 후 프롬프트로 폴백합니다

### 기본 차단 작업

오토 모드는 기본적으로 다음을 차단합니다:

| 차단 작업 | 예시 |
|----------------|---------|
| 셸로 파이프 설치 | `curl \| bash` |
| 민감 데이터 외부 전송 | 네트워크를 통한 API 키, 자격 증명 |
| 프로덕션 배포 | 프로덕션을 대상으로 하는 배포 명령 |
| 대량 삭제 | 대규모 디렉터리에 대한 `rm -rf` |
| IAM 변경 | 권한 및 역할 수정 |
| main 강제 푸시 | `git push --force origin main` |

> **분류기로 넘어간 판단이 늘어남(v2.1.218)**: 분류기는 이제 `rm -rf /`나 `rm -rf ~`처럼 파일시스템 루트나 홈 디렉터리를 대상으로 하는 삭제도 판단하며, 명령 치환이나 프로세스 치환 안에 들어 있는 경우도 포함합니다. v2.1.218 이전에는 단순한 형태가 승인을 요구했고, 치환 형태는 v2.1.208부터 v2.1.217까지 승인을 요구했습니다. 백그라운드 `&`와 의심스러운 Windows 경로 검사도 마찬가지로 더 이상 권한 대화상자를 열지 않고 분류기가 판단합니다.

### 기본 허용 작업

| 허용 작업 | 예시 |
|----------------|---------|
| 로컬 파일 작업 | 프로젝트 파일 읽기, 쓰기, 편집 |
| 선언된 의존성 설치 | 매니페스트 기반 `npm install`, `pip install` |
| 읽기 전용 HTTP | 문서 조회용 `curl` |
| 현재 브랜치로 푸시 | `git push origin feature-branch` |

### 오토 모드 구성

**기본 규칙을 JSON으로 출력**:
```bash
claude auto-mode defaults
```

**기본 오토 모드 구성 복원**(v2.1.212), 확인 프롬프트 포함(`--yes`로 건너뜀):
```bash
claude auto-mode reset
claude auto-mode reset --yes
```

**신뢰할 수 있는 인프라 구성**: 엔터프라이즈 배포에서는 `autoMode.environment` 관리형 설정을 사용합니다. 관리자가 신뢰할 수 있는 CI/CD 환경, 배포 대상, 인프라 패턴을 정의할 수 있습니다.

#### `"$defaults"`로 기본값 확장(v2.1.118)

v2.1.118부터 `autoMode.allow`, `autoMode.soft_deny`, `autoMode.environment`는 기본 목록을 교체하는 대신 사용자 규칙을 **덧붙이는** `"$defaults"` 토큰을 허용합니다. v2.1.118 이전에는 사용자 정의 배열이 내장 목록을 조용히 덮어썼습니다.

#### `autoMode.hard_deny`로 무조건 차단(v2.1.136)

`autoMode.hard_deny`(v2.1.136+)는 추론된 사용자 의도와 **무관하게** 특정 부류의 작업을 차단하는 분류기 규칙 배열입니다. 오토 모드에서 절대 실행되어서는 안 되는 작업 — 예를 들어 루트 경로에 대한 `rm -rf`나 보호된 브랜치에 대한 `git push --force` — 에 사용하세요. `soft_deny`와 달리 hard-deny 규칙은 분류기가 협상할 수 없습니다.

```json
{
  "autoMode": {
    "hard_deny": ["Bash(rm -rf /:*)", "Bash(git push --force*)"]
  }
}
```

**이전(내장 목록 교체 — v2.1.118 이전 동작):**

```json
{
  "autoMode": {
    "allow": ["Bash(gh pr list:*)"]
  }
}
```

**이후(내장 목록 확장 — v2.1.118+):**

```json
{
  "autoMode": {
    "allow": ["$defaults", "Bash(gh pr list:*)"],
    "soft_deny": ["$defaults", "Bash(kubectl delete:*)"],
    "environment": ["$defaults", "trusted-ci.internal"]
  }
}
```

배포되는 기준 규칙을 유지하면서 그 위에 조직 또는 프로젝트별 추가 규칙을 얹으려면 `"$defaults"`를 사용하세요.

#### `autoMode.classifyAllShell`로 모든 셸 명령 분류(v2.1.193)

`autoMode.classifyAllShell`(불리언, v2.1.193+)은 **모든** Bash/PowerShell 명령을 오토 모드 분류기로 라우팅합니다. 세션의 모든 셸 명령을 분류기가 검사하도록 하려면 활성화하세요.

```json
{
  "autoMode": {
    "classifyAllShell": true
  }
}
```

같은 릴리스에서는 오토 모드가 작업을 차단할 때 **거부 사유**를 표시합니다. 트랜스크립트, 거부 토스트, `/permissions`의 최근 거부 목록에서 확인할 수 있습니다(v2.1.193+).

#### 내장 의도 기반 보호(v2.1.183)

사용자가 구성한 `hard_deny`와는 별개로, 오토 모드는 이번 세션에서 명시적으로 요청하지 않은 한 다음 파괴적 명령을 기본으로 차단합니다:

- `git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`
- `git commit --amend`(이번 세션에서 에이전트가 만든 커밋이 아닌 경우)
- `terraform destroy`, `pulumi destroy`, `cdk destroy`(특정 스택을 요청하지 않은 경우)

이는 추론된 의도에 기반한 내장 기본 보호이므로, 사용자가 직접 `hard_deny`에 추가할 필요가 없습니다.

### 폴백 동작

분류기가 확신하지 못하면 오토 모드는 사용자에게 묻는 방식으로 폴백합니다:
- 분류기 차단이 **연속 3회** 발생한 후
- 세션에서 분류기 차단이 **누적 20회** 발생한 후

이를 통해 분류기가 작업을 확신 있게 승인하지 못할 때는 항상 사용자가 제어권을 유지합니다.

### 오토 모드 등가 권한 시딩

백그라운드 분류기 없이 더 단순한 방식을 원한다면, `~/.claude/settings.json`에 보수적인 안전 권한 규칙 기준선을 시딩할 수 있습니다. 스크립트는 읽기 전용 및 로컬 검사 규칙으로 시작하고, 편집, 테스트, 로컬 git 쓰기, 패키지 설치, GitHub 쓰기 작업은 원할 때만 옵트인할 수 있습니다.

**파일:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Preview what would be added (no changes written)
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Apply the conservative baseline
python3 09-advanced-features/setup-auto-mode-permissions.py

# Add more capability only when you need it
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

스크립트는 다음 범주에 걸쳐 규칙을 추가합니다:

| 범주 | 예시 |
|----------|---------|
| 핵심 읽기 전용 도구 | `Read(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)`, `WebFetch(*)` |
| 로컬 검사 | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)`, `Bash(cat:*)` |
| 선택적 편집 | `Edit(*)` |
| 선택적 테스트/빌드 | `Bash(pytest:*)`, `Bash(python3 -m pytest:*)`, `Bash(cargo test:*)` |
| 선택적 git 쓰기 | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)`, `Bash(git switch:*)`, `Bash(git stash:*)`, `Bash(git tag:*)` |
| 패키지 관리자 | `Bash(npm ci:*)`, `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(pip3 install:*)` |
| 빌드 및 테스트 | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| 일반 셸 | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

위험한 작업(`rm -rf`, `sudo`, 강제 푸시, `DROP TABLE`, `terraform destroy` 등)은 의도적으로 제외됩니다. 스크립트는 멱등이므로 두 번 실행해도 규칙이 중복되지 않습니다.

---

## 백그라운드 작업

백그라운드 작업을 사용하면 장기 실행 작업이 대화를 막지 않고 실행됩니다.

### 백그라운드 작업이란?

백그라운드 작업은 사용자가 계속 작업하는 동안 비동기로 실행됩니다:
- 긴 테스트 스위트
- 빌드 프로세스
- 데이터베이스 마이그레이션
- 배포 스크립트
- 분석 도구

**기본 사용법:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/tasks    # View and manage background work (shells and subagents); stop a task from here
Ctrl+B    # Move a running Bash command or agent to the background
```

### 백그라운드 작업 시작

```
User: Run the full test suite in the background

Claude: Starting tests in background (task-id: bg-1234)
You can continue working while tests run.

[You can continue the conversation]

User: Meanwhile, let's refactor the auth module

Claude: [Works on auth module while tests run in background]

[Later, when tests complete]

Claude: 📢 Background task bg-1234 completed:
✅ 245 tests passed
❌ 3 tests failed
View results: /tasks
```

### 백그라운드 작업 관리

`/tasks`(별칭 `/bashes`)를 실행하면 실행 중인 셸과 서브에이전트 목록이 표시되고, 항목을 열어 출력을 확인하거나 중지할 수 있습니다. `/task` 하위 명령은 없습니다.

```text
User: /tasks

[Opens the background-work view: running shells and subagents,
 including subagents that have finished. Select one to see its
 output, or stop it from here.]
```

### 예제: 병렬 개발

```
User: Run the build in the background

Claude: Starting build... (task-id: bg-5001)

User: Also run the linter in background

Claude: Starting linter... (task-id: bg-5002)

User: While those run, let's implement the new API endpoint

Claude: [Implements API endpoint while build and linter run]

[10 minutes later]

Claude: 📢 Build completed successfully (bg-5001)
📢 Linter found 12 issues (bg-5002)

User: Show me the linter issues

Claude: [Shows linter output from bg-5002]
```

### 구성

백그라운드 작업용 `settings.json` 블록은 없습니다. 이 기능은 환경 변수로 제어합니다:

```bash
# Turn background tasks off entirely
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
```

동시성도 백그라운드 작업 설정이 아닙니다. 동시에 실행되는 에이전트 수는 `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`(기본값 `20`)로 결정됩니다.

백그라운드 Bash 및 PowerShell 명령은 무인 세션에서만 시간 제한이 적용됩니다(v2.1.288). `-p` 실행, Agent SDK 세션, CI, 클라우드 세션에서는 `run_in_background`로 시작한 명령이 `timeout` 후에 중지되며(기본 30분, 최대 2시간), 중지되면 Claude에게 알림이 전달됩니다. 터미널, 데스크톱 앱, VS Code 세션의 백그라운드 명령에는 시간 제한이 없습니다(v2.1.285–v2.1.287에서는 모든 세션에 제한이 적용되었습니다).

---

## Monitor 도구 (이벤트 기반 스트림)

> **v2.1.98의 신규 기능**: Monitor 도구를 사용하면 Claude가 백그라운드 명령의 stdout을 지켜보다가 일치하는 이벤트가 나타나는 즉시 반응합니다. 장기 실행 프로세스를 기다릴 때 폴링 루프와 `sleep`을 대체합니다.

Monitor는 stdout에 쓰는 모든 셸 명령에 연결됩니다. 명령의 각 stdout 줄이 세션을 깨우는 알림이 됩니다. Claude가 명령을 지정하면 하네스가 출력을 스트리밍하고 이벤트가 발생하는 대로 전달합니다. 기반 프로세스를 시작하는 방법은 관련 [백그라운드 작업](#백그라운드-작업) 절을 참고하세요.

> **기한(v2.1.271)**: 이제 모든 Monitor 감시에는 기한이 있습니다 — 최대 30분, 단일 프롬프트 `-p` 실행에서는 10분입니다. 기한이 지나면 Claude에게 알림이 전달되어 감시를 다시 걸 수 있습니다. 시간 초과 없이 유지되는 감시를 거는 방법은 더 이상 없습니다.

### 중요한 이유

`/loop`나 `sleep`으로 폴링하면 변화가 있든 없든 매 주기마다 API 왕복이 한 번씩 소모됩니다. Monitor는 이벤트가 발생할 때까지 조용히 대기하므로 명령이 조용한 동안 **토큰을 전혀** 소비하지 않습니다. 이벤트가 발생하면 Claude는 다음 폴링 주기를 기다리지 않고 즉시 반응합니다. 몇 분 이상 걸리는 작업이라면 폴링 루프보다 저렴하고 빠릅니다.

### 두 가지 일반 패턴

**스트림 필터**는 장기 실행 소스의 연속 출력을 감시합니다. 명령은 계속 실행되고, 일치하는 모든 줄이 이벤트가 됩니다.

```bash
tail -f /var/log/app.log | grep --line-buffered "ERROR"
```

**폴링 후 방출 필터**는 소스를 주기적으로 확인하고 변경이 있을 때만 이벤트를 방출합니다. API, 데이터베이스처럼 네이티브 스트림이 없는 대상에 사용하세요.

```bash
last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
while true; do
  gh api "repos/owner/repo/issues/123/comments?since=$last" || true
  last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  sleep 30
done
```

### 구체적 예시

"개발 서버를 시작하고 오류를 모니터링해 줘"라고 하면, Claude는 서버를 백그라운드 작업으로 실행하고 Monitor 필터(`tail -F server.log | grep --line-buffered -E "ERROR|FATAL"`)를 연결하며 세션은 조용해집니다. 로그에 오류 줄이 나타나는 순간 Claude가 깨어나 오류를 읽고 대응합니다 — 서버 재시작, 버그 수정, 또는 사용자에게 알림 — 사용자가 직접 확인할 필요가 없습니다.

> **경고**: `grep`으로 파이프할 때는 **반드시** `grep --line-buffered`를 사용하세요. 이 옵션이 없으면 grep이 stdout을 4KB 단위로 버퍼링하여 트래픽이 적은 스트림에서는 이벤트가 몇 분씩 지연될 수 있습니다. 실제로 Monitor가 깨지는 가장 흔한 원인입니다. 필터가 조용해서는 안 될 때 조용하다면 `--line-buffered` 플래그부터 확인하세요.

---

## 동적 워크플로

> **v2.1.154의 신규 기능**

동적 워크플로를 사용하면 Claude가 수십에서 수백 개의 백그라운드 [서브에이전트](../04-subagents/README.md)를 **결정적으로** 오케스트레이션할 수 있습니다. 팬아웃, 파이프라인, 병렬 단계를 모델의 즉흥성에 맡기지 않고 스크립트에 인코딩합니다. 단일 에이전트는 컨텍스트 창 하나를 사용하지만, 워크플로는 작업을 여러 에이전트에 분해하고 결과를 다시 결합합니다.

v2.1.219부터 동적 워크플로의 기본값은 **중간 크기 가이드라인(에이전트 10개 미만 목표)** 이며, v2.1.271부터 Pro 플랜으로 로그인한 경우에는 **소규모**입니다. `/config`의 **Dynamic workflow size**에서 다른 크기나 무제한을 선택하거나, 설정 파일의 `workflowSizeGuideline` 키로 지정할 수 있습니다. 실행 중인 워크플로의 상태 표시줄에 활성 크기가 표시되며, 변경은 `/config`에서 하라고 안내합니다.

### 사용 시점

- **포괄적 커버리지** — 여러 파일/차원에 걸친 감사나 리뷰를 병렬로 수행합니다.
- **확신** — 독립적인 관점을 생성한 뒤 적대적으로 검증한 후 확정합니다.
- **하나의 컨텍스트를 넘는 규모** — 단일 컨텍스트로 감당할 수 없는 대규모 마이그레이션, 광범위한 훑기, 리서치에 사용합니다.

이미 이해하고 있는 일회성 작업에는 단일 에이전트(또는 직접 편집)가 여전히 적합합니다. 워크플로는 작업이 팬아웃될 때 가치가 있습니다.

### 실행 및 확인

- **실행**: Claude에게 해당 작업용 워크플로 생성을 요청하세요(예: "`src/`의 모든 파일을 리뷰하는 워크플로를 실행해 줘"). Claude가 오케스트레이션 스크립트를 작성하고 백그라운드에서 실행합니다.
- **확인**: `/workflows` 명령은 실행 중이거나 완료된 워크플로 실행을 실시간 진행 상황과 함께 보여줍니다.
- **`ultracode`**: `/effort` 슬라이더의 Ultracode 토글(Tab) 또는 `/effort ultracode [on|off]`로 켜면, Claude가 세션이 동작하는 노력 수준에서 동적 워크플로를 기본으로 오케스트레이션합니다. v2.1.284부터 토글은 노력 수준을 변경하지 않습니다(이전에는 `xhigh`를 강제했습니다). `--effort ultracode`와 Agent SDK의 `effortLevel: "ultracode"`는 여전히 `xhigh`를 설정합니다. `/effort ultracode`는 세션 동안 유지되며, 설정의 `ultracode` 키를 지정하면 모든 세션을 그것으로 시작합니다(`effortLevel`과 `CLAUDE_CODE_EFFORT_LEVEL`은 `ultracode`를 허용하지 않습니다). v2.1.160부터 트리거 키워드는 `ultracode`이며, "workflow"라는 단어만으로는 더 이상 실행이 트리거되지 않습니다.

워크플로는 서브에이전트 모델 위에 구축됩니다. 개별 에이전트가 어떻게 정의되고 범위가 정해지는지는 [서브에이전트](../04-subagents/README.md)를 참고하세요.

---

## 예약된 작업

예약된 작업을 사용하면 프롬프트를 반복 일정에 따라 자동으로 실행하거나 일회성 알림으로 설정할 수 있습니다. 작업은 세션 범위이며 Claude Code가 활성 상태일 때 실행되고 세션이 끝나면 정리됩니다. v2.1.72+부터 사용할 수 있습니다.

> **claude.com에서 "Routines"로 마케팅됨(2026-05-14)**: Anthropic 제품 블로그는 이 기능을 **Routines**로 소개합니다. CLI 명령은 `/schedule`로 유지되며, 이 안내서는 연속성을 위해 원래 이름인 "예약된 작업"을 사용합니다. claude.com 문서나 데스크톱 앱에서 "Routines"를 보면 같은 기능을 가리킵니다.

### `/loop` 명령

```bash
# Explicit interval
/loop 5m check if the deployment finished

# Natural language
/loop check build status every 30 minutes
```

정확한 일정 지정을 위해 표준 5필드 cron 표현식도 지원합니다.

### 일회성 알림

특정 시각에 한 번 발생하는 알림을 설정합니다:

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### 예약된 작업 관리

| 도구 | 설명 |
|------|-------------|
| `CronCreate` | 새 예약 작업 생성 |
| `CronList` | 활성 예약 작업 전체 나열. v2.1.136부터 출력에 한정자와 예약된 프롬프트 본문도 포함되므로, 각 cron을 열지 않고도 무엇이 실행될지 감사할 수 있습니다. |
| `CronDelete` | 예약 작업 제거 |

**제한 및 동작**:
- 세션당 최대 **50개 예약 작업**
- 세션 범위 — 세션이 끝나면 정리됨
- 반복 작업은 **3일** 후 자동 만료
- Claude Code가 실행 중일 때만 작업이 발생하며, 놓친 실행은 보충되지 않음

### 동작 세부 사항

| 항목 | 세부 내용 |
|--------|--------|
| **반복 지터** | 간격의 최대 10%(최대 15분) |
| **일회성 지터** | :00/:30 경계에서 최대 90초 |
| **놓친 실행** | 보충 없음 — Claude Code가 실행 중이 아니면 건너뜀 |
| **지속성** | 재시작 후 유지되지 않음 |

### 클라우드 예약 작업

`/schedule`을 사용하면 Anthropic 인프라에서 실행되는 클라우드 예약 작업을 만들 수 있습니다:

```
/schedule daily at 9am run the test suite and report failures
```

클라우드 예약 작업은 재시작 후에도 유지되며 Claude Code가 로컬에서 실행 중일 필요가 없습니다.

### 예약된 작업 비활성화

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

> **API 키 티어에 의해 `/schedule` 자동 비활성화(v2.1.139)**: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper` 중 하나라도 설정되어 있으면 클라우드 `/schedule`은 조용히 사용할 수 없게 됩니다. claude.ai로 함께 로그인되어 있어도 마찬가지입니다. 같은 조건에서 [원격 제어](#remote-control-비활성화-disableremotecontrol-v21128), claude.ai MCP 커넥터, 알림 환경설정도 비활성화됩니다. `/schedule`을 사용하려면 API 키를 해제하거나 Pro/Max OAuth 티어로 실행하세요. 로컬 `CronCreate`는 영향을 받지 않습니다.

### 예제: 배포 모니터링

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **팁**: 예약된 작업은 세션 범위입니다. 재시작에도 살아남는 영구 자동화가 필요하면 CI/CD 파이프라인, GitHub Actions, 데스크톱 앱의 예약 작업을 대신 사용하세요.

---

## 권한 모드

권한 모드는 Claude가 명시적 승인 없이 수행할 수 있는 작업을 제어합니다.

### 사용 가능한 권한 모드

| 모드 | 동작 |
|---|---|
| `manual` | 파일만 읽기, 그 외 모든 작업은 프롬프트로 확인. v2.1.200에서 `default`라는 이름이 변경되었고 `default`도 별칭으로 계속 허용됩니다 |
| `acceptEdits` | 파일 읽기와 편집, 명령은 프롬프트로 확인 |
| `plan` | 파일만 읽기(리서치 모드, 편집 없음) |
| `auto` | 모든 작업에 백그라운드 안전 분류기 검사 적용. 자격을 갖춘 모델(모든 공급자에서 Sonnet 5 이상, Opus 4.7 이상, Haiku 5.5, Fable 모델. Anthropic API 및 AWS의 Claude Platform에서는 Opus 4.6과 Sonnet 4.6도 해당)과 공급자가 필요하며, 모든 플랜에서 사용 가능 — [오토 모드](#오토-모드) 참고 |
| `bypassPermissions` | 모든 작업 허용, 권한 검사 없음(위험) |
| `dontAsk` | 사전 승인된 도구만 실행하고 나머지는 모두 거부 |

> **참고**: `default` 권한 모드는 v2.1.200에서 **Manual**로 이름이 변경되었으며(CLI, `--help`, VS Code, JetBrains 전반), 활성 상태일 때 하단에 회색 ⏸ 배지가 표시됩니다(v2.1.203). `--permission-mode manual`과 `--permission-mode default`가 모두 동작하고, 설정의 `"defaultMode": "manual"`과 `"defaultMode": "default"`도 모두 동작합니다. 설정 키는 `permissions.defaultMode`라는 점에 유의하세요. `permissions.mode` 키는 없으므로 아래 예시는 정규 표기를 사용합니다.

CLI에서 `Shift+Tab`으로 모드를 순환합니다. `--permission-mode` 플래그나 `permissions.defaultMode` 설정으로 기본값을 지정하세요. 권한 모드가 구성되지 않은 경우, v2.1.284부터 모든 플랜과 공급자에서 대화형 터미널과 VS Code 세션이 오토 모드로 시작합니다(v2.1.283에서는 Bedrock, Google Cloud의 Agent Platform, Foundry 같은 서드파티 공급자이거나 텔레메트리가 꺼진 경우에만 그렇게 했습니다). `permissions.defaultMode`가 여전히 이를 재정의하며, 오토 모드를 사용할 수 없는 세션은 대신 Manual로 시작합니다. v2.1.302부터 권한 모드를 지정하지 않은 `claude -p` 및 Agent SDK 세션은 서드파티 공급자이거나, 텔레메트리가 꺼져 있거나, 새로 설치한 경우 `default` 모드로 시작합니다. 오토 모드를 유지하려면 `--permission-mode auto`를 전달하세요.

> **플랜 모드는 셸 명령을 분류기에 위임(v2.1.218)**: [오토 모드](#오토-모드)를 사용할 수 있고 `useAutoModeDuringPlan` 설정이 켜져 있을 때(기본값이 켜짐) 분류기가 플래닝 중 셸 명령을 사용자에게 묻는 대신 검토합니다. 승인된 명령은 실행되고 거부된 명령은 차단됩니다. 플랜 모드는 여전히 파일 쓰기를 무조건 차단합니다.

v2.1.160부터 `acceptEdits`도 셸 시작 파일(`.zshenv`, `.zlogin`, `.bash_login`, `~/.config/git/`)과 코드를 실행하는 빌드 구성(`.npmrc`, `.yarnrc*`, `bunfig.toml`, `.bazelrc`, `.pre-commit-config.yaml`, `.devcontainer/` 등)에 쓰기 전에 확인을 요구합니다. 그렇지 않으면 의도치 않은 명령 실행으로 이어질 수 있기 때문입니다.

> **`--dangerously-skip-permissions` 경로 범위 확대(v2.1.121, v2.1.126)**: `--dangerously-skip-permissions` CLI 플래그(및 이에 상응하는 `bypassPermissions` 모드)가 훨씬 넓은 허용 목록에 대한 쓰기 프롬프트를 우회합니다 — `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/`, `.git/`, `.vscode/`, 셸 구성 파일. 재앙적인 삭제 명령(`rm -rf /` 등)은 이 모드에서도 여전히 프롬프트를 표시합니다. v2.1.281부터 해당 프롬프트는 2분 대기한 뒤 재작성 힌트와 함께 명령을 거부하므로 무인 세션이 계속 진행할 수 있습니다(`CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1`로 끌 수 있음). 오토 모드에서는 크리티컬 패스 삭제가 대신 분류기로 전달되지만, `rm -rf "$(pwd)"` 같은 다른 위험한 `rm` 형태는 여전히 프롬프트를 표시합니다 — [오토 모드](#오토-모드) 참고. 이 플래그는 이전보다 예리한 도구이므로 일회용 샌드박스에서만 사용하세요.

> **Windows 셸 감지(v2.1.120, v2.1.126)**: Git for Windows / Git Bash가 더 이상 필요하지 않습니다. Git Bash가 없으면 Claude Code가 PowerShell을 셸 도구로 사용합니다. v2.1.126부터 PowerShell 도구가 활성화된 경우 PowerShell이 *주* 셸이며, 감지는 Microsoft Store로 설치한 PowerShell 7, PATH가 없는 MSI 설치, `.NET global tool` 설치까지 포함합니다.

> **Windows에서 Bedrock/Vertex/Foundry용 PowerShell 도구 기본 활성화(v2.1.143)**: v2.1.143부터 Bedrock, Vertex, Foundry 사용자의 경우 **Windows에서 PowerShell 도구가 기본 활성화**됩니다. Claude Code는 시스템 정책이 `Restricted`여도 스크립트가 실행되도록 `-ExecutionPolicy Bypass`로 PowerShell을 호출합니다. Claude Code가 시스템 실행 정책을 따르게 하려면 `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`을 설정하세요. PowerShell 도구를 완전히 비활성화하려면 `CLAUDE_CODE_USE_POWERSHELL_TOOL=0`을 설정하세요.

### 활성화 방법

**키보드 단축키**:
```bash
Shift + Tab  # Cycle default → acceptEdits → plan, then bypassPermissions/auto when available (dontAsk never appears in the cycle)
```

**슬래시 커맨드**:
```bash
/plan                  # Enter plan mode
```

**CLI 플래그**:
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**설정**:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### 권한 모드 예제

#### 기본 모드
Claude가 중요한 작업에 대해 확인을 요청합니다:

```
User: Fix the bug in auth.ts

Claude: I need to modify src/auth.ts to fix the bug.
The change will update the password validation logic.

Approve this change? (yes/no/show)
```

#### 플랜 모드
실행 전에 구현 계획을 검토합니다:

```
User: /plan Implement user authentication system

Claude: I'll create a plan for implementing authentication.

## Implementation Plan
[Detailed plan with phases and steps]

Ready to proceed? (yes/no/modify)
```

#### 편집 수락 모드
파일 수정을 자동으로 승인합니다:

```
User: acceptEdits
User: Fix the bug in auth.ts

Claude: [Makes changes without asking]
```

### 사용 사례

**코드 리뷰**:
```
User: claude --permission-mode plan
User: Review this PR and suggest improvements

Claude: [Reads code, provides feedback, but cannot modify]
```

**페어 프로그래밍**:
```
User: claude --permission-mode default
User: Let's implement the feature together

Claude: [Asks for approval before each change]
```

**자동화 작업**:
```
User: claude --permission-mode acceptEdits
User: Fix all linting issues in the codebase

Claude: [Auto-accepts file edits without asking]
```

---

## 헤드리스 모드

프린트 모드(`claude -p`)를 사용하면 Claude Code가 대화형 입력 없이 실행되므로 자동화와 CI/CD에 적합합니다. 이것이 비대화형 모드이며, 이전의 `--headless` 플래그를 대체합니다.

### 프린트 모드란?

프린트 모드는 다음을 가능하게 합니다:
- 자동화된 스크립트 실행
- CI/CD 통합
- 배치 처리
- 예약 작업

### 프린트 모드로 실행 (비대화형)

```bash
# Run specific task
claude -p "Run all tests"

# Process piped content
cat error.log | claude -p "Analyze these errors"

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### 추가 프린트 모드 사용 예시

```bash
# Run a specific task with output capture
claude -p "Run all tests and generate coverage report"

# With structured output
claude -p --output-format json "Analyze code quality"

# With input from stdin
echo "Analyze code quality" | claude -p "explain this"
```

### 예제: CI/CD 통합

**GitHub Actions**:
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for:
            - Code quality issues
            - Security vulnerabilities
            - Performance concerns
            - Test coverage
            Output results as JSON" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: JSON.stringify(review, null, 2)
            });
```

### 프린트 모드 구성

프린트 모드(`claude -p`)는 자동화를 위한 여러 플래그를 지원합니다:

```bash
# Limit autonomous turns
claude -p --max-turns 5 "refactor this module"

# Structured JSON output
claude -p --output-format json "analyze this codebase"

# With schema validation
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# Disable session persistence
claude -p --no-session-persistence "one-off analysis"
```

### 안전 모드 (문제 해결)

`--safe-mode`(및 `CLAUDE_CODE_SAFE_MODE` 환경 변수, 예: `CLAUDE_CODE_SAFE_MODE=1`)는 **모든 사용자 정의를 비활성화한** 상태로 Claude Code를 시작합니다. CLAUDE.md, 플러그인, 스킬, 훅, MCP 서버가 모두 꺼집니다.

```bash
# Launch with every customization disabled
claude --safe-mode

# Equivalent via environment variable
CLAUDE_CODE_SAFE_MODE=1 claude
```

문제 해결 도구입니다. 사용자 정의 구성이 문제를 일으킬 때 안전 모드로 실행하여, 문제가 설정에 있는지 Claude Code 자체에 있는지 분리해 확인할 수 있습니다.

---

## 세션 관리

여러 Claude Code 세션을 효과적으로 관리합니다.

### 세션 관리 명령

| 명령 | 설명 |
|---------|-------------|
| `/resume` | ID 또는 이름으로 대화를 재개합니다 |
| `/rename` | 현재 세션에 이름을 지정합니다 |
| `/fork [prompt]` | 대화를 새 독립 백그라운드 세션으로 복사하고 여기서 계속 작업합니다(v2.1.212+) |
| `/subtask <task>` | 전체 대화를 상속하는 포크된 서브에이전트를 생성하고 결과를 여기로 보고합니다(v2.1.212+) |
| `/branch [name]` | 현재 지점의 대화 복사본으로 전환하며 원본은 보존합니다 |
| `claude -c` | 가장 최근 대화를 계속합니다 |
| `claude -r "session"` | 이름 또는 ID로 세션을 재개합니다 |

### 세션 재개

**마지막 대화 계속**:
```bash
claude -c
```

**이름이 지정된 세션 재개**:
```bash
claude -r "auth-refactor" "finish this PR"
```

**현재 세션 이름 변경**(REPL 내부):
```
/rename auth-refactor
```

> **v2.1.212 업데이트**: 에이전트 뷰에서 `/resume`을 인수 없이 입력하면 과거 세션 선택기가 열리고(표시 목록에서 제거된 세션 포함), 선택한 세션을 백그라운드 세션으로 재개합니다.

### 세션 포크 및 분기

대화의 복사본을 만드는 세 가지 명령이 있으며, **복사본이 실행되는 위치**가 다릅니다:

`/subtask <task>`는 전체 대화를 상속하는 포크된 서브에이전트를 생성하여 사용자가 계속 작업하는 동안 해당 작업을 수행합니다. `claude agents`에 자체 행이 표시되고, 완료되면 결과가 사용자 대화로 반환됩니다:

```
/subtask Investigate why the auth tests are flaky
```

`/fork [prompt]`는 대신 대화를 새 **백그라운드 세션**으로 복사합니다. 복사본은 지금까지의 모든 내용으로 시작하여 독립적으로 실행되며, 이 대화로 돌아오는 것은 없습니다:

```
/fork Try the OAuth approach end to end
```

위임하지 않고 직접 복사본으로 전환하려면 `/branch [name]`을 사용하세요. 원본을 보존하며 `/resume`으로 원본으로 돌아올 수 있습니다:

```
/branch try-oauth-instead
```

> **참고**: `/fork`와 `/subtask`는 **v2.1.212**에서 역할이 바뀌었습니다. v2.1.161 이전에는 `/fork`가 `/branch`의 별칭이었고, v2.1.161부터 v2.1.211까지는 포크된 서브에이전트를 시작했으며, 이 동작은 이제 `/subtask`가 담당합니다. 에이전트 뷰가 꺼져 있으면 `/subtask`를 사용할 수 없고 `/fork`가 포크된 서브에이전트 동작을 유지합니다.

또는 CLI에서 포크할 수 있습니다:
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### 세션 지속성

세션은 자동으로 저장되고 재개할 수 있습니다:

```bash
# Continue last conversation
claude -c

# Resume specific session by name or ID
claude -r "auth-refactor"

# Resume and fork for experimentation
claude --resume auth-refactor --fork-session "alternative approach"
```

### 사용량 한도 자동 계속 (v2.1.234)

**v2.1.234**부터 claude.ai 사용량 한도로 막힌 세션은 한도가 재설정되면 자동으로 계속됩니다. 다시 프롬프트할 필요가 없습니다. `/config`의 "Continue automatically at usage limit"에서 토글할 수 있습니다.

### 세션 요약 (v2.1.108)

자리를 비운 뒤 세션으로 돌아오면 Claude가 그동안 무엇을 했는지 간단한 요약을 보여줄 수 있습니다. 모든 플랜과 공급자에서 기본으로 켜져 있으며, `/config` → **Session recap**에서 끌 수 있습니다.

> **OTEL 텔레메트리 — 피드백 설문 재활성화(v2.1.136+)**: OpenTelemetry 데이터를 수집하는 조직은 `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL=1`을 설정하여 Anthropic의 세션 품질 설문을 다시 활성화할 수 있습니다. 이 설문은 이전에 텔레메트리 파이프라인에서 우회되었기 때문에 OTEL 배포에서는 기본적으로 꺼져 있습니다.

> **OTEL 텔레메트리 — `assistant_response` 로그 이벤트(v2.1.193+)**: Claude Code는 모델의 응답 텍스트를 담은 `claude_code.assistant_response` OpenTelemetry 로그 이벤트를 내보내므로, OTEL 파이프라인이 기존 도구/이벤트 텔레메트리와 함께 Claude가 한 말을 수집할 수 있습니다.

> **OTEL 텔레메트리 — 캐시 및 GenAI 속성(v2.1.300)**: `api_request` 이벤트에 `cache_creation_5m_tokens`/`cache_creation_1h_tokens`가 추가되고, 스팬에 `gen_ai.provider.name` 같은 GenAI 시맨틱 컨벤션 속성이 포함됩니다.

> **OTEL 텔레메트리 — `tool_decision` 속성(v2.1.301)**: `tool_decision` 이벤트에 `classifier_verdict`와 `permission_mode`가 추가됩니다.

**요약 동작 제어:**

```bash
/recap                                 # manually trigger a recap
/config                                # toggle auto-recap on/off
```

또는 환경 변수로:
```bash
CLAUDE_CODE_ENABLE_AWAY_SUMMARY=0 claude   # disable recap
CLAUDE_CODE_ENABLE_AWAY_SUMMARY=1 claude   # force enable recap
```

---

## 세션 간 메시징

> **v2.1.224에 추가**, v2.1.239까지 확장. **macOS, Linux, 그리고 v2.1.239부터 Windows**에서 사용할 수 있습니다.

세션은 원래 섬과 같았습니다. 세션 간 메시징을 사용하면 한 Claude Code 세션이 다른 세션과 대화할 수 있습니다 — 다른 장비의 세션과 클라우드 세션도 포함됩니다. 따라서 이미 올바른 컨텍스트가 로드된 세션에 질문을 넘길 수 있고, 다시 설명할 필요가 없습니다.

### 세션 탐색

`ListAgents`는 주소를 지정할 수 있는 모든 대상을 나열합니다: 직접 생성한 서브에이전트, 이 장비의 다른 로컬 세션, 클라우드 세션, 그리고 원격 제어가 연결되어 있을 때 다른 장비의 세션입니다. 각 행은 종류로 표시되며, v2.1.229부터는 `offline` 및 `cloud` 레이블도 함께 표시되어 도달 가능한 세션과 휴면 세션을 구분할 수 있습니다.

**각 행의 이름이 곧 주소입니다** — 그 이름으로 메시지를 보냅니다.

### 메시지 보내기

`SendMessage`는 대상과 메시지를 받습니다:

```text
SendMessage({ to: "<session name>", message: "What did you conclude about the retry logic?" })
```

v2.1.232부터는 이름만으로 충분합니다. 두 행이 실제로 같은 이름을 공유하는 경우가 아니면 구분용 ref를 덧붙일 필요가 없습니다.

### 세션이 유휴 상태가 될 때까지 대기 (`notify_when_idle`, v2.1.236)

메시지를 보내는 세션이 작업 중일 때는 폴링하기보다 언제 끝나는지 알고 싶을 때가 많습니다. `SendMessage`는 바로 그 용도로 `notify_when_idle` 입력을 받습니다:

```text
SendMessage({
  to: "auth-refactor",
  message: "ping me when the migration finishes",
  notify_when_idle: true
})
```

**옵트인이며 일회성**입니다. 대상 세션은 다음에 유휴 상태가 될 때 알림을 한 번 보내고 구독이 종료됩니다. 폴링 루프가 없고, 세션이 다시 바쁘다가 유휴해져도 알림이 반복되지 않습니다.

v2.1.239의 관련 변경 두 가지: `ListAgents`가 이제 **세션 자신의 이름**도 함께 보고하며(세션이 다른 세션에 자신의 주소를 알려줄 수 있도록) 활성 동료 목록과 나란히 표시되고, 세션 간 메시징이 **Windows**에서도 사용 가능해졌습니다.

### `@` 멘션 축약 (v2.1.232)

도구를 명시적으로 호출하는 대신, 프롬프트에서 세션을 직접 `@` 멘션하여 도달할 수 있습니다:

```text
@auth-refactor did the migration tests pass?
```

### 도착 메시지 제어: `crossSessionInbound`

수신 메시지는 `crossSessionInbound` 설정(v2.1.224+)으로 제어합니다:

| 값 | 동작 |
|---|---|
| `"accept"` | 수신 메시지가 이 세션의 Claude에게 전달됩니다 |
| `"hold"` | 메시지가 도착했다는 알림만 표시되고 전달되지는 않습니다 |
| `"refuse"` | 수신 메시지가 폐기됩니다 |

값은 사다리 형태이며(`accept < hold < refuse`), **프로젝트 및 로컬 설정은 사용자 범위 값보다 엄격할 때만** 적용됩니다. 프로젝트는 수신 전달을 강화할 수만 있고 완화할 수는 없습니다. v2.1.232부터 이 설정에는 `/config`의 "Messages from your other sessions" 행도 있습니다.

### 도달 범위와 제한

- 같은 장비의 로컬 세션과 클라우드 세션.
- 다른 장비의 원격 제어 세션(이름으로 주소 지정, v2.1.225).
- 클라우드 세션은 메시지를 **수신**하지만 아직 로컬 세션에 답신할 수 없습니다 — 답변은 해당 세션의 트랜스크립트에서 확인하세요.
- v2.1.224부터 macOS와 Linux, v2.1.239부터 Windows.

---

## 대화형 기능

### 키보드 단축키

Claude Code는 효율을 위해 키보드 단축키를 지원합니다. 공식 문서의 전체 목록은 다음과 같습니다:

| 단축키 | 설명 |
|----------|-------------|
| `Ctrl+C` | 현재 입력/생성 취소 |
| `Ctrl+D` | Claude Code 종료 |
| `Ctrl+G` | 외부 편집기에서 계획 편집 |
| `Ctrl+L` | 화면 다시 그리기(재페인트만 — 두 번 눌러 `/clear`하는 단축키는 v2.1.238에서 제거됨) |
| `Ctrl+O` | 상세 출력 토글(추론 보기) |
| `Ctrl+R` | 기록 역방향 검색. 기본값은 **모든 프로젝트의 모든 프롬프트**(v2.1.129+)이며, 선택기 안에서 `Ctrl+S`를 눌러 현재 프로젝트로 좁힐 수 있습니다. 이전 버전은 프로젝트 한정이 기본이었습니다. |
| `Ctrl+T` | 작업 목록 보기 토글 |
| `Ctrl+B` | 실행 중인 작업을 백그라운드로 |
| `Esc+Esc` | 코드/대화 되감기 |
| `Shift+Tab` / `Alt+M` | 권한 모드 토글 |
| `Option+P` / `Alt+P` | 모델 전환 |
| `Option+T` / `Alt+T` | 확장 사고 토글 |
| `Option+O` / `Alt+O` | 패스트 모드 토글(`/fast`) |
| `Ctrl+X` `Ctrl+K` | 모든 백그라운드 서브에이전트 중지 |
| `Ctrl+Enter`(또는 `Ctrl+X` `Ctrl+S`) | 즉시 전송 — 대기 중인 모든 메시지를 한 번에 보냅니다. v2.1.281부터 턴이 취소되는 대신 실행 중인 도구와 서브에이전트가 백그라운드로 이동합니다. 전송·대기 중인 메시지는 모델이 받을 때까지 회색으로 표시됩니다(v2.1.275) |
| `Ctrl+S` | 현재 프롬프트를 보관하고, 다시 누르면 복원합니다 |
| `Ctrl+_` | 프롬프트 입력에 대한 마지막 편집 실행 취소 |
| `:` | 단어 시작에서 `:`를 입력하면 이모지 단축 코드 완성이 열립니다(예: `:heart:`, v2.1.217+) |

**라인 편집(표준 readline 단축키):**

| 단축키 | 동작 |
|----------|--------|
| `Ctrl + A` | 줄 시작으로 이동 |
| `Ctrl + E` | 줄 끝으로 이동 |
| `Ctrl + K` | 줄 끝까지 잘라내기 |
| `Ctrl + U` | 줄 시작까지 잘라내기 |
| `Ctrl + W` | 단어 단위로 뒤로 삭제 |
| `Ctrl + Y` | 붙여넣기(yank) |
| `Tab` | 자동 완성 |
| `↑ / ↓` | 명령 기록 |

### 접근성

스크린 리더 모드(v2.1.208+)는 CLI를 스크린 리더용으로 설계된 평문 렌더링 모드로 전환합니다. CLI 플래그, 환경 변수, 설정 키 중 하나로 활성화하세요:

```bash
claude --ax-screen-reader
```

```bash
export CLAUDE_AX_SCREEN_READER=1
```

```json
{
  "axScreenReader": true
}
```

### 키바인딩 사용자 정의

`/keybindings`를 실행하면 편집용 `~/.claude/keybindings.json`이 열리며, 여기서 사용자 지정 키보드 단축키를 만들 수 있습니다(v2.1.18+).

**구성 형식**:

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    },
    {
      "context": "Confirmation",
      "bindings": {
        "ctrl+a": "confirmation:yes"
      }
    }
  ]
}
```

기본 단축키를 해제하려면 바인딩을 `null`로 설정하세요.

### 사용 가능한 컨텍스트

키바인딩은 특정 UI 컨텍스트에 범위가 지정됩니다:

| 컨텍스트 | 주요 액션 |
|---------|-------------|
| **Chat** | `submit`, `cancel`, `cycleMode`, `modelPicker`, `thinkingToggle`, `undo`, `externalEditor`, `stash`, `imagePaste` |
| **Confirmation** | `yes`, `no`, `previous`, `next`, `nextField`, `cycleMode`, `toggleExplanation` |
| **Global** | `interrupt`, `exit`, `toggleTodos`, `toggleTranscript` |
| **Autocomplete** | `accept`, `dismiss`, `next`, `previous` |
| **HistorySearch** | `search`, `previous`, `next` |
| **Settings** | 컨텍스트별 설정 탐색 |
| **Tabs** | 탭 전환 및 관리 |
| **Help** | 도움말 패널 탐색 |

`Transcript`, `Task`, `ThemePicker`, `Attachments`, `Footer`, `MessageSelector`, `DiffDialog`, `ModelPicker`, `Select`를 포함해 총 18개 컨텍스트가 있습니다.

### 코드(chord) 지원

키바인딩은 코드 시퀀스(다중 키 조합)를 지원합니다:

```
"ctrl+k ctrl+s"   → Two-key sequence: press ctrl+k, then ctrl+s
"ctrl+shift+p"    → Simultaneous modifier keys
```

**키 입력 문법**:
- **수정자**: `ctrl`(또는 `control`), `alt`(또는 `opt`, `option`, `meta`), `shift`, `cmd`(또는 `command`, `super`, `win`) — `cmd`는 `meta`의 별칭이 아닌 별도 수정자이며, Super 키를 보고하는 터미널에서만 감지됩니다
- **대문자는 Shift를 의미**: `K`는 `shift+k`와 같습니다
- **특수 키**: `escape`, `enter`, `return`, `tab`, `space`, `backspace`, `delete`, 화살표 키

### 예약 및 충돌 키

| 키 | 상태 | 비고 |
|-----|--------|-------|
| `Ctrl+C` | 예약됨 | 재바인딩 불가(중단) |
| `Ctrl+D` | 예약됨 | 재바인딩 불가(종료) |
| `Ctrl+B` | 터미널 충돌 | tmux 접두 키 |
| `Ctrl+A` | 터미널 충돌 | GNU Screen 접두 키 |
| `Ctrl+Z` | 터미널 충돌 | 프로세스 일시 중단 |

> **팁**: 단축키가 동작하지 않으면 터미널 에뮬레이터나 멀티플렉서와의 충돌을 확인하세요.

### 탭 완성

Claude Code는 지능형 탭 완성을 제공합니다:

```
User: /rew<TAB>
→ /rewind

User: /plu<TAB>
→ /plugin

User: /plugin <TAB>
→ /plugin install
→ /plugin enable
→ /plugin disable
```

### 명령 기록

이전 명령에 접근합니다:

```
User: <↑>  # Previous command
User: <↓>  # Next command
User: Ctrl+R  # Search history

(reverse-i-search)`test': run all tests
```

### 여러 줄 입력

`\` + Enter, Option+Enter(macOS), Shift+Enter, 또는 Ctrl+J로 새 줄을 시작하세요. `\end` 종료자는 없으며, Enter를 눌러 전송합니다:

```bash
User: Long complex prompt \
spanning multiple lines
```

**예시:**

```
User: Implement a user authentication system \
with the following requirements: \
- JWT tokens \
- Email verification \
- Password reset \
- 2FA support

Claude: [Processes the multi-line request]
```

### 인라인 편집

보내기 전에 명령을 편집합니다:

```
User: Deploy to prodcution<Backspace><Backspace>uction

[Edit in-place before sending]
```

### Vim 모드

텍스트 편집을 위한 Vi/Vim 키바인딩을 활성화합니다:

**활성화**:
- `/config`에서 토글("Editor / Vim mode")하거나 `~/.claude/settings.json`의 `editorMode: "vim"`으로 활성화합니다. 독립 실행 `/vim` 슬래시 커맨드는 제거되었으며([이슈 #43370](https://github.com/anthropics/claude-code/issues/43370) 참고), 이제 vim 모드는 구성으로 제어합니다.
- 모드 전환은 `Esc`로 NORMAL, `i/a/o`로 INSERT, `v`로 VISUAL, `V`로 VISUAL-LINE(v2.1.118+)

**탐색 키**:
- `h` / `l` - 왼쪽/오른쪽 이동
- `j` / `k` - 아래/위 이동
- `w` / `b` / `e` - 단어 단위 이동
- `0` / `$` - 줄 시작/끝으로 이동
- `gg` / `G` - 텍스트 시작/끝으로 이동
- `%` - 짝이 맞는 괄호로 이동. `d`, `c`, `y`와 조합 가능(v2.1.301)

**텍스트 객체**:
- `iw` / `aw` - 단어 내부/주변
- `i"` / `a"` - 따옴표 문자열 내부/주변
- `i(` / `a(` - 괄호 내부/주변

**비주얼 모드(v2.1.118+)**:

| 키 | 모드 | 동작 |
|-----|------|----------|
| `v` | Visual | 문자 단위 선택과 시각적 피드백, 이동 키로 확장 |
| `V` | Visual-line | 줄 단위 선택, 항상 전체 줄을 선택 |
| `y` | Yank | 현재 비주얼 선택 복사 |
| `d` / `x` | Delete | 현재 비주얼 선택 삭제 |
| `c` | Change | 선택을 삭제하고 INSERT 모드로 진입 |
| `Esc` | Exit | NORMAL 모드로 복귀 |

비주얼 선택은 입력 필드에 강조 표시되므로, 연산자를 확정하기 전에 무엇이 복사·삭제·변경될지 정확히 확인할 수 있습니다.

### Bash 모드

`!` 접두사로 셸 명령을 직접 실행합니다:

```bash
! npm test
! git status
! cat src/index.js
```

컨텍스트를 전환하지 않고 명령을 빠르게 실행할 때 사용하세요.

**v2.1.193부터:** bash 모드(`!`)에 실시간 파일 경로 자동 완성이 있어, 프롬프트를 벗어나지 않고 셸 명령을 입력하면서 경로가 완성됩니다.

**v2.1.186부터:** `!` 명령의 출력이 자동으로 Claude에게 전달되고 Claude가 이에 응답합니다. 출력을 컨텍스트에만 추가하고 응답하지 않는 이전 동작을 유지하려면 `settings.json`에서 `"respondToBashCommands": false`를 설정하세요.

---

## 출력 스타일

출력 스타일은 Claude가 **어떻게** 응답하는지를 바꾸며, 아는 내용을 바꾸지는 않습니다. 시스템 프롬프트를 수정하여 역할, 어조, 기본 응답 형식을 설정합니다. 매 턴 같은 말투를 다시 요구하게 될 때, 또는 Claude가 소프트웨어 엔지니어가 아닌 다른 역할을 하길 원할 때 사용하세요.

프로젝트나 코드베이스에 관한 지침은 대신 [CLAUDE.md](../02-memory/)를 사용하세요. 그것은 트레이드오프가 다른 별개의 메커니즘입니다.

### 내장 스타일

| 스타일 | 동작 |
|-------|----------|
| **Default** | 소프트웨어 엔지니어링 작업을 효율적으로 완수하도록 조정된 표준 시스템 프롬프트 |
| **Proactive** | Claude가 일상적 결정을 위해 멈추지 않고 즉시 실행하며 합리적 가정을 합니다. 오토 모드보다 강한 자율 실행 지침이지만, 권한 모드를 **바꾸지는 않으므로** 여전히 권한 프롬프트가 표시됩니다 |
| **Explanatory** | 단계 사이에 교육적인 "Insights"를 추가하여 구현 선택과 코드베이스 패턴을 설명합니다 |
| **Learning** | 함께 해보며 배우는 협업형입니다. Claude가 인사이트를 공유하고 *또한* `TODO(human)` 마커를 남겨, 작고 전략적인 부분을 직접 구현하게 합니다 |
| **Concise**(v2.1.237) | Claude가 결과부터 제시하고 서두와 설명을 생략합니다. 철저함은 그대로이며 답변을 감싸는 틀만 제거됩니다. `/config` → Output style에서 선택하거나 `"outputStyle": "Concise"`로 설정하세요 |

### 스타일 선택

`/config`를 실행해 **Output style**을 선택하거나, `/output-style <style>`로 직접 전환하세요. 인수 없이 실행하면 사용 가능한 스타일 목록과 현재 스타일 표시가 나옵니다. 어느 쪽이든 선택은 `.claude/settings.local.json`에 저장됩니다. 메뉴 없이 설정하려면 설정을 직접 편집하세요:

```json
{
  "outputStyle": "Explanatory"
}
```

> **참고**: 독립 실행 `/output-style` 명령은 v2.1.73에서 사용 중단되고 v2.1.91에서 제거되었지만, **v2.1.269에서 다시 돌아왔고** v2.1.278에서 동작합니다. 헤드리스 및 원격 제어 세션에서도 동작합니다. `/config`와 `outputStyle` 설정도 여전히 유효합니다.

출력 스타일은 시스템 프롬프트의 일부이며 Claude Code가 세션 시작 시 한 번 읽으므로, 변경 사항은 `/clear` 후 또는 새 세션에서 적용됩니다.

### 사용자 지정 출력 스타일

사용자 지정 스타일은 프론트매터가 있는 Markdown 파일이며, 세 가지 수준 중 하나에 저장합니다:

- 사용자: `~/.claude/output-styles/`
- 프로젝트: `.claude/output-styles/`
- 관리 정책: 관리형 설정 디렉터리 내부의 `.claude/output-styles/`

프로젝트 스타일은 작업 디렉터리와 저장소 루트 사이의 모든 `.claude/output-styles/`에서 로드됩니다. v2.1.178부터 중첩된 디렉터리가 같은 스타일 이름을 정의하면 작업 디렉터리에 가장 가까운 것이 우선합니다.

```markdown
---
name: Diagrams first
description: Lead every explanation with a diagram
keep-coding-instructions: true
---

When explaining code, architecture, or data flow, start with a Mermaid diagram
showing the structure, then explain in prose.
```

| 프론트매터 | 용도 | 기본값 |
|-------------|---------|---------|
| `name` | 파일명과 다른 경우의 스타일 이름 | 파일명에서 상속 |
| `description` | `/config` 선택기에 표시 | 없음 |
| `keep-coding-instructions` | Claude Code의 내장 소프트웨어 엔지니어링 지침 유지 | `false` |
| `force-for-plugin` | 플러그인 스타일 전용: 플러그인이 활성화되면 사용자의 `outputStyle`을 재정의하고 자동 적용 | `false` |

Claude의 소통 방식을 바꾸면서 코딩 방식은 그대로 두려면 **`keep-coding-instructions: true`를 설정**하세요. Claude가 소프트웨어 엔지니어링을 전혀 하지 않는 경우 — 글쓰기 보조나 데이터 분석가 — 라면 생략하세요.

### 범위와 비용

출력 스타일은 **주 대화에만** 적용됩니다. 서브에이전트는 자체 시스템 프롬프트로 실행되므로 스타일이 서브에이전트의 응답 방식을 바꾸지 않습니다. 단, 포크는 부모의 전체 시스템 프롬프트를 상속하므로 예외입니다.

지침을 추가하면 입력 토큰이 늘어나지만, 첫 요청 이후에는 프롬프트 캐싱이 대부분을 흡수합니다. Explanatory와 Learning은 설계상 더 긴 응답을 생성하므로 출력 토큰이 증가합니다.

### 비교

| 기능 | 동작 방식 | 사용 시점 |
|---------|--------------|-------------|
| 출력 스타일 | 시스템 프롬프트를 수정합니다 | 매 턴 다른 역할, 어조, 형식을 원할 때 |
| [CLAUDE.md](../02-memory/) | 시스템 프롬프트 뒤에 사용자 메시지를 추가합니다 | Claude가 항상 프로젝트 관례를 알아야 할 때 |
| `--append-system-prompt` | 아무것도 제거하지 않고 시스템 프롬프트에 덧붙입니다 | 단일 호출을 위한 일회성 추가 |
| [서브에이전트](../04-subagents/) | 자체 시스템 프롬프트, 모델, 도구로 실행됩니다 | 별도로 범위가 지정된 도우미를 원할 때 |
| [스킬](../03-skills/) | 호출 시 작업별 지침을 로드합니다 | 재사용 가능한 워크플로가 있을 때 |

---

## 상태 표시줄

상태 표시줄은 출력이 세션 하단에 렌더링되는 사용자 지정 명령입니다. `/statusline`으로 구성하거나 직접 설정하세요:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh",
    "padding": 0
  }
}
```

`padding`의 기본값은 `0`입니다. Claude Code가 stdin으로 JSON 객체를 명령에 전달하므로, 표시할 내용은 스크립트가 결정합니다.

### 사용 가능한 입력 필드

| 그룹 | 필드 |
|-------|--------|
| 세션 | `session_id`, `session_name`, `prompt_id`, `transcript_path`, `cwd`, `version` |
| 모델 | `model.id`, `output_style.name`, `effort.level`, `fast_mode`, `thinking.enabled` |
| 에이전트 | `agent.name`, `vim.mode` |
| 비용 | `cost.total_cost_usd`, `cost.total_duration_ms`, `cost.total_api_duration_ms`, `cost.total_lines_added` |
| 컨텍스트 | `context_window.context_window_size`, `.current_usage`, `.remaining_percentage`, `.total_input_tokens`, `.used_percentage` |
| 한도 | `rate_limits.five_hour.used_percentage`, `.resets_at` |
| 저장소 | `pr.number`, `pr.review_state`, `workspace.project_dir`, `workspace.added_dirs`, `workspace.git_worktree`, `workspace.repo.host` |
| 워크트리 | `worktree.name`, `.branch`, `.path`, `.original_branch`, `.original_cwd` |

### 예시

```bash
#!/bin/bash
# ~/.claude/statusline.sh — model, context usage, and cost
input=$(cat)
model=$(echo "$input" | jq -r '.model.id')
used=$(echo "$input" | jq -r '.context_window.used_percentage')
cost=$(echo "$input" | jq -r '.cost.total_cost_usd')
printf '%s | ctx %.0f%% | $%.2f' "$model" "$used" "$cost"
```

> **참고**: `statusLine`은 워크스페이스 신뢰가 필요합니다. 상태 표시줄 스크립트는 출력을 터미널 크기에 맞출 수 있도록 환경에 `COLUMNS`와 `LINES`도 받습니다(v2.1.153+).

---

## TUI 모드 (전체 화면)

> **v2.1.110의 신규 기능**

TUI(텍스트 사용자 인터페이스) 모드는 Claude Code를 깜빡임 없는 전체 화면으로 렌더링하며, tmux나 iTerm2 분할 창 같은 터미널 멀티플렉서에 적합합니다.

### TUI 모드 활성화

`/tui` 명령으로 렌더러를 전환하거나, 실행 전에 `CLAUDE_CODE_NO_FLICKER=1`을 설정하세요:

```bash
/tui fullscreen               # switch to fullscreen from within a session
/tui default                  # switch back to the classic renderer
CLAUDE_CODE_NO_FLICKER=1 claude  # start directly in fullscreen
```

### 구성

| 설정 | 설명 | 기본값 |
|---------|-------------|---------|
| `autoScrollEnabled` | 최신 메시지로 자동 스크롤 | `true` |

`/config` 또는 `settings.json`으로 자동 스크롤을 끕니다:

```json
{
  "autoScrollEnabled": false
}
```

### 포커스 뷰

`/focus` 명령은 가장 관련 있는 출력만 보여주는 방해 없는 화면인 포커스 뷰를 토글합니다. 이제 `Ctrl+O`는 일반 트랜스크립트와 상세 트랜스크립트 사이만 전환합니다(포커스 뷰는 `/focus`).

---

## 음성 받아쓰기

음성 받아쓰기는 Claude Code에 누르고 말하기 방식의 음성 입력을 제공하여, 프롬프트를 타이핑하는 대신 말할 수 있게 합니다.

### 음성 받아쓰기 활성화

```
/voice
```

### 기능

| 기능 | 설명 |
|---------|-------------|
| **누르고 말하기** | 키를 누르고 있는 동안 녹음하고, 놓으면 전송합니다 |
| **20개 언어** | 음성-텍스트 변환이 20개 언어를 지원합니다 |
| **사용자 지정 키바인딩** | `/keybindings`로 누르고 말하기 키를 구성합니다 |
| **계정 요구 사항** | STT 처리를 위해 Claude.ai 계정이 필요합니다 |

### 구성

키바인딩 파일(`/keybindings`)에서 누르고 말하기 키바인딩을 사용자 정의하세요. 음성 받아쓰기는 음성-텍스트 처리에 사용자의 Claude.ai 계정을 사용합니다.

---

## 채널

채널은 MCP 서버를 통해 외부 서비스의 이벤트를 실행 중인 Claude Code 세션으로 밀어 넣는 Research Preview 기능입니다. 소스로는 Telegram, Discord, iMessage, 임의의 웹훅이 있으며, Claude가 폴링 없이 실시간 알림에 반응할 수 있습니다.

> **인증(v2.1.128+)**: `--channels`는 이제 Pro/Max OAuth **및** API 키(콘솔) 인증 모두에서 동작합니다. 이전 릴리스에서는 OAuth가 필요했습니다.

### 채널 구독

```bash
# Subscribe to a channel plugin at startup
claude --channels plugin:telegram@claude-plugins-official

# Subscribe to multiple sources (space-separated)
claude --channels plugin:discord@claude-plugins-official plugin:telegram@claude-plugins-official
```

### 지원 통합

| 통합 | 설명 |
|-------------|-------------|
| **Discord** | 세션에서 Discord 메시지를 받고 응답합니다 |
| **Telegram** | 세션에서 Telegram 메시지를 받고 응답합니다 |
| **iMessage** | 세션에서 iMessage 알림을 받습니다 |
| **Webhooks** | 임의의 웹훅 소스에서 이벤트를 받습니다 |

### 구성

채널은 시작 시 `--channels` 플래그로 구성합니다. 엔터프라이즈 배포에서는 관리형 설정으로 허용할 채널 플러그인을 제어하세요:

```json
{
  "channelsEnabled": true,
  "allowedChannelPlugins": [
    { "marketplace": "claude-plugins-official", "plugin": "discord" },
    { "marketplace": "claude-plugins-official", "plugin": "telegram" }
  ]
}
```

`allowedChannelPlugins` 관리형 설정은 조직 전체에서 허용할 채널 플러그인을 제어합니다. Anthropic이 유지 관리하는 허용 목록을 대체하며 `channelsEnabled: true`가 필요합니다.

### 동작 방식

1. MCP 서버가 외부 서비스에 연결하는 채널 플러그인 역할을 합니다
2. 수신 메시지와 이벤트가 활성 Claude Code 세션으로 밀려 들어옵니다
3. Claude가 세션 컨텍스트 안에서 메시지를 읽고 응답할 수 있습니다
4. 채널 플러그인은 Anthropic이 유지 관리하는 허용 목록에 있거나, 관리자가 설정한 조직의 `allowedChannelPlugins` 목록에 있어야 합니다
5. 폴링이 필요 없습니다 — 이벤트가 실시간으로 푸시됩니다

---

## Chrome 통합

Chrome 통합은 Claude Code를 Chrome 또는 Microsoft Edge 브라우저에 연결하여 실시간 웹 자동화와 디버깅을 제공합니다. v2.0.73+부터 제공되는 베타 기능입니다(Claude in Chrome 확장 v1.0.36+ 필요).

### Chrome 통합 활성화

**시작 시**:

```bash
claude --chrome      # Enable Chrome connection
claude --no-chrome   # Disable Chrome connection
```

**세션 내에서**:

```
/chrome
```

"Enabled by default"를 선택하면 이후 모든 세션에서 Chrome 통합이 활성화됩니다. Claude Code는 브라우저의 로그인 상태를 공유하므로 인증된 웹 앱과 상호작용할 수 있습니다.

> **참고**: v2.1.290부터 프로젝트 설정 파일로는 Chrome 통합을 켤 수 없습니다 — `--chrome`, `/chrome`, 또는 사용자 설정을 사용하세요.

### 기능

| 기능 | 설명 |
|------------|-------------|
| **실시간 디버깅** | 콘솔 로그를 읽고, DOM 요소를 검사하고, JavaScript를 실시간으로 디버깅합니다 |
| **디자인 검증** | 렌더링된 페이지를 디자인 목업과 비교합니다 |
| **폼 검증** | 폼 제출, 입력 검증, 오류 처리를 테스트합니다 |
| **웹 앱 테스트** | 인증된 앱(Gmail, Google Docs, Notion 등)과 상호작용합니다 |
| **데이터 추출** | 웹 페이지의 내용을 스크레이핑하여 처리합니다 |
| **세션 녹화** | 브라우저 상호작용을 GIF 파일로 녹화합니다 |

### 사이트 수준 권한

Chrome 확장은 사이트별 접근을 관리합니다. 확장 팝업에서 언제든 특정 사이트의 접근을 허용하거나 철회하세요. Claude Code는 명시적으로 허용한 사이트와만 상호작용합니다.

### 동작 방식

Claude Code는 보이는 창에서 브라우저를 제어하므로 동작을 실시간으로 지켜볼 수 있습니다. 브라우저가 로그인 페이지나 CAPTCHA를 만나면 Claude는 일시 정지하고 사용자가 직접 처리할 때까지 기다린 후 계속합니다.

### 알려진 제한

- **브라우저 지원**: Chrome과 Edge. Claude Code는 Brave, Arc, Vivaldi, Opera 같은 다른 Chromium 기반 브라우저에서도 연결됩니다
- **WSL**: Windows Subsystem for Linux에서는 사용할 수 없습니다
- **서드파티 공급자**: Bedrock, Vertex, Foundry API 공급자에서는 지원되지 않습니다
- **서비스 워커 유휴**: 장시간 세션에서 Chrome 확장의 서비스 워커가 유휴 상태가 될 수 있습니다

> **팁**: Chrome 통합은 베타 기능입니다. 브라우저 지원은 향후 릴리스에서 확대될 수 있습니다.

---

## 원격 제어

원격 제어를 사용하면 휴대폰, 태블릿, 또는 아무 브라우저에서 로컬로 실행 중인 Claude Code 세션을 이어갈 수 있습니다. 로컬 세션은 계속 사용자의 장비에서 실행되며 클라우드로 이동하지 않습니다. Pro, Max, Team, Enterprise 플랜에서 사용할 수 있습니다(v2.1.51+).

원격 제어는 **더 이상 리서치 프리뷰가 아닙니다** — 2026년 34주차에 해당 레이블이 제거되었습니다. 이제 `claude remote-control`을 실행 중인 모든 장비가 Claude 앱 Code 탭에 **장치 카드**로 나타나므로, 장비에서 세션을 먼저 시작한 뒤 연결하지 않고도 휴대폰에서 바로 해당 장비의 세션을 시작할 수 있습니다.

### 원격 제어 시작

**CLI에서**:

```bash
# Start with default session name
claude remote-control

# Start with a custom name
claude remote-control --name "Auth Refactor"
```

**세션 내부에서**:

```
/remote-control
/remote-control "Auth Refactor"
```

**사용 가능한 플래그**:

| 플래그 | 설명 |
|------|-------------|
| `--name "title"` | 쉽게 식별할 수 있는 사용자 지정 세션 제목 |
| `--verbose` | 상세 연결 로그 표시 |

> **참고(v2.1.300)**: `claude remote-control`은 더 이상 `--sandbox`나 `--no-sandbox`를 받지 않습니다(효과가 없었으며, 이제 둘 중 하나를 전달하면 오류로 종료됩니다). 원격 제어 세션을 샌드박스로 실행하려면 설정 파일에서 `sandbox.enabled`를 지정하세요.

### 세션에 연결

다른 장치에서 연결하는 세 가지 방법:

1. **세션 URL** — 세션 시작 시 터미널에 출력되며, 아무 브라우저에서나 열 수 있습니다
2. **QR 코드** — 시작 후 `spacebar`를 누르면 스캔 가능한 QR 코드가 표시됩니다
3. **이름으로 찾기** — claude.ai/code 또는 Claude 모바일 앱(iOS/Android)에서 세션을 찾아봅니다

### 보안

- 사용자 장비에 **인바운드 포트를 열지 않습니다**
- TLS를 통한 **아웃바운드 HTTPS만** 사용합니다
- **범위가 제한된 자격 증명** — 수명이 짧고 범위가 좁은 여러 토큰을 사용합니다
- **세션 격리** — 각 원격 세션은 독립적입니다

### 원격 제어 vs 웹의 Claude Code

| 항목 | 원격 제어 | 웹의 Claude Code |
|--------|---------------|-------------------|
| **실행 위치** | 사용자의 장비에서 실행 | Anthropic 클라우드에서 실행 |
| **로컬 도구** | 로컬 MCP 서버, 파일, CLI에 완전 접근 | 로컬 의존성 없음 |
| **사용 사례** | 다른 장치에서 로컬 작업 이어가기 | 아무 브라우저에서 새로 시작 |

### 제한 사항

- 대화형 Claude Code 프로세스당 원격 세션 하나 — 서버 모드(`claude remote-control`)는 여러 세션을 동시에 제공합니다(`--capacity`, 기본값 32)
- 호스트 장비에서 터미널을 열어 두어야 합니다
- 네트워크에 도달할 수 없으면 서버 모드는 약 10분 후 종료되고, 대화형 세션은 계속 재시도하다가 네트워크가 돌아오면 재연결합니다

### 사용 사례

- 자리를 비운 동안 모바일 장치나 태블릿에서 Claude Code를 제어합니다
- 로컬 도구 실행을 유지하면서 더 풍부한 claude.ai UI를 사용합니다
- 완전한 로컬 개발 환경으로 이동 중에 빠르게 코드를 리뷰합니다

### 푸시 알림 (v2.1.110)

원격 제어가 활성 상태이고 `/config`에서 "Push when Claude decides"가 활성화되어 있으면, Claude가 휴대폰으로 모바일 푸시 알림을 보낼 수 있습니다. 예를 들어 긴 작업이 완료되거나 사용자 입력이 필요할 때입니다.

활성화 방법:
1. 원격 제어 활성화: `/remote-control` 또는 `claude --rc`
2. `/config`를 열고 **Push when Claude decides** 활성화

푸시 알림에는 Claude 구독과 Claude 모바일 앱이 필요합니다.

### Remote Control 비활성화 (`disableRemoteControl`, v2.1.128+)

Team 또는 Enterprise 플랜의 관리자는 `disableRemoteControl` 설정으로 원격 제어를 완전히 차단할 수 있습니다. `true`이면 `claude remote-control`과 `/remote-control` 모두 시작을 거부합니다.

```json
{
  "disableRemoteControl": true
}
```

이 설정은 **관리/정책** 범위(예: macOS의 `/Library/Application Support/ClaudeCode/managed-settings.json`)에서 적용되므로 개별 사용자가 재정의할 수 없습니다. 로컬 전용 실행을 조직 전체에 강제해야 할 때 유용합니다.

> **API 키 티어에 의해 원격 제어가 자동 비활성화될 때(v2.1.139)**: 다음 중 하나라도 설정되어 있으면 claude.ai로 동시에 로그인되어 있어도 원격 제어가 **조용히 비활성화**됩니다:
>
> - `ANTHROPIC_API_KEY`
> - `ANTHROPIC_AUTH_TOKEN`
> - `apiKeyHelper`(settings.json)
>
> 같은 조건에서 [`/schedule`](#예약된-작업), claude.ai MCP 커넥터, 알림 환경설정도 비활성화됩니다 — claude.ai로 연결되는 네 가지 기능 모두 OAuth 로그인이 활성 자격 증명일 것을 요구합니다. 이 기능들을 사용하려면 API 키를 해제하거나 Pro/Max OAuth 티어로 실행하세요.

---

## 웹 세션

웹 세션을 사용하면 claude.ai/code에서 브라우저로 Claude Code를 직접 실행하거나 CLI에서 웹 세션을 만들 수 있습니다.

### 웹 세션 생성

```bash
# Create a new web session from the CLI
claude --remote "implement the new API endpoints"
```

이렇게 하면 claude.ai에 Claude Code 세션이 시작되고 아무 브라우저에서나 접근할 수 있습니다.

### 웹 세션을 로컬에서 재개

웹에서 세션을 시작했는데 로컬에서 이어가고 싶다면:

```bash
# Resume a web session in the local terminal — opens a picker of your web sessions
claude --teleport
```

또는 대화형 REPL 안에서:

```text
/teleport
```

`/tp`는 `/teleport`의 별칭입니다. 둘 다 claude.ai 구독이 필요합니다. 클라우드 세션은 로컬에서 계속하는 방법을 설명하는 `/teleport` 힌트를 표시합니다(v2.1.223).

> **체인지로그 기반**: v2.1.223 체인지로그에는 알려진 세션으로 바로 이동하는 인수 형태
> `claude --teleport <session id>`가 나옵니다. CLI 레퍼런스에는 선택기 형태만
> 문서화되어 있으므로, 세션 ID를 이미 가지고 있지 않다면 `claude --teleport`를 사용하세요.

### 사용 사례

- 한 장비에서 작업을 시작하고 다른 장비에서 이어갑니다
- 팀원과 세션 URL을 공유합니다
- 웹 UI로 시각적 diff를 검토한 뒤 터미널로 전환하여 실행합니다

---

## 데스크톱 앱

Claude Code 데스크톱 앱은 시각적 diff 검토, 병렬 세션, 통합 커넥터를 갖춘 독립 실행 애플리케이션을 제공합니다. macOS와 Windows에서 사용할 수 있습니다(Pro, Max, Team, Enterprise 플랜).

### 설치

[claude.ai](https://claude.ai)에서 플랫폼에 맞는 버전을 내려받으세요:
- **macOS**: 유니버설 빌드(Apple Silicon 및 Intel)
- **Windows**: x64 및 ARM64 설치 파일 제공

설정 방법은 [데스크톱 빠른 시작](https://code.claude.com/docs/en/desktop-quickstart)을 참고하세요.

### CLI에서 핸드오프

현재 CLI 세션을 데스크톱 앱으로 옮깁니다:

```
/desktop
```

### 핵심 기능

| 기능 | 설명 |
|---------|-------------|
| **Diff 보기** | 인라인 코멘트가 있는 파일별 시각적 검토. Claude가 코멘트를 읽고 수정합니다 |
| **앱 미리보기** | 내장 브라우저와 함께 개발 서버를 자동으로 시작하여 실시간 검증 |
| **PR 모니터링** | GitHub CLI 통합으로 CI 실패 자동 수정 및 검사 통과 시 자동 병합 |
| **병렬 세션** | 사이드바의 여러 세션과 자동 Git 워크트리 격리 |
| **예약 작업** | 앱이 열려 있는 동안 실행되는 반복 작업(매시간, 매일, 평일, 매주) |
| **풍부한 렌더링** | 구문 강조가 있는 코드, 마크다운, 다이어그램 렌더링. GitHub Flavored Markdown 작업 목록 체크박스(`- [ ]` / `- [x]`)가 체크박스로 렌더링됩니다(v2.1.149+) |

### 앱 미리보기 구성

`.claude/launch.json`에서 개발 서버 동작을 구성합니다:

```json
{
  "version": "0.0.1",
  "configurations": [
    {
      "name": "my-app",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run", "dev"],
      "port": 3000
    }
  ]
}
```

### 커넥터

더 풍부한 컨텍스트를 위해 외부 서비스를 연결합니다:

| 커넥터 | 기능 |
|-----------|------------|
| **GitHub** | PR 모니터링, 이슈 추적, 코드 리뷰 |
| **Slack** | 알림, 채널 컨텍스트 |
| **Linear** | 이슈 추적, 스프린트 관리 |
| **Notion** | 문서, 지식 베이스 접근 |
| **Asana** | 작업 관리, 프로젝트 추적 |
| **Calendar** | 일정 인식, 회의 컨텍스트 |

> **참고**: 커넥터는 원격(클라우드) 세션에서는 사용할 수 없습니다.

### 원격 및 SSH 세션

- **원격 세션**: Anthropic 클라우드 인프라에서 실행되며 앱을 닫아도 계속됩니다. claude.ai/code 또는 Claude 모바일 앱에서 접근할 수 있습니다
- **SSH 세션**: SSH로 원격 장비에 연결하여 원격 파일시스템과 도구에 완전히 접근합니다. 원격 장비에 Claude Code가 설치되어 있어야 합니다

### 데스크톱의 권한 모드

데스크톱 앱은 CLI와 동일한 권한 모드를 지원합니다:

| 모드 | 동작 |
|------|----------|
| **Manual**(기본) | 모든 편집과 명령을 검토하고 승인합니다 |
| **Accept edits** | 파일 편집은 자동 승인되고 명령은 수동 승인이 필요합니다 |
| **Plan** | 변경이 이루어지기 전에 접근 방식을 검토합니다 |
| **Auto** | 일상적 프롬프트 없이 실행되며, 백그라운드 분류기가 먼저 작업을 검사합니다 |
| **Bypass permissions** | 자동 실행(샌드박스 전용, 관리자 제어) |

### 엔터프라이즈 기능

- **관리 콘솔**: 조직의 Code 탭 접근과 권한 설정을 제어합니다
- **MDM 배포**: macOS에서는 MDM, Windows에서는 MSIX로 배포합니다
- **SSO 통합**: 조직 구성원에게 싱글 사인온을 요구합니다
- **관리형 설정**: 팀 구성과 모델 가용성을 중앙에서 관리합니다

---

## 작업 목록

작업 목록 기능은 컨텍스트 압축(컨텍스트 창에 맞추기 위해 대화 기록이 잘리는 것)을 넘어 지속되는 작업 추적을 제공합니다.

### 작업 목록 토글

세션 중에 `Ctrl+T`를 눌러 작업 목록 보기를 켜거나 끕니다.

### 지속되는 작업

작업은 컨텍스트 압축을 넘어 지속되므로, 대화 컨텍스트가 잘려도 장기 실행 작업 항목이 유실되지 않습니다. 복잡한 다단계 구현에서 특히 유용합니다.

### 이름이 지정된 작업 디렉터리

`CLAUDE_CODE_TASK_LIST_ID` 환경 변수를 사용하면 세션 간에 공유되는 이름이 지정된 작업 디렉터리를 만들 수 있습니다:

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

이를 통해 여러 세션이 같은 작업 목록을 공유할 수 있으므로 팀 워크플로나 다중 세션 프로젝트에 유용합니다.

---

## 프롬프트 제안

프롬프트 제안은 git 기록과 현재 대화 컨텍스트를 바탕으로 회색으로 표시된 예시 명령을 보여줍니다.

### 동작 방식

- 제안은 입력 프롬프트 아래에 회색 텍스트로 표시됩니다
- `Tab`을 눌러 제안을 수락합니다
- `Enter`를 눌러 수락하고 즉시 전송합니다
- 제안은 컨텍스트를 인식하며 git 기록과 대화 상태에서 가져옵니다

### 프롬프트 제안 비활성화

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git 워크트리

Git 워크트리를 사용하면 격리된 워크트리에서 Claude Code를 시작할 수 있어, 스태시하거나 브랜치를 전환하지 않고도 여러 브랜치에서 병렬로 작업할 수 있습니다.

### 워크트리에서 시작

```bash
# Start Claude Code in an isolated worktree
claude --worktree
# or
claude -w
```

### 워크트리 위치

워크트리는 다음 위치에 생성됩니다:
```
<repo>/.claude/worktrees/<name>
```

### 모노레포용 스파스 체크아웃

`worktree.sparsePaths` 설정을 사용하면 모노레포에서 스파스 체크아웃을 수행하여 디스크 사용량과 클론 시간을 줄일 수 있습니다:

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### 기준 브랜치 참조 (`worktree.baseRef`)

**`worktree.baseRef`**(v2.1.133 추가) — `claude --worktree`가 `origin/<default>`에서 분기할지 로컬 `HEAD`에서 분기할지 제어합니다.

- `"fresh"`(기본값) — 로컬의 푸시되지 않은 커밋을 무시하고 `origin/<default-branch>`에서 분기합니다. **이것은 v2.1.128에서 도입된 동작을 되돌리는 것**이므로, v2.1.128 이후 로컬 HEAD 분기에 의존했던 사용자는 다시 옵트인해야 합니다.
- `"head"` — 푸시되지 않은 커밋을 보존하며 로컬 `HEAD`에서 분기합니다.

`~/.claude/settings.json`에 설정합니다:

```json
{ "worktree": { "baseRef": "head" } }
```

### 백그라운드 세션 격리 (`worktree.bgIsolation`)

**`worktree.bgIsolation`**(v2.1.143 추가) — 백그라운드 세션(`/bg`, `claude --bg`, Agent View 등)이 자체 워크트리를 가질지, 아니면 포그라운드 작업 복사본을 직접 편집할지 제어합니다.

- *(기본값)* — 백그라운드 세션은 `--worktree`와 같은 방식으로 `<repo>/.claude/worktrees/` 아래에 격리된 워크트리를 만듭니다.
- `"none"` — 백그라운드 세션이 현재 작업 복사본을 직접 편집합니다. 워크트리가 비현실적일 때(예: 무거운 네이티브 빌드 산출물) 또는 백그라운드 에이전트가 포그라운드 세션과 편집을 조율해야 할 때 사용하세요.

```json
{ "worktree": { "bgIsolation": "none" } }
```

트레이드오프: `"none"`은 워크트리 격리라는 안전망을 제거하므로, 백그라운드 세션과 포그라운드 세션의 동시 편집이 실제 작업 복사본에서 병합 충돌을 일으킬 수 있습니다.

### 워크트리 도구 및 훅

| 항목 | 설명 |
|------|-------------|
| `EnterWorktree` | 워크트리로 진입하는 도구. v2.1.157부터 세션 중간에 Claude가 관리하는 워크트리 사이를 전환할 수 있습니다 |
| `ExitWorktree` | 현재 워크트리를 나가고 정리하는 도구 |
| `WorktreeCreate` | 워크트리가 생성될 때 발생하는 훅 이벤트 |
| `WorktreeRemove` | 워크트리가 제거될 때 발생하는 훅 이벤트 |

v2.1.157부터 Claude가 관리하는 워크트리는 에이전트가 끝나면 잠금이 해제되어 `git worktree remove`/`prune`으로 정리할 수 있습니다.

### 자동 정리

워크트리에서 변경이 없으면 세션이 끝날 때 자동으로 정리됩니다.

### 사용 사례

- main 브랜치를 그대로 두고 기능 브랜치에서 작업합니다
- 작업 디렉터리에 영향을 주지 않고 격리된 환경에서 테스트를 실행합니다
- 일회용 환경에서 실험적 변경을 시도합니다
- 모노레포에서 특정 패키지만 스파스 체크아웃하여 시작 속도를 높입니다

---

## 샌드박싱

샌드박싱은 Claude Code가 실행하는 Bash 명령에 OS 수준의 파일시스템·네트워크 격리를 제공합니다. 권한 규칙을 보완하며 추가 보안 계층을 제공합니다.

### 샌드박싱 활성화

**슬래시 커맨드**(선택 사항을 이 프로젝트의 `.claude/settings.local.json`에 저장):
```text
/sandbox
```

**설정 파일**(모든 프로젝트): `~/.claude/settings.json`에 `"sandbox": { "enabled": true }`를 설정합니다.

**세션 단위**로, 설정 파일을 쓰지 않고:
```bash
claude --settings '{"sandbox": {"enabled": true}}'
```

> `claude --sandbox` / `--no-sandbox` 플래그는 없습니다. v2.1.300부터 `claude remote-control`에 이들을 전달하면 오류로 종료됩니다.

### 구성 설정

| 설정 | 설명 |
|---------|-------------|
| `sandbox.enabled` | 샌드박싱 활성화 또는 비활성화 |
| `sandbox.failIfUnavailable` | 샌드박싱을 활성화할 수 없으면 실패 |
| `sandbox.filesystem.allowWrite` | 쓰기가 허용된 경로 |
| `sandbox.filesystem.allowRead` | 읽기가 허용된 경로 |
| `sandbox.filesystem.denyRead` | 읽기가 거부된 경로 |
| `sandbox.network.allowedDomains` | Bash로 실행된 프로세스가 접근할 수 있는 도메인(`*.` 와일드카드 지원) |
| `sandbox.network.deniedDomains` | `allowedDomains` 와일드카드가 허용하더라도 차단할 도메인(v2.1.113+) |
| `sandbox.network.strictAllowlist` | (v2.1.219) 샌드박스 명령에 대해 허용 목록에 없는 호스트를 프롬프트 없이 거부 |
| `sandbox.enableWeakerNetworkIsolation` | macOS에서 더 약한 네트워크 격리 활성화 |
| `sandbox.bwrapPath` | (v2.1.133+, Linux/WSL) `bubblewrap` 바이너리 경로. 기본값: `$PATH` 탐색. |
| `sandbox.socatPath` | (v2.1.133+, Linux/WSL) `socat` 바이너리 경로. 기본값: `$PATH` 탐색. |
| `sandbox.credentials` | (v2.1.187+) 샌드박스 명령이 자격 증명 파일과 비밀 환경 변수를 읽지 못하도록 차단. |
| `sandbox.allowAppleEvents` | (v2.1.181+, macOS) 샌드박스 명령이 Apple 이벤트를 보내도록 옵트인. |
| `sandbox.filesystem.disabled` | (v2.1.216+) 네트워크 격리는 유지하면서 파일시스템 격리를 완전히 건너뜀 — 파일 샌드박싱이 도구를 깨뜨리지만 네트워크 이그레스 제어는 유지해야 할 때 유용합니다. 사용자 설정, 관리형 설정, `--settings`에서만 적용되며 프로젝트 설정으로는 지정할 수 없습니다. |

**Linux/WSL 바이너리 경로**(v2.1.133+) — 비표준 설치 위치를 Claude Code에 알려 줍니다:

```json
{
  "sandbox": {
    "bwrapPath": "/opt/bubblewrap/bin/bwrap",
    "socatPath": "/opt/socat/bin/socat"
  }
}
```

넓은 와일드카드를 `deniedDomains`가 재정의하는 예(v2.1.113+):

```json
{
  "sandbox": {
    "network": {
      "allowedDomains": ["*.example.com"],
      "deniedDomains": ["evil.example.com"]
    }
  }
}
```

와일드카드는 `example.com`의 모든 호스트를 통과시키지만, `deniedDomains`는 특정 이름의 호스트를 여전히 차단합니다.

> **참고**(v2.1.243): 샌드박스 Bash 도구의 권한 프롬프트가 **더 이상 허용된 네트워크 호스트를 나열하지 않습니다**. Claude가 요청을 그대로 시도하고, 새 호스트가 나올 때마다 사용자가 승인합니다. 따라서 프롬프트에 허용 목록이 미리 표시될 것이라 기대하지 마세요. 같은 릴리스에서는 차단된 명령이 우연히 종료 코드 `0`으로 끝날 때 네트워크 위반 세부 정보를 누락하던 문제도 수정되어, 성공처럼 조용해 보이는 경우에도 무엇이 차단되었는지 보고됩니다.

### 자격 증명 마스킹 (v2.1.221, v2.1.224)

> **체인지로그 기반**: 이 `sandbox.credentials` 옵션들은 v2.1.221 및
> v2.1.224 체인지로그 항목에서 가져온 것이며, 설정 레퍼런스에는 아직 상세히 설명되어 있지 않습니다.

v2.1.221 이전에는 `sandbox.credentials`가 자격 증명 파일을 `deny`만 할 수 있었고, 자격 증명이 필요한 샌드박스 명령은 그냥 실패했습니다. `mode: "mask"`는 비밀을 노출하지 않고 명령이 계속 동작하도록 합니다. 샌드박스 프로세스는 파일의 **센티널** 사본을 읽고, 샌드박스 프록시가 네트워크로 나가는 경로에서 실제 값으로 대체합니다.

```json
{
  "sandbox": {
    "network": { "tlsTerminate": true },
    "credentials": {
      "files": [
        { "path": "~/.aws/credentials", "mode": "mask" }
      ]
    }
  }
}
```

| 기능 | 도입 | 동작 |
|---|---|---|
| 자격 증명 **파일**에 대한 `mode: "mask"` | v2.1.221 | 샌드박스 명령은 센티널을 읽고, 프록시가 이그레스 시 실제 값으로 교체합니다. **Linux 및 WSL 전용** — macOS에서는 파일 마스킹이 `deny`로 폴백됩니다. |
| `extract` / `onExtractNoMatch` | v2.1.224 | 변수 전체가 아니라 구조화된 환경 값 내부의 한 필드만 마스킹하고, 패턴이 일치하지 않을 때의 동작을 결정합니다. |
| `maskClaims`와 함께 쓰는 `decode: "jwt"` | v2.1.224 | JWT를 디코드하여 지정한 클레임만 마스킹하고 나머지는 읽을 수 있게 둡니다. |
| `awsPairs` / `sigv4` | v2.1.224 | 실제 액세스 키를 대체한 뒤 프록시에서 AWS SigV4 요청을 다시 서명합니다. |

**놓치기 쉬운 두 가지 제약:**

- 모든 마스킹에는 `network.tlsTerminate`가 필요합니다. 프록시가 요청 내부를 봐야 값을
  대체할 수 있기 때문입니다.
- 이 옵션들은 사용자 설정, 관리형 설정, `--settings`에서만 적용됩니다.
  프로젝트 설정으로는 마스킹을 켜거나 마스킹 대상을 변경할 수 없습니다.

### 구성 예시

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    }
  }
}
```

### 동작 방식

- Bash 명령은 파일시스템 접근이 제한된 샌드박스 환경에서 실행됩니다
- 의도치 않은 외부 연결을 막기 위해 네트워크 접근을 격리할 수 있습니다
- 심층 방어를 위해 권한 규칙과 함께 동작합니다
- macOS에서 Seatbelt는 샌드박스 프록시로 가는 연결을 제외한 모든 네트워크 연결을 차단합니다. `sandbox.enableWeakerNetworkIsolation`은 이 격리를 **약화**시키며, MITM `httpProxyPort` 프록시 뒤에 있는 Go CLI 같은 도구에만 사용해야 합니다

### 사용 사례

- 신뢰할 수 없거나 생성된 코드를 안전하게 실행합니다
- 프로젝트 외부 파일의 우발적 수정을 방지합니다
- 자동화 작업 중 네트워크 접근을 제한합니다

---

## 관리형 설정 (엔터프라이즈)

관리형 설정을 사용하면 엔터프라이즈 관리자가 플랫폼 고유의 관리 도구로 조직 전체에 Claude Code 구성을 배포할 수 있습니다.

### 배포 방법

| 플랫폼 | 방법 | 도입 |
|----------|--------|-------|
| macOS | 관리형 plist 파일(MDM) | v2.1.51+ |
| Windows | Windows 레지스트리 | v2.1.51+ |
| 크로스 플랫폼 | 관리형 구성 파일 | v2.1.51+ |
| 크로스 플랫폼 | 관리형 드롭인(`managed-settings.d/` 디렉터리) | v2.1.83+ |

### 관리형 드롭인

v2.1.83부터 관리자는 여러 관리형 설정 파일을 `managed-settings.d/` 디렉터리에 배포할 수 있습니다. 파일은 알파벳 순서로 병합되므로 팀별로 모듈식 구성이 가능합니다. 이 디렉터리는 시스템 디렉터리(macOS의 `/Library/Application Support/ClaudeCode/`, Linux의 `/etc/claude-code/`, Windows의 `C:\Program Files\ClaudeCode\`)에서 `managed-settings.json` 옆에 위치합니다:

```
/etc/claude-code/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### 사용 가능한 관리형 설정

| 설정 | 설명 |
|---------|-------------|
| `permissions.disableBypassPermissionsMode` | `"disable"`로 설정하면 사용자가 바이패스 권한을 활성화하지 못합니다 |
| `availableModels` | 사용자가 선택할 수 있는 모델 제한 |
| `enforceAvailableModels` | (v2.1.175) `true`이면 `availableModels` 허용 목록이 **Default** 모델도 제약합니다 — 구성된 기본값이 목록에 없으면 Claude Code가 허용된 첫 모델로 폴백합니다. 사용자 및 프로젝트 설정으로는 관리형 `availableModels` 목록을 더 넓힐 수 없습니다. |
| `allowedChannelPlugins` | 허용할 채널 플러그인 제어 |
| `autoMode.environment` | 오토 모드용 신뢰 인프라 구성 |
| `workflowSizeGuideline` | (v2.1.219) 권고용 [동적 워크플로 크기 가이드라인](#동적-워크플로) 설정. 관리형 설정뿐 아니라 모든 설정 파일에서 읽을 수 있으며, 이 값이 설정되어 있으면 `/config`에서 **Dynamic workflow size** 행이 숨겨집니다 |
| `wslInheritsWindowsSettings` | Windows/WSL 전용(v2.1.118+): `true`이면 WSL 안에서 실행되는 Claude Code가 Windows 호스트의 관리형 설정을 상속하므로, 레지스트리/MDM으로 배포한 엔터프라이즈 정책이 Windows와 WSL 셸에 일관되게 적용됩니다 |
| `parentSettingsBehavior` | (v2.1.133+, 관리자 계층) SDK의 `managedSettings`가 부모 프로세스 설정과 병합되는 방식을 제어합니다. `"first-wins"`는 기존 우선순위를 유지하고(충돌 시 앞선 설정이 우선), `"merge"`는 값을 깊은 병합합니다. |
| 사용자 지정 정책 | 조직별 권한 및 도구 정책 |

### 예시: macOS Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>permissions</key>
  <dict>
    <key>disableBypassPermissionsMode</key>
    <string>disable</string>
  </dict>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

## 구성 및 설정

### 구성 파일 위치

1. **사용자 설정**: `~/.claude/settings.json`
2. **프로젝트 설정**: `.claude/settings.json`(체크인됨)
3. **로컬 프로젝트 설정**: `.claude/settings.local.json`(체크인되지 않음)
4. **관리형 설정**: 시스템 디렉터리의 `managed-settings.json`([관리형 설정](#관리형-설정-엔터프라이즈) 참고)

### 전체 구성 예시

**핵심 고급 기능 구성**(`.claude/settings.json`):

```json
{
  "permissions": {
    "defaultMode": "manual"
  },
  "hooks": {
    "PreToolUse": [
      { "matcher": "Edit", "hooks": [{ "type": "command", "command": "~/.claude/hooks/eslint-fix.sh" }] }
    ],
    "PostToolUse": [
      { "matcher": "Write", "hooks": [{ "type": "command", "command": "~/.claude/hooks/security-scan.sh" }] }
    ]
  }
}
```

훅 스크립트는 stdin으로 도구 입력을 JSON으로 받습니다(예: `tool_input.file_path`). `${file_path}` 치환은 없습니다. MCP 서버는 설정 키가 아니며, 프로젝트 루트의 `.mcp.json`에 정의합니다:

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": { "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}" }
    }
  }
}
```

**확장 구성 예시:**

```json
{
  "permissions": {
    "defaultMode": "manual",
    "allow": ["Bash(git log:*)", "Read"],
    "deny": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": [{ "type": "command", "command": "~/.claude/hooks/eslint-fix.sh" }] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": [{ "type": "command", "command": "~/.claude/hooks/security-scan.sh" }] }],
    "Stop": [{ "hooks": [{ "type": "command", "command": "~/.claude/hooks/notify.sh" }] }]
  }
}
```

이 구성의 GitHub MCP 서버는 위와 같이 `.mcp.json`에 넣습니다.

### 사용자별 추가 설정

이 키들은 `~/.claude/settings.json`(또는 프로젝트의 `.claude/settings.json`)에 넣어 개별 사용자의 대화형 동작을 제어합니다:

| 설정 | 설명 |
|---------|-------------|
| `askUserQuestionTimeout` | 응답이 없는 `AskUserQuestion` 대화상자를 유휴 시간 후 자동으로 계속합니다. **v2.1.200**부터 대화상자는 기본으로 자동 계속되지 않으므로, 시간 제한 자동 계속을 다시 사용하려면 이 값을 설정하세요. |
| `enableArtifact` | 사용자별 Artifact 도구 활성화/비활성화(v2.1.196). |
| `crossSessionInbound` | (v2.1.224) 수신 [세션 간 메시지](#세션-간-메시징) 처리 방식 — `"accept"`, `"hold"`, `"refuse"`. 프로젝트 및 로컬 값은 `accept < hold < refuse` 사다리에서 *더 엄격할 때만* 적용됩니다. v2.1.232부터 `/config`에 "Messages from your other sessions"로 표시됩니다. |
| `dialogExpiry` | (v2.1.224) 응답이 없는 대화상자가 열려 있는 시간. 기본값 `"5m"`이며 `"60s"`, `"5m"`, `"10m"`, `"never"`를 허용합니다. `CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS`가 우선합니다. v2.1.232부터 `/config`에 "Dialog expiry"로 표시됩니다. |
| `modelPicker` | (v2.1.243) `/model` 선택기에 나열할 모델을 원하는 순서와 레이블로 선택합니다. 설정 계층 간에 **병합이 아니라 교체**되는 몇 안 되는 설정 중 하나로, 가장 가까운 범위의 값이 그대로 우선합니다. |
| `promptCacheTtl` | (v2.1.243) 주 대화의 프롬프트 캐시 수명을 선택합니다. |
| `subagentPromptCacheTtl` | (v2.1.243) 서브에이전트와 주 대화 외 요청에 대한 동일한 선택. |
| `modelPricing` | (v2.1.243) **관리형 설정.** 조직의 계약 요율을 제공하여 `/cost`, 상태 표시줄, 텔레메트리가 정가 대신 해당 요율을 보고하게 합니다. |
| `keybindingFlavor` | **v2.1.261부터 사용 중단되었으며 효과가 없습니다.** 프롬프트의 단어 편집 키는 Bash와 마찬가지로 항상 readline 관례를 따릅니다. `Ctrl+W`는 공백까지 삭제하고, `Alt+F`와 `Alt+D`는 단어 끝에서 멈추며, 구두점이 단어를 구분합니다. Claude Code가 여전히 이 키를 허용하므로 이 값을 설정한 설정 파일은 유효하게 유지됩니다. (v2.1.238–v2.1.260에서는 `"classic"`과 `"readline"` 중 하나를 선택했습니다.) |
| `spellcheck` | (v2.1.235) `PATH`에 있는 `aspell`, `hunspell`, `ispell` 중 하나를 해당 순서로 사용하여 프롬프트 입력의 철자가 틀린 단어에 밑줄을 표시합니다. 객체 값이며(`{"enabled": true, "language": "en_GB"}`) 기본값은 꺼짐입니다. **사용자 설정, `--settings` 플래그, 관리형 설정에서만 읽습니다**: 프로젝트의 `.claude/settings.json`이나 `.claude/settings.local.json`에 있는 `spellcheck` 블록은 무시됩니다. |
| `bashOutputMaxChars` | (v2.1.261) **성공한** Bash 또는 PowerShell 명령 출력 중 Claude가 인라인으로 받는 문자 수(최대 128K). 한도를 넘으면 Claude Code가 출력을 파일로 저장하고 Claude는 짧은 미리보기와 경로를 받습니다. 이 값을 설정하면 Claude Code가 `BASH_MAX_OUTPUT_LENGTH`를 무시합니다. |
| `taskOutputMaxChars` | (v2.1.261) **v2.1.278에서 대체되었으며 효과가 없습니다.** 이전에는 `TaskOutput` 도구로 읽을 때 Claude가 인라인으로 받는 **백그라운드 작업** 출력의 문자 수를 제한했습니다. v2.1.278에서 `TaskOutput` 도구가 제거되어 Claude가 이제 `Read`로 백그라운드 작업의 출력 파일을 읽으므로, 이 키와 `TASK_MAX_OUTPUT_LENGTH`는 모두 무효입니다. Claude Code가 여전히 키를 허용하므로 이 값을 설정한 설정 파일은 유효하게 유지됩니다. |
| `maxEffortLevel` | (v2.1.267) Bedrock, Vertex, Foundry를 포함한 모든 공급자에서 Claude Code가 사용할 수 있는 노력 수준을 제한합니다. 최상위 또는 `modelSettings` 아래 모델별로 설정할 수 있습니다. 사용자는 여전히 더 낮은 수준을 선택할 수 있습니다. |
| `bashEditDiffEnabled` | (v2.1.269) Bash 도구 결과에 명령이 변경한 파일의 diff가 포함됩니다. |
| `syncClaudeAiSkills` / `syncClaudeAiPlugins` | (v2.1.275) claude.ai 계정에서 활성화한 스킬이나 플러그인을 터미널 세션으로 동기화하지 않으려면 둘 중 하나를 `false`로 설정합니다. |

### 폴백 모델 (`fallbackModel`)

`fallbackModel` 설정을 사용하면 기본 모델이 과부하되었거나 사용할 수 없을 때 순서대로 시도할 폴백 모델을 **최대 세 개**까지 구성할 수 있습니다.

```json
{
  "fallbackModel": ["claude-opus-4-8", "claude-sonnet-4-6", "claude-haiku-4-5"]
}
```

**v2.1.166**부터 `--fallback-model` 플래그가 헤드리스뿐 아니라 대화형 세션에도 적용됩니다. 폴백 시 Claude Code는 예상치 못한 재시도 불가 오류를 한 번 재시도하며, 인증, 속도 제한, 요청 크기, 전송 오류는 여전히 즉시 실패합니다.

### 환경 변수

환경 변수로 구성을 재정의합니다:

```bash
# Model selection
export ANTHROPIC_MODEL=claude-opus-4-8
export ANTHROPIC_DEFAULT_MODEL=claude-opus-4-8   # (v2.1.236) Model new sessions start on. Unlike ANTHROPIC_MODEL, a /model pick still overrides it — and that pick persists across restarts
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-8
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# API configuration
export ANTHROPIC_API_KEY=sk-ant-...

# Thinking configuration
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high   # low, medium, high, xhigh (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7), or max — default is high on Opus 5 and Opus 4.8 (supported on Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6)

# Feature toggles
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1    # Disable auto memory (no auto memory files are created or loaded)
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=0          # Task tools are the default; 0 reverts to the legacy TodoWrite tool
export CLAUDE_CODE_SIMPLE=true              # Set by --bare flag

# MCP configuration
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# Prompt caching
export ENABLE_PROMPT_CACHING_1H=1      # Request 1-hour cache TTL for all requests (default: 1h for the main conversation on a subscription, 5 min on API key / cloud providers)

# Task management
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Agent teams (experimental)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Subagent and plugin configuration
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=1

# Subprocess and streaming
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000

# Output and package manager (v2.1.129+)
export CLAUDE_CODE_FORCE_SYNC_OUTPUT=1                      # Force synchronous output for terminals where auto-detect misses (Emacs eat, etc.)
export CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1            # Enable background upgrades for Homebrew/WinGet installs
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1         # Opt in to /v1/models gateway discovery when ANTHROPIC_BASE_URL is set

# Windows PowerShell tool (v2.1.143+) — default-on for Bedrock/Vertex/Foundry on Windows
export CLAUDE_CODE_USE_POWERSHELL_TOOL=0                    # Disable the PowerShell tool entirely
export CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1    # Honor system ExecutionPolicy instead of `-ExecutionPolicy Bypass`

# Workload identity federation (v2.1.141+)
export ANTHROPIC_WORKSPACE_ID=ws_abc123                     # Scope the federated token to a specific workspace when the rule covers multiple

# Stop hook safety cap (v2.1.143+)
export CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=8                    # Max consecutive Stop-hook blocks before the session ends with a warning. Set 0 to disable the cap.

# Session-wide spawn caps (v2.1.212)
export CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION=200         # Cap on WebSearch tool calls per session, to stop runaway search loops. Default 200.
export CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR=100       # (v2.1.290) Refill rate for that budget, in calls/hour. Default 100 interactive, 0 (no refill) with -p.

# Accessibility (v2.1.208)
export CLAUDE_AX_SCREEN_READER=1                            # Enable plain-text screen reader rendering mode. Same effect as --ax-screen-reader or "axScreenReader": true in settings.

# Newer variables (v2.1.221–v2.1.234) — changelog-sourced; the CLI reference has no env-var section
export CLAUDE_CODE_ENABLE_TODO_TOOLS=1                      # (v2.1.233) Restore the todo/task-tracking tools (TaskCreate/Get/Update/List, TodoWrite), which are available by default only on Claude 3.x models, Opus 4 through 4.7, Sonnet 4 through 4.6, and Haiku 4.5 (v2.1.268)
export CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS=900000             # (v2.1.233) WebFetch URL cache TTL. Default 15 minutes.
export CLAUDE_CODE_TOOL_MEMORY_LIMIT=2G                     # (v2.1.233, Linux) Opt-in memory cgroup applied to Bash commands
export ANTHROPIC_BEDROCK_REGION_PREFIX=us                   # (v2.1.224) Prefer a specific Bedrock cross-region inference profile
export CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT=1  # (v2.1.223) Restore pre-v2.1.223 auto-compact behavior on unrecognized model IDs
export CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS=0             # (v2.1.229) Disable prefix staggering on dynamic-workflow fan-out
export CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS=300000            # (v2.1.224) Overrides the dialogExpiry setting
export CLAUDE_CODE_PROJECT_DIR_NAME=my-app                  # (v2.1.234) Short name for the per-project transcript directory, for hosts that give each session its own config directory
export CLAUDE_CODE_GOAL_CHECKIN_MINUTES=30                  # (v2.1.234) Minutes a background task may stall before Claude checks in while a /goal is active. Set 0 to disable check-ins.

# Newer variables (v2.1.268-v2.1.278) - changelog-sourced
export CLAUDE_CODE_MCP_STARTUP_WAIT_MS=5000                 # (v2.1.274) How long the first non-interactive turn waits for MCP servers that are still connecting. 0 = do not wait, except for servers named by --allowedTools or an mcp_tool hook (still up to 2s, v2.1.284+).
export CLAUDE_CODE_WEBFETCH_DEADLINE_MS=300000              # (v2.1.268) Overrides WebFetch's new 300-second deadline. 0 disables the deadline.
export CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS=32        # (v2.1.269) Raises the Workflow tool's per-run concurrent agent limit. Accepts 1-256.
export CLAUDE_CODE_AUTO_MODE_SERVER=0                       # (v2.1.278; direct Anthropic API since v2.1.281) Opt out of server-side auto-mode classifier review

# Newer variables (v2.1.299-v2.1.300)
export CLAUDE_CODE_DISABLE_FILE_MENTIONS=1                  # (v2.1.299) Don't expand @ file/directory mentions; Claude gets the paths and reads them with its file tools. Ignored in project/local settings.
export CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS=200000           # (v2.1.299, needs v2.1.290+) Context size at which idle compaction applies. Default 200000, minimum 100000. "idleCompaction": false turns it off.
export CLAUDE_CODE_GZIP_REQUEST_BODIES=0                    # (v2.1.300) Turn off gzip of large request bodies to api.anthropic.com (use if a TLS-inspecting proxy mishandles them).
export CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS=0                 # (v2.1.300) Edit artifact files with file tools, then publish as a separate step, instead of in-publish edits.

# Newer variables (v2.1.301-v2.1.302)
export CLAUDE_CODE_AUTO_MODE_MODEL=claude-sonnet-5-5  # client-side auto mode classifier model (v2.1.302)
export CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS=3600000  # stop waiting on far-off usage-limit resets (v2.1.301)
```

> **v2.1.223 — `CLAUDE_CODE_DISABLE_1M_CONTEXT` 확대**: 이 변수는 이제 고정된 모델 ID 목록이 아니라, 네이티브 1M 토큰 창을 가진 **모든** Claude 모델을 자동 압축을 통해 200K까지 낮춥니다.

> **v2.1.108**: `ENABLE_PROMPT_CACHING_1H=1` — 주 대화와 기타 요청에 1시간 프롬프트 캐시 TTL을 요청합니다. 이 설정이 없으면 주 대화는 Claude 구독에서 플랜 사용량 범위 내 1시간, API 키·사용 크레딧·클라우드 공급자에서는 5분을 받습니다. `FORCE_PROMPT_CACHING_5M=1`은 5분을 강제합니다. (v2.1.129에서 1시간 TTL이 조용히 5분으로 다운그레이드되던 회귀가 수정되었습니다.)

> **v2.1.129**: `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1`은 기능 자동 감지가 실패하는 터미널(예: Emacs `eat`)에 동기 출력을 강제합니다. `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1`은 Homebrew/WinGet 설치에서 백그라운드 업그레이드를 활성화합니다. 그렇지 않으면 이 설치들은 자동 업데이트되지 않습니다.

### 구성 관리 명령

```
User: /config
[Opens interactive configuration menu]
```

`/config` 명령은 다음과 같은 설정을 토글하는 대화형 메뉴를 제공합니다:
- 확장 사고 켜기/끄기
- 상세 출력
- 권한 모드
- 모델 선택
- 동적 워크플로 크기(v2.1.219) — 설정 파일에 `workflowSizeGuideline`이 설정되어 있으면 숨겨집니다. [동적 워크플로](#동적-워크플로) 참고
- 유휴 압축(v2.1.302)

대화형 메뉴에서 Enter 또는 Space로 선택한 설정을 변경하고, Esc로 저장하고 닫습니다(v2.1.183+).

메뉴를 열지 않고 프롬프트에서 직접 설정할 수도 있습니다:

```bash
/config thinking=false      # set a single setting inline (v2.1.181+)
/config --help              # list available shorthand keys (v2.1.183+)
```

`key=value` 축약은 대화형 세션, `-p`, 원격 제어에서 동작합니다.

### 프로젝트별 구성

프로젝트에 `.claude/settings.json`을 만듭니다:

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": [{ "type": "command", "command": "npm test && npm run lint" }] }]
  },
  "permissions": {
    "defaultMode": "manual"
  }
}
```

프로젝트의 MCP 서버는 프로젝트 루트의 `.mcp.json`에 넣습니다:

```json
{
  "mcpServers": {
    "project-db": {
      "command": "mcp-postgres",
      "env": {
        "DATABASE_URL": "${PROJECT_DB_URL}"
      }
    }
  }
}
```

---

## 신뢰 및 권한 범위

> **체인지로그 기반(v2.1.222, v2.1.232)**: 이 강화 조치들은 체인지로그에서 가져온 것이며,
> 설정 레퍼런스에는 아직 명시되어 있지 않습니다.

최근 릴리스의 반복되는 주제: 보안 관련 설정은 클론한 저장소로 넓힐 수 없습니다. 알아 둘 세 가지 변경이 있습니다.

**중첩 저장소는 자체 신뢰 확인이 필요합니다(v2.1.232).** 신뢰된 상위 디렉터리 안의 git 저장소는 더 이상 그 신뢰를 상속하지 않습니다. `~/work/monorepo`를 신뢰했고 그 안에 벤더링된 서브모듈이 있다면, Claude Code가 그 안에서 처음 작업할 때 서브모듈을 별도로 신뢰할 것인지 묻습니다.

**`sandbox.ripgrep`은 사용자 범위 전용입니다(v2.1.232).** 샌드박스가 사용할 ripgrep 바이너리를 지정하는 이 설정은 사용자 설정, 관리형 설정, `--settings`에서만 적용됩니다. 프로젝트 설정으로는 샌드박스가 다른 바이너리를 가리키게 할 수 없습니다.

**원격 제어 자동 시작은 사용자 범위 전용입니다(v2.1.222).** 저장소 로컬 설정으로는 원격 제어 자동 시작을 켤 수 없으며, `/config`를 통한 사용자 범위에서만 켤 수 있습니다.

기억할 패턴: 체크인된 파일이 사용자 장비에서 Claude Code가 할 수 있는 일을 확장할 수 있는 설정이라면, 이제 사용자 범위 전용이라고 가정하세요.

---

## 에이전트 팀

에이전트 팀은 여러 Claude Code 인스턴스가 하나의 작업에서 협업할 수 있게 하는 실험적 기능입니다. 기본적으로 비활성화되어 있습니다.

### 에이전트 팀 활성화

환경 변수 또는 설정으로 활성화합니다:

```bash
# Environment variable
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

또는 설정 JSON에 추가합니다:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### 에이전트 팀 동작 방식

- **팀 리드**가 전체 작업을 조정하고 하위 작업을 팀원에게 위임합니다
- **팀원**은 각자 자체 컨텍스트 창을 가지고 독립적으로 작업합니다
- **공유 작업 목록**을 통해 팀 구성원 간 자기 조정이 가능합니다
- 서브에이전트 정의(`.claude/agents/` 또는 `--agents` 플래그)로 팀원 역할과 전문화를 정의합니다

### 표시 모드

에이전트 팀은 `--teammate-mode` 플래그로 구성하는 두 가지 표시 모드를 지원합니다:

| 모드 | 설명 |
|------|-------------|
| `in-process`(기본값) | 팀원이 같은 터미널 프로세스 안에서 실행됩니다 |
| `tmux` | 팀원마다 전용 분할 창이 주어집니다(tmux 또는 iTerm2 필요) |
| `auto` | 최적의 표시 모드를 자동으로 선택합니다 |

```bash
# Use tmux split panes for teammate display
claude --teammate-mode tmux

# Explicitly use in-process mode
claude --teammate-mode in-process
```

### 사용 사례

- 서로 다른 팀원이 서로 다른 모듈을 담당하는 대규모 리팩터링
- 병렬 코드 리뷰와 구현
- 코드베이스 전반의 조율된 다중 파일 변경

> **참고**: 에이전트 팀은 실험적이며 향후 릴리스에서 변경될 수 있습니다. 전체 레퍼런스는 [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams)를 참고하세요.

---

## 모범 사례

### 플랜 모드
- ✅ 복잡한 다단계 작업에 사용하세요
- ✅ 승인 전에 계획을 검토하세요
- ✅ 필요하면 계획을 수정하세요
- ❌ 단순한 작업에는 사용하지 마세요

### 확장 사고
- ✅ 아키텍처 결정에 사용하세요
- ✅ 복잡한 문제 해결에 사용하세요
- ✅ 사고 과정을 검토하세요
- ❌ 단순한 질의에는 사용하지 마세요

### 백그라운드 작업
- ✅ 장기 실행 작업에 사용하세요
- ✅ 작업 진행 상황을 모니터링하세요
- ✅ 작업 실패를 원만하게 처리하세요
- ❌ 동시 작업을 너무 많이 시작하지 마세요

### 권한
- ✅ 코드 리뷰에는 `plan`을 사용하세요(읽기 전용)
- ✅ 대화형 개발에는 `default`를 사용하세요
- ✅ 자동화 워크플로에는 `acceptEdits`를 사용하세요
- ✅ 안전 장치가 있는 자율 작업에는 `auto`를 사용하세요
- ❌ 꼭 필요하지 않으면 `bypassPermissions`를 사용하지 마세요

### 세션
- ✅ 작업별로 별도 세션을 사용하세요
- ✅ 중요한 세션 상태를 저장하세요
- ✅ 오래된 세션을 정리하세요
- ❌ 한 세션에 무관한 작업을 섞지 마세요

---

## 추가 자료

Claude Code와 관련 기능에 대한 자세한 내용:

- [공식 대화형 모드 문서](https://code.claude.com/docs/en/interactive-mode)
- [공식 헤드리스 모드 문서](https://code.claude.com/docs/en/headless)
- [CLI 레퍼런스](https://code.claude.com/docs/en/cli-reference)
- [체크포인트 안내서](../08-checkpoints/) - 세션 관리와 되감기
- [슬래시 커맨드](../01-slash-commands/) - 명령 레퍼런스
- [메모리 안내서](../02-memory/) - 지속되는 컨텍스트
- [스킬 안내서](../03-skills/) - 자율 기능
- [서브에이전트 안내서](../04-subagents/) - 위임된 작업 실행
- [MCP 안내서](../05-mcp/) - 외부 데이터 접근
- [훅 안내서](../06-hooks/) - 이벤트 기반 자동화
- [플러그인 안내서](../07-plugins/) - 번들 확장
- [공식 예약 작업 문서](https://code.claude.com/docs/en/scheduled-tasks)
- [공식 Chrome 통합 문서](https://code.claude.com/docs/en/chrome)
- [공식 원격 제어 문서](https://code.claude.com/docs/en/remote-control)
- [공식 키바인딩 문서](https://code.claude.com/docs/en/keybindings)
- [공식 데스크톱 앱 문서](https://code.claude.com/docs/en/desktop)
- [공식 에이전트 팀 문서](https://code.claude.com/docs/en/agent-teams)

---

**마지막 업데이트**: 2026년 10월 18일
**Claude Code 버전**: 2.1.302
**출처**:
- https://code.claude.com/docs/en/output-styles
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/workflows#set-a-size-guideline
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/auto-mode-classifier-billing
- https://code.claude.com/docs/en/env-vars
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/sandboxing
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/cli-reference
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/settings.md
- https://code.claude.com/docs/en/settings-reference
- https://code.claude.com/docs/en/whats-new/2026-w34
- https://code.claude.com/docs/en/model-config#adjust-effort-level
- https://code.claude.com/docs/en/interactive-mode
- https://code.claude.com/docs/en/keybindings#modifiers
- https://code.claude.com/docs/en/model-config#extended-thinking
- https://github.com/anthropics/claude-code/releases/tag/v2.1.281
- https://github.com/anthropics/claude-code/releases/tag/v2.1.283
- https://code.claude.com/docs/en/permission-modes#critical-paths
- https://code.claude.com/docs/en/settings-reference#ultracode
- https://code.claude.com/docs/en/permission-modes#which-mode-a-session-starts-in
- https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode
- https://github.com/anthropics/claude-code/releases/tag/v2.1.284
- https://github.com/anthropics/claude-code/releases/tag/v2.1.285
- https://code.claude.com/docs/en/tools-reference
- https://code.claude.com/docs/en/chrome
- https://github.com/anthropics/claude-code/releases/tag/v2.1.288
- https://github.com/anthropics/claude-code/releases/tag/v2.1.290
- https://github.com/anthropics/claude-code/releases/tag/v2.1.293
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/changelog#2-1-299
- https://code.claude.com/docs/en/changelog#2-1-300
- https://code.claude.com/docs/en/settings-reference#sandbox-enabled
- https://code.claude.com/docs/en/prompt-caching
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/monitoring-usage
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/managed-settings
- https://code.claude.com/docs/en/channels
- https://code.claude.com/docs/en/desktop
- https://code.claude.com/docs/en/fullscreen
- https://code.claude.com/docs/en/changelog#2-1-301
- https://code.claude.com/docs/en/changelog#2-1-302
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
