# 02. 규정 · 심사 · 상금

조사 시각: 2026-09-15 21:20 KST

---

## 0. 먼저 읽을 것: 메인 페이지와 규정 페이지가 서로 다릅니다

이 대회의 가장 큰 리스크는 **문서 간 불일치**입니다. 아래 표가 핵심입니다.

| 항목 | 메인 페이지 (`/`) | 규정 페이지 (`/rules`) | 어느 쪽을 따를 것인가 |
| --- | --- | --- | --- |
| 참가 자격 | `Students only` | `open to participants from around the world` + 6개 그룹 열거 | **규정 페이지.** 주최측이 포럼에서 위젯을 "display issue"로 공식 정정 |
| 상금 | `$ 33,900 + in prizes`, 상 6종 금액 명시 | `Prizes` / **`TBD`** | **메인 페이지.** 규정 페이지는 갱신되지 않은 상태 |
| 심사 기준 | 5항목 + **가중치 %** | 5항목, **가중치 없음**, 대신 `Scalability and feasibility` 포함 | **메인 페이지 가중치를 기준**으로 삼되 확장성 항목도 커버 |
| 영상 길이 | `a video of up to 5 minutes` | `A demo video (3–5 minutes recommended)` | **5분 초과 금지, 4분 40초 목표** |
| 수상 발표 | (스케줄 페이지) `September 25 at 9:00am EDT` | `Winners Announcement: September 2026` | **스케줄 페이지** |
| 제출물 | 5개 항목 상세 (덱 10장 포함) | 5개 항목 간략 (덱 언급 없음) | **메인 페이지가 상위집합.** 덱까지 준비 |
| 기간 길이 | 8/21~9/15 | `25 days` | 실제는 26일. 무의미한 오기 |

> **원칙: 두 페이지가 충돌하면 더 엄격한 쪽을 따르십시오.** 영상은 5분 이하, 제출물은 덱 포함, 심사는 확장성까지 언급. 이게 실격 리스크를 0으로 만드는 유일한 방법입니다.

---

## 1. 참가 자격 원문

### 메인 페이지 "Who can participate" 위젯

> Above legal age of majority in country of residence
> Students only
> Companies/professional organizations excluded from participation
> All countries/territories, excluding standard exceptions

### 규정 페이지 Eligibility

> The AI Builders Hackathon is open to participants from around the world.
>
> Eligible participants include:
> • Students and recent graduates
> • Software developers and engineers
> • AI/ML practitioners and researchers
> • Designers and product builders
> • Startup founders and entrepreneurs
> • Open-source contributors and technology enthusiasts
>
> Participants may compete individually or as a team.
>
> No prior hackathon experience is required. Whether you are building your first AI application or deploying advanced multi-agent systems, you are welcome to participate.

### 주최측 공식 해소 (포럼 `/forum_topics/44559`, 유일한 매니저 답변)

참가자 Damon Bree의 문제 제기:
> `I'm not a student, I'm an Entrepreneur. But when I go to join it says "Students only" which means I don't qualify.`

Deependra Gaur (Manager) 답변:
> `Yes, you're absolutely eligible! The "Students only" message is a display issue on the registration page. Entrepreneurs, founders, developers, researchers, and all other eligible participants listed are welcome to join.`

**본 개발자는 재학생이므로 양쪽 해석 모두에서 자격이 있습니다.** 연령(만 20세 > 한국 성년 19세), 국가(대한민국, 표준 제재국 아님), 개인 참가 모두 충족.

### 미확인 자격 사항

| 항목 | 상태 |
| --- | --- |
| 최대 팀 규모 | **미확인.** 포럼 질문 `Is a team of three participants allowed, and is there a maximum team size?` 미응답 |
| 18세 미만 보호자 동의 | **미확인.** 포럼 질문 미응답 (본 건과는 무관) |
| 기존 코드 재사용 허용 범위 | **미확인.** 규정은 `All submissions must be created during the hackathon period` 한 줄뿐, 관련 질문 3건 전부 미응답 |
| 라이선스 요구 | **요구 조항 없음.** 사이트 어디에도 오픈소스 라이선스 명시 요구 문구 없음 |

---

## 2. "해커톤 기간 중 제작" 조항 : 가장 애매하고 가장 위험한 조항

규정 원문은 단 한 줄입니다.

> `All submissions must be created during the hackathon period and align with the theme of Artificial Intelligence, Agentic AI, or Intelligent Systems.`

세부 예외 규정이 전혀 없고, 포럼에 올라온 **관련 질문 3건 모두 미응답**입니다.

- `/forum_topics/44785`: `May I take part if I started earlier?` → 미응답
- `/forum_topics/45000`: `I have already realised some front-end parts, but the main core AI-related part will be realised during this hackathon competition time. Is that acceptable?` → 미응답
- `/forum_topics/45165`: 기존 브랜드 위에 새 AI 워크플로를 얹는 경우 적격 여부 질문 → 미응답

