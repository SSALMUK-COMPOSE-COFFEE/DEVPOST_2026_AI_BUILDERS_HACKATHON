# 03. 과거 우승작 분석 — AI Builders Hackathon 2026 대비

조사일: 2026-09-15 (제출 마감일 당일)
조사 방법: Devpost 공개 API(`/api/hackathons`) + 각 해커톤 project-gallery(`?sort=winner`) + 개별 프로젝트 페이지 스크레이핑.
분석 표본: 15개 해커톤, **우승작 38건 정밀 분석 + 비우승작 8건 대조**.

---

## 0. 먼저: 우리 대회의 실제 심사 기준 (중요 — 브리핑과 다름)

출처: https://ai-builders-hackathon-2026.devpost.com/

사전 브리핑에는 "technical completeness 30% / product-market fit 30% / UX·design 20% / originality 20%"로 되어 있었으나,
**Devpost 공식 페이지의 실제 기준은 5개 항목**이다.

| 항목 | 비중 | 공식 문구 |
| --- | --- | --- |
| Innovation & Creativity | **20%** | "originality and uniqueness of the idea, including how creatively AI technologies are applied" |
| Technical Implementation | **25%** | "design and implementation of AI models, agents, workflows, and system architecture" |
| Problem Solving & Impact | **25%** | "how well the solution addresses user needs, its practical applicability, potential real-world impact" |
| User Experience & Design | **15%** | "user interface, ease of use, workflow design, accessibility considerations, and the overall polish" |
| **Presentation & Demo** | **15%** | "how effectively they communicate their project vision, solution, and technical decisions" |

제출물 요건(반드시 5종 전부):
1. Project Submission Form
2. **Working Product** (동작하는 프로토타입 — 심사위원이 직접 이해·평가 가능해야 함)
3. **Public GitHub repo** (문서·셋업 가이드 포함)
4. **Demo Video, 최대 5분** — 문제 / 동작 원리 / 핵심 기능 / **AI의 역할** / 라이브 데모 5요소 명시
5. **Presentation Deck, 최대 10슬라이드** — Problem / Solution / Target Users / Features / **Technical Architecture** / AI Technologies / Impact & Value / **Future Roadmap**

상금: 총 $33,900+. 최상위는 **Best SaaS Product $4,000 (1팀)**.
심사위원 20명 구성이 결정적 힌트다: Apple·Microsoft·PayPal·Visa·IBM·AWS·ServiceNow의 **시니어 엔지니어 + Sr. Product Manager가 절반**.
→ 순수 기술 자랑보다 **"PM이 납득하는 문제 정의 + 엔지니어가 납득하는 아키텍처"** 조합이 표를 얻는다.
참가자 3,403명. Devpost 갤러리는 마감 전까지 비공개.

> "We are not looking for pitch decks, concept videos, or **AI wrappers with minimal differentiation**."
> "If you can build something that makes people say, **'I would use this tomorrow,'** you're exactly who this challenge is for."
> — 대회 공식 소개문

"AI Builders Hackathon"의 **이전 에디션은 Devpost에 존재하지 않는다**(2026이 1회차). 이름이 비슷한 "Claude Builders Club" 계열(McGill, ALU, SoCal, UW 등)은 전부 오프라인 대학 이벤트이고 수상작 갤러리가 비공개라 참고 가치가 낮아, **온라인·일반 AI/SaaS 대회**로 표본을 대체했다.

---

## 1. 분석 대상 해커톤 15개

| 해커톤 | 기간 | 참가자 | 성격 |
| --- | --- | --- | --- |
| World's Largest Hackathon presented by Bolt | 2025-05-30~06-30 | 128,334 | 온라인, vibe coding, 상금 최대 |
| RevenueCat Shipaton 2025 | 2025-07-31~10-01 | 51,882 | 온라인, **실매출 SaaS** |
| OpenAI Build Week | 2026-07-13~21 | 46,703 | 온라인, 1주일 |
| H0: Hack the Zero Stack (Vercel v0 + AWS) | 2026-05-27~06-29 | 9,729 | 온라인, **"Monetizable B2B/B2C App" 트랙** |
| AWS AI Agent Global Hackathon | 2025-09-08~10-22 | 9,466 | 온라인, 에이전트 |
| OpenAI Open Model Hackathon | 2025-08-05~09-11 | 8,636 | 온라인 |
| USAII® Global AI Hackathon 2026 | 2026-06-14~22 | 6,066 | 온라인, **8일** |
| UiPath AgentHack | 2026-05-15~06-29 | 4,007 | 온라인, 엔터프라이즈 에이전트 |
| Mind the Product — World Product Day | 2026-05-20~06-20 | 1,310 | 온라인, **PM이 심사** |
| Maximally Vibe-a-thon | 2025-12-26~29 | 1,296 | **3일 단기** |
| Wix Make-A-SaaS Hackathon | 2023-02~04 | 1,133 | SaaS 전용 |
| Maximally Startup Makeathon | 2025-07-01~06 | 437 | 6일 |
| Global AI Agents League (Fetch.ai) | 2025-02~04 | 1,456 | 에이전트 |
| AGI, Inc. × OpenAI × Lovable REAL Agent Challenge | 2025-11-23 | 132 | **1일** |
| Accel + Anthropic Dev Day Showcase | 2025-10-01~05 | 201 | 쇼케이스 |

---

## 2. 우승작 정밀 분석 (18선)

각 항목: 대회/수상 → 한 줄 피치 → 문제·타깃·BM → 스택 → Devpost 글 구조 → 데모 영상 → 우승 사유.

