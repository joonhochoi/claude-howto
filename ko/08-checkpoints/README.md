<!-- i18n-source: 08-checkpoints/README.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# 체크포인트와 되감기

체크포인트를 쓰면 대화 상태를 저장하고 Claude Code 세션의 이전 지점으로 되감을 수 있습니다. 다른 접근을 시험해 보거나, 실수를 수습하거나, 대안을 비교할 때 매우 유용합니다.

## 개요

체크포인트는 대화 상태를 저장해 이전 지점으로 되감을 수 있게 해 주므로, 안전하게 실험하고 여러 접근을 탐색할 수 있습니다. 체크포인트는 대화 상태의 스냅샷이며 다음을 포함합니다.
- 주고받은 모든 메시지
- 수행된 파일 수정
- 도구 사용 이력
- 세션 컨텍스트

다른 접근을 탐색하거나, 실수를 수습하거나, 대안을 비교할 때 체크포인트는 특히 유용합니다.

## 핵심 개념

| 개념 | 설명 |
|------|------|
| **체크포인트** | 메시지·파일·컨텍스트를 포함한 대화 상태 스냅샷 |
| **되감기(Rewind)** | 이전 체크포인트로 돌아가 이후 변경을 버리는 것 |
| **분기점** | 여러 접근을 시험해 보는 기준 체크포인트 |

## 체크포인트 접근 방법

체크포인트를 다루는 방법은 크게 두 가지입니다.

### 키보드 단축키 사용
`Esc`를 두 번 누르면(`Esc` + `Esc`) 체크포인트 인터페이스가 열리고, 저장된 체크포인트를 둘러볼 수 있습니다.

### 슬래시 커맨드 사용
빠르게 접근하려면 `/rewind` 커맨드를 씁니다(별칭: `/checkpoint`, `/undo`).

```bash
# Open rewind interface
/rewind

# Or use the alias
/checkpoint
```

## 되감기 옵션

되감을 때 다음 여섯 가지 중에서 고르게 됩니다.

1. **코드와 대화 복원** -- 해당 체크포인트로 파일과 메시지를 모두 되돌립니다.
2. **대화 복원** -- 메시지만 되감고, 현재 코드는 그대로 둡니다.
3. **코드 복원** -- 파일 변경만 되돌리고, 대화 기록은 전부 유지합니다.
4. **여기서부터 요약** -- 이 지점 이후의 대화를 AI 요약으로 압축해 컨텍스트 창 공간을 확보합니다. 선택한 지점 이전의 메시지는 그대로 남습니다. 디스크의 파일은 바뀌지 않습니다. 원본 메시지는 세션 트랜스크립트에 보존됩니다. 원하면 특정 주제에 초점을 맞추라는 지시를 함께 줄 수 있습니다.
5. **여기까지 요약** -- 반대 방향입니다. 선택한 지점 *이전*의 내용을 AI 요약으로 압축하고, 이 지점 이후의 메시지는 그대로 유지합니다. "여기서부터 요약"과 함께 쓰면 컨텍스트 창을 양방향으로 표적 압축할 수 있습니다. 디스크의 파일은 바뀌지 않고, 원본 메시지는 세션 트랜스크립트에 보존됩니다.
6. **취소** -- 취소하고 현재 상태로 돌아갑니다.

> **참고**: 대화를 복원하거나 **여기서부터 요약**을 고르면, 선택한 메시지의 원래 프롬프트가 입력 필드에 복원되어 다시 보내거나 편집할 수 있습니다. **여기까지 요약**을 고르면 입력 필드가 빈 상태로 대화 끝에 위치하게 됩니다.

> **`/clear`는 더 이상 경계가 아닙니다(v2.1.191+)**: `/rewind`는 `/clear`를 실행하기 *전*에 만들어진 체크포인트에서도 이어갈 수 있습니다. 대화를 비워도 그 이전 상태가 영구히 사라지지 않으므로, 그때의 코드나 컨텍스트가 다시 필요하면 clear 지점을 넘어 되감을 수 있습니다.

## 자동 체크포인트

Claude Code가 알아서 체크포인트를 만듭니다.