### 방어 전략 (오늘 반드시 실행)

1. **해커톤 전용 신규 레포**를 만드십시오. 커밋 히스토리가 오늘 날짜부터 시작하면 논쟁 자체가 없어집니다.
2. 레포 루트에 `HACKATHON.md`를 두고 무엇이 언제 만들어졌는지 명시하십시오. 포럼 45165의 참가자가 제안한 `transparent changelog` 방식과 동일합니다.
3. 재사용하는 라이브러리/보일러플레이트는 README에 목록으로 공개하십시오. 숨기는 것보다 공개하는 쪽이 안전합니다.

---

## 3. 제출물 요건 (메인 페이지 원문, 가장 상세)

> To complete your participation in the AI Builders Hackathon, each team must submit the following materials before the submission deadline.
>
> **1. Project Submission Form**
> Complete the official submission form with your project details, including team information, project name, description, and all required links.
>
> **2. Working Product**
> Your submission must include a functional prototype, application, platform, agent, or software solution that demonstrates the core capabilities of your project. Judges should be able to understand and evaluate how your product works.
>
> **3. Source Code**
> Provide a public GitHub repository containing the source code for your project. The repository should include clear documentation, setup instructions, and any information required to review your work.
>
> **4. Demo Video**
> Submit a video of up to 5 minutes showcasing your project. The video should clearly explain:
> • The problem being solved
> • How the solution works
> • Key features and functionality
> • The role of AI within the product
> • A live demonstration of the product in action
>
> **5. Presentation Deck**
> Submit a presentation deck of up to 10 slides covering:
> • Problem Statement
> • Solution Overview
> • Target Users
> • Product Features
> • Technical Architecture
> • AI Technologies Used
> • Impact and Value Proposition
> • Future Roadmap

### 공개 레포는 예외 없음

한 참가자가 상용화 우려로 비공개 레포 + 라이브 데모 대체를 요청했습니다(`/forum_topics/44732`).

> `Would it be possible to submit a live, fully functional demo instead of a public GitHub repository, along with detailed technical documentation explaining the architecture, AI components, and how the system works?`

→ **주최측 미응답.** 예외가 승인된 사례가 없으므로 **public 레포는 필수로 간주**하십시오. 제출 직전 레포 공개 여부를 눈으로 다시 확인하십시오.

### 슬라이드 업로드 위치 불명

포럼에 2건의 질문(`/forum_topics/45157`, `/forum_topics/45206`)이 있으나 **전부 미응답**입니다.

> `where exactly do i upload my powerpoint presentation?`
> `Where to upload slides?`

한 참가자의 대안:
> `If we don't get an answer soon, I might just put it into my repo and link to it.`

→ **권장: 레포에 PDF를 넣고 Devpost 설명에 링크 + Devpost 폼에 업로드 필드가 보이면 병행 업로드.**

---

## 4. 심사 기준 (메인 페이지, 가중치 포함)

> **Innovation & Creativity (20%)**
> Judges will assess the originality and uniqueness of the idea, including how creatively AI technologies are applied to solve a problem.
>
> **Technical Implementation (25%)**
> Projects will be evaluated on the quality of their technical execution, including the design and implementation of AI models, agents, workflows, and system architecture.
>
> **Problem Solving & Impact (25%)**
> Judges will evaluate how well the solution addresses user needs, its practical applicability, potential real-world impact, and the clarity with which benefits and outcomes are demonstrated.
>
> **User Experience & Design (15%)**
> Judges will assess the quality of the user interface, ease of use, workflow design, accessibility considerations, and the overall polish and usability of the product.
>
> **Presentation & Demo (15%)**
> Teams will be evaluated on how effectively they communicate their project vision, solution, and technical decisions.

합계 100%.

### 규정 페이지의 심사 기준 (가중치 없음, 항목 하나 추가)

> Judging will consider:
> • Innovation and originality
> • Technical implementation
> • Real-world impact
> • User experience and design
> • **Scalability and feasibility**
>
> Participants are encouraged to build solutions that address meaningful challenges and demonstrate how AI can create measurable value for individuals, businesses, or communities.

`Scalability and feasibility`는 메인 페이지 가중치표에 **없는 항목**입니다. 심사위원 안내문에는 살아 있을 가능성이 높으므로, 아키텍처 슬라이드에 큐/캐시/비용 모델/수평 확장을 한 줄씩 넣어 커버하십시오.

### 배점 기반 시간 배분

| 항목 | 비중 | 남은 10시간 중 배분 |
| --- | --- | --- |
| Technical Implementation | 25% | 코딩 4h + 아키텍처 다이어그램 0.5h |
| Problem Solving & Impact | 25% | 정량 수치 3개 확보 1h (측정 스크립트 포함) |
| Innovation & Creativity | 20% | 고유 메커니즘 1개 설계 (코딩에 포함) |
| User Experience & Design | 15% | UI 마감 1.5h |
| Presentation & Demo | 15% | 영상 1.5h + 덱 1h |

