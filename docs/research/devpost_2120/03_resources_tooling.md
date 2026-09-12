# 03. 리소스 · 스폰서 크레딧 · 툴링

조사 시각: 2026-09-15 21:20 KST

---

## 1. 공식 `/resources` 페이지: 비어 있음

https://ai-builders-hackathon-2026.devpost.com/resources

페이지는 200으로 응답하지만 **본문 콘텐츠가 없습니다.** 내비게이션과 푸터만 존재하고 리소스 목록, API 키 배포, 프로모 코드, 문서 링크가 한 건도 게시되지 않았습니다.

> 이는 메인 페이지 Get started 4단계의 `Explore the challenge themes, resources, and sponsor technologies.` 안내와 모순됩니다. 탐색하라고 한 리소스 페이지 자체가 비어 있습니다.

**실무적 의미: 본 대회에서 무료로 받을 수 있는 API 크레딧은 사실상 없습니다.** 본인이 이미 보유한 API 접근(Featherless 쿠폰 `VOLT26`, OpenAI, Anthropic)으로 전부 커버해야 합니다.

---

## 2. Tin Computer $299 크레딧 : 클레임 경로 추적 결과

### 상 원문 (메인 페이지 Prizes 섹션)

> `The first 100 eligible AI Builders Hackathon teams can each claim $299 in Tin Computer credits, equivalent to one month of the Tin Computer Growth Plan. Credits are available exclusively to official participating teams, with one claim per team. No credit card, payment, paperwork, or ongoing commitment is required.`
>
> `Teams can claim their credits, and the claim window will remain open for 60 days from the date the page goes live. Credits are available on a first come, first served basis and are limited to the first 100 eligible teams.`

### 🔴 클레임 URL: **미확인**

추적한 경로와 결과:

| 확인처 | 결과 |
| --- | --- |
| Devpost 메인 페이지 Prizes 섹션 | 링크 없음. 텍스트만 게시 |
| Devpost `/resources` | **본문 비어 있음** |
| Devpost `/updates` 9건 전수 | Tin Computer 크레딧 클레임 링크 언급 **없음** (NexFellow·Algoverse 스폰서 공지만 존재) |
| https://tin.computer/ | 해커톤 프로모, 크레딧 클레임 페이지, 쿠폰 코드 **없음** |
| https://lite.tin.computer | 무료 브라우저 체험판. 크레딧 클레임 플로우 **없음** |
| 웹 검색 | Devpost 페이지 문구가 그대로 색인되어 있을 뿐, 독립된 클레임 URL 없음 |

원문의 `from the date the page goes live` 표현은 **클레임 페이지가 아직 공개되지 않았을 가능성**을 시사합니다. 60일 창이 "페이지가 살아난 날부터"라고 쓰여 있다는 것은, 작성 시점에 그 페이지가 없었다는 뜻입니다.

### 권장 행동

1. **Discord `#ai-builders-hackathon` 채널에서 "Tin" 검색.** 클레임 링크가 공개되었다면 거의 확실히 여기에 있습니다. Discord 가입은 어차피 필수입니다.
2. 없으면 `hello@osconnect.org` 로 한 줄 문의. 다만 답변 기대치는 낮습니다(포럼 10스레드 중 답변 1건).
3. **이 크레딧을 프로젝트 계획의 전제로 삼지 마십시오.** Tin은 마케팅 자동화 도구라 어차피 오늘의 빌드와 무관합니다. 확보하면 보너스, 못 하면 손실 0입니다.

### Tin Computer가 실제로 무엇인가

- `open-source marketing system built for coding agents` (Apache 2.0)
- MCP 서버로 코딩 에이전트에 연결. Google Search Console, GitHub, Stripe, 애널리틱스와 연동해 SEO 페이지·랜딩 수정·아웃리치 PR을 자동 생성
- Docker 셀프호스팅 가능, 무료 체험은 https://lite.tin.computer
- Growth Plan 정가는 **미확인** (상 문구의 "$299 = 1개월분"이 유일한 단서)

---

## 3. NexFellow

| 항목 | 내용 |
| --- | --- |
| URL | https://www.nexfellow.com/ |
| 펠로십 | https://fellowship.nexfellow.com/ |
| 정체 | 빌더와 경험 있는 리뷰어를 매칭해 제품 피드백을 주는 플랫폼 |
| 해커톤 상 | Founder Plan 3개월 / 2개월 / 1개월 (3종) |
| 펠로십 | 100명 선발, 8주 글로벌 프로그램, 4개 트랙, **참가 무료** |

주최측 공지(`/updates/46412`)는 링크드인에서 펠로십 공지에 좋아요·댓글·리포스트를 요청하고 있습니다. 이는 상금 조건이 아니며 **제출과 무관한 홍보 요청**입니다.

> 전략적 시사점: NexFellow의 정체성이 "제품 검증과 피드백"입니다. 제출물에 **실제 사용자 피드백 인용 1건**이 들어가면 NexFellow 상 3종에 직접적으로 유리합니다. 오늘 밤 지인 3명에게 라이브 URL을 보내고 한 줄 피드백을 받아 덱에 인용하십시오. 30분이면 됩니다.

---

## 4. Algoverse / Sylus AI