### 2-1. Tailored Labs — **Grand Prize**, World's Largest Hackathon (Bolt, 2025)
- URL: https://devpost.com/software/civilink · 제품: https://tailorlabsai.com
- 피치: "AI-powered video timeline editor that lets creators build professional edits through natural language commands ... end to end 'one-shot' video generation."
- 문제/타깃: 영상 편집의 수작업 컷·배치에 수 시간 소모 / 크리에이터. BM: Stripe 구독(스택에 명시).
- 스택: Next.js 15, **OpenAI GPT-4 + Claude Opus**, Remotion(클라우드 렌더), Supabase(DB·auth·storage), Stripe, Tailwind, AWS Lambda(에이전틱 플로우), Bolt.new.
- 글: 386단어로 **가장 짧은 축**. 섹션 = Inspiration / What it does / How we built it 3개뿐. 이모지 헤딩. 코드 스니펫 1개. 이미지 0장, 대신 **자체 도메인 데모 링크**(`?demo=bolthackathon` 심사 전용 파라미터까지 달았다).
- 영상: YouTube **2분 55초**.
- 우승 이유: "Bolt.new for Video Editing"이라는 **한 문장 유비**로 포지셔닝이 즉시 전달됨 + 타임라인 UI라는 난도 높은 결과물 + 자체 도메인 + Stripe. 글이 짧아도 **제품이 있으면 이긴다**는 표본.

### 2-2. Weight Coach — 2nd Place + Voice AI Challenge, Bolt WLH
- URL: https://devpost.com/software/weight-coach · https://weight.coach · TestFlight 링크 동봉
- "AI-powered meal planner with voice cooking assistant."
- 스택: React Native/Expo, AWS, TypeScript. 영상 **2분 48초**, 글 1,273단어, 이미지 6.
- 우승 이유: **TestFlight 실배포**. 심사위원이 실제 폰에 설치 가능 = "working product"의 최상급 증거.

### 2-3. KeyHaven — 3rd Place, Bolt WLH
- URL: https://devpost.com/software/keyhaven · https://keyhaven.netlify.app
- "secure platform for developers and teams to store, rotate, and monitor API keys."
- 문제: **본인이 해커톤 중 직접 겪은 통증**("I found myself repeatedly running into issues related to securely storing API keys ... Conversations with other builders confirmed that I was not alone") → 타깃: 솔로 해커·소규모 팀.
- BM: **"KeyHaven offers a tiered subscription model"** — Stripe 동적 가격 로직 직접 구현.
- 스택: React/Vite/TS, Supabase, Postgres, Stripe, **Resend(알림 메일)**, Netlify.
- 글 532단어, 커스텀 섹션(🚀 Project Overview / 💡 What I Learned / 🛠️ How I Built It / ⚠️ Challenges / 🌱 Reflection), 스크린샷 3장(Landing / Dashboard / Key Storage).
- 영상 **3분 1초**. 우승 이유: **결제·이메일·암호화까지 붙은 완결형 SaaS**. "prototype"이 아니라 "사업".

### 2-4. Klinva — 4th Place, Bolt WLH (**SaaS 트랙 참고 최적 표본**)
- URL: https://devpost.com/software/klinva-ultimate-crm-saas-for-commercial-cleaning-companies · http://www.klinva.com
- "AI-powered SaaS CRM built exclusively for commercial cleaning companies."
- 문제/타깃: 상업용 청소업체. 초니치. "Despite being a multi-billion-dollar industry, no software truly caters to their specific needs."
- BM: 명시적 시장 규모 계산 — **"With over 150,000 commercial cleaning companies across the US, UK, Canada, and Australia even capturing 10% market share could make Klinva a multi-million dollar business."**
- 스택: Bolt + React 18 + Tailwind, **Supabase**, **Clerk(auth)**, Netlify.
- 글 433단어(짧음), 표준 7섹션, 이미지 1. 영상 **정확히 2분 00초**.
- 우승 이유: **① 초니치 타깃 ② 4개 역할 기반 대시보드(Owner/Staff/Client/Telemarketing)라는 "진짜 업무 구조" 반영 ③ What's next에 TAM·베타·과금 로드맵.** 글은 짧지만 PMF 문장이 전부 들어있다.

### 2-5. ModelMash — 7th Place + **"Most Likely to Get Funded"**, Bolt WLH
- URL: https://devpost.com/software/modelmash-find-the-perfect-llm · https://modelmash.site
- "Easily test hundreds of different LLMs to find the best one for your specific task."
- BM 명시: **"Pay-as-You-Go Model: Users design their test, pay a few dollars to run it ... I didn't feel like building a subscription business out of this."**
- 바이럴 설계: 리포트 공유 링크 + 공개 템플릿 라이브러리("This encourages sharing and viral spread").
- 스택: Bolt/React, Supabase, **OpenRouter**(단일 API로 수십 모델), Railway(장시간 작업), Netlify.
- 글 1,129단어, 스크린샷 5장(Homepage/Comparison/Templates/Results/Detail). 영상 **4분 20초**.
- 우승 이유: 자기 다른 프로젝트에서 발견한 진짜 문제 → 일반화. **과금 모델과 바이럴 루프를 글에 명시적으로 서술**한 것이 "Most Likely to Get Funded" 특별상으로 직결.

### 2-6. Payout — **Grand Prize (Build & Grow Award)**, RevenueCat Shipaton 2025
- URL: https://devpost.com/software/payout-cwdniv · https://www.trypayout.app
- "Discover brands that owe you money through class action settlements."
- **실측 지표를 그대로 박음**: "Shipped v1 in 10 days by leveraging AI. Hit both the App Store and Google Play with: **17,000+ users / $30,017 revenue / 1750+ paid subscriptions / 500,000 X impressions**."
- 스택: React Native, Node/TS on Vercel, **RevenueCat + Adjust + Mixpanel**, Figma, v0 + Cursor + Claude Code.
- 글 462단어로 짧지만 **숫자 밀도 최고**. 섹션을 Mobile/Website/Backend/Analytics/Design으로 쪼갬. What's next = "October 🎃" 월별 로드맵.
- 우승 이유: **매출·유저 수라는 반박 불가 증거**. PMF 항목에서 만점 이외의 채점이 불가능.

