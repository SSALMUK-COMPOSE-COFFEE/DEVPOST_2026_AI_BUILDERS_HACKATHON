# A. 심사위원 적합도 렌즈 — 신규 아이디어 8선

> 작성: 2026-09-15 16:30 KST · 마감까지 19.5h (실코딩 9~10h 가정)
> 렌즈: **Judge-panel fit** — 20명 심사위원이 *자기 본업에서 겪는 고통*으로 즉시 알아보는가
> 제외: 기존 10선(Clause50, AgentReady, MCPGuard, TrustReply, TaskCost, Roundtable, RenewalRadar, RubricRoom, NightDesk, VoiceIntake)과 중복되지 않는 **완전 신규 8건**

---

## 0. 이 렌즈의 선별 규칙

패널 20명은 VC도 인플루언서도 아니다. 구성은 **대기업 IC 엔지니어 7~8 + 엔터프라이즈 B2B SaaS PM 7 + QA/관측성/보안 특화 3**이다. 따라서 "시장이 크다"보다 **"이 사람이 지난주에 겪었다"** 가 훨씬 강한 무기다. 8건 전부 아래 5개를 통과시켰다.

1. **심사위원 최소 2명의 직무 기술서에 그대로 박혀 있는 문제**일 것
2. **결정론적(비-LLM) 코어**가 제품의 절반 이상을 차지할 것 — 주최측 배제 문구 `"AI wrappers with minimal differentiation"` 방어
3. **10시간 안에 라이브 URL까지** 도달 가능할 것 (Python/FastAPI + Next.js/shadcn + Postgres, hajin.xyz 서브도메인)
4. **일부러 실패시키는 데모 모먼트**가 설계 안에 있을 것 — Vudathala(관측성) · Peri(검증) 직격
5. **가격표가 자연스러울 것** — 유일한 현금상 이름이 문자 그대로 *Best SaaS Product*

### 심사위원 → 고통 매핑 (이번 8건이 노리는 표적)

| 심사위원 | 소속·직무 | 공개된 고통 신호 |
| --- | --- | --- |
| **Vasuki Uday Kiran Vudathala** | Staff Performance Engineer, ServiceNow | *"I Watched Our AI Pipeline Silently Fail While Kubernetes Said Everything Was Fine"* (HackerNoon, 2026-04-23) · *"Why GPU Utilization Is the Wrong North Star for Production AI Inference"* (HPCwire, 2026-07-21) — 새벽 2시 GPU 87%, 알럿 0건, 그런데 p99가 1.2s→6.4s |
| **Lakshmi Vidya Peri** | Board of Director, TMMi America (ex-Principal Engineer, Dell) | Dell "Modern Validation Playbook" 저자, TMMi Level 3 9년 여정 주도. 테스트 **스코어링·KPI·추적성 매트릭스**가 본업 |
| **Shania Rasheed Nalagath** | Sr. PM, Microsoft | 엔터프라이즈 AI **grounding/retrieval 인프라**, 에이전트 관리 시스템, M365 Copilot |
| **Aakanksha Joshi** | Sr. Generative & Agentic AI Solution Architect, IBM | 금융·공급망 GenAI 도입. "왜 파일럿이 프로덕션에 못 가는가"가 본업 |
| **Ishan Shah** | Staff SWE, PayPal (보안) / **Nanda Kishore Kande** Sr. SWE, Visa | 결제 승인·거절·리트라이·스킴 규칙 |
| **Udaya Bhaskar Vemuri** | Sr. Security Analyst, Corteva Agriscience | 사내 미승인 도구·데이터 유출 |
| **Gouthami Boinpally** | Sr. PM, Omnissa (ex-VMware, PayPal) | 디지털 워크스페이스 = 엔드포인트에서 직원이 뭘 쓰는지 |
| **Nilesh Dhage** | Director PM, Fidelity Investments | 금융 규제·감사 증적 |
| **Iryna Havryliuk** | Sr. PM, CareerPlug (ATS/채용 SaaS) | 지원서 홍수, 스크리닝 |
| **Sourav Sarkar** (AWS SA) · **Pulkit Arya** (Pointer) · **Anudeep Reddy Mutyala** (휴먼 승인 게이트 파이프라인) | | 마이그레이션·컴퓨터유즈·승인 게이트 |
| PM 7인 (MS×2, Fidelity, Omnissa, CareerPlug, TechCareers, Global Chamber) | | 스펙↔구현 정합, 릴리스 품질, 백로그 |

---

# 1. SilentSLO — AI 응답의 무음 실패에 SLO와 에러버짓을 붙인다

