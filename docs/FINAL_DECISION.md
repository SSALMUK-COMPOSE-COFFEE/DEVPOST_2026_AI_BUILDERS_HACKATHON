# 00. 최종 결정 — 무엇을 만들 것인가

작성 2026-09-15 17:15 KST · 마감 2026-09-16 12:00 KST
코딩 창 17:30 → 03:00 (≈9h) · 영상/덱/README/제출 03:00 → 08:00 · 버퍼 08:00 → 12:00
목표 상: **Best SaaS Product $4,000** (유일 현금상)
배점: Technical 25 / Impact 25 / Innovation 20 / UX 15 / Presentation 15

---

## 결론 먼저

| | 선택 | 한 줄 |
| --- | --- | --- |
| **최종 빌드** | **KillScore** | AI가 쓴 테스트가 실제로 버그를 잡는지 채점하는 PR 단위 뮤테이션 테스팅 릴리스 게이트 SaaS |
| **헤지** | **SilentSLO** | 2026-09-15 **22:30 KST** 고/노고. 기준은 아래 §5 |
| **탈락시킨 최고점 후보** | Clock14 (EV 94.3, 전체 1위) | 사용자가 건 하드 필터 ③(미검증 외부 서비스 의존) 위반 — §3에서 명시적으로 기각 |

---

# 1. 정규화 후보 표 (전체 29건, 자체 재채점)

> **점수는 세 원본 문서의 자체 점수를 신뢰하지 않고 전부 다시 매겼다.** 원칙:
> ① Innovation은 "갤러리에 없음"이 아니라 **"시장에 명명된 경쟁사가 몇이나 있는가"** 로 깎는다.
> ② Impact는 "큰 시장"이 아니라 **"이 20명이 지난주에 겪었는가"** 로 본다.
> ③ P(무결점 라이브 데모)는 **솔로 9시간 + 심사위원이 직접 입력을 넣는 상황**을 가정한다.
> ④ `degraded` = T-6h에 라이브 루프가 안 돌아 시드+리플레이로 영상을 찍은 경우.
> ⑤ EV = P × (works) + (1−P) × (degraded).
>
> 약칭: **니치** = 프록시 갤러리 310건 중 유사 건수(0=완전 공백) · **WN** = why-now가 날짜로 고정되는가

| # | 이름 | 한 줄 | 니치 | Why-now (날짜 고정?) | P(무결점) | works | degraded | **EV** | Wrapper | 심사위원 공명 (실명) | 내일 쓸까? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Clock14** | CRA Art.14 24h 보고 시계 + SBOM↔KEV 매칭 | 0 | ✅ **2026-09-11 (D+4)** ENISA SRP 가동 | 0.85 | 96.5 | 82 | **94.3** | 🟢 최저 | Vemuri(Corteva 보안), Peri, Vudathala, Sarkar, Joshi | △ 인지는 하나 본인이 쓰진 않음 |
| 2 | **KillScore** | PR diff 뮤테이션 스코어 릴리스 게이트 | 0 | 🟡 GitClear 2026-06 (623M 변경) | **0.93** | 91.5 | 84 | **90.9** | 🟢 매우낮음 | **Peri(TMMi/Dell) 1:1**, Patel(Apple), Shah(PayPal), Arya(Pointer) | ✅ **엔지니어 8인 전원** |
| 3 | **SilentSLO** | LLM 무음 실패 SLO·에러버짓 (프록시+invariant) | 1 | 🟡 Vudathala 기고 2026-04/07 | 0.82 | 88 | 80 | **86.6** | 🟢 최저 | **Vudathala(ServiceNow) 1:1**, Joshi, Peri, Sarkar | ✅ 온콜 도는 사람 |
| 4 | **Article50** (S1 = Clause50 재설계) | EU AI Act Art.50 투명성 감사, Playwright 직행 | 0 | ✅ 2026-08-02 적용 / **12-02 만료 D-78** | 0.70 | 89.5 | 74 | **84.9** | 🟢 낮음 | Joshi, Nalagath, Dhage, Vemuri | ✅ URL 하나 |
| 5 | **AgreeGate** (S4 = RubricRoom) | LLM 저지 vs 인간 κ 측정 + 서명 증적 | 0 | 🔴 없음 | **0.95** | 83 | 76 | **82.7** | 🟢 낮음 | Peri, Joshi, Anudeep | △ |
| 6 | **MCPGate** (S3 = MCPGuard 재설계) | MCP 공급망 심사 + 헤더 라우팅 정책 프록시 | 0 | ✅ **MCP 2026-07-28 스펙** | **0.92** | 83 | 76 | **82.4** | 🟢 최저 | Arya(Pointer), Vemuri, Joshi, Sarkar | ✅ 플랫폼 엔지니어 |
| 7 | **FirstPass** | 프랑스 전자송장 EN 16931 Schematron 검증기 | 1 | ✅ **2026-09-01 (D+14)** | 0.90 | 83 | 77 | **82.4** | 🟢 매우낮음 | (도메인 판정단 0명) | ✅ 단 심사위원과 무관 |
| 8 | **Delta549** | EN 301 549 v3.2.1→v4.1.1 델타 접근성 감사 | 0 | ✅ **2026-09-02 (D+13)** | 0.68 | 85 | 70 | **80.2** | 🟡 중 | Boinpally, Havryliuk | ✅ 자사 URL |
| 9 | **SpecDrift** | 머지된 PR ↔ 수용기준 추적성 매트릭스 | 0 | 🟡 2026 SDD 툴 전면화 | 0.88 | 81 | 74 | **80.2** | 🟡 중 | **PM 7인 전체 + Peri** (최대 다수) | ✅ PM |
| 10 | **Clause50** (원안, browser_toolset) | 상동 · 브라우저 에이전트 전제 | 0 | ✅ D-78 | **0.45** | 92 | 70 | **79.9** | 🟢 낮음 | 상동 | — |
| 11 | **MCPGuard** (원안, 샌드박스 포함) | 상동 + 격리 샌드박스 | 0 | ✅ | 0.40 | 91 | 72 | **79.6** | 🟢 최저 | 상동 | — |
| 12 | **ShadowLedger** | OAuth 로그에서 미승인 AI 앱 + 유출 반경 | 0 | 🟡 IBM 2025 침해비용(+$670K) | 0.92 | 80 | 74 | **79.5** | 🟢 낮음 | **Vemuri 1:1**, Boinpally(Omnissa), Dhage | ✅ IT 관리자 |
| 13 | **RetryRail** | 카드 스킴 재시도 규칙 강제 엔진 | 0 | 🟡 MC 초과수수료 2025-01 | 0.92 | 80 | 74 | **79.5** | 🟢 매우낮음 | **Kande(Visa), Shah(PayPal)** — 단 2명 | △ 2명만 |
| 14 | **AgentGate** (S2 = AgentReady 재설계) | 12개 결정론 프로브 에이전트 대응력 점수 | 0 | ✅ ACP/UCP/AP2 2026 | 0.72 | 85 | 64 | **79.1** | 🟢 매우낮음 | Arya(Pointer) | ✅ |
| 15 | **PlaybookDrift** | 지원 매크로 모순 그래프 + 야간 스테이징 | **0** | ✅ Fable 5.1 2026-09-01 | 0.85 | 80 | 70 | **78.5** | 🟢 낮음 | Havryliuk, Nikam, Namana(FlowOps) | △ |
| 16 | **EOLRadar** | 레포 내 모델ID·API의 벤더 셧다운 D-day | 0 | ✅ **Assistants API 2026-08-26 종료** | **0.93** | 79 | 73 | **78.6** | 🟢 낮음 | Sarkar, Joshi, Nalagath, Vudathala (폭 최대) | ✅ 레포 URL 하나 |
| 17 | **TaskLedger** (S5 = TaskCost) | 토큰이 아닌 태스크 단위 실비용 원장 | 1 | ✅ Fable 5.1 캐시 0.025배 | **0.96** | 78.5 | 74 | **78.3** | 🟢 낮음 (단 AI 過소) | Vudathala, Dhage | ✅ |
| 18 | **BandProof** | EU Pay Transparency Art.9 6개 법정지표 | 1 | ✅ 2026-06-07 경과, D-107 | 0.92 | 78 | 72 | **77.5** | 🟢 낮음 | (HR 판정단 0명) | ✕ |
| 19 | **ApplyGuard** | 지원서 "공장" 지문 탐지 (채점 안 함) | 1 | 🟡 LinkedIn 분당 11k, +45% | 0.90 | 78 | 72 | **77.4** | 🟢 낮음 | **Havryliuk(CareerPlug) 1:1**, Nikam | △ |
| 20 | **MarkGate** 🇰🇷 | 한국 AI 기본법 + EU Art.50 이중 워터마크 게이트 | 0 | ✅ 2026-01-22 시행 | 0.72 | 78 | 68 | **75.2** | 🟢 매우낮음 | Joshi, Nalagath | ✅ API 3줄 |
| 21 | **CiteGate** | 무근거 문장 런타임 스트립 게이트 | 1 | 🟡 Fable 5.1 캐시 | 0.78 | 76 | 68 | **74.2** | 🟠 중 | **Nalagath(MS grounding) 1:1**, Joshi, Dhage | ✅ |
| 22 | **DefaultGap** 🇰🇷🇯🇵 | CBAM 실제배출량 vs default 격차 | 0 | ✅ 2026-01-01 시행 | 0.75 | 73 | 64 | **70.8** | 🟢 낮음 | (판정단 0명) | ✕ |
| 23 | **TrustReply** | SIG/CAIQ 보안설문 자동응답 | 0 | 🟡 캐시 경제 | 0.88 | 71 | 66 | **70.4** | 🟠 중상 | Shah, Vemuri | ✅ 단 경쟁 포화 |
| 24 | **SwitchClause** | EU Data Act Art.25/26/29 MSA 결손 체크 | 0 | ✅ 2027-01-12 D-119 | 0.90 | 71 | 64 | **70.3** | 🟠 중상 | Dhage, Tripathi | △ |
| 25 | **AgentReady** (원안) | 진짜 에이전트가 실제 구매 시도 | 0 | ✅ | **0.30** | 93 | 60 | **69.9** | 🟢 매우낮음 | Arya | — |
| 26 | **RenewalRadar** | 계약 자동갱신 조항 레이더 | 0 | 🟡 캐시 경제 | 0.90 | 70 | 64 | **69.4** | 🟠 중 | Dhage, Tripathi | △ |
| 27 | **Roundtable** | 멀티플레이어 에이전트 세션 | 1 | 🟡 Managed Agents | 0.55 | 78 | 58 | **69.0** | 🟡 중 | Arya, Namana | △ |
| 28 | **NightDesk** | 야간 리테이너 애널리스트 (cron 에이전트) | 2 | 🔴 전제 일부 붕괴 | 0.80 | 64 | 58 | **62.8** | 🔴 높음 | — | ✕ |
| 29 | **VoiceIntake** | 풀듀플렉스 규제 아웃바운드 음성 | 0 | ✅ GPT-Live 1 2026-09-10 | **0.20** | 74 | 48 | **53.2** | 🟡 중 | — | ✕ |

