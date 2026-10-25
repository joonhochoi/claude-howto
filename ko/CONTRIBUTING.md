<!-- i18n-source: CONTRIBUTING.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude How To 기여하기

이 프로젝트에 기여해 주셔서 감사합니다! 이 가이드는 효과적으로 기여하는 방법을 이해하는 데 도움이 됩니다.

## 프로젝트 소개

Claude How To는 Claude Code를 다루는 시각적이고 예제 중심의 가이드입니다. 다음을 제공합니다:
- 기능이 동작하는 방식을 설명하는 **Mermaid 다이어그램**
- 즉시 사용할 수 있는 **프로덕션급 템플릿**
- 맥락과 모범 사례를 곁들인 **실제 사례**
- 초급에서 고급까지 이어지는 **단계적 학습 경로**

## 기여 유형

### 1. 새 예제 또는 템플릿
기존 기능(슬래시 커맨드, 스킬, 훅 등)에 대한 예제를 추가합니다:
- 복사해 바로 쓸 수 있는 코드
- 동작 방식에 대한 명확한 설명
- 사용 사례와 이점
- 문제 해결 팁

### 2. 문서 개선
- 이해하기 어려운 부분을 명확하게 다듬기
- 오타와 문법 오류 수정
- 빠진 정보 추가
- 코드 예제 개선

### 3. 기능 가이드
새로운 Claude Code 기능에 대한 가이드를 작성합니다:
- 단계별 튜토리얼
- 아키텍처 다이어그램
- 흔한 패턴과 안티패턴
- 실제 워크플로

### 4. 버그 보고
직접 겪은 문제를 보고합니다:
- 기대한 동작 설명
- 실제로 일어난 일 설명
- 재현 단계 포함
- 관련 Claude Code 버전과 OS 기재

### 5. 피드백과 제안
가이드 개선을 돕습니다:
- 더 나은 설명 제안
- 다루지 못한 부분 지적
- 새 섹션이나 재구성 제안

## 시작하기

### 1. 포크와 클론
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2. 브랜치 생성
의미가 드러나는 브랜치 이름을 사용하세요:
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3. 환경 설정

pre-commit 훅은 매 커밋 전에 CI와 동일한 검사를 로컬에서 실행합니다. PR이 승인되려면 다섯 가지 검사를 모두 통과해야 합니다.

**필수 의존성:**

```bash
# Python tooling (uv is the package manager for this project)
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Markdown linter (Node.js)
npm install -g markdownlint-cli

# Mermaid diagrams render with Pele, which needs Node.js >= 20 (nothing to
# install globally). Check your version:
node --version

# Install pre-commit and activate hooks
uv pip install pre-commit
pre-commit install
```

**설정 검증:**

```bash
pre-commit run --all-files
```

첫 실행 시 Mermaid 훅을 위해 Node.js 22를 내려받고(pre-commit이 직접 준비하므로 시스템에 Node.js가 없어도 동작합니다) 고정된 Pele 번들을 `scripts/.vendor-cache/pele/`로 내려받습니다. 이후 실행은 오프라인에서도 동작합니다. Mermaid 훅은 엄격 모드로 실행되며 Pele이 실행되지 않으면 실패합니다. 첫 다운로드 전에 오프라인으로 커밋하려면 `SKIP=mermaid,vietnamese-mermaid,japanese-mermaid`로 해당 훅을 건너뛰세요.

매 커밋마다 실행되는 훅은 다음과 같습니다:

| 훅 | 검사 내용 |
|------|---------------|
| `markdown-lint` | Markdown 서식과 구조 |
| `cross-references` | 상대 링크, 앵커, 코드 펜스 |
| `mermaid-syntax` | 모든 ` ```mermaid ` 블록의 파싱 성공 여부 |
| `link-check` | 외부 URL 접근 가능 여부 |
| `build-epub` | EPUB이 오류 없이 생성되는지 (`.md` 변경 시) |

## 디렉터리 구조

```
├── 01-slash-commands/      # User-invoked shortcuts
├── 02-memory/              # Persistent context examples
├── 03-skills/              # Reusable capabilities
├── 04-subagents/           # Specialized AI assistants
├── 05-mcp/                 # Model Context Protocol examples
├── 06-hooks/               # Event-driven automation
├── 07-plugins/             # Bundled features
├── 08-checkpoints/         # Session snapshots
├── 09-advanced-features/   # Planning, thinking, backgrounds
├── 10-cli/                 # CLI reference
├── scripts/                # Build and utility scripts
└── README.md               # Main guide
```

## 예제 기여 방법

### 슬래시 커맨드 추가
1. `01-slash-commands/`에 `.md` 파일을 만드세요
2. 다음을 포함하세요:
   - 무엇을 하는지에 대한 명확한 설명
   - 사용 사례
   - 설치 방법
   - 사용 예제
   - 커스터마이징 팁
3. `01-slash-commands/README.md`를 갱신하세요

### 스킬 추가
1. `03-skills/`에 디렉터리를 만드세요
2. 다음을 포함하세요:
   - `SKILL.md` - 본문 문서
   - `scripts/` - 필요하면 보조 스크립트
   - `templates/` - 프롬프트 템플릿
   - README의 사용 예제
3. `03-skills/README.md`를 갱신하세요

### 서브에이전트 추가
1. `04-subagents/`에 `.md` 파일을 만드세요
2. 다음을 포함하세요:
   - 에이전트의 목적과 기능
   - 시스템 프롬프트 구조
   - 사용 사례 예시
   - 통합 예제
3. `04-subagents/README.md`를 갱신하세요

### MCP 설정 추가
1. `05-mcp/`에 `.json` 파일을 만드세요
2. 다음을 포함하세요:
   - 설정에 대한 설명
   - 필요한 환경 변수
   - 설정 절차
   - 사용 예제
3. `05-mcp/README.md`를 갱신하세요

### 훅 추가
1. `06-hooks/`에 `.sh` 파일을 만드세요
2. 다음을 포함하세요:
   - 셔뱅과 설명
   - 로직을 설명하는 명확한 주석
   - 오류 처리
   - 보안 고려 사항
3. `06-hooks/README.md`를 갱신하세요

## 작성 가이드

### Markdown 스타일
- 명확한 제목을 사용하세요(섹션은 H2, 하위 섹션은 H3)
- 문단은 짧고 초점을 유지하세요
- 목록에는 글머리 기호를 사용하세요
- 언어를 명시한 코드 블록을 포함하세요
- 섹션 사이에 빈 줄을 넣으세요

### 코드 예제
- 예제는 복사해 바로 쓸 수 있게 만드세요
- 직관적이지 않은 로직에는 주석을 다세요
- 단순한 버전과 고급 버전을 함께 넣으세요
- 실제 사용 사례를 보여주세요
- 잠재적 문제를 짚어 주세요

### 문서
- "무엇"뿐 아니라 "왜"를 설명하세요
- 사전 요구 사항을 포함하세요
- 문제 해결 섹션을 추가하세요
- 관련 주제로 링크하세요
- 초보자도 이해할 수 있게 유지하세요

### JSON/YAML
- 올바른 들여쓰기를 사용하세요(2칸 또는 4칸을 일관되게)
- 설정을 설명하는 주석을 추가하세요
- 검증 예제를 포함하세요

### 다이어그램
- 가능하면 Mermaid를 사용하세요
- 다이어그램은 단순하고 읽기 쉽게 유지하세요
- 다이어그램 아래에 설명을 붙이세요
- 관련 섹션으로 링크하세요

## 커밋 규칙

conventional commit 형식을 따릅니다:
```
type(scope): description

[optional body]
```

유형:
- `feat`: 새 기능 또는 예제
- `fix`: 버그 수정 또는 정정
- `docs`: 문서 변경
- `refactor`: 코드 구조 개선
- `style`: 서식 변경
- `test`: 테스트 추가 또는 변경
- `chore`: 빌드, 의존성 등

예시:
```
feat(slash-commands): Add API documentation generator
docs(memory): Improve personal preferences example
fix(README): Correct table of contents link
docs(skills): Add comprehensive code review skill
```

## 제출 전 확인

### 체크리스트
- [ ] 코드가 프로젝트 스타일과 규약을 따릅니다
- [ ] 새 예제에 명확한 문서가 포함되어 있습니다
- [ ] README 파일이 갱신되었습니다(로컬과 루트 모두)
- [ ] 민감한 정보(API 키, 자격 증명)가 없습니다
- [ ] 예제를 테스트했고 정상 동작합니다
- [ ] 링크를 확인했고 올바릅니다
- [ ] 파일 권한이 올바릅니다(스크립트는 실행 가능)
- [ ] 커밋 메시지가 명확하고 설명적입니다

### 로컬 테스트
```bash
# Run all pre-commit checks (same checks as CI)
pre-commit run --all-files