### 2-7. Gurwi — 1st Place (#BuildInPublic), Shipaton 2025
- URL: https://devpost.com/software/gurwi-learn-anything · iOS·Android·웹 3채널 링크
- 글 **3,003단어**로 표본 중 최장급. What's next를 8개 번호 항목으로 분해(콘텐츠 확장 → 언어학습 → 코딩모듈 → B2B/B2G). 이미지 11장. 영상 3분 28초.
- 스택: Flutter, Firebase, Google Cloud, TypeScript.
- 우승 이유: "Achieving overwhelming **market validation**"을 별도 소제목으로 뽑아 증거 나열. 3개 스토어 동시 배포.

### 2-8. Second Voice — **1st Place | Apps for Your Life**, OpenAI Build Week 2026
- URL: https://devpost.com/software/second-voice-uk1peq · GitHub: https://github.com/dondetir/SecondVoice
- "A zero-training AI communication aid that turns unclear speech from people with dysarthria into what they meant to say."
- 문제 정의가 **수치로 시작**: "Most ALS patients eventually develop it, along with over half of children with cerebral palsy and a large share of stroke and Parkinson's patients."
- **경쟁사 대비 차별점을 한 문장으로**: "Existing tools like **Voiceitt** ask users to record 50+ phrases before they even work. We wanted something that works **from the first sentence**."
- 핵심 UX 원칙: **"confirm-before-speak"** — "Nothing is said on the user's behalf without that explicit confirmation."
- 스택: GPT-5.6(Responses API), STT/TTS, Codex로 구현.
- 글 **394단어**(표본 중 최단급), 이미지 0장, 표준 7섹션. 영상 **2분 44초**.
- 우승 이유: **이미지 0장·글 394단어로도 1등**. 이유는 ① 정량화된 문제 ② 명명된 경쟁사와의 1문장 차별점 ③ "zero-training"이라는 기억되는 제품 속성 ④ 윤리적 UX 결정을 제품 사양으로 승격. → **원고 길이는 상관없고, 문장의 정보 밀도가 전부**.

### 2-9. veTriage — 1st Place | Work & Productivity, OpenAI Build Week
- URL: https://devpost.com/software/veterinary-four-color-triage-app · https://vetriage.netlify.app · GitHub 공개
- "Built by a veterinarian & practice owner with **no coding experience**."
- 글 **6,460단어**(표본 최장), 소제목 40개, 이미지 15장. 영상 **2분 34초**로 짧음.
- 우승 이유: **"From a required pilot to routine use in one day"** — 자기 병원에서 실사용 중. 도메인 전문가가 직접 만든 제품 + 결정론적 안전 아키텍처("A deterministic safety architecture"). 실사용 증거 > 기술 화려함.

### 2-10. Sentinel — 2nd Place | Developer Tools, OpenAI Build Week
- URL: https://devpost.com/software/sentinel-way5bd · GitHub: https://github.com/BashaarJavaid/MCP-Sentinel
- "Catch security holes in your MCP server before you ship it."
- **3계층 아키텍처를 글에서 명확히 서술**: ① 결정론적 정적분석(Python AST + Semgrep, 7 rule) → ② GPT-5.6 리뷰(단, **"it's a reviewer, not an author"** — 새 취약점 생성·probe 코드 작성 금지, 실제 line range 인용 강제) → ③ Docker 격리 샌드박스에서 4종 실제 probe 실행.
- 출력이 **SARIF 2.1.0** → GitHub code scanning에 그대로 꽂히고 GitHub Action으로 PR fail 가능. 모든 findings를 **OWASP Agentic Top 10**에 매핑.
- 글 1,318단어, 이미지 0. 영상 **2분 45초**.
- 우승 이유: **"LLM을 어디에 쓰고 어디에 안 쓰는지"를 설계 결정으로 설명**한 것. `store:false`, Structured Outputs, redacted context까지 언급 → Technical Implementation 항목 만점 설계. AI wrapper가 아님을 증명하는 교과서.

### 2-11. Waylo — **First Place | Monetizable B2C App**, H0 (Vercel v0 + AWS, 2026)
- URL: https://devpost.com/software/fdvnjvd · https://waylo-web-virid.vercel.app
- "An AI that lives on your Mac and guides you through anything — a pulsing red dot + voice, step by step."
- 문제 도입부가 압도적: "My grandmother calls me every week — not to chat, but to ask how to attach a photo to an email."
- **비용 우선 4계층 캐스케이드** (이 대회 최고의 기술 서술):
  - L0 Accessibility Tree (~5ms, **free**) → L1 On-device OCR/Apple Vision (~40ms, free) → L2.5 **듀얼 YOLO**(OmniParser + Screen2AX, ~150–300ms, near-free) → L3 AWS Bedrock Nova 2 Lite (~800ms, **paid**) → **Tap-to-Teach 휴먼 폴백**.
  - "designed to use **AI as a last resort, not a first instinct**."
- 자가학습: Aurora PostgreSQL + pgvector, Titan Embeddings 1536-dim, **유사도 0.92 임계**로 "create a new folder"와 "make a new folder"를 같은 캐시에 히트 → 반복 작업은 Nova 호출 0회. 한 유저의 Tap-to-Teach 교정이 전체 유저에게 반영.
- 글 1,592단어, 이미지 9, 아키텍처 소제목 4개. 영상 **3분 9초**.
- 우승 이유: **레이턴시·비용을 숫자로 명시한 아키텍처** + 감정적 훅 + 자가개선 플라이휠(= 해자). "Monetizable" 트랙에서 단가 구조를 증명한 유일 수준.

### 2-12. Mnema — Second Place | **Monetizable B2B App**, H0
- URL: https://devpost.com/software/mnema · http://mnema-iota.vercel.app
- "The translation workspace with a memory. Context-aware localization for film and media."
- 글 **4,016단어**(이미지 0). 스택: React/TS, Amazon RDS, FFmpeg, AWS. 영상 **3분 15초**.
- 우승 이유: B2B 워크플로 도구 + "memory"라는 단일 차별점에 글 전체를 집중.