> 중복 처리: **Clause50 ≡ Article50(S1)**, **AgentReady ≡ AgentGate(S2)**, **MCPGuard ≡ MCPGate(S3)**,
> **RubricRoom ≡ AgreeGate(S4)**, **TaskCost ≡ TaskLedger(S5)** — 원안과 솔로-세이프 재설계판을
> **둘 다 표에 남겼다.** 재설계가 원안을 EV로 이기는 것 자체가 오늘의 핵심 논거이기 때문이다(§2-C).

---

# 2. 문서 간 불일치 명시적 판정

### A. A문서 "SilentSLO 93" vs C문서 "Article50 EV 89.4" — 누가 맞나

**둘 다 자기 유리하게 반올림했다. 내 판정: SilentSLO 88 / Article50 works 89.5, P 0.70.**

- **A문서의 SilentSLO Innovation ★4는 과대평가다.** A문서는 갤러리 공백만 봤고 **시장**을 안 봤다.
  Langfuse, Arize Phoenix, Helicone, Braintrust, Datadog LLM Observability가 전부 이 자리에 있고,
  05문서 §2.3·§4.4가 "에이전트 인프라"를 **포화 구역으로 명시 배제**했다. 게다가 Berkeley 프록시
  갤러리에서 가장 중복이 심한 클러스터가 에이전트 인프라다. **Innovation ★3으로 내린다(−4점).**
  또 A문서는 SilentSLO의 데모 좌측 "Grafana풍 인프라 패널 전부 초록"이 **내가 만든 목업**이라는
  사실을 계산에 넣지 않았다. 목업 화면이 영상의 훅이라는 건 주최측 배제 문구
  ("pitch decks, concept videos")에 가장 가까이 가는 구성이다. **Presentation도 ★5 유지하되 리스크 표기.**
- **C문서의 Article50 P=88%는 낙관이다.** C문서는 Playwright 크롤이 **내 픽스처**에서 도는 확률을 쟀지,
  **심사위원이 자기 회사 URL을 붙여넣는 상황**을 재지 않았다. 실제로는 (i) Cloudflare/WAF 차단,
  (ii) fingerprint DB 40개 커버리지 밖의 챗봇 벤더, (iii) 45초 타임아웃 내 8페이지 크롤,
  (iv) 상시 서버에 headless chromium 배포 — 네 개가 곱해진다. **P = 0.70으로 내린다(EV 89.4 → 84.9).**
  C문서 스스로 "잔존 리스크 ①"에 이 문제를 적어놓고 확률에는 반영하지 않았다.

**결론: 두 문서의 1위가 서로를 이기지 못한다. 재채점 후 둘 다 2·4위로 내려가고, A문서가 2위로 둔
KillScore와 B문서가 1위로 둔 Clock14가 올라온다.**

### B. B문서 "Clock14 93" — 상향 조정한다 (96.5)

B문서가 오히려 **자기 아이디어를 과소평가**했다. **why-now가 D+4**라는 것은 3,403팀 중
**누구도 선점할 수 없었다**는 뜻이고, 이건 Innovation 20점에서 ★4가 아니라 ★4.5다.
법정 상태기계 + append-only 해시체인 + 승인 게이트는 Tech ★5가 맞다. **EV 94.3으로 전체 1위.**

### C. 세 문서를 관통하는 진짜 발견 — "원안은 전부 자기 축소판에 진다"

C문서 §0의 검증(**`browser_toolset_20260801`은 클라이언트 툴셋이고 executor는 개발자가 Playwright로
직접 구현해야 하며, Anthropic 측에서는 아무것도 실행되지 않는다**)이 05문서 1·2위의 전제를 깼다.
표에서 보듯 Clause50 79.9 < Article50 84.9, MCPGuard 79.6 < MCPGate 82.4, AgentReady 69.9 < AgentGate 79.1.
**각 원안에서 정확히 하나의 무거운 배관(브라우저 executor / 격리 샌드박스 / 남의 상용 스토어)을
들어내면 EV가 3~9점 오른다.** 오늘의 결정은 "무엇을 만들까"가 아니라 **"무엇을 안 만들까"** 다.

### D. "성공 시 최고점"과 "EV"의 역전

AgentReady는 works 93으로 **전체 최고점**인데 EV는 69.9로 **뒤에서 5위**다.
단일 상 winner-take-all에 18시간 남은 상황에서 기준은 상한이 아니라 기대값이다.
**영상이 가장 강한 아이디어가 아니라, 영상이 반드시 찍히는 아이디어를 고른다.**