# Review your changes
git diff
```

## PR 절차

1. **명확한 설명과 함께 PR을 작성하세요**:
   - 무엇을 추가하거나 수정하는지
   - 왜 필요한지
   - 관련 이슈(있는 경우)

2. **관련 세부 정보를 포함하세요**:
   - 새 기능인가요? 사용 사례를 포함하세요
   - 문서인가요? 개선 내용을 설명하세요
   - 예제인가요? 전후 비교를 보여주세요

3. **이슈에 연결하세요**:
   - `Closes #123`을 사용하면 관련 이슈가 자동으로 닫힙니다

4. **리뷰를 기다려 주세요**:
   - 메인테이너가 개선을 제안할 수 있습니다
   - 피드백에 따라 반복해서 다듬습니다
   - 최종 결정은 메인테이너에게 있습니다

## 코드 리뷰 절차

리뷰어는 다음을 확인합니다:
- **정확성**: 설명대로 동작하는가?
- **품질**: 프로덕션에 바로 쓸 수 있는가?
- **일관성**: 프로젝트 패턴을 따르는가?
- **문서화**: 명확하고 완전한가?
- **보안**: 취약점은 없는가?

## 이슈 보고

### 버그 보고
포함할 내용:
- Claude Code 버전
- 운영체제
- 재현 단계
- 기대 동작
- 실제 동작
- 해당되는 경우 스크린샷

### 기능 요청
포함할 내용:
- 사용 사례 또는 해결하려는 문제
- 제안하는 해결책
- 검토한 대안
- 추가 맥락

### 문서 이슈
포함할 내용:
- 혼란스럽거나 빠진 부분
- 제안하는 개선안
- 예제 또는 참고 자료

## 프로젝트 정책

### 민감한 정보
- API 키, 토큰, 자격 증명을 절대 커밋하지 마세요
- 예제에는 자리표시자 값을 사용하세요
- 설정 파일용 `.env.example`을 포함하세요
- 필요한 환경 변수를 문서화하세요

### 코드 품질
- 예제는 초점을 유지하고 읽기 쉽게 만드세요
- 해결책을 과도하게 설계하지 마세요
- 직관적이지 않은 로직에는 주석을 다세요
- 제출 전에 충분히 테스트하세요

### 지적 재산
- 원본 콘텐츠의 권리는 저자에게 있습니다
- 이 프로젝트는 교육용 라이선스를 사용합니다
- 기존 저작권을 존중하세요
- 필요한 경우 출처를 명시하세요

## 도움 받기

- **질문**: GitHub Issues에서 토론을 여세요
- **일반 도움**: 기존 문서를 확인하세요
- **개발 도움**: 비슷한 예제를 참고하세요
- **코드 리뷰**: PR에서 메인테이너를 태그하세요

## 기여자 인정

기여자는 다음 위치에서 인정받습니다:
- README.md의 Contributors 섹션
- GitHub 기여자 페이지
- 커밋 이력

## 보안

예제와 문서를 기여할 때는 안전한 코딩 관행을 따르세요:

- **시크릿이나 API 키를 절대 하드코딩하지 마세요** - 환경 변수를 사용하세요
- **보안 영향을 경고하세요** - 잠재적 위험을 짚어 주세요
- **안전한 기본값을 사용하세요** - 보안 기능을 기본으로 켜 두세요
- **입력을 검증하세요** - 적절한 입력 검증과 정제 방법을 보여주세요
- **보안 노트를 포함하세요** - 보안 고려 사항을 문서화하세요

보안 문제는 취약점 신고 절차를 다루는 [SECURITY.md](SECURITY.md)를 보세요.

## 행동 강령

우리는 환영하고 포용적인 커뮤니티를 제공하기 위해 노력합니다. 전체 커뮤니티 기준은 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)를 읽어 주세요.

요약하면:
- 존중하고 포용하세요
- 피드백을 겸허하게 받아들이세요
- 다른 사람이 배우고 성장하도록 도우세요
- 괴롭힘이나 차별을 피하세요
- 문제는 메인테이너에게 알리세요

모든 기여자는 이 강령을 준수하고 서로를 친절과 존중으로 대해야 합니다.

## 라이선스

이 프로젝트에 기여하면 귀하의 기여가 MIT 라이선스로 배포되는 데 동의하게 됩니다. 자세한 내용은 [LICENSE](../LICENSE) 파일을 보세요.

## 질문이 있으신가요?

- [README](README.md)를 확인하세요
- [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)를 검토하세요
- 기존 예제를 살펴보세요
- 토론을 위해 이슈를 여세요

기여해 주셔서 감사합니다! 🙏

---
**최종 업데이트**: 2026년 8월 4일
**Claude Code 버전**: 2.1.220
**출처**:
- https://code.claude.com/docs/en/overview
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