- **모든 사용자 프롬프트마다** - 입력이 있을 때마다 새 체크포인트가 생성됩니다.
- **영속적** - 체크포인트는 대화와 함께 저장되므로 세션을 이어받아도 `/rewind`가 동작합니다.
- **자동 정리** - 체크포인트는 30일 뒤 자동으로 정리됩니다.

따라서 몇 분 전부터 며칠 전까지, 대화의 어느 이전 지점으로든 되감을 수 있습니다.

## 활용 사례

| 상황 | 워크플로 |
|------|----------|
| **접근 방식 탐색** | 저장 → A 시도 → 저장 → 되감기 → B 시도 → 비교 |
| **안전한 리팩터링** | 저장 → 리팩터링 → 테스트 → 실패 시 되감기 |
| **A/B 테스트** | 저장 → 설계 A → 저장 → 되감기 → 설계 B → 비교 |
| **실수 수습** | 문제 발견 → 마지막 정상 상태로 되감기 |

## 체크포인트 사용하기

### 보기와 되감기

`Esc`를 두 번 누르거나 `/rewind`로 체크포인트 브라우저를 엽니다. 타임스탬프와 함께 사용 가능한 체크포인트 목록이 보이고, 아무 지점이나 골라 그 상태로 되감을 수 있습니다.

### 체크포인트 세부 정보

각 체크포인트는 다음을 보여 줍니다.
- 생성 시각
- 수정된 파일
- 대화의 메시지 수
- 사용된 도구

## 실전 예시

### 예시 1: 다른 접근 방식 탐색

```
User: Let's add a caching layer to the API

Claude: I'll add Redis caching to your API endpoints...
[Makes changes at checkpoint A]

User: Actually, let's try in-memory caching instead

Claude: I'll rewind to explore a different approach...
[User presses Esc+Esc and rewinds to checkpoint A]
[Implements in-memory caching at checkpoint B]

User: Now I can compare both approaches
```

### 예시 2: 실수 복구

```
User: Refactor the authentication module to use JWT

Claude: I'll refactor the authentication module...
[Makes extensive changes]

User: Wait, that broke the OAuth integration. Let's go back.

Claude: I'll help you rewind to before the refactoring...
[User presses Esc+Esc and selects the checkpoint before the refactor]

User: Let's try a more conservative approach this time
```

### 예시 3: 안전한 실험

```
User: Let's try rewriting this in a functional style
[Creates checkpoint before experiment]

Claude: [Makes experimental changes]

User: The tests are failing. Let's rewind.
[User presses Esc+Esc and rewinds to the checkpoint]

Claude: I've rewound the changes. Let's try a different approach.
```

### 예시 4: 접근 방식 분기

```
User: I want to compare two database designs
[Takes note of checkpoint - call it "Start"]

Claude: I'll create the first design...
[Implements Schema A]

User: Now let me go back and try the second approach
[User presses Esc+Esc and rewinds to "Start"]

Claude: Now I'll implement Schema B...
[Implements Schema B]

User: Great! Now I have both schemas to choose from
```

## 체크포인트 보존

Claude Code가 체크포인트를 자동으로 관리합니다.

- 사용자 프롬프트마다 자동으로 생성됩니다.
- 오래된 체크포인트는 최대 30일까지 보존됩니다.
- 저장 공간이 무한히 늘지 않도록 자동으로 정리됩니다.

## 워크플로 패턴

### 탐색을 위한 분기 전략

여러 접근을 시험할 때:

```
1. Start with initial implementation → Checkpoint A
2. Try Approach 1 → Checkpoint B
3. Rewind to Checkpoint A
4. Try Approach 2 → Checkpoint C
5. Compare results from B and C
6. Choose best approach and continue
```

### 안전한 리팩터링 패턴

큰 변경을 할 때:

```
1. Current state → Checkpoint (auto)
2. Start refactoring
3. Run tests
4. If tests pass → Continue working
5. If tests fail → Rewind and try different approach
```

## 모범 사례

체크포인트는 자동으로 만들어지므로 수동으로 상태를 저장할 걱정 없이 작업에 집중할 수 있습니다. 다만 다음 습관은 지키세요.

### 체크포인트를 효과적으로 쓰기