> **핵심**: Technical + Impact = 50%. 그런데 이 두 항목은 **코드 품질이 아니라 "설계가 보이는가"와 "숫자가 있는가"** 로 채점됩니다. 심사위원은 레포를 정독하지 않습니다. 다이어그램 1장과 숫자 3개가 코드 500줄보다 점수가 높습니다.

---

## 5. 상금 상세

메인 페이지 표기: `$ 33,900 + in prizes` / `+ other prizes`

| 상 | 원문 | 수상자 수 | 실질 가치 |
| --- | --- | --- | --- |
| **Best SaaS Product** | `$ 4,000 in cash` | 1 | 🟢 현금 약 560만원 |
| **Tin Computer Credits** | `$ 299 in cash` | **100** | 🔴 Tin Growth Plan 1개월 크레딧 |
| NexFellow Founder's Choice Award | `3 Months of NexFellow Founder Plan for the most compelling AI product with strong user value and founder potential.` | 1 | 🔴 구독권 |
| NexFellow Product Excellence Award | `2 Months of NexFellow Founder Plan for the best executed product with excellent usability, technical quality, and real world value.` | 1 | 🔴 구독권 |
| NexFellow Innovation Award | `1 Month of NexFellow Founder Plan for the most creative and technically innovative use of AI.` | 1 | 🔴 구독권 |
| Top IDEAS will get Exposure | (별도 설명 없음) | 미확인 | 🔴 비현금 |

### $33,900의 정체

$4,000 + ($299 × 100) = **$33,900**. 광고 금액은 정확히 이 합입니다.

Tin Computer 상의 원문이 스스로 "크레딧"임을 인정합니다.

> `The first 100 eligible AI Builders Hackathon teams can each claim $299 in Tin Computer credits, equivalent to one month of the Tin Computer Growth Plan. Credits are available exclusively to official participating teams, with one claim per team. No credit card, payment, paperwork, or ongoing commitment is required.`
>
> `Teams can claim their credits, and the claim window will remain open for 60 days from the date the page goes live. Credits are available on a first come, first served basis and are limited to the first 100 eligible teams.`

> ### 결론: 실제 현금은 $4,000 하나뿐이며 1등 독식입니다.
> 명목 $33,900의 88%는 스폰서 크레딧이고, 그마저 "선착순 100팀"이라 심사 결과와 무관합니다.

### 4개 상을 한 프로젝트로 동시 조준하는 서사

상 문구가 각각 다른 축을 명시하므로 하나의 스토리로 전부 만족시킬 수 있습니다.

| 상 | 원문 키워드 | 대응 자산 |
| --- | --- | --- |
| Best SaaS Product | "SaaS" | 배포된 라이브 URL + 로그인 + 요금제 페이지 + 팀 개념 |
| Founder's Choice | `strong user value and founder potential` | 실사용자 인용 1개 + 시장 규모 + 창업 의지 슬라이드 1장 |
| Product Excellence | `usability, technical quality, and real world value` | 온보딩 30초 이내 + CI 배지 + 실제 사용 사례 |
| Innovation | `creative and technically innovative use of AI` | 고유 메커니즘 다이어그램 1장 |

### 참가 증서

> `Please note that Certificates of Participation will be awarded to all eligible participants who meet the participation requirements.` (`/updates/45816`)

---

## 6. 지식재산권 · 라이선스

**사이트 전체에 IP 조항이 존재하지 않습니다.** 규정 페이지에 지식재산권, 소유권 이전, 사용 허락에 관한 문구가 한 줄도 없습니다. 이는 참가자에게 유리하지만 동시에 규정 문서의 미완성을 보여줍니다. 오픈소스 라이선스 강제도 없으므로 레포 라이선스는 자유롭게 선택하십시오(공개만 하면 됩니다).

---

## 출처

- https://ai-builders-hackathon-2026.devpost.com/
- https://ai-builders-hackathon-2026.devpost.com/rules
- https://ai-builders-hackathon-2026.devpost.com/details/dates
- https://ai-builders-hackathon-2026.devpost.com/forum_topics/44559
- https://ai-builders-hackathon-2026.devpost.com/forum_topics/44732
- https://ai-builders-hackathon-2026.devpost.com/forum_topics/44785
- https://ai-builders-hackathon-2026.devpost.com/forum_topics/45000
- https://ai-builders-hackathon-2026.devpost.com/forum_topics/45157
- https://ai-builders-hackathon-2026.devpost.com/forum_topics/45165
- https://ai-builders-hackathon-2026.devpost.com/forum_topics/45206
- https://ai-builders-hackathon-2026.devpost.com/updates/45816
