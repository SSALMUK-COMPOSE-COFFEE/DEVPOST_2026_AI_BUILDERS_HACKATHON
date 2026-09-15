# QA 점검 (2026-09-15)

제출 직전 최종 점검. 실제 결함만 고쳤고, 기능 추가는 하지 않았다.

## 고친 것

**apps/web**

- `src/app/runs/[id]/page.tsx` · `runs/[id]/mutants/page.tsx` · `runs/[id]/mutants/[k]/page.tsx`
  API fetch에 try/catch가 없어, 없는 run id를 열거나 API가 죽으면 서버 컴포넌트가
  그대로 터져 500이 떴다. 이제 "Run not available / Mutants not available /
  Mutant not available" 안내와 되돌아가기 링크를 보여준다.
- `src/components/RunLive.tsx` — Replay 카운터 중복 집계.
  `initial`에 이미 killed/survived가 채워진 상태에서 replay의 `mutant` 이벤트가
  다시 증가시켜 Progress가 `78 / 39`처럼 두 배로 찍혔다. `snapshot` 핸들러가
  뮤턴트 상태로 카운터를 다시 계산하도록 바꿔, replay는 0에서 시작한다.
- `src/components/RunLive.tsx` — 렌더 중 `Date.now()` 호출 (`react-hooks/purity` lint 에러).
  `useRef<number | null>(null)`로 바꾸고 effect에서 초기화.
- `src/components/GatePanel.tsx` — effect 본문에서 동기 `setState`
  (`react-hooks/set-state-in-effect` lint 에러). `setError(null)`을 성공 콜백으로 이동.
  겸사겸사 에러 문구를 `Error: 404 ...` 원문 대신 사람이 읽을 문장으로 바꿨다.
- `src/components/Badge.tsx` — 다크 모드에서 `pending` / `queued` 뱃지 글자가
  `zinc-800` 배경 위 `zinc-500/600`이라 거의 안 읽혔다. `timeout` 뱃지와 맞춰
  `dark:text-` 추가.
- `src/app/page.tsx` — API 불통 시 쓰는 히어로 폴백 수치가 옛날 값(31% · 47 tests ·
  7/10)이라 README 헤드라인(100% / 63% / 40 tests)과 어긋났다. 63% · 40 · 14/39로 정정.
  API가 살아 있으면 지금도 최신 billing-api 런에서 동적으로 가져온다.

**apps/api**

- `killscore/broker.py` — SSE 구독자 맵이 계속 자랐다. `_subs`가 defaultdict라
  `publish`가 구독자 없는 run id마다 빈 리스트를 만들고, `unsubscribe`는 빈 리스트를
  지우지 않았다. `publish`는 `.get()`으로, `unsubscribe`는 비면 키 삭제로 바꿨다.

## 확인만 하고 둔 것

- `runner.py` `execute_one` — pytest 종료 코드 2/3/4/5를 `error`로 처리하고
  분모에서 제외하는 것은 의도대로다(README에 명시). 그대로 둔다.
  `timeout`은 분모에 남고 분자에 안 들어가는 것도 의도대로.
- `routes_runs.py` SSE 제너레이터 — `finally: broker.unsubscribe(...)`가 있어
  클라이언트가 중간에 끊어도 구독은 해제된다. 누수 없음.
- `service.py` `create_inline_repo` — `runs_root / run_id`이고 `run_id`는 서버가 만든
  uuid4 hex 12자라 경로 이탈 여지가 없다. 사용자 소스는 `mod.py`,
  테스트는 `tests/test_mod.py`로만 쓰인다. 뮤턴트 타임아웃
  (`settings.mutant_timeout_sec`, 8초)은 인라인 런에도 그대로 적용된다.
  플레이그라운드 특성상 임의 코드 실행 자체는 설계된 동작.
- 다크 모드 — `bg-white` / `bg-zinc-50` / `text-zinc-900` 등 하드코딩된 밝은 클래스
  전체를 스캔했고, 같은 줄에 `dark:` 짝이 다 있었다. 위 Badge 두 건만 예외였다.
- 모바일(400px) — `/gate`는 테이블이 없고 그리드가 세로로 쌓인다.
  `/runs/[id]/mutants`, `/runs`, `/evals` 테이블은 모두 `overflow-x-auto` 컨테이너 안이다.

## 안 한 것

- `GET /v1/runs/{id}/survivors` 편의 엔드포인트 — 기능 추가라 하지 않았다.
  `/v1/runs/{id}/mutants?status=survived`로 이미 된다.
- 인라인 런의 `runs_root` 디렉터리는 런이 끝나도 지워지지 않아 디스크가 조금씩 는다.
  데모 범위에서는 문제 없어 그대로 둔다.

## 검사 결과

- `apps/web`: `npx tsc --noEmit` 통과 · `npm run lint` 0 errors (고치기 전 2 errors)
- `apps/api`: `uv run pytest -q` 20 passed
