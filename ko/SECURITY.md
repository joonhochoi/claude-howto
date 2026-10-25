<!-- i18n-source: SECURITY.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

# 보안 정책

## 개요

Claude How To 프로젝트의 보안은 우리에게 중요합니다. 이 문서는 우리의 보안 관행을 정리하고 보안 취약점을 책임 있게 신고하는 방법을 설명합니다.

## 지원 버전

다음 버전에 대해 보안 업데이트를 제공합니다:

| 버전 | 상태 | 지원 기한 |
|---------|--------|---------------|
| 최신(main) | ✅ 활성 | 현재 + 6개월 |

**참고**: 교육용 가이드 프로젝트로서 우리는 전통적인 버전 지원보다 현재의 모범 사례와 문서 보안을 유지하는 데 초점을 둡니다. 업데이트는 `main` 브랜치에 직접 적용됩니다.

## 보안 관행

### 코드 보안

1. **의존성 관리**
   - 모든 Python 의존성은 `requirements.txt`에 버전이 고정되어 있습니다
   - dependabot과 수동 검토를 통한 정기 업데이트
   - 매 커밋마다 Bandit으로 보안 스캔
   - 보안 검사를 위한 pre-commit 훅

2. **코드 품질**
   - Ruff 린트로 흔한 문제를 잡습니다
   - mypy 타입 검사로 타입 관련 취약점을 방지합니다
   - pre-commit 훅으로 표준을 강제합니다
   - 모든 변경은 병합 전에 검토합니다

3. **접근 제어**
   - `main` 브랜치에 브랜치 보호 적용
   - 병합 전 리뷰 필수
   - 병합 전 상태 검사 통과 필수
   - 저장소 쓰기 권한 최소화

### 문서 보안

1. **예제에 시크릿 없음**
   - 예제의 모든 API 키는 자리표시자입니다
   - 자격 증명은 절대 하드코딩하지 않습니다
   - `.env.example` 파일이 필요한 변수를 보여줍니다
   - 시크릿 관리에 대한 명확한 경고

2. **보안 모범 사례**
   - 예제가 안전한 패턴을 보여줍니다
   - 문서에서 보안 경고를 강조합니다
   - 공식 보안 가이드로 링크합니다
   - 관련 섹션에서 자격 증명 처리를 다룹니다

3. **콘텐츠 검토**
   - 모든 문서를 보안 문제 관점에서 검토합니다
   - 기여 가이드라인에 보안 고려 사항 포함
   - 외부 링크와 참조 검증

### 의존성 보안

1. **스캔**
   - Bandit이 모든 Python 코드의 취약점을 스캔합니다
   - GitHub 보안 경고를 통한 의존성 취약점 검사
   - 정기적인 수동 보안 감사

2. **업데이트**
   - 보안 패치를 신속히 적용합니다
   - 메이저 버전은 신중히 검토합니다
   - 체인지로그에 보안 관련 업데이트를 포함합니다

3. **투명성**
   - 보안 업데이트를 커밋에 기록합니다
   - 취약점 공개는 책임 있게 처리합니다
   - 필요하면 공개 보안 권고문을 발행합니다

## 취약점 신고

### 우리가 중요하게 보는 보안 문제

다음에 대한 신고를 환영합니다:
- 스크립트나 예제의 **코드 취약점**
- Python 패키지의 **의존성 취약점**
- 코드 예제의 **암호화 문제**
- 문서의 **인증/인가 결함**
- 설정 예제의 **데이터 노출 위험**
- **인젝션 취약점**(SQL, 명령 등)
- **SSRF/XXE/경로 순회** 문제

### 범위 밖 보안 문제

다음은 이 프로젝트의 범위를 벗어납니다:
- Claude Code 자체의 취약점(Anthropic에 신고)
- 외부 서비스나 라이브러리의 문제(업스트림에 신고)
- 사회공학 또는 사용자 교육(이 가이드에는 해당하지 않음)
- 개념 증명이 없는 이론적 취약점
- 공식 채널을 통해 신고된 의존성 취약점

