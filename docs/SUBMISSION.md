# 제출 패키지

마감: 2026-09-15 23:00 EDT = 2026-09-16 12:00 KST. 자체 마감 10:00 KST.

## 1. Devpost 폼

| 필드 | 값 |
| --- | --- |
| Project name | KillScore |
| Tagline | 100% coverage. 63% mutation score. The SaaS release gate that scores whether your AI-written tests can actually catch a bug. |
| Try it out | https://killscore.hajin.xyz |
| Repo | https://github.com/SSALMUK-COMPOSE-COFFEE/DEVPOST_2026_AI_BUILDERS_HACKATHON |
| Video | (YouTube URL, Not for Kids) |
| Built with | python, fastapi, sqlalchemy, postgresql, pytest, ast, mutation-testing, weasyprint, sse, nextjs, react, typescript, tailwind, claude, openrouter, docker, apache-2.0 |

### Inspiration

In 2026 roughly a quarter of merged commits carry AI traces. Coding agents write the tests too, and the tests reach 100% line coverage on the first try. That number is what release engineers use to approve a merge. We flipped one comparison operator in a payment function and all 40 AI-written tests still passed. Coverage never moved. The metric we gate on cannot see the failure mode that AI-written tests introduce, because a test derived from the implementation cannot disagree with the implementation.

### What it does

KillScore is a pull-request gate. It reads the PR diff, finds only the Python functions the diff touched, and plants small deliberate bugs (mutants) in them: `>` becomes `>=`, `and` becomes `or`, a constant shifts by one, an `except: raise` becomes `except: pass`. It then runs your own test suite against every mutant in an isolated subprocess. A mutant your suite fails on is killed. A mutant your suite passes on survived, and that is a bug your tests would not catch. The mutation score is the share killed. Below your threshold, the merge check fails.

For each survivor, Claude drafts one test that should kill it. Before you see that test, our runner executes it twice: it must pass on the original and fail on the mutant. Only then is it labelled VERIFIED KILL. Otherwise it is REJECTED and queued for a human. The model never computes the score, never marks a mutant killed, and never edits the code under test.

### How we built it

- FastAPI + SQLAlchemy + Postgres. Structured JSON logs, an `llm_call` table with tokens, cost and latency per request.
- Mutation engine on Python `ast`, 9 operators. Diff scoper maps unified-diff line ranges to `FunctionDef` nodes.
- Runner copies a worktree per mutant, runs `pytest -x -q` with an 8-second timeout across 8 workers, and reads the exit code. Timeouts stay in the denominator and never count as kills.
- Server-Sent Events push each verdict to a Next.js run view where tiles flip green, red or grey as they land.
- Gate policy produces a GitHub Checks payload and a TMMi-style evidence PDF with a SHA-256 over every verdict.
- Claude Sonnet via OpenRouter with a strict JSON schema for `propose_test`. A proposal citing a mutant id not in the run is rejected before execution.
- Three seeded demo repos: an AI-tested billing module, an auth module with 59% coverage but better tests, and a vendored real OSS package (inflection 0.5.1, MIT).

### Challenges

Getting the score to mean something. Timeouts are the obvious way to inflate mutation scores, so they are excluded from kills by design. Making the diff scoper the product: full-repo mutation takes hours; scoping to touched functions makes it seconds and makes it a PR gate rather than a CLI. Keeping the model honest: on the demo repo the verification loop accepted 9 of 10 Claude proposals and rejected one that failed on the original code, meaning the model had encoded a wrong expectation as a test. That rejection is the product working.

### Accomplishments

The product refuses its own AI output on camera. Coverage 100%, mutation 63%, 10 survivors surfaced with the exact line and operator, on a live system.

### What we learned

Success-case appeal is not the same as expected value. We picked the idea whose demo cannot fail over the idea whose demo would be flashiest.

### What's next

GitHub App with real Checks API, JavaScript/TypeScript operators, Slack alerts, and self-hosted runners for private code.

## 2. 영상 대본 (2:45, 라이브 60% 이상)