✅ **권장:**
- 되감기 전에 사용 가능한 체크포인트를 확인합니다.
- 다른 방향을 시험해 보고 싶을 때 되감기를 사용합니다.
- 서로 다른 접근을 비교하려고 체크포인트를 남겨 둡니다.
- 되감기 옵션이 각각 무엇을 하는지 이해합니다(코드와 대화 복원, 대화 복원, 코드 복원, 요약).

❌ **비권장:**
- 코드 보존을 체크포인트에만 의존합니다.
- 외부 파일 시스템 변경까지 체크포인트가 추적한다고 기대합니다.
- 체크포인트를 git 커밋의 대체물로 사용합니다.

## 설정

체크포인트는 Claude Code의 기본 동작이라 켜기 위한 설정이 필요 없습니다. 사용자 프롬프트마다 체크포인트가 자동으로 만들어집니다.

체크포인트 동작을 좌우하는 설정은 두 가지입니다. 스냅샷을 만들지 여부, 그리고 얼마나 오래 보관할지입니다.

```json
{
  "fileCheckpointingEnabled": true,
  "cleanupPeriodDays": 30
}
```

| 설정 | 기본값 | 효과 |
|------|--------|------|
| `fileCheckpointingEnabled` | `true` | 편집 전에 파일을 스냅샷해 `/rewind`로 복원할 수 있게 합니다. v2.1.119+ 필요. `/config`에 **Rewind code (checkpoints)** 로 표시됩니다. 환경변수 대응: `CLAUDE_CODE_DISABLE_FILE_CHECKPOINTING` |
| `cleanupPeriodDays` | `30` | 세션 이력과 체크포인트를 보관하는 일수 |

Claude Code는 **최근 체크포인트 100개**까지 스냅샷을 유지하며, 그보다 오래된 것은 보관 기간 안이어도 버려집니다.

> **v2.1.117 업데이트**: `cleanupPeriodDays`는 이제 체크포인트뿐 아니라 여러 디스크 캐시의 보관 기간도 좌우합니다(아래는 일부이며, 세션 트랜스크립트, `file-history/`, `plans/`, `debug/`, `paste-cache/` 등도 포함됩니다).
>
> - 세션 체크포인트
> - `~/.claude/tasks/` — 영속 작업 목록
> - `~/.claude/shell-snapshots/` — 셸 환경 스냅샷
> - `~/.claude/backups/` — `~/.claude.json`의 이전 버전(최신 5개 유지)
>
> 이제 설정 하나로 이 디렉터리들이 같은 일수 뒤에 일괄 정리됩니다.

## 한계

체크포인트에는 다음 한계가 있습니다.

- **Bash 명령 변경은 추적하지 않음** - 파일 시스템에 대한 `rm`, `mv`, `cp` 같은 작업은 체크포인트에 담기지 않습니다.
- **외부 변경은 추적하지 않음** - Claude Code 밖(에디터·터미널 등)에서 일어난 변경은 담기지 않습니다.
- **버전 관리의 대체물이 아님** - 영구적이고 감사 가능한 변경은 git을 쓰세요.
- **서브에이전트의 편집은 복원하지 않음** - 서브에이전트가 편집한 파일은 추적되지 않으므로 `/rewind`는 그대로 둡니다. 예외는 포그라운드 `context: fork` 스킬이며, 그 편집은 메인 세션처럼 복원됩니다.

> **v2.1.216 업데이트**: `/rewind`는 이제 추적 경로의 심볼릭 링크나 하드 링크를 따라가 파일을 복원하거나 삭제하지 않습니다. 추적 경로가 심볼릭 링크나 하드 링크를 통해 해석되면 링크를 따라가지 않고 건너뛰며, 이 이유로 건너뛴 경로 수를 보고합니다.

## 문제 해결

### 체크포인트가 없음

**증상**: 기대한 체크포인트가 보이지 않음

**해결**:
- 체크포인트가 지워졌는지 확인합니다.
- 디스크 공간을 확인합니다.
- `cleanupPeriodDays`가 충분히 큰지 확인합니다(기본값: 30일).

### 되감기 실패

**증상**: 체크포인트로 되감을 수 없음

**해결**:
- 커밋하지 않은 변경이 충돌하지 않는지 확인합니다.
- 체크포인트가 손상되지 않았는지 확인합니다.
- 다른 체크포인트로 되감아 봅니다.

## Git과의 통합

