# 확정안 대비 달라진 점

`FINAL_DECISION.md` 5장 빌드 브리프와 실제 구현의 차이. 2026-09-15 기준.

| 항목 | 계획 | 실제 | 이유 |
| --- | --- | --- | --- |
| LLM 경로 | Anthropic SDK, claude-opus-5 | OpenRouter OpenAI 호환 API, anthropic/claude-sonnet-5 | Anthropic 키 없음. OpenRouter 키만 있음. 호출당 약 $0.02, 15초 |
| DB | Neon | docker compose 안 Postgres 16 | Neon 계정 없음. 배포가 단일 머신이라 불필요 |
| 결제 | Stripe Pricing Table test mode | 정적 3티어 카드, "Billing integration is not live yet" 문구 | Stripe는 한국 거주자 계정 개설 불가 |
| 히어로 수치 | 커버리지 100% / 뮤테이션 31% / 47 tests | 100% / 63% / 40 tests, 최신 billing-api 런에서 동적 표시 | 구현 파생 테스트 40개로도 63% 아래로는 안 내려감. 더 내리면 테스트가 아무것도 검증하지 않아 가짜처럼 보임 |
| 러너 네트워크 차단 | 격리 | 미적용. `unshare -rn`이 이 머신과 컨테이너 모두에서 불허 | 데모 영향 없음. 러너 전용 컨테이너 `network_mode: none`으로 후속 |
| 인증 | `?demo=1` 우회 | 인증 자체 없음. 단일 데모 org | 심사 항목 아님 |
| name_cluster | 생존자 묶음 이름 붙이기 | 미구현 | 시간. 검증 루프가 더 중요 |
| API 도메인 | api.killscore.hajin.xyz | killscore-api.hajin.xyz | 와일드카드 인증서가 한 단계 서브도메인만 커버 |
| 호스트 포트 | 3000 / 8000 | 18093 / 18094 (127.0.0.1) | 같은 머신의 다른 프로젝트와 충돌 |
| PDF | WeasyPrint | WeasyPrint. 컨테이너에 pango 설치 | 계획대로 |
| 시간표 | 17:30 시작, 22:30 고/노고 | 21:40 KST 시작. 고/노고 기준 3개 모두 통과(뮤턴트 39개, 7초, 결제 경로 생존자 11개) | 세션 시작이 늦음 |