---

# 3. 하드 필터 적용

| 필터 | 내용 |
| --- | --- |
| **F1 SaaS** | 로그인·팀·요금제가 억지가 아닐 것 |
| **F2 결정론적 코어** | LLM을 전부 꺼도 제품의 절반 이상이 동작할 것 |
| **F3 미검증 외부 서비스 비의존** | 스키마·레이트리밋·가용성을 내가 확인하지 못한 외부 API/양식에 데모가 걸리지 않을 것 |
| **F4 CAPTCHA·제3자 사이트 협조 불요** | 남의 상용 사이트가 협조해야 데모가 성립하지 않을 것 |
| **F5 9h 완주** | 솔로 9시간 안에 라이브 URL까지 |

### 탈락

| 이름 | 탈락 필터 | 사유 |
| --- | --- | --- |
| **Clock14** | **F3** | ① **ENISA SRP 폼의 실제 필드 스키마는 어느 문서에서도 검증되지 않았다.** "17개 필드 프리필"은 내가 **규제 양식을 지어내는 것**이고, 패널에 보안 분석가(Vemuri)와 대기업 컴플라이언스 인접 인력이 앉아 있다. 규제 양식을 그럴싸하게 위조한 화면은 발각되면 제품 전체의 신뢰가 0이 된다. ② NVD API는 키 없이 레이트리밋이 걸리고, purl↔CPE 매칭은 KEV의 자유 텍스트 제품명과 붙여야 해서 **유일한 난제가 곧 핵심 판정 로직**이다. → 전체 EV 1위지만 **기각**. (사용자가 F3를 완화할 의사가 있다면 이것이 1순위 대안이다 — §6 참조) |
| AgentReady / **AgentGate** | **F4** | 남의 스토어 봇 차단·ToS. 자체 Shopify 개발 스토어로 바꾸면 통과하나 그 시점에 "장애물 코스 체크리스트"로 축소되어 works가 85→79로 내려감 |
| **Article50** / Clause50 | **F4 (부분)** | 히어로 데모가 "심사위원이 자기 URL을 넣는다"인데 그건 제3자 사이트 협조에 걸린다. 내 픽스처만 쓰면 F4는 통과하지만 와우 모먼트가 소멸 |
| **Delta549** | **F4** | 동일 |
| **VoiceIntake** | F3·F5 | SIP 트렁크·번호 프로비저닝 |
| **NightDesk** | F2·F5 | Managed Agents에 브라우저 툴 없음 + "밤에 돌았다"를 라이브로 못 보여줌 |
| **Roundtable** | F5 | 실시간 동기화 + 포크/머지 |
| **TrustReply** | F3 | 실제 SIG는 Shared Assessments 유료 라이선스, 합성하면 순환 eval |
| **MarkGate** | F3·F5 | C2PA 서명 인증서 체인 |
| **DefaultGap** | F5 | Annex IV 산정식 독해 시간 |
| **BandProof / FirstPass / SwitchClause** | (통과) | 단 **판정 가능한 심사위원이 0~1명** — 필터가 아니라 §4의 패널 적합도에서 탈락 |

### 5개 필터를 모두 통과한 후보 (EV 순)

**KillScore 90.9** → SilentSLO 86.6 → AgreeGate 82.7 → MCPGate 82.4 → FirstPass 82.4 → SpecDrift 80.2
→ ShadowLedger 79.5 → RetryRail 79.5 → EOLRadar 78.6 → TaskLedger 78.3 → PlaybookDrift 78.5 → ApplyGuard 77.4 → BandProof 77.5 → CiteGate 74.2 → SwitchClause 70.3 → RenewalRadar 69.4

---

# 4. 최종 선택 — **KillScore** · 헤지 **SilentSLO**

### 왜 KillScore가 이 루브릭과 이 패널에서 준우승 후보들을 이기는가 (10문장)

1. 5개 하드 필터를 통과한 후보 중 **EV가 가장 높고(90.9), 그중에서도 P(무결점 데모)가 0.93으로 최상위권**이다 — 외부 API·외부 사이트·외부 양식·브라우저 자동화·CAPTCHA 어느 것에도 걸리지 않고, 화면의 모든 픽셀이 내 서버의 서브프로세스가 실제로 실행한 결과다.
2. Impact 25점에서 **"이 20명이 지난주에 겪었는가"** 로 재면 `>` 를 `>=` 로 바꿨는데 47개 테스트가 전부 통과하는 장면은 Apple·PayPal·Visa·Microsoft·ServiceNow 엔지니어 8인 전원의 트라우마이고, Clock14·Article50의 "EU 과징금"은 그들이 **인지만 하고 겪지는 않는** 고통이다.
3. Technical 25점에서, 이 제품의 코어는 **AST 변형 + 격리 서브프로세스 실행 + diff 스코핑**이라 LLM을 전부 꺼도 점수가 나온다 — 주최측이 명시 배제한 `"AI wrappers with minimal differentiation"`에 구조적으로 걸릴 수가 없다.
4. 동시에 **Innovation 20점의 "creatively AI technologies are applied"** 를 SilentSLO·TaskLedger·RetryRail처럼 잃지 않는다: Claude가 생존 뮤턴트를 죽이는 테스트를 쓰고, **러너가 "원본에서 통과 + 뮤턴트에서 실패"를 실증한 뒤에만** 사용자에게 보이는 구조는 AI에 **검증 가능한 오라클**을 붙인 것이고, 이건 OpenAI Build Week 2위 Sentinel의 `"it's a reviewer, not an author"` 패턴 그대로다.
5. 의도적 실패 데모가 **억지로 끼워넣은 장치가 아니라 제품 그 자체**다 — `Proposed test did NOT kill mutant #7 — rejected` 는 제품이 자기 AI의 출력을 거부하는 장면이고, Vudathala의 기고 제목(*"I Watched Our AI Pipeline Silently Fail While Kubernetes Said Everything Was Fine"*)이 겨냥하는 정확한 실패 모드다.
6. 심사위원 20명 중 **자기 도메인의 제품이 나올 확률이 가장 낮은 사람**이 Lakshmi Vidya Peri(TMMi America 이사, Dell "Modern Validation Playbook" 저자, 9년간 테스트 스코어링·KPI 플랫폼 구축)인데, **mutation score는 TMMi Level 4~5의 측정 어휘 그 자체**이고 Business 티어의 TMMi 형식 증적 PDF는 그녀가 9년간 만든 산출물이다 — 3,403팀 중 그녀에게 이걸 들고 가는 팀은 사실상 없다.
7. 반대로 SilentSLO는 같은 급의 1:1 저격(Vudathala)을 갖지만 **Innovation에서 Langfuse·Arize·Helicone·Braintrust·Datadog라는 명명된 경쟁사 다섯에 둘러싸여 있고**, 영상의 훅이 **내가 만든 가짜 Grafana 패널**이라 "concept video" 쪽으로 반 걸음 기운다.
8. Clock14는 EV 1위지만 **존재하지 않는 규제 양식을 화면에 그려야** 하고, Article50은 **심사위원이 자기 URL을 넣는 순간 WAF와 40개짜리 fingerprint DB에 운명이 걸린다** — 둘 다 "발각되면 0점"인 종류의 리스크이고, KillScore에는 그런 표면이 한 곳도 없다.
9. UX 15 + Presentation 15 = 30점에서, `Coverage 100% ✅ / Mutation score 31% ❌` 라는 **두 숫자의 대비 한 장**이 설명 없이 즉시 이해되는 유일한 후보다(MCPGate는 도메인 설명에 30초, FirstPass·BandProof·DefaultGap은 판정 가능한 심사위원이 0~1명).
10. 마지막으로 **"I would use this tomorrow"** — 공개 repo 무제한 무료 + 함수/테스트를 붙여넣는 플레이그라운드가 있으면 **심사위원 20명 중 8명이 영상을 보는 동안 자기 코드로 실제로 눌러볼 수 있고**, 그건 Clause50의 URL 한 칸과 달리 실패할 방법이 없다.

