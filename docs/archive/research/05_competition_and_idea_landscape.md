# 05. 경쟁 구도 · 시장 트렌드 · 아이디어 랜드스케이프

조사일: 2026-09-15 / 대상: **AI Builders Hackathon 2026** (Devpost)
마감: 2026-09-15 23:00 EDT · 참가자 3,403명 · 상금 풀 $33,900+

> 출처: https://ai-builders-hackathon-2026.devpost.com/

---

## 0. 먼저 확인해야 할 사실 정정 (Fact check)

의뢰 브리프와 Devpost 공식 페이지의 내용이 **다릅니다**. 제출 전략에 직접 영향을 주므로 먼저 정리합니다.

| 항목 | 브리프 가정 | Devpost 실제 기재 |
| --- | --- | --- |
| 심사 기준 | technical completeness 30 / PMF 30 / UX 20 / originality 20 | **Innovation & Creativity 20% · Technical Implementation 25% · Problem Solving & Impact 25% · User Experience & Design 15% · Presentation & Demo 15%** |
| 최고 상금 | Best SaaS $4,000 | Best SaaS Product **$4,000** (일치) |
| 참가 자격 | (미언급) | 페이지에 따라 기술이 엇갈림. 메인 페이지는 "Students only / 법적 성년 이상 / 기업·전문조직 제외", rules 페이지는 "학생 및 최근 졸업자, 개발자, AI/ML 실무자·연구자, 디자이너, 창업자" 로 더 넓게 기술. **제출 전 Discord 확인 필요.** |
| 제출물 | (미언급) | 제출 폼 + 동작하는 프로토타입 + **공개 GitHub 저장소** + 데모 영상(최대 5분) + 발표 덱(최대 10장) |
| 기간 | — | 2026-08-21 ~ 2026-09-15, 심사 2026-09-16~20 |

**전략적 함의 — 브리프 대비 배점 이동**
- `Presentation & Demo 15%` 가 **독립 배점**으로 존재합니다. 브리프에는 없던 항목이며, 데모 영상 + 10장 덱의 완성도가 총점의 1/7을 좌우합니다. 24시간 예산에서 **최소 3~4시간을 영상·덱에 배정**해야 합니다.
- `Technical Implementation 25% + Problem Solving & Impact 25% = 50%`. 즉 **"진짜 문제 × 진짜 구현"** 이 절반입니다. Originality는 20%로 상대적으로 낮으므로, **기발함보다 완성도·실사용 가능성**에 무게를 두는 편이 기대값이 높습니다.
- UX 비중이 브리프(20%)보다 낮은 **15%** 이나, Presentation 15%와 합치면 30%가 "보여지는 품질"입니다. 결국 **화면이 예뻐야 한다**는 결론은 동일합니다.

### 트랙 구조 (스폰서 NexFellow 기준)
오거나이저 업데이트에 따르면 NexFellow Fellowship 트랙이 4개로 구분됩니다:
**SaaS & Products / AI & Agents / Developer & Open Source / Web3 & Emerging Tech**
→ 목표인 *Best SaaS Product $4,000* 는 첫 번째 트랙과 정렬됩니다. **"에이전트 데모"가 아니라 "제품(SaaS)"으로 포지셔닝**해야 합니다. 가격표, 로그인, 멀티테넌시, 온보딩이 있어야 SaaS로 읽힙니다.

- 업데이트 원문: https://ai-builders-hackathon-2026.devpost.com/updates

---

## 1. 경쟁 스캔 (Competition scan)

### 1.1 결론: 본 대회 갤러리는 **아직 비공개**

- https://ai-builders-hackathon-2026.devpost.com/project-gallery
- https://ai-builders-hackathon-2026.devpost.com/submissions

두 URL 모두 *"The hackathon managers haven't published this gallery yet, but hang tight!"* 만 반환합니다.
참가자 목록(`/participants`)도 로그인이 필요합니다. **마감 전 경쟁작 직접 조회는 불가능**합니다.

### 1.2 대체 표본: UC Berkeley AI Hackathon 2026

동일 시즌(2026)·동일 인재풀(북미 학생/AI 빌더)·동일 툴체인(Claude, Redis, ElevenLabs, Deepgram 스폰서)을 가진 **400개 프로젝트 공개 갤러리**를 프록시로 사용했습니다.
본 조사에서 **17페이지 중 13페이지, 약 310개 프로젝트**의 이름·태그라인·좋아요를 수집했습니다.

- 갤러리: https://ai-hackathon-2026.devpost.com/project-gallery

> 주의: 완전한 대체재는 아닙니다. Berkeley 쪽은 로보틱스/하드웨어 스폰서 비중이 커서 물리 AI 프로젝트가 과대표집되어 있습니다. 반대로 AI Builders는 "SaaS & Products" 트랙이 명시되어 있어 **B2B SaaS 비중이 더 높을 것**으로 보정해서 읽어야 합니다.

### 1.3 테마 클러스터링 (수집 표본 ~310개 기준)

| # | 클러스터 | 대략 비중 | 대표 프로젝트 | 포화도 |
| --- | --- | --- | --- | --- |
| 1 | **에이전트 인프라 · 관측 · 메모리 · 컨텍스트 압축** | ~13% | Quad(38❤ 최다), Accordion, Re:Compress, TokenC, BrowserDelta(-78% 컨텍스트), Mimic($1.55→$0.06), RAVEN(-80~90% 토큰), engram, Shepherd, Promptetheus, GlassBox, Redundant, ContextMaster, The Memory Pod, Precedent, IMMUNE, Beacon | 🔴 **극포화** |
| 2 | **헬스케어 · 임상** | ~11% | Scribe(닥터 번아웃), MedRAG, ReferralGuard(사전승인 거절), Interim, Cadence(고위험 임신), scanOTiC, DoseDNA, SonoXR, Fetch Health, CareLoop, Workbench, Phagentic, RecoverAI | 🔴 **극포화** |
| 3 | **재난 · 응급 · 911 디스패치** | ~8% | SIREN, Dispatch AI, Aegis, FirstResponder-Relay, Lifeline AI, CrisisRoom, Nos(구급 코파일럿), RELAY, baymax, Fireflai, Ember, Lighthouse, TrailAid, 311.ai | 🔴 **극포화** (지역 재난 뉴스 영향) |
| 4 | **교육 · 튜터 · 학습** | ~9% | StoryLearn AI, VibeProf, GBTutor, Tiruno, CurricuLearn, AttentionRetention, Retention, Pathwise, Triad, prism, Langtour, Uni Pilot, ClassPilot | 🔴 **극포화** |
| 5 | **로보틱스 · 피지컬 AI · 하드웨어** | ~12% | StudForge, Omniscient, AxisGen, Topo, GroundTruth, Ghost Fighter, Infer, Plantcasso, Saffron, Etch, Tracer, PinPal, SiliconYOLO, Radical, Diffusion Accelerator | 🟠 포화 (단 24h 솔로 난이도 높음) |
| 6 | **접근성 (시각·청각·언어 장애)** | ~7% | Lucid Voice, BrailleAI, Daisy, Tactus, CupVoice, SignCast, Phone With Hands, BirdBox.ai, VoxAid, MatchVision, KindCursor | 🟠 포화 |
| 7 | **AI 보안 · 레드팀 · 에이전트 안전** | ~6% | Sentinel, Riposte, Gauntlet(Team Spartan), SIFT Guardian, Agent Immunity, BrowseCheck, AI/CD, ShadowGuard-AI, MantleGuard, WatchTower AI | 🟠 포화, 단 **기술 깊이 점수 높음** |
| 8 | **개발자 도구 · QA · 코딩 에이전트** | ~6% | FlowProof(16❤), Inspector, Canary, Triage, Refactorika, GitIntent, UserSwarm, Signoff, BuildProof, Quant-Code | 🟠 포화 |
| 9 | **시민 인프라 · 정부 · 건설** | ~6% | Sivie(포트홀), SafeStreets, FirstPass(인허가), Constructa, ZoneGuard, Dwell, UrbanPilot, Open Door, Foreman(시공 인보이스), Finding the Lost Wells | 🟡 중간 |
| 10 | **소비자 재미 · 게임 · 메모리** | ~8% | Rem(15❤, 사진→3D), MOGGIE(8❤), Séance, Re:Dream, Glimpse, Neural Arcade, ClaudeDJ, Eve, Debate RPG, recapsule, Dream Book | 🟡 중간 (SaaS 트랙과 무관) |
| 11 | **연구 에이전트 · 팩트체크** | ~5% | AlphaResearch, ASET, Faultline, AnchorPoint, BASKR, Continuum, Fact Check, RhetoriQ, AgentDex | 🟡 중간 |
| 12 | **고령자 · 스캠 방지 · 가족 케어** | ~4% | AIntercept, STING, Lighthouse, Kindred, My Friend, Tendly, Recall | 🟡 중간 |
| 13 | **커머스 · 리셀 · 마케팅** | ~4% | TreasureLens AI, Traide, RESELLER., Bang4YourBuck, Lumen, Marquee, DemoAgent, Meridian | 🟢 얕음 |
| 14 | **핀테크 · 투자** | ~3% | WalletOS, AI Hedge Fund, Captain Ddoski, CommunityLend, MoneyPenny, DeepDrive | 🟢 얕음 |
| 15 | **농업 · 환경** | ~3% | AgroMind, Acre, HiveSense, Offline AI Farming Advisor, Foodprint | 🟢 얕음 |

### 1.4 관찰: **좋아요가 몰리는 곳 = 정량 수치를 내건 인프라 프로젝트**

표본 내 최다 좋아요 프로젝트를 보면 패턴이 뚜렷합니다.

| 프로젝트 | ❤ | 태그라인의 공통점 |
| --- | --- | --- |
| Quad | 38 | "Knowledge infrastructure for every agent" |
| FlowProof | 16 | "persona-based AI browser agents across website flows" |
| Rem | 15 | 사진 → 3D 씬 (시각적 임팩트) |
| Mimic | 11 | **"$1.55 → $0.06 per run"** |
| FormBridge | 8 | 이민자 가족 영어 서식 (Chrome 확장) |
| Promptetheus | 7 | "trace runs, catch silent failures, replay the bad step" |
| BrowserDelta | 5 | **"cuts browser-agent context by ~78%"** |

→ **교훈 1**: 태그라인에 **숫자(before→after)** 를 박은 프로젝트가 일관되게 상위. 데모 영상 첫 10초에 숫자를 띄워야 합니다.
→ **교훈 2**: "누구를 돕는다"보다 "무엇을 몇 % 줄인다"가 강합니다.
→ **교훈 3**: 시각적으로 즉시 이해되는 결과물(3D, 대시보드, 리플레이)이 좋아요를 받습니다.

### 1.5 **비어 있는 니치 (Whitespace)** — 가장 중요한 발견

310개 표본에서 **거의 0건**이었던 카테고리들입니다. 그리고 공교롭게도 **실제 B2B SaaS 시장에서 돈이 가장 많이 도는 영역**과 일치합니다.

