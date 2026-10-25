<!-- i18n-source: 08-checkpoints/checkpoint-examples.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

# 체크포인트 예제

Claude Code에서 체크포인트를 효과적으로 활용하는 실제 사례를 정리합니다.

참고: 체크포인트는 사용자 프롬프트마다 자동으로 생성됩니다. 직접 저장할 필요가 없습니다. 되감으려면 `Esc`를 두 번(`Esc+Esc`) 누르거나 `/rewind`로 체크포인트 브라우저를 열면 됩니다.

## 예제 1: 데이터베이스 마이그레이션

### 시나리오
MySQL에서 PostgreSQL로 마이그레이션해야 하는데, 직접 마이그레이션하는 방식과 점진적 듀얼 라이트(dual-write) 방식 두 가지를 모두 검토하려 합니다.

### 워크플로

```
User: Let's implement a direct migration from MySQL to PostgreSQL
      [Checkpoint A created automatically]

Claude: I'll implement the direct migration...
[Changes database driver, updates queries, modifies schema]

User: Run the tests
      [Checkpoint B created automatically]

Claude: Running tests...
❌ 15 tests failing - connection pool issues

User: This approach has issues. Let's try the dual-write pattern instead.
[User presses Esc+Esc, selects Checkpoint A, chooses "Restore code and conversation"]

User: Now implement a dual-write pattern where we write to both databases

Claude: I'll implement dual-write migration...
[Implements dual-write layer, gradual migration strategy]

User: Run the tests

Claude: Running tests...
✅ All tests passing

User: The dual-write approach is clearly safer. Let's commit this.
```

## 예제 2: 성능 최적화

### 시나리오
여러 가지 성능 최적화 전략을 시험해 봅니다.

### 워크플로

```
User: Let's optimize the API response time. Current: 450ms
      [Checkpoint "Baseline" created automatically]

Claude: I'll add database query caching...
[Implements Redis caching]

User: Run performance tests

Claude: Results: 280ms average response time (38% improvement)

User: Let me try a different approach.
[User presses Esc+Esc, selects "Baseline" checkpoint, chooses "Restore code and conversation"]

User: Try database query optimization instead

Claude: I'll optimize database queries...
[Adds indexes, optimizes N+1 queries]

User: Run performance tests

Claude: Results: 180ms average response time (60% improvement)

User: Let me also try a third approach.
[User presses Esc+Esc, selects "Baseline" checkpoint, chooses "Restore code and conversation"]

User: Try response compression and CDN

Claude: I'll add compression and CDN...
[Implements gzip, sets up CDN]

User: Run performance tests

Claude: Results: 320ms average response time (29% improvement)

User: Query optimization was the best. Let me go back and combine it with caching.
[User presses Esc+Esc, selects the checkpoint after query optimization, chooses "Restore code and conversation"]

User: Now add Redis caching on top of these optimized queries

Claude: [Adds Redis caching on top of optimized queries]

User: Run performance tests

Claude: Results: 95ms average response time (79% improvement) 🎉

User: Perfect! This is the winner. Let's commit this.
```

## 예제 3: UI/UX 반복 개선

### 시나리오
대시보드의 여러 레이아웃을 시험해 봅니다.

### 워크플로

```
User: Let's redesign the dashboard with a sidebar layout
      [Checkpoint "Start" created automatically]

Claude: [Implements sidebar layout]

User: Show me a screenshot

Claude: [Shows screenshot]

User: The sidebar feels cramped. Let's try a top navigation instead.
[User presses Esc+Esc, selects "Start" checkpoint, chooses "Restore code and conversation"]

User: Try a top navigation layout

Claude: [Implements top navigation]

User: Show me a screenshot

Claude: [Shows screenshot]

User: Better, but let's try a card-based grid layout
[User presses Esc+Esc, selects "Start" checkpoint, chooses "Restore code and conversation"]

User: Try a card-based grid layout

Claude: [Implements card grid]

User: Show me a screenshot

Claude: [Shows screenshot]

User: This is great! But can we combine the top nav with the card grid?
[User presses Esc+Esc, selects the checkpoint after the card grid, chooses "Restore code and conversation"]

User: Add top navigation to the card grid layout

Claude: [Adds top navigation to card grid]

User: Perfect! This is the final design.
```

## 예제 4: 디버깅 세션

### 시나리오
여러 가설을 세워 까다로운 버그를 추적합니다.

### 워크플로