### 헤지: **SilentSLO** — 고/노고 2026-09-15 **22:30 KST** (H5 종료 시점)

**전환 기준 (세 개 전부 참이어야 KillScore 유지, 하나라도 거짓이면 즉시 전환):**
1. 3개 데모 repo 각각에서 뮤테이션 엔진이 **뮤턴트 30개 이상**을 생성한다.
2. 러너가 그 전부에 대해 `killed / survived / timeout` 판정을 **repo당 60초 이내**에 반환한다.
3. 결제/금액 계산 경로에 **생존 뮤턴트(히어로 뮤턴트)가 최소 1개** 존재한다 (`>` → `>=` 계열).

**왜 SilentSLO인가**: (a) 필터 통과 후보 중 EV 2위(86.6), (b) **H0~H2에 이미 세운 스캐폴드(FastAPI + Postgres +
Next.js 대시보드 + Stripe Pricing Table + `make eval` 하네스)를 100% 재사용**한다, (c) 가장 어려운 부분인
invariant 엔진 8종이 **순수 파이썬 함수**이고 트래픽은 내가 시드로 생성하므로 외부 의존이 0이다,
(d) 22:30에 시작해도 남은 4.5시간(invariant 1.5h + 시드 트래픽 0.5h + 분할 대시보드 1.5h + eval 0.5h + 폴리시 0.5h)으로
완주 가능한 유일한 카드다, (e) 저격 대상(Vudathala)이 KillScore(Peri)와 **직교**해서 피치를 다시 쓸 필요가 없다.
**전환 시 즉시 버리는 것**: 스트리밍 패스스루 프록시 — non-stream + 시드 리플레이만.

---

# 5. 빌드 브리프 — KillScore

## 5.1 제품명 · 태그라인

- **제품명**: **KillScore**
- **태그라인 (숫자 포함, 영문 verbatim)**:
  > **"100% coverage. 31% mutation score. The SaaS release gate that scores whether your AI-written tests can actually catch a bug."**
- **영상·덱 1장 훅 (verbatim)**:
  > **"We flipped `>` to `>=` in your payment logic and all 47 tests still passed."**
- 제출 제목·태그라인·덱 1번 슬라이드에 **"SaaS"** 라는 단어가 물리적으로 존재한다.

## 5.2 타깃 유저 (초니치 1인)

**코딩 에이전트를 도입한 20~200명 규모 엔지니어링 조직의 QA 리드 겸 릴리스 엔지니어 1인.**
"AI가 테스트도 써준다"를 근거 없이 믿어야 하는 입장이고, 매주 머지 버튼 앞에서
커버리지 숫자 하나로 릴리스를 승인하는 사람. PM도 CTO도 아니다.

## 5.3 3문장 피치 ("most X do A / we do B / because C", 영문 verbatim)

> **Most teams measure test quality with coverage** — they let a coding agent write the tests, watch the number hit 100%, and merge, which is how a suite can execute every line of your code and still miss 96% of the bugs in it.
>
> **We do it with diff-scoped mutation testing**: we mutate only the functions your pull request touched, re-run your own suite against every mutant, and report the percentage your tests actually killed — then Claude proposes tests for the survivors, and a proposed test is shown to you *only after our runner proves it passes on the original and fails on the mutant.*
>
> **Because a test derived from the implementation cannot disagree with the implementation** — if the code has a bug, an AI-written test records that bug as the expected value and reports green, and the only way to catch that is to break the code on purpose and see whether anything screams.

## 5.4 MVP 정확 스코프

### 화면 (6개, 이 이상 만들지 않는다)

| # | 경로 | 내용 |
| --- | --- | --- |
| 1 | `/` | 랜딩. 히어로에 `Coverage 100% ✅ / Mutation 31% ❌` 대비 카드. **데모 repo 3개 프리셋 버튼** + **"Paste a function + its tests" 플레이그라운드**(로그인 불필요, `?demo=1`) |
| 2 | `/runs/[id]` | **라이브 런 뷰.** SSE로 뮤턴트 타일이 하나씩 초록(killed)/빨강(survived)/회색(timeout)으로 뒤집힘. 상단 고정: 커버리지 vs 뮤테이션 스코어, 진행률, 경과 시간, 누적 비용 |
| 3 | `/runs/[id]/mutants/[k]` | **생존자 상세.** 원본↔뮤턴트 diff, `47 tests still passed`, 함수별 그룹, `Propose a test` 버튼 → 검증 결과 배지 `VERIFIED KILL` / `REJECTED — did not kill mutant` |
| 4 | `/gate` | 게이트 정책: `mutation score >= N% 미만이면 머지 차단` 슬라이더, GitHub Checks 형식 JSON 프리뷰, PR 배지 미리보기, **TMMi 형식 증적 PDF 내보내기** |
| 5 | `/evals` | **공개 eval 페이지.** 20건 결과 표를 제품 안에서 상시 노출 (README·덱과 동일한 표) |
| 6 | `/pricing` | Stripe Pricing Table (test mode, `pk_test_`) |

### API 엔드포인트 (FastAPI)

```
GET    /healthz                              → {"status","version","db","runner_workers"}
POST   /v1/runs                              → {repo_preset | inline_source+inline_tests, diff_only}
GET    /v1/runs/{id}                         → 요약(coverage, mutation_score, killed/survived/timeout/error)
GET    /v1/runs/{id}/events                  → SSE 진행 스트림
GET    /v1/runs/{id}/mutants?status=survived → 뮤턴트 목록
GET    /v1/mutants/{id}                      → 원본/뮤턴트 소스, 실행 로그
POST   /v1/mutants/{id}/propose-test         → Claude 초안 → 러너 2회 검증 → verdict
GET    /v1/runs/{id}/report.pdf              → TMMi 형식 증적 (WeasyPrint)
GET    /v1/gate/{repo}/check                 → GitHub Checks 형식 JSON
GET    /v1/usage/{run_id}                    → 토큰·비용·레이턴시
```

### DB 테이블 (Postgres / Neon)

`org` · `user` · `membership` · `repo` · `run` · `target_function` · `mutant` ·
`test_execution`(mutant_id, phase=`original|mutant`, exit_code, duration_ms, stdout_tail) ·
`proposed_test`(mutant_id, source, verdict=`verified|rejected|error`, llm_call_id) ·
`gate_policy` · `evidence_export` · `llm_call`(model, input_tok, output_tok, cost_usd, latency_ms)

> `llm_call` 테이블이 있다는 사실 자체가 관측성 심사위원(Vudathala)에게 보내는 신호다.
> `/healthz` + 구조화 로그 + 요청당 토큰·비용 기록을 **H0에** 넣는다.

### 결정론적 엔진 (제품의 80%, LLM 0회)

1. **Diff 스코퍼** — `git diff` → 변경 라인 범위 → Python `ast`로 그 라인을 포함하는 `FunctionDef`만 추출.
   (전체 repo 뮤테이션이 몇 시간 걸리는 것을 **수십 초**로 떨어뜨리는 유일한 장치이자, 이 제품이
   `mutmut`/`cosmic-ray` CLI가 아니라 **PR 게이트 SaaS**인 이유.)
2. **Mutation Engine** — AST 변환 연산자 **9종**:
   `>`↔`>=` · `<`↔`<=` · `==`↔`!=` · `and`↔`or` · 숫자 상수 ±1 · `True`↔`False` ·
   조건식 반전(`not`) · `return <expr>` → `return None` · `except: raise` → `except: pass`.
   (시간이 부족하면 **앞 5종으로 축소** — 데모는 그대로 성립.)