## 신고 방법

### 비공개 신고(권장)

**민감한 보안 문제는 GitHub의 비공개 취약점 신고를 사용해 주세요:**

1. 방문: https://github.com/luongnv89/claude-howto/security/advisories
2. "Report a vulnerability" 클릭
3. 취약점 세부 정보 입력
4. 다음 포함:
   - 취약점에 대한 명확한 설명
   - 영향받는 구성 요소(파일, 섹션, 예제)
   - 잠재적 영향
   - 재현 단계(해당하는 경우)
   - 제안하는 수정(있다면)

**이후 진행:**
- 48시간 이내에 접수 확인을 드립니다
- 조사하고 심각도를 평가합니다
- 함께 수정 방안을 마련합니다
- 공개 일정을 조율합니다
- 보안 권고문에 신고자를 명시합니다(익명을 원하시면 제외)

### 공개 신고

민감하지 않은 문제나 이미 공개된 문제의 경우:

1. `security` 라벨을 붙여 **GitHub 이슈를 여세요**
2. 다음 포함:
   - 제목: `[SECURITY]` 뒤에 간단한 설명
   - 상세 설명
   - 영향받는 파일 또는 섹션
   - 잠재적 영향
   - 제안하는 수정

## 취약점 대응 절차

### 평가 (24시간)

