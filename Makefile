.PHONY: up down logs api-test seed eval

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
	cd apps/api && uv run python -m evals.run