3. **Runner** — 뮤턴트마다 워크트리 복사 → `pytest -x -q` 서브프로세스, per-mutant 타임아웃 8초,
   네트워크 차단, 병렬 8워커. 판정 = `killed`(테스트 실패) / `survived`(전부 통과) /
   `timeout` / `error`. **Score = killed / (total − error)**, `timeout`은 **분모에 남기고 kill로 치지 않는다.**
4. **Gate** — 임계값 비교 + GitHub Checks 형식 JSON 생성 + 증적 해시.

### Claude를 쓰는 곳과 금지 사항 (화면에 상시 표시, 덱에 이 문장 그대로)

**사용처는 정확히 두 곳이다.**
1. `propose_test(mutant)` — 생존 뮤턴트를 죽이는 pytest 테스트 초안 작성.
   출력 스키마 강제 `{test_name, test_code, targets_mutant_id, rationale}`.
   **검증 루프**: ① 원본에서 실행 → **반드시 PASS** ② 뮤턴트에서 실행 → **반드시 FAIL**.
   둘 다 만족할 때만 `VERIFIED KILL`로 사용자에게 노출. 아니면 `REJECTED` + 사람 큐.
2. `name_cluster(survivors)` — 생존 뮤턴트 묶음에 사람이 읽을 이름 붙이기
   (`"6 survivors are all boundary conditions in price_after_discount"`).
   인용한 mutant_id가 이번 런에 없으면 **하드 리젝트**.

**금지 (영문 verbatim, 화면 배지 + 덱 아키텍처 슬라이드에 빨간 선으로):**
> **The model never computes the score. The model never marks a mutant killed.
> The model never edits the code under test. A proposed test is shown only after our runner
> proves it passes on the original and fails on the mutant.**

모델: `claude-opus-5`, `thinking: {type:"adaptive"}`, `output_config: {effort: "medium"}`.
벌크 분류는 `claude-haiku-4-5`. **`thinking.budget_tokens` 절대 금지(Opus 5 / Sonnet 5에서 400).**
`output_format`이 아니라 `output_config: {format: {...}}`. 어시스턴트 prefill 금지(400).

## 5.5 Eval 표 설계 (20건) — H9, 협상 불가

### 픽스처 생성법 (<30분)

`fixtures/billing.py` 순수 파이썬 모듈 하나(요금 티어, 할인, 반올림, 재시도 윈도, 날짜 경계) +
**"AI가 쓴 것 같은" pytest 스위트**(라인 커버리지 100% 달성, 전부 구현에서 파생).
그 다음 `fixtures/bugs.yaml`에 **버그 20개를 (파일, 라인, old, new) 패치로 선언**하고
`python -m fixtures.gen` 이 20개 repo 사본을 찍어낸다. **Ground truth가 생성 시점에 정의상 확정**된다.

버그 20종 구성: 티어 경계 off-by-one 3 · `>=`→`>` 3 · 반올림 방향 2 · `and`↔`or` 2 ·
None 체크 누락 2 · early-return 반전 2 · 날짜 윈도 off-by-one 2 · 기본값 오류 2 · 예외 삼킴 2.

### 메트릭과 표 (README · 덱 7번 슬라이드 · `/evals` · 영상 2:05 네 곳에 동일한 표)

| Metric | AI-written suite (baseline) | LLM-only reviewer (ablation) | **KillScore** | n |
| --- | --- | --- | --- | --- |
| 심은 버그 탐지 (escaped-bug catch) | 3 / 20 | 9 / 20 | **18 / 20** | 20 |
| Mutation score | 31% | — | **78%** | 45 mutants |
| **Line coverage** | **100%** | — | **100%** | — |
| 제안 테스트 검증 통과율 (Claude 초안이 실제로 뮤턴트를 죽인 비율) | — | — | **71% (22/31)** | 31 |
| 근거 없이 노출된 테스트 | — | — | **0 (구조적으로 불가능)** | — |
| 런당 p50 / p95 | — | — | **38s / 61s** | 20 |
| 런당 비용 | — | **$0.11** | **$0.04** | 20 |

> **표의 진짜 킬러는 세 번째 줄이다: 커버리지는 100%에서 움직이지 않는데 뮤테이션 스코어만 31→78로 간다.**
> "당신이 지금 보고 있는 숫자는 움직이지 않으면서 품질만 움직인다"를 한 줄로 증명한다.
> **ablation 열(LLM-only reviewer = "이 diff 보고 테스트가 충분한지 말해줘")** 은 10분이면 돌고,
> Algoverse 코드워드(`baseline`, `ablation`)를 정확히 친다.

`evals/` 디렉토리 + `make eval` 한 줄 + 결과 마크다운 표 **자동 생성**.

## 5.6 의도적 실패 데모 모먼트 (영상 1:50~2:10, 20초)

**두 개를 연속으로 보여준다.**

1. **제품이 자기 AI를 거부한다.** 생존 뮤턴트 #7에 `Propose a test` 클릭 → Claude가 테스트를 씀 →
   러너가 원본에서 PASS, **뮤턴트에서도 PASS** → 화면이 빨갛게
   `REJECTED — proposed test passes on both. It does not kill mutant #7. Escalated to human review.`
   나레이션: *"That's our own AI failing, on camera. The product refused to show you its output.
   The score is not something the model is allowed to move."*
2. **타임아웃을 kill로 세지 않는다.** 무한루프를 만드는 뮤턴트 1개를 일부러 심어둔다 →
   회색 `TIMEOUT` 타일 + 툴팁 `A timeout is not a kill. Counting it as one would inflate our own score.`

> 컴플라이언스 도구가 아니라 **품질 측정 도구**이므로 "자기 점수를 부풀리지 않는다"가 곧 제품의 정직성이다.
> Peri(검증)와 Vudathala(관측성)를 동시에 정조준하는 20초.

## 5.7 가격 (Stripe Pricing Table, test mode · 좌석 아님 · repo 단위)

| 티어 | 가격 | 내용 |
| --- | --- | --- |
| **Free** | $0 | **공개 repo 무제한** (주최 OSC 오픈소스 취향 정렬), 런당 뮤턴트 200개, 게이트 없음 |
| **Team** | **$99/mo** | 비공개 repo 5개, **PR 머지 게이트**, Slack 알림, 런당 뮤턴트 2,000개 |
| **Business** | **$399/mo** | repo 무제한, **TMMi 형식 증적 PDF 내보내기**, SSO, 셀프호스트 러너 |

Stripe Pricing Table은 **노코드**(대시보드에서 생성 → `<script>` + `<stripe-pricing-table>` 붙여넣기),
`pk_test_`로 테스트 모드 동작, **렌더링에 도메인 필요** → `killscore.hajin.xyz`. 실측 15분.

## 5.8 시드 데모 데이터 (빈 대시보드 금지)

- `demo/billing-api` — 픽스처. **커버리지 100% / 뮤테이션 31%.** 히어로 뮤턴트(`>`→`>=`, 결제 금액 경로) 보유.
- `demo/auth-tokens` — **커버리지 60% / 뮤테이션 58%.** 커버리지가 낮은데 테스트는 더 좋은 역설 사례.
  영상에서 10초 쓰면 "이 팀은 지표를 진짜로 이해한다"는 신호가 된다.
- `demo/oss-small` — 실제 소형 OSS 패키지를 벤더링(자체 테스트 포함). 실코드에서도 돈다는 증거.
- **완료된 과거 런 2건**을 미리 넣어 대시보드가 절대 비어 보이지 않게 한다.
- **`?replay=<run_id>` 리플레이 모드** — 라이브 실패 보험. H7에 반드시.

## 5.9 시간별 계획 17:30 → 08:00 KST (체크포인트마다 화면에 무엇이 있는가)

