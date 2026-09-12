# AI Builders Hackathon 2026 리서치 종합 (2026-09-15 크롤링)

마감: **2026-09-15 23:00 EDT = 2026-09-16 12:00 KST**. 심사 9/16~9/20 EDT, 발표 9/25 09:00 EDT.

## 문서 목록

| 파일 | 내용 | 분량 |
| --- | --- | --- |
| [01_official_devpost.md](01_official_devpost.md) | 공식 규칙·제출물·심사기준 원문, 공지 9건·포럼 10건 전문, 심사위원 20명 명단, 규정 공백 | 644줄 |
| [02_organizers_sponsors_judges.md](02_organizers_sponsors_judges.md) | 주최 OSC, 스폰서 4곳, 심사위원 배경 분석, 취향 맞춤 전략 | 377줄 |
| [03_past_winners_analysis.md](03_past_winners_analysis.md) | 유사 온라인 AI/SaaS 대회 우승작 38건 vs 비우승작 8건 정량 비교, 우승 패턴 체크리스트 | 428줄 |
| [04_submission_playbook.md](04_submission_playbook.md) | Devpost 규정, 영상·스토리 템플릿, T-24h~T-0 체크리스트, 영상 대본 스켈레톤 | 824줄 |
| [05_competition_and_idea_landscape.md](05_competition_and_idea_landscape.md) | 경쟁작 프록시 310건 클러스터링, 빈 니치, 2026-08~09 시장 트렌드, 아이디어 10선 순위 | 619줄 |
| [06_rapid_build_toolkit.md](06_rapid_build_toolkit.md) | 배포 스택 무료 한도, Claude API 최신 코드, 템플릿 10개, Linux 영상 파이프라인, 24h 빌드 순서 | 1457줄 |

## 기존 summary.md에서 틀렸던 전제 (전부 정정됨)

| 항목 | 이전 summary | 실제 (Devpost 확인) |
| --- | --- | --- |
| 주최 | AI Builders Club | **Open Source Connect (OSC)**, osconnect.org |
| 스폰서 | NexFellow, Tin Computer | **NexFellow, Algoverse, Tin Computer, Sylus AI** |
| 심사 기준 | 기술 30 / PMF 30 / UX 20 / 독창성 20 | **Technical Implementation 25 / Problem Solving & Impact 25 / Innovation & Creativity 20 / UX & Design 15 / Presentation & Demo 15** (+ rules 페이지에 Scalability and feasibility 별도 언급) |
| 제출물 | 영상 + GitHub | **5종: 제출폼 + 동작하는 제품 + 공개 GitHub(README·셋업 가이드) + 데모 영상 ≤5분(AI 역할 명시) + 슬라이드 ≤10장(8개 지정 섹션)** |
| Tin Computer | 개발환경 크레딧 | **코딩 에이전트용 오픈소스 그로스 마케팅 MCP 서버.** 크레딧은 선착순 100팀, 수상과 무관 |
| 심사위원 | 미상 | **20명. 대기업 엔지니어 7~8명 + B2B SaaS PM 7명 + QA·관측성·보안 전문가.** VC·인플루언서 0명 |
| 참가 자격 | 대학생 | 메인 페이지 "Students only"는 주최측(Deependra Gaur)이 포럼에서 **표시 오류**라고 답변. 창업자·개발자 모두 가능 |
| 현금 상금 | 여러 개 | **Best SaaS Product $4,000 단 1개.** 나머지는 크레딧·구독권 |

## 6개 문서를 관통하는 결론 10가지

