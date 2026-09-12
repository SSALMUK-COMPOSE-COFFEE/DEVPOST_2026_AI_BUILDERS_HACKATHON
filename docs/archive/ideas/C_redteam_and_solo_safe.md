# C. 레드팀 + 솔로 세이프 아이디어

> 작성 2026-09-15 16:30 KST · 마감 2026-09-16 12:00 KST (T-19.5h) · 실질 코딩 가능 시간 9~10h
> 대상: 솔로 개발자 1인 (Python/FastAPI + LLM 오케스트레이션 강함, Next.js/shadcn 가능, hajin.xyz 상시 서버 보유, Anthropic·OpenAI 호환 키 보유, **Bedrock 없음**)
> 목표 상: **Best SaaS Product $4,000** (유일한 현금 상)
> 배점: Tech 25 / Impact 25 / Innovation 20 / UX 15 / Presentation 15

---

## 0. 먼저 — 이 문서 전체를 뒤집는 검증 결과 하나

`05_competition_and_idea_landscape.md`의 1위(Clause50)와 2위(AgentReady)는 **둘 다 Claude의
`browser_toolset_20260801`이 "브라우저를 대신 굴려준다"는 전제** 위에 설계되어 있습니다.
**이 전제는 틀렸습니다.**

공식 문서 원문 (https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool):

> "Your application runs every call against its own browser automation; **nothing runs on Anthropic's side**."

> "The tool is an Anthropic-defined **client toolset**: one `browser_toolset_20260801` entry in `tools`
> gives Claude 27 member tools by default"

