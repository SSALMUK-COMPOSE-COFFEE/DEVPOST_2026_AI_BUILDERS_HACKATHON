# 05. 제출작 갤러리와 경쟁 구도

조사 시각: 2026-09-15 21:20 KST

---

## 1. 공식 갤러리: 미공개 (확정)

두 URL 모두 동일한 문구만 반환합니다. WebFetch와 헤드리스 Chromium 양쪽으로 확인했습니다.

- https://ai-builders-hackathon-2026.devpost.com/project-gallery
- https://ai-builders-hackathon-2026.devpost.com/submissions

> `The hackathon managers haven't published this gallery yet, but hang tight!`

참가자 명단도 막혀 있습니다.

> `Please log in to browse this hackathon's participants.`

> ### 마감 전 실제 경쟁작을 직접 조회하는 것은 불가능합니다.
> 이는 양방향입니다. 나도 남을 못 보지만 **남도 나를 못 봅니다.** 아이디어 선점 리스크가 없고, 마지막 순간의 모방 리스크도 없습니다.

---

## 2. 경쟁 규모 추정

| 지표 | 값 | 확도 |
| --- | --- | --- |
| 등록 참가자 | **3,449명** (2026-09-15 21:20 KST) | 🟢 실측 |
| Discord 멤버 | 약 2,600명 | 🟢 실측 |
| 제출작 수 | **170 ~ 520건** | 🔴 **미확인 추정** |

추정 근거: 대형 온라인 해커톤의 등록 대비 제출 전환율 5~15%. Discord 활동 멤버가 등록의 75%라는 점은 이 대회의 참여도가 평균보다 높다는 신호이므로, **실제로는 300건 이상**일 가능성이 있습니다.

### 현금상 관점의 경쟁 계산

| 상 | 슬롯 | 300건 가정 시 확률 |
| --- | --- | --- |
| Best SaaS Product ($4,000 현금) | 1 | **0.33%** |
| NexFellow 3종 (구독권) | 3 | 1.0% |
| Tin 크레딧 ($299) | 100 | 심사 무관, **선착순** |

> 현금상은 1등 독식입니다. **상금 기대값으로는 합리적이지 않은 대회**이며, 실질 수익은 포트폴리오 자산, 전원 지급 참가 증서, 그리고 선착순 Tin 크레딧입니다. 이 인식을 가지고 시간을 배분하십시오. 즉 **완벽을 추구하다 미제출하는 것이 최악**입니다.

---

## 3. 대체 표본으로 읽은 테마 밀도

공식 갤러리가 막혔으므로 두 경로로 우회했습니다.

### 경로 A: Devpost 전역 검색 (오늘 실측, 태그라인 70+건 정독)

`https://devpost.com/software/search?query=ai+builders+hackathon` 을 헤드리스 브라우저로 3페이지(1~72위, 총 517건 중) 수집했습니다. 정렬 기본값이 관련도이며 최근 제출물이 다수 포함됩니다.

읽은 태그라인에서 즉시 드러난 밀집 패턴:

| 클러스터 | 표본 내 사례 |
| --- | --- |
| **WebMCP / 에이전트 네이티브 협업 UI** 🔴 극포화 | Relays, NodeCraft, HowToPC, FreeSpirits Real Estate WebMCP, Redactly, Full Loop, Stacks |
| **에이전트 거버넌스 · 승인 게이트 · 감사 추적** 🔴 극포화 | ROSIE, Greenroom, Fleetwright, Redactly, Cherry, IFF Sentinel |
| **토큰 비용 최적화 · 라우팅** 🟠 포화 | LeanMind AI, TokenC 계열 |
| **창업자/빌더 지원 도구** 🟠 포화 | Foundry, PitchPatch, Forze IDE, ShipCat AI, VISION(3건 중복), Grant Scout, Opportunity Hunter, mida, Signal-Scout, HackMate AI |
| **영상/미디어 편집 에이전트** 🟡 중간 | EditOS(3건 중복), CutProof, Glance |
| **채용 · 매칭** 🟡 중간 | TruMatch(**9건 중복 제출**), Real Passion ProjectMatch, Relays |
| **개발자 디버깅 · PR 에이전트** 🟡 중간 | RAZE Debug Mentor, PARS-Agent, Cherry |
| **접근성 · 케어** 🟡 중간 | ReadEasy, Yadira Calls, Onramp, Recall, Planterra |
| **음성 · 통화** 🟢 얕음 | Akira, Sundials, Yadira Calls |