```
User: There's a memory leak in the application
      [Checkpoint "Before debugging" created automatically]

Claude: Let me investigate...
[Analyzes code]

User: I think it's in the event listeners. Let's fix those.

Claude: [Fixes event listener cleanup]

User: Run memory profiler

Claude: Still leaking memory - event listeners weren't the issue

User: Let me go back and try a different hypothesis.
[User presses Esc+Esc, selects "Before debugging" checkpoint, chooses "Restore code and conversation"]

User: Maybe it's the database connections?

Claude: [Implements connection pooling fixes]

User: Run memory profiler

Claude: Still leaking - not the connections either

User: Let me go back and try another angle.
[User presses Esc+Esc, selects "Before debugging" checkpoint, chooses "Restore code and conversation"]

User: Let's check for circular references

Claude: [Finds and fixes circular references in cache]

User: Run memory profiler

Claude: ✅ Memory leak fixed! The circular references in the caching layer were the culprit.

User: Excellent! Let's commit this fix.
```

## 예제 5: API 설계 진화

### 시나리오
여러 차례 반복하며 REST API를 설계합니다.

### 워크플로

```
User: Create a REST API for our blog platform
      [Checkpoint "Before API design" created automatically]

Claude: [Creates basic CRUD API]

User: This is too simple. Let's add pagination and filtering

Claude: [Adds pagination and filtering]

User: We need better resource relationships

Claude: [Implements HATEOAS links]

User: Actually, let's try GraphQL instead of REST
[User presses Esc+Esc, selects "Before API design" checkpoint, chooses "Restore code and conversation"]

User: Implement a GraphQL API for our blog platform instead

Claude: [Implements GraphQL API]

User: I think REST is better for our use case.
[User presses Esc+Esc, selects the checkpoint after HATEOAS, chooses "Restore code and conversation"]

User: Let's finalize the REST approach.
```

## 예제 6: 구성 관리

### 시나리오
여러 구성 방식을 시험해 봅니다.

### 워크플로

```
User: Move configuration to environment variables
      [Checkpoint "Original config" created automatically]

Claude: [Implements env var configuration]

User: Test in development

Claude: Works locally but deployment issues in production

User: Let me try a different approach.
[User presses Esc+Esc, selects "Original config" checkpoint, chooses "Restore code and conversation"]

User: Try a config file approach with validation

Claude: [Implements YAML config with JSON schema validation]

User: Test in development

Claude: ✅ Works well, good validation errors

User: Can we also support env vars for sensitive values?

Claude: [Adds env var override for secrets]

User: Test deployment

Claude: ✅ All environments working correctly

User: Perfect! This is production-ready.
```

## 예제 7: 테스트 전략

### 시나리오
포괄적인 테스트를 구현합니다.

### 워크플로

```
User: Add unit tests for the auth module
      [Checkpoint created automatically]

Claude: [Adds Jest unit tests]

User: Run tests

Claude: 45 tests passing, 78% coverage

User: Add integration tests too

Claude: [Adds integration tests]

User: Run tests

Claude: 89 tests passing, 92% coverage, but tests are slow (3 minutes)

User: The tests are too slow. Let's optimize.

Claude: [Optimizes test setup, adds parallel execution]

User: Run tests

Claude: 89 tests passing, 92% coverage, 35 seconds ✅

User: Great! Now add E2E tests for critical paths

Claude: [Adds Playwright E2E tests]

User: Run all tests

Claude: 112 tests passing, 94% coverage, 2 minutes

User: Perfect balance of coverage and speed!
```

## 예제 8: 체크포인트에서 요약 사용

### 시나리오
긴 디버깅 세션을 마친 뒤, 맥락은 유지하면서 대화를 압축하고 싶을 때가 있습니다.

### 워크플로

```
User: [After 20+ messages of debugging and exploration]

[User presses Esc+Esc, selects an early checkpoint, chooses "Summarize from here"]
[Optionally provides instructions: "Focus on what we tried and what worked"]

Claude: [Generates a summary of the conversation from that point forward]
[Original messages are preserved in the transcript]
[The summary replaces the visible conversation, reducing context window usage]

User: Now let's continue with the approach that worked.
```

## 핵심 정리

1. **체크포인트는 자동입니다**: 사용자 프롬프트마다 체크포인트가 생성되므로 직접 저장할 필요가 없습니다
2. **`Esc+Esc` 또는 `/rewind`를 사용하세요**: 체크포인트 브라우저에 접근하는 두 가지 방법입니다
3. **상황에 맞는 복원 옵션을 고르세요**: 필요에 따라 코드, 대화, 둘 다 복원하거나 요약할 수 있습니다
4. **실험을 두려워하지 마세요**: 체크포인트가 있으면 과감한 변경도 안전하게 시도할 수 있습니다
5. **git과 함께 쓰세요**: 탐색에는 체크포인트를, 확정된 작업에는 git을 사용합니다
6. **긴 세션은 요약하세요**: "Summarize from here"로 대화를 관리 가능한 크기로 유지합니다

---
**최종 갱신**: 2026년 7월 29일
**Claude Code 버전**: 2.1.220
**출처**:
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/model-config
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