체크포인트는 git을 보완합니다(대체하지는 않습니다).

| 항목 | Git | 체크포인트 |
|------|-----|------------|
| 범위 | 파일 시스템 | 대화 + 파일 |
| 지속성 | 영구 | 세션 기반 |
| 세밀도 | 커밋 단위 | 임의 지점 |
| 속도 | 느림 | 즉시 |
| 공유 | 가능 | 제한적 |

둘을 함께 쓰세요.
1. 빠른 실험에는 체크포인트를 씁니다.
2. 확정된 변경은 git 커밋으로 남깁니다.
3. git 작업 전에 체크포인트를 만듭니다.
4. 성공한 체크포인트 상태를 git에 커밋합니다.

## 빠른 시작 가이드

### 기본 워크플로

1. **평소처럼 작업** - Claude Code가 체크포인트를 자동으로 만듭니다.
2. **되돌아가고 싶다면** - `Esc`를 두 번 누르거나 `/rewind`를 씁니다.
3. **체크포인트 선택** - 목록에서 골라 되감습니다.
4. **복원 범위 선택** - 코드와 대화 복원, 대화 복원, 코드 복원, 여기서부터 요약, 여기까지 요약, 취소 중에서 고릅니다.
5. **작업 계속** - 그 지점으로 돌아왔습니다.

### 키보드 단축키

- **`Esc` + `Esc`** - 체크포인트 브라우저 열기
- **`/rewind`** - 체크포인트에 접근하는 또 다른 방법
- **`/checkpoint`**, **`/undo`** - `/rewind`의 별칭

## 언제 되감아야 하는가: 컨텍스트 모니터링

체크포인트로 되돌아갈 수는 있습니다. 그런데 *언제* 되감아야 하는지는 어떻게 알까요? 대화가 길어지면 Claude의 컨텍스트 창이 차고 모델 품질이 조용히 떨어집니다. 알아차리지 못한 채 절반쯤 장님 상태인 모델이 만든 코드를 커밋하고 있을 수도 있습니다.

**[cc-context-stats](https://github.com/luongnv89/cc-context-stats)** 는 Claude Code 상태 표시줄에 실시간 **컨텍스트 구역**을 더해 이 문제를 해결합니다. **Plan**(초록, 계획과 코딩에 안전)에서 **Code**(노랑, 새 계획은 피할 때)를 거쳐 **Dump**(주황, 마무리하고 되감을 때)까지, 지금 어디에 있는지 추적합니다. 구역이 바뀌는 것이 보이면 품질이 떨어진 출력으로 밀어붙이지 말고 체크포인트를 남기고 새로 시작할 때입니다.

## 관련 개념

- **[고급 기능](../09-advanced-features/)** - 플랜 모드와 그 밖의 고급 기능
- **[메모리 관리](../02-memory/)** - 대화 이력과 컨텍스트 관리
- **[슬래시 커맨드](../01-slash-commands/)** - 사용자가 직접 호출하는 단축 기능
- **[훅](../06-hooks/)** - 이벤트 기반 자동화
- **[플러그인](../07-plugins/)** - 묶음으로 배포되는 확장 패키지

## 추가 자료

- [공식 체크포인트 문서](https://code.claude.com/docs/en/checkpointing)
- [고급 기능 가이드](../09-advanced-features/) - 확장 사고(extended thinking)와 그 밖의 기능

## 요약

체크포인트는 Claude Code의 자동 기능으로, 작업을 잃을 걱정 없이 여러 접근을 안전하게 시험해 볼 수 있게 합니다. 사용자 프롬프트마다 새 체크포인트가 자동으로 만들어지므로 세션의 어느 이전 지점으로든 되감을 수 있습니다.

주요 장점:
- 여러 접근을 두려움 없이 실험할 수 있습니다.
- 실수에서 빠르게 회복합니다.
- 서로 다른 해법을 나란히 비교합니다.
- 버전 관리 시스템과 안전하게 병행합니다.

기억하세요. 체크포인트는 git의 대체물이 아닙니다. 빠른 실험은 체크포인트로, 영구적인 코드 변경은 git으로 하세요.

---

**최종 갱신**: 2026년 10월 18일
**Claude Code 버전**: 2.1.302
**출처**:
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/settings
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/claude-directory
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
