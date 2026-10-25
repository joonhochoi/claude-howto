<!-- i18n-source: resources/DESIGN-SYSTEM.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

# Claude How To - 디자인 시스템

## 비주얼 아이덴티티

### 아이콘 디자인 콘셉트: 코드 브래킷이 있는 나침반

Claude How To 아이콘은 코드 속 안내된 내비게이션을 표현하기 위해 **`>` 코드 브래킷이 있는 나침반**을 사용합니다:

```
     N (green)
     ▲
     │
W ───>─── E     Compass = Guidance/Direction
     │          > Bracket = Code/Terminal/CLI
     ▼
     S (black)
```

이 디자인이 만들어내는 것:
- **시각적 명료성**: "코드 내비게이션 가이드"를 즉시 전달합니다
- **상징적 의미**: 나침반 = 길 찾기, `>` = 코드/터미널
- **확장성**: 16px부터 512px까지 어떤 크기에서도 동작합니다
- **브랜드 정합성**: 최소한의 팔레트로 개발자 도구 미학에 맞습니다

---

## 색상 시스템

### 팔레트

| 색상 | Hex | RGB | 용도 |
|-------|-----|-----|-------|
| Black (Primary) | `#000000` | 0, 0, 0 | 메인 스트로크, 텍스트, 남쪽 바늘 |
| White (Background) | `#FFFFFF` | 255, 255, 255 | 라이트 배경 |
| Gray (Secondary) | `#6B7280` | 107, 114, 128 | 보조 눈금, 보조 텍스트 |
| Bright Green (Accent) | `#22C55E` | 34, 197, 94 | 북쪽 바늘, 중앙 점, 액센트 라인 |
| Near Black (Dark BG) | `#0A0A0A` | 10, 10, 10 | 다크 모드 배경 |

### 명암비(WCAG)

- 화이트 위 블랙: **21:1** AAA
- 화이트 위 그레이: **4.6:1** AA
- 화이트 위 그린: **3.2:1** (장식 전용, 텍스트에 사용 금지)
- 다크 위 화이트: **19.5:1** AAA

### 액센트 색상 규칙