1. 신고 접수를 확인합니다
2. [CVSS v3.1](https://www.first.org/cvss/v3.1/specification-document)로 심각도를 평가합니다
3. 범위 내인지 판단합니다
4. 초기 평가 결과를 신고자에게 전달합니다

### 개발 (1-7일)

1. 수정 사항을 개발합니다
2. 수정 사항을 검토하고 테스트합니다
3. 보안 권고문을 작성합니다
4. 릴리스 노트를 준비합니다

### 공개 (심각도에 따라 다름)

**Critical (CVSS 9.0-10.0)**
- 수정 사항 즉시 릴리스
- 공개 권고문 발행
- 신고자에게 24시간 사전 통보

**High (CVSS 7.0-8.9)**
- 48-72시간 이내 수정 사항 릴리스
- 신고자에게 5일 사전 통보
- 릴리스 시 공개 권고문 발행

**Medium (CVSS 4.0-6.9)**
- 다음 정기 업데이트에 수정 사항 포함
- 릴리스 시 공개 권고문 발행

**Low (CVSS 0.1-3.9)**
- 다음 정기 업데이트에 수정 사항 포함
- 릴리스 시 권고문 발행

### 발행

우리가 발행하는 보안 권고문에는 다음이 포함됩니다:
- 취약점 설명
- 영향받는 구성 요소
- 심각도 평가(CVSS 점수)
- 수정 버전
- 우회 방법(해당하는 경우)
- 신고자 명시(허락한 경우)

## 신고자를 위한 모범 사례

### 신고 전

- **문제를 확인하세요**: 일관되게 재현되나요?
- **기존 이슈를 검색하세요**: 이미 보고된 문제인가요?
- **문서를 확인하세요**: 안전한 사용법에 대한 안내가 있나요?
- **수정 방안을 테스트하세요**: 제안하는 수정이 동작하나요?

### 신고할 때

- **구체적으로**: 정확한 파일 경로와 줄 번호를 제시하세요
- **맥락을 포함하세요**: 왜 보안 문제인가요?
- **영향을 보여주세요**: 공격자가 무엇을 할 수 있나요?
- **단계를 제공하세요**: 어떻게 재현할 수 있나요?
- **수정을 제안하세요**: 어떻게 고치면 좋을까요?

### 신고 후

- **기다려 주세요**: 우리의 자원은 제한적입니다
- **응답해 주세요**: 후속 질문에 신속히 답해 주세요
- **기밀을 유지하세요**: 수정 전에 공개하지 마세요
- **조율을 존중하세요**: 우리의 공개 일정을 따라 주세요

## 보안 헤더와 설정

### 저장소 보안

- **브랜치 보호**: `main` 브랜치는 변경에 2명의 승인이 필요합니다
- **상태 검사**: 모든 CI/CD 검사를 통과해야 합니다
- **CODEOWNERS**: 핵심 파일에 지정된 리뷰어
- **서명된 커밋**: 기여자에게 권장

### 개발 보안

```bash
# Install pre-commit hooks
pre-commit install

# Run security scans locally
bandit -c pyproject.toml -r scripts/
mypy scripts/ --ignore-missing-imports
ruff check scripts/
```

### 의존성 보안

```bash
# Check for known vulnerabilities
pip install safety
safety check

# Or use pip-audit
pip install pip-audit
pip-audit
```

## 기여자를 위한 보안 지침

### 예제를 작성할 때

1. **시크릿을 절대 하드코딩하지 마세요**
   ```python
   # ❌ Bad
   api_key = "sk-1234567890"

   # ✅ Good
   api_key = os.getenv("API_KEY")
   ```

2. **보안 영향을 경고하세요**
   ```markdown
   ⚠️ **Security Note**: Never commit `.env` files to git.
   Add to `.gitignore` immediately.
   ```

3. **안전한 기본값을 사용하세요**
   - 인증을 기본으로 활성화
   - 해당되는 경우 HTTPS 사용
   - 입력 검증과 정제
   - 매개변수화된 쿼리 사용

4. **보안 고려 사항을 문서화하세요**
   - 보안이 왜 중요한지 설명
   - 안전한 패턴과 안전하지 않은 패턴 비교
   - 권위 있는 출처로 링크
   - 경고를 눈에 띄게 표시

### 기여를 검토할 때

1. **노출된 시크릿 확인**
   - 흔한 패턴 스캔(api_key=, password=)
   - 설정 파일 검토
   - 환경 변수 확인

2. **안전한 코딩 관행 검증**
   - 하드코딩된 자격 증명 없음
   - 적절한 입력 검증
   - 안전한 인증/인가
   - 안전한 파일 처리

3. **보안 영향을 테스트**
   - 오용될 수 있나요?
   - 최악의 경우는 무엇인가요?
   - 엣지 케이스가 있나요?

## 보안 자료

### 공식 표준
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [CVSS Calculator](https://www.first.org/cvss/calculator/3.1)

### Python 보안
- [Python Security Advisories](https://www.python.org/dev/security/)
- [PyPI Security](https://pypi.org/help/#security)
- [Bandit Documentation](https://bandit.readthedocs.io/)

### 의존성 관리
- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)
- [GitHub Security Alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)

### 일반 보안
- [Anthropic Security](https://www.anthropic.com/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

## 보안 권고문 아카이브

지난 보안 권고문은 [GitHub Security Advisories](https://github.com/luongnv89/claude-howto/security/advisories) 탭에서 확인할 수 있습니다.

## 문의

보안 관련 질문이나 보안 관행 논의:

1. **비공개 보안 신고**: GitHub의 비공개 취약점 신고 사용
2. **일반 보안 질문**: `[SECURITY]` 태그로 토론 열기
3. **보안 정책 피드백**: `security` 라벨로 이슈 생성

## 감사의 말

이 프로젝트의 보안을 유지하도록 도와주는 보안 연구자와 커뮤니티 구성원에게 감사드립니다. 취약점을 책임 있게 신고한 기여자는 보안 권고문에 명시됩니다(익명을 원하시면 제외).

## 정책 업데이트

이 보안 정책은 다음 시점에 검토·갱신됩니다:
- 새로운 취약점이 발견될 때
- 보안 모범 사례가 발전할 때
- 프로젝트 범위가 변경될 때
- 최소 연 1회

**최종 업데이트**: 2026년 8월 25일
**Claude Code 버전**: 2.1.245
**출처**:
- https://code.claude.com/docs/en/overview
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
**다음 검토**: 2027년 4월

---

Claude How To의 보안 유지에 도움을 주셔서 감사합니다! 🔒