| 비어 있는 영역 | 표본 내 건수 | 왜 비어 있나 | 왜 "Best SaaS"에 유리한가 |
| --- | --- | --- | --- |
| **법무 · 계약서 리뷰/협상** | 0건 | 학생에게 낯선 도메인 | 명백한 유료 시장, ACV 높음 |
| **컴플라이언스 · SOC 2 · 감사 증적** | 0건 | 지루해 보임 | 반복 매출의 교과서. "SaaS"로 즉시 읽힘 |
| **HR · 채용 · 온보딩 · 성과관리** | 1건(HirED) | — | 모든 회사가 산다 |
| **세일즈/RevOps · CRM 위생 · 파이프라인** | 1건(Meridian) | 학생이 겪어본 적 없는 고통 | 가장 명확한 ROI 스토리 |
| **회계 · 청구 · 수익 인식** | 1건(Foreman, 시공 한정) | — | 돈을 직접 만짐 = 임팩트 설명 쉬움 |
| **고객지원 티켓 처리 / 디플렉션** | **0건** | "너무 뻔하다"고 다들 회피 | 오히려 역설적 기회 |
| **데이터/BI 운영 (dbt, 시맨틱 레이어, 데이터 품질)** | 1건(datalab-ai) | — | 기술 깊이 어필 용이 |
| **다국어 현지화 · i18n 운영** | 0건 | — | 한국 팀의 구조적 강점 |
| **AI 비용 거버넌스 · FinOps** | 1건(GridMind) | — | 2026년 CFO 최우선 관심사 |
| **조달 · 벤더 심사 · 보안설문(SIG/CAIQ) 자동화** | 0건 | 도메인 인지 부족 | 고통이 극심하고 자동화 적합도 최상 |
| **보험 · 청구 심사 (헬스 외)** | 0건 | — | — |
| **프로덕트 애널리틱스 · 실험 설계** | 0건 | — | — |

**전략 결론**
> 포화 구역(에이전트 인프라 / 헬스 / 재난 / 교육)을 피하고, **"지루하지만 돈이 되는 백오피스 B2B"** 중 하나를 골라 **완성도 높은 SaaS 껍데기(인증·팀·요금제·대시보드)** 를 씌우는 것이 *Best SaaS Product $4,000* 에 대한 최적 전략입니다.
> 단, Originality 20%를 방어하기 위해 **기술적 훅(예: 결정론적 검증 루프, 브라우저 에이전트, 증적 그래프)** 을 하나 반드시 심어야 합니다.

---

## 2. 시장 트렌드 스캔 (2026-08 ~ 2026-09)

> 조사 방법: TechCrunch, Product Hunt 리더보드(2026-08 월간 / week 36), Y Combinator RFS, Hacker News Algolia(Show HN 150pt+), Sequoia/Menlo/Bessemer 자료, 펀딩 트래커 교차 확인. 1차 출처로 확인된 건과 2차 집계 사이트만 있는 건을 구분해 표기했습니다.

### 2.1 뜨거운 카테고리 15선