**브라이트 그린(#22C55E)은 하이라이트 전용입니다:**
- 나침반 북쪽 바늘
- 중앙 점
- 액센트 밑줄/테두리
- 배경색으로는 절대 사용하지 않습니다
- 본문 텍스트로는 절대 사용하지 않습니다

---

## 타이포그래피

### 로고 글꼴
- **글꼴 패밀리**: Inter, SF Pro Display, -apple-system, Segoe UI, sans-serif
- **"Claude"**: 42px, 굵기 700(bold), 블랙
- **"How-To"**: 32px, 굵기 500(medium), 그레이(#6B7280)
- **부제**: 10px, 굵기 500, 그레이, letter-spacing 1.5px, 대문자

### 인터페이스 글꼴
- **글꼴 패밀리**: Inter, SF Pro, 시스템 글꼴(sans-serif)
- **굵기**: 400-600
- **스타일**: 깔끔하고 읽기 쉬움

---

## 아이콘 세부 사항

### 나침반 사양

나침반 마크는 다음 기하학적 요소로 구성됩니다:

```
Element             | Stroke/Fill    | Color
--------------------|----------------|------------------
Outer ring          | 3px stroke     | Black / White (dark mode)
North tick          | 2.5px stroke   | Black / White (dark mode)
Other cardinal ticks| 2px stroke     | Gray / White 50% (dark mode)
Intercardinal ticks | 1.5px stroke   | Gray / White 40% (dark mode)
North needle        | filled polygon | #22C55E (always green)
South needle        | filled polygon | Black / White (dark mode)
> bracket           | 3px stroke     | Black / White (dark mode)
Center dot          | filled circle  | #22C55E (always green)
```

### 크기별 변화

```
16px  → Ring + needles + chevron only (minimal)
32px  → Adds cardinal tick marks
64px  → Adds intercardinal tick marks
128px → Full detail, all elements crisp
256px → Maximum detail, thick strokes
```

---

## 크기 가이드라인

### 로고 크기

- **최소**: 200px 너비(웹 기준)
- **권장**: 520px(원본 크기)
- **최대**: 제한 없음(벡터 형식)
- **가로세로 비**: 약 4.3:1 (너비:높이)

### 아이콘 크기

- **최소**: 16px(파비콘)
- **권장**: 64-256px(앱, 아바타)
- **최대**: 제한 없음(벡터 형식)
- **가로세로 비**: 1:1 (정사각형)

---

## 여백과 정렬

### 로고 여백

```
┌─────────────────────────────────────┐
│                                     │
│        Clear Space Minimum          │
│         (logo height / 2)           │
│                                     │
│    [COMPASS]  Claude                │
│               How-To                │
│                                     │
└─────────────────────────────────────┘
```

### 아이콘 중심점

모든 아이콘은 캔버스의 중앙에 정렬됩니다:
- 256px 캔버스는 128×128
- 128px 캔버스는 64×64
- 다른 UI 요소와 정렬을 유지합니다

---

## 접근성

### 색상 명암비
- 모든 텍스트가 WCAG AA(최소 4.5:1)를 충족합니다
- 그린 액센트는 장식용이며 정보 전달용이 아닙니다
- 적록 색상 의존이 없습니다

### 확장성
- 벡터 형식이라 어떤 크기에서도 선명합니다
- 기하학적 형태가 16px에서도 식별됩니다
- 가용 크기에 따른 점진적 디테일

---

## 적용 예시

### 웹 헤더
- 크기: 520×120px 로고
- 파일: `logos/claude-howto-logo.svg`
- 배경: 흰색 또는 다크(#0A0A0A)
- 패딩: 최소 20px

### 앱 아이콘
- 크기: 256×256px
- 파일: `icons/claude-howto-icon.svg`
- 배경: 흰색 또는 다크
- 용도: 앱 단축키, 아바타

### 브라우저 파비콘
- 크기: 32px(기본), 16px(대체)
- 파일: `favicons/favicon-32.svg`
- 형식: 선명한 표시를 위한 SVG

### 소셜 미디어
- 프로필: 256×256px 아이콘
- 배너: 520×120px 로고(가운데 정렬)

### 문서
- 챕터 헤더: 크기에 맞게 조정한 로고
- 섹션 아이콘: 64×64px 파비콘
- 인라인: 32×32px 파비콘

---

## 파일 형식 세부 사항

### SVG 구조

모든 SVG 파일은 플랫 디자인입니다:
- 그라디언트 없음(단색만)
- 필터 효과 없음(블러, 글로우, 그림자 없음)
- 깔끔한 스트로크와 채우기 지오메트리
- 반응형 확장을 위한 ViewBox
- 읽기 쉽게 주석을 단 코드

### 브라우저 호환성

- Chrome/Edge: 완전 지원
- Firefox: 완전 지원
- Safari: 완전 지원
- iOS Safari: 완전 지원
- 모든 최신 브라우저: 완전 지원

---

## 사용자 지정

### 액센트 색상 변경하기

다른 액센트 색상으로 변형을 만들려면:

1. `#22C55E`를 모두 원하는 액센트 색상으로 바꿉니다
2. 장식 요소의 명암비가 3:1 이상으로 유지되는지 확인합니다
3. 블랙/화이트/그레이 구조는 그대로 둡니다

### 크기 조정

```css
svg {
  width: 256px;
  height: 256px;
}
```

SVG는 viewBox를 통해 자동으로 확장되므로 변환이 필요하지 않습니다.

---

## 버전 관리

git에서 디자인 변경을 추적합니다:
- SVG 파일은 일반 텍스트 파일이므로 평소처럼 버전 관리합니다
- 디자인 변경이 있는 릴리스에 태그를 답니다
- 커밋에 DESIGN-SYSTEM.md를 포함합니다

---

**최종 업데이트**: 2026년 2월
**디자인 시스템 버전**: 3.0
