# 04. 제출 플레이북 — Devpost 온라인 해커톤 우승 전략

> 대상: AI Builders Hackathon 2026 / 마감 2026-09-16 12:00 KST
> 심사 배점(Devpost 공식 확인): Technical Implementation 25% · Problem Solving & Impact 25% · Innovation & Creativity 20% · UX & Design 15% · Presentation & Demo 15%
> (초기 브리핑의 30/30/20/20은 오류. 제출물은 제출폼 + 동작하는 제품 + 공개 GitHub + 데모 영상 ≤5분 + 슬라이드 ≤10장 5종)
> 제출물: 데모 영상 + GitHub 저장소 + Devpost 프로젝트 페이지
> 조사일: 2026-09-15

---

## 0. 한 문장 요약

> 심사위원이 실제로 소비하는 것은 **3분짜리 영상 한 편과 프로젝트 페이지 첫 화면**이다.
> 코드는 그 다음이다. 그러므로 남은 24시간 중 **최소 4~6시간을 "제출물 제작"에 별도 프로젝트로 배정**하고,
> 기능 개발은 T-8h에 코드 프리즈한다.

AngelHack이 반복 우승자를 분석한 결론이 정확히 이것이다:

> "Winners pick a problem they can finish rather than one they want to solve."
> "Winners treat the final phase as a distinct project, locking code four hours before submission and hardcoding the demo path."
> — https://angelhack.com/blog/hackathon-tips-for-winners/

---

## 1. Devpost 공식 규정 — 반드시 지켜야 하는 것들

### 1.1 제출 단계 (Know Your Submission Steps)

출처: https://help.devpost.com/article/126-know-your-submission-steps

| 단계 | 내용 | 실무 메모 |
| --- | --- | --- |
| 1. Manage Team | "Add your teammates by entering their email in the prompt or copy and share your invitation link" | **팀원 초대는 마감 전에 반드시 완료.** 초대 수락이 안 되면 상금 분배·수상자 명단에서 누락 |
| 2. Project Overview | Project name + tagline (둘 다 필수), Thumbnail | Thumbnail: "JPG, PNG or GIF format, 5 MB max file size", **3:2 비율 권장** |
| 3. Project Details | Project story (Markdown/LaTeX 지원), Built with 태그 **최대 25개**, Video demo, Try It Out 링크, Image Gallery | Video demo는 "usually required" 이며 **"must be hosted publicly on YouTube, or Vimeo"** |
| 4. Additional Details | 파일 업로드(최대 35MB; zip/pdf/word/apk), 제출자 유형, 거주 국가, 카테고리, **"URL to your code repository" with MIT License requirement**, 해커톤 기간 중 개선 내용 설명 | 대회별 상이. **오픈소스 라이선스 요구가 흔하므로 LICENSE 파일을 미리 커밋** |
| 5. Submit | 약관 동의 | |
| 6. Proofread | View 버튼으로 최종 검토 | |

공식 팁: **"Submitting at least one week early allows Devpost to check eligibility and request revisions if needed."**
→ 우리는 그럴 시간이 없으므로, **최소 T-3h에 "일단 제출" 후 마감 전까지 계속 수정**하는 전략을 쓴다(아래 1.3 참조).

### 1.2 Draft vs Submitted

출처: https://help.devpost.com/article/122-how-to-enter-a-submission

- Draft 상태는 **제출이 아니다**: "have not been submitted to the hackathon, and you still need to enter all information"
- 제출 성공 시: "a green notification bar at the top of the window confirming your submission" + My Projects에서 초록색 **"Submitted"** 배지
- **"You can always go back into your project and edit it before the submission deadline."**

### 1.3 마감 후 수정 — 불가능하다고 봐야 한다

출처: https://help.devpost.com/article/123-how-to-edit-a-submission

> "these changes will not be reflected in your hackathon submission, only in the project within your portfolio."

즉 **마감 후 편집은 내 포트폴리오에만 반영되고 심사 대상에는 반영되지 않는다.**
→ **마감 시각 기준으로 모든 것이 확정된다. T-0에 의존하지 말 것.**

또한 갤러리 게시 후 수정하면 재검수 큐로 돌아가며, 재검수 전까지는 **본인과 팀원만 볼 수 있다.**

### 1.4 프로젝트 갤러리 공개 시점

출처: https://help.devpost.com/article/80-what-is-the-project-gallery

프로젝트는 두 조건이 모두 충족돼야 공개된다:
1. "the hackathon manager turns on the gallery (usually happens after the submission deadline)"
2. "the hackathon manager has reviewed and moderated the project"

갤러리 검색은 **"the project's title, description, sponsor prizes, answers to custom questions fields, and screen names"** 를 인덱싱한다.
→ **제목·태그라인·설명에 검색될 키워드를 의도적으로 심어라.**
수상작은 "yellow 'winner' banner" 와 함께 갤러리 최상단 노출.

### 1.5 심사 플랫폼이 실제로 어떻게 동작하는가

출처: https://help.devpost.com/article/64-judging-public-voting

- "The Devpost Judging Platform is considered Online Judging on Devpost." — 모든 심사위원이 **단일 기준 세트**를 쓸 때 사용
- **"Judging criteria is usually weighted equally and this is how the Devpost judging platform is set up."**
- 더 복잡한 가중치가 필요하면 주최측이 Excel/Google Sheets로 오프라인 심사

> **해석**: 이번 대회는 25/25/20/15/15의 비대칭 가중치를 명시했으므로 오프라인 스프레드시트 심사일 가능성이 높다.
> 이 경우 심사위원이 **항목별로 수동 채점**하므로, **프로젝트 페이지에 심사 항목별 근거를 명시적으로 라벨링해 주는 것**이 매우 효과적이다.
> (예: 페이지에 "## 기술 완성도" "## 왜 시장이 있는가" 소제목을 그대로 두면 채점자가 찾기 쉽다.)

### 1.6 흔한 실격 사유

출처: https://info.devpost.com/blog/understanding-hackathon-submission-and-judging-criteria

> "many submissions are disqualified simply because they didn't meet the baseline criteria."

실격 유발 요인:
- 참가 자격 위반 (나이, 거주 지역)
- **요구된 기술/API 미사용** (스폰서 기술 요건)
- **접근 불가능한 데모 링크** (로그인 벽, 죽은 URL, private repo)
- **데모 영상 길이 초과**