관찰 3가지:

1. **`human in the loop` / `autonomous` / `agent-native` 라는 단어가 태그라인에 범람합니다.** 이 단어들은 이제 차별화 신호가 아니라 배경 소음입니다. 본인의 태그라인에서 이 표현들을 전부 빼십시오.
2. **중복 제출이 극심합니다.** TruMatch 9건, VISION 3건, EditOS 3건. 심사위원 피로도가 높다는 뜻이고, 첫 문장에서 구분되지 않으면 즉시 스킵됩니다.
3. **숫자가 들어간 태그라인이 압도적으로 적습니다.** 70건 중 정량 수치가 있는 것은 Sundials(`leads called within 5 mins are 21× more likely to qualify`) 정도입니다. **숫자 하나만 넣어도 상위 5% 안에 듭니다.**

### 경로 B: 동시기 대형 AI 해커톤 갤러리 프록시 (약 310건)

같은 시즌·같은 인재풀의 공개 갤러리(UC Berkeley AI Hackathon 2026, 400건 중 약 310건 수집)를 프록시로 사용한 선행 조사가 있습니다. 클러스터 비중은 다음과 같습니다.

| # | 클러스터 | 비중 | 포화도 |
| --- | --- | --- | --- |
| 1 | 에이전트 인프라 · 관측 · 메모리 · 컨텍스트 압축 | ~13% | 🔴 극포화 |
| 2 | 로보틱스 · 피지컬 AI | ~12% | 🟠 (솔로 10h 불가) |
| 3 | 헬스케어 · 임상 | ~11% | 🔴 극포화 |
| 4 | 교육 · 튜터 | ~9% | 🔴 극포화 |
| 5 | 재난 · 응급 · 911 | ~8% | 🔴 극포화 |
| 6 | 소비자 재미 · 게임 | ~8% | 🟡 (SaaS 트랙과 무관) |
| 7 | 접근성 | ~7% | 🟠 |
| 8 | AI 보안 · 레드팀 | ~6% | 🟠 단 기술 점수 높음 |
| 9 | 개발자 도구 · QA | ~6% | 🟠 |
| 10 | 시민 인프라 · 정부 | ~6% | 🟡 |
| 11 | 연구 에이전트 · 팩트체크 | ~5% | 🟡 |
| 12 | 고령자 · 스캠 방지 | ~4% | 🟡 |
| 13 | 커머스 · 마케팅 | ~4% | 🟢 |
| 14 | 핀테크 | ~3% | 🟢 |
| 15 | 농업 · 환경 | ~3% | 🟢 |

> ⚠️ 프록시의 한계: Berkeley 쪽은 하드웨어 스폰서 비중이 커서 로보틱스가 과대표집되어 있습니다. 반대로 본 대회는 `Best SaaS Product`가 유일 현금상이므로 **B2B SaaS 비중이 더 높을 것**으로 보정해 읽어야 합니다.

### 좋아요가 몰린 프로젝트의 공통점

| 프로젝트 | ❤ | 태그라인 특성 |
| --- | --- | --- |
| Quad | 38 | 인프라 포지셔닝 |
| FlowProof | 16 | 구체적 동작 서술 |
| Rem | 15 | 즉시 이해되는 시각적 결과 |
| Mimic | 11 | **`$1.55 → $0.06 per run`** |
| Promptetheus | 7 | `trace runs, catch silent failures, replay the bad step` |
| BrowserDelta | 5 | **`cuts browser-agent context by ~78%`** |