| 시각 | 작업 | **그 시점에 화면에 보이는 것** |
| --- | --- | --- |
| **17:30–18:00** (H0) | 레포 생성 + `HACKATHON.md`(재사용 범위 명시) + FastAPI + Postgres(Neon) + Next.js/shadcn 스캐폴드. **배포 먼저** (`killscore.hajin.xyz` / `killscore-api.hajin.xyz`). `/healthz` + 구조화 로그 + `llm_call` 테이블 | 브라우저에 `{"status":"ok","version":"0.1.0","db":"up"}` |
| **18:00–19:00** (H1) | **Mutation Engine v1** — AST 연산자 5종. `python -m killscore.mutate fixtures/billing.py` | 터미널에 뮤턴트 30+개의 diff 목록 |
| **19:00–20:00** (H2) | **Runner** — 워크트리 복사, pytest 서브프로세스, 타임아웃, 8워커 병렬. `python -m killscore.run demo/billing-api` | 터미널에 `mutation score 31% (14/45 killed, 2 timeout)` ← **이 순간 제품이 존재한다** |
| **20:00–20:45** (H3) | diff 스코핑(git diff → FunctionDef) + 연산자 4종 추가 + Postgres 스키마 + 영속화 | `curl /v1/runs/{id}` 전체 JSON |
| **20:45–21:45** (H4) | **Next.js 런 뷰 + SSE** — 뮤턴트 타일이 실시간으로 초록/빨강으로 뒤집힘. 상단 커버리지 vs 뮤테이션 대비 카드 | **와우 모먼트 #1** |
| **21:45–22:30** (H5) | 생존자 상세 — 원본↔뮤턴트 diff, `47 tests still passed`, 함수별 그룹 | **히어로 뮤턴트(`>`→`>=`, 결제 경로)가 풀스크린에** |
| **🚦 22:30** | **고/노고 게이트 (§4의 기준 3개)** | 거짓이면 즉시 SilentSLO 전환 |
| **22:30–23:30** (H6) | Claude `propose_test` + **2단 검증 루프** + `VERIFIED KILL` / `REJECTED` 배지 + 사람 큐 | **와우 모먼트 #2 + 의도적 실패 장면** |
| **23:30–00:15** (H7) | 인증(단일 데모 org + `?demo=1` 우회) · org/팀 모델 · 시드 런 3개 · `/gate` 임계값 슬라이더 + Checks JSON 프리뷰 · **`?replay=` 리플레이 모드** | 대시보드에 repo 3개, 절대 비지 않음 |
| **00:15–01:00** (H8) | **Stripe Pricing Table(15분)** + `/evals` 공개 페이지 + 빈 상태·에러 상태·다크모드 + 400px 모바일 + TMMi 증적 PDF(WeasyPrint 1장) | 가격 페이지 + PDF 다운로드 |
| **01:00–02:00** (H9) | **`make eval`** — 20건 픽스처 + baseline + ablation 실행 → 마크다운 표 자동 생성 → README·덱·`/evals`에 주입 | 터미널에 완성된 eval 표 |
| **02:00–03:00** (H10) | 폴리시, 헤더 카피, **아키텍처 다이어그램**, 비용·레이턴시 계측 노출(`$/run`, `mutants/sec`) | — |
| **🔒 03:00** | **코드 프리즈** | — |
| **03:00–04:00** | 영상 촬영 (2:45, 테이크 3~4회) | — |
| **04:00–05:00** | 편집 + 자막 + **YouTube 업로드**(Public 또는 Unlisted, **"Not for Kids"**). 처리 시간 때문에 여기서 반드시 올린다 | — |
| **05:00–06:15** | **10장 덱** (8개 지정 섹션) → PDF → 레포 + Devpost 양쪽 | — |
| **06:15–07:00** | README + LICENSE(Apache-2.0) + `.env.example` + 셋업 가이드 + 스크린샷 3장 | — |
| **07:00–08:00** | **1차 제출 완료 + Submitted 배지 확인.** 시크릿 창에서 라이브 URL·영상·GitHub·덱 4개 링크 전부 확인. **Tin Computer $299 크레딧 청구**. NexFellow 제출 | — |
| **08:00–11:00** | 수면 / 버퍼 | — |
| **11:00–12:00** | 동결. 링크 재확인만. 코드 수정 금지 | — |

## 5.10 데모 영상 2:45 구성

| 타임 | 화면 | 내레이션 (verbatim) |
| --- | --- | --- |
| **0:00–0:12** | 초록 pytest 출력 `47 passed in 2.31s` + `Coverage: 100%`. 그 위로 빨간 카드가 슬라이드인 | *"Forty-seven tests. One hundred percent coverage. I flipped one character in the payment logic — greater-than to greater-than-or-equal — and every single one of them still passed."* |
| **0:12–0:22** | 얼굴 10초. 뒤로 GitClear 그래프 | *"I'm Hajin. The world doesn't need another AI demo. In 2026 about a quarter of merged commits carry AI traces, refactoring is down 70% and duplication is up 81% — and the one number we use to gate releases doesn't move when the tests get worse."* |
| **0:22–0:35** | **라이브 시작.** `killscore.hajin.xyz`, 데모 repo 선택 → 런 시작 | *"This is live at killscore.hajin.xyz right now — nothing here is pre-rendered. KillScore takes the diff, finds only the functions this PR touched, and mutates them."* |
| **0:35–1:15** | 뮤턴트 타일이 초록/빨강으로 실시간 뒤집힘. 상단 두 숫자가 벌어짐 | *"Forty-five mutants, your own test suite re-run against each one. Killed in green, survived in red. Coverage stays at a hundred. Mutation score lands at thirty-one. Your tests execute every line and catch three bugs in ten."* |
| **1:15–1:35** | 히어로 생존자 상세. 원본↔뮤턴트 diff 풀스크린 | *"Here's the one that matters. This is the boundary in the discount tier. We changed it, and forty-seven tests still passed. No model decided that — a subprocess ran your suite and read the exit code."* |
| **1:35–1:50** | `Propose a test` → Claude 초안 → 검증 → `VERIFIED KILL` 초록 | *"Now Claude writes a test for it. And before you ever see that test, our runner proves two things: it passes on the original, and it fails on the mutant. Verified kill."* |
| **1:50–2:10** | **의도적 실패 ×2.** #7 `REJECTED` 빨강 → 회색 `TIMEOUT` 타일 | *"Let me show you it failing. Here the model's test passes on both — it doesn't kill anything. Rejected, queued for a human. And this one timed out: a timeout is not a kill. Counting it as one would inflate our own score."* |
| **2:10–2:28** | **아키텍처 1장.** 박스 6개: Diff Scoper / AST Mutation Engine / Sandboxed Runner / Score & Gate / Evidence Export / *LLM Test Proposer*(작게, 점선). 하단 수치 | *"Six components, exactly one is a model call and it's the dotted box. p50 run time thirty-eight seconds, four cents a run. The model never computes the score, never marks a mutant killed, and never edits the code under test."* |
| **2:28–2:38** | **eval 표 한 컷** | *"Twenty repos with twenty bugs I planted myself. The AI-written suite caught three. After KillScore, eighteen. Coverage never moved."* |
| **2:38–2:45** | 가격 3티어 + URL 자막 | *"Free forever on public repos. Ninety-nine dollars a month for the release engineer who has to press merge. killscore.hajin.xyz — paste your own function and see what survives."* |

**규칙**: 라이브 화면 60% 이상(1:40+), 슬라이드 1장만, 자막 필수, 로딩은 컷하되
**"this is not pre-rendered"를 명시적으로 말한다**(Gauntlet 교훈).

## 5.11 10장 덱 ↔ 8개 지정 섹션 매핑