추가로 실무에서 자주 터지는 것:
- YouTube 영상이 **Unlisted가 아니라 Private**
- YouTube "Made for Kids" 설정 → 임베드·댓글 차단으로 심사 방해.
  Devpost 공식 팁: **"Upload your video to YouTube" and mark it "Not for Kids"** (https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video)
- GitHub repo가 private
- LICENSE 파일 누락 (MIT 요구 대회 다수)

---

## 2. 데모 영상 — 가장 높은 ROI

### 2.1 공식 가이드라인

출처: https://help.devpost.com/article/84-video-making-best-practices

- **스크린캐스트를 권장**: "creating a screencast (a video screen capture with audio narration)" — 마케팅 영상보다 낫다. 심사위원이 앱이 실제로 어떻게 동작하는지 이해할 수 있기 때문
- **첫 몇 초에 정체를 밝혀라**: "explain what your app does (and if making the video for a specific hackathon, how it addresses the hackathon) in the first few seconds"
- **업로드를 미루지 마라**: "don't wait until the last minute to upload it" — 처리 시간이 포맷·용량·회선에 따라 "hours or more" 걸릴 수 있다
- **편집하라**: "Edit out the messy stuff, if you can, and don't be afraid to do multiple takes."
- **대본을 써라**: "Write out a script of what you'll say/show in your video, rehearse it before recording"
- 호스팅: YouTube, Vimeo, Youku

### 2.2 길이