| 시각 | 화면 | 대사 |
| --- | --- | --- |
| 0:00–0:12 | 터미널 `40 passed` + `Coverage: 100%`, 위로 빨간 카드 | Forty tests. One hundred percent coverage. I flipped one character in the payment logic and every single one of them still passed. |
| 0:12–0:22 | 얼굴 10초 | I'm Hajin. The world doesn't need another AI demo. In 2026 about a quarter of merged commits carry AI traces, and the one number we use to gate releases doesn't move when the tests get worse. |
| 0:22–0:35 | killscore.hajin.xyz 랜딩, demo/billing-api 클릭 | This is live at killscore dot hajin dot xyz right now. Nothing here is pre-rendered. KillScore takes the diff, finds only the functions this PR touched, and mutates them. |
| 0:35–1:15 | 타일 실시간 뒤집힘 | Twenty-seven mutants. Coverage stays at a hundred. Mutation score lands at sixty-three. Ten bugs your tests would let through. |
| 1:15–1:35 | 생존자 상세, diff 풀스크린 | Here's the one that matters. This is the boundary in the tier check. We changed it, and forty tests still passed. No model decided that. A subprocess ran your suite and read the exit code. |
| 1:35–1:50 | Propose a test → VERIFIED KILL | Now Claude writes a test for it. Before you ever see that test, our runner proves two things: it passes on the original, and it fails on the mutant. Verified kill. |
| 1:50–2:10 | billing-api 생존자 `calculate_invoice L47 0→1`의 REJECTED 배지 · auth-tokens 회색 TIMEOUT 타일 | Let me show you it failing. Here the model's test fails on the original. It encoded a wrong expectation, exactly the failure mode we're gating. Rejected, queued for a human. And this one timed out. A timeout is not a kill. Counting it as one would inflate our own score. |
| 2:10–2:28 | README 아키텍처 다이어그램 | Six components. Exactly one is a model call, and its output never touches the score. Seven seconds a run, four cents when you ask for a test. |
| 2:28–2:38 | /evals 표 | Twenty repos with twenty bugs I planted. The AI-written suite caught six. KillScore surfaced nineteen. Coverage never moved. |
| 2:38–2:45 | /gate 배지 + /pricing | Free on public repos. Ninety-nine dollars a month for the release engineer who has to press merge. |

규칙: 자막 필수. "not pre-rendered"를 입으로 말할 것. 슬라이드는 아키텍처 1장만.

촬영 전 준비: billing-api 최신 런의 생존자 10개에 이미 제안이 붙어 있음(VERIFIED 9 · REJECTED 1, `calculate_invoice` L47). 런을 새로 돌리면 제안이 없는 새 런이 생기니 촬영은 기존 런 URL로 할 것. auth-tokens 런의 next_free_slot 타일이 회색인지 확인.

## 3. 덱 10장

| # | 제목 | 내용 |
| --- | --- | --- |
| 1 | KillScore, the SaaS release gate for AI-written tests | 훅 문장 한 줄 |
| 2 | The number you gate on cannot see this | Coverage 100% vs Mutation 63% 카드 |
| 3 | Why AI-written tests fail silently | 구현 파생 테스트는 구현과 다툴 수 없다 |
| 4 | The person who presses merge | QA 리드·릴리스 엔지니어. Codecov/SonarQube measure whether code ran. We measure whether tests can disprove it. |
| 5 | How it works | 다이어그램 6박스, LLM 점선 |
| 6 | Live demo | 스크린샷 3장 |
| 7 | Reviewer, not author | 금지 4문장 + 2단 검증 루프 |
| 8 | Evaluation | /evals 표 |
| 9 | Free / $99 / $399, priced per repo | 가격 3티어 |
| 10 | What's next | GitHub App · JS/TS · self-hosted runner |

## 4. 제출 전 체크리스트

- [ ] 시크릿 창에서 https://killscore.hajin.xyz 4개 페이지 열림
- [ ] `curl https://killscore-api.hajin.xyz/healthz` → db up
- [ ] YouTube 영상 공개(또는 일부 공개), Not for Kids
- [ ] 레포 public 전환 + push
- [ ] README 상단 링크 3개 클릭 확인
- [ ] Devpost 폼 저장 후 Submitted 배지 확인