#### ① 에이전트 보안 · 거버넌스 (Agent Security & Governance)
- **AIR** — 사내 에이전트를 자동 발견하고, 에이전트가 끌어오는 skill/plugin/**MCP 서버**를 심사·차단. 발견한 애드온의 약 27%를 위험으로 필터링. **2026-09-01 총 $50M 발표** (시드 ~$10M Sequoia, $40M Greenoaks). 고객 20곳 이상.
  https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/
- **Zenity** — 런타임에서 의도를 벗어난 에이전트 행동을 차단. **2026-08 Series C $125M** (Norwest 리드).
- **Obsidian Security** — 비인간 ID(NHI) + 서드파티 SaaS 에이전트 보안. **2026-08 Series D $85M**.
- **Alice (구 ActiveFence)** — ARR ~$100M, 주요 모델 랩 10곳 중 8곳이 고객. **$140M** (Apax Digital 리드).
  https://forkast.news/enterprise-ai-agent-funding-surges-to-435m-in-five-months-security-and-governance-lead/

**Why now**: 2026-04~09 5개월간 12건 $435M, 그중 9건이 순수 에이전트 보안. 병목이 "모델 성능"에서 "거버넌스 승인"으로 이동. 에이전트 이니셔티브를 가진 기업의 **88%가 프로덕션 배포에 실패**(IDC/Lenovo 인용), Gartner는 2027년 말까지 에이전트 프로젝트의 40% 이상이 취소될 것으로 전망.
**혼잡도**: 경계(perimeter) 방어는 이미 혼잡 — Noma Security, Astrix, Operant AI가 직접 경쟁. **빈 곳: MCP 서버/스킬의 공급망 심사, 그리고 에이전트 행동의 사후 포렌식·귀속(attribution).**

#### ② AI 네이티브 컴플라이언스 · 규제 에이전트
- **Norm Ai** — 규제를 실행 가능한 에이전트로 컴파일. M365 Copilot 옆에서 누락된 고지·정책 충돌을 감지하고 감사 증적을 남기는 에이전트를 2026-05 출시. **2026-07-07 Series C $120M, 밸류 $1.2B** (Khosla 리드, Blackstone·BCV·Coatue 참여). 고객 운용자산 합계 $30T 이상.
  https://www.lawnext.com/2026/07/norm-ai-hits-unicorn-status-with-120m-series-c-at-1-2-billion-valuation.html
- **YC가 명시적으로 요청**: RFS "AI-Native Compliance Infrastructure". https://www.ycombinator.com/rfs

**Why now (본 해커톤에 가장 중요)**:
- **EU AI Act Article 50 투명성 의무가 2026-08-02 발효**. 챗봇의 기계 신원 고지, AI 생성 콘텐츠 마킹, 딥페이크·AI 작성 뉴스 라벨링, 감정인식/생체분류 고지. **과징금 최대 €15M 또는 전세계 매출 3%**.
  https://artificialintelligenceact.eu/transparency-rules-article-50/
- 2026-08-02 이전 출시된 시스템에는 **2026-12-02까지 유예기간**. → **지금이 정확히 그 유예 창(window) 한가운데**입니다.
  https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article-50-transparency-20260729/
- 반면 고위험(Annex III) 의무는 Digital Omnibus(2026-07-27 발효)로 **2027-12-02로 연기**. 즉 단기 구매 트리거는 **라벨링/투명성**이고, 고위험은 예산만 잡히는 단계.
  https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines/

**혼잡도**: Norm Ai가 금융 컴플라이언스를 독주. **빈 곳: 비금융 규제 버티컬(의료기기, 채용, 교육), 그리고 Article 50 라벨링 자체.**

#### ③ 규제 산업 버티컬 에이전트 (법률·의료·보험·건설)
- **Harvey** — 2026-05 기준 ARR $300M. **2026-03-25 Series G $200M, 밸류 $11B** (GIC·Sequoia 공동 리드).
- **Legora** — **2026-03-10 $550M, 밸류 $5.55B** (Accel 리드).
- **HappyRobot** — 물류 음성/이메일/문서 에이전트. **2026-08 Series C $150M**.
- **Corgi Insurance** — AI 네이티브 보험사, $108M.

**Why now**: 2026-07까지 12개월간 버티컬 AI 73건 $3.07B. $50M 초과 라운드는 17건뿐인데 자본의 **61%**를 가져감 → 투자자는 "유연한 에이전트"가 아니라 **ROI가 증명된 좁은 에이전트**에 돈을 냄.
https://pulseline.substack.com/p/the-18b-agent-wave-why-vertical-ai
**혼잡도**: 법률은 상위가 닫힘(2026년 16건 ~$1B). 의료는 건수는 많지만(25건) 자본 점유율이 56.7%→27.1%로 하락 = 소액 다수 = **진입 여지 있음**. 숫자상 진짜 빈 곳: **부동산**(1건→8건/$228M), **건설**(6건/$119M), **보험**(3건/$146M).

#### ④ 앰비언트 임상 AI → 수익주기(RCM)·사전승인
- **Abridge** — 진료기록 작성에서 벗어나 코딩·RCM·**실시간 사전승인**(Availity 제휴, 2026-01 발표)으로 확장.
- **Ambience Healthcare** — 문서화 + 코딩 + CDI를 "수익주기 성과"로 리포지셔닝.
- **R1이 Humata Health(사전승인 자동화) 인수 합의** — 기존 RCM 강자가 AI 레이어를 사들임.
  https://www.marketscale.com/industries/healthcare/ambient-ai-is-moving-from-clinician-productivity-to-consent-and-revenue-cycle-controls

**Why now**: 세일즈 피치가 "의사 시간 절약"(이미 가격 압박)에서 **"회수한 달러"**(CFO 라인 아이템)로 이동.
**혼잡도**: 순수 전사(transcription)는 단독 제품으로 사망. **빈 곳: 지불자(payer) 측, 거절 항소(denial appeal) 에이전트.**
> ⚠️ 해커톤 관점: 헬스케어는 프록시 갤러리에서도 **극포화**. 피하는 것을 권장.

#### ⑤ 에이전트 런타임 인프라 (샌드박스 · 실행 · 오케스트레이션)
- **Modal** — **2026-05 $355M, 밸류 $4.65B**, ARR ~$300M.
- **E2B** — Firecracker microVM, 콜드스타트 ~150ms, **누적 10억 샌드박스 기동**, Fortune 100의 94%가 사용.
- **Daytona** — 콜드스타트 100ms 미만, **2026-02 Series A $24M**.
- **Naïve** — 샌드박스+라우팅+메모리+오케스트레이션, **2026-08 Series A $28.5M**.
  https://bex.co/blog/2026/09/11/ai-sandbox-funding-modal-daytona-e2b

**혼잡도**: 원시 실행 프리미티브는 상품화 진행(Vercel Sandbox, Fly Machines, Cloudflare 진입). **빈 곳: 며칠 단위 장기 실행(stateful long-horizon), 비용 귀속.**

#### ⑥ 멀티플레이어 / 협업형 에이전트 워크스페이스 ⭐ **가장 깨끗한 화이트스페이스**
- **YC RFS "Multiplayer AI"** (파트너 Aaron Epstein): "팀 누구나 같은 라이브 에이전트 세션에 들어올 수 있어야 한다." https://www.ycombinator.com/rfs
- **Grok Bot** — "진짜 일을 맡길 수 있는 AI 팀원", PH 2026-08 월간 7위(554표).
- **MagiCrew** — PH 2026-08.

**Why now**: 모델은 이미 되는데 **UX 공백**. 개발자의 **59%가 AI 코딩 툴 3개 이상을 동시에** 돌려 세션 파편화가 실생활 고통.
https://sourceryintel.com/reports/the-state-of-ai-coding-agents-2026
**혼잡도**: 펀딩된 카테고리 리더 없음 = **진짜 빈 곳**. 단 YC가 공개 지목했으므로 2개 배치 안에 혼잡해질 것.

#### ⑦ 배포·통합 에이전트 ("FDE를 없애라")
- **June** — 기존 엔터프라이즈 시스템을 스캔해 프로세스·병목을 매핑하고 에이전트 워크플로를 자동 구축. **2026-08-03 프리시드 $20M** (Marc Benioff의 Time Ventures 리드, Michael Dell·Aaron Levie·George Kurtz 참여).
  https://techcrunch.com/2026/08/03/a-marc-benioff-backed-startup-thinks-ai-can-solve-the-ai-deployment-problem/
- **Arga Labs** — Salesforce/Workday/이메일의 디지털 트윈에서 에이전트를 사전 테스트. **2026-08 $10M** (General Catalyst 리드).

**Why now**: 구매자 육성: CMG CSO Paul Akinmade — *"If your product requires FDEs, I don't want your product… I want an easy-to-use tool."*
**혼잡도**: 프리시드/시드 단계뿐 = 매우 이름. 리스크는 모델 랩의 서비스 조직이 같은 일을 함.

#### ⑧ AI 평가(Evals) · 관측성
- **Braintrust** — **2026-02 Series B $80M, 밸류 $800M** (ICONIQ 리드, a16z·Greylock·Elad Gil).
- **LangSmith** — 2026-03 Sandboxes 출시 + NVIDIA 제휴. **Langfuse / Arize** — OSS·MLOps 축.
- LLM 관측성 시장 **2026년 $2.69B → 2030년 $9.26B (CAGR 36.2%)**.
  https://www.marktechpost.com/2026/08/09/top-llm-observability-and-evaluation-platforms-in-2026-langfuse-langsmith-braintrust-arize-and-more-compared/

**혼잡도**: 개발자 툴 레이어는 혼잡. **빈 곳: 비엔지니어(도메인 전문가)가 채점하는 평가, 그리고 "평가 결과 = 컴플라이언스 증적"** (②와 직결).

#### ⑨ 음성 AI 에이전트
- **ElevenLabs** — **2026-06 ARR $600M**(2025년 말 $330M에서), 2026-02 Series D $500M, 밸류 $11B(Sequoia 리드). Fortune 500의 41%가 사용. https://sacra.com/c/elevenlabs/
- **Vapi** — **2026-05 Series B $50M, 밸류 ~$500M**. Amazon Ring이 40개 경쟁사 중 Vapi 선택.
  https://techcrunch.com/2026/05/12/vapi-hits-500m-valuation-as-amazon-ring-chose-its-ai-platform-over-40-rivals/
- **Decagon** — Series D $250M. **Dograh** — "오픈소스 VAPI 대안", PH 2026-08 5위(598표). **ThunderPhone** — 분당 2센트.

**혼잡도**: 🔴 **본 리포트에서 가장 혼잡**. Sierra, PolyAI, Bland, Retell, Decagon, ElevenLabs가 고객지원을 두고 난투. **빈 곳: 비영어권/비미국 규제 음성, 그리고 아웃바운드 규제 통화(추심, 사전승인, 클레임).**

#### ⑩ 에이전틱 커머스 · 에이전트 결제
- 2026년에 프로토콜 스택이 정착: **ACP**(OpenAI+Stripe), **UCP**(Google), **AP2**(Google+카드사), **MCP**(Anthropic), **A2A**, **Visa TAP**. AP2는 Intent/Cart/Payment Mandate를 W3C Verifiable Credentials로 정의.
  https://agenticplug.ai/current-state-of-agentic-commerce
- **Visa가 Stripe/Tempo의 Machine Payments Protocol로 카드 결제 개통**, Stripe는 Shared Payment Token을 Mastercard Agent Pay·Visa Intelligent Commerce와 Affirm/Klarna BNPL로 확장.
  https://www.pymnts.com/visa/2026/visa-scales-agentic-commerce-through-stripe-protocol-collaboration/
- **Salesforce**가 Stripe와 함께 ACP 지원 발표.

**핵심 수치(기회의 위치)**: 브라우저 기반 에이전트가 전체 에이전트 활동의 **약 71%**, 그중 이커머스 사이트가 **38.2%**를 받는데 **결제/체크아웃 경로에 닿는 건 3.16%뿐**. CAPTCHA·다단계 폼·3DS·주소검증이 전부 사람을 전제하기 때문.
https://agentlux.ai/blog/agentic-traffic-is-here-how-websites-should-prepare-for-ai-browsers-and-shopping-agents
**혼잡도**: 레일은 Stripe/Visa/Google 소유 — **거기 짓지 말 것**. **빈 곳: 머천트 측 에이전트 대응력(agent-readiness), 에이전트 사기·차지백 판정, 에이전트별 지출 한도.**

#### ⑪ AI 네이티브 서비스 롤업 ("툴이 아니라 일을 판다")
- **Thrive Holdings** — **2026-08 $2B+ 조달**(D1 Capital·Altimeter·SoftBank), 2026-08 두 번째로 큰 스타트업 라운드.
- **Current**(Thrive, OpenAI 제휴) — 2년간 $500M 인수 예산. **Multiplier** — $62.5M, 회계법인 8곳 인수.
- **General Catalyst Creation Fund** — AI 기반 롤업 전용 **$1.5B**로 확대.
- Sequoia 테제: 기업은 소프트웨어 $1당 서비스에 약 $6를 쓴다. 약 **$10T** 서비스 시장이 기계 처리 가능해짐. *"툴을 팔면 모델 개선이 당신을 상품화하고, 일을 팔면 모델 개선이 당신을 싸게 만든다."*
  https://sequoiacap.com/article/ai-in-2026-the-tale-of-two-ais/
> 해커톤에는 부적합(자본집약). 단 **피치 프레이밍**으로는 매우 유용 — "우리는 도구가 아니라 결과물을 판다".

#### ⑫ GEO / AI 검색 가시성 (Generative Engine Optimization)
- **Profound** — ChatGPT·Perplexity·Google AI Overviews·Copilot·Claude 전반의 브랜드 가시성 모니터링/최적화. **2026-02 Series C $96M, 밸류 $1B**(Lightspeed 리드). 18개월간 총 ~$155M. 월 1억 건 이상의 AI 검색 질의 처리.
  https://fortune.com/2026/02/24/exclusive-as-ai-threatens-search-profound-raises-96-million-to-help-brands-stay-visible/
- 관련 신호: **Chrome Lighthouse에 "Agentic Browsing" 카테고리와 llms.txt 감사 항목이 추가됨**. 단, GPTBot·ClaudeBot·PerplexityBot은 실제로는 /llms.txt를 거의 가져가지 않고 HTML을 직접 크롤함 — **llms.txt 단독 제품은 근거가 약함**.
  https://limy.ai/blog/llms-txt-in-2026-the-full-guide

**Why now**: 2026년 카테고리 중 드물게 **이미 예산 라인(SEO)이 존재**하고 그걸 잠식하면 됨.
**혼잡도**: 18개월 만에 리더가 나옴 = 제너럴리스트 자리는 사라짐. **빈 곳: 규제 버티컬 GEO(제약·금융, 주장 근거 입증 필요), 공급 측(퍼블리셔가 에이전트에 접근권을 가격 매기기).**

#### ⑬ 대중 시장 개인 AI 에이전트
- **Instinct** — 앱·기기에 연결되어 문자/전화로 작동. **2026-08-26 Series B $250M**(Index·Benchmark 공동 리드), **누적 $350M, 밸류 $2.5B**, 창업 1년, 창업자 23세. **"과도한 권한"과 ToS로 비판 받는 중**.
  https://techcrunch.com/2026/08/26/viral-ai-startup-instinct-has-raised-350-million-at-a-2-5-billion-valuation/
- **River AI** (Igor Babuschkin, ex-xAI 공동창업자) — **창업 2개월에 $1.1B** (General Catalyst·AMP PBC 리드, Nvidia·AMD Ventures·YC·Temasek).
  https://techcrunch.com/2026/08/11/general-catalyst-leads-1-1b-round-into-2-month-old-river-ai/
- **Hey Noah** — 창업자용 선제적 비서, **PH 2026-08 월간 1위(655표)**. **AirJelly** — 온디바이스 프라이빗 메모리.

**Why now**: YC RFS "AI-Powered Consumer Products for 1 Billion People".
**혼잡도**: 자본은 격렬하게 몰리지만 승자 없음. 2026-08~09의 차별점은 **프라이버시 포지션** — Instinct의 권한 백래시 vs AirJelly의 온디바이스.

#### ⑭ 인간 증명 · 딥페이크 방어 = 신뢰 인프라
- **YC RFS "Proving You're Human"** — 2026 Fall 명시 요청. https://explainx.ai/blog/yc-requests-for-startups-fall-2026
- **Phenom Fraud Detection Agent** — 라이브/녹화 면접에서 신원 일관성과 AI 생성 응답 패턴 분석.
- 반대편 증거: **JINKUSU CAM** — 은행·거래소의 원격 신원확인을 뚫기 위해 만들어진 라이브 딥페이크 도구.
  https://www.biometricupdate.com/202604/new-deepfake-tool-shows-why-face-alone-is-no-longer-proof-of-identity

**Why now (숫자가 강력)**: Deloitte 추정 미국 AI 기반 사기 손실 **2023년 $12.3B → 2027년 $40B**. 채용에서는 **채용담당자 62%가 "지원자가 HR이 잡을 수 있는 수준보다 잘 신원을 위조한다"**고 답했는데 **딥페이크 탐지를 배포한 곳은 31%뿐**. 대면 면접 요구가 2024년 5% → 2025년 30%로 **500% 급증**.
  https://www.biometricupdate.com/202608/why-deepfake-detection-is-becoming-trust-infrastructure
**혼잡도**: 기존 IDV(Jumio·Incode·Proof)가 기능으로 붙이는 중. **빈 곳: 채용/면접, 사내 커뮤니케이션(음성 복제 CFO 사기), 그리고 EU AI Act Art.50 라벨링용 콘텐츠 출처증명** — ②와 ⑭가 수렴 중.

#### ⑮ "스몰 소프트웨어" / 개인용 앱 빌더
- **x1** — "아이디어에서 App Store까지, 아이폰 앱을 위한 Lovable", PH 2026-08 9위(527표).
- **Lovable** — 밸류 ~$6.6B, 2025-11 ARR $206M. **Replit** — 밸류 $9B.
- **YC RFS "Small Software cloud"** — 에이전트가 만든 1인용·소팀용 툴의 배포/공유 레이어.

**혼잡도**: 수평적 웹 빌더는 잔혹하게 혼잡(Claude Code/Cursor와 직접 경쟁). **빈 곳: YC가 지목한 그대로 — 사용자 1명짜리 소프트웨어의 호스팅·공유 레이어.**

### 2.2 횡단 시프트 (피치에 반드시 반영할 것)

| 시프트 | 근거 |
| --- | --- |
| **좌석당 과금의 종말** | SaaS CEO 300명 설문(2026-04): **97%가 2년 내 좌석 기반 과금 폐지 계획**. 하이브리드(좌석+AI 크레딧)가 43%→연말 61%. 에이전트는 좌석이 필요 없음. ⚠️ Cruxy 설문은 1차 검증 실패, 방향성으로만 사용. https://www.getmonetizely.com/blogs/the-2026-guide-to-saas-ai-and-agentic-pricing-models |
| **성장 기준선** | Bessemer: "Supernovas"(1.5년 만에 ARR $100M, 리텐션 취약) vs "Shooting Stars"($3M→$100M 4년, 견고). AI 네이티브 중앙값 성장률 ~55%, 동일 ARR대 레거시 SaaS의 약 2배. https://www.bvp.com/atlas/the-state-of-ai-2025 |
| **지출 배경** | Menlo: 엔터프라이즈 genAI 지출 2023년 $1.7B → 2025년 $37B. 애플리케이션이 절반 이상($19B): 코딩/개발툴 $7.3B, 산업특화 $3.5B, 범용 코파일럿 $8.4B. a16z: 엔터프라이즈 **81%가 프로덕션에서 3개 이상 모델 패밀리를 오케스트레이션**(68%에서 상승). https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/ |
| **코딩 툴은 닫힌 카테고리** | Cursor ARR $2B 돌파(2026-03). **2026-08-14 SpaceX가 Anysphere를 $60B 전액 주식으로 인수 완료**, SpaceXAI로 편입 — 역대 최대 벤처 스타트업 인수. Claude Code 엔터프라이즈 점유율 ~54%(Menlo). Cognition $1B@$26B, Devin ARR $492M. **범용 코딩 어시스턴트는 절대 시작하지 말 것.** https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html |
| **주권 AI** | **Mistral 2026-09-08 €3B 조달, 포스트 밸류 €21B 초과**(Samsung 리드) — 유럽 테크 역대 최대 지분 라운드. 유럽 소버린 클라우드 지출 2025→2027 3배 전망($6.9B→$23.1B). https://techcrunch.com/2026/09/08/mistral-raises-e3b-as-sovereign-ai-becomes-big-business/ |
| **자본이 순수 소프트웨어를 떠남** | 2026-08 상위 10개 라운드: Databricks $5B, Thrive $2B+, Hadrian $1.37B, River AI $1.1B, Base Power $1B, Valar Atomics $1B, Castelion $1B, SpaceSail $1B, XPENG Robotics $900M+, Form Energy $750M — 대부분 에너지·방산·제조·로보틱스. 방산 테크만 2026년 **$14.6B** 돌파(2025년 기록 $9.6B 초과). |

### 2.3 의도적으로 제외한 영역 (혼잡/얇음/늦음)

| 영역 | 이유 |
| --- | --- |
| **AI SDR / 아웃바운드** | 11x(~$76M), Artisan(~$36M), Regie, Qualified, Agentforce, Clay(밸류 $7.1B)가 난투. **11x는 ARR 부풀리기와 가짜 로고 사용이 공개적으로 적발됨.** 상품화된 아웃리치는 제로를 향한 경주. |
| **범용 미팅 노트테이커** | Zoom/Teams/Granola 안에 무료로 내장됨. |
| **독립 제품으로서의 에이전트 메모리** | 고통은 진짜(엔터프라이즈 에이전트 실패의 65%가 모델이 아닌 컨텍스트 드리프트). 그러나 구매자는 **내장 기능**으로 취급 — 에이전트 자본의 **0.6%만** 메모리 시스템에 투입. Mem0 누적 조달 $24.5M에 그침. **메모리는 버티컬 에이전트 안에 넣을 것, SKU로 팔지 말 것.** https://valueaddvc.com/blog/the-ai-memory-problem-how-startups-are-solving-for-persistent-context |

> 🔴 **해커톤 직결 경고**: 위 "제외" 목록 + §1.3의 포화 클러스터(에이전트 메모리/컨텍스트 압축, 헬스, 재난, 교육)를 합치면, **프록시 갤러리에서 가장 많이 나온 주제가 곧 시장에서 가장 가치 없는 주제**라는 결론이 나옵니다. 특히 "컨텍스트 압축 -80%" 류는 Berkeley 갤러리에 최소 8개가 있었고 시장에서는 0.6%의 자본만 갑니다.

### 2.4 검증 한계 (반드시 인지)
1. Product Hunt 순위는 **런칭일 인기 신호**이지 매출·트랙션 증거가 아님 (Hey Noah, Coldtea, MagiCrew, x1, Monid).
2. **YC S26/F26 기업 디렉터리는 수집 실패** (JS SPA). YC 근거는 RFS 원문 + 2차 보도임.
3. **Hacker News Show HN(2026-08~09, 150pt+)은 VC 자금과 정반대 방향**: 로컬/엣지 모델(Needle2 14MB 에이전틱 LLM, Gemma 4 26B를 2GB RAM에, 919pt / Maple 20B MoE on iPhone)과 **AI 슬롭 필터링**("Hacker News without AI" 2건)에 쏠림. 빌더 커뮤니티는 로컬·저가·오픈웨이트·AI 필터링을 향하고, 자본은 엔터프라이즈 에이전트를 향함.
4. 1차 출처로 교차 확인된 라운드: AIR, Instinct, River AI, June, Mistral, Vapi, Profound, Norm Ai, Harvey, SpaceX/Anysphere. 나머지는 집계 사이트 기반.
5. 2026-09는 아직 절반만 경과 + 발표 지연으로 데이터가 얇음. 8월 데이터가 훨씬 완전함.

---

## 3. 최근 능력 해금 (2026-06 ~ 2026-09) 과 그것이 여는 SaaS

> **[1차]** = 벤더 문서/뉴스룸 직접 확인. **[2차]** = 언론/애널리스트 경유(슬라이드에 넣기 전 재확인 필요).
> openai.com/index/* 는 HTTP 403 으로 직접 확인 불가했습니다. OpenAI 수치는 개발자 문서(1차) 또는 언론(2차) 기준입니다.

### 3.1 가격 · 모델

| # | 해금 | 핵심 수치 | 이것이 새로 여는 SaaS |
| --- | --- | --- | --- |
| 1 | **Claude Fable 5.1 / Mythos 5.1** (2026-09-01) **[1차]** | $10/$50 per Mtok. 결정적으로 **캐시 히트 $0.25/Mtok = 기본 입력의 0.025배**. 다른 Claude 모델은 전부 0.1배. 1시간 캐시 쓰기 $20. Batch로 절반. | **"문서 1건당 프런티어 모델"** 리뷰 SaaS. 500페이지 계약서/사업설명서/코드베이스를 1시간 캐시에 한 번 올리고($20/Mtok 쓰기), 이후 수백 개 독립 질의를 $0.25/Mtok로 실행. 예전엔 캐시 읽기 $1/Mtok이라 RAG 청킹+중급 모델로 갈 수밖에 없었음. **전 코퍼스 프런티어 추론이 검색 수준 가격이 됨.** |
| 2 | **Claude Opus 5** (2026-07-24) **[가격/모드 1차, 컨텍스트/벤치 2차]** | $5/$25(Opus 4.8 동일), 배치 $2.50/$12.50, 캐시 읽기 $0.50. **Fast mode**(리서치 프리뷰) = 기본 대비 ~2.5배 속도, $10/$50, 200k 초과 요청 포함 전 컨텍스트에 적용. **대화 중 툴 교체**, **자동 폴백** 베타. | **레이턴시 티어드 에이전트**: 같은 에이전트가 "사람이 보고 있는" 인터랙티브 경로는 2.5배 속도로, 백그라운드 경로는 1배로. 요청당 `speed:"fast"` 플래그라 **프롬프트 스택도 평가 스위트도 두 벌 유지할 필요 없음.** |
| 3 | **Claude Sonnet 5** (2026-06-30) **[1차]** | 도입가 $2/$10이 **영구 확정**. 2026-09-01 예정이던 $3/$15 인상 **취소**. Sonnet 4.6 대비 입출력 **각 33% 인하**. BrowseComp(에이전틱 검색), OSWorld-Verified(컴퓨터 사용) 개선. 캐시 읽기 $0.20. | **정액 좌석제 에이전틱 SaaS**. $29/월 "브라우징과 폼 작성을 대신 해주는" 어시스턴트. 인상이 예고된 $3/$15에서는 헤비 유저가 있는 정액제를 인수(underwrite)할 수 없었음. |
| 4 | **OpenAI 2026-07-30 가격 인하** **[2차, CNBC·VentureBeat 교차]** | GPT-5.6 **Luna $1/$6 → $0.20/$1.20 (−80%)**, Terra −20%($2/$12), Sol 유지($5/$30). 촉발 요인으로 7/24 Opus 5 $5/$25, 같은 달 Gemini 3.6 Flash $1.50/$7.50이 지목됨. | **무료 티어로 굴러가는 소비자 AI**. 입력 $0.20/Mtok이면 의미 있는 무료 티어가 MAU당 월 몇 센트. **"AI 스타트업은 무료 티어를 감당 못 한다"는 2025년 테제가 처음으로 반증 가능해짐.** |
| 5 | **Gemini 3.8 Flash** (2026-09-02) **[1차]** | 1M 컨텍스트, 64k 출력. **$0.75/$3.75 — 단 2026-12-31까지 도입가이며 2027-01-01에 약 2배.** DeepSWE v1.1 **73.7%**(3.7 Flash 65.3%), OSWorld-2.0 **59.0%**(50.6%). Flash Cyber 변형은 20개 언어 자율 취약점 발견 성공률 70% 초과. | **대규모 자율 코드 유지보수** — 고객사 전체 레포 플릿에 야간으로 의존성 업그레이드·CVE 패치 PR을 여는 봇. "5,000개 레포에 매일 밤 에이전트를 돌린다"가 처음으로 계산이 맞음. ⚠️ **$0.75에 사업모델을 세우지 말 것 — 12/31 만료.** |
| 6 | **Anthropic 토크나이저 세금** **[1차]** | Claude 4.7 이상 + Mythos Preview는 **같은 텍스트에 약 30% 더 많은 토큰**을 만드는 새 토크나이저 사용. Sonnet 4.6 이하는 구 토크나이저. 별도로 `inference_geo:"us"`는 입력/출력/캐시 전부에 **1.1배**, Bedrock/Vertex 리전 엔드포인트는 글로벌 대비 **10% 프리미엄**. | **토큰이 아니라 "태스크" 단위 비용을 모델링하는 크로스 프로바이더 FinOps SaaS**. 토크나이저 차이, 캐시 배수(0.025배 vs 0.1배), Fast mode 프리미엄, 레지던시 배수, 세션-시간 과금을 정규화. **정가표 $/Mtok 비교는 이제 적극적으로 오해를 유발** — 유료 도구가 태어나는 정확한 조건. |

### 3.2 에이전트 실행 · 도구

| # | 해금 | 핵심 수치 | 이것이 새로 여는 SaaS |
| --- | --- | --- | --- |
| 7 | **Claude `computer_toolset_20260801`** — 컴퓨터 사용 **GA** **[1차]** | 베타 헤더 불필요. 멤버 툴 17종 전부 기본 활성, **`zoom`**(화면 영역을 전체 스크린샷 픽셀 공간에서 풀해상도 캡처) 포함. 툴셋 오버헤드 ~4,500 입력 토큰. fable-5-1/mythos-5-1/fable-5/opus-5/sonnet-5/opus-4-8 지원. | **레거시 데스크톱 RPA 대체**를 규제 산업 SMB(치과 PM 시스템, 권원보험, 손해사정)에 판매. API가 없는 Windows 데스크톱이 기록 시스템인 곳. **GA + 베타 헤더 없음 = 진짜 SLA를 서명할 수 있음.** `zoom`이 1990년대식 촘촘한 그리드 UI를 OCR 파이프라인 없이 읽게 만듦. |
| 8 | **Claude `browser_toolset_20260801`** — 컴퓨터 사용과 **별개**의 31툴 브라우저 툴셋 **[1차]** | 뷰포트 픽셀 좌표. `read_page`(접근성 트리 + 엘리먼트 레퍼런스), **`find`(자연어 엘리먼트 검색)**, `get_page_text`, `form_input`, `file_upload`, **`read_console`**, **`read_network`**, `javascript_exec`, 탭 관리 4종. 오버헤드 ~6,600 토큰. ZDR 적격. AWS/Bedrock/Foundry 및 Managed Agents에서는 **불가**. | **콘솔·네트워크까지 읽는 연속 E2E 웹 QA 서비스**. `read_console`/`read_network`가 1급 툴이라는 것은 에이전트가 **"버튼이 안 눌렸어요"가 아니라 실제 500 응답과 스택트레이스가 담긴 버그 리포트**를 낼 수 있다는 뜻 — 이전까지 에이전틱 QA를 팔 수 없게 만들던 바로 그 조각. |
| 9 | **Claude Managed Agents** **[1차]** | 베타 헤더 `managed-agents-2026-04-01`, 전 API 계정 기본 활성. Anthropic이 루프·샌드박스·압축·캐싱을 운영. Agent/Environment/Session/Events 프리미티브, SSE 스트리밍, 서버측 이벤트 영속화, **세션 간 영속 파일시스템**, 실행 중 조종·중단, 셀프호스트 샌드박스, **cron 스케줄 배포**. 런타임 **$0.08/세션-시간**, 밀리초 단위 과금, `running` 상태에서만 발생(유휴·재스케줄·종료는 무료). 문서 예시: Opus 5 1시간 세션 50k in/15k out = **총 $0.705**. ZDR·HIPAA BAA 부적격. | **"야간 리테이너 애널리스트"** SaaS — 새벽 2시에 깨어나 그날 데이터를 당겨 40분 일하고 메모를 남기는 스케줄 에이전트. **유휴 시간 무료 + 관리형 cron** 덕에 샌드박스 플릿을 직접 운영하지 않고도 한계 인프라 비용 몇 센트로 $99/월 좌석을 팔 수 있음. |
| 10 | **Managed Agents "Dreams"** — 오프라인 메모리 통합을 API로 **[1차]** | 리서치 프리뷰, 헤더 `dreaming-2026-04-21`. 메모리 스토어 1개 + **과거 세션 트랜스크립트 1~100개**를 받아 중복 병합·구식/모순 항목 교체·새 인사이트를 담은 **새 스토어**를 생성. **입력 스토어는 절대 변경되지 않음.** `instructions`(4,096자)로 합성 방향 조정. 수 분~수 시간 소요. | **버티컬 "조직 기억" 제품** — 지원 조직용 에이전트가 매일 밤 티켓 100건을 모순 없는 플레이북 스토어로 통합. **"검토 후 승격(review-then-adopt)" 형태(입력 불변)가 컴플라이언스 민감 구매자에게 팔 수 있게 만드는 핵심.** |
| 11 | **MCP 튜널** **[1차]** | 리서치 프리뷰. cloudflared 기반 **아웃바운드 전용**(198.41.192.0/19, 7844 TCP+UDP), **인바운드 포트 개방 불필요**. Anthropic 프록시가 **내부 TLS**를 종단하는데 인증서는 고객만 보유 → **Cloudflare가 페이로드를 못 읽음**. 3중 보안(외부 mTLS+IP 검증, 내부 TLS, 서버별 OAuth). Helm/Docker Compose 배포. "as-is", 가동률 약정 없음. | **온프렘 시스템 위에 반나절 만에 얹는 에이전트 레이어** — 보안팀이 인바운드 포트를 열거나 벤더 IP를 허용하지 않는 병원 EHR·공장 MES·은행 코어. **"전송 경로가 읽을 수 없다"는 성질 자체가 세일즈 논거.** ⚠️ 리서치 프리뷰라 가동률 약속 불가. |
| 12 | **MCP 2026-07-28 스펙** — 무상태 코어 + 헤더 라우팅 **[1차]** | 출시 이래 최대 개정. `initialize`/`initialized` 핸드셰이크와 `Mcp-Session-Id` 헤더 **제거** → 모든 요청이 자기기술적, 평범한 로드밸런서 뒤 아무 인스턴스나 응답 가능. **MRTR**(Multi Round-Trip Requests)이 `elicitation/create`·`sampling/createMessage`를 양방향 스트림 없이 대체. **메서드·툴 이름이 `Mcp-Method`/`Mcp-Name` HTTP 헤더에 실림** → 게이트웨이·WAF가 JSON 바디 파싱 없이 라우팅·인가 가능. 리스트 응답에 `ttlMs`/`cacheScope`. **Tasks**가 공식 확장으로 승격. 인증: RFC 9207 issuer 검증, DCR → **CIMD**. 12개월 지원 중단 창. TS/Python/Go/C# 정식, Rust 베타. https://blog.modelcontextprotocol.io/posts/2026-07-28/ | **MCP 게이트웨이 / 방화벽** — `Mcp-Method`와 `Mcp-Name` 헤더만으로 툴 단위 인가·레이트리밋·감사·DLP를 HTTP 엣지에서 강제. JSON 바디 검사도, 스티키 세션도 불필요. **헤더 라우팅 + 무상태가 정확히 이것을 가능하게 만든 변화** — 평범한 리버스 프록시 플러그인으로 CDN 스케일에서 돌릴 수 있음. |

### 3.3 음성 · 멀티모달 · 온디바이스

| # | 해금 | 핵심 수치 | 이것이 새로 여는 SaaS |
| --- | --- | --- | --- |
| 13 | **GPT-6 Astra** (2026-09-03) **[changelog 1차, 벤치 2차]** | "가장 어려운 엔드투엔드 작업용." **비동기 툴 호출, 실행 중 조종(mid-turn steering), 대화 중 추론 강도 변경.** 보도: 1M 컨텍스트, **OSWorld 2.0 72.6%**, GPT-5.6 Sol 대비 **태스크당 벽시계 시간 ~47% 감소**, FrontierMath Tier 4 97.6%, ExploitBench 100%. KiCad PCB 레이아웃·Blender·Excel↔Power BI 데모. API $10/$1(캐시)/$50. | **결과 과금형 데스크톱 작업 SaaS** — "당신의 PCB DRC 정리 / Blender 에셋 준비 / 월간 Power BI 갱신을 완료 건당 $X에." 실행 중 조종 + 47% 시간 단축이 컴퓨터 사용을 **데모에서 "완료 건당 청구해도 두 번 시도까지는 마진이 남는" 것**으로 바꿈. |
| 14 | **GPT-Live 1 GA** (2026-09-10) **[메커니즘 1차, 가격 2차]** | **풀듀플렉스**(말하면서 동시에 듣기), **분당 $0.05** 정액, 초 단위 과금. **위임(delegation) 모델** — 백엔드 에이전트가 작업하는 동안 대화가 계속됨. 2가지 모드(Responses 관리형 / 클라이언트 제어). WebRTC, WebSocket, 서버측 제어, **텔레포니/SIP**. 음성 모델과 백엔드 모델을 독립 선택. ⚠️ 백엔드 토큰·툴은 별도 과금이라 실제 견적은 유의미하게 높음. | **일하면서 말하는 음성 에이전트** — "지금 조회해 드릴게요, 잠시만요. 불러오는 동안 생년월일 확인 부탁드립니다"를 **진짜로** 하는 인바운드 클레임/예약 라인. 반듀플렉스 리얼타임은 툴 호출 중 무음이나 필러 오디오를 강요했음. 풀듀플렉스 + 명시적 백엔드 위임 + SIP = **IVR만이 아니라 IVR+사람 하이브리드를 대체.** |
| 15 | **GPT Transcribe / GPT Live Transcribe** (2026-07-28) **[존재·날짜 1차, 가격 2차]** | **자유형식 전사 컨텍스트, 키워드 힌트, 복수 예상 입력 언어**(`languages`가 단수 `language` 대체) 지원. 2차: 배치 $0.0045/분, 라이브 $0.017/분, 99개 이상 언어, 라이브 지연 5단계(minimal~xhigh). **Whisper-1과 GPT-4o 전사 모델은 2026-08-26 지원 중단, 2027-02-26 종료. Assistants API는 2026-08-26 종료.** | **코드스위칭 회의용 도메인 어휘 정확 실시간 자막** — 이중언어 임상/법률 세션에서 `languages` 배열 + 키워드 힌트 + 자유형식 컨텍스트("신장내과 협진이고 아래 40개 약물명이 나옴")가 **고유명사와 문장 중간 언어 전환**이라는 이전 제품들을 죽인 두 실패 모드를 해결. 경쟁 하한선: ElevenLabs Scribe v2 Realtime 30~80ms. |

### 3.4 보너스 (각 1줄)

- **Anthropic Model Hardware Standard (MHS)** (2026-08-27 리서치 프리뷰) **[2차]** — MCP가 소프트웨어 툴에 한 일을 물리 기계에. 표준 드라이버, `read`/`write` 프리미티브, 무게·안전 한계·조정 파라미터를 포함한 기기 메타데이터. 파트너: AWS, Danaher, Tecan, QIAGEN, Doosan Robotics, Automata, Universal Robots, Hugging Face, Raspberry Pi. 주장: 셋업이 수주~수개월 → 수시간~수분. QuEra 에이전트가 레이저 락 복구 700회 시도에서 **99.3% 성공(수기 스크립트 58%)**. → **SaaS 아이디어**: CRO·대학 코어 시설용 "랩 에이전트" 구독. MHS 통합 1회가 현재 컨설팅 사업으로 만들어 놓은 기기별 SDK 작업을 대체. https://www.anthropic.com/news/model-hardware-standard-research-preview
- **MCP Apps (SEP-1865)** — OpenAI·Anthropic 공동 저작의 공식 MCP 확장. Anthropic이 **2026-01-26** Claude에 지원 출시(Amplitude, Asana, Box, Canva, Clay, Figma, Hex, monday.com, Slack). 샌드박스 iframe에서 postMessage-over-JSON-RPC로 **서버 렌더링 인터랙티브 HTML**. 모델 생성 아티팩트와는 구분됨. **[2차]**
- **음성 하한선 (2026-09)** **[2차 — 비교 블로그 기반, 인용 전 재확인]** — Cartesia Sonic 4 Turbo TTFA ~40ms(표준 ~90ms), ElevenLabs Flash v2.5 모델 추론 ~50ms, Scribe v2 Realtime STT 30~80ms, Eleven v3 GA(2026-02-02, 오디오 태그·다화자 대화·70개 이상 언어), Deepgram Nova-3 스트리밍 $0.0048/분·Flux English $0.0065/분·Aura-2 TTS $0.030/1k자·Voice Agent API 번들 ~$4.50/시간. Cartesia Sonic 2는 2026-06-01 은퇴.
- **Apple WWDC 2026** **[2차]** — Foundation Models 프레임워크가 하이브리드 플랫폼으로. 하나의 Swift 세션 API가 재구축된 온디바이스 System Language Model(프롬프트에 이미지 수용), Private Cloud Compute 서버 모델(**추론 + 32K 컨텍스트**), `LanguageModel` 프로토콜을 통한 서드파티 프런티어 모델을 모두 포괄. Gemini가 Apple Intelligence 기반 모델 옵션으로 추가. → **SaaS 아이디어**: 일상 턴은 온디바이스 무료, 어려운 턴만 유료 클라우드로 승격하는 **프라이버시 티어드 iOS 앱 — 라우팅 정책 자체가 제품.** https://developer.apple.com/wwdc26/guides/apple-intelligence/
- **오픈 웨이트 (2026-09)** **[2차 — 집계 블로그만 확인, 벤더 릴리스 페이지 미확인]** — Llama 4(Scout/Maverick), Qwen 3.5(397B total / 17B active MoE), DeepSeek V4(Pro/Flash), Gemma 4(최강 온디바이스 소형), Mistral Medium 3.5.
- **Browserbase Agents** (2026-06 출시) **[2차]** — API 호출 하나로 웹 에이전트 배포, 유지할 인프라 없음. Stagehand(act/extract/observe/agent)와 Director(노코드) 위에 구축.
- **Chrome Lighthouse "Agentic Browsing" 카테고리** — llms.txt 감사 항목 추가. 단 GPTBot·ClaudeBot·PerplexityBot은 실제로 /llms.txt를 거의 안 가져가고 HTML을 직접 크롤함. **llms.txt 단독 제품은 근거 약함.**

---

## 4. 심사위원 친화적 아이디어 10선

### 4.0 아이디어 선별에 쓴 필터

1. **§1.5의 화이트스페이스** 안에 있을 것 (프록시 갤러리 310개에서 0~1건)
2. **§2의 자금·수요가 실재하는 카테고리**일 것 (단 §2.3 제외 목록은 회피)
3. **§3의 2026년 해금**이 없었다면 못 만들었을 것 ("Why now"의 기술적 근거)
4. **FastAPI / Next.js / Postgres / Claude 로 24시간 내 완성** 가능할 것
5. **"SaaS"로 읽힐 것** — 로그인, 팀, 요금제, 대시보드가 있을 것 (Best SaaS Product 트랙)
6. **결정론적 코드가 LLM 출력을 검증**할 것 (thin wrapper 방어의 유일한 확실한 방법)

> 점수 표기는 Devpost 실제 배점 기준입니다: **Tech 25 / Impact 25 / Innovation 20 / UX 15 / Presentation 15**.

---

### 🥇 1위 — **Clause50** : EU AI Act Article 50 투명성 감사 SaaS

| 항목 | 내용 |
| --- | --- |
| **타깃 유저** | EU 사용자를 대상으로 하는 SaaS·이커머스·미디어 기업의 **법무/컴플라이언스 담당자 + 프로덕트 매니저**. 특히 직원 20~500명, 전담 법무팀이 없는 회사. |
| **아픈 문제** | 2026-08-02부터 **웹사이트 챗봇은 스스로가 기계임을 고지해야 하고, AI 생성 콘텐츠는 마킹되어야 하며, 딥페이크·AI 작성 뉴스는 라벨링되어야** 합니다. 이 의무는 **제3자 도구를 썼어도, EU 밖에 설립된 회사여도** 적용됩니다. 과징금 **최대 €15M 또는 전세계 매출 3%**. 그런데 대부분의 회사는 자기 사이트 어디에 챗봇이 몇 개 박혀 있는지도 모릅니다. |
| **Why now** | ① Article 50이 **2026-08-02 발효**, 기존 시스템 유예가 **2026-12-02 만료** → 지금이 정확히 그 창. ② 고위험(Annex III) 의무는 2027-12로 연기되어 **시장의 단기 수요가 전부 Article 50 한 곳으로 몰림**. ③ 기술적으로는 **Claude `browser_toolset_20260801`의 `read_page`(접근성 트리) + `read_network` + `find`(자연어 엘리먼트 검색)** 가 GA 되면서, "이 페이지에 사용자에게 고지되지 않은 AI 인터랙션이 있는가"를 스크립트가 아니라 에이전트가 판정할 수 있게 됨.<br>https://artificialintelligenceact.eu/transparency-rules-article-50/<br>https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool |
| **24h MVP 범위** | ① 도메인 입력 → 브라우저 에이전트가 상위 N개 페이지 크롤 → 챗봇 위젯/AI 생성 이미지 메타데이터/합성 음성 플레이어/감정인식 스크립트를 탐지. ② **결정론적 룰 엔진**이 Article 50(1)~(4) 조항별로 PASS/FAIL/REVIEW 판정 — LLM은 증거 추출만, 판정은 코드. ③ 조항별 증거 스크린샷 + DOM 스니펫을 Postgres에 저장(감사 증적). ④ 각 FAIL에 대해 **붙여넣기 가능한 수정 코드**(고지 배너 HTML, `<meta>` 프로비넌스 태그) 생성. ⑤ PDF 감사 리포트 export. ⑥ 주간 재스캔 cron + 변경 알림. |
| **데모 와우 모먼트** | **"URL 하나 붙여넣고 90초."** 화면 왼쪽에 실제 브라우저 세션이 실시간으로 사이트를 돌아다니고, 오른쪽에 조항별 체크리스트가 하나씩 빨강/초록으로 채워짐. 마지막에 **"Article 50 준수율 41% · 노출 과징금 최대 €15M · 유예 만료까지 78일"** 카운트다운. 그리고 "Fix" 버튼 한 번에 수정 스니펫이 나옴. |
| **수익화** | 1회 스캔 $299 → 도메인당 지속 모니터링 **$249/월** → 에이전시·MSP용 멀티테넌트 $999/월. 좌석이 아니라 **도메인 단위** 과금(§2.2 좌석제 종말과 정렬). |
| **Tech 25** | ★★★★☆ 브라우저 에이전트 + 결정론적 룰 엔진 + 증거 그래프 + 크론. LLM과 코드의 역할 분리가 명확. |
| **Impact 25** | ★★★★★ 날짜가 박힌 법적 의무 + 금액이 박힌 과징금. 해커톤 전체에서 **가장 반박 불가능한 임팩트 서사**. |
| **Innovation 20** | ★★★★☆ 갤러리 310개 중 0건. 규제 타이밍 자체가 독창성. |
| **UX 15** | ★★★★★ 리포트/대시보드는 24시간 안에 아름답게 만들 수 있는 가장 쉬운 UI. |
| **Presentation 15** | ★★★★★ "URL 붙여넣기 → 점수"는 3분 영상에 완벽히 맞음. |
| **Thin wrapper 리스크** | 🟢 **낮음.** 판정 로직이 코드에 있고, 크롤·증거저장·재스캔 파이프라인이 실재함. "Claude한테 물어본 것"으로 보이지 않음. |
| **주요 리스크** | 법률 자문으로 오해될 소지 → UI에 "이것은 법률 자문이 아닙니다" 명시 + "REVIEW" 상태를 적극 사용. 조항 해석을 과신하면 심사위원이 반박할 수 있음. |

---

### 🥈 2위 — **AgentReady** : 에이전틱 커머스 대응력 진단 SaaS

| 항목 | 내용 |
| --- | --- |
| **타깃 유저** | Shopify/커스텀 스토어를 운영하는 **이커머스 성장 담당자 / 헤드오브이커머스**. 이미 GEO/SEO 예산을 집행 중인 조직. |
| **아픈 문제** | 브라우저 기반 에이전트가 전체 에이전트 트래픽의 **약 71%**, 그중 **38.2%가 이커머스 사이트**로 오는데, **결제/체크아웃 경로에 도달하는 건 3.16%뿐**입니다. CAPTCHA·다단계 폼·3DS·주소검증이 전부 사람을 전제하기 때문. 머천트는 **에이전트가 자기 사이트 어디에서 죽는지 볼 방법이 전혀 없습니다.**<br>https://agentlux.ai/blog/agentic-traffic-is-here-how-websites-should-prepare-for-ai-browsers-and-shopping-agents |
| **Why now** | ① 2026년에 레일이 정착됨 — ACP(OpenAI+Stripe), UCP(Google), AP2, Visa TAP. Visa가 Stripe/Tempo MPP로 카드 결제 개통, Salesforce가 ACP 지원 발표. **레일은 완성됐는데 머천트 측 준비가 안 됨.** ② `browser_toolset`의 `read_network`/`read_console`이 GA 되어 **에이전트가 실패 지점의 실제 HTTP 응답과 콘솔 에러를 리포트**할 수 있게 됨(§3.2 #8). |
| **24h MVP 범위** | ① 스토어 URL + 목표 상품 입력 → **진짜 Claude 브라우저 에이전트가 실제로 구매를 시도**. ② 전 여정을 단계별로 기록: 검색 → PDP → 장바구니 → 체크아웃 → 결제. 각 단계 스크린샷 + 소요 토큰 + 네트워크 실패. ③ 죽은 지점을 **분류된 차단 사유**로 매핑(CAPTCHA / 로그인 월 / 무한 스크롤 / 접근성 트리 누락 / 3DS / 재고 표기 없음). ④ **Agent Readiness Score 0~100** + 차단 사유별 수정 가이드. ⑤ 경쟁사 3곳 동시 스캔 → 비교 바 차트. ⑥ 주간 재실행. |
| **데모 와우 모먼트** | **화면 분할로 자사 스토어와 경쟁사 스토어에 동시에 에이전트를 붙임.** 왼쪽 에이전트는 CAPTCHA에서 막혀 빨갛게 죽고, 오른쪽은 체크아웃까지 통과. 그리고 **"당신은 에이전트 매출의 96.8%를 잃고 있습니다"** 한 줄. 시각적으로 이보다 강한 데모가 드뭄. |
| **수익화** | 스토어당 **$199/월** 모니터링, 에이전시 리셀 $899/월. GEO 예산(§2 ⑫ Profound가 밸류 $1B로 검증한 라인)에서 나오는 돈. |
| **Tech 25** | ★★★★★ 실제 브라우저 에이전트 오케스트레이션 + 실패 분류기 + 네트워크 트레이스 파싱. **10개 중 기술 깊이 최상.** |
| **Impact 25** | ★★★★☆ 숫자(71% / 38.2% / 3.16%)가 강력. 다만 "오늘의 손실"이 아니라 "다가오는 손실"이라 Clause50보다 반 칸 약함. |
| **Innovation 20** | ★★★★★ 갤러리 0건, 시장에도 뚜렷한 리더 없음(§2 ⑩ "빈 곳: 머천트 측 에이전트 대응력"). |
| **UX 15** | ★★★★☆ 여정 타임라인 + 점수 카드. |
| **Presentation 15** | ★★★★★ **10개 아이디어 중 데모 영상이 가장 강함.** |
| **Thin wrapper 리스크** | 🟢 **매우 낮음.** 에이전트를 *쓰는* 게 아니라 에이전트를 *테스트 대상에 투입*하는 구조. |
| **주요 리스크** | 라이브 데모에서 에이전트가 예기치 않게 성공/실패할 수 있음 → **녹화 + 리플레이 모드를 반드시 만들 것.** 실제 결제까지 가지 말 것(테스트 상품/샌드박스). |

---

### 🥉 3위 — **MCPGuard** : MCP 서버 공급망 심사 · 게이트웨이

| 항목 | 내용 |
| --- | --- |
| **타깃 유저** | 사내에서 에이전트를 굴리기 시작한 **플랫폼 엔지니어링 / AppSec 팀**. |
| **아픈 문제** | 공식 MCP 레지스트리에만 **9,652개 서버(28,959개 버전)**가 있고 소프트웨어 조직의 **41%가 MCP를 프로덕션에 투입**했는데, 개발자들이 아무 서버나 설치합니다. AIR은 자기가 온라인에서 발견한 애드온의 **약 27%를 위험으로 필터링**한다고 밝혔습니다. **에이전트가 무엇을 할 수 있는지 아무도 모르는 상태.** |
| **Why now** | ① **MCP 2026-07-28 스펙**이 세션을 없애고 **`Mcp-Method`/`Mcp-Name`을 HTTP 헤더로 승격** → **JSON 바디 파싱 없이 평범한 리버스 프록시에서 툴 단위 인가·감사가 가능해짐.** 이전 스펙에서는 불가능했던 제품 형태. ② 자본이 이미 증명 — AIR $50M(2026-09-01, Sequoia·Greenoaks), Zenity $125M(2026-08). ③ 그런데 **AIR의 웨지인 "MCP 서버/스킬 공급망 심사"는 아직 nascent**(§2 ①의 화이트스페이스). |
| **24h MVP 범위** | ① MCP 서버 URL/패키지 입력 → 매니페스트·툴 스키마 수집. ② **정적 분석**(요청하는 스코프, 네트워크 목적지, 파일시스템 접근, 프롬프트 인젝션 페이로드 패턴) + Claude의 툴 설명 의미 분석. ③ **격리 샌드박스에서 실제 툴 호출을 재생**하고 아웃바운드를 기록. ④ **Risk Score + 자동 생성 정책**(허용 툴 화이트리스트를 `Mcp-Name` 헤더 규칙으로 export). ⑤ FastAPI 리버스 프록시가 그 정책을 실제로 강제 — **차단 로그가 실시간으로 쌓이는 대시보드**. |
| **데모 와우 모먼트** | 레지스트리에서 무해해 보이는 서버를 하나 고름 → MCPGuard가 **"이 `search_docs` 툴이 설명에 없는 `POST https://…` 로 데이터를 보냅니다"** 를 잡아냄 → 정책 생성 → 프록시 켬 → **같은 호출이 실시간 로그에 BLOCKED로 찍힘.** 공격→탐지→차단→증명의 완결 루프. |
| **수익화** | 심사한 서버 수 기준 $0.5k/월부터, 엔터프라이즈 게이트웨이 좌석 무관 정액. |
| **Tech 25** | ★★★★★ **10개 중 최고.** 정적분석 + 샌드박스 실행 + 정책 컴파일 + 실동작 프록시. |
| **Impact 25** | ★★★★☆ 구매자는 명확하나, 학생 심사위원에게는 고통이 간접적으로 느껴질 수 있음. |
| **Innovation 20** | ★★★★★ 갤러리 0건 + 2026-07-28 스펙 변화에 정확히 올라탐. |
| **UX 15** | ★★★☆☆ 보안 대시보드는 예쁘게 만들기 어렵고 시간이 듦. |
| **Presentation 15** | ★★★★☆ 공격-차단 서사는 좋지만 도메인 설명에 30초가 듦. |
| **Thin wrapper 리스크** | 🟢 **최저.** LLM이 없어도 절반은 동작하는 제품. |
| **주요 리스크** | 24시간 내 샌드박스 구현이 가장 무거움. **프록시+정책만 확실히 하고 샌드박스는 사전 녹화 데모로 대체**하는 축소 경로를 미리 준비할 것. |

---

### 4위 — **TrustReply** : 보안 설문(SIG/CAIQ) · 벤더 실사 자동응답

- **타깃**: 시리즈 A~C SaaS의 **보안 리드 겸 딜 데스크**. 고객사 보안 설문 때문에 딜이 멈추는 사람.
- **문제**: 표준 **SIG 설문이 20개 도메인 800문항 이상**. 2026-04 기준 엔터프라이즈 보안팀이 받는 **분기당 설문 수가 2025 Q1 대비 23% 증가**. 통합 AI 레이어를 쓴 팀은 **회신 소요를 3~5일에서 4시간 미만으로** 단축.
  https://autorfp.ai/blog/best-security-questionnaire-software
- **Why now**: §3.1 #1 — **Fable 5.1 캐시 읽기 $0.25/Mtok(기본의 0.025배)**. 회사의 정책·SOC2·아키텍처 문서 전체를 1시간 캐시에 한 번 올리고 **800개 질문을 각각 프런티어 모델 풀컨텍스트로** 답하는 게 처음으로 경제적. RAG 청킹 없이.
- **24h MVP**: 정책 문서 업로드 → 캐시 프라임 → 설문 XLSX 업로드 → 문항별 (답변 + 근거 문서 인용 + 신뢰도) 생성 → **신뢰도 임계치 미만은 자동으로 사람 검토 큐로** → 승인 시 답변 라이브러리에 학습 → XLSX 원본 포맷 그대로 export.
- **와우**: 800행 스프레드시트를 드롭하고 **진행 바가 차오르며 셀이 채워지는 화면**, 최후에 "4시간 → 6분, 인간 검토 필요 41문항".
- **수익화**: $499/월 (설문 무제한) — 딜 하나 살리면 회수되는 가격.
- **점수**: Tech ★★★☆☆ / Impact ★★★★★ / Innovation ★★☆☆☆ / UX ★★★★☆ / Presentation ★★★★☆
- **Thin wrapper 리스크**: 🟠 **중간~높음.** 본질이 "문서 위의 RAG"로 보일 수 있음. **방어책**: 신뢰도 캘리브레이션, 인용 없으면 답변 거부하는 하드 게이트, 답변 라이브러리 버전 관리 + 재사용률 지표를 전면에 세울 것.
- **비고**: **PMF는 10개 중 가장 확실하지만 Innovation 20점에서 가장 크게 잃습니다.** Vanta·Drata·Conveyor·Loopio가 이미 함.

### 5위 — **TaskCost** : 토큰이 아니라 "태스크" 단위 AI 비용 원장

- **타깃**: AI 제품을 운영하는 **엔지니어링 리드 / FinOps**.
- **문제**: **FinOps 실무자의 98%가 AI 지출을 관리**(전년 63%에서 급증). 2026 State of FinOps 리포트에서 **가장 많이 요청된 기능이 토큰·LLM 요청·GPU 단위의 세밀한 모니터링**. 그런데 정가표 비교가 이제 **틀립니다**.
  https://www.nops.io/blog/finops-tools-for-ai/
- **Why now**: §3.1 #6 — Claude 4.7+ 토크나이저가 **같은 텍스트에 ~30% 더 많은 토큰**을 만들고, Fable 5.1만 캐시 배수가 **0.025배**(나머지 0.1배)이며, `inference_geo:"us"`는 **1.1배**, Bedrock/Vertex 리전은 **10% 프리미엄**, Managed Agents는 **$0.08/세션-시간**이 따로 붙고, Gemini 3.8 Flash의 $0.75는 **2026-12-31 만료**. **정가표 $/Mtok 비교가 적극적으로 오해를 유발하는 상태 = 유료 도구가 태어나는 조건.**
- **24h MVP**: OpenTelemetry/로그 업로드 또는 SDK 미들웨어 → 태스크 단위로 스팬 묶기 → **정규화 가격 엔진**(토크나이저 배수, 캐시 배수, Fast mode, 레지던시, 세션-시간, 만료 예정 프로모 가격) → "태스크당 실비용" 대시보드 → **반사실 시뮬레이터**("Fable 5.1 + 1시간 캐시로 바꾸면 태스크당 $0.42 → $0.11").
- **와우**: **가격 만료 타임머신** — "2027-01-01에 Gemini 3.8 Flash가 2배 되면 당신의 월 비용은 $4,100 → $7,900". 아무도 안 보여주는 화면.
- **수익화**: 추적 지출의 1%, 최소 $200/월.
- **점수**: Tech ★★★★☆ / Impact ★★★★☆ / Innovation ★★★★☆ / UX ★★★★☆ / Presentation ★★★☆☆
- **Thin wrapper 리스크**: 🟢 **낮음** (LLM이 거의 안 쓰임 — 역설적으로 "AI 해커톤"에서 감점 요인이 될 수 있으니 이상탐지에 Claude를 명확히 한 군데 쓸 것).

### 6위 — **Roundtable** : 멀티플레이어 에이전트 세션

- **타깃**: AI 코딩/리서치 에이전트를 각자 따로 돌리는 **제품·엔지니어링 팀**.
- **문제**: 개발자의 **59%가 AI 코딩 툴을 3개 이상 병행** → 세션이 파편화되고 같은 질문을 각자 다시 물음.
- **Why now**: **YC RFS "Multiplayer AI"** 가 직접 요청한 카테고리이고 **펀딩된 리더가 없음**(§2 ⑥). 기술적으로는 Claude **Managed Agents**의 서버측 이벤트 영속화 + SSE 스트리밍 + **실행 중 조종/중단**이 "여러 사람이 같은 세션에 끼어든다"를 처음으로 구현 가능하게 만듦(§3.2 #9).
- **24h MVP**: 공유 에이전트 룸(웹소켓) → 누구나 실행 중 세션에 메시지 주입 → 발언자별 색상 표시된 타임라인 → 세션 포크/머지 → 룸별 영속 파일시스템.
- **와우**: 두 브라우저 창을 나란히 놓고 **한 사람이 에이전트를 실행 중일 때 다른 사람이 끼어들어 방향을 틀고, 에이전트가 즉시 반응**하는 장면.
- **수익화**: 워크스페이스당 $20/월.
- **점수**: Tech ★★★★☆ / Impact ★★★☆☆ / Innovation ★★★★★ / UX ★★★★★ / Presentation ★★★★☆
- **Thin wrapper 리스크**: 🟡 중간 — "Claude에 채팅방을 붙였다"로 보일 수 있음. **포크/머지와 충돌 해소를 반드시 보여줄 것.**
- **비고**: Innovation과 UX는 최상이지만 **Impact 25점에서 "그래서 얼마를 아끼나"를 답하기 어려움.**

### 7위 — **RenewalRadar** : 벤더 계약 자동갱신 조항 레이더

- **타깃**: 스타트업 **재무/오퍼레이션 담당자** (SaaS 계약 40~200건 보유).
- **문제**: 자동갱신·해지통보 기한(보통 갱신 60~90일 전)을 놓쳐 쓰지도 않는 툴에 1년을 더 지불. 법무 없는 회사는 계약서가 Drive에 흩어져 있음.
- **Why now**: §3.1 #1 캐시 경제 — 계약서 전문을 잘라내지 않고 **통째로** 읽혀야 "Notwithstanding Section 4.2…" 같은 교차참조 조항을 잡는데, 이게 $0.25/Mtok 캐시 읽기로 처음 저렴해짐.
- **24h MVP**: 계약서 다중 업로드 → 조항 추출(갱신 유형, 통보 기한, 인상 상한, 해지 조건) → **역산 캘린더 + 이메일 알림** → "다음 90일 노출 금액" 대시보드 → 해지 통보 메일 초안 생성.
- **와우**: 20개 계약을 드롭하고 **타임라인에 빨간 마감이 줄줄이 꽂히며 "62일 안에 조치하지 않으면 $147,000 자동 갱신"**.
- **수익화**: $99/월.
- **점수**: Tech ★★★☆☆ / Impact ★★★★☆ / Innovation ★★★☆☆ / UX ★★★★☆ / Presentation ★★★★☆
- **Thin wrapper 리스크**: 🟠 중간. **방어책**: 조항 추출에 근거 하이라이트 강제 + 날짜 계산은 전부 코드.
- **비고**: 갤러리 0건(법무 카테고리 전무)이지만, 시장에서는 Harvey/Legora가 상위를 닫은 영역이라 **"작아서 안전한" 아이디어.**

### 8위 — **RubricRoom** : 도메인 전문가용 평가(Evals) → 컴플라이언스 증적

- **타깃**: 규제 산업에서 에이전트를 배포하려는 팀의 **도메인 전문가**(간호사, 준법감시인, 보험 심사역) — 엔지니어가 아님.
- **문제**: 에이전트 이니셔티브를 가진 기업의 **88%가 프로덕션 배포에 실패**하고, Gartner는 2027년 말까지 40% 이상 취소를 전망. 막는 건 모델 성능이 아니라 **거버넌스 승인**인데, 승인자는 LangSmith를 쓸 줄 모름.
- **Why now**: §2 ⑧의 화이트스페이스("비엔지니어가 채점하는 평가 + 평가 결과를 컴플라이언스 증적으로")가 §2 ②(규제)와 수렴 중. 기술적으로는 **Dreams**(§3.2 #10)가 **입력 스토어 불변 + 검토 후 승격** 구조라 감사 대상 파이프라인을 만들 수 있음.
- **24h MVP**: 엔지니어가 트레이스를 올림 → 도메인 전문가에게 **스프레드시트 없는 카드 UI**로 채점 요청(👍/👎 + 사유 태그) → 합의도/신뢰구간 계산 → **서명·타임스탬프된 평가 증적 PDF** 생성 → 회귀 감지 시 알림.
- **와우**: 두 화면 — 엔지니어 화면과 간호사 화면. 간호사가 카드 5장을 넘기자 **"승인 게이트: 92% 합의 · 증적 서명 완료"** 배지가 켜지고 PDF가 떨어짐.
- **수익화**: $299/월 + 평가자 좌석.
- **점수**: Tech ★★★☆☆ / Impact ★★★★☆ / Innovation ★★★★☆ / UX ★★★★★ / Presentation ★★★☆☆
- **Thin wrapper 리스크**: 🟢 낮음(LLM 비중 자체가 작음).

### 9위 — **NightDesk** : 야간 리테이너 애널리스트

- **타깃**: 전담 리서처가 없는 **소규모 전략/컴플라이언스 팀**.
- **문제**: 규제·경쟁사·공급업체 변화를 따라갈 사람이 없음.
- **Why now**: §3.2 #9 — **Managed Agents의 cron 스케줄 배포 + $0.08/세션-시간 + 유휴 무료 + 세션 간 영속 파일시스템.** 문서 예시로 Opus 5 1시간 세션이 총 $0.705. **샌드박스 플릿을 운영하지 않고도 $99/월 좌석의 한계 비용이 몇 센트**가 되는 첫 순간.
- **24h MVP**: 감시 대상(규제 사이트, 경쟁사 가격 페이지, 채용 공고) 등록 → 매일 새벽 에이전트가 깨어나 diff를 뜨고 40분 조사 → 아침에 "무엇이 바뀌었고 왜 중요한가" 메모 → 근거 링크 + 이전 스냅샷 대비 하이라이트.
- **와우**: **비용 라인이 실시간으로 도는 화면** — "어젯밤 7개 소스, 38분 작업, 총 비용 $0.51. 당신의 구독료는 $99."
- **수익화**: $99/월.
- **점수**: Tech ★★★☆☆ / Impact ★★★☆☆ / Innovation ★★★☆☆ / UX ★★★★☆ / Presentation ★★★★☆
- **Thin wrapper 리스크**: 🔴 **높음.** "cron + Claude"로 보이기 쉬움. 24시간 안에 차별화 요소를 넣기 어려움.

### 10위 — **VoiceIntake** : 풀듀플렉스 규제 아웃바운드 음성

- **타깃**: 추심·사전승인·클레임 후속 등 **아웃바운드 규제 통화**를 돌리는 팀 (§2 ⑨의 명시적 화이트스페이스).
- **Why now**: **GPT-Live 1 GA(2026-09-10) 풀듀플렉스, 분당 $0.05, SIP 지원, 백엔드 위임 모델**(§3.3 #14). 조회하는 동안 무음이나 필러 오디오가 필요 없어짐 → **IVR이 아니라 IVR+사람 하이브리드를 대체.**
- **24h MVP**: 통화 목록 업로드 → 에이전트가 SIP로 발신 → 백엔드 위임으로 조회하면서 대화 유지 → 통화별 전사 + 결과 태깅 + 규제 고지 문구 자동 삽입 검증.
- **점수**: Tech ★★★★☆ / Impact ★★★★☆ / Innovation ★★★☆☆ / UX ★★★☆☆ / Presentation ★★★★☆
- **Thin wrapper 리스크**: 🟡 중간.
- **⚠️ 왜 10위인가**: **§2 ⑨는 본 리포트에서 가장 혼잡한 카테고리**(Sierra, PolyAI, Bland, Retell, Decagon, ElevenLabs, 그리고 오픈소스 Dograh). 게다가 라이브 전화 데모는 24시간 해커톤에서 실패 확률이 가장 높습니다. **기술은 멋지지만 위험 대비 보상이 나쁨.**

---

### 4.1 종합 랭킹표

| 순위 | 이름 | Tech 25 | Impact 25 | Innov 20 | UX 15 | Pres 15 | 가중 합 | Wrapper 리스크 | 24h 난이도 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Clause50** | 4 | 5 | 4 | 5 | 5 | **89** | 🟢 낮음 | 중 |
| 2 | **AgentReady** | 5 | 4 | 5 | 4 | 5 | **89** | 🟢 매우낮음 | 중상 |
| 3 | **MCPGuard** | 5 | 4 | 5 | 3 | 4 | **85** | 🟢 최저 | 상 |
| 4 | **TrustReply** | 3 | 5 | 2 | 4 | 4 | **73** | 🟠 중상 | 하 |
| 5 | **TaskCost** | 4 | 4 | 4 | 4 | 3 | **77** | 🟢 낮음 | 중 |
| 6 | **Roundtable** | 4 | 3 | 5 | 5 | 4 | **80** | 🟡 중 | 중 |
| 7 | **RenewalRadar** | 3 | 4 | 3 | 4 | 4 | **71** | 🟠 중 | 하 |
| 8 | **RubricRoom** | 3 | 4 | 4 | 5 | 3 | **74** | 🟢 낮음 | 하 |
| 9 | **NightDesk** | 3 | 3 | 3 | 4 | 4 | **66** | 🔴 높음 | 하 |
| 10 | **VoiceIntake** | 4 | 4 | 3 | 3 | 4 | **73** | 🟡 중 | 상(라이브 실패 위험) |

> 가중 합 = (별점/5) × 배점의 합. Clause50과 AgentReady가 동점이며, **차이는 성격**입니다:
> - **Clause50** = 임팩트 서사가 가장 안전 (날짜·과징금이 문서로 존재). 리스크 낮음, 상한도 약간 낮음.
> - **AgentReady** = 데모 영상이 가장 강함. Presentation 15 + Innovation 20에서 만점을 노릴 수 있지만 "다가오는 손실"이라 Impact에서 반박 가능.
> - **하이브리드 권장**: AgentReady를 만들되 **Clause50식 "규제 마감 카운트다운" 프레이밍을 피치에 빌려올 것**. 반대로 Clause50을 만든다면 **AgentReady식 "라이브 브라우저 에이전트가 화면에서 실제로 움직이는" 데모 연출을 빌려올 것.**

### 4.2 24시간 시간 배분 권장 (Presentation 15%가 독립 배점임을 기억할 것)

| 시간 | 작업 |
| --- | --- |
| 0–1h | 스코프 확정 · Next.js + FastAPI + Postgres 스캐폴드 · 배포 파이프라인 먼저 (Vercel + Fly/Railway) |
| 1–3h | **핵심 루프 하나만** 엔드투엔드로 동작시키기 (입력 → 에이전트 → 결정론적 판정 → DB) |
| 3–9h | 판정 엔진 · 증거 저장 · 실패 분류기 (여기가 Tech 25점의 실체) |
| 9–14h | UI — 대시보드, 리포트, 점수 카드. **디자인에 최소 3시간.** |
| 14–16h | SaaS 껍데기 — 로그인, 팀, 요금제 페이지, 온보딩 빈 상태 |
| 16–18h | **리플레이/녹화 모드** (라이브 데모 실패 보험) · 시드 데이터 |
| 18–21h | **데모 영상 5분** — 첫 10초에 숫자, 중간에 실시간 에이전트, 마지막에 가격표 |
| 21–23h | **10장 덱** — 1) 문제의 숫자 2) 마감/규제 3) 제품 4) 아키텍처 5) 기술적 깊이 6) 데모 스크린샷 7) 시장 규모 8) 가격 9) 경쟁 10) 로드맵 |
| 23–24h | GitHub README(아키텍처 다이어그램 필수) · Devpost 폼 제출 |

### 4.3 Thin wrapper로 보이지 않기 위한 체크리스트

- [ ] **LLM 출력을 검증하는 결정론적 코드**가 있는가 (룰 엔진, 스키마 검증, 날짜 계산)
- [ ] **LLM이 없어도 절반은 동작**하는가 (크롤러, 프록시, 스케줄러, diff 엔진)
- [ ] 근거·인용 없이 나온 답변을 **하드하게 거부**하는가
- [ ] 아키텍처 다이어그램에 **모델 호출이 아닌 박스가 5개 이상** 있는가
- [ ] 화면에 **모델이 못 하는 것**(증적 저장, 재스캔, 정책 강제, 회귀 감지)이 보이는가
- [ ] README에 **왜 이 모델/가격 조합을 골랐는지**가 §3의 수치로 설명되어 있는가

### 4.4 반드시 피해야 할 것 (본 조사의 결론)

| 피할 것 | 이유 |
| --- | --- |
| 컨텍스트 압축 / 토큰 절감 / 에이전트 메모리 **단독 제품** | Berkeley 갤러리에 최소 8건 중복(BrowserDelta, Re:Compress, TokenC, RAVEN, compressor, Better Solutions, Accordion, Redundant). 시장에서는 에이전트 자본의 **0.6%만** 메모리로 감. |
| 범용 코딩 어시스턴트 | Cursor ARR $2B, SpaceX가 Anysphere를 **$60B에 인수**. 카테고리 종료. |
| 미팅 노트테이커 | Zoom/Teams/Granola에 무료 내장. |
| AI SDR / 콜드 아웃바운드 | 상품화 + **11x의 ARR 부풀리기·가짜 로고 적발**로 카테고리 평판 훼손. |
| 순수 의료 전사(scribe) | 단독 제품으로 사망, M&A로 통합 중. 갤러리에도 극포화. |
| 911/재난 대응 | 갤러리 최다 중복 중 하나(14건+). SaaS 트랙과도 무관. |
| 범용 학습 튜터 | 갤러리 13건+. 차별화 불가. |
| llms.txt 최적화 단독 제품 | GPTBot·ClaudeBot·PerplexityBot이 실제로는 /llms.txt를 거의 안 가져감. |

---

## 5. 참고 출처 모음

**대회**
- https://ai-builders-hackathon-2026.devpost.com/
- https://ai-builders-hackathon-2026.devpost.com/rules
- https://ai-builders-hackathon-2026.devpost.com/updates
- https://ai-builders-hackathon-2026.devpost.com/project-gallery (미공개)
- https://ai-hackathon-2026.devpost.com/project-gallery (프록시 표본 400건)

**시장 · 펀딩**
- https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/
- https://techcrunch.com/2026/08/26/viral-ai-startup-instinct-has-raised-350-million-at-a-2-5-billion-valuation/
- https://techcrunch.com/2026/08/11/general-catalyst-leads-1-1b-round-into-2-month-old-river-ai/
- https://techcrunch.com/2026/08/03/a-marc-benioff-backed-startup-thinks-ai-can-solve-the-ai-deployment-problem/
- https://techcrunch.com/2026/09/08/mistral-raises-e3b-as-sovereign-ai-becomes-big-business/
- https://techcrunch.com/2026/05/12/vapi-hits-500m-valuation-as-amazon-ring-chose-its-ai-platform-over-40-rivals/
- https://fortune.com/2026/02/24/exclusive-as-ai-threatens-search-profound-raises-96-million-to-help-brands-stay-visible/
- https://www.lawnext.com/2026/07/norm-ai-hits-unicorn-status-with-120m-series-c-at-1-2-billion-valuation.html
- https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html
- https://forkast.news/enterprise-ai-agent-funding-surges-to-435m-in-five-months-security-and-governance-lead/
- https://pulseline.substack.com/p/the-18b-agent-wave-why-vertical-ai
- https://sequoiacap.com/article/ai-in-2026-the-tale-of-two-ais/
- https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
- https://www.bvp.com/atlas/the-state-of-ai-2025
- https://www.ycombinator.com/rfs
- https://explainx.ai/blog/yc-requests-for-startups-fall-2026
- https://www.producthunt.com/leaderboard/monthly/2026/8
- https://www.producthunt.com/leaderboard/weekly/2026/36

**규제**
- https://artificialintelligenceact.eu/transparency-rules-article-50/
- https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
- https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article-50-transparency-20260729/
- https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines/

**능력 해금**
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool
- https://platform.claude.com/docs/en/managed-agents/overview
- https://platform.claude.com/docs/en/managed-agents/dreams
- https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview
- https://www.anthropic.com/news/claude-opus-5
- https://www.anthropic.com/news/claude-sonnet-5
- https://www.anthropic.com/news/model-hardware-standard-research-preview
- https://blog.modelcontextprotocol.io/posts/2026-07-28/
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/guides/live
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/
- https://ai.google.dev/gemini-api/docs/pricing
- https://developer.apple.com/wwdc26/guides/apple-intelligence/

**도메인**
- https://autorfp.ai/blog/best-security-questionnaire-software
- https://www.nops.io/blog/finops-tools-for-ai/
- https://agentlux.ai/blog/agentic-traffic-is-here-how-websites-should-prepare-for-ai-browsers-and-shopping-agents
- https://agenticplug.ai/current-state-of-agentic-commerce
- https://www.pymnts.com/visa/2026/visa-scales-agentic-commerce-through-stripe-protocol-collaboration/
- https://www.biometricupdate.com/202608/why-deepfake-detection-is-becoming-trust-infrastructure
- https://valueaddvc.com/blog/the-ai-memory-problem-how-startups-are-solving-for-persistent-context
- https://sourceryintel.com/reports/the-state-of-ai-coding-agents-2026