### 2-13. GraphFlow — Second Place | Open Innovation, H0
- URL: https://devpost.com/software/graphflow-release-safety-intelligence · https://graphflow-ten.vercel.app
- "Release pipelines as a live dependency graph — see blast radius, not just red X's."
- **"Why This Is Different"라는 전용 섹션을 직접 만들어 넣음** — 표준 7섹션에 차별점 섹션을 추가한 유일 표본.
- 글 1,377단어, 이미지 6, 영상 **3분 48초**. 스택: AWS, DynamoDB.

### 2-14. TradeWizard — Second Place | Monetizable B2C, H0
- URL: https://devpost.com/software/tradewizard-8xp61z · https://tradewizard.live · GitHub 공개
- 글 **6,623단어**. 소제목이 곧 심사 루브릭: "AI Architecture Explanation" / "**Human-in-the-Loop Decision**" / "**Responsible AI Guardrail**" / "Agent architecture and coordination" / "Conflict resolution and validation chain" / "Memory without anchoring" / "**Hallucination resistance**" / "**What happens when a recommendation is wrong**" / "**Cost and operational shape**".
- 영상 2분 47초. 우승 이유: **금융 도메인의 리스크를 정면으로 문서화**. "틀렸을 때 어떻게 되는가"를 쓰면 심사위원의 최대 반론이 사전 제거된다.

### 2-15. Province — 3rd Place, AWS AI Agent Global Hackathon
- URL: https://devpost.com/software/province · https://www.provincetax.com
- "An AI-native tax filing agent system that turns complex tax prep into a natural conversation."
- 문제를 **가격으로 정의**: "DIY software that bombards users with 100+ confusing questions" vs "Professional CPAs charging **$300-500+** for simple returns."
- 기술적 킬러 포인트: **"AI-Powered Form Filling with Zero Manual Mapping"** — 기존 세무SW는 폼 필드를 사람이 수작업 매핑(폼당 수시간, IRS 개정 때마다 파손). FormMappingAgent가 Claude 3.5 Sonnet으로 `f1_32[0]` 같은 난독 필드명을 의미 매핑 → DynamoDB 캐시 → 이후 **~100ms**.
- 멀티에이전트 4종(Intake / Tax Planner / FormMapping / Review) on AWS Bedrock Agent runtime. Bedrock Data Automation(IDP), ElasticSearch 지식베이스, Next.js 15.
- **"Accomplishments: 1. 100% Form Filling Accuracy"** — 정확도 수치 제시. Challenges에 "AWS Bedrock Rate Limits (2 RPM)" 같은 진짜 제약을 솔직히 씀.
- 글 1,865단어, 이미지 5, 영상 **2분 50초**.
- 우승 이유: **"이 부분이 기술적으로 어렵고 우리만 풀었다"를 한 곳으로 좁힌 것.** 계산 결과를 실제 숫자 예시(AGI $55,151.93 → REFUND $11,971.94)로 보여줌.

### 2-16. Gauntlet — **Grand Prize**, UiPath AgentHack 2026
- URL: https://devpost.com/software/gauntlet-go-safe-or-go-home · GitHub: https://github.com/tdries/uipath-hackathon-gauntlet
- "GAUNTLET sends adversarial AI's to attack your AI service agent with multi-turn attacks."
- 포지셔닝 한 문장: "Every other agent eval framework we looked at is **cooperative** ... So we built the opposite." / "Think **AlphaGo self-play, but for prompt-injection**."
- 검증 가능한 실적: "Today the corpus is **42 fights** against fake-ceo-naive, with the Coach having invented several attacks **no human seeded**."
- 컴포넌트를 표로 매핑(Maestro Case / Flow / Test Manager / Action Center / Coded App). OWASP LLM Top-10 + MITRE ATLAS 커버리지 히트맵.
- **데모 정직성을 명시**: "We didn't want a faked demo. CoachLab's live mode makes a **real** Anthropic call ... The persona you see was written **during the demo, not pre-recorded**."
- 글 963단어, 영상 **5분 44초**(이 대회는 길이 제한이 느슨). Claude Code로 전체 구축.
- 우승 이유: ① 기존 카테고리의 **반대편**이라는 명확한 originality ② 스폰서 제품 표면을 전부 사용(HITL 승인까지) ③ "슬라이드도 localhost도 아니다"를 스스로 증명.

### 2-17. Park Pal — **GOLD**, Mind the Product World Product Day 2026 (PM 심사)
- URL: https://devpost.com/software/park-pal-wbgqmk · https://parkpal-delta.vercel.app
- "The Airbnb for Parking."
- **고객 리서치 수치**: "We validated this with **260+ surveys** of drivers and homeowners, and the central finding shaped the whole product: homeowners didn't ask 'who needs parking?', they asked **'what happens if something goes wrong?'**"
- 그 인사이트를 제품으로 직결: ID·번호판 검증, 호스트 사전 승인, 체크인/아웃 타임스탬프 사진, **예약 확정 전까지 정확한 주소 비공개**. 자평: "The less exciting the feature sounded, the more it mattered."
- GTM 증거: 주차 티켓·이벤트 데이터로 수요 GIS 맵 별도 구축, 부동산 관리사 PMI Arka로부터 **LOI 확보**.
- 스택: Next.js, Supabase(Postgres/auth/storage), **Stripe**, Mapbox, Vercel, shadcn/ui, v0 + Claude Code, Novus(제품 분석).
- 글 646단어. 섹션 구조를 **표준 7섹션 대신 PM 언어로 재구성**: "What we built / **Who it's for** / **What makes it distinctly ours** / Tools we used / What we learned shipping it". 영상 **2분 51초**.
- 우승 이유: PM 심사위원단이 채점하는 대회에서 **PM의 언어로 썼다**. 우리 대회도 심사위원 절반이 Sr. PM이므로 **이 구조가 가장 이식 가치가 높다**.
- 인용할 만한 마무리: "When anyone can build, the thing that separates a demo from a product is **knowing what's worth building**."