| # | 슬라이드 | 지정 섹션 | 핵심 1줄 |
| --- | --- | --- | --- |
| 1 | **KillScore — the SaaS release gate for AI-written tests** | (표지) | 태그라인 + "SaaS" 물리적 존재 + 라이브 URL |
| 2 | 100% coverage, 3 bugs in 10 | **Problem statement** | GitClear 623M 변경: 리팩터링 −70%, 중복 +81%, catch 블록 +47% |
| 3 | Break the code on purpose | **Solution** | diff-scoped 뮤테이션 + 게이트, `>`→`>=` 예시 한 장 |
| 4 | The person who presses merge | **Target users** | QA 리드·릴리스 엔지니어 1인. 명명된 경쟁: *"Codecov/SonarQube measure whether code ran. We measure whether tests can disprove it."* |
| 5 | Score · Survivors · Proposed kills · Gate | **Product features** | 화면 4장 스크린샷 |
| 6 | 6 boxes, 1 dotted | **Technical architecture** | 아키텍처 + 확장성·성능·보안·테스트 각 1줄 (p50 38s, 8워커, 네트워크 차단 서브프로세스, 단위테스트 N개) |
| 7 | Reviewer, not author | **AI technologies used** | Claude Opus 5, 스키마 강제, **금지 4개 문장**, 2단 검증 루프 |
| 8 | 31% → 78%, coverage never moved | **Impact & value** | **eval 표** + baseline + ablation |
| 9 | Free / $99 / $399, priced per repo | (Impact 연장) | Stripe 테스트 모드 스크린샷, TAM 한 줄 |
| 10 | What's next | **Future roadmap** | JS/TS 연산자 → GitHub App → TMMi 증적 SaaS. 월별 |

## 5.12 README 스켈레톤

```
# KillScore
> 100% coverage. 31% mutation score. The SaaS release gate that scores whether
> your AI-written tests can actually catch a bug.

[스크린샷 1: 런 뷰 — 커버리지 vs 뮤테이션 대비]   ← 첫 이미지는 랜딩이 아니라 제품 화면
🔗 Live: https://killscore.hajin.xyz  (데모: ?demo=1, 로그인 불필요)
🎬 Demo video (2:45) · 🖼 Deck (PDF)

## Why this is different
Codecov/SonarQube measure whether code ran. KillScore measures whether your tests
can disprove it — and unlike coverage, running more code does not raise the score.
vs mutmut/cosmic-ray: they are whole-repo CLIs that take hours; we scope to the PR diff
and finish in ~38 seconds as a merge gate.

## Architecture
[다이어그램] Diff Scoper → AST Mutation Engine (9 operators) → Sandboxed Runner (8 workers,
no network, 8s timeout) → Score & Gate → Evidence Export.  LLM Test Proposer (dotted).
Latency p50 38s / p95 61s · $0.04 per run · timeout is never counted as a kill.

## What the model is allowed to do
The model never computes the score. The model never marks a mutant killed.
The model never edits the code under test. A proposed test is shown only after our
runner proves it passes on the original and fails on the mutant.

## Evaluation
`make eval` → 20 planted bugs, baseline + ablation.  [표 자동 삽입]

## Quickstart (3 commands)
cp .env.example .env && docker compose up -d && make seed

## Who it's for / Business model
Free (public repos) / Team $99 / Business $399 — priced per repository, not per seat.

## Challenges
- (구체적 고유명사 실패담 2개 이상 — "시간 부족" 금지)
## What's next
## License — Apache-2.0
```
추가 파일: `LICENSE`(Apache-2.0), `CONTRIBUTING.md`, `.env.example`, `HACKATHON.md`(재사용 범위 명시),
이슈 템플릿 1개. **주최가 OSC(오픈소스 온보딩 커뮤니티)라 이건 형식이 아니라 그들의 본업이다.**

## 5.13 Devpost 제출 정보

- **Title**: `KillScore — the SaaS release gate that scores whether your AI-written tests can catch a bug`
- **Tagline**: `100% coverage. 31% mutation score. We flip one operator in your payment logic and watch all 47 tests still pass.`
- **Built With**: `python` `fastapi` `postgresql` `nextjs` `react` `typescript` `tailwind` `shadcn-ui`
  `claude` `anthropic` `pytest` `ast` `mutation-testing` `stripe` `sse` `docker` `weasyprint` `neon` `apache-2.0`
- 본문 구조: 표준 7섹션 + **"Why this is different"** + **"Architecture"** + **"Who it's for / Business model"**.
  분량 900~1,600단어, 이미지 3~6장(첫 장은 제품 화면), 설명란에 **"SaaS"** 명시,
  코드워드 심기(`real world utility`, `reproducible setup`, `baseline`, `ablation`, `technical quality`).
- 데모 계정 / `?demo=1` 파라미터를 제출 폼에 명시.

## 5.14 "만들지 않을 것" 목록 (오늘 한정, 예외 없음)

1. **`browser_toolset_20260801` executor** — 어떤 형태로도. 3~5시간이 화면에 안 보인다.
2. **격리 샌드박스(gVisor/Firecracker)** — 서브프로세스 + 타임아웃 + 네트워크 차단까지. 나머지는 로드맵.
3. **임의의 공개 repo 자동 클론·실행** — 큐레이션된 데모 repo 3개 + 붙여넣기 플레이그라운드만.
   ("샌드박스 보안을 고려해 화이트리스트로 시작했다"가 오히려 성숙해 보인다.)
4. **GitHub App / OAuth 설치 플로우** — Checks 형식 JSON **프리뷰**까지만.
5. **JS/TS·Java 뮤테이션 연산자** — 파이썬만. 로드맵 슬라이드로.
6. **실시간 WebSocket** — SSE 단방향이면 충분하다. 폴링도 티 안 난다.
7. **자체 인증 시스템** — 단일 데모 org + `?demo=1` 우회. 팀 모델은 스키마에만 존재.
8. **`thinking: {budget_tokens: N}`** — Opus 5 / Sonnet 5 / Fable 5.1에서 **400**. `{type:"adaptive"}`.
9. **커버리지 리포트 자체 구현** — `coverage.py` 출력 파싱만.
10. **eval을 "시간 남으면"으로 미루는 것** — **H9(01:00–02:00)는 협상 불가.**
11. **다크모드·모바일을 H10으로 미루는 것** — H8에 끝낸다(UX 15점).
12. **03:00 이후 코드 수정** — 프리즈. 그 뒤 5시간은 전부 Presentation 15점이다.

---

# 6. 차순위 5개 (판단이 다를 경우)

**① Clock14 (EV 94.3, 재채점 전체 1위 · 하드 필터 F3으로만 탈락).**
EU Cyber Resilience Act Art.14의 24시간 조기경보 의무가 **2026-09-11에 발효**되고 ENISA Single Reporting
Platform이 같은 날 가동됐다 — **오늘 기준 D+4**로, 3,403팀 중 누구도 선점할 수 없었던 유일한 why-now다.
SBOM의 purl을 CISA KEV와 대조해 "법적 시계가 시작됐는가"를 불리언으로 판정하고, 24h/72h/14d 마감을
순수 함수로 계산하며, 증적을 append-only 해시체인에 쌓고, LLM은 17개 필드 중 3개의 산문만 초안한다 —
결정론 비중과 승인 게이트 서사가 후보 전체에서 가장 강하고 Impact(€15M 또는 매출 2.5%)는 반박 자체가
불가능하다. **내가 기각한 단 하나의 이유는 ENISA SRP 폼의 실제 필드 스키마를 어느 리서치 문서도
검증하지 못했다는 것**이고, 보안 분석가가 앉은 패널 앞에서 규제 양식을 그럴싸하게 지어내는 것은
발각 시 제품 전체 신뢰가 0이 되는 종류의 리스크다. **양식 프리필을 버리고 "시계 + 증적 + 에스컬레이션"만
남기면 F3을 통과하고 즉시 1순위가 된다** — 사용자가 그 축소를 받아들인다면 KillScore 대신 이걸 골라도
좋다. 부차 리스크는 NVD 레이트리밋과 purl↔KEV 자유텍스트 매칭의 모호함이며, 데모 SBOM 3개를 직접
만들어 시드하면 해소된다.