| 스폰서 | 내용 |
| --- | --- |
| **Algoverse** (https://algoverseairesearch.org/) | 대학생 AI 연구 프로그램. NeurIPS/ICLR/ICML 논문 출판 지원, 12주. **상금 제공 아님.** Fall 코호트 지원 마감은 `Sunday, August 23 at 11:59 PM PT` 로 이미 경과. 문의 `admissions@algoverse.us` |
| **Sylus AI** (https://sylusai.com/) | 로고만 게시. 상금 항목 없음. AI 소셜미디어 자동화 플랫폼 |

> 재학생인 본 개발자에게 Algoverse는 **해커톤과 별개로 가치 있는 후속 경로**입니다. 다만 Fall 마감은 지났고 롤링 어드미션 여부는 미확인입니다.

---

## 5. Discord (유일한 필수 사항)

| 항목 | 값 |
| --- | --- |
| 초대 링크 | https://discord.com/invite/umEXASsAev |
| 서버명 | Open Source Connect |
| 멤버 | 약 2,600명 |
| 필수 채널 | `#introductions`, `#ai-builders-hackathon` |

주최측 원문:
> `Joining our Discord server is mandatory for all participants, as all important hackathon updates, announcements, discussions, and community interactions will happen there.`
>
> `1. Introduce yourself: Go to # introductions and share a short introduction along with your country name.`

> ⚠️ 푸터의 `https://discord.com/invite/HP4BhW3hnp` 는 **Devpost 공식 서버**로 본 해커톤과 무관합니다. 혼동 주의.
>
> ⚠️ 포럼에 초대 링크 무효 신고가 2건 있었습니다(`/forum_topics/44715`). 위 링크가 안 되면 `/updates/46223` 본문의 링크를 사용하십시오.

**5분 작업입니다. 실격 리스크 제거 차원에서 가장 먼저 하십시오.**

---

## 6. 본 개발자 스택 매핑 (오늘 쓸 것만)

이 대회는 지정 기술이 없으므로 **가장 빨리 배포되는 스택이 정답**입니다.

### 인프라: 이미 승리 조건을 갖췄습니다

| 자산 | 활용 |
| --- | --- |
| **상시 가동 Intel N150 서버** | 라이브 데모 호스팅. 무료 티어 슬립/콜드스타트 없음. 심사 기간 5일 내내 살아 있어야 하는데 이 조건을 만족하는 참가자는 소수 |
| **hajin.xyz 와일드카드 + TLS** | `<프로젝트>.hajin.xyz` 로 30분 내 HTTPS 라이브 URL. Devpost 폼의 "Try it out" 링크에 바로 들어감 |
| **nginx map 기반 서브도메인** | 새 서브도메인 추가가 설정 한 줄 |
| Android 폰 | 모바일 반응형 실기기 확인. 심사위원 중 일부는 폰으로 볼 가능성 |

> **오늘 23:00 KST 이전에 `https://<이름>.hajin.xyz` 가 "Hello" 한 줄이라도 응답하게 만드십시오.** 배포를 마지막에 하면 새벽 4시에 TLS 문제로 죽습니다.

### LLM

| 제공자 | 용도 |
| --- | --- |
| **Anthropic** | 주력. 구조화 출력, 도구 호출, 긴 컨텍스트 |
| **OpenAI** | 폴백 경로. 심사위원이 누를 때 한쪽이 죽어도 살아남게 |
| **Featherless (쿠폰 `VOLT26`)** | OpenAI 호환 엔드포인트. 비용 절감 경로이자 **"멀티 프로바이더 라우팅" 자체를 기술 포인트로 전시** 가능 |

> 💡 **폴백 라우터를 만드는 데 20분이 들고, 아키텍처 슬라이드에서 `Scalability and feasibility` 항목을 정확히 때립니다.** 비용이 다른 3개 프로바이더 사이의 라우팅 그래프 1장은 그 자체로 점수입니다.

### 웹/서버/DB

- 백엔드: FastAPI 또는 Node. 본인이 더 빠른 쪽. **오늘은 익숙함이 우월성을 이깁니다.**
- DB: SQLite로 시작하십시오. 10시간 안에 Postgres 마이그레이션 문제로 시간을 잃을 이유가 없습니다. 아키텍처 슬라이드에는 "현재 SQLite, 확장 시 Postgres + 큐" 로 적으면 오히려 feasibility 점수가 됩니다.
- 프런트: 단일 페이지 + Tailwind CDN. UX 15%는 **화면이 깨끗한가**로 결정되지 프레임워크로 결정되지 않습니다.

### 반드시 넣어야 할 SaaS 껍데기 (Best SaaS Product 조준)

1. 게스트 모드 또는 데모 계정 (심사위원이 회원가입 없이 누를 수 있어야 함)
2. 로그인 화면 (있다는 사실 자체가 "제품"으로 읽힘)
3. 요금제 페이지 1장 (Free / Pro / Team 3단. 가짜 결제 버튼 금지, "Coming soon" 표기)
4. 대시보드 화면 (설정, 히스토리, 지표)

### 영상 제작 (리눅스)

- 화면 녹화: `ffmpeg -f x11grab` 또는 OBS
- 편집: 컷 편집만. 트랜지션 금지. 시간 낭비입니다
- 자막: 필수. 심사위원 20명 중 상당수가 비영어권이고 음소거로 볼 수도 있습니다
- 업로드: YouTube **공개 또는 일부공개**. 비공개는 심사위원이 못 봅니다

---

## 출처

- https://ai-builders-hackathon-2026.devpost.com/
- https://ai-builders-hackathon-2026.devpost.com/resources
- https://ai-builders-hackathon-2026.devpost.com/updates
- https://ai-builders-hackathon-2026.devpost.com/updates/46223
- https://ai-builders-hackathon-2026.devpost.com/updates/46003
- https://ai-builders-hackathon-2026.devpost.com/updates/46412
- https://ai-builders-hackathon-2026.devpost.com/forum_topics/44715
- https://tin.computer/ , https://lite.tin.computer
- https://www.nexfellow.com/ , https://fellowship.nexfellow.com/
- https://algoverseairesearch.org/ , https://sylusai.com/
- https://discord.com/invite/umEXASsAev