### 2-18. Penetron — Honorable Mention + **Best First-Time Builder**, UiPath AgentHack
- URL: https://devpost.com/software/penetron · GitHub: https://github.com/kryo-o/penetron
- "Penetron **proves** vulnerabilities instead of just flagging them."
- 제목 자체가 주장: "Inspiration — **security tools cry wolf**". 이미지 9장, 글 869단어, 영상 4분 56초.
- 우승 이유: 기존 도구의 실패 모드(오탐)를 제품의 존재 이유로 삼은 **한 줄 차별화**.

### 보조 표본(요약)
- **AegisAgent** (AWS 2nd): 보험 청구 자동화, "fully developed by Kiro"를 제목에 박아 스폰서 도구 활용을 전면화. 영상 2분 24초.
- **Oratio** (AWS, Best Bedrock App): Nova Sonic 음성 에이전트 빌더. 영상 **14분 36초** — 표본 중 최장이자 명백한 안티패턴(그럼에도 카테고리상 수상).
- **AgentShell** (AWS, Best Strands SDK): "MCP를 정보 검색에서 신체 제어로 재정의". 소제목에 "📊 Impact & Value / Measurable Impact / Extreme Cost-Effectiveness / Reproducibility" — **심사 항목을 소제목으로 직역**한 구조.
- **BrandIQ** (Mind the Product): 썸네일 생성. 영상 **1분 57초**로 최단, 이미지 8장. 섹션을 파이프라인 4단계로 분해.
- **warmscreen** (AGI×OpenAI×Lovable, Best Use of Daytona): 7-agent 리플렉션 채용 에이전트. 글 474단어, 영상 **1분 59초**. 1일 해커톤에서는 이 정도 스코프가 상한.
- **Launchify** (USAII 3rd): "Know what you don't know — before you build." 이미지 11장, GitHub 공개, 자체 도메인. Gemini + Postgres + AWS.
- **Alyosha** (USAII High School Grand Prize): 출소자 지원 정보 통합. 글 1,880단어, 영상 6분 31초.

---

## 3. 우승작 vs 비우승작 정량 대조

같은 해커톤 갤러리의 비우승작 8건(H0, OpenAI Build Week, UiPath AgentHack)과 비교.

| 지표 | 우승작 (n=38) | 비우승작 (n=8) |
| --- | --- | --- |
| Devpost 본문 단어 수(중앙값) | **1,004** (386~6,623) | **483** (210~2,287) |
| 데모 영상 길이(중앙값) | **174초 ≈ 2분 54초** | 236초, 분산 극심(59초~807초) |
| 영상 길이 분포 | **31건 중 24건이 2~5분 구간** | 59초·448초·807초 등 양극단 |
| 본문 이미지 수(중앙값) | 3.5장 | 6장 |
| 공개 GitHub 링크 | 18/38 (대회 요건 아닐 때가 많음) | 4/8 |
| **동작하는 라이브 URL** | **27/38 (71%)** | 6/8 |
| "What's next" 섹션 | 29/38 | 7/8 |

**해석**
- **이미지 수는 우승과 무관하다.** 오히려 비우승작이 더 많았다. 스크린샷 도배 ≠ 설득.
- **본문 길이는 2배 차이**지만, Second Voice(394단어 1위)·Klinva(433단어 4위)처럼 짧아도 이긴다. 결정 변수는 길이가 아니라 **"단어당 검증 가능한 주장 수"**다. 비우승작의 483단어는 전부 일반론이었다.
- **영상 길이가 가장 선명한 신호**다. 우승작은 2:00~3:30에 몰려 있고, 비우승작에는 59초(설명 부족)와 807초·448초(심사위원이 끝까지 안 봄)가 섞여 있다.

**비우승작에서 반복된 실패 패턴 (실제 관찰)**
1. **태그라인이 카테고리 설명**: "Nexlytic unifies every marketing channel into a single AI-powered dashboard" — 누구를 위한 건지, 기존 도구 대비 뭐가 다른지 없음. 본문 447단어에 Built With는 `css` 하나.
2. **Live URL 부재 또는 깨짐**: Chronos AI는 Try it out 링크 자체가 없음. CXOS는 제품명과 무관한 `salesforce-metadata-catalog.vercel.app`으로 연결(심사위원 신뢰 즉사).
3. **섹션은 다 채웠는데 내용이 없음**: ChronoState AI는 "How we built it"·"Challenges"를 아예 비우고 299단어. 배포처가 `*.chatgpt.site`.
4. **영상이 8~13분**: AI-Powered OffboardCare는 2,287단어·11이미지·상세한 Phase별 타임라인으로 **문서 품질은 우승작급**이었으나 영상이 **13분 27초**. 수상 실패.
5. **영상이 1분 미만**: Chronos AI 59초 — "working product"를 입증할 시간이 없음.
6. **스코프 과다**: "Operating System" / "unifies every channel"류 플랫폼 선언. 우승작은 예외 없이 **하나의 워크플로**를 끝까지 판다.

---

## 4. 종합 패턴

### 4-1. 1~2일에 달성 가능한 현실적 스코프
표본상 **1일 대회(AGI×Lovable, 132명)의 우승 스코프**는: 단일 워크플로 + 에이전트 3~7개 또는 파이프라인 3~4단계 + 배포된 웹앱 + GitHub + 2분 영상. (warmscreen: 474단어, 영상 1:59)

마감 하루 전 기준 권장 스코프:
- **핵심 유저 여정 1개**를 로그인→작업→결과까지 끊김 없이. 나머지는 과감히 잘라내고 글에 "다음 단계"로 배치.
- 제품 표면 3~5화면. Klinva처럼 **역할 기반 뷰**가 있으면 "진짜 업무 도구"로 보인다.
- 반드시 포함해야 값이 오르는 것: **공개 URL / 시드 데모 데이터 / 결제(Stripe 테스트 모드라도) / 공개 repo + README**.
- 기술 차별점은 **딱 하나**를 깊게. Waylo의 4계층 캐스케이드, Province의 zero-manual form mapping, Sentinel의 "reviewer, not author" 제약처럼.