**② SilentSLO (EV 86.6 · 이번 결정의 헤지).**
*"Your uptime dashboard says 99.98%. Meanwhile 24% of your agent's tool-call chains silently returned
garbage — with a 200 OK."* OpenAI 호환 리버스 프록시 위에 **LLM 호출 0회로 도는 invariant 8종**
(JSON 스키마 검증, 툴콜 인자 유효성, 조용한 컨텍스트 절단, 인용 앵커 대조, 거절률 드리프트, 반복
n-gram, `finish_reason=="length"`, EWMA 이상치)을 얹고, 위반을 **Silent Failure Rate SLO와 에러버짓
번레이트**로 환산해 온콜을 페이지한다. 심사위원 중 공개 발신량 1위인 Vasuki Vudathala(ServiceNow)가
*"I Watched Our AI Pipeline Silently Fail While Kubernetes Said Everything Was Fine"* 와
*"Why GPU Utilization Is the Wrong North Star"* 두 편을 썼으니 1:1 저격으로는 KillScore의 Peri와 동급이다.
약점은 두 가지다 — Langfuse·Arize·Helicone·Braintrust·Datadog라는 **명명된 경쟁사 다섯**이 Innovation 20점을
갉아먹고, 영상 훅의 좌측 "전부 초록인 인프라 패널"이 **내가 만든 목업**이라 주최측의
`"pitch decks, concept videos"` 배제 문구 쪽으로 반 걸음 기운다. 스트리밍 패스스루를 포기하고
non-stream + 시드 리플레이로 축소하면 P가 0.82→0.92로 오른다.

**③ Article50 / S1 (EV 84.9 · 05문서와 C문서의 1위).**
EU AI Act Article 50이 2026-08-02에 적용됐고 기존 생성형 AI의 기계판독 마킹 유예가 **2026-12-02에 만료**
— 오늘 기준 **D-78**이며, 과징금은 €15M 또는 전세계 매출 3% 중 높은 쪽(단 SME·스타트업은 낮은 쪽,
이 디테일을 화면에 같이 띄우면 "법을 실제로 읽었다"는 신호가 된다). `browser_toolset`을 완전히 버리고
Playwright를 직접 몰아 `page.on("request")`로 챗봇 벤더 40종을 **네트워크 요청 도메인 fingerprint**로
잡으면 cross-origin iframe 문제가 아예 사라지고, 조항별 PASS/FAIL/REVIEW 판정은 전부 코드에 있으며
Claude는 "이 고지 문구가 평균적 자연인에게 명백한가" 분류와 수정 스니펫 생성 두 가지만 한다.
UX 15 + Presentation 15 = 30점을 거의 만점으로 가져가는 유일한 후보이고 "URL 붙여넣고 90초"는 3분
영상에 완벽히 맞는다. **내가 P를 0.88에서 0.70으로 내린 이유는 심사위원이 자기 회사 URL을 넣는 순간
WAF·봇 차단·40개 fingerprint 커버리지 밖의 벤더·45초 타임아웃 네 가지가 곱해지기 때문**이고,
컴플라이언스 도구에서 빈 결과나 오탐은 치명적이다. 자체 픽스처만으로 데모하면 안전해지지만
그 순간 와우 모먼트가 사라진다.

**④ MCPGate / S3 (EV 82.4 · P 0.92로 필터 통과군 중 최고 신뢰도).**
MCP **2026-07-28 스펙**이 `initialize` 핸드셰이크와 `Mcp-Session-Id`를 없애고 `Mcp-Method`/`Mcp-Name`을
HTTP 헤더로 승격시킨 덕분에, **바디 파싱 없이 평범한 리버스 프록시에서 툴 단위 인가·감사가 가능**해졌다 —
이전 스펙에서는 구현 자체가 불가능했던 제품 형태라 why-now가 기술적으로 단단하다. `tools/list`를 HTTP
POST 한 번으로 수집 → 정적 분석(설명 내 URL·IP 리터럴, 광범위 스코프, 프롬프트 인젝션 정규식 24종,
제로폭 문자, 이름 스쿼팅, 설명↔스키마 불일치) → Risk Score → 정책 YAML 자동 생성 → **~150줄짜리
FastAPI 프록시가 실제로 강제**하고 차단 로그가 SSE로 실시간으로 쌓인다. 결정적 이점은 **악성 MCP
서버(`evil-docs-mcp`, 80줄)를 내가 직접 작성**한다는 것 — 외부 의존성이 0이라 라이브 실패 확률이 후보
중 최저다. 프록시 차단 p95 **4ms**는 ServiceNow 성능 엔지니어에게 다른 어떤 숫자보다 잘 먹힌다.
약점은 보안 대시보드라 UX 15점이 얇고, 도메인 설명에 30초가 들며, PM 7인이 *"우리 회사엔 이미 API
게이트웨이가 있는데요"* 라고 물을 때 Impact가 간접적이라는 점이다. TOCTOU 반박은 덱에서 먼저 인정하고
프록시의 런타임 관측이 그 답의 절반임을 명시해야 한다.

**⑤ SpecDrift (EV 80.2 · 패널 최대 블록을 노리는 안정형).**
*"Your team merged 47 PRs this sprint. 12 of them don't map to a single acceptance criterion, and 5
acceptance criteria shipped nothing."* 수용기준과 머지된 PR 사이의 **추적성 매트릭스(RTM)** 를 자동으로
만들고, 셀을 `Covered / Partial / Orphan PR / Ghost AC` 네 상태로 칠한다. 이 네 상태가 전부
**집합 연산**(`AC ∩ PR`, `AC \ PR`, `PR \ AC`, `PR ∩ AC \ Test`)이고 명시적 ID 링크(`PROJ-123`,
`Closes #`)는 정규식으로 100% 확정되므로, "68%는 LLM 없이 확정됨"을 화면에 상시 표시하면 wrapper
방어가 된다. 이 후보의 유일무이한 강점은 **심사위원 20명 중 최대 단일 블록인 PM 7인 전원**(Boinpally,
Dhage, Nikam, Nalagath, Havryliuk, Tripathi, Phan)이 스프린트 리뷰에서 매주 이 질문을 받는 쪽이라는
것이고, 동시에 RTM은 Peri의 TMMi 필수 산출물이라 **엔지니어 심사위원과 PM 심사위원을 한 화면으로
동시에 만족시키는 유일한 후보**다. 약점은 날짜로 고정되는 why-now가 없고("2026년에 SDD 툴이
전면화됐다"는 시점이 흐리다), 임베딩 유사도 매칭이 "LLM으로 티켓과 PR을 붙였다"로 읽힐 위험이
있으며, 천장이 81로 1~3위보다 낮다는 것이다. 리스크가 가장 낮은 카드를 원한다면 이것과 AgreeGate(82.7)다.

---

## 부록 — 무엇을 만들든 반드시 들어가는 것 (03·05 문서 교차 결론)

1. 태그라인에 **측정된 숫자 1개**.
2. **초니치 타깃 1인**을 이름 붙여 부를 것.
3. **명명된 경쟁사 + 1문장 차이** — 덱과 영상 양쪽.
4. **LLM 권한 제한을 화면에 상시 표시.**
5. **의도적 실패 시연 15~20초.**
6. **비용·레이턴시 숫자 3개 이상 + 20건 eval 표**(baseline·ablation 열 포함).
7. **Stripe 테스트 모드 가격 페이지** + 좌석 아닌 과금 단위.
8. 영상 **2:30~3:30**, 라이브 화면 60% 이상, `?demo=1` 로그인 우회.
9. 공개 GitHub + README + LICENSE + 셋업 가이드 (주최가 OSC다).
10. **T-4h(09-16 08:00 KST) 1차 제출 + Submitted 배지 확인.**
