<!-- i18n-source: resources/README.md -->
<!-- i18n-source-sha: 188f468 -->
<!-- i18n-status: translated -->
<!-- i18n-date: 2026-10-26 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="logos/claude-howto-logo.svg">
</picture>

# Claude How To - 브랜드 자산

Claude How To 프로젝트의 로고, 아이콘, 파비콘 전체 모음입니다. 모든 자산은 V3.0 디자인을 따릅니다. 코드 브래킷(`>`) 기호가 있는 나침반으로 코드를 안내하는 내비게이션을 표현하며, 블랙/화이트/그레이 팔레트에 브라이트 그린(#22C55E) 액센트를 사용합니다.

## 디렉터리 구조

```
resources/
├── logos/
│   ├── claude-howto-logo.svg       # Main logo - Light mode (520×120px)
│   └── claude-howto-logo-dark.svg  # Main logo - Dark mode (520×120px)
├── icons/
│   ├── claude-howto-icon.svg       # App icon - Light mode (256×256px)
│   └── claude-howto-icon-dark.svg  # App icon - Dark mode (256×256px)
└── favicons/
    ├── favicon-16.svg              # Favicon - 16×16px
    ├── favicon-32.svg              # Favicon - 32×32px (primary)
    ├── favicon-64.svg              # Favicon - 64×64px
    ├── favicon-128.svg             # Favicon - 128×128px
    └── favicon-256.svg             # Favicon - 256×256px
```

`assets/logo/`의 추가 자산:
```
assets/logo/
├── logo-full.svg       # Mark + wordmark (horizontal)
├── logo-mark.svg       # Compass symbol only (120×120px)
├── logo-wordmark.svg   # Text only
├── logo-icon.svg       # App icon (512×512, rounded)
├── favicon.svg         # 16×16 optimized
├── logo-white.svg      # White version for dark backgrounds
└── logo-black.svg      # Black monochrome version
```

## 자산 개요

### 디자인 콘셉트 (V3.0)

**코드 브래킷이 있는 나침반** — 안내와 코드의 만남:
- **나침반 링** = 내비게이션, 길을 찾는 일
- **북쪽 바늘(그린)** = 방향, 학습 경로의 진행
- **남쪽 바늘(블랙)** = 접지, 견고한 기반
- **`>` 브래킷** = 터미널 프롬프트, 코드, CLI 맥락
- **눈금 표시** = 정밀함, 구조화된 학습

### 로고

**파일**:
- `logos/claude-howto-logo.svg` (라이트 모드)
- `logos/claude-howto-logo-dark.svg` (다크 모드)

**사양**:
- **크기**: 520×120 px
- **용도**: 워드마크가 포함된 메인 헤더/브랜딩 로고
- **사용처**:
  - 웹사이트 헤더
  - README 배지
  - 마케팅 자료
  - 인쇄물
- **형식**: SVG(완전 확장 가능)
- **모드**: 라이트(흰색 배경) & 다크(#0A0A0A 배경)

### 아이콘

**파일**:
- `icons/claude-howto-icon.svg` (라이트 모드)
- `icons/claude-howto-icon-dark.svg` (다크 모드)

**사양**:
- **크기**: 256×256 px
- **용도**: 애플리케이션 아이콘, 아바타, 썸네일
- **사용처**:
  - 앱 아이콘
  - 프로필 아바타
  - 소셜 미디어 썸네일
  - 문서 헤더
- **형식**: SVG(완전 확장 가능)
- **모드**: 라이트(흰색 배경) & 다크(#0A0A0A 배경)

**디자인 요소**:
- 기본·중간 방위 눈금이 있는 나침반 링
- 그린 북쪽 바늘(방향/안내)
- 블랙 남쪽 바늘(기반)
- 중앙의 `>` 코드 브래킷(터미널/CLI)
- 그린 중앙 점 액센트

### 파비콘

웹 사용을 위해 여러 크기로 최적화한 버전입니다:

| 파일 | 크기 | DPI | 용도 |
|------|------|-----|-------|
| `favicon-16.svg` | 16×16 px | 1x | 브라우저 탭(구형 브라우저) |
| `favicon-32.svg` | 32×32 px | 1x | 표준 브라우저 파비콘 |
| `favicon-64.svg` | 64×64 px | 1x-2x | 고DPI 디스플레이 |
| `favicon-128.svg` | 128×128 px | 2x | Apple 터치 아이콘, 북마크 |
| `favicon-256.svg` | 256×256 px | 4x | 최신 브라우저, PWA 아이콘 |

**최적화 노트**:
- 16px: 최소 지오메트리 — 링, 바늘, 셰브론만
- 32px: 기본 방위 눈금 추가
- 64px 이상: 중간 방위 눈금까지 전체 디테일
- 모두 메인 아이콘과 시각적 일관성을 유지합니다
- SVG 형식이라 어떤 크기에서도 선명하게 표시됩니다

## HTML 통합

### 기본 파비콘 설정

```html
<!-- Browser favicon -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

<!-- Apple touch icon (mobile home screen) -->
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

<!-- PWA & modern browsers -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
```

### 전체 설정

```html
<head>
  <!-- Primary favicon -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

  <!-- Apple touch icon -->
  <link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

  <!-- PWA icons -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">

  <!-- Android -->
  <link rel="shortcut icon" href="/resources/favicons/favicon-256.svg">

  <!-- PWA manifest reference (if using manifest.json) -->
  <meta name="theme-color" content="#000000">
</head>
```

## 색상 팔레트

### 기본 색상
- **블랙**: `#000000` (기본 텍스트, 스트로크, 남쪽 바늘)
- **화이트**: `#FFFFFF` (라이트 배경)
- **그레이**: `#6B7280` (보조 텍스트, 보조 눈금)

### 액센트 색상
- **브라이트 그린**: `#22C55E` (북쪽 바늘, 중앙 점, 액센트 라인 — 하이라이트 전용이며 배경으로는 절대 쓰지 않습니다)

### 다크 모드
- **배경**: `#0A0A0A` (거의 검정)

### CSS 변수
```css
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

### Tailwind 설정
```js
colors: {
  brand: {
    primary: '#000000',
    secondary: '#6B7280',
    accent: '#22C55E',
  }
}
```

### 사용 지침
- 기본 텍스트와 구조 요소에는 블랙을 사용합니다
- 보조·지원 요소에는 그레이를 사용합니다
- 그린은 **오직** 하이라이트(바늘, 점, 액센트 라인)에만 사용합니다
- 그린을 배경색으로 사용하지 않습니다
- WCAG AA 명암비(최소 4.5:1)를 유지합니다

## 디자인 가이드라인

### 로고 사용
- 흰색 또는 다크(#0A0A0A) 배경에 사용합니다
- 비율을 유지해 확대·축소합니다
- 로고 주변에 여백을 둡니다(최소: 로고 높이 / 2)
- 배경에 맞는 라이트/다크 변형을 사용합니다

### 아이콘 사용
- 표준 크기(16, 32, 64, 128, 256px)로 사용합니다
- 나침반 비율을 유지합니다
- 비율을 유지해 확대·축소합니다

### 파비콘 사용
- 맥락에 맞는 크기를 사용합니다
- 16-32px: 브라우저 탭, 북마크
- 64px: 사이트 파비콘
- 128px 이상: Apple/Android 홈 화면

## SVG 최적화

모든 SVG 파일은 그라디언트나 필터가 없는 플랫 디자인입니다:
- 깔끔한 스트로크 기반 지오메트리
- 내장 래스터 없음
- 최적화된 패스
- 반응형 viewBox

웹 최적화:
```bash
# Compress SVG while maintaining quality
svgo --config='{
  "js2svg": {
    "indent": 2
  },
  "plugins": [
    "convertStyleToAttrs",
    "removeRasterImages"
  ]
}' input.svg -o output.svg
```

## PNG 변환

구형 브라우저 지원을 위해 SVG를 PNG로 변환합니다:

```bash
# Using ImageMagick
convert -density 300 -background none favicon-256.svg favicon-256.png

# Using Inkscape
inkscape -D -z --file=favicon-256.svg --export-png=favicon-256.png
```

## 접근성

- 높은 명암비(WCAG AA 준수 — 최소 4.5:1)
- 모든 크기에서 식별 가능한 깔끔한 기하학적 형태
- 확장 가능한 벡터 형식
- 아이콘에 텍스트 없음(텍스트는 워드마크에서 별도로 추가)
- 의미 전달을 적록 색상에 의존하지 않음

## 출처 표시

이 자산들은 Claude How To 프로젝트의 일부입니다.

**라이선스**: MIT(프로젝트 LICENSE 파일 참고)

## 버전 이력

- **v3.0** (2026년 2월): 블랙/화이트/그레이 + 그린 액센트 팔레트의 나침반-브래킷 디자인
- **v2.0** (2026년 1월): 에메랄드 팔레트의 Claude에서 영감을 받은 12광선 스타버스트 디자인
- **v1.0** (2026년 1월): 헥사곤 기반의 최초 진행 아이콘 디자인

---

**최종 업데이트**: 2026년 2월
**현재 버전**: 3.0 (Compass-Bracket)
**모든 자산**: 프로덕션 준비 완료 SVG, 완전 확장 가능, WCAG AA 접근성