- Devpost 생태계 표준: **3분 이내** (World's Largest Hackathon: "3 minutes maximum" — https://worldslargesthackathon.devpost.com/updates/36832-demo-video-tips)
- RevenueCat Shipaton: **"A demonstration video (max three minutes judges are required to watch)"** — 즉 심사위원은 3분까지만 의무적으로 본다. **3분을 넘기면 그 뒤는 안 본다고 가정하라.**
  (https://www.revenuecat.com/blog/engineering/how-to-win-shipaton-part-4-pitching-your-app)
- **권장: 2분 20초 ~ 2분 50초.** 3분 상한이면 절대 넘기지 말 것.

### 2.3 구조 (타임코드 배분)

Devpost 공식 6팁(https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video) + 반복 우승자 조언을 종합:

| 구간 | 시간 | 내용 |
| --- | --- | --- |
| Hook | 0:00–0:15 | 문제를 **구체적 인물**로 제시. 통계·도발적 질문·개인 경험. 제품명과 한 줄 피치 |
| Problem | 0:15–0:35 | 왜 지금 이게 아픈 문제인가. (AngelHack: 피치의 **약 30%를 문제 정의**, 70%를 솔루션 시연에) |
| Live Demo | 0:35–2:10 | **실제 동작하는 제품 화면.** 슬라이드 금지 |
| Tech/Arch | 2:10–2:35 | 아키텍처 다이어그램 1장 + 어려웠던 지점 1개 |
| Traction & CTA | 2:35–2:50 | 검증 수치 + 라이브 URL + "지금 써보세요" |

### 2.4 반복 우승자들의 핵심 원칙

browser-use "How to Win Hackathons" (https://browser-use.com/posts/how-to-win-hackathons):

> "explain with as few words as possible, and let your demo do the talking"
> "Have one short, sweet, and clear sentence for your pitch. Should be your first sentence."
> "One sentence pitch → problem → solution → demo format"
> "it's difficult for judges to understand technical depth in the span of a few minutes" — 대신 훌륭한 UI/UX에 투자하라
> "Assume the judges know basic principles of full-stack development, and nothing else"
> **"For judges, it's simple to tell what has been mocked, and it really hurts your project"**
> 심사위원이 던지는 질문: "Is it showstopping? Will any engineer see it and go, 'That's cool'?" / "What problem does it solve?" / "Who is it for?"

Devpost 공식 팁 중 중요한 것:
> **"Write a script! Try to avoid ChatGPT here if you can—its output is often too generic."**
> "Make your presentation clear and concise. Don't try to pack in way too much information or speed up the audio."
> "Leave at least two or three hours before the end of the hackathon to polish, record, and upload"

RevenueCat Shipaton 영상 구조:
> "show the problem your app solves, how it works, and why it matters"
> 시작은 "Setup + Need: introduce who you're building for and the frustration they face"
> 중반은 "what the user is achieving, not just what the interface looks like"
> 마무리는 "the new normal and wrap with a one-line transformation plus a clear call to action"

### 2.5 차별화 사례

PartyRock Generative AI Hackathon 1위 Param (https://info.devpost.com/blog/user-story-param):

> "I decided to think outside the box and produce a trailer-like experience akin to a real game launch."
> "A key strategy was avoiding the 'feature vortex' by only implementing the most important elements given the time constraints."

→ 남들이 다 쓰는 템플릿 영상 포맷에서 한 칸 벗어나면 기억에 남는다. 단, **실제 동작 화면을 희생하면서 연출하면 역효과**.

### 2.6 제작 도구 (하루 안에 끝내는 스택)

Devpost 권장: "Options include Microsoft PowerPoint for quick video export, Google Slides for team collaboration, **OBS Studio** for desktop recording, or Premiere Pro for editing." — **"Use Tools That Are Fastest for You to Use"**

실전 추천:
- 화면 녹화: **OBS Studio**(무료·리눅스 가능) / Loom(즉시 링크) / macOS는 QuickTime
- 커서 강조·줌: Screen Studio(macOS, 유료지만 품질 압도적) / Kap
- 편집: DaVinci Resolve(무료) / CapCut(자막 자동 생성 빠름)
- 자막: **반드시 넣는다.** 심사위원이 음소거로 볼 가능성, 비영어권 억양 보정, YouTube 자동자막은 부정확 → CapCut/Whisper로 SRT 생성 후 업로드
- 음성: 조용한 방·외장 마이크. 녹음 실패가 가장 흔한 재촬영 사유

### 2.7 영상 체크리스트

- [ ] 3분 이하 (권장 2:50 이하)
- [ ] YouTube 업로드, **Public 또는 Unlisted** (Private 아님)
- [ ] **"Not made for kids"** 설정
- [ ] 저작권 음악 미사용 (Shipaton: "No copyrighted music, trademarks, or other protected material")
- [ ] 첫 10초에 제품명 + 한 줄 피치
- [ ] 목업/하드코딩 화면 없음 (있다면 화면에 명시)
- [ ] 자막 포함
- [ ] 화면 텍스트가 720p에서 읽히는 크기
- [ ] 마지막 프레임에 라이브 URL + GitHub URL 정지 표시 (심사위원이 일시정지해 옮겨적을 수 있게)

---

## 3. 프로젝트 페이지 / README

### 3.1 Devpost 기본 템플릿

Devpost는 Project story에 아래 헤딩을 자동으로 채워준다 (수정 가능, Markdown/LaTeX 지원):

```
## Inspiration
## What it does
## How we built it
## Challenges we ran into
## Accomplishments that we're proud of
## What we learned
## What's next for [프로젝트명]
```

> "your project story section will prompt you with headings that make for a strong description. You can change it as you'd like and use Markdown or LaTeX to fancy it up!"

**전략적 수정**: 이번 대회 배점(기술 25 / 임팩트 25 / 혁신 20 / UX 15 / 발표·데모 15)에 맞춰 섹션을 **추가**한다.

```
## What it does            ← 최상단, 30초 안에 이해되게
## Why now / Who it's for  ← Problem Solving & Impact 25%
## Traction                ← Problem Solving & Impact 25% (검증 수치)
## How we built it         ← Technical Implementation 25% (아키텍처 다이어그램)
## Evals & Guardrails      ← Technical Implementation 25% + AI 프로젝트 차별화
## Design decisions        ← UX & Design 15%
## What makes it different ← Innovation & Creativity 20% (+ Presentation & Demo 15%는 영상·덱으로)
## Challenges / What we learned / What's next
```

### 3.2 제목 · 태그라인 공식

RevenueCat이 제시한 로그라인 포맷:

> "For [who], [App Name] helps [job to be done] by [distinct approach], so they can [valuable outcome]."

그리고 핵심 원칙: **"emphasize outcomes over features."**

제목 공식 (택 1):
- `<제품명> — <대상>을 위한 <성과>` (예: "Ledgerly — 1인 개발자를 위한 30초 회계 마감")
- `<제품명>: <익숙한 것> for <새로운 맥락>` (독창성 프레이밍에 유용)

태그라인 규칙:
- 60자 내외, **기술 나열 금지**("GPT-4o와 Next.js로 만든" ❌)
- 동사 + 구체적 성과 중심
- 갤러리 검색 인덱싱 대상이므로 핵심 키워드 포함

### 3.3 히어로 이미지 / GIF

- Devpost 썸네일: **3:2 비율, 5MB 이하, JPG/PNG/GIF**
- GIF 썸네일도 허용됨 → **제품이 실제로 동작하는 3초 루프 GIF**는 정적 로고보다 압도적으로 강하다
- Image Gallery에는 스크린샷 4~6장: 랜딩 → 온보딩 → 핵심 기능 → 결과 → 아키텍처 다이어그램

### 3.4 Built with 태그 (최대 25개)

전략:
1. **스폰서/필수 기술을 맨 앞에** (주최측 자동 필터링에 걸려야 함)
2. 실제 쓴 것만 — 안 쓴 걸 넣으면 심사위원 질문에서 무너진다
3. 검색 유입을 위해 대중적 태그(`python`, `react`, `openai`)와 차별화 태그(`langgraph`, `pgvector`)를 섞는다
4. 25개를 다 채울 필요 없다. 8~15개가 적당

### 3.5 README (GitHub)

> "A screenshot or a short GIF of the tool in action is almost always worth more than another badge."
> "Lead with a precise one-line description. Say exactly what the project does and for whom."
> "show value within the first screen. A usage example, a screenshot, or a GIF before the reader has to scroll."
> "every badge should answer a question a real evaluator asks"
> — https://pushpen.dev/blog/github-readme-best-practices-2026

권장 README 뼈대:

~~~markdown
<h1 align="center">프로젝트명</h1>
<p align="center">한 줄 로그라인</p>
<p align="center">
  <a href="LIVE_URL">🔗 Live Demo</a> ·
  <a href="VIDEO_URL">▶️ 3분 데모</a> ·
  <a href="DEVPOST_URL">🏆 Devpost</a>
</p>

![hero](docs/hero.gif)

## 문제
## 해결 방식
## 아키텍처
```mermaid ... ```
## 빠른 시작 (60초)
## 기술 스택
## 평가(Evals) 결과
## 한계 및 다음 단계
## 라이선스 (MIT)
~~~

**중요**: 심사위원은 커밋 히스토리를 본다.
> "they will be checking the commit history of the project to ensure that you have made that project during the hackathon period not before"
> — https://arindam1729.hashnode.dev/how-to-use-github-effectively-at-hackathons

→ 커밋을 한 방에 몰아넣지 말고, 의미 단위로 쪼개서 기간 내 분산 커밋. repo는 **Public**.

---

## 4. Problem Solving & Impact 25% (PMF) — 하루 만에 만드는 검증 증거

해커톤에서 "시장이 있다"를 말로만 하면 점수가 안 나온다. **관찰 가능한 신호**를 만들어라.

### 4.1 24시간 안에 가능한 검증 전술 (ROI 순)

| 전술 | 소요 | 산출물 | 비고 |
| --- | --- | --- | --- |
| **사용자 인터뷰 5~8명** | 2~3h | 인용문 3개 + 문제 확인율 | 가장 설득력 높음. 지인·커뮤니티 DM으로 15분씩 |
| **랜딩 + 대기자 명단** | 1h | 가입 수 스크린샷 | Framer/Carrd/Vercel 템플릿. 실제 제품 링크 옆에 배치 |
| **Reddit / X / 관련 커뮤니티 포스팅** | 1h | 조회수·댓글·"이거 언제 나와요?" | 문제 공감 댓글 캡처가 강력한 증거 |
| **Fake-door 테스트** | 30m | 클릭률 | "Pro 플랜" 버튼 → "곧 출시, 알림 받기" |
| **가격 페이지** | 30m | 가격 가설 제시 | 비즈니스 모델을 생각했다는 신호 자체가 점수 |
| **디자인 파트너 LOI / 사용 의향 서면** | 1h | 스크린샷 1장 | 소수라도 실명 조직이면 압도적 |

근거:
> "At pre-seed, qualitative traction counts: 50 customer interviews validating the problem, 200 waitlist signups, or a signed letter of intent from a design partner are legitimate proof points."
> — https://waveup.com/blog/market-validation/

> "Market validation ... combines quantitative signals (sign-ups, pre-orders, waitlist growth) with qualitative insight (customer interviews, problem-confirmation surveys)."

### 4.2 제시 방법

프로젝트 페이지에 **`## Traction` 섹션**을 두고 숫자를 그대로 쓴다:

```
- 해커톤 기간 중 7명 인터뷰 — 7/7이 "매주 이 작업에 30분 이상 쓴다"고 답변
- 랜딩 공개 후 18시간 만에 대기자 43명 (전환율 11%)
- r/xxx 게시글 조회 2,400 / 댓글 31 — "이거 지금 쓸 수 있나요?" 9건
- 실사용자 5명이 실제 계정 생성, 누적 세션 22건
```

**원칙**: 숫자를 부풀리지 말고, 작은 숫자라도 **모수와 기간을 함께** 적는다. 심사위원은 정직한 43명을 과장된 "수천 명 관심"보다 높게 평가한다.

### 4.3 PMF 서사 구조

1. **누가** — 페르소나를 이름·직무 수준으로 좁혀라 (AngelHack: "specific personas rather than broad categories")
2. **지금 어떻게 하고 있나** — 현재의 대체재(엑셀, 수작업, 경쟁 제품)
3. **왜 그게 아픈가** — 시간/비용 수치
4. **왜 지금인가** — 기술적 변곡점(모델 가격 하락, 새 API 등)
5. **우리가 본 증거** — 4.2의 숫자
6. **어떻게 돈을 버나** — 가격 가설 한 줄

---

## 5. Technical Implementation 25% — 심사위원이 실제로 알아채는 최소 집합

browser-use의 경고를 다시:
> "For judges, it's simple to tell what has been mocked, and it really hurts your project"

### 5.1 필수 (없으면 감점)

- [ ] **배포된 공개 URL** — 로그인 없이 최소한 무언가는 보여야 함. 게스트/데모 계정 제공
- [ ] **동작하는 인증** — 이메일 매직링크 또는 OAuth 1개면 충분. 자체 구현보다 Clerk/Supabase Auth/Auth.js
- [ ] **영속성** — 새로고침·재로그인 후 데이터가 남는다. 인메모리 상태만 있으면 즉시 들통
- [ ] **에러 처리** — API 실패 시 사용자에게 보이는 메시지. 빈 화면·콘솔 스택트레이스 금지
- [ ] **Public GitHub repo + LICENSE(MIT) + README**
- [ ] **환경변수 예시 파일**(`.env.example`)과 60초 안에 로컬 실행되는 스크립트

### 5.2 있으면 확실히 눈에 띄는 것

- [ ] **아키텍처 다이어그램 1장** (Mermaid로 README에 인라인 — 이미지 관리 부담 없음)
- [ ] **핵심 로직 테스트 몇 개 + 통과하는 CI 배지** — "every badge should answer a question a real evaluator asks"
- [ ] **평가(eval) 결과 표** — AI 프로젝트에서 가장 차별화됨 (6장 참조)
- [ ] **관측성**: 요청 추적 로그, LLM 호출 토큰/비용/지연 기록. 대시보드 스크린샷 1장이면 충분
- [ ] **레이트리밋 / 입력 검증 / 프롬프트 인젝션 방어** — 한 줄이라도 언급

### 5.3 시간이 없을 때의 우선순위

> 배포 URL > 영속성 > 에러 처리 > 인증 > eval 표 > 테스트/CI > 관측성

---

## 6. AI/LLM 프로젝트 특수 심사 포인트

### 6.1 "얇은 래퍼" 문제

> Judges disqualify projects where AI is purely cosmetic (e.g., "we called ChatGPT once" with no integration into the product).

> "A chatbot responds to a single prompt. An agent works through a goal, calling APIs and adjusting as it goes."
> — https://angelhack.com/blog/ai-agent-hackathon/

래퍼에서 벗어나는 방법:
1. **멀티스텝 오케스트레이션** — 여러 시스템을 가로지르는 워크플로 (CRM 조회 → 데이터 질의 → 트래커 갱신 → 요약 전송)
2. **도구 사용** — 실제 외부 API/DB에 쓰기 작업을 하는가
3. **상태와 메모리** — 세션 간 컨텍스트 유지
4. **재시도·실패 복구** — 도구 호출 실패 시 계획을 바꾸는가
5. **도메인 데이터** — 범용 모델이 모르는 자체 데이터/인덱스
6. **결정론적 경계** — LLM이 하면 안 되는 부분을 코드로 강제

> "Most 'agent demos' look magical because they hide the hardest parts: state, tool contracts, retries, evaluation, and safety boundaries. In production, an agent is not a prompt — it's a distributed system where the LLM happens to be the planner/executor."
> — https://andriifurmanets.com/blogs/ai-agents-2026-practical-architecture-tools-memory-evals-guardrails

### 6.2 Eval을 보여줘라 (가장 저평가된 가점 요소)

> "Without an evaluation framework, judges score videos and vibes—whoever made the slickest demo wins, regardless of whether their agent actually worked."

표준 에이전트 eval 5지표 (AngelHack 2026 playbook, 원문 인용):

> "Task completion rate. Percentage of test scenarios that end with the goal met. Tool-use accuracy. Whether the agent calls the right tool at the right step. Cost per run. Token spend and API costs per successful task. Latency. Time from prompt to completion. Hallucination rate. Frequency of false claims or fabricated tool calls."

**하루 안에 만드는 최소 eval**:
- 대표 시나리오 **15~20개**를 YAML/JSON으로 작성
- 자동 실행 스크립트 1개 → 표 출력
- README에 결과 표 + 실패 케이스 2개를 **정직하게** 기재

```
| 시나리오 세트 | 성공률 | 도구 호출 정확도 | 평균 지연 | 회당 비용 |
| --- | --- | --- | --- | --- |
| 기본 20건 | 18/20 (90%) | 94% | 6.2s | $0.013 |
```

**실패 케이스를 공개하는 팀은 거의 없다. 이게 신뢰를 만든다.**

### 6.3 가드레일

영상/페이지에서 30초만 써도 인상이 달라진다:
- 입력 검증 + 프롬프트 인젝션 필터
- 출력 스키마 강제 (structured output / JSON schema)
- 민감 작업 전 사용자 확인 단계 (human-in-the-loop)
- 근거 인용 / 출처 표시로 환각 억제
- 비용 상한·타임아웃

### 6.4 데모에서 에이전트를 인상적으로 보이게 하는 법

- **추론 과정(trace)을 UI에 노출** — 어떤 도구를 왜 호출했는지 실시간 스트리밍
- **실패에서 복구하는 장면을 일부러 보여주기** — "이 API가 죽으면 이렇게 우회합니다"
- **실제 외부 부작용** — 이메일이 진짜로 오고, 시트가 진짜로 갱신되는 장면
- 속도가 느리면 **배속 표시 후 배속 재생**(속임수 아님을 명시)

---

## 7. UX & Design 15% — 하루 안의 빠른 승리

> "it's difficult for judges to understand technical depth in the span of a few minutes" → 대신 UI/UX에 투자하라. "Visual excellence is universal."
> — browser-use

### 7.1 컴포넌트/템플릿 (직접 디자인하지 말 것)

- **shadcn/ui + Tailwind** — 기본값이 이미 좋고, 다크모드가 토큰으로 내장
- **Tailwind UI / shadcnblocks / Magic UI** — 랜딩 섹션 복붙
- **Vercel / Next.js 템플릿** — 인증·DB 연결된 SaaS 스타터
- 아이콘: **Lucide** 하나로 통일
- 폰트: 본문 1개 + 제목 1개, 최대 2종

### 7.2 한 시간 안에 티 나는 개선 10가지

1. **여백과 타이포 스케일 정리** — 가장 큰 체감 차이
2. **다크모드** — 토글 1개. 심사위원 다수가 다크모드 사용자
3. **빈 상태(empty state)** — 일러스트 + 다음 행동 버튼. "an honest empty state protects trust"
4. **스켈레톤 로딩** — "Use a skeleton when you know the shape of the answer and the wait is one to ten seconds"
5. **LLM 응답 스트리밍** — "streaming cuts perceived wait time by 55 to 70 percent even when the total generation time is identical" (https://www.boundev.ai/blog/ai-feature-loading-error-empty-states-ux)
6. **상태 문구**(status line) — "문서 3건 검색 중…" 같은 진행 설명.
   "With streaming and a clear status line, users tolerate ten seconds or more, while with a blank screen, patience runs out in two to three seconds."
7. **온보딩 3스텝** — 첫 로그인 후 샘플 데이터 1클릭 주입("데모 데이터로 시작하기"). 심사위원이 빈 화면을 보지 않게 하는 결정적 장치
8. **에러 상태 디자인** — 재시도 버튼 + 사람이 읽는 문구
9. **모바일 반응형** — 심사위원이 폰으로 열어볼 수 있다. 최소 랜딩과 핵심 화면 1개는 필수
10. **토스트/마이크로 인터랙션** — 저장·완료 피드백

### 7.3 빈 상태 활용

> "I see your project list is empty. Would you like me to walk you through creating your first project?"
> — AI 앱의 빈 상태를 대화형 온보딩으로 쓰는 패턴 (https://www.eleken.co/blog-posts/empty-state-ux)

### 7.4 절대 하지 말 것

- 데모 영상 촬영 전 UI 대규모 리팩터링
- 로딩 스피너만 있는 30초 대기
- 콘솔 에러가 보이는 화면 녹화
- lorem ipsum, 깨진 이미지, 미완성 페이지 링크

---

## 8. Innovation & Creativity 20% — 익숙한 아이디어를 새롭게 포지셔닝하기

핵심 사실: **아이디어 자체가 새로울 필요는 없다.**

> Hackathon ideas do not need to be original—judges reward execution and problem-solving more than raw novelty. Winning projects often improve on an existing concept by targeting a specific audience, applying a new technology, or combining two ideas unexpectedly.
> 또한 "a new approach to an existing challenge can be just as impressive as a completely novel idea", "solve an unoriginal problem in an original way", 그리고 **"narrow scope that demonstrates product thinking—scoping to specific triggers or domains signals domain understanding rather than generic application of technology."**
> — https://whereuelevate.com/blogs/15-crazy-hackathon-ideas-that-actually-win , https://unstop.com/blog/how-to-judge-a-hackathon

### 8.1 포지셔닝 레버 5가지 (택 1~2)

| 레버 | 문장 틀 | 예 |
| --- | --- | --- |
| **대상 좁히기** | "X는 많지만, <아주 좁은 대상>을 위한 X는 없다" | "노션 AI는 많지만 임상시험 문서 담당자용은 없다" |
| **트리거 좁히기** | "우리는 <특정 순간>에만 개입한다" | "PR이 열리는 순간에만 작동" |
| **예상 밖 결합** | "A + B" | "스프레드시트 + 에이전트 트레이스" |
| **작업 방식 전환** | "사람이 묻는 대신 시스템이 먼저 제안한다" | 채팅 → 백그라운드 자동화 |
| **새 제약을 무기로** | "완전 로컬/오프라인/비용 1/10" | 온디바이스 모델 |

### 8.2 독창성 문장 공식

> "대부분의 <카테고리>는 <통념적 접근>을 한다. 우리는 <반대 접근>을 택했다. 왜냐하면 <인사이트>이기 때문이다."

이 세 문장을 프로젝트 페이지의 `## What makes it different` 최상단에 배치.

### 8.3 하지 말 것

- "세계 최초", "혁신적인" 같은 형용사 — 근거 없는 주장은 감점
- 경쟁 제품 부정 — 대신 "우리는 다른 문제를 푼다"로 프레이밍
- 기술 스택을 독창성으로 포장 ("최신 GPT-5를 사용" ❌)

---

## 9. 제출 24시간 전 실행 체크리스트

> 기준 시각: 마감 2026-09-16 12:00 KST
> 원칙: **영상과 페이지를 별도 프로젝트로 취급하고, 마감 3시간 전에 "일단 제출" 상태를 만든다.**

### T-24h → T-20h (09/15 12:00 – 16:00) · 기능 확정과 자료 수집

- [ ] **스코프 동결**: 데모에 나올 화면만 남기고 나머지 기능은 숨긴다 ("feature vortex" 회피)
- [ ] 데모 시나리오(golden path) 1개를 확정하고 문서화
- [ ] **PMF 검증 착수 (병렬)**: 랜딩+대기자 페이지 배포, 커뮤니티 포스팅 게시, 인터뷰 5~8건 일정 잡기 — **이건 시간이 지나야 숫자가 쌓이므로 가장 먼저 시작**
- [ ] Devpost에서 프로젝트 **Draft 생성**, 팀원 초대 발송, 프로젝트명·태그라인 입력
- [ ] 대회 규정 재확인: 필수 기술/API, 영상 길이, 라이선스, 자격 요건

### T-20h → T-14h (16:00 – 22:00) · 기능 마무리 + 배포

- [ ] 핵심 기능 완성, **목업 제거** (남는 목업은 UI에 명시)
- [ ] 인증 / 영속성 / 에러 처리 3종 확인
- [ ] **프로덕션 배포 + 공개 URL 확보**, 게스트 데모 계정 생성
- [ ] 샘플 데이터 1클릭 주입 버튼 추가 (빈 화면 방지)
- [ ] eval 시나리오 15~20건 작성 및 1회 실행, 결과 표 확보

### T-14h → T-10h (22:00 – 09/16 02:00) · **코드 프리즈** + UX 폴리시

- [ ] ⛔ **코드 프리즈 (T-12h 권장)** — 이후 기능 추가 금지, 버그 수정만
- [ ] UX 빠른 승리 적용: 빈 상태 / 스켈레톤 / 스트리밍 상태 문구 / 다크모드 / 토스트
- [ ] 모바일에서 랜딩 + 핵심 화면 1개 확인
- [ ] 콘솔 에러 제거, 깨진 링크 제거
- [ ] 아키텍처 다이어그램 작성 (Mermaid)
- [ ] 스크린샷 4~6장 촬영, 히어로 GIF 3초 루프 제작 (3:2, 5MB 이하)

### T-10h → T-7h (02:00 – 05:00) · 영상 제작

- [ ] **대본 작성** (11장 스켈레톤 사용) — 소리 내어 읽으며 2:40 안에 들어오는지 측정
- [ ] 리허설 2회
- [ ] 녹화 (실패 대비 **2~3 테이크**)
- [ ] 편집: 군더더기 제거, 텍스트 오버레이, 마지막 프레임에 URL 고정
- [ ] 자막 생성 및 삽입
- [ ] **YouTube 업로드** — 여기서 처리 지연이 가장 흔한 사고. Public/Unlisted + **Not for kids** 설정
- [ ] 다른 브라우저 시크릿 모드에서 영상 재생 확인

### T-7h → T-4h (05:00 – 08:00) · 페이지와 README

- [ ] GitHub repo **Public 전환**, LICENSE(MIT), `.env.example`, README 완성
- [ ] 커밋 히스토리 정리 (기간 내 분산돼 있는지 확인)
- [ ] Devpost Project story 전 섹션 작성 (10장 템플릿 사용)
- [ ] Traction 섹션에 실제 수치 기입 (지금까지 쌓인 대기자/인터뷰/댓글)
- [ ] Built with 태그 8~15개, **스폰서 기술을 맨 앞에**
- [ ] 썸네일 업로드(3:2), 이미지 갤러리 4~6장
- [ ] Try It Out 링크 = 라이브 URL + GitHub URL
- [ ] 추가 질문(Additional Details) 전부 응답

### T-4h → T-3h (08:00 – 09:00) · **1차 제출**

- [ ] ✅ **Submit 버튼 클릭** — 초록색 확인 배너 + "Submitted" 배지 확인
- [ ] 마감 후에는 수정이 심사에 반영되지 않으므로, 이후 수정은 모두 마감 전에

### T-3h → T-1h (09:00 – 11:00) · 외부 눈으로 검증

- [ ] **팀 밖의 사람 1명**에게 링크만 주고 "이게 뭐하는 건지 30초 안에 설명해 보라" 시키기
- [ ] 로그아웃 상태 시크릿 창에서 라이브 URL 접속 → 데모 계정으로 golden path 완주
- [ ] 영상 링크, GitHub 링크, 라이브 링크 3개 전부 외부 환경에서 클릭 테스트
- [ ] 오탈자 교정 (Devpost View 버튼)
- [ ] 심사 4개 항목이 페이지에서 각각 찾아지는지 자가 채점

### T-1h → T-0 (11:00 – 12:00) · 동결

- [ ] ⛔ 변경 금지. 배포 금지. 새 커밋 금지
- [ ] 제출 상태 스크린샷 보관
- [ ] 라이브 서비스가 살아 있는지 마지막 확인 (심사 기간 내내 유지되어야 함)
- [ ] API 키 사용량 한도 / 결제 수단 확인 — **심사 중 크레딧 소진으로 데모가 죽는 사고가 흔하다**

---

## 10. Devpost 프로젝트 스토리 — 빈칸 채우기 템플릿

```markdown
## What it does

**[제품명]은(는) [대상 페르소나]가 [해야 하는 일]을 [독자적 접근]으로 해결해,
[가치 있는 결과]를 얻게 합니다.**

지금 [대상]은 [현재 방식]으로 이 일을 처리하며, 여기에 [시간/비용 수치]가 듭니다.
[제품명]은 [핵심 동작 한 문장]으로 이를 [개선 수치]로 줄입니다.

▶️ 데모 영상: [YOUTUBE_URL]
🔗 지금 사용해보기: [LIVE_URL]  (데모 계정: demo@____ / ____)
💻 소스: [GITHUB_URL]

---

## Why now / Who it's for

- **대상**: [직무·상황까지 좁힌 페르소나 — "마케터" ❌ / "시드 단계 B2B SaaS의 1인 그로스 담당" ⭕]
- **현재의 대체재**: [엑셀 / 수작업 / 경쟁 제품]
- **왜 아픈가**: [주당 N시간, 월 $N, 오류율 N%]
- **왜 지금인가**: [기술적 변곡점 — 모델 가격, 새 API, 규제 변화]

---

## Traction

해커톤 기간(약 __시간) 동안 확보한 실제 신호입니다.

- 사용자 인터뷰 **__명** — __/__ 가 "[구체적 문제 진술]"에 동의
- 랜딩 페이지 공개 후 __시간 만에 대기자 **__명** (방문 __명, 전환율 __%)
- [커뮤니티명] 게시글 조회 **__**, 댓글 **__** — "언제 쓸 수 있나요" 문의 __건
- 실제 가입 후 핵심 액션 완료 **__명 / __세션**

> 대표 인용: "[인터뷰 대상자의 실제 발언 한 줄]" — [역할, 회사 규모]

---

## How we built it

[아키텍처 다이어그램 이미지 또는 Mermaid]

- **프론트엔드**: [___]
- **백엔드 / API**: [___]
- **데이터**: [DB, 벡터 스토어, 인덱싱 전략]
- **모델 / 오케스트레이션**: [모델명, 에이전트 루프, 도구 정의 방식]
- **인프라**: [배포, 인증, 큐, 관측성]

핵심 설계 결정 3가지:
1. **[결정]** — [왜. 대안은 무엇이었고 왜 안 택했는지]
2. **[결정]** — [___]
3. **[결정]** — [___]

---

## Evals & Guardrails

에이전트가 "데모에서만 되는" 것이 아님을 확인하기 위해 __개 시나리오로 평가했습니다.

| 지표 | 결과 |
| --- | --- |
| Task completion rate | __ / __ (__%) |
| Tool-use accuracy | __% |
| Avg latency | __s |
| Cost per run | $__ |
| Hallucination / 잘못된 도구 호출 | __건 |

아직 실패하는 케이스(정직하게 공개):
- [실패 케이스 1] → [현재 대응 / 다음 계획]
- [실패 케이스 2] → [___]

가드레일:
- [입력 검증 / 프롬프트 인젝션 필터]
- [출력 스키마 강제]
- [민감 작업 전 사용자 확인]
- [비용 상한·타임아웃]

---

## Design decisions

- **[온보딩]**: [빈 화면 대신 무엇을 보여주는가]
- **[대기 경험]**: [스트리밍 + 상태 문구로 체감 대기 축소]
- **[에러]**: [무엇이 잘못됐고 무엇을 하면 되는지 사람 말로]
- **[접근성/반응형]**: [다크모드, 모바일, 키보드]

---

## What makes it different

대부분의 [카테고리]는 **[통념적 접근]**을 합니다.
우리는 **[반대 접근]**을 택했습니다. 왜냐하면 **[인사이트]**이기 때문입니다.

구체적으로:
- [기존 제품]은 [일반적 대상]을 노리지만, 우리는 [아주 좁은 대상/트리거]에만 개입합니다
- [A]와 [B]를 결합해 [기존에 없던 결과]를 만듭니다

---

## Challenges we ran into

1. **[문제]** — [어떻게 진단했고 어떻게 해결했는지. 구체적 기술 디테일 1개]
2. **[문제]** — [___]

---

## What we learned

- [기술적 배움 1개 — 구체적으로]
- [사용자에 대한 배움 1개 — 인터뷰에서 가설이 틀렸던 지점]

---

## What's next for [제품명]

- **1주 내**: [___]
- **1개월 내**: [___]
- **비즈니스 모델**: [무료 티어 ___ / 유료 $__ per __ — 근거: ___]

> 🔗 [LIVE_URL] · ▶️ [YOUTUBE_URL] · 💻 [GITHUB_URL]
```

---

## 11. 데모 영상 대본 스켈레톤 (2:30 ~ 2:50)

> 사용법: 대괄호를 채우고 **소리 내어 읽으면서 초를 재라.** 한국어 기준 분당 300~330자.
> Devpost 공식 경고: "Write a script! Try to avoid ChatGPT here if you can—its output is often too generic."

### [0:00 – 0:12] HOOK — 화면: 문제 상황 실물

> "[대상]은 매주 [N시간]을 [지겨운 작업]에 씁니다.
> 저희도 그랬습니다. 그래서 [제품명]을 만들었습니다.
> **[제품명]은 [한 문장 피치].**"

- 화면: 현재의 고통스러운 방식(엑셀, 탭 20개, 수작업) 3초 → 제품 로고/이름
- ⚠️ 이 12초 안에 제품명과 무엇인지가 나와야 한다

### [0:12 – 0:35] PROBLEM — 화면: 페르소나 + 수치

> "[구체적 인물]을 예로 들겠습니다. [상황].
> 지금은 [현재 방식]으로 처리하는데, [시간/비용/오류] 문제가 있습니다.
> 기존 도구들은 [왜 안 맞는지]."

- 화면: 간단한 텍스트 카드 1~2장 (여기만 슬라이드 허용)
- 전체 피치의 약 30%를 문제 정의에 (AngelHack)

### [0:35 – 2:05] LIVE DEMO — 화면: 실제 제품, 끊김 없이

> "[제품명]에서는 이렇게 합니다."

1. **(0:35–0:50) 진입** — 로그인 후 첫 화면. 빈 상태 → 온보딩 → 샘플 데이터
2. **(0:50–1:25) 핵심 액션** — [사용자가 하는 한 가지 동작]과 그 결과.
   *"보시는 것처럼 [에이전트]가 [도구 A]를 호출해서 [B]를 가져오고, [C]를 갱신합니다."*
   → **추론/도구 호출 trace를 화면에 노출**
3. **(1:25–1:45) 차별 기능** — 남들이 못 하는 한 가지.
   *"여기가 다른 점입니다. [___]"*
4. **(1:45–2:05) 실제 부작용 확인** — 메일함/시트/DB가 진짜로 바뀐 화면.
   *"실제로 [외부 시스템]에 반영된 걸 보실 수 있습니다."*

- ⚠️ 목업 금지. "For judges, it's simple to tell what has been mocked"
- ⚠️ 느린 구간은 배속 + 화면에 "2x" 표기
- ⚠️ 마우스 움직임을 천천히, 클릭 대상은 줌

### [2:05 – 2:30] TECH & RIGOR — 화면: 아키텍처 다이어그램 + eval 표

> "구조는 이렇습니다. [프론트] – [API] – [오케스트레이터] – [도구들].
> 가장 어려웠던 건 [문제]였고, [해결책]으로 풀었습니다.
> 그리고 데모에서만 되는 게 아니라는 걸 보이기 위해 [N]개 시나리오로 평가했습니다.
> **성공률 [__]%, 도구 호출 정확도 [__]%, 회당 비용 [$__].**"

- 화면: 다이어그램 8초 → eval 결과 표 8초
- ⚠️ 기술 설명은 두 문장을 넘기지 마라 (browser-use)

### [2:30 – 2:48] TRACTION & CTA — 화면: 대기자/댓글 캡처 → URL 정지 화면

> "만들면서 [N]명을 인터뷰했고 [N]/[N]이 같은 문제를 겪고 있었습니다.
> 랜딩을 연 지 [N]시간 만에 [N]명이 대기자로 등록했습니다.
> **지금 [도메인]에서 바로 써보실 수 있습니다. 감사합니다.**"

- 마지막 5초: **라이브 URL · GitHub URL · 데모 계정**을 큰 글씨로 정지 표시
- 배경음악은 여기서 페이드아웃, 저작권 없는 트랙만

### 녹화 전 최종 점검

- [ ] 브라우저: 북마크바 숨김, 시크릿 창, 알림 끄기, 확대 125%
- [ ] 화면: 1080p, 불필요한 탭·데스크톱 아이콘 정리
- [ ] 데이터: 실명·실제 이메일·API 키가 화면에 노출되지 않는지
- [ ] 오디오: 30초 테스트 녹음 후 재생 확인
- [ ] 네트워크: 데모 중 API가 죽지 않도록 크레딧 확인

---

## 12. 출처 목록

### Devpost 공식
- 제출 단계 상세 — https://help.devpost.com/article/126-know-your-submission-steps
- 제출 방법 — https://help.devpost.com/article/122-how-to-enter-a-submission
- 제출 수정 — https://help.devpost.com/article/123-how-to-edit-a-submission
- 영상 제작 베스트 프랙티스 — https://help.devpost.com/article/84-video-making-best-practices
- 심사 및 공개 투표 — https://help.devpost.com/article/64-judging-public-voting
- 프로젝트 갤러리 — https://help.devpost.com/article/80-what-is-the-project-gallery
- 제출 갤러리 카테고리 — https://help.devpost.com/category/35-submission-gallery
- 해커톤 제출 카테고리 — https://help.devpost.com/category/20-submitting-to-a-hackathon
- 우승 데모 영상 6팁 — https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video
- 제출·심사 기준 이해하기 — https://info.devpost.com/blog/understanding-hackathon-submission-and-judging-criteria
- 1위 수상자 인터뷰(Param) — https://info.devpost.com/blog/user-story-param
- Devpost 심사 방법 영상 — https://www.youtube.com/watch?v=kpV6-T0KB40
- 제출 예시 템플릿 — https://devpost.com/software/example-template-submission

### 해커톤 운영·심사
- MLH 심사 계획 — https://guide.mlh.com/general-information/judging-and-submissions/judging-plan
- AngelHack: 반복 우승자가 다르게 하는 것 — https://angelhack.com/blog/hackathon-tips-for-winners/
- AngelHack: AI 에이전트 해커톤 2026 플레이북 — https://angelhack.com/blog/ai-agent-hackathon/
- World's Largest Hackathon 데모 영상 팁 — https://worldslargesthackathon.devpost.com/updates/36832-demo-video-tips
- HackHarvard 프로젝트 규칙 — https://info.hhuh.io/rules/project_rules/
- 해커톤 심사 5기준 — https://eventornado.com/blog/how-to-judge-a-hackathon-5-criteria-to-pick-winners
- 해커톤 심사 방법 — https://unstop.com/blog/how-to-judge-a-hackathon

### 우승 전략 / 피치
- browser-use: How to Win Hackathons — https://browser-use.com/posts/how-to-win-hackathons
- RevenueCat Shipaton 파트4: 앱 피칭 — https://www.revenuecat.com/blog/engineering/how-to-win-shipaton-part-4-pitching-your-app
- Gary Yau Chan: 해커톤 우승 8단계 — https://medium.com/garyyauchan/ultimate-8-step-guide-to-winning-hackathons-84c9dacbe8e
- szeyusim: 연쇄 해커 프로 팁 — https://szeyusim.medium.com/how-i-win-most-hackathons-stories-pro-tips-from-a-serial-hacker-1969c6470f92
- Cloudinary/DEV: How to Win a Hackathon — https://dev.to/cloudinary/how-to-win-a-hackathon-1377

### PMF / 검증
- Waveup: 2026 시장 검증 11가지 방법 — https://waveup.com/blog/market-validation/
- Thin Slices: 프리시드 시장 검증 전술 — https://www.thinslices.com/insights/market-validation-tactics-for-pre-seed-and-seed-tech-startups

### 기술 / AI
- AI Agents in 2026: Tools, Memory, Evals, Guardrails — https://andriifurmanets.com/blogs/ai-agents-2026-practical-architecture-tools-memory-evals-guardrails

### UX
- AI 기능의 로딩·에러·빈 상태 UX — https://www.boundev.ai/blog/ai-feature-loading-error-empty-states-ux
- Eleken: 빈 상태 UX 예시와 규칙 — https://www.eleken.co/blog-posts/empty-state-ux
- Pencil & Paper: 빈 상태 베스트 프랙티스 — https://www.pencilandpaper.io/articles/empty-states
- Raw.Studio: 빈 상태·에러·온보딩 — https://raw.studio/blog/empty-states-error-states-onboarding-the-hidden-ux-moments-users-notice/
- UX Collective: 로더와 빈 상태를 언제 쓸 것인가 — https://uxdesign.cc/when-to-use-loaders-empty-states-ebd23cecc7d6

### README / GitHub
- GitHub README 베스트 프랙티스 2026 — https://pushpen.dev/blog/github-readme-best-practices-2026
- GitHub README 템플릿 가이드 2026 — https://gingiris.github.io/growth-tools/blog/2026/04/02/github-readme-template-guide/
- 해커톤 GitHub 치트시트 — https://arindam1729.hashnode.dev/how-to-use-github-effectively-at-hackathons
- freeCodeCamp: 좋은 README 쓰기 — https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/

### 독창성 / 아이디어
- 2026년 실제로 우승하는 해커톤 아이디어 15 — https://whereuelevate.com/blogs/15-crazy-hackathon-ideas-that-actually-win
- HackerEarth: 50+ 해커톤 아이디어 2026 — https://www.hackerearth.com/blog/hackathon-ideas