| 항목 | 내용 |
| --- | --- |
| **한 줄 태그라인** | *"Your uptime dashboard says 99.98%. Meanwhile 24% of your agent's tool-call chains silently returned garbage — with a 200 OK."* AI 기능 전용 SLO·에러버짓 SaaS. |
| **타깃 유저 (1개 역할)** | AI 기능을 프로덕션에 올린 회사의 **온콜을 도는 플랫폼/성능 엔지니어** (SRE 겸직, 팀 규모 5~50). PM도 CTO도 아니고 새벽에 페이지를 받는 사람. |
| **아픈 문제 + 출처 통계** | LLM 실패는 **HTTP 200으로 돌아온다.** 프로덕션 환각률은 태스크 형태별로 추출형 QA 3~8%, 개방형 생성 15~25%, **멀티스텝 에이전트 툴콜 체인 20~40%** ([digitalapplied.com/blog/ai-model-hallucination-rate-benchmarks-2026-study](https://www.digitalapplied.com/blog/ai-model-hallucination-rate-benchmarks-2026-study)). 그런데 탐지 경로는 대시보드가 아니라 고객이다 — *"prompt regressions surface as customer complaints rather than CI failures"*, 한 사례에서는 **컨텍스트 오버플로로 입력이 11일간 조용히 잘려나갔는데 표준 모니터링은 아무것도 표시하지 않았다** ([dev.to/.../production-llm-observability](https://dev.to/hassan_4e2f0901edda/production-llm-observability-what-youre-missing-when-your-ai-feature-goes-dark-3nli)). |
| **Why now (2026)** | ① **2026-07-21 HPCwire** 기고에서 Vudathala 본인이 *"GPU utilization belongs in capacity planning… it will not tell you whether the hardware you have is serving users well"* 라고 씀 — 인프라 지표와 사용자 체감 사이의 간극이 2026년 업계 공론이 됨 ([hpcwire.com](https://www.hpcwire.com/2026/07/21/why-gpu-utilization-is-the-wrong-north-star-for-production-ai-inference/)). ② 같은 저자의 2026-04-23 HackerNoon 글 제목이 문자 그대로 이 제품의 문제 진술문 ([hackernoon.com](https://hackernoon.com/i-watched-our-ai-pipeline-silently-fail-while-kubernetes-said-everything-was-fine)). ③ 기존 LLM 관측성 툴(Langfuse, Arize)은 **트레이스를 보여줄 뿐 SLO·에러버짓·번레이트 알럿이라는 SRE 언어로 번역하지 않는다.** |
| **10h MVP 범위** | **화면 4개**: ① Onboarding — OpenAI/Anthropic 호환 베이스 URL을 우리 프록시로 바꾸는 한 줄 코드 스니펫 + "Send test traffic" 버튼. ② **Split Dashboard** — 왼쪽 "Infra (green)" 패널(요청수·p50/p99·5xx·전부 초록), 오른쪽 "Semantic (red)" 패널(Silent Failure Rate, 에러버짓 소진율, 번레이트). ③ Failure Explorer — 실패 이벤트 리스트, 위반한 invariant 배지, 원문 diff. ④ Pricing/Settings — SLO 목표치 편집(예: Silent Failure Rate < 2%), Slack webhook. **백엔드 5개**: (a) FastAPI **OpenAI-호환 리버스 프록시** (`/v1/chat/completions` 그대로 받아 업스트림으로 패스스루, 스트리밍 포함), (b) **Invariant Engine** — 아래 결정론 섹션, (c) 분포 드리프트 모듈(거절률·응답길이·툴콜 인자 카디널리티의 **PSI + KS 검정**, 롤링 윈도), (d) **에러버짓/번레이트 계산기**(Google SRE 멀티윈도 멀티번레이트 공식, 순수 산술), (e) Postgres 이벤트 스토어 + Slack 알림 워커. |
| **결정론적(비-LLM) 코어** | **Invariant Engine.** LLM 호출 0회로 돌아가는 규칙 8종: ① JSON 스키마 검증(응답이 스키마 선언과 맞는가), ② **툴콜 인자 유효성** — 함수 시그니처와 enum/타입 대조, 존재하지 않는 인자·필수 인자 누락 탐지, ③ 빈 답변/자기반복(n-gram 루프) 탐지, ④ `finish_reason == "length"` 절단률, ⑤ **인용 앵커 검증** — 응답이 참조한 문서 ID가 실제 컨텍스트에 있었는가(문자열 대조), ⑥ 입력 토큰이 컨텍스트 한도의 X%를 넘겨 조용히 잘렸는가, ⑦ 거절 문구 패턴 급증, ⑧ 레이턴시/비용 이상치(EWMA). **즉 LLM을 끄면 제품의 80%가 그대로 동작한다.** LLM은 오직 "실패 클러스터에 사람이 읽을 이름 붙이기" 1군데만 사용. |
| **Eval / 실패 처리 데모** | 시드 트래픽 300건을 **정상 240 + 의도 주입 실패 60**(스키마 위반 15, 툴콜 인자 환각 15, 조용한 절단 15, 빈답변 15)으로 구성. 대시보드에 **Detection Precision / Recall 표**를 상시 노출: `Recall 58/60 = 96.7%, Precision 0.94, 탐지 지연 중앙값 1.2s, invariant당 비용 $0.0000`. **놓친 2건도 화면에 그대로 표시**하고 "왜 놓쳤는가(의미적 오류는 규칙으로 못 잡음)" → LLM 2차 심판으로 에스컬레이션되는 경로를 보여준다. 심사위원 앞에서 자기 제품의 한계를 먼저 말하는 팀은 1%다. |
| **데모 영상 0:10 화면** | 화면 분할. 왼쪽은 **진짜 Grafana풍 인프라 패널 — 전부 초록, "All systems operational", p99 정상.** 오른쪽 패널이 빨갛게 켜지며 **"Silent Failure Rate 24.1% · Error budget 100% burned in 3h 12m"**. 나레이션 한 줄: *"The world doesn't need another AI demo. It needs to know when the AI is already broken."* |
| **가격** | Free 10k 이벤트/월 → **Team $149/월** (100만 이벤트, SLO 5개, Slack) → **Business $599/월** (무제한 SLO, 온프렘 프록시, 감사 로그 내보내기). **좌석이 아니라 이벤트 단위** — 온콜 엔지니어가 카드로 긁을 수 있는 가격대. |
| **명명된 경쟁사 + 차별화 1문장** | **Langfuse / Arize Phoenix**: 그들은 *트레이스를 보여주고 나중에 평가하게* 해준다 — SilentSLO는 **트래픽 경로 위에 앉아, 결정론적 invariant 위반을 SLO 번레이트로 환산해 온콜 페이지를 발생시킨다.** 즉 "분석 도구"가 아니라 **"알럿 소스"** 다. |
| **별점 (Tech25/Impact25/Innov20/UX15/Pres15)** | ★★★★★ / ★★★★★ / ★★★★☆ / ★★★★☆ / ★★★★★ → **가중합 93** |
| **Thin-wrapper 리스크** | 🟢 **최저.** LLM을 끄면 80%가 동작. 오히려 "AI 해커톤에서 AI를 덜 쓴다"는 역리스크가 있으니 실패 클러스터링 1군데에 Claude를 쓰고 덱에 명시할 것. |
| **10h 실현 리스크** | 🟡 **중간.** 스트리밍 패스스루 프록시가 유일한 난관(SSE 청크를 버퍼링하면서 그대로 흘려보내기). **축소 경로**: 스트리밍 포기하고 non-stream만 지원 + 시드 트래픽 리플레이 모드. 이것만으로도 데모는 100% 성립한다. |
| **누가 반응하는가** | **Vudathala (ServiceNow)** — 그의 두 기고문 제목을 합친 것이 이 제품이다. 심사표에 그의 이름이 있는 한 이보다 정확한 저격은 없다. **Aakanksha Joshi (IBM)** — 에이전틱 도입이 프로덕션에서 죽는 지점이 정확히 여기. **Lakshmi Vidya Peri (TMMi)** — "탐지 Precision/Recall 표"는 그녀의 언어 그 자체. **Sourav Sarkar (AWS SA)** — 고객사에 "GenAI 운영 준비됐나요"를 설명할 때 쓸 슬라이드. |

---

# 2. KillScore — AI가 쓴 테스트가 실제로 버그를 잡는지 채점한다

| 항목 | 내용 |
| --- | --- |
| **한 줄 태그라인** | *"Coverage 100%. Mutation score 31%. Your AI-written tests catch 3 bugs out of 10."* PR 단위 뮤테이션 테스팅 릴리스 게이트 SaaS. |
| **타깃 유저 (1개 역할)** | 코딩 에이전트를 도입한 조직의 **QA 리드 / 릴리스 엔지니어**. "AI가 테스트도 써준다"는 말을 믿어야 하는 입장인데 근거가 없는 사람. |
| **아픈 문제 + 출처 통계** | AI가 만든 테스트는 **커버리지를 올리지만 버그를 못 잡는다.** MutGen 연구에서 바닐라 LLM 프롬프트의 뮤테이션 스코어는 **53%**, 그리고 *"a test suite with 100% coverage but 4% mutation score executes every line but misses 96% of potential bugs"* ([augmentcode.com 가이드](https://www.augmentcode.com/guides/mutation-testing-ai-generated-code)). 근본 원인도 명확하다 — **구현에서 파생된 테스트는 구현과 불일치할 수 없으며, 버그가 있으면 그 버그를 기대값으로 기록하고 초록을 띄운다.** Meta의 뮤테이션 유도 테스트 생성 연구에서는 **라인 커버리지만 봤다면 버려졌을 테스트 277건**이 실제로 유효했다 ([arxiv.org/pdf/2501.12862](https://arxiv.org/pdf/2501.12862)). |
| **Why now (2026)** | ① **GitClear "The Maintainability Gap" (2026-06)**, 623M 코드 변경 분석: 커밋의 약 1/4에 AI 흔적이 보이는 지금 **리팩터링 −70%, 중복 +81%, 복붙 +41%, 에러 은폐 catch 블록 +47%** ([gitclear.com](https://www.gitclear.com/the_ai_code_quality_maintainability_gap)). 즉 **AI가 만드는 코드량이 폭증했는데 그것을 검증하는 신호는 오히려 약해졌다.** ② 뮤테이션 테스팅은 20년 된 기술이지만 항상 **너무 느려서** 못 썼다 — PR의 **변경 라인에만** 뮤턴트를 생성하면(diff-scoped mutation) 수십 초로 떨어지고, 이게 AI가 작은 PR을 대량으로 여는 2026년에 처음으로 경제적이 된다. |
| **10h MVP 범위** | **화면 4개**: ① Repo 연결 (GitHub OAuth 또는 공개 repo URL 붙여넣기) + 데모 repo 3개 프리셋. ② **Report 화면** — 상단에 `Line coverage 100% ✅ / Mutation score 31% ❌` 대비 카드, 아래에 **생존한 뮤턴트(surviving mutants) 목록**: 원본 코드 ↔ 변형 코드 diff, "이 변형을 넣어도 테스트가 전부 통과했습니다". ③ **Fix 화면** — 생존 뮤턴트별로 Claude가 **그 뮤턴트를 죽이는 테스트**를 제안, 재실행해서 kill 확인 후에만 초록. ④ Gate/Pricing — `mutation score >= 60% 미만이면 머지 차단` 설정 + PR 체크 배지. **백엔드 4개**: (a) Git diff 파서 → 변경된 함수만 추출(Python `ast`), (b) **Mutation Engine** — AST 변환으로 뮤턴트 생성, (c) 샌드박스 러너(서브프로세스 + 타임아웃, pytest 실행), (d) 결과 스토어 + GitHub Checks 형식 JSON. |
| **결정론적(비-LLM) 코어** | **Mutation Engine 전체.** Python AST를 직접 변형하는 연산자 9종: `>` ↔ `>=`, `==` ↔ `!=`, `and` ↔ `or`, `+` ↔ `-`, 상수 ±1, `True` ↔ `False`, 조건 반전, return 값 제거, 예외 삼키기. 각 뮤턴트에 대해 테스트 스위트를 실제로 실행하고 **killed / survived / timeout**을 집계한다. 여기에는 LLM이 한 줄도 없다. **점수는 코드가 매기고, LLM은 오직 "생존 뮤턴트를 죽이는 테스트 초안"만 쓴다 — 그리고 그 초안조차 실제로 뮤턴트를 죽였는지 코드가 재검증한 뒤에만 사용자에게 보여준다.** 이것이 "reviewer, not an author" 구조. |
| **Eval / 실패 처리 데모** | 데모 repo에 **알려진 버그 10개를 심어둔** 벤치마크를 내장. 표: `AI-generated suite: coverage 100%, mutation 31%, 심은 버그 10개 중 3개 탐지` vs `KillScore 보강 후: mutation 78%, 10개 중 9개 탐지`. **실패 처리**: Claude가 제안한 테스트 중 일부는 여전히 뮤턴트를 못 죽인다 → 화면에 `Proposed test did NOT kill mutant #7 — rejected, escalated to human` 배지가 빨갛게 뜨고 큐로 넘어간다. **LLM 출력을 제품이 스스로 거부하는 장면**을 카메라에 담는 것이 이 데모의 핵심. |
| **데모 영상 0:10 화면** | 초록색 pytest 출력 `47 passed in 2.31s`와 `Coverage: 100%` 위로, 빨간 카드가 슬라이드인: **"Mutation score: 31%. We flipped `>` to `>=` in your payment logic and every test still passed."** 그리고 그 뮤턴트 diff가 실제 결제 코드 한 줄로 확대된다. |
| **가격** | Free 공개 repo 무제한(오픈소스 — 주최 OSC 취향 정렬) → **Team $99/월** (비공개 repo 5개, PR 게이트) → **Business $399/월** (무제한 repo, TMMi 형식 **증적 PDF 내보내기**, SSO). |
| **명명된 경쟁사 + 차별화 1문장** | **Codecov / SonarQube**: 그들은 *"코드가 실행됐는가"* 를 잰다 — KillScore는 **"테스트가 반증할 능력이 있는가"** 를 재며, 커버리지와 달리 **코드를 더 실행한다고 점수가 오르지 않는다.** (오픈소스 `mutmut`/`cosmic-ray` 대비: 그것들은 전체 repo를 몇 시간 돌리는 CLI이고, KillScore는 **PR diff 범위로 한정해 수십 초에 끝내는 SaaS 게이트**다.) |
| **별점** | ★★★★★ / ★★★★☆ / ★★★★☆ / ★★★★☆ / ★★★★★ → **가중합 88** |
| **Thin-wrapper 리스크** | 🟢 **매우 낮음.** 핵심이 AST 변환 + 서브프로세스 실행이다. |
| **10h 실현 리스크** | 🟡 **중간.** 임의의 repo를 안전하게 실행하는 것이 위험 — **축소 경로: 큐레이션된 데모 repo 3개만 지원**하고 "Bring your own repo"는 웨이팅 리스트로. 심사위원에게는 오히려 "샌드박스 보안을 고려해 화이트리스트로 시작했다"가 성숙해 보인다. 뮤테이션 연산자는 5종으로 줄여도 데모 성립. |
| **누가 반응하는가** | **Lakshmi Vidya Peri (TMMi America, ex-Dell)** — Dell "Modern Validation Playbook" 저자이자 **테스트 스코어링·KPI 플랫폼을 직접 구축한 사람**. 뮤테이션 스코어는 TMMi Level 4~5 측정 언어 그 자체이고, 증적 PDF 내보내기는 그녀가 9년간 한 일이다. **Disha Patel (Apple)** · **Ishan Shah (PayPal)** — 결제 로직에서 `>`가 `>=`로 바뀌는 예시는 모든 대기업 엔지니어의 트라우마. **Pulkit Arya (Pointer)** — 에이전트가 쓴 코드를 신뢰할 근거를 파는 입장. |

---

# 3. SpecDrift — 머지된 PR과 수용기준(AC) 사이의 추적성 매트릭스를 자동으로 만든다

| 항목 | 내용 |
| --- | --- |
| **한 줄 태그라인** | *"Your team merged 47 PRs this sprint. 12 of them don't map to a single acceptance criterion, and 5 acceptance criteria shipped nothing."* 스펙↔코드 드리프트 레이더 SaaS. |
| **타깃 유저 (1개 역할)** | 엔지니어링 팀 2~4개를 담당하는 **B2B SaaS 프로덕트 매니저**. 스프린트 리뷰에서 "우리가 약속한 걸 실제로 냈나"를 증명해야 하는 사람. |
| **아픈 문제 + 출처 통계** | 2026년의 병목은 생성 속도가 아니라 드리프트다 — *"the problem isn't generation speed — it's drift: confident, plausible code that quietly solves the wrong problem because nobody grounded the work in a real specification"*, 그리고 *"AI coding agents ship features fast, but specs, tests, and code quietly drift apart"* ([glukhov.org](https://www.glukhov.org/app-architecture/testing-architecture/specs-tests-code-traceability-ai-development), [augmentcode.com](https://www.augmentcode.com/guides/what-is-spec-driven-development)). 코드량 자체가 폭증한 증거는 GitClear: **리팩터링 −70%, 중복 +81%** (623M 변경, 2026-06). PM은 PR 47건을 읽을 시간이 없다. |
| **Why now (2026)** | ① 2026년에 **모든 메이저 AI 코딩 툴이 SDD(Spec-Driven Development)를 출시**했다 — GitHub Spec Kit, AWS Kiro, Claude Code, Cursor, OpenSpec, BMAD, Tessl, Google Antigravity ([thebcms.com](https://www.thebcms.com/blog/spec-driven-development/)). **즉 "스펙 파일"이 레포 안에 기계가 읽을 수 있는 형태로 처음 존재하게 됐다.** ② 그런데 SDD 툴은 전부 **"스펙으로 코드를 생성"** 하는 방향뿐이고, **"이미 머지된 코드가 스펙을 지켰는지 역방향으로 검증"** 하는 제품은 비어 있다. ③ 요구사항 ID ↔ 설계 ↔ 테스트의 매핑(RTM)은 TMMi가 요구하는 산출물인데, 지금까지 손으로 만들었다. |
| **10h MVP 범위** | **화면 4개**: ① Import — Jira/Linear CSV 업로드 또는 마크다운 PRD 붙여넣기 + GitHub repo 연결(공개 repo면 토큰 불필요). ② **Traceability Matrix** — 행=AC, 열=PR/커밋/테스트. 셀 상태 4종: `✅ Covered` / `⚠️ Partial (코드는 있는데 테스트 없음)` / `🔴 Orphan PR (어떤 AC에도 안 붙음)` / `👻 Ghost AC (아무것도 안 나감)`. ③ **Drift Detail** — 한 AC를 클릭하면 근거(PR 링크, 변경 파일, 매칭된 테스트 이름, 매칭 점수)와 **Claude의 1문장 diff 요약 + "이 PR은 AC를 초과 구현했습니다" 판정**. ④ Sprint Report — PDF 내보내기 + 가격표. **백엔드 5개**: (a) GitHub API 수집기(PR 제목/본문/변경파일/커밋 메시지), (b) **ID Linker** — `PROJ-123` 패턴, 브랜치명, PR 본문의 `Closes #` 를 정규식으로 추출(결정론), (c) **Semantic Matcher** — 임베딩 코사인 유사도 + 임계값, (d) **Matrix Builder** — 커버리지 상태 4종을 순수 집합 연산으로 계산, (e) PDF 생성기(WeasyPrint). |
| **결정론적(비-LLM) 코어** | **Traceability Matrix 계산 전체.** ① 정규식 ID 추출 → 명시적 링크는 100% 확정(LLM 불필요), ② 임베딩 유사도는 **임계값 위/아래로 이진 분류**되며 그 임계값은 우리가 튜닝한 숫자다, ③ **매트릭스의 4상태는 전부 집합 연산** — `AC ∩ PR`, `AC \ PR`(Ghost), `PR \ AC`(Orphan), `PR ∩ AC \ Test`(Partial). ④ LLM은 **판정을 내리지 않는다** — 오직 매칭된 쌍에 대한 사람 읽을 요약 1줄만 생성하며, **인용(PR 번호 + 파일 경로) 없이 생성된 요약은 하드 거부**된다. |
| **Eval / 실패 처리 데모** | 실제 오픈소스 repo(예: FastAPI 또는 자기 repo)의 스프린트 1개를 **사람이 손으로 라벨링한 정답 매트릭스**와 대조. 표: `Precision 0.91 / Recall 0.84 / Orphan PR 오탐 3건`. **실패 데모**: 리팩터링 전용 PR을 시스템이 Orphan으로 잘못 찍는다 → 화면에서 **"Not every PR should map to an AC"** 라는 사용자 피드백 버튼을 눌러 `Excluded: chore/refactor` 라벨로 학습시키고, **오탐률이 표에서 실시간으로 내려가는 것**을 보여준다. 휴먼 인 더 루프가 제품 기능으로 존재한다는 증명. |
| **데모 영상 0:10 화면** | 12×20 매트릭스가 한 화면에 깔리고, **빨간 셀 5개와 주황 셀 12개가 순차적으로 켜진다.** 상단 헤더: **"Sprint 24: 5 acceptance criteria shipped nothing. 12 PRs answer to no one."** PM이 스프린트 리뷰 전날 밤에 보고 싶은 정확히 그 화면. |
| **가격** | Free 공개 repo 1개 → **Team $79/월** (repo 5개, 스프린트 리포트) → **Business $349/월** (무제한, **RTM 감사 증적 내보내기**, Jira 양방향). |
| **명명된 경쟁사 + 차별화 1문장** | **Jellyfish / LinearB**: 그들은 *엔지니어링 산출량(사이클 타임, DORA)* 을 잰다 — SpecDrift는 **산출물이 약속과 일치하는가**를 재며, 출력이 지표가 아니라 **감사 가능한 추적성 매트릭스**다. |
| **별점** | ★★★★☆ / ★★★★☆ / ★★★★☆ / ★★★★★ / ★★★★☆ → **가중합 83** |
| **Thin-wrapper 리스크** | 🟡 **중간.** "LLM으로 PR과 티켓을 매칭했다"로 보일 수 있음. **방어**: 매트릭스 4상태 계산이 집합 연산임을 아키텍처 슬라이드에 수식으로 박고, **명시적 ID 링크 비율(예: 68%는 LLM 없이 확정)** 을 화면에 상시 표시할 것. |
| **10h 실현 리스크** | 🟢 **낮음.** GitHub API + 임베딩 + 매트릭스 렌더링. 가장 안전한 축에 속한다. 데이터는 공개 repo에서 즉시 얻는다. |
| **누가 반응하는가** | **PM 7인 전체가 표적** — 이 패널의 최대 단일 블록이다. **Gouthami Boinpally (Omnissa)**, **Nilesh Dhage (Fidelity)**, **Aniruddha Nikam (TechCareers)**, **Shania Rasheed Nalagath (Microsoft)** 모두 스프린트 리뷰에서 이 질문을 받는 쪽이다. 동시에 **Lakshmi Vidya Peri** 에게는 RTM(Requirements Traceability Matrix)이 TMMi 필수 산출물이라 **엔지니어링 심사위원과 PM 심사위원을 하나의 화면으로 동시 만족**시키는 유일한 후보. |

---

# 4. ShadowLedger — OAuth·SSO 로그에서 사내 미승인 AI 도구를 찾아내고 데이터 유출 반경을 계산한다

| 항목 | 내용 |
| --- | --- |
| **한 줄 태그라인** | *"Shadow AI adds $670,000 to the average breach. We found 23 unsanctioned AI apps in your Workspace logs in 90 seconds — and 4 of them can read every file in Drive."* |
| **타깃 유저 (1개 역할)** | 직원 200~2,000명 기업의 **보안 분석가 / IT 관리자** (전담 CASB 예산은 없고 Google Workspace나 Okta 로그는 있는 조직). |
| **아픈 문제 + 출처 통계** | IBM **Cost of a Data Breach 2025**: 섀도우 AI가 얽힌 침해는 평균 **$4.63M — 일반 사건보다 $670,000 비쌌고**, 조사 대상 조직의 **5곳 중 1곳(20%)** 이 섀도우 AI 관련 침해를 겪었다. AI 관련 침해를 보고한 조직의 **97%가 적절한 접근 통제가 없었다**고 답했고, 섀도우 AI 침해의 **65%가 고객 PII를 노출**했다 ([kiteworks.com 요약](https://www.kiteworks.com/cybersecurity-risk-management/ibm-2025-data-breach-report-ai-risks/), [nudgesecurity.com](https://www.nudgesecurity.com/post/shadow-ai-the-emerging-security-threat-in-ibms-2025-cost-of-a-data-breach-report)). |
| **Why now (2026)** | ① 2025~2026년에 **AI 도구의 기본 진입 경로가 "Sign in with Google/Microsoft"** 가 됐다 — 즉 직원이 설치한 모든 AI 앱이 **IdP 로그에 OAuth grant로 흔적을 남긴다.** 이건 예전 섀도우 IT(네트워크 프록시 로그 필요)와 결정적으로 다르다. ② MCP·에이전트가 확산되면서 요청 스코프가 `drive.readonly`가 아니라 **`drive` 전체 쓰기, `gmail.modify`** 로 커지고 있다 — 권한 인플레이션 자체가 새 신호다. ③ IBM 2025 리포트가 **섀도우 AI를 처음으로 별도 비용 항목으로 계량**하면서 예산이 생겼다. |
| **10h MVP 범위** | **화면 4개**: ① Import — Google Workspace **OAuth Token Audit CSV** 또는 Okta 시스템 로그 CSV 드래그앤드롭 (+ 샘플 데이터 버튼). ② **Inventory** — 발견된 앱 테이블: 앱명, 사용자 수, 최초 승인일, 요청 스코프, **Risk Score 0~100**, `Sanctioned / Unknown / AI-suspected` 라벨. ③ **Blast Radius** — 앱 하나를 고르면 "이 앱이 접근 가능한 것"을 시각화: `Drive 전체 읽기+쓰기 · Gmail 읽기 · 사용자 41명 · 예상 노출 문서 수`. ④ **Actions & Pricing** — 앱별 "Revoke 스크립트 생성"(실행은 사람이) + 정책(`새 AI 앱이 drive 쓰기 스코프를 요청하면 Slack 알림`). **백엔드 4개**: (a) CSV 정규화 파서(Workspace/Okta 두 포맷), (b) **Scope Risk Engine**(아래), (c) **AI App Classifier** — 도메인/클라이언트ID를 내장 카탈로그와 대조, 미상만 LLM에게 물음, (d) 시계열 스토어 + 신규 앱 탐지 크론. |
| **결정론적(비-LLM) 코어** | **Scope Risk Engine.** OAuth 스코프 문자열을 파싱해 권한 등급표(read < modify < full)에 매핑하고, `민감 서비스 가중치 × 권한 등급 × 영향 사용자 수 × 미승인 여부`로 Risk Score를 **산술 계산**한다. 여기에 **200여 개 알려진 AI 앱 클라이언트ID 카탈로그**(하드코딩 JSON)와의 정확 일치. **LLM은 카탈로그에 없는 미상 앱의 도메인만 받아 "이것이 AI 서비스인가"를 판정**하고, 그 판정은 반드시 `evidence_url` 필드를 동반해야 하며 없으면 `UNKNOWN`으로 강등된다. 즉 **점수는 코드, 분류만 LLM, 그마저 근거 강제.** |
| **Eval / 실패 처리 데모** | 합성 로그 500행(승인 앱 30 + AI 앱 23 + 무관한 SaaS 47)에 대해 **분류 Precision/Recall 표**를 화면에 상시 노출: `AI 앱 탐지 Recall 21/23 = 91.3%, 오탐 2건`. **실패 처리**: LLM이 사내 자체 툴을 "AI 앱"으로 오탐 → 사용자가 `Mark as sanctioned` 클릭 → **allowlist에 들어가고 이후 스캔에서 영구 제외**되는 걸 보여준다. 그리고 **"우리는 절대 자동으로 revoke하지 않습니다 — 스크립트를 드릴 뿐입니다"** 를 명시(confirm-before-act). |
| **데모 영상 0:10 화면** | CSV 한 개를 드롭하는 순간 테이블이 촤르륵 채워지고, 상단 카운터가 회전하며 멈춘다: **"23 unsanctioned AI apps · 4 with full Drive write · 312 employees affected · Estimated breach premium $670,000."** 마지막 숫자 옆에 IBM 리포트 출처가 작게 박혀 있다. |
| **가격** | Free 1회 스캔(직원 100명까지) → **Team $249/월** (지속 모니터링, 주간 diff, Slack) → **Business $899/월** (다중 테넌트, SIEM 내보내기, 감사 증적). **좌석이 아니라 모니터링 대상 직원 수** 단위. |
| **명명된 경쟁사 + 차별화 1문장** | **Nudge Security / Netskope**: 그들은 *전사 SaaS 거버넌스 플랫폼*이라 도입에 몇 주와 에이전트 설치가 필요하다 — ShadowLedger는 **이미 가지고 있는 CSV 한 장으로 90초 만에 첫 리포트를 내는 "AI 앱 전용" 단일 목적 도구**다. |
| **별점** | ★★★★☆ / ★★★★★ / ★★★☆☆ / ★★★★☆ / ★★★★☆ → **가중합 81** |
| **Thin-wrapper 리스크** | 🟢 **낮음.** 파서 + 점수 엔진 + 카탈로그가 전부 코드. |
| **10h 실현 리스크** | 🟢 **낮음.** 입력이 CSV라 외부 의존이 0이다. 가장 안전한 후보. 다만 **UI가 테이블 위주라 지루해질 수 있으니 Blast Radius 시각화에 시간을 배분할 것.** |
| **누가 반응하는가** | **Udaya Bhaskar Vemuri (Sr. Security Analyst, Corteva Agriscience)** — 직무가 그대로 타깃 페르소나다. **Gouthami Boinpally (Omnissa)** — Omnissa는 VMware EUC 분사, 즉 "직원 엔드포인트에서 무슨 일이 일어나는가"가 회사의 제품 자체. **Nilesh Dhage (Fidelity)** · **Ishan Shah (PayPal 보안)** — 금융권에서 섀도우 AI는 이미 이사회 안건. |

---

# 5. RetryRail — 카드 네트워크 리트라이 규칙을 강제하는 결정론적 결제 재시도 엔진

| 항목 | 내용 |
| --- | --- |
| **한 줄 태그라인** | *"Visa caps you at 15 retries per 30 days. Mastercard at 10. We replayed your last 30 days of declines and found 4,112 illegal attempts — and 1,847 soft declines you never retried at all."* |
| **타깃 유저 (1개 역할)** | 구독형 SaaS·커머스의 **결제/빌링 엔지니어** (Stripe 위에 직접 재시도 로직을 짜 둔 사람). |
| **아픈 문제 + 출처 통계** | 리트라이 규칙은 **네트워크가 벌금으로 강제**한다: Visa는 30일 내 단일 거래 재시도를 **최대 15회**로 제한하고 초과 국내 시도당 약 **$0.10**, Mastercard는 **10회** 제한에 2025년 1월부터 초과 승인 수수료가 건당 **최대 $0.50** ([slickerhq.com 2026-06 정리](https://www.slickerhq.com/resources/blog/visa-mastercard-payment-retry-rules)). 반대 방향의 손실은 더 크다 — **false decline은 2026년 이커머스에서 $231B 규모로 추산**되고, **거절 거래의 60~65%가 실제로는 정상 고객**이다 ([ecommercegermany.com](https://ecommercegermany.com/blog/false-decline-ecommerce/), [beastinsights.com](https://beastinsights.com/blog/false-decline)). 그런데 대부분의 팀은 **decline code별 재시도 적격성 테이블을 코드에 안 갖고 있다** — `if failed: retry in 3 days`가 전부다. |
| **Why now (2026)** | ① Mastercard 초과 승인 수수료가 **2025-01부터 최대 $0.50/건**으로 인상되면서 무지성 재시도가 처음으로 **눈에 보이는 비용**이 됐다. ② 에이전틱 커머스(ACP/UCP/AP2, Visa TAP)로 **사람이 없는 재시도**가 늘어나면서 스킴 규칙 위반이 자동으로 누적되는 구조가 생겼다. ③ 첫 재시도가 soft decline의 **40~60%를 회수**하지만 3회차 이후 급감한다는 데이터가 공개되면서, "몇 번"이 아니라 **"어떤 코드를 언제"** 가 문제라는 게 확정됐다. |
| **10h MVP 범위** | **화면 4개**: ① Import — Stripe 테스트 모드 API 키 연결 또는 **거래 CSV 업로드**(`charge_id, amount, decline_code, network, timestamp, card_fingerprint`) + 샘플 데이터. ② **Audit** — 상단 3개 카드: `Illegal retries: 4,112 ($411 in scheme fines)` / `Missed recoverable declines: 1,847 ($92,350 unrecovered)` / `Compliance score: 62/100`. 아래 decline code별 테이블: 코드, 분류(soft/hard), 시도 횟수, **규칙 위반 여부**, 권장 케이던스. ③ **Simulator** — 케이던스를 슬라이더로 바꾸면 **과거 30일 데이터를 그 규칙으로 리플레이**해서 회수액·벌금·시도수가 실시간으로 다시 계산됨. ④ **Policy Export** — 확정한 규칙을 JSON/Python 스니펫으로 내보내기 + 가격표. **백엔드 4개**: (a) CSV/Stripe 정규화, (b) **Scheme Rule Engine**(아래), (c) **Replay Simulator** — 순수 함수, (d) 리포트 PDF. |
| **결정론적(비-LLM) 코어** | **Scheme Rule Engine이 제품 전체다.** 네트워크별 decline code 테이블(Visa 카테고리 1~4, Mastercard, Amex)을 하드코딩하고, 각 코드에 `retriable: bool`, `max_attempts`, `min_interval_hours`, `window_days`, `fine_per_excess_usd`를 부여. 거래 로그를 **카드 fingerprint × 30일 슬라이딩 윈도**로 그룹핑해 위반을 **수학적으로 카운트**한다. 시뮬레이터도 순수 함수다. **LLM은 단 한 곳** — "이 decline code가 왜 위험한지, 이 고객에게 보낼 결제수단 갱신 이메일 초안"을 쓰는 데만 쓰이고, **금액·횟수·적격성 판정에는 절대 관여하지 않는다.** 이걸 아키텍처 슬라이드에 빨간 선으로 그려라. |
| **Eval / 실패 처리 데모** | 5,000건 합성 거래(의도적으로 규칙 위반 4,112건 포함)에 대해 **정답 라벨과 대조한 표**: `위반 탐지 Recall 100% (결정론이므로), 오탐 0`. 그리고 **회수 시뮬레이션의 정직성**: `우리 케이던스로 리플레이 시 예상 회수 $92,350 — 단, 이는 "soft decline 첫 재시도 회수율 40~60%" 문헌값을 적용한 추정이며 보수적 하한(40%)을 표시합니다.` **추정치에 신뢰구간을 붙이고 근거를 링크하는 것 자체가 이 패널에게는 가점이다.** 실패 처리: 알 수 없는 decline code가 들어오면 → **`UNKNOWN: do not retry` 로 안전측 폴백**하고 사람 검토 큐로. |
| **데모 영상 0:10 화면** | CSV 드롭 → 카운터가 돌다 멈춤: **"4,112 retries you were not allowed to make. $411 in scheme fines. And 1,847 declines you gave up on that Visa says you could have recovered."** 오른쪽에 규칙 슬라이더를 움직이자 숫자 3개가 동시에 재계산되는 장면. |
| **가격** | Free 1회 감사(거래 10k까지) → **Team $199/월** (지속 감사 + 정책 내보내기) → **Business GMV의 0.05%**, 최소 $799/월. |
| **명명된 경쟁사 + 차별화 1문장** | **Gravy / Butter Payments / Churnbuster**: 그들은 *ML 블랙박스로 "언제 재시도할지"를 추측*하고 성과 기반 수수료를 받는다 — RetryRail은 **네트워크 규칙을 명문화된 테이블로 강제해 "재시도해서는 안 되는 시도"를 먼저 없애는 컴플라이언스 레이어**이며, 결과를 감사 가능한 규칙으로 내보낸다(블랙박스 아님). |
| **별점** | ★★★★☆ / ★★★★★ / ★★★☆☆ / ★★★★☆ / ★★★★☆ → **가중합 81** |
| **Thin-wrapper 리스크** | 🟢 **매우 낮음** (오히려 LLM 사용량이 너무 적어 "AI 해커톤" 적합성이 약함 — 이메일 초안 생성과 "미상 코드 조사 에이전트"를 명확히 1~2군데 배치하고 덱에서 설명할 것). |
| **10h 실현 리스크** | 🟢 **낮음.** 규칙 테이블 작성(1.5h)이 가장 지루한 부분. Stripe 테스트 모드 연동은 선택으로 두고 CSV만으로 시작. **Best SaaS Product 상 특성상 Stripe 결제 화면이 제품 안에 자연스럽게 들어간다는 부수 이점**이 있다. |
| **누가 반응하는가** | **Nanda Kishore Kande (Sr. SWE, Visa)** — Visa 규칙 테이블이 화면에 그대로 뜨는 걸 보면 진위를 즉시 판별할 수 있고, 맞으면 강하게 반응한다. **Ishan Shah (Staff SWE, PayPal)** — 같은 규칙과 싸운 사람. **Gouthami Boinpally** (前 PayPal) · **Nilesh Dhage (Fidelity)** 도 도메인을 안다. ⚠️ **반대로 나머지 14명에게는 설명에 30초가 든다** — 이것이 이 아이디어의 유일한 구조적 약점. |

---

# 6. ApplyGuard — 지원자를 채점하지 않고 "지원서 공장"만 찾아낸다

| 항목 | 내용 |
| --- | --- |
| **한 줄 태그라인** | *"11,000 applications per minute, up 45% in a year. ApplyGuard flags the 340 that came from 7 automation farms — and never scores a single human."* |
| **타깃 유저 (1개 역할)** | 중견 ATS 벤더 또는 채용 대행사의 **채용 오퍼레이션 매니저** (하루 수백~수천 건의 지원서를 받는 쪽). |
| **아픈 문제 + 출처 통계** | LinkedIn에서 **분당 약 11,000건의 지원서**가 제출되며 이는 **1년 만에 45% 증가**한 수치로, 주된 원인이 생성형 AI다 ([clever.cv 정리](https://www.clever.cv/blog/ai-job-application-flood-how-to-stand-out-2026)). 채용팀의 **77%가 AI 생성/보조 지원서를 정기적으로 접한다**(2024년 초 53% → 2026년 77%, Willo Hiring Trends Report 2026). 단일 원격 공고에 **1,200건 이상**이 몰려 공고 자체를 내린 사례도 보고됐다. |
| **Why now (2026)** | ① 지원서 자동 제출 에이전트(컴퓨터 유즈 기반)가 2026년에 대중화되면서 **한 사람이 수백 곳에 동일 템플릿을 뿌리는 것이 기본값**이 됐다. ② 동시에 **NYC Local Law 144, EU AI Act** 등으로 **"AI가 지원자를 채점하는 것" 자체가 규제 대상**이 됐다 — 그래서 시장에 나온 AI 스크리닝 툴들이 법무 리뷰에서 막힌다. ③ **이 두 사실의 교집합이 빈 니치**다: *지원자를 평가하지 않으면서* 홍수를 줄이는 방법. |
| **10h MVP 범위** | **화면 4개**: ① Import — 지원서 CSV/JSON 업로드(이름 익명화 옵션) + 데모 데이터셋. ② **Farm Map** — 지원서를 노드로 그린 **클러스터 그래프**: 같은 템플릿 지문을 공유하는 지원서들이 덩어리로 묶여 보임. 클러스터별 배지: `Farm #3 · 47 applications · identical structure, swapped keywords · submitted within 11 minutes`. ③ **Evidence** — 클러스터 하나를 열면 두 지원서를 나란히 diff(공통 문장 하이라이트), 제출 타임스탬프 히스토그램, 연락처 도메인 분포. ④ **Queue & Pricing** — `Deprioritize farm / Keep all / Export flags`(자동 거절 없음, 명시적으로 불가) + 가격표. **백엔드 4개**: (a) 정규화·익명화 파서, (b) **Fingerprint Engine**(아래), (c) 클러스터링(연결 요소 탐색), (d) 결과 스토어 + 공정성 리포트 생성기. |
| **결정론적(비-LLM) 코어** | **Fingerprint Engine.** ① **MinHash + LSH**로 지원서 본문의 shingle 유사도를 계산해 근접 중복을 O(n)에 찾음, ② **구조 지문** — 문단 수·문장 길이 분포·불용어 비율의 벡터(내용이 아니라 형태), ③ **제출 버스트 탐지** — 타임스탬프의 포아송 검정, ④ 연락처/도메인/UTM 파라미터 정확 일치. **이 4개 신호 전부에 LLM이 없고, 전부 지원자 개인의 자질과 무관하다.** 제품이 출력하는 것은 "이 지원서가 좋은가"가 아니라 **"이 47건이 서로 같은 기계에서 나왔는가"** 다. LLM은 클러스터에 사람이 읽을 이름을 붙이는 데만 쓰인다(`"Farm #3: cover letters differ only in company name"`). |
| **Eval / 실패 처리 데모** | 합성 데이터셋 800건(진짜 사람 700 + 심어놓은 farm 100, 7개 클러스터)으로 **표**: `클러스터 탐지 Recall 94/100, Precision 0.97, 오탐 3건`. **그리고 공정성 테스트를 별도 표로**: `비영어권 이름 그룹 / 영어권 이름 그룹의 flag rate 차이 = 0.4%p (통계적 유의하지 않음)` — **AI 채용 툴에 대한 규제 환경에서 "우리는 편향을 측정했다"를 먼저 보여주는 것이 이 제품의 가장 강한 카드.** 실패 처리: 오탐 3건을 화면에 그대로 띄우고 *"These 3 were real people using the same résumé template. We show you the evidence; you decide. ApplyGuard never rejects anyone."* |
| **데모 영상 0:10 화면** | 800개의 점이 흩뿌려진 화면에서 **7개의 덩어리가 색을 띠며 수축**한다. 헤더: **"7 farms. 340 applications. 4 minutes of your recruiter's day instead of 6 hours."** 그리고 바로 다음 컷에 빨간 배너: **"ApplyGuard does not score candidates. Ever."** |
| **가격** | Free 지원서 500건/월 → **Team $149/월** (10,000건, ATS webhook) → **Business $699/월** (무제한, 공정성 감사 리포트, SSO). |
| **명명된 경쟁사 + 차별화 1문장** | **HireVue / Paradox / 각종 AI 스크리너**: 그들은 *지원자를 점수화*해서 법무·규제 리스크를 떠안는다 — ApplyGuard는 **지원자를 절대 평가하지 않고 제출 행위의 기계적 지문만 본다**, 그래서 NYC LL144 편향 감사의 대상 자체가 아니다. |
| **별점** | ★★★★☆ / ★★★★☆ / ★★★★☆ / ★★★★☆ / ★★★★☆ → **가중합 80** |
| **Thin-wrapper 리스크** | 🟢 **낮음.** MinHash/LSH/포아송 검정은 전부 코드. |
| **10h 실현 리스크** | 🟢 **낮음.** 합성 데이터 생성 1h + 알고리즘 2h + 그래프 UI 3h. 다만 **그래프 시각화(d3/react-force-graph)가 예상보다 시간을 먹을 수 있음** — 축소 경로: 그래프 대신 클러스터 카드 리스트. |
| **누가 반응하는가** | **Iryna Havryliuk (Sr. PM, CareerPlug)** — CareerPlug가 곧 ATS다. 이 문제는 그녀 회사의 고객 지원 티켓이다. 20명 중 이 아이디어를 **가장 강하게 단독으로 밀어줄 사람**. **Ashish Tripathi (Founder, GraphicNote / Enterprise SaaS PM)** · **Aniruddha Nikam (TechCareers)** — 채용 도메인 인접. ⚠️ 엔지니어 심사위원 8명에게는 도메인 매력이 약하다 — **MinHash/LSH 알고리즘 슬라이드로 기술 점수를 보충할 것.** |

---

# 7. EOLRadar — 당신의 AI 스택이 며칠 뒤에 죽는지 센다

| 항목 | 내용 |
| --- | --- |
| **한 줄 태그라인** | *"OpenAI shut the Assistants API down on Aug 26 with no automated migration. Your repo still imports it. EOLRadar found 3 hard shutdown dates in your stack — the nearest is in 47 days."* |
| **타깃 유저 (1개 역할)** | AI 기능을 서비스에 붙여둔 회사의 **백엔드 테크리드** (모델·API를 고르고 나면 다시 안 보는 사람). |
| **아픈 문제 + 출처 통계** | 2026년 AI 스택의 폐기 주기는 인프라 주기보다 짧다. **OpenAI Assistants API는 2026-08-26에 실제로 종료됐고 자동 마이그레이션이 제공되지 않았다** ([OpenAI Deprecations](https://developers.openai.com/api/docs/deprecations), [techtimes.com 2026-08-24](https://www.techtimes.com/articles/325345/20260824/openai-assistants-api-shuts-down-tuesday-no-automated-migration-threads-risk.htm)). 같은 날 **whisper-1, gpt-4o-transcribe, gpt-4o-mini-transcribe, gpt-4o-transcribe-diarize가 deprecation 통보**를 받았고 **2027-02-26 제거** 예정이다. 그리고 **OpenAI만 2026년 하반기에 7개의 셧다운 데드라인**을 갖고 있다 ([ampm-aiops.com](https://ampm-aiops.com/en/guides/openai-shutdown-deadlines-h2-2026/)). |
| **Why now (2026)** | ① 위 날짜들이 **전부 2026년 하반기~2027년 초에 몰려 있다** — 지금이 정확히 그 창. ② 가격 만료도 같은 성격의 시한폭탄이다: **Gemini 3.8 Flash의 $0.75/$3.75는 2026-12-31까지의 도입가이며 2027-01-01에 약 2배**가 된다. ③ **MCP 2026-07-28 스펙**이 `Mcp-Session-Id` 헤더와 `initialize` 핸드셰이크를 제거하며 **12개월 지원 중단 창**을 열었다 ([blog.modelcontextprotocol.io](https://blog.modelcontextprotocol.io/posts/2026-07-28/)). ④ **이 정보는 지금 벤더별 문서 페이지에 흩어져 있고, 아무도 자기 repo와 대조해주지 않는다.** |
| **10h MVP 범위** | **화면 4개**: ① Scan — 공개 GitHub repo URL 붙여넣기 또는 `requirements.txt`/`package.json` 업로드 (+ "Scan this repo" 데모 버튼). ② **Countdown Board** — 발견된 항목을 **남은 일수 오름차순**으로 카드 배열: `gpt-4o-transcribe · REMOVED in 164 days · found in 3 files · 🔴 BREAKING` / `gemini-3.8-flash pricing · 2x price in 107 days · 💰 COST` / `mcp session header · unsupported in 316 days · 🟡 SPEC`. ③ **Evidence & Fix** — 항목 클릭 시 정확한 파일:라인, 벤더 공지 원문 링크, 그리고 **Claude가 생성한 마이그레이션 diff**. ④ **Watch & Pricing** — repo 워치 등록(주간 재스캔 + 이메일) + 가격표. **백엔드 4개**: (a) 코드/락파일 **정적 스캐너**(정규식 + AST로 모델 ID 문자열·SDK import·엔드포인트 경로 추출), (b) **Deprecation Calendar DB**(아래), (c) **Date Math + 심각도 분류기**, (d) 주간 크론 + 이메일. |
| **결정론적(비-LLM) 코어** | **Deprecation Calendar DB + 정적 스캐너.** 벤더 공지에서 수집한 큐레이션 테이블(모델/API 식별자 → `deprecated_on`, `shutdown_on`, `replacement`, `source_url`, `severity`)에 **60~100행**을 채워 넣고, 스캐너가 repo에서 찾은 리터럴과 **정확 문자열 매칭**한다. 남은 일수와 심각도는 산술과 분기문이다. **LLM은 오직 마이그레이션 diff 초안 생성 1군데**에만 쓰이고, **날짜·매칭·경보에는 전혀 관여하지 않는다** — 환각한 날짜로 사람을 깨우는 것이 이 카테고리 최악의 실패이므로. |
| **Eval / 실패 처리 데모** | 공개 repo 15개(일부러 구형 SDK를 쓰는 것 포함)를 스캔한 **벤치마크 표**: `탐지 26/28 = 92.9%, 오탐 1건, 평균 스캔 4.1s`. **실패 처리 데모 (이 제품의 하이라이트)**: 화면에 **"⚠️ We do not trust the model for dates"** 배너가 있고, 그 옆에서 일부러 Claude에게 *"When is whisper-1 removed?"* 를 물어 **모델이 틀린 날짜를 말하는 장면**을 보여준 뒤, 우리 캘린더 DB가 **2027-02-26 + 출처 링크**를 반환하는 걸 대비시킨다. *"This is exactly why the date never comes from the model."* 이 30초가 Innovation과 Technical 점수를 동시에 가져온다. |
| **데모 영상 0:10 화면** | 검은 화면에 카운트다운 3개가 **초 단위로 실제로 줄어들고 있다**: `164d 07:12:44 · gpt-4o-transcribe REMOVED` / `107d · Gemini Flash price ×2` / `47d · your nearest breaking change`. 그 아래 한 줄: **"Your repo. Right now."** |
| **가격** | Free 공개 repo 1개 주간 스캔 → **Team $59/월** (비공개 repo 10개, Slack/이메일 경보) → **Business $299/월** (조직 전체 스캔, SBOM 내보내기, 온프렘 스캐너). 가격이 싸다는 것 자체가 도입 장벽을 없앤다. |
| **명명된 경쟁사 + 차별화 1문장** | **Dependabot / Snyk**: 그들은 *패키지 버전과 CVE*를 본다 — EOLRadar는 **패키지에 없는 것**, 즉 코드 안에 문자열 리터럴로 박힌 **모델 ID·API 엔드포인트·프로토콜 헤더의 벤더 셧다운 날짜**를 본다(`"gpt-4o-transcribe"`는 어떤 의존성 그래프에도 나타나지 않는다). |
| **별점** | ★★★☆☆ / ★★★★☆ / ★★★★☆ / ★★★★☆ / ★★★★★ → **가중합 78** |
| **Thin-wrapper 리스크** | 🟢 **낮음.** 다만 "정규식 grep + 하드코딩 JSON"으로 축소되어 보일 위험이 있다 — **AST 기반 스캔, 심각도 모델, 주간 재스캔·알림 파이프라인을 아키텍처에 반드시 그릴 것.** |
| **10h 실현 리스크** | 🟢 **가장 낮음.** 10h 중 실제 코딩은 5~6h면 충분. **진짜 비용은 캘린더 DB 큐레이션(1.5~2h의 순수 리서치 노동)** 이며, 그 노동이 곧 해자(moat)다. |
| **누가 반응하는가** | **Sourav Sarkar (Sr. WW Specialist SA, AWS)** — 메인프레임 현대화 = 직업이 곧 마이그레이션 데드라인 관리. **Aakanksha Joshi (IBM)** — 고객사에 "이 모델을 2년 써도 되나요"를 답해야 하는 사람. **Vasuki Vudathala (ServiceNow)** — 조용히 깨지는 프로덕션이 그의 주제. **Shania Rasheed Nalagath (Microsoft)** — MS의 모델 수명주기 안내가 그녀 조직의 일. 패널 폭이 가장 넓다. |

---

# 8. CiteGate — 근거 없는 문장을 사용자에게 도달하기 전에 잘라내는 런타임 grounding 게이트

| 항목 | 내용 |
| --- | --- |
| **한 줄 태그라인** | *"RAG still hallucinates on 5–15% of answers. CiteGate strips every sentence that no retrieved span supports — before the user sees it, in 180ms."* |
| **타깃 유저 (1개 역할)** | 고객 대면 RAG 챗봇을 운영하는 회사의 **AI 애플리케이션 엔지니어** (법무가 "출처 없는 답변이 나가면 안 된다"고 말한 뒤 곤란해진 사람). |
| **아픈 문제 + 출처 통계** | RAG는 환각을 **30~70% 줄이지만 없애지 못한다** — **RAG 시스템도 5~15%의 경우에 여전히 환각하며, 특히 검색이 실패했을 때** 그렇다. 프런티어 모델조차 **grounded 답변의 5~8%에서 groundedness를 통과하지 못하고**, 인용 환각과 인접 청크 환각이 발생한다 ([cmarix.com RAG 통계 2026](https://www.cmarix.com/blog/rag-ai-statistics/), [futureagi.com](https://futureagi.com/glossary/rag-hallucination/)). 그런데 대부분의 팀은 이걸 **오프라인 eval에서만** 측정하고, 런타임에는 아무 장치가 없다. |
| **Why now (2026)** | ① **Claude Fable 5.1 (2026-09-01)의 캐시 읽기 $0.25/Mtok = 기본 입력의 0.025배** — 다른 모든 Claude 모델이 0.1배인 것과 대비된다. 즉 **검증용 2차 패스를 켜도 비용이 40분의 1**이라, "모든 응답을 검증한다"가 처음으로 경제적이 됐다. ② EU AI Act 투명성 의무와 금융·의료 규제가 **"출처 없는 AI 답변"을 리스크 항목으로 명문화**하는 중. ③ 기존 도구(Ragas, TruLens)는 **오프라인 평가 라이브러리**이고, **인라인 프록시로 실제 응답을 차단·수정하는 제품은 비어 있다.** |
| **10h MVP 범위** | **화면 4개**: ① Setup — 베이스 URL 교체 한 줄 + 정책 선택(`strip` 무근거 문장 제거 / `annotate` 표시만 / `block` 전체 거부). ② **Live Gate** — 좌: 모델 원본 응답, 우: 게이트 통과 후 응답. **잘려나간 문장은 취소선 + 빨간 배경으로 남아 보인다.** 각 통과 문장에는 근거 스팬 배지. ③ **Evidence Inspector** — 문장 하나를 클릭하면 검색된 청크 원문에서 **지지 스팬이 하이라이트**됨. ④ Metrics/Pricing — 게이트 통과율, 평균 지연 추가분, 차단된 문장 수 추이. **백엔드 4개**: (a) OpenAI 호환 프록시(SilentSLO와 같은 뼈대), (b) **문장 분할기 + 스팬 정렬기**(아래), (c) NLI/entailment 판정기, (d) 이벤트 스토어 + 지표 집계. |
| **결정론적(비-LLM) 코어** | **Span Aligner.** 응답을 문장 단위로 쪼갠 뒤(규칙 기반 분할), 각 문장에 대해 **검색된 컨텍스트 청크와의 정렬을 계산**: ① 숫자·날짜·고유명사·인용부호 안 문자열의 **정확 문자열 존재 검증** — 컨텍스트에 없는 숫자가 응답에 등장하면 **무조건 FAIL**(여기엔 판단이 없다), ② n-gram 중첩(ROUGE-L 스팬) 임계값, ③ 임베딩 코사인 최대값. **①이 가장 중요하다 — "컨텍스트에 존재하지 않는 숫자를 말하면 자른다"는 규칙 하나가 RAG 환각의 가장 위험한 부류를 LLM 없이 잡는다.** ①~③을 통과 못 한 문장만 소형 모델 entailment 판정으로 2차 심판하며, **판정 불가는 안전측(strip)으로 폴백**한다. |
| **Eval / 실패 처리 데모** | 자체 테스트셋 50건(근거 있는 답변 30 + 인용 환각 10 + 숫자 환각 10)에 대한 표: `무근거 문장 탐지 Recall 0.90 / Precision 0.86 / 추가 지연 중앙값 180ms / 응답당 추가 비용 $0.0004(Fable 5.1 캐시 히트 $0.25/Mtok 기준)`. **실패 처리**: 과차단(over-strip) 4건을 화면에 그대로 보여주고 — *"We cut 4 sentences that were actually fine. That is the trade we chose: we would rather delete a true sentence than ship a false one, and here is the dial to change it."* — 임계값 슬라이더를 움직여 Precision/Recall 곡선이 실시간으로 움직이는 걸 보여준다. |
| **데모 영상 0:10 화면** | 챗봇 답변이 타이핑되며 나타나는데, **두 번째 문장("2026년 3분기 매출은 $4.2M입니다")이 나타나자마자 빨갛게 취소선이 그어지고 사라진다.** 옆 패널: **"No retrieved span contains '$4.2M'. Stripped in 180ms."** 사용자에게는 애초에 도달하지 않았다는 자막. |
| **가격** | Free 5,000 검증/월 → **Team $199/월** (50만 검증, 정책 3종) → **Business $799/월** (온프렘 프록시, 감사 로그, SLA). 검증 단위 과금. |
| **명명된 경쟁사 + 차별화 1문장** | **Ragas / TruLens / Galileo**: 그들은 *나중에 점수를 매기는 평가 도구*다 — CiteGate는 **응답 경로 위에 인라인으로 앉아 무근거 문장을 사용자에게 도달하기 전에 실제로 제거하는 게이트**이며, 그래서 대시보드가 아니라 **컴플라이언스 통제 장치**로 팔린다. |
| **별점** | ★★★★☆ / ★★★★☆ / ★★★☆☆ / ★★★★☆ / ★★★★☆ → **가중합 76** |
| **Thin-wrapper 리스크** | 🟠 **중간.** "LLM으로 LLM을 검증"으로 보일 위험이 실재한다. **방어: 숫자·고유명사 정확 매칭이 1차 게이트이고 그것만으로 몇 %를 잡는지 숫자로 제시할 것**(예: "환각 20건 중 13건은 LLM 호출 없이 문자열 검증만으로 잡혔다"). |
| **10h 실현 리스크** | 🟡 **중간.** 스팬 하이라이트 UI가 까다롭고(문자 오프셋 관리), 프록시 + 스트리밍 + 문장 단위 게이팅이 겹치면 시간이 샌다. **축소 경로: 스트리밍 포기, "붙여넣기 데모" 모드**(컨텍스트와 응답을 붙여넣으면 게이트 결과를 보여줌)로 시작. |
| **누가 반응하는가** | **Shania Rasheed Nalagath (Sr. PM, Microsoft — grounding/retrieval 인프라)** — 이 제품의 문제 진술이 그녀의 직무 기술서다. **Aakanksha Joshi (IBM Agentic AI SA)** — 금융 고객에게 GenAI를 넣을 때 법무를 통과시키는 도구. **Anudeep Reddy Mutyala** — 그의 Content-Agent가 LangGraph 리서치→**팩트체크**→발행 구조다. **Nilesh Dhage (Fidelity)** — 규제 산업에서 출처 없는 답변은 금지. |

---

# 9. 종합 랭킹

> 가중합 = Σ (별점/5 × 배점). 배점 = Tech 25 / Impact 25 / Innovation 20 / UX 15 / Presentation 15.

| 순위 | 이름 | Tech 25 | Impact 25 | Innov 20 | UX 15 | Pres 15 | **가중합** | Wrapper | 10h 리스크 | 핵심 표적 심사위원 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **1** | **SilentSLO** | ★5 | ★5 | ★4 | ★4 | ★5 | **93** | 🟢 최저 | 🟡 중 | Vudathala, Joshi, Peri, Sarkar |
| **2** | **KillScore** | ★5 | ★4 | ★4 | ★4 | ★5 | **88** | 🟢 매우낮음 | 🟡 중 | Peri, Patel, Shah, Arya |
| **3** | **SpecDrift** | ★4 | ★4 | ★4 | ★5 | ★4 | **83** | 🟡 중 | 🟢 낮음 | PM 7인 전체 + Peri |
| **4** | **ShadowLedger** | ★4 | ★5 | ★3 | ★4 | ★4 | **81** | 🟢 낮음 | 🟢 낮음 | Vemuri, Boinpally, Dhage |
| **4** | **RetryRail** | ★4 | ★5 | ★3 | ★4 | ★4 | **81** | 🟢 매우낮음 | 🟢 낮음 | Kande(Visa), Shah(PayPal) |
| **6** | **ApplyGuard** | ★4 | ★4 | ★4 | ★4 | ★4 | **80** | 🟢 낮음 | 🟢 낮음 | Havryliuk(CareerPlug) |
| **7** | **EOLRadar** | ★3 | ★4 | ★4 | ★4 | ★5 | **78** | 🟢 낮음 | 🟢 최저 | Sarkar, Joshi, Nalagath |
| **8** | **CiteGate** | ★4 | ★4 | ★3 | ★4 | ★4 | **76** | 🟠 중 | 🟡 중 | Nalagath, Joshi, Dhage |

### 랭킹 해설

- **SilentSLO가 1위인 이유는 시장이 아니라 명단 때문이다.** 심사위원 중 공개 발신량이 압도적 1위인 사람(Vudathala)이 **정확히 이 제품의 문제 진술문을 제목으로 쓴 글을 두 편** 썼다. 다른 어떤 아이디어도 이 수준의 1:1 저격이 불가능하다.
- **KillScore가 2위인 이유는 유일하게 "AI 시대의 QA"라는 미개척 각도를 잡기 때문이다.** 그리고 Peri는 이 패널에서 **자기 도메인의 제품이 나올 확률이 가장 낮은 심사위원**이다 — 3,400팀 중 뮤테이션 테스팅을 들고 오는 팀은 거의 없다. 희소성 자체가 점수다.
- **SpecDrift는 "최대 다수 만족"형이다.** 20명 중 7명(PM)이 최대 블록이고, Peri까지 겹친다. 단독 임팩트의 날카로움은 1·2위보다 낮지만 **평균 점수가 가장 안정적**이다.
- **RetryRail은 도메인 판정단이 2명뿐이라는 구조적 한계**로 4위. 반대로 그 2명에게는 만점을 받을 수 있다.
- **CiteGate가 8위인 이유는 Innovation 20점**이다. Ragas/TruLens/Galileo가 이미 인접해 있어 "런타임 게이트"라는 차이를 30초 안에 설득해야 하는데, 그 30초가 비싸다.

### 기존 10선과의 관계 (참고)

기존 1·2위였던 **Clause50(89)** · **AgentReady(89)** 와 비교하면, **SilentSLO(93)** 와 **KillScore(88)** 는 같은 등급이다. 차이는 성격이다.

- Clause50/AgentReady = **문제의 외부 증거**(규제 날짜, 시장 통계)가 강하다.
- SilentSLO/KillScore = **심사위원 개인의 이력서**가 증거다. 이 패널이 VC가 아니라 현업 실무자 20명인 이상, 후자가 더 안전한 베팅이다.
- **하이브리드 권장**: SilentSLO를 만들되 **Clause50식 "카운트다운" UI 연출**(에러버짓 소진 타이머)을 빌려오고, KillScore의 **"일부러 실패를 보여주는 데모"** 를 그대로 이식할 것.

---

# 10. Top 2 피치 (3문장, "most X do A / we do B / because C")

### 🥇 1위 — SilentSLO

> **Most AI teams do observability by collecting traces and reading them after a customer complains** — their dashboards answer "was the request served?" while 20–40% of agent tool-call chains return garbage with a 200 OK, and the fastest detector in the building is still the support inbox.
>
> **We do it the way SRE does it**: a drop-in OpenAI-compatible proxy runs eight deterministic invariants on every response — schema validity, tool-call argument existence, silent context truncation, citation anchors, refusal-rate drift — converts violations into a *Silent Failure Rate* SLO with a real error budget, and pages on-call on burn rate, with no model in the detection path at all.
>
> **Because the failure mode that kills AI products isn't the one that throws an exception** — it's the one where, in the words of the ServiceNow engineer whose article gave us this problem, you watch your AI pipeline silently fail while Kubernetes says everything is fine, and nothing in your stack is even asking the question.

### 🥈 2위 — KillScore

> **Most teams do test quality with coverage** — they let a coding agent write the tests, watch the number hit 100%, and merge, which is why a suite can execute every line and still miss 96% of the bugs in it.
>
> **We do it with diff-scoped mutation testing**: we mutate only the functions your PR touched, re-run your own suite against each mutant, and report the percentage of mutants your tests actually killed — then Claude proposes tests for the survivors, and a test is only shown to you *after our runner confirms it kills the mutant it was written for.*
>
> **Because a test derived from the implementation cannot disagree with the implementation** — if the code has a bug, an AI-written test records that bug as the expected value and reports green, and the only way to catch that is to break the code on purpose and see whether anything screams.

---

# 11. 부록 — 출처 목록

| 사실 | 출처 |
| --- | --- |
| Vudathala, *"I Watched Our AI Pipeline Silently Fail While Kubernetes Said Everything Was Fine"* (2026-04-23) | https://hackernoon.com/i-watched-our-ai-pipeline-silently-fail-while-kubernetes-said-everything-was-fine |
| Vudathala, *"Why GPU Utilization Is the Wrong North Star for Production AI Inference"* (HPCwire, 2026-07-21) | https://www.hpcwire.com/2026/07/21/why-gpu-utilization-is-the-wrong-north-star-for-production-ai-inference/ |
| 프로덕션 환각률 (추출형 3~8% / 개방형 15~25% / 에이전트 툴콜 체인 20~40%) | https://www.digitalapplied.com/blog/ai-model-hallucination-rate-benchmarks-2026-study |
| 무음 회귀 · 컨텍스트 오버플로 11일 사례 · "customer complaints rather than CI failures" | https://dev.to/hassan_4e2f0901edda/production-llm-observability-what-youre-missing-when-your-ai-feature-goes-dark-3nli |
| 뮤테이션 스코어 vs 커버리지, MutGen 바닐라 LLM 53%, "100% coverage / 4% mutation" | https://www.augmentcode.com/guides/mutation-testing-ai-generated-code |
| Meta 뮤테이션 유도 LLM 테스트 생성 (라인 커버리지만 봤다면 버려졌을 테스트 277건) | https://arxiv.org/pdf/2501.12862 |
| LLM 생성 테스트의 커버리지·뮤테이션·실버그 상관 재현 연구 (2026) | https://arxiv.org/html/2607.22880 |
| GitClear *"The Maintainability Gap"* (2026-06, 623M 변경): 리팩터링 −70%, 중복 +81%, 복붙 +41%, catch 블록 +47% | https://www.gitclear.com/the_ai_code_quality_maintainability_gap |
| 스펙 드리프트 · 스펙/테스트/코드 추적성 | https://www.glukhov.org/app-architecture/testing-architecture/specs-tests-code-traceability-ai-development |
| 2026년 SDD 툴 전면화 (GitHub Spec Kit, AWS Kiro, Cursor, Tessl, Antigravity 등) | https://www.thebcms.com/blog/spec-driven-development/ · https://www.augmentcode.com/guides/what-is-spec-driven-development |
| IBM Cost of a Data Breach 2025: 섀도우 AI +$670K, 20% 조직, 97% 접근통제 부재, 65% PII 노출 | https://www.kiteworks.com/cybersecurity-risk-management/ibm-2025-data-breach-report-ai-risks/ · https://www.nudgesecurity.com/post/shadow-ai-the-emerging-security-threat-in-ibms-2025-cost-of-a-data-breach-report |
| Visa 30일 15회 / Mastercard 10회 제한, 초과 수수료 $0.10 / 최대 $0.50(2025-01~) | https://www.slickerhq.com/resources/blog/visa-mastercard-payment-retry-rules |
| False decline 2026년 $231B 추산, 거절의 60~65%가 정상 고객, 첫 재시도 회수율 40~60% | https://ecommercegermany.com/blog/false-decline-ecommerce/ · https://beastinsights.com/blog/false-decline · https://beastinsights.com/blog/issuer-decline |
| LinkedIn 분당 11,000건 지원 · 1년간 +45% | https://www.clever.cv/blog/ai-job-application-flood-how-to-stand-out-2026 |
| 채용팀 77%가 AI 생성 지원서 상시 접함 (2024초 53% → 2026 77%, Willo Hiring Trends Report 2026) | https://www.thehirehub.ai/blog/ai-generated-job-applications |
| OpenAI Assistants API 2026-08-26 종료 (자동 마이그레이션 없음) | https://developers.openai.com/api/docs/deprecations · https://www.techtimes.com/articles/325345/20260824/openai-assistants-api-shuts-down-tuesday-no-automated-migration-threads-risk.htm |
| whisper-1 / gpt-4o-transcribe 계열 2026-08-26 통보 → 2027-02-26 제거 | https://developers.openai.com/api/docs/deprecations |
| OpenAI 2026년 하반기 7개 셧다운 데드라인 (Prompts 객체 11-30 포함) | https://ampm-aiops.com/en/guides/openai-shutdown-deadlines-h2-2026/ |
| RAG 환각 잔존 5~15%, 프런티어 모델 groundedness 실패 5~8% | https://www.cmarix.com/blog/rag-ai-statistics/ · https://futureagi.com/glossary/rag-hallucination/ |
| MCP 2026-07-28 스펙 (세션 헤더 제거, 12개월 지원 중단 창) | https://blog.modelcontextprotocol.io/posts/2026-07-28/ |
| Claude Fable 5.1 캐시 읽기 $0.25/Mtok (기본 입력의 0.025배) · Gemini 3.8 Flash 도입가 2026-12-31 만료 | research/05_competition_and_idea_landscape.md §3.1 (벤더 문서 1차 확인분) |
| 심사위원 20인 배경 | research/02_organizers_sponsors_judges.md §4 |