### 4-2. "Technical Implementation(25%)"에서 심사위원이 보상하는 것
관찰된 공통 요소, 빈도순:
1. **아키텍처 다이어그램 또는 계층 서술** — 어떤 단계에 LLM을 쓰고 어디는 결정론적으로 처리했는지. (Sentinel, Waylo, Province, TradeWizard 전원)
2. **비용·레이턴시 숫자** — "~5ms, free / ~800ms, paid", "0.92 similarity threshold", "~100ms", "2 RPM rate limit". 숫자는 "실제로 돌려봤다"의 증거다.
3. **LLM의 권한 제한** — "it's a reviewer, not an author", "host-validated: can't cite a line of code that doesn't exist", confirm-before-speak. **AI wrapper가 아님을 증명하는 가장 강한 수단**.
4. **실패 모드 문서화** — "What happens when a recommendation is wrong", HITL 승인 게이트, 가드레일.
5. **진짜 막힌 지점을 Challenges에 솔직히** — 우승작은 예외 없이 구체적 실패담(Bedrock 2 RPM, Supabase 함수 슬립, Maestro canvas v20 크래시)을 쓴다. 비우승작은 "시간이 부족했다" 수준.
6. **표준 준수/통합** — SARIF 2.1.0, OWASP Agentic Top 10, MITRE ATLAS, GitHub Action. 심사위원(특히 AWS/Microsoft 엔지니어)이 즉시 알아보는 신호.

### 4-3. "Problem Solving & Impact(25%)"에서 심사위원이 보상하는 것
1. **수치화된 문제**: "48 million Americans get sick from food every year", "CPAs charging $300-500+", "over half of children with cerebral palsy".
2. **명명된 경쟁사 + 1문장 차별점**: "Existing tools like Voiceitt ask users to record 50+ phrases. We work from the first sentence."
3. **실사용/검증 증거**(가장 강력, 순서대로):
   실매출·유저수(Payout $30,017 / 17,000 users) > 실운영(veTriage "routine use in one day") > LOI·파트너십(Park Pal PMI Arka) > 고객 인터뷰 수(Park Pal 260+ surveys) > 스토어 배포(Gurwi 3채널, Weight Coach TestFlight) > 라이브 URL.
4. **TAM 계산 한 줄**: Klinva의 "150,000 companies × 10% = multi-million".
5. **초니치 타깃**: "상업용 청소업체 CRM", "영화·미디어 현지화", "수의과 전화 트리아지". 범용 플랫폼은 전부 비우승 쪽에 있다.