→ **교훈: before → after 숫자를 태그라인에 박아라. "누구를 돕는다"보다 "무엇을 몇 % 줄인다"가 강하다.**

---

## 4. 비어 있는 니치 (가장 중요한 발견)

프록시 310건과 오늘 읽은 70건을 합쳐 **거의 0건**이었던 영역입니다. 그리고 이 영역들이 실제 B2B SaaS 시장에서 돈이 가장 많이 도는 곳과 정확히 겹칩니다.

| 공백 영역 | 표본 내 건수 | 왜 비어 있나 | 왜 `Best SaaS`에 유리한가 |
| --- | --- | --- | --- |
| **뮤테이션 테스팅 · 테스트 품질 게이트** | **0건** | 지루하고 개념이 덜 알려짐 | 심사위원 Peri(TMMi America, QA 성숙도 이사회)와 1:1 정렬 |
| **법무 · 계약서 리뷰** | 0건 | 학생에게 낯선 도메인 | 명백한 유료 시장 |
| **컴플라이언스 · 감사 증적** | 0건 | 재미없어 보임 | 반복 매출의 교과서. "SaaS"로 즉시 읽힘 |
| **고객지원 티켓 디플렉션** | **0건** | "너무 뻔하다"고 다들 회피 | 역설적 기회 |
| **조달 · 벤더 보안설문 자동화** | 0건 | 도메인 인지 부족 | 자동화 적합도 최상 |
| **다국어 현지화 · i18n 운영** | 0건 | (없음) | 한국 개발자의 구조적 강점 |
| **프로덕트 애널리틱스 · 실험 설계** | 0건 | (없음) | PM 심사위원 7명과 정렬 |
| **AI 비용 거버넌스 · FinOps** | 1건 | (없음) | 2026년 CFO 최우선 관심사 |
| **세일즈 RevOps · CRM 위생** | 1건 | 학생이 겪어본 적 없는 고통 | 가장 명확한 ROI 스토리 |
| **HR · 온보딩 · 성과관리** | 1건 | (없음) | 모든 회사가 삼 |

### 전략 결론

> **포화 구역(에이전트 인프라 / WebMCP 데모 / 헬스 / 교육 / 재난 / 창업자 도구)을 피하고, "지루하지만 돈이 되는 백오피스 B2B" 중 하나를 골라 완성도 높은 SaaS 껍데기(게스트 모드, 로그인, 요금제, 대시보드)를 씌우는 것이 최적 전략입니다.**
>
> 단 Innovation 20%를 방어하려면 **기술적 훅 하나**를 반드시 심어야 합니다. 결정론적 검증 루프, 자체 채점 메커니즘, 증적 그래프 같은 "LLM 호출 한 번이 아님"을 증명하는 장치입니다.

---

## 5. 우리의 구조적 우위 3가지

| 우위 | 왜 희소한가 |
| --- | --- |
| **상시 가동 서버 + 와일드카드 TLS** | 대다수 참가자는 무료 티어(Vercel/Render)를 쓰고, 콜드스타트나 슬립으로 **심사 5일 중 일부 시점에 죽습니다.** 심사위원이 눌렀을 때 살아 있는 것만으로 상위권입니다 |
| **LLM 에이전트 백엔드 실무 경험** | 표본의 대다수가 프롬프트 래핑 수준입니다. 주최측이 명시적으로 배제한 `AI wrappers with minimal differentiation` 이 경쟁작의 다수라는 뜻 |
| **재학생 + 개인 참가** | 자격 요건 4개를 전부 깔끔히 충족. 위젯의 `Students only`로 이탈한 비학생 경쟁자가 존재할 가능성 |

---

## 출처

- https://ai-builders-hackathon-2026.devpost.com/project-gallery
- https://ai-builders-hackathon-2026.devpost.com/submissions
- https://ai-builders-hackathon-2026.devpost.com/participants
- https://devpost.com/software/search?query=ai+builders+hackathon (1~3페이지, 2026-09-15 수집)
- https://ai-hackathon-2026.devpost.com/project-gallery (프록시 표본)
