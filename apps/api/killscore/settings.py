from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://killscore:killscore@localhost:5432/killscore"
    openrouter_api_key: str = ""
    openrouter_model: str = "anthropic/claude-sonnet-5"
    runner_workers: int = 8
    mutant_timeout_sec: int = 8
    demo_root: str = "demo"
    runs_root: str = "/tmp/killscore-runs"
    evals_results: str = "evals/out/results.json"
    log_json: bool = True


settings = Settings()