1. **현금 상은 하나뿐이다.** 제목·태그라인·덱 첫 장에 "SaaS"를 명시하고, Stripe 테스트 모드라도 결제 화면과 가격 티어 페이지를 만든다. 우승작 분석에서 Stripe 유무가 prototype과 business를 가른다.
2. **심사위원은 PM과 대기업 엔지니어다.** 슬라이드 Problem / Target Users / Impact 3장에 가장 공을 들이고, 아키텍처 슬라이드에 확장성·성능·보안·테스트를 한 줄씩 넣는다.
3. **주최측 배제 문구 2개**: "pitch decks, concept videos"와 "AI wrappers with minimal differentiation". 영상에 반드시 라이브 시연 화면이 들어가야 하고, 차별화 지점을 30초 안에 말한다. 훅으로 주최 카피 "The world doesn't need another AI demo"를 인용한다.
4. **영상은 2분 45초 목표.** 우승작 중앙값 174초. 5분 초과는 실격 리스크. 구조 = 훅 20초 → 문제 25초 → 라이브 데모 90초 → 아키텍처 30초 → 타깃·과금·URL 15초. YouTube는 Public/Unlisted + "Not for Kids", 처리 시간 때문에 미리 업로드.
5. **마감 후 수정은 심사에 반영되지 않는다.** T-4h(09/16 08:00 KST)에 1차 제출을 끝내고 Submitted 배지를 확인한다.
6. **이 심사진 한정 최대 차별화 = Eval 표 + 실패 처리 데모.** 자체 테스트셋 20~50건, 태스크 성공률·툴 사용 정확도·비용·레이턴시·환각률을 표로 README와 영상에 넣고, 일부러 모델 실패를 보여주고 감지·에스컬레이션을 시연한다. 심사위원 중 ServiceNow 관측성 엔지니어, Dell 검증 플레이북 저자, MS grounding 인프라, IBM Agentic AI SA가 있다.
7. **LLM 권한 제한을 설계로 명시한다.** "reviewer, not an author", confirm-before-act, human-in-the-loop 승인 게이트 + 롤백. 이것이 wrapper가 아니라는 증명이다.
8. **비용·레이턴시 숫자를 3개 이상 박는다.** 우승작은 예외 없이 태그라인이나 본문에 숫자가 있다.
9. **초니치 타깃 + 명명된 경쟁사 1문장.** "Operating System", "unifies every channel" 같은 플랫폼 선언은 전부 비우승 쪽이었다. 빈 니치는 법무·계약, 컴플라이언스·감사, 고객지원, 조달·벤더심사, 현지화 (경쟁작 프록시 310건 중 0~1건).
10. **규정 공백 방어**: 기존 코드 재사용 범위 질문은 전부 미응답. 해커톤 기간 커밋만 있는 전용 레포 + HACKATHON.md에 범위 명시. 레포 public 재확인. 슬라이드는 레포 PDF + Devpost 업로드 병행. Discord 가입은 공지상 mandatory (`discord.com/invite/umEXASsAev`).

## 추천 아이디어 Top 3 (05 문서 §4)

| 순위 | 이름 | 한 줄 | 강점 |
| --- | --- | --- | --- |
| 1 | **Clause50** | URL 입력 → EU AI Act Article 50 투명성 준수 감사 SaaS | Article 50이 2026-08-02 발효, 유예 2026-12-02 만료, 갤러리 0건, 판정이 코드에 있어 wrapper 리스크 낮음 |
| 2 | **AgentReady** | Claude 브라우저 에이전트가 머천트 스토어에서 실제 구매 시도 → Agent Readiness Score | 데모 영상 가장 강력, wrapper 리스크 가장 낮음 |
| 3 | **MCPGuard** | MCP 서버 공급망 심사 + 정책 강제 프록시 | 기술 깊이 최상, 24h 내 샌드박스 구현이 리스크 |

## 지금 당장 할 일 (순서대로)

1. Discord 가입 + `#introductions` 자기소개 (5분)
2. Tin Computer $299 크레딧 클레임 (5분, 선착순)
3. NexFellow 무료 가입 → 24h 리뷰 신청 → "피드백 반영" 슬라이드 재료 확보
4. 아이디어 확정 + 스코프 동결 → 06 문서의 24h 빌드 순서 진행
5. 랜딩 + 대기자 폼을 가장 먼저 띄워 숫자가 쌓이게 함 (Impact 25%)
6. 04 문서의 T-24h~T-0 체크리스트를 그대로 따름

## 접근 불가했던 것

- 본 대회 프로젝트 갤러리 (마감 전 비공개) → 경쟁작 직접 확인 불가, UC Berkeley AI Hackathon 2026 갤러리로 대체
- Devpost 제출 폼 실제 필드 (로그인 필요)
- 주최·심사위원의 이 대회 관련 X·LinkedIn 게시물 (없거나 접근 차단)
- NexFellow Founder Plan 구체 가격·내역

## 2차 리서치 (2026-09-15 21:20 KST, `devpost_2120/`)

위 1차 문서(14:55~17:15 KST) 이후 마감 6시간 전에 다시 크롤링한 스냅샷. 결론은 1차와 같고(KillScore), 아래 항목은 여기에만 있다.

| 파일 | 여기에만 있는 것 |
| --- | --- |
| [devpost_2120/00_README.md](devpost_2120/00_README.md) | 마감 3중 교차 확인(연장 없음), 참가 자격 4조건 판정, 상금 산술 검증($4,000 + $299×100 = $33,900), Go/No-Go |
| [devpost_2120/03_resources_tooling.md](devpost_2120/03_resources_tooling.md) | `/resources` 페이지 비어 있음, Tin $299 클레임 URL 미공개 추적 결과, NexFellow 피드백 인용 전략 |
| [devpost_2120/06_project_ideas.md](devpost_2120/06_project_ideas.md) | 인증키 없이 응답 확인된 외부 API 5개(GitHub·npm·PyPI·endoflife·OSV), 아이디어 7선 |
| [devpost_2120/07_submission_checklist.md](devpost_2120/07_submission_checklist.md) | Devpost 제출 폼 필드별 준비물, 21:30~10:00 KST 시간표, 빈 제출물 선생성 보험 |

최종 빌드 결정은 [../../FINAL_DECISION.md](../../FINAL_DECISION.md) 참조.
