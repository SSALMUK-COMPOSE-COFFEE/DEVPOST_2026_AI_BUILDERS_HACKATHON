.PHONY: up down logs api-test seed eval eval-fast

up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f api web

api-test:
	cd apps/api && uv run pytest -q

seed:
	docker compose exec api python -m killscore.seed

eval:
	cd apps/api && set -a && . ../../.env && set +a && PYTHONPATH=../.. uv run python -m evals.run

eval-fast:
	cd apps/api && PYTHONPATH=../.. uv run python -m evals.run --no-llm