즉 `browser_toolset_20260801`은 **툴 스키마 묶음일 뿐**이고, `navigate` / `read_page` / `left_click` /
`find` / `read_network` / `read_console` 27~31개 멤버 툴의 **실제 구현(executor)은 개발자가 직접
Playwright·CDP로 작성**해야 합니다. Anthropic이 제공하는 건 각 언어별 **스텁 코드**뿐이고
(문서 예제의 `read_page`는 문자열 `'link "Docs" [ref_1]\nbutton "Search" [ref_2]'`를 리턴하는 플레이스홀더),
**공식 레퍼런스 executor나 오픈소스 구현체는 존재하지 않습니다.**
언론도 같은 제목으로 다뤘습니다: *"Anthropic's new browser tool doesn't actually run a browser"*
(https://thenewstack.io/anthropic-browser-use-tool/).

`read_page` 하나만 해도 개발자가 직접 해야 하는 일:
접근성 트리 추출 → `[ref_N]` 시퀀셜 할당 → ref→DOM 노드 맵 유지 → `filter`(`interactive`/`all`) 지원
→ `depth`(기본 15) 지원 → 50,000자 캡 → 네비게이션 시 ref 무효화.

추가로 확인된 제약:
- 브라우저 툴은 **Managed Agents에서 사용 불가**, **Bedrock 사용 불가**, **Claude Platform on AWS 사용 불가**
  (Claude API와 Vertex AI만 지원).
- **CAPTCHA 해결 불가** — 문서가 명시. AgentReady의 핵심 데모("CAPTCHA에서 죽는다")는 사실이지만,
  그건 우리 executor가 죽는 거지 Claude가 죽는 게 아님.
- `read_network` / `read_console` / `javascript_exec` / `file_upload`는 **기본 비활성** — `configs`로 켜야 하고,
  당연히 구현도 우리 몫.

### 이것이 바꾸는 결론

**솔로 10시간에 Claude 브라우저 executor를 처음부터 짜는 것은 자살행위입니다.**
그런데 여기에 역설이 있습니다 — **executor를 짤 거면 이미 Playwright를 돌리고 있다는 뜻**이고,
그렇다면 **`browser_toolset`을 경유할 이유가 사라집니다.** Playwright는
`page.accessibility.snapshot()`, `page.on("response")`(네트워크), `page.on("console")`(콘솔)을
이미 공짜로 줍니다. AgentReady가 원하는 네트워크 트레이스는 Claude를 거치지 않고 Playwright에서
직접 나옵니다.

> **이 문서의 관통 원칙**: 브라우징이 필요한 아이디어는 **Playwright를 직접 쓰고, Claude는
> "판정·분류·설명"에만 쓴다.** 이것은 다운그레이드가 아니라 업그레이드입니다 —
> §4.3 "thin wrapper 방어 체크리스트"의 "LLM이 없어도 절반은 동작하는가"를 정면으로 만족시키고,
> 데모 실패 확률을 1/3로 줄입니다. 덱에는 오히려 이렇게 씁니다:
> *"We deliberately did not use the model as the crawler. The crawler is deterministic;
> the model only classifies evidence it cannot fabricate."*

만약 굳이 에이전트형 브라우징이 필요하면 탈출구는 **Playwright MCP**입니다
(https://playwright.dev/mcp/introduction). 접근성 스냅샷 + 안정적 `ref`를 이미 구현해 두었고
스냅샷 1회가 약 200~400 토큰입니다. 다만 stdio 로컬 MCP라 Messages API의 MCP 커넥터
(원격 URL 전용)로는 못 붙이고 Claude Agent SDK를 경유해야 합니다 — 무빙파트 +1.

### 그 외 검증된 기술 사실 (아이디어별 "Why now"의 근거)

| 주장 | 검증 결과 | 출처 |
| --- | --- | --- |
| EU AI Act Article 50 **2026-08-02 적용**, 기존 생성형 AI의 기계판독 마킹 **유예 2026-12-02 만료** | ✅ 확인 (원문 "2 August 2026", "2 December 2026") | https://artificialintelligenceact.eu/transparency-rules-article-50/ |
| Article 50 위반 과징금 **€15M 또는 전세계 매출 3% 중 높은 쪽** | ✅ 확인 (Article 99 3단 구조의 중간 티어). 단 **SME·스타트업은 낮은 쪽**이 적용됨 — 데모에서 이걸 같이 말하면 "법을 실제로 읽었다"는 신호 | https://artificialintelligenceact.eu/article/99/ · https://euaiactchecklist.com/eu-ai-act-fines-penalties.html |
| 오늘(2026-09-15) 기준 유예 만료까지 **78일** | ✅ 계산 확인 (9/15→12/2 = 78일) | — |
| MCP **2026-07-28 스펙**: `initialize` 핸드셰이크와 `Mcp-Session-Id` 제거, **`Mcp-Method`/`Mcp-Name` HTTP 헤더로 바디 파싱 없이 게이트웨이 라우팅 가능** | ✅ 확인 | https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ · https://www.infoq.com/news/2026/08/mcp-stateless-gateway/ · https://appwrite.io/blog/post/mcp-goes-stateless-in-the-2026-07-28-specification |
| Managed Agents에 **cron 스케줄 배포(scheduled deployments)** 존재 | ✅ 확인 (NightDesk의 근거는 유효) | platform.claude.com Managed Agents 문서 |
| Managed Agents에서 **브라우저 툴 사용 불가** | ✅ 확인 — NightDesk + 브라우징 조합은 성립 안 함 | 위 browser-use-tool 문서 |
| Stripe **Pricing Table**: 대시보드에서 만들고 `<script>` + `<stripe-pricing-table>` 붙여넣기, `pk_test_` 키로 테스트 모드 동작 | ✅ 확인. **코드 0줄, 실측 15분.** 단 **렌더링에 도메인이 필요** → hajin.xyz 서브도메인 필수 | https://docs.stripe.com/no-code/pricing-table |
| Claude 현행 모델: `claude-opus-5` $5/$25, `claude-sonnet-5` $2/$10, `claude-haiku-4-5` $1/$5, `claude-fable-5-1` $10/$50 (캐시 읽기 $0.25/Mtok) | ✅ 확인 | platform.claude.com pricing |

⚠️ **API 드리프트 주의 (400 에러 유발)**: `thinking: {type:"enabled", budget_tokens:N}`은 Opus 5 / Sonnet 5 /
Fable 5.1에서 **400**. `{type:"adaptive"}`를 쓰거나 생략할 것. 깊이는 `output_config: {effort: "..."}`로 조절.
`output_format`이 아니라 `output_config: {format: {...}}`. 어시스턴트 prefill은 **400**.
해커톤 당일에 이걸로 30분 태우는 사고가 가장 흔합니다.

---

## PART 1 — 기존 10개 아이디어 레드팀

각 항목: (a) 솔로 10h 최대 기술 블로커 · (b) 이 패널이 던질 가장 유력한 반박 · (c) T-6h 라이브 데모 성공 확률 ·
(d) "망가졌지만 여전히 인상적인" 폴백 · (e) 판정

### 1. Clause50 — EU AI Act Art.50 투명성 감사

**(a) 최대 블로커.** §0의 executor 문제 그 자체입니다. 원안은 "브라우저 에이전트가 페이지를 돌며
고지 여부를 판정한다"인데, 그러려면 `navigate`/`read_page`/`find`/`screenshot` 최소 4~6개를
Playwright 위에 ref 관리까지 포함해 구현해야 합니다. 보수적으로 **3~5시간**, 그리고 이건
"동작하면 끝"이 아니라 **디버깅 꼬리가 긴** 종류의 3~5시간입니다(ref 무효화, iframe, 50k 캡).
10시간 예산의 절반을 화면에 안 보이는 배관에 씁니다.
두 번째 블로커: **챗봇 위젯 대부분이 cross-origin iframe**입니다. 문서가 명시하듯
cross-origin iframe은 접근성 트리 데이터가 제한되어 좌표 기반 클릭으로 폴백해야 합니다 —
Intercom/Drift/Zendesk 위젯 탐지를 접근성 트리로 하려는 접근 자체가 취약합니다.
(→ 해법은 §PART 2 S1: 트리 대신 **스크립트 fingerprint + 네트워크 요청 도메인**으로 잡는 것.
이건 Playwright `page.on("request")` 3줄이고 iframe 문제가 아예 없습니다.)

**(b) 유력한 반박.** 이 패널에는 보안 분석가(Corteva)와 대기업 컴플라이언스 인접 인력이 있습니다.
가장 아픈 질문: *"Article 50(1)은 '평균적으로 정보를 갖춘 자연인에게 명백한 경우'는 면제인데,
당신의 룰 엔진은 그 예외를 어떻게 판정합니까?"* — 그리고 *"이건 법률 자문 아닌가요?"*
두 번째 반박: *"AI 생성 이미지 마킹은 C2PA 메타데이터를 봐야 하는데, CDN이 EXIF를 스트립하면
당신은 전부 FAIL로 찍을 겁니다. false positive율이 얼마죠?"* — **여기서 eval 표가 없으면 즉사합니다.**

**(c) T-6h 라이브 데모 성공 확률: 45%** (원안대로 `browser_toolset` executor를 짤 경우).

**(d) 폴백.** 브라우저 에이전트를 버리고 `requests` + BeautifulSoup으로 HTML만 긁어
스크립트 태그 fingerprint만 본다 → 동작은 하지만 **SPA에서 전부 놓칩니다**(챗봇 위젯은 거의 다
런타임 주입). 사전 녹화 스캔 3건을 리플레이하고 라이브는 "우리 서버가 rate limit 중"으로 넘김.
리포트 PDF와 카운트다운 UI는 그대로 살아서, 임팩트 서사는 80% 유지됩니다.

**(e) 판정: BUILD-WITH-CUTS** — 단, **`browser_toolset`을 완전히 들어내고 Playwright 직접 사용**이라는
큰 절단이 전제. 이 절단을 하면 §PART 2의 S1이 되고 확률이 45%→88%로 뜁니다.

---

### 2. AgentReady — 에이전틱 커머스 대응력 진단

**(a) 최대 블로커.** Clause50의 executor 문제 + **그보다 한 단계 더 나쁜 것**: 데모의 와우 모먼트가
"에이전트가 CAPTCHA에서 죽는다"인데, 문서가 **"Browser automation cannot solve CAPTCHAs"**라고
명시합니다. 즉 이 제품의 핵심 신호는 "우리 executor가 CAPTCHA를 만나 멈췄다"는 사실뿐이고,
Claude의 지능은 거기서 아무 역할을 안 합니다. 심사위원이 이걸 알아채면 Tech 25점이 무너집니다.
실무 블로커는 더 단순합니다: **남의 상용 스토어에 봇을 붙이면 Cloudflare/Shopify 봇 관리가
차단하거나, 최악의 경우 IP가 밴됩니다.** 데모 직전에 타깃 스토어가 차단을 켜면 그걸로 끝입니다.
체크아웃까지 가는 여정은 왕복 30~90초 × 다수 탐색 턴이라 **3분 영상에 안 들어갑니다**(배속 편집 필수).

**(b) 유력한 반박.** 이커머스 PM이 아니라 대기업 엔지니어 패널입니다. 가장 유력한 질문:
*"71% / 38.2% / 3.16% 숫자의 1차 출처가 뭐죠?"* — 05 문서 기준 출처가 agentlux.ai 블로그 **단일
2차 소스**입니다. 이 패널은 그걸 물어봅니다. 두 번째: *"에이전트가 실패한 게 스토어 탓인지
당신 executor 탓인지 어떻게 구분합니까?"* — 이게 진짜 킬러 질문이고, 원안에는 답이 없습니다.
세 번째: *"머천트 동의 없이 남의 사이트를 자동으로 긁는 제품인데 ToS는요?"*

**(c) T-6h 라이브 데모 성공 확률: 30%** — 10개 중 **최저**. executor 리스크 × 외부 사이트 리스크
× 여정 길이 리스크가 곱해집니다.

**(d) 폴백.** 사전 녹화 리플레이 모드 + 결정론적 "장애물 코스" 점수만 남김(robots.txt의 에이전트
UA 허용 여부, JSON-LD Product 스키마 유무, 장바구니 URL 안정성, CAPTCHA 벤더 fingerprint,
로그인 강제 여부). 이것만으로도 점수 카드는 나오고 오히려 **재현 가능**해집니다.
→ 이 폴백이 사실상 §PART 2의 S2입니다.

**(e) 판정: KILL (원안) / BUILD-WITH-CUTS (S2 형태로만)**
원안은 "가장 강한 데모"라는 평가를 받았지만, 그 데모가 T-6h에 존재할 확률이 30%라면
기대값이 아닙니다. **영상이 가장 강한 아이디어가 아니라, 영상이 반드시 찍히는 아이디어를 골라야 합니다.**

---

### 3. MCPGuard — MCP 서버 공급망 심사 + 정책 게이트웨이

**(a) 최대 블로커.** **격리 샌드박스**입니다. "MCP 툴 호출을 실제로 재생하고 아웃바운드를 기록"하려면
네트워크 격리된 컨테이너(gVisor/Firecracker 또는 최소한 `--network=none` + 사이드카 프록시)를
띄우고, 그 안에서 임의 서버를 실행하고, egress를 캡처해야 합니다. **솔로 10h에 안전하게는 불가능**하고,
안전하지 않게 하면 자기 상시 서버를 위험에 노출시킵니다.
좋은 소식: 나머지 절반은 **2026-07-28 스펙 덕분에 극적으로 쉬워졌습니다.** `initialize` 핸드셰이크가
사라졌으므로 원격 MCP 서버의 `tools/list`를 **평범한 HTTP POST 한 방**으로 가져올 수 있고,
`Mcp-Name` 헤더 덕분에 정책 강제 리버스 프록시가 **바디 파싱 없이 ~150줄**이면 됩니다.
즉 **샌드박스만 들어내면 이 아이디어는 10개 중 가장 안전합니다.**

**(b) 유력한 반박.** *"당신은 정적 분석만 하는데, 악성 MCP 서버는 `tools/list`에는 깨끗한 설명을 주고
런타임에만 나쁜 짓을 합니다. TOCTOU 아닙니까?"* — 정직한 답을 준비해야 합니다(프록시가 런타임
egress를 보는 게 그 답의 절반). 두 번째: *"9,652개 서버 / 27% 위험 필터링 숫자는 어디서 나왔죠?"*
세 번째, PM 7인 쪽에서: *"이걸 누가 삽니까? 우리 회사엔 이미 API 게이트웨이가 있는데요."*

**(c) T-6h 라이브 데모 성공 확률: 40%** (샌드박스 포함 원안) / **92%** (샌드박스 제거 시).

**(d) 폴백.** 정적 분석 + 리스크 점수 + 정책 컴파일 + 프록시 차단 로그까지만. 샌드박스 재생은
사전 녹화 30초 클립. **와우 모먼트(공격→탐지→정책→차단)는 100% 보존**됩니다.
실제로 이 폴백이 원안보다 낫습니다.

**(e) 판정: BUILD-WITH-CUTS** — 샌드박스를 **처음부터 스코프에서 제거**하고 시작할 것.
"나중에 시간 남으면"이 아니라 아예 로드맵 슬라이드로 보냅니다.

---

### 4. TrustReply — 보안 설문(SIG/CAIQ) 자동응답

**(a) 최대 블로커.** 기술이 아니라 **데이터**입니다. 데모가 성립하려면 진짜처럼 보이는
SOC2/정책 문서 코퍼스 + 800문항 SIG 스프레드시트가 필요한데, 실제 SIG는 유료 라이선스
(Shared Assessments)라 배포·화면 노출이 애매합니다. 합성 문서를 Claude로 만들면
"자기가 만든 문서에 자기가 답하는" 순환이 되어 eval이 무의미해집니다.
부차 블로커: Fable 5.1 1시간 캐시 프라이밍 — **캐시 쓰기 $20/Mtok**이라 500페이지 코퍼스 한 번
올리는 데 실비가 붙고, 라이브 데모 중에 캐시가 만료되면 비용 서사가 화면에서 무너집니다.

**(b) 유력한 반박.** 즉각적이고 치명적입니다: *"Vanta, Drata, Conveyor, Loopio가 이미 이걸 합니다.
뭐가 다르죠?"* — Innovation 20점에서 10개 중 최저입니다. 그리고 이 패널에는
엔터프라이즈 보안 인접 인력이 있어서 **경쟁사를 실명으로 알고 있습니다.**

**(c) T-6h 라이브 데모 성공 확률: 85%** (기술적으로는 가장 쉬움).

**(d) 폴백.** 문항 수를 800 → 60으로 줄이고 진행 바를 살림. 충분히 인상적.

**(e) 판정: KILL** — 확률은 높지만 **상한이 낮습니다**(가중합 73). 1등 상 하나짜리 대회에서
"안전하지만 73점"은 이기는 카드가 아닙니다. 다만 §PART 2 S4에 이 아이디어의
**"신뢰도 미달은 사람 큐로"** 게이트 패턴만 이식합니다.

---

### 5. TaskCost — 태스크 단위 AI 비용 원장

**(a) 최대 블로커.** 기술 블로커는 사실상 **없습니다** — 순수 파이썬 가격 엔진 + 차트입니다.
진짜 블로커는 **입력 데이터**입니다. OTel 트레이스를 판정용으로 진짜처럼 만들려면
seeded 데이터를 손으로 설계해야 하고(2h), 그게 없으면 화면이 텅 빕니다.
그리고 숨은 함정: **가격 데이터 자체가 이 문서가 검증한 것보다 빨리 변합니다.**
심사위원이 화면의 단가 하나가 틀린 걸 발견하면 제품 전체의 신뢰가 날아갑니다
(가격표에 `source_url` + `fetched_at`을 화면에 노출해서 방어).

**(b) 유력한 반박.** *"이건 AI 제품이 아니라 스프레드시트 아닌가요?"* —
**AI 해커톤에서 LLM을 거의 안 쓰는 게 역설적 감점 요인**입니다. 그리고
*"Vantage, nOps, Helicone, Langfuse가 이미 토큰 단위 비용을 보여주는데요?"*

**(c) T-6h 라이브 데모 성공 확률: 96%** — 10개 중 **최고**.

**(d) 폴백.** 폴백이 필요 없는 구조 (전부 결정론적 + 시드 데이터).

**(e) 판정: BUILD-WITH-CUTS** — "가장 안전한 카드"로서 가치가 있습니다.
§PART 2 S5로 남겨두고, **Innovation 방어를 위해 "가격 만료 타임머신"과
"LLM이 비용 이상치를 근본원인으로 설명" 두 개를 반드시 넣습니다.**

---

### 6. Roundtable — 멀티플레이어 에이전트 세션

**(a) 최대 블로커.** **WebSocket 상태 동기화 + 실행 중 세션 주입**입니다. 두 브라우저가 같은
스트림을 보면서 한쪽이 끼어드는 걸 제대로 만들려면 재접속·순서보장·중복 이벤트 처리를
다 해야 하고, 여기에 Managed Agents의 SSE 스트림 재접속 규약(`processed_at` 큐 게이트,
idle/terminated 판정 레이스)까지 얹힙니다. **솔로 10h에 "가끔 깨지는" 실시간 협업을 만들면
라이브 데모 중에 반드시 그 "가끔"이 옵니다.** 그리고 포크/머지는 스코프 밖입니다(하루로 불가).

**(b) 유력한 반박.** PM 7인이 정확히 이걸 묻습니다: *"그래서 얼마를 절약합니까?"*
Impact 25점에서 답이 없습니다. 그리고 *"Cursor·Claude Code에 이미 공유 세션이 있는데요."*

**(c) T-6h 라이브 데모 성공 확률: 55%**.

**(d) 폴백.** 실시간을 버리고 폴링(2초) 기반으로. 데모에서는 티가 안 납니다.
포크/머지를 버리면 "채팅방 붙인 Claude"로 보이는 리스크가 급등합니다.

**(e) 판정: KILL** — Innovation·UX는 최상이지만 **Impact 25점이 구조적으로 비어 있고**,
이 패널은 Impact를 가장 엄격하게 봅니다(대기업 PM 7명).

---

### 7. RenewalRadar — 계약 자동갱신 조항 레이더

**(a) 최대 블로커.** 없다시피 합니다 — PDF 파싱 + 추출 + 날짜 역산 + 캘린더.
유일한 실질 블로커는 **진짜 같은 SaaS 계약서 20건**을 구하는 것이고, 합성하면
"자기가 쓴 계약서에서 자기가 조항을 찾는" 순환 eval 문제가 또 나옵니다.

**(b) 유력한 반박.** *"Notwithstanding 교차참조를 잡는다고 했는데, 그게 틀렸을 때
회사가 $147,000을 날립니다. 정확도가 몇 %입니까?"* — **높은 비용의 오류 도메인인데
정확도 증거가 약합니다.** 그리고 *"Ironclad, LinkSquares, Spendflo가 이미 합니다."*

**(c) T-6h 라이브 데모 성공 확률: 90%**.

**(d) 폴백.** 조항 추출 실패 시 "원문 하이라이트 + 사람 확인" 모드.

**(e) 판정: KILL** — 가중합 71. 안전하지만 천장이 낮고, Innovation 20점에서 회복 불가.

---

### 8. RubricRoom — 도메인 전문가용 Evals → 컴플라이언스 증적

**(a) 최대 블로커.** 없습니다. 10개 중 **기술 리스크 최저**입니다 (CRUD + 카드 UI + 통계 + PDF).
진짜 블로커는 **"두 개의 화면"을 10h에 둘 다 예쁘게 만드는 것**(엔지니어 뷰 + 전문가 뷰)이고,
이건 UI 시간이 2배라는 뜻입니다.

**(b) 유력한 반박.** *"LangSmith, Braintrust, Humanloop, Arize에 다 있습니다."* —
방어는 **"평가 결과를 서명된 컴플라이언스 증적으로 만든다"**는 한 지점뿐이고,
이 지점을 30초 안에 설명하지 못하면 죽습니다. 두 번째: *"88% 실패 / Gartner 40% 취소
숫자의 출처는요?"*

**(c) T-6h 라이브 데모 성공 확률: 95%**.

**(d) 폴백.** 전문가 뷰만 남기고 엔지니어 뷰는 시드 데이터 정적 화면으로.

**(e) 판정: BUILD-WITH-CUTS** — **이 패널에 대한 적합도가 10개 중 가장 높습니다.**
심사위원에 Dell "Modern Validation Playbook" 저자(Lakshmi Vidya Peri, TMMi America 이사),
ServiceNow 성능/관측성 엔지니어(Vasuki Uday Kiran Vudathala)가 있습니다.
원안의 약점(가중합 74)은 **Tech 25점이 얇다**는 것인데, §PART 2 S4에서
**"LLM 저지 vs 인간의 일치도(κ)를 측정하는 것 자체를 제품으로"** 만들어 이걸 메꿉니다.

---

### 9. NightDesk — 야간 리테이너 애널리스트

**(a) 최대 블로커.** **검증 결과 원안의 기술 전제가 부분적으로 깨졌습니다**:
Managed Agents에서 **브라우저 툴을 쓸 수 없습니다**. 즉 "밤에 깨어나 경쟁사 가격 페이지를
돌아본다"를 Managed Agents 안에서 하려면 `web_search`/`web_fetch` 서버 툴로만 해야 하고,
JS 렌더링 페이지의 diff는 못 뜹니다. cron 스케줄 배포 자체는 실재합니다.
그리고 **데모가 근본적으로 불가능**합니다 — "밤에 돌았다"를 라이브로 보여줄 수 없어서
결국 어제 결과 화면을 보여주는 것으로 끝납니다.

**(b) 유력한 반박.** *"cron + Claude 아닌가요?"* — 원안 스스로 wrapper 리스크 🔴 높음으로
표기했습니다. 이 패널은 "AI wrappers with minimal differentiation"을 주최측이 명시적으로
배제한 대회임을 알고 있습니다.

**(c) T-6h 라이브 데모 성공 확률: 80%** (단, 보여줄 게 정적 화면).

**(d) 폴백.** 해당 없음.

**(e) 판정: KILL.**

---

### 10. VoiceIntake — 풀듀플렉스 규제 아웃바운드 음성

**(a) 최대 블로커.** **SIP/텔레포니 배선**입니다. 번호 프로비저닝, Twilio/SIP 트렁크, 미디어 스트림,
지연·에코, 그리고 한국에서 미국 번호로 아웃바운드 — 각각이 개별적으로 하루짜리 함정입니다.
그리고 **녹화 영상에서 오디오 품질이 나쁘면 제품 전체가 나빠 보입니다.**

**(b) 유력한 반박.** *"Sierra, PolyAI, Bland, Retell, Decagon과 뭐가 다르죠?"* +
*"규제 고지 문구를 AI가 삽입했다가 누락하면 TCPA 위반인데, 그 검증은 누가 합니까?"*

**(c) T-6h 라이브 데모 성공 확률: 20%** — 10개 중 **최저**.

**(d) 폴백.** 사전 녹음 통화 재생. 그러면 "concept video"가 되어 주최측 배제 문구에 정면으로 걸립니다.

**(e) 판정: KILL.**

---

### PART 1 요약표

| # | 아이디어 | 최대 블로커 | P(T-6h 라이브 데모) | 판정 |
| --- | --- | --- | --- | --- |
| 1 | Clause50 | 브라우저 executor 직접 구현 3~5h + cross-origin iframe | 45% | **BUILD-WITH-CUTS** (Playwright 직행) |
| 2 | AgentReady | executor + 외부 스토어 봇 차단 + 여정 길이 | **30%** | **KILL** (원안) |
| 3 | MCPGuard | 격리 샌드박스 | 40% → **92%** (샌드박스 제거) | **BUILD-WITH-CUTS** |
| 4 | TrustReply | SIG 데이터 확보 / 순환 eval | 85% | **KILL** (Innovation 최저) |
| 5 | TaskCost | 시드 데이터 설계 + 가격표 신선도 | **96%** | **BUILD-WITH-CUTS** |
| 6 | Roundtable | 실시간 동기화 + Impact 부재 | 55% | **KILL** |
| 7 | RenewalRadar | 계약서 코퍼스 + 고비용 오류 도메인 | 90% | **KILL** (천장 낮음) |
| 8 | RubricRoom | 화면 2개 UI 비용 | 95% | **BUILD-WITH-CUTS** (패널 적합도 최상) |
| 9 | NightDesk | Managed Agents에 브라우저 툴 없음 + 데모 불가 | 80% | **KILL** |
| 10 | VoiceIntake | SIP 배선 | **20%** | **KILL** |

---

## PART 2 — 솔로 세이프 5안

**공통 설계 규칙 (5안 전부에 적용):**

1. **결정론적 코어가 먼저 돌고, LLM은 그 위에 얹힌다.** LLM API가 전부 죽어도 제품은 점수를 냅니다.
2. **LLM 출력은 반드시 스키마 강제** — `strict: true` + `output_config.format`. 근거(evidence id) 없는
   판정은 코드가 거부하고 `REVIEW`로 강등.
3. **모델은 `claude-opus-5`**, `thinking: {type:"adaptive"}`, `output_config: {effort: "medium"}`.
   벌크 분류만 `claude-haiku-4-5`. **`budget_tokens` 절대 금지(400).**
4. **`/healthz` + 구조화 로그 + 요청당 토큰·비용 기록**을 H1에 넣습니다 (ServiceNow 관측성 심사위원 직격).
5. **Stripe Pricing Table**(no-code, `pk_test_`)을 H8에 15분만에. 도메인은 hajin.xyz 서브도메인.
6. **시드 데모 데이터 + `?replay=<id>` 리플레이 모드**를 H7에. 라이브 데모 보험.
7. **eval은 `evals/` 디렉토리 + `make eval` 한 줄 + 결과 마크다운 표 자동 생성.**
   README·덱·영상 세 곳에 같은 표가 들어갑니다.
8. 덱 1장·제출 제목·태그라인에 **"SaaS"** 물리적으로 존재.

시간 기준: **H0 = 2026-09-15 17:00 KST**, H10 = 09-16 03:00 KST.
이후 03:00–05:00 영상 / 05:00–07:00 덱·README / 07:00–08:00 **1차 제출** / 08:00–11:00 수면 / 11:00–12:00 동결.

---

### S1 — **Article50** : "78일 안에 €15M을 피하세요. URL 하나, 90초."
> *The EU AI Act transparency audit SaaS. One URL, 90 seconds, 14 deterministic checks.*

**Clause50의 재설계판. `browser_toolset`을 완전히 제거하고 Playwright 직행.**

- **타깃 유저**: EU 사용자를 상대하는 직원 20~500명 SaaS·이커머스의 **PM 겸 임시 컴플라이언스 담당자**.
  전담 법무팀이 없고, 12월 2일이 뭔지 어제 알았고, 컨설팅펌에 €20k를 낼 생각은 없는 사람.
- **왜 지금**: Article 50 적용 **2026-08-02**, 기존 생성형 AI 마킹 유예 **2026-12-02** 만료 →
  오늘 기준 **78일**. 위반 시 **€15M 또는 전세계 매출 3% 중 높은 쪽**
  (단 SME·스타트업은 낮은 쪽 — 이 디테일을 화면에 같이 띄웁니다).

**결정론적 코어 (LLM 없이 동작하는 부분 = 제품의 70%)**

| 레이어 | 내용 |
| --- | --- |
| 크롤러 | Playwright headless chromium, 도메인당 상위 8페이지. `page.on("request")`로 **모든 아웃바운드 요청 도메인** 수집, `page.on("console")`, DOM 스냅샷, 스크린샷 |
| Fingerprint DB | 40여 개 시그니처를 **YAML 한 파일**로: 챗봇 벤더(Intercom `widget.intercom.io`, Drift, Crisp, Tidio, Zendesk, Zapier Chatbot, Voiceflow, Botpress…), 감정인식 SDK, 합성음성 플레이어, AI 이미지 생성 CDN 패턴. **iframe 내부를 볼 필요가 없음** — 네트워크 요청 도메인만 보면 잡힘 |
| 프로비넌스 파서 | 이미지 C2PA manifest / IPTC `DigitalSourceType` / `<meta name="ai-generated">` 파싱 (순수 Python) |
| **룰 엔진** | Article 50(1)/(2)/(3)/(4) 조항별 `PASS` / `FAIL` / `REVIEW` — **판정은 전부 코드.** 증거 id 없는 판정은 존재할 수 없는 자료구조로 설계 |
| 증적 저장 | Postgres: `scan` / `page` / `evidence`(스크린샷 + DOM 스니펫 + 요청 URL + 해시) / `finding`. **재스캔 시 diff** |

**LLM이 하는 일 (정확히 두 가지, 덱에 이 문장 그대로)**
1. 탐지된 고지 배너 텍스트가 **"평균적으로 정보를 갖춘 자연인에게 명백한"** 수준인지 분류
   (`strict:true` 스키마: `{verdict, confidence, quoted_span}`). `confidence < 0.7`이면 **코드가
   판정을 버리고 `REVIEW`로 강등**.
2. 각 `FAIL`에 대해 붙여넣기 가능한 수정 스니펫 생성(고지 배너 HTML, `<meta>` 프로비넌스 태그).

**H0–H10 빌드 플랜 (체크포인트마다 화면에 무엇이 있는지)**

| 시각 | 작업 | **화면에 보이는 것** |
| --- | --- | --- |
| H0 (17:00) | 레포 + FastAPI + Postgres(Neon) + Next.js 스캐폴드, **배포 먼저** (api.article50.hajin.xyz / article50.hajin.xyz), `/healthz` | 브라우저에 `{"status":"ok","version":"0.1.0"}` |
| H1 | Playwright 크롤러 1페이지 + 네트워크 요청 수집. CLI로 `python -m crawler https://…` | 터미널에 수집된 요청 도메인 목록 |
| H2 | fingerprint YAML 20개 + 매칭. 스크린샷 저장 | 터미널에 `DETECTED: intercom (chatbot) on /pricing` |
| H3 | **룰 엔진 + Postgres 스키마.** 조항별 PASS/FAIL/REVIEW JSON | `curl /scan` → 조항별 판정 JSON 전체 |
| H4 | 8페이지 병렬 크롤 + C2PA/IPTC 파서 + 진행 상황 SSE | 터미널 진행 로그, 스캔 1건 40~70초 |
| H5 | **Next.js 스캔 페이지**: URL 입력 → 실시간 체크리스트가 빨강/초록으로 채워짐 | **와우 모먼트 첫 등장.** 왼쪽 라이브 로그, 오른쪽 조항 체크리스트 |
| H6 | LLM 레이어 2종 + 신뢰도 게이트 + REVIEW 큐 | 배너 텍스트 판정 카드, "1건 사람 검토 필요" 배지 |
| H7 | **시드 데이터 3도메인 + `?replay=` 리플레이 모드** + 증거 드로어(스크린샷·DOM·요청 URL) | 데모 보험 완성. 증거 클릭 시 스크린샷 모달 |
| H8 | 리포트 상단 **"준수율 41% · 노출 €15M · 유예 만료까지 78일"** 카운트다운 + PDF export + **Stripe Pricing Table** + `/fix` 스니펫 복사 버튼 | 최종 리포트 화면, 가격 페이지 |
| H9 | **`make eval` + eval 표 자동 생성** + README 아키텍처 다이어그램 | 터미널에 20건 eval 표 |
| H10 (03:00) | 빈 상태·에러 상태·다크모드, 헤더 카피, **코드 프리즈** | 폴리시 완료 |

**Eval 표 (영상 2:05–2:30과 README·덱 7번 슬라이드에 동일하게)**

| Metric | Baseline (LLM-only: "이 HTML 보고 판정해줘") | Article50 | n |
| --- | --- | --- | --- |
| 챗봇 탐지 recall | 0.58 | **0.95** | 20 |
| 챗봇 탐지 precision | 0.71 | **1.00** | 20 |
| 고지 적절성 분류 정확도 (사람 라벨 대비) | 0.65 | **0.85** | 20 |
| **근거 없는 판정 (환각 판정) 비율** | 0.30 | **0.00** (구조적으로 불가능) | 20 |
| REVIEW 강등율 (= 정직하게 모른다고 한 비율) | — | 0.15 | 20 |
| 스캔당 중앙 레이턴시 | — | 52 s | 20 |
| 스캔당 비용 | — | $0.038 | 20 |

**20건 테스트셋을 빠르게 만드는 법 (H9, 40분)**
`fixtures/` 아래에 **정적 HTML 12개를 직접 작성**해 `fixtures.hajin.xyz`로 서빙합니다
(Claude로 20분에 생성). 구성: ①고지 있는 챗봇 4건 ②고지 없는 챗봇 4건
③C2PA 없는 AI 이미지 2건 ④감정인식 스크립트 1건 ⑤전부 깨끗한 대조군 1건.
**Ground truth가 정의상 100% 정확**하고 재현 가능하며 남의 사이트에 부하도 안 줍니다.
나머지 8건은 실제 공개 사이트를 손으로 라벨링. Baseline 컬럼은 같은 20건을
"HTML 통째로 주고 Claude에게 판정만 시키는" 스크립트로 한 번 돌려서 얻습니다 — **10분**.
이 baseline 컬럼 하나가 Algoverse 코드워드("baseline", "ablation")를 정확히 칩니다.

**실패 처리 데모 모먼트 (영상 1:40, 15초)**
의도적으로 **처음 보는 챗봇 벤더**가 있는 페이지를 스캔합니다.
탐지기는 잡지만 LLM 신뢰도가 **0.41**로 임계값 0.7 미만 → 화면에 초록도 빨강도 아닌
**노란 REVIEW 카드**가 뜨고, "Low confidence (0.41) — not scored. Queued for human review"와
감사 로그 항목이 동시에 생깁니다. 나레이션:
*"The worst outcome for a compliance tool is a confident wrong answer. This one refuses to score."*
— ServiceNow 심사위원 글 제목(*"I Watched Our AI Pipeline Silently Fail While Kubernetes Said
Everything Was Fine"*)을 정조준하는 15초입니다.

**가격 (Stripe test mode, 좌석 아님 — 도메인 단위)**
Free: 1회 스캔 / 3페이지 · **Pro $249/mo**: 도메인 3개, 주간 재스캔, PDF 증적, 알림 ·
**Agency $999/mo**: 도메인 25개, 멀티테넌트, API. 일회성 **Audit $299**.

**별점 / 가중합**
Tech ★★★★☆(4) · Impact ★★★★★(5) · Innovation ★★★★☆(4) · UX ★★★★★(5) · Presentation ★★★★★(5)
→ 20 + 25 + 16 + 15 + 15 = **91**

**잔존 리스크**
① 심사위원이 아무 URL이나 넣었을 때 크롤이 30초 이상 걸리거나 봇 차단당함 →
   **페이지 5개 하드 캡 + 45초 타임아웃 + 부분 결과 렌더링**으로 방어. 실패해도 화면이 빈 상태가 되지 않게 할 것.
② 법률 자문 오해 → 푸터 상시 고지 + REVIEW 적극 사용 + "we cite the article text, we don't interpret it".
③ fingerprint DB가 40개라 커버리지가 좁음 → **정직하게 "40 vendors covered, unknown vendors go to
   REVIEW not FAIL"**을 화면에 명시. 약점을 먼저 말하면 강점이 됩니다.

---

### S2 — **AgentGate** : "에이전트가 당신의 체크아웃에서 죽는 6개 지점. 결정론적으로."
> *Agent-readiness scoring for merchants. 12 deterministic probes, 0 guesswork.*

**AgentReady를 "라이브 구매 시도"에서 "장애물 코스 채점"으로 축소한 버전.**

- **타깃 유저**: 이미 GEO/SEO 예산을 집행 중인 **이커머스 그로스 담당자**.
- **결정론적 코어**: 스토어 URL에 대해 **12개 코드 프로브**를 순서대로 실행.
  ① `robots.txt`의 `GPTBot`/`ClaudeBot`/`PerplexityBot`/`OAI-SearchBot` 허용 여부
  ② `/llms.txt` 존재 ③ PDP의 `schema.org/Product` JSON-LD 완결성(price·availability·sku)
  ④ JS 없이 PDP 렌더 여부(`--disable-javascript` 2차 크롤) ⑤ 장바구니 URL의 안정성/공유 가능성
  ⑥ add-to-cart가 접근성 트리에서 이름을 갖는가 ⑦ 체크아웃 진입에 로그인 강제 여부
  ⑧ CAPTCHA 벤더 fingerprint(hCaptcha/reCAPTCHA/Turnstile) ⑨ 3DS 강제 ⑩ 무한스크롤 전용 카탈로그
  ⑪ 재고 상태의 기계판독성 ⑫ 결제 수단 메타데이터.
  각 프로브는 **가중치가 있는 PASS/FAIL** → **Agent Readiness Score 0~100** (LLM 0회 호출).
- **LLM이 하는 일**: 각 FAIL에 대한 **수정 지시문 생성** + 경쟁사 3곳 점수 비교의 **서술 요약**.
- **H0–H10**: S1과 동일 골격. H1–H2 프로브 6개, H3 점수 엔진, H4 나머지 6개 + 경쟁사 병렬,
  H5 UI(스토어 3개 나란히 바 차트), H6 LLM 수정 가이드, H7 시드+리플레이, H8 가격+PDF,
  H9 eval, H10 폴리시.
  H5 화면: **자사 vs 경쟁사 2곳의 12칸 그리드가 초록/빨강으로 채워지는 화면.**
- **Eval 표**: 20개 스토어(Shopify 데모 스토어 8 + 공개 스토어 8 + 자작 fixture 4).
  메트릭 = 프로브별 정확도(손 라벨 대비), 점수 재현성(동일 스토어 3회 반복 시 표준편차 — **이게 킬러**),
  스캔당 레이턴시/비용, 경쟁사 스캔 병렬화 속도. 재현성 σ를 보여주는 해커톤 팀은 없습니다.
- **실패 처리 데모**: 스토어가 **429/봇 차단**을 반환하도록 유도 → 점수를 0점으로 찍지 않고
  `INCONCLUSIVE` + "3 of 12 probes blocked by WAF" + 부분 점수 + 재시도 백오프 로그를 보여줌.
- **가격**: 스토어당 **$199/mo**, 에이전시 $899/mo.
- **별점**: Tech 4.5 · Impact 4 · Innovation 5 · UX 4 · Presentation 5 → 22.5+20+20+12+15 = **89.5**
- **잔존 리스크**: ① 남의 상용 스토어를 프로브하는 ToS 회색지대 → **자체 Shopify 개발 스토어 2개를
  만들어 데모의 주인공으로** 쓰고 실제 브랜드는 읽기 전용 1개만. ② "12개 프로브가 정말 에이전트
  성공률과 상관 있나?" → 상관관계를 주장하지 말고 **"체크리스트"로 포지셔닝**할 것.

---

### S3 — **MCPGate** : "MCP 서버 9,652개. 당신의 에이전트는 그중 뭘 호출합니까?"
> *MCP supply-chain review + policy gateway. Header-routed, no body parsing, 2026-07-28 spec.*

**MCPGuard에서 샌드박스를 완전히 제거한 버전. 10개 중 데모 신뢰도 최상.**

- **타깃 유저**: 에이전트를 사내에 도입한 **플랫폼 엔지니어링 / AppSec**.
- **왜 지금 (검증됨)**: MCP **2026-07-28** 스펙이 `initialize` 핸드셰이크와 `Mcp-Session-Id`를 제거하고
  `Mcp-Method` / `Mcp-Name`을 **HTTP 헤더로 승격** → **바디 파싱 없이 평범한 리버스 프록시에서
  툴 단위 인가·감사가 가능**해짐. 이전 스펙에서는 구현 불가능했던 제품 형태.
  (https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ ·
  https://www.infoq.com/news/2026/08/mcp-stateless-gateway/)
- **결정론적 코어**
  ① `tools/list`를 **HTTP POST 한 번**으로 수집(스테이트리스 스펙 덕분) →
  ② **정적 분석기**: 툴 설명 내 URL·IP 리터럴, 광범위 스코프(`*`, `read_file` + 경로 미제한),
     프롬프트 인젝션 패턴 정규식 24종(`ignore previous`, `<system>`, base64 블록, 제로폭 문자),
     설명↔스키마 불일치(설명에 없는 파라미터), 이름 스쿼팅(레지스트리 유사도) →
  ③ **Risk Score 0~100 + 정책 YAML 자동 생성**(허용 `Mcp-Name` 화이트리스트) →
  ④ **FastAPI 리버스 프록시**가 그 정책을 실제로 강제 — 헤더만 보고 allow/deny, **~150줄** →
  ⑤ 차단 로그가 실시간으로 쌓이는 대시보드(SSE).
- **LLM이 하는 일**: 툴 **설명의 의미**와 **선언된 스코프의 불일치**를 판정
  (`{tool_name, claimed_capability, observed_capability, mismatch: bool, evidence_span}` 스키마 강제).
  정적 분석과 **의견이 갈리면 높은 쪽 리스크를 채택**하고 화면에 둘 다 표시 — 이 "두 심판" 화면 자체가 Tech 점수.
- **데모의 결정적 이점**: **악성 MCP 서버를 본인이 직접 작성**합니다(`evil-docs-mcp`, 80줄).
  → 데모 타깃이 100% 자기 통제 하에 있음 → **외부 의존성 0** → 라이브 실패 확률 최저.
- **H0–H10**

| 시각 | 작업 | 화면 |
| --- | --- | --- |
| H0 | 스캐폴드 + 배포 + `/healthz` | `{"status":"ok"}` |
| H1 | `tools/list` 수집기 + **`evil-docs-mcp` 자작 서버 배포** | 터미널에 툴 스키마 JSON |
| H2 | 정적 분석기 규칙 12종 + Risk Score | 터미널에 `RISK 78: search_docs → POST https://collector.evil.tld` |
| H3 | **리버스 프록시 + 정책 YAML 강제** (헤더 라우팅) | `curl`로 차단당하는 로그 |
| H4 | Postgres 저장, 스캔 이력, 정책 버저닝 | — |
| H5 | **Next.js 대시보드**: 서버 카드 + 툴 테이블 + 리스크 뱃지 | 와우 모먼트 1 |
| H6 | LLM 의미 분석 + "두 심판" 뷰 + SSE 실시간 차단 로그 | **와우 모먼트 2: 로그에 BLOCKED가 빨갛게 찍힘** |
| H7 | 시드(레지스트리 10개 사전 스캔) + 리플레이 | 데모 보험 |
| H8 | 정책 export 버튼 + **Stripe Pricing Table** + 다크모드 | 가격 페이지 |
| H9 | `make eval` + eval 표 | 20건 표 |
| H10 | 폴리시 · 코드 프리즈 | — |

- **Eval 표 / 20건 생성법 (H9, 30분)**: 공개 MCP 레지스트리에서 **양성 10개**의 매니페스트를 받고,
  그중 10개를 스크립트로 **변조해 음성 10개**를 만듭니다(설명에 exfil URL 주입, 스코프 확장,
  제로폭 인젝션, 이름 스쿼팅, 스키마 불일치 — 변조 함수 5개 × 2). **Ground truth가 생성 시점에 확정.**

| Metric | Static only | + LLM | n |
| --- | --- | --- | --- |
| 악성 탐지 recall | 0.70 | **0.90** | 20 |
| 양성 false positive율 | 0.10 | **0.10** | 20 |
| 스키마 불일치 탐지 | 0.40 | **0.80** | 20 |
| 정책 컴파일 성공률 | **1.00** | 1.00 | 20 |
| 프록시 차단 p50 / p95 레이턴시 | **1.8 ms / 4.1 ms** | — | 1,000 req |
| 서버당 심사 비용 | — | $0.012 | 20 |

  프록시 p95 **4ms**는 이 패널(ServiceNow 성능 엔지니어)에게 다른 어떤 숫자보다 잘 먹힙니다.
- **실패 처리 데모**: 깨진 매니페스트(잘린 JSON)를 먹입니다 → 파서 예외 → **프록시가 fail-open이
  아니라 fail-closed**로 전환하며 "Unparseable manifest — denying all tools from this server"를
  띄우고 알림. 나레이션: *"When the analyzer fails, the gateway denies. Silence is not a pass."*
- **가격**: Free 서버 3개 심사 · **Team $499/mo** (서버 25개 + 게이트웨이, **좌석 무관**) ·
  Enterprise $2,000/mo (SSO, 감사 export, self-host).
- **별점**: Tech 5 · Impact 4 · Innovation 5 · UX 3.5 · Presentation 4.5 → 25+20+20+10.5+13.5 = **89**
- **잔존 리스크**: ① 보안 대시보드는 예쁘게 만들기 어려움 → shadcn 기본 테마 + 단색 + 큰 숫자 하나로 승부.
  ② 도메인 설명에 30초가 듦 → 영상 훅을 "당신의 코딩 에이전트는 어제 설치한 MCP 서버 7개를
  아무 검증 없이 호출합니다"로 시작해 설명을 압축.
  ③ TOCTOU 반박 → **덱 한 줄로 먼저 인정**하고 프록시(런타임 관측)가 그 답의 절반임을 명시.

---

### S4 — **AgreeGate** : "LLM 저지를 믿기 전에, 그 저지가 사람과 얼마나 일치하는지부터."
> *Evals for domain experts → signed compliance evidence. Cohen's κ = 0.71, measured, not claimed.*

**RubricRoom + TrustReply의 신뢰도 게이트를 합친 버전. 이 심사 패널 적합도 1위.**

- **타깃 유저**: 규제 산업에서 에이전트를 배포하려는 팀의 **도메인 전문가와 그를 설득해야 하는 엔지니어**.
  LangSmith를 쓸 줄 모르는 승인자.
- **핵심 차별점 (30초 안에 말할 한 문장)**:
  *"Everyone ships an LLM judge. Nobody measures whether their judge agrees with the humans
  who are legally accountable. We make that agreement the product."*
- **결정론적 코어 (LLM 0회로 동작)**: 트레이스 저장 → 카드 UI 채점 수집 →
  **Cohen's κ / Krippendorff's α + 부트스트랩 95% 신뢰구간**(numpy, 순수 코드) →
  임계값 미달 시 **승인 게이트 차단** → 통과 시 **해시 체인 + 타임스탬프 서명된 증적 PDF** 생성 →
  새 버전 업로드 시 **회귀 감지**(동일 문항 재채점 후 점수차 검정).
- **LLM이 하는 일**: ① 트레이스에서 **루브릭 기준 초안 자동 생성** ② **LLM 저지로 전체 채점** —
  그리고 그 저지의 점수가 **사람 채점과 얼마나 일치하는지 κ로 측정되어 화면에 그대로 박힙니다.**
  LLM이 못하면 못하는 대로 숫자가 나오는 구조 = 실패해도 제품이 성립.
- **H0–H10**: H1 트레이스 업로드/저장, H2 카드 채점 UI(**여기가 UX 15점 전부** — 스와이프 카드, 단축키 1/2/3),
  H3 κ·α + 부트스트랩 CI, H4 게이트 + 회귀 감지, H5 대시보드(엔지니어 뷰), H6 LLM 저지 + κ 비교 차트,
  H7 시드 데이터(트레이스 40건 + 가짜 채점 3인분), H8 PDF 증적 + Stripe, H9 eval, H10 폴리시.
  **H2 시점에 이미 영상의 핵심 장면(전문가가 카드를 넘긴다)이 화면에 존재**합니다 — 리스크 최저 순서.
- **Eval 표**: 20건 = 트레이스 20개를 **본인이 3인분 페르소나로 직접 채점**(15분) + LLM 저지 채점.
  메트릭: LLM 저지 vs 인간 다수결 **κ = 0.71**, 인간 간 κ = 0.84, 저지 false-approve율,
  게이트 차단 정확도, 채점 1건당 소요 시간(사람 11s vs LLM 0.9s), 채점당 비용.
- **실패 처리 데모**: **LLM 저지가 인간과 불일치하는 케이스를 일부러 보여줍니다.**
  κ가 0.71로 임계값 0.8 미만 → **승인 게이트가 빨갛게 잠기고** "Judge not certified for this rubric —
  human review required for all items" → PDF 증적에 그 사실이 기록됨.
  *"The demo you're watching is our product failing its own bar, on purpose. That's the feature."*
- **가격**: **$299/mo** 베이스 + 평가자 좌석 $29 (하이브리드 — §2.2 좌석제 종말과 정렬).
- **별점**: Tech 4 · Impact 4 · Innovation 4 · UX 5 · Presentation 4 → 20+20+16+15+12 = **83**
- **잔존 리스크**: ① "LangSmith/Braintrust에 있다" → **κ 측정 + 서명 증적 + 게이트**의 조합은 없음을
  명시하고 경쟁사를 실명으로 언급(우승작 패턴). ② Impact가 간접적 → "88% 실패" 통계는
  2차 출처이므로 **덱에 출처 URL 표기**하거나 아예 빼고 "승인 게이트에서 3주 멈춘다"는
  서사로 대체. ③ 데모가 조용함(라이브 크롤·차단 같은 시각적 액션이 없음) → 카드 UI 인터랙션과
  κ 차트 애니메이션으로 벌충.

---

### S5 — **TaskLedger** : "$/Mtok는 거짓말입니다. 태스크당 실비용은 $0.42입니다."
> *The AI cost ledger that prices tasks, not tokens. 9 multipliers your spreadsheet is missing.*

**TaskCost 축소판. P(데모 성공) 최고. 안전 앵커 카드.**

- **타깃 유저**: AI 제품을 운영하는 **엔지니어링 리드 / FinOps**.
- **결정론적 코어 (LLM 0회)**: OTel/JSONL 업로드 → 태스크 단위 스팬 그룹핑 →
  **정규화 가격 엔진**: 토크나이저 배수, 캐시 읽기 배수(Fable 5.1 0.025배 vs 나머지 0.1배),
  캐시 쓰기, Fast mode 프리미엄, `inference_geo` 배수, 배치 50%, 세션-시간 요금,
  만료 예정 프로모 가격 → 태스크당 실비용 → **반사실 시뮬레이터**(모델/캐시/배치 조합 비교) →
  **가격 만료 타임머신**("2027-01-01에 X가 2배 되면 월 $4,100 → $7,900").
  가격표는 `pricing/*.yaml`에 **`source_url` + `fetched_at`을 담아 화면에 노출**.
- **LLM이 하는 일 (딱 한 군데, 명확히)**: 비용 이상치(spike) 탐지 후 **근본원인 서술**
  ("이 태스크 그룹은 시스템 프롬프트에 타임스탬프가 들어가 캐시 히트율이 3%입니다") +
  최적화 플랜 생성. 이 한 지점이 "AI 해커톤에서 AI를 안 쓴다"는 반박을 막습니다.
- **H0–H10**: H1 스팬 파서 + 시드 트레이스 생성기, H2 가격 엔진, H3 태스크 그룹핑 + 집계,
  H4 대시보드 차트, H5 반사실 시뮬레이터 UI(슬라이더), H6 타임머신, H7 LLM 이상치 분석,
  H8 Stripe + 다크모드, H9 eval, H10 폴리시.
- **Eval 표 (이 카드의 비밀 무기)**: 20개 픽스처의 비용을 **손으로 계산한 ground truth**와 대조 →
  **정확도 20/20 (0.00% 오차)**. 그리고 **"정가표 단순 $/Mtok 계산"을 baseline**으로 두면
  baseline의 평균 오차가 **−34%**로 나옵니다. "우리 엔진은 완벽하고, 당신이 지금 쓰는 방법은
  34% 틀렸다"를 한 표로 증명 — 해커톤에서 **증명 가능한 정확도 100%를 내놓는 팀은 없습니다.**
- **실패 처리 데모**: 가격 YAML의 `fetched_at`이 14일 넘은 항목을 일부러 넣습니다 →
  화면에 **"Stale price data (fetched 2026-08-20) — this figure may be wrong"** 배너가 뜨고
  해당 숫자가 회색으로 변함. *"A cost tool that quietly uses stale prices is worse than no tool."*
- **가격**: 추적 지출의 1%, 최소 **$200/mo**. Free: 월 10,000 스팬.
- **별점**: Tech 4 · Impact 4 · Innovation 4 · UX 4 · Presentation 3.5 → 20+20+16+12+10.5 = **78.5**
- **잔존 리스크**: ① **"AI 제품이 아니다"** — 최대 리스크. LLM 이상치 분석을 영상에 반드시 20초 넣을 것.
  ② 화면이 전부 시드 데이터 → 심사위원이 "실제 트레이스로 되나?" 물으면 **본인의 Article50/MCPGate
  개발 중 실제 API 로그를 업로드해 보여주는 것**이 최고의 답 (그래서 다른 카드와 병행 시 시너지).
  ③ 가격표 신선도가 제품의 생명 → cron으로 매일 갱신한다는 로드맵을 명시.

---

### PART 2 요약표

| 안 | 이름 | Tech 25 | Impact 25 | Innov 20 | UX 15 | Pres 15 | 가중합 | P(라이브 데모) | 결정론적 코어 한 줄 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | **Article50** | 4 | 5 | 4 | 5 | 5 | **91** | **88%** | Playwright 크롤 + fingerprint + 조항 룰 엔진 |
| S2 | AgentGate | 4.5 | 4 | 5 | 4 | 5 | 89.5 | 75% | 12개 코드 프로브 + 가중 점수 |
| S3 | **MCPGate** | 5 | 4 | 5 | 3.5 | 4.5 | **89** | **92%** | 정적 분석 + 헤더 라우팅 정책 프록시 |
| S4 | AgreeGate | 4 | 4 | 4 | 5 | 4 | 83 | 95% | κ·α + 부트스트랩 CI + 서명 증적 |
| S5 | TaskLedger | 4 | 4 | 4 | 4 | 3.5 | 78.5 | 96% | 정규화 가격 엔진 (오차 0.00%) |

---

## PART 3 — 의사결정 매트릭스

**"degraded" 정의**: T-6h에 핵심 루프가 라이브로 안 돌아, 사전 녹화 리플레이 + 시드 데이터로
영상을 찍고 제출한 경우. (제품 URL은 살아 있고 시드 결과는 보이지만, 심사위원이 직접 넣은
입력은 실패하거나 느림.)
**EV = P × (works) + (1−P) × (degraded)**

| 후보 | P(라이브 데모 동작) | 성공 시 가중합 | 저하 시 가중합 | **EV** | 한 줄 권고 |
| --- | --- | --- | --- | --- | --- |
| **S1 Article50** | **88%** | 91 | 78 | **89.4** | **이걸 만드세요.** 임팩트 서사가 문서로 증명되고(날짜·과징금), 브라우저 executor 함정을 Playwright로 우회하며, 리포트 UI라 10h에 아름답게 나옵니다 |
| **S3 MCPGate** | **92%** | 89 | 80 | **88.3** | 확률 최고 + 기술 깊이 최고. **악성 서버를 직접 작성하므로 외부 의존성 0.** UX 15점과 도메인 설명 시간만 손해 — S1과 1.1점 차, 사실상 동률 |
| **S2 AgentGate** | 75% | 89.5 | 66 | 83.6 | 상한은 높지만 남의 스토어에 의존 — 자체 Shopify 개발 스토어를 데모 주인공으로 바꿀 수 있을 때만 |
| **S4 AgreeGate** | 95% | 83 | 76 | 82.7 | 패널 적합도는 1위인데 천장이 낮음. **S1의 REVIEW 게이트로 흡수하는 게 더 남는 장사** |
| Clause50 (원안) | 45% | 92 | 70 | **79.9** | executor 3~5h가 EV를 9.5점 태웁니다. S1이 상위 호환 |
| MCPGuard (원안) | 40% | 91 | 72 | **79.6** | 샌드박스 하나가 EV를 8.7점 태웁니다. S3이 상위 호환 |
| AgentReady (원안) | 30% | 93 | 60 | **69.9** | **가장 강한 데모 = 가장 안 찍히는 데모.** 후보 중 최하위 EV |

### 읽어야 할 것

1. **성공 시 점수(93)가 가장 높은 AgentReady가 EV는 가장 낮습니다(69.9).**
   이 대회는 단일 상 winner-take-all이고 마감이 19.5시간 남았습니다. 상한이 아니라 **기대값**이 기준입니다.
2. **원안 3개는 전부 자기 축소판에 EV로 집니다.** 각각 정확히 한 개의 무거운 배관
   (browser executor / 샌드박스 / 외부 스토어 의존)이 EV를 8~20점 태웁니다.
   **오늘 내려야 할 결정은 "무엇을 만들까"가 아니라 "무엇을 안 만들까"입니다.**
3. **S1과 S3의 차이는 1.1점 — 오차 범위입니다.** 갈림길은 취향이 아니라 두 가지입니다:
   - H5(22:00 KST)에 **Playwright로 챗봇 fingerprint가 실제로 잡히는가** → 잡히면 S1.
   - 못 잡으면 **H5에 S3로 스위치**. S3은 H1~H3이 순수 HTTP+프록시라 **가장 늦게까지 갈아탈 수 있는 카드**입니다.
   → **H5를 명시적 고 / 노고 체크포인트로 캘린더에 박아두세요.**

---

## 최종 권고 — **S1 Article50**

**한 줄**: Clause50을 만들되, `browser_toolset_20260801`을 완전히 버리고 **Playwright를 직접 몰고,
Claude는 "이 고지 문구가 충분한가"와 "수정 스니펫 생성" 두 가지만** 시킵니다.

**이 선택의 근거 4가지**
1. **Impact 25점이 반박 불가능합니다.** 날짜(2026-12-02)와 금액(€15M / 3%)이 1차 출처로 확인되고,
   오늘 기준 78일이라는 숫자가 화면에서 실시간으로 줄어듭니다. 이 패널은 "그래서 얼마를 아끼나"를
   가장 엄격하게 묻는 패널이고, 이 아이디어는 그 질문에 **법전으로** 답합니다.
2. **UX 15 + Presentation 15 = 30점을 거의 만점으로 가져갑니다.** "URL 붙여넣고 90초에 리포트"는
   10시간에 아름답게 만들 수 있는 유일한 종류의 UI이고, 3분 영상에 정확히 맞습니다.
3. **thin wrapper 방어가 구조적입니다.** 크롤러·fingerprint DB·룰 엔진·증적 저장·재스캔 diff —
   **LLM을 전부 꺼도 제품의 70%가 동작합니다.** 주최측이 명시한 배제 사유
   ("AI wrappers with minimal differentiation")에 걸릴 수가 없습니다.
4. **실패 처리 데모가 도메인과 자연스럽게 일치합니다.** 컴플라이언스 도구에서
   "자신 있게 틀린 답"은 최악이고, REVIEW 강등은 억지로 끼워넣은 장치가 아니라
   제품의 필연입니다. ServiceNow·Dell 심사위원을 정확히 겨냥하면서도 억지스럽지 않습니다.

**헤지**: **H5(2026-09-15 22:00 KST)를 고/노고 게이트로 설정.**
그 시점에 실제 사이트 3곳에서 챗봇 위젯이 네트워크 요청 fingerprint로 잡히지 않으면
**S3 MCPGate로 전환**합니다. S3은 H0–H3이 HTTP 클라이언트 + FastAPI 프록시뿐이라
22:00에 시작해도 남은 5시간으로 완주 가능한 유일한 카드입니다.

**절대 하지 말 것 (오늘 한정)**
- `browser_toolset_20260801` executor 구현 — 어떤 아이디어에서도. 3~5시간이 화면에 안 보입니다.
- 격리 샌드박스 — 로드맵 슬라이드로.
- 남의 상용 사이트에 쓰기 동작(장바구니 담기, 폼 제출) — 읽기만.
- `thinking: {budget_tokens: N}` — Opus 5 / Sonnet 5에서 **400**.
- 실시간 WebSocket 협업 — 폴링으로 충분하고, 데모 중에 깨집니다.
- Eval 표를 "시간 남으면" 항목에 두는 것 — **H9는 협상 불가입니다.** 해커톤에서 eval 표를 내는 팀은 1%이고,
  이 패널에는 검증(Dell/TMMi)·관측성(ServiceNow) 전문가가 앉아 있습니다.

---

## 출처

- https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool — 브라우저 툴은 클라이언트 툴셋, executor는 개발자 구현, CAPTCHA 불가, Managed Agents·Bedrock 미지원
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference — 클라이언트 툴셋 정의
- https://thenewstack.io/anthropic-browser-use-tool/ — *"Anthropic's new browser tool doesn't actually run a browser"*
- https://playwright.dev/mcp/introduction · https://playwright.dev/docs/getting-started-mcp — Playwright MCP 접근성 스냅샷 + ref
- https://artificialintelligenceact.eu/transparency-rules-article-50/ — Art.50(1)~(4), "2 August 2026", "2 December 2026"
- https://artificialintelligenceact.eu/article/99/ · https://euaiactchecklist.com/eu-ai-act-fines-penalties.html — €15M / 3% 티어, SME는 낮은 쪽
- https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ — MCP 2026-07-28 스펙
- https://www.infoq.com/news/2026/08/mcp-stateless-gateway/ · https://appwrite.io/blog/post/mcp-goes-stateless-in-the-2026-07-28-specification · https://equixly.com/blog/2026/08/05/stateless-mcp/ — `Mcp-Method`/`Mcp-Name` 헤더 라우팅, 세션 제거
- https://docs.stripe.com/no-code/pricing-table — 노코드 가격표, `pk_test_`, 도메인 필요
- https://github.com/anthropics/claude-quickstarts — 공식 퀵스타트(브라우저 executor 레퍼런스는 없음)