### 4-4. Devpost 글 구조 — 검증된 템플릿
Devpost 기본 7섹션(Inspiration / What it does / How we built it / Challenges / Accomplishments / What we learned / What's next)이 **우승작의 다수(38건 중 27건)**가 쓴 포맷이다. 안전하다. 다만 상위 수상작은 **여기에 한 가지를 더한다**:
- GraphFlow → "**Why This Is Different**" 섹션 신설
- TradeWizard → "AI Architecture Explanation", "Responsible AI Guardrail", "Hallucination resistance"
- AgentShell → "📊 Impact & Value", "Measurable Impact", "Reproducibility"
- Park Pal → 아예 PM 언어로 재구성: "What we built / **Who it's for** / **What makes it distinctly ours**"
- Province → "How we built it" 아래에 번호 붙인 기술 하위 섹션 4개

권장: **기본 7섹션 유지 + "Why this is different" + "Architecture" + "Who it's for / Business model" 3개 추가.**
이미지는 3~6장이면 충분하되, **첫 장은 반드시 제품 스크린샷**(랜딩 페이지 아님). GIF는 필수 아님.
"What's next"는 우승작 29/38이 작성 — **Klinva·Payout·Gurwi처럼 시장·과금·월별 로드맵을 쓸 것.** "더 많은 기능 추가" 같은 문장은 무의미.

### 4-5. 데모 영상 — 우승 공식
- **길이: 2분 30초 ~ 3분 30초.** 5분 제한이지만 우승작 중앙값은 2분 54초. 5분을 채우지 마라.
- 검증된 구조(우승작 다수 공통):
  1. **0:00–0:20 훅** — 개인적 일화 또는 충격적 수치 1문장. (Waylo: "My grandmother calls me every week...")
  2. **0:20–0:45 문제 + 기존 대안의 실패** — 경쟁사 실명 언급이 효과적.
  3. **0:45–2:15 라이브 데모** — 영상의 **60% 이상**. 슬라이드가 아니라 화면. 실제 입력 → 실제 출력. 편집으로 대기 시간만 잘라낼 것.
  4. **2:15–2:45 아키텍처 1장** — 어디에 LLM이 들어가고 어디가 결정론적인지 한 슬라이드.
  5. **2:45–3:00 클로즈** — 타깃 유저 / 과금 / 다음 단계 한 문장씩 + 라이브 URL 자막.
- **얼굴 출연**: 표본에서 강제 요소는 아니나, 도메인 전문가가 자기 문제를 말할 때(veTriage 수의사, Park Pal 창업자) 신뢰도가 뚜렷이 올라간다. **오프닝 10초만 얼굴, 나머지는 화면 녹화 + 보이스오버**가 최적.
- 반드시 피할 것: 무음 화면 녹화, 12분짜리 전체 투어, 로딩 스피너를 그대로 보여주기, 슬라이드만 보여주고 제품을 안 보여주기.
- Gauntlet의 교훈: **"미리 녹화된 게 아니다"를 명시적으로 말하라.** 심사위원의 첫 의심은 항상 "이거 진짜 돌아가나?"이다.

### 4-6. 관찰된 기술 스택 표준 (2025–2026 우승작)
- **프론트/호스팅**: Next.js + Vercel (압도적 1위), 또는 React + Vite + Netlify. UI는 Tailwind + shadcn/ui.
- **DB/Auth**: **Supabase**(Postgres + auth + storage 한 방)가 사실상 표준. 대안: Clerk(auth) + Postgres, AWS Aurora/DynamoDB.
- **결제**: **Stripe**. SaaS 트랙에서 Stripe 태그 유무가 "prototype vs business"를 가른다 (Tailored Labs, KeyHaven, Park Pal 모두 Stripe).
- **LLM**: 스폰서 종속 없는 대회에서는 **OpenRouter로 멀티 프로바이더**(ModelMash) 또는 Claude/GPT 혼용(Tailored Labs: "GPT-4/Claude Opus"). 벡터: **pgvector**.
- **부가 신호**: Resend(트랜잭션 메일), Mixpanel/PostHog(분석), Twilio/ElevenLabs(음성).
- **빌드 도구 자체를 글에 밝히는 것이 유리**: Claude Code / Codex / Cursor / v0 / Bolt 사용을 당당히 적은 우승작 다수(Payout "not one line of code written by hand", Gauntlet "Built entirely with Claude Code", Park Pal "v0 + Claude Code"). 감점 요인이 아니라 **속도의 증거**로 읽힌다.

### 4-7. 흔한 실수 총정리
1. 영상 5분 채우기 / 8분 넘기기 → 심사위원 이탈.
2. Try it out 링크가 없거나, 깨졌거나, 프로젝트와 다른 제품으로 연결.
3. 로그인 벽 뒤에 데모를 두고 테스트 계정을 안 줌 → **데모 계정 또는 `?demo=` 파라미터를 반드시 제공**(Tailored Labs 사례).
4. 태그라인이 "AI-powered platform that unifies X" 류의 카테고리 설명.
5. 타깃 유저가 "everyone".
6. 비즈니스 모델 문장이 아예 없음 — **Best SaaS Product $4,000 트랙에서는 치명적**.
7. GitHub repo가 비어 있거나 README가 없음(우리 대회는 문서·셋업 가이드를 명시 요구).
8. Challenges에 "시간 부족" 같은 일반론.
9. 10슬라이드 덱 미제출(요건 위반 → 실격 리스크).
10. "AI wrapper" — 프롬프트 한 번 던지고 끝. 대회 소개문이 직접 배제한 유형이다.

---

## 우승 패턴 체크리스트

> 마감 전 이 목록을 한 줄씩 지워라. `[필수]`는 하나라도 빠지면 상위권 탈락.

### A. 제품 (Working Product)
- [ ] **[필수]** 인증 없이(또는 데모 계정 제공으로) 즉시 접근 가능한 **공개 URL**. 마감 직전 다른 브라우저·시크릿 모드에서 실제로 열어볼 것.
- [ ] **[필수]** 핵심 유저 여정 **1개**가 처음부터 끝까지 끊기지 않음. 반쯤 된 기능 5개보다 완결된 기능 1개.
- [ ] 심사위원이 바로 결과를 볼 수 있도록 **시드 데이터 주입** (빈 대시보드 금지).
- [ ] 로딩 상태·에러 상태 처리 (심사위원 앞에서 스피너가 멈추면 끝).
- [ ] 모바일 폭(≈400px)에서 레이아웃 깨지지 않음 (UX 15%).
- [ ] SaaS 트랙 노리면 **Stripe 결제 화면**(테스트 모드 가능) + 가격 티어 페이지.

### B. Devpost 글
- [ ] **[필수]** 태그라인 1문장 = **누구를 위해 + 무엇을 + 기존 대비 왜 다른가**. "AI-powered platform" 금지.
- [ ] 첫 문단에 **수치화된 문제** 또는 개인적 일화.
- [ ] **명명된 경쟁/대안 + 1문장 차별점** 한 줄.
- [ ] 표준 7섹션(Inspiration / What it does / How we built it / Challenges / Accomplishments / What we learned / What's next).
- [ ] **+ "Why this is different"** 섹션 추가.
- [ ] **+ "Architecture"** 섹션 — 계층별로 무엇이 LLM이고 무엇이 결정론적인지. **레이턴시·비용 숫자 최소 3개**.
- [ ] **+ "Who it's for / Business model"** 섹션 — 타깃 페르소나 + 가격 + **TAM 한 줄 계산**.
- [ ] **LLM 권한 제한 문장** 1개 이상 ("모델은 X를 할 수 없고, Y만 한다").
- [ ] **실패 모드** 문장 1개 ("추천이 틀리면 어떻게 되는가", HITL 게이트).
- [ ] Challenges에 **구체적 고유명사 실패담** 2개 이상 (레이트리밋 수치, 라이브러리 버그 등). "시간 부족" 금지.
- [ ] 검증 증거 — 가능한 가장 높은 등급 하나: 매출 > 실사용 > LOI > 인터뷰 N명 > 스토어 배포 > 라이브 URL. **숫자로**.
- [ ] What's next = 시장 확장 + 과금 + 다음 마일스톤 (기능 나열 금지).
- [ ] 이미지 **3~6장**, 첫 장은 제품 화면. 랜딩 페이지 목업 아님.
- [ ] 분량 목표 **900~1,600단어**. (짧아도 되지만 문장마다 검증 가능한 주장이 있어야 함)
- [ ] Built With 태그에 실제 스택 전부 입력 (심사위원 필터링에 쓰임).

### C. 데모 영상 (5분 제한 / 목표 2:45)
- [ ] **[필수]** 길이 **2분 30초 ~ 3분 30초**.
- [ ] 0:00–0:20 훅 (일화 or 수치).
- [ ] 0:20–0:45 문제 + 기존 대안이 실패하는 이유.
- [ ] 0:45–2:15 **라이브 화면 데모**(영상의 60%+). 실제 입력 → 실제 출력. 대기 시간은 컷.
- [ ] 2:15–2:45 아키텍처 1슬라이드 + **AI의 역할** 명시 (대회 요건).
- [ ] 2:45–3:00 타깃 유저 / 과금 / 다음 단계 + 라이브 URL 자막.
- [ ] 오프닝 10초 얼굴 출연(도메인 배경 있으면 특히).
- [ ] "이 데모는 사전 녹화가 아니라 실제로 도는 것" 명시.
- [ ] 자막 또는 또렷한 보이스오버. 무음 녹화 금지.
- [ ] YouTube **공개 또는 일부 공개**로 업로드 확인 (비공개면 심사 불가 = 실격).

### D. 코드 & 덱 (대회 명시 요건)
- [ ] **[필수]** **공개** GitHub repo. 마감 후 private 전환 금지.
- [ ] **[필수]** README: 한 줄 소개 / 스크린샷 / 아키텍처 다이어그램 / `.env.example` / 로컬 실행 3~5 커맨드 / 라이브 URL / 데모 영상 링크.
- [ ] 시크릿 커밋 안 됨 (보안 배경 심사위원 다수).
- [ ] 커밋 히스토리가 존재 (단일 "initial commit" 덤프 지양).
- [ ] **[필수]** **10슬라이드 이하 덱**, 요구 8항목 전부: Problem / Solution / Target Users / Product Features / **Technical Architecture** / AI Technologies Used / Impact & Value Proposition / **Future Roadmap**.
- [ ] 덱은 공개 링크(Google Slides "링크가 있는 모든 사용자" 또는 PDF)로 접근 확인.

### E. 마감 직전 최종 점검
- [ ] 시크릿 창에서 라이브 URL·영상·GitHub·덱 4개 링크 전부 열어봄.
- [ ] Devpost 제출 폼의 5개 요건 전부 채움.
- [ ] 태그라인을 소리 내어 읽었을 때 **"내일 당장 쓰겠다"**는 반응이 나오는가. (대회 공식 문구: "I would use this tomorrow")

---

## 출처

**대회 페이지**
- https://ai-builders-hackathon-2026.devpost.com/ (본 대회 — 심사 기준·제출 요건·상금·심사위원)
- https://worldslargesthackathon.devpost.com/ · https://revenuecat-shipaton-2025.devpost.com/ · https://openai.devpost.com/ · https://h01.devpost.com/ · https://aws-agent-hackathon.devpost.com/ · https://openai2025.devpost.com/ · https://uipath-agenthack.devpost.com/ · https://mindtheproduct.devpost.com/ · https://usaii-global-ai-hackathon-2026.devpost.com/ · https://vibe-a-thon.devpost.com/ · https://maximally-makeathon-2025.devpost.com/ · https://wixsaas.devpost.com/ · https://agi-real.devpost.com/ · https://fetch-ai-hackathon.devpost.com/ · https://accel-anthropic-ai-dev-day.devpost.com/

**우승 프로젝트**
- https://devpost.com/software/civilink (Tailored Labs, Grand Prize)
- https://devpost.com/software/weight-coach (Weight Coach, 2nd)
- https://devpost.com/software/keyhaven (KeyHaven, 3rd)
- https://devpost.com/software/klinva-ultimate-crm-saas-for-commercial-cleaning-companies (Klinva, 4th)
- https://devpost.com/software/callvance (CallVance, 6th + Startup Challenge)
- https://devpost.com/software/modelmash-find-the-perfect-llm (ModelMash, 7th + Most Likely to Get Funded)
- https://devpost.com/software/solarscope (SolarScope, EMEA)
- https://devpost.com/software/startsnap-fun (startsnap.fun)
- https://devpost.com/software/payout-cwdniv (Payout, Shipaton Grand Prize)
- https://devpost.com/software/gurwi-learn-anything (Gurwi, Shipaton 1st #BuildInPublic)
- https://devpost.com/software/voicetree (Voicetree, Shipaton 2nd)
- https://devpost.com/software/second-voice-uk1peq (Second Voice, OpenAI 1st)
- https://devpost.com/software/veterinary-four-color-triage-app (veTriage, OpenAI 1st)
- https://devpost.com/software/pulse-ewjaf9 (Pulse, OpenAI 2nd)
- https://devpost.com/software/sentinel-way5bd (Sentinel, OpenAI 2nd Dev Tools)
- https://devpost.com/software/fdvnjvd (Waylo, H0 1st B2C)
- https://devpost.com/software/tradewizard-8xp61z (TradeWizard, H0 2nd B2C)
- https://devpost.com/software/mnema (Mnema, H0 2nd B2B)
- https://devpost.com/software/graphflow-release-safety-intelligence (GraphFlow, H0 2nd Open)
- https://devpost.com/software/syntact-23l7ei (Syntact, H0 3rd Open)
- https://devpost.com/software/province (Province, AWS 3rd)
- https://devpost.com/software/aegisagent-an-insurance-claim-app-fully-developed-by-kiro (AegisAgent, AWS 2nd)
- https://devpost.com/software/oratio-merd5o (Oratio, AWS Best Bedrock)
- https://devpost.com/software/agent-shell (AgentShell, AWS Best Strands)
- https://devpost.com/software/ai-driven-multi-agent-fraud-alert-triage-system (AWS Best AgentCore)
- https://devpost.com/software/gauntlet-go-safe-or-go-home (Gauntlet, UiPath Grand Prize)
- https://devpost.com/software/penetron (Penetron, UiPath)
- https://devpost.com/software/zeroday (SpectreAI, UiPath Best Maestro BPMN)
- https://devpost.com/software/park-pal-wbgqmk (Park Pal, MTP GOLD)
- https://devpost.com/software/postmortem (PostMortem, MTP)
- https://devpost.com/software/brandiq-0r4wxa (BrandIQ, MTP)
- https://devpost.com/software/alyosha · https://devpost.com/software/wayfinder-1y4xbe · https://devpost.com/software/launchify · https://devpost.com/software/haven-dn65lq (USAII 2026)
- https://devpost.com/software/warmscreen · https://devpost.com/software/ux-ai-web-agent (AGI×OpenAI×Lovable)
- https://devpost.com/software/cost-vortex (Maximally Startup Makeathon)

**대조용 비우승작**
- https://devpost.com/software/cxos-agentic-customer-experience-operating-system · https://devpost.com/software/nexlytic · https://devpost.com/software/chronos-ai-e7y9ud · https://devpost.com/software/lingohan · https://devpost.com/software/socialaia · https://devpost.com/software/chronostate-ai · https://devpost.com/software/ai-powered-offboardcare · https://devpost.com/software/novafabric-flaky-detective
