import json
import time
from dataclasses import dataclass

import httpx

from killscore.logging import get_logger
from killscore.settings import settings

log = get_logger("killscore.llm")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


@dataclass
class LLMResult:
    content: dict
    model: str
    input_tok: int
    output_tok: int
    cost_usd: float
    latency_ms: int


class LLMError(Exception):
    pass


def chat_json(system: str, user: str, schema: dict, purpose: str, max_tokens: int = 4000) -> LLMResult:
    if not settings.openrouter_api_key:
        raise LLMError("OPENROUTER_API_KEY is not set")
    body = {
        "model": settings.openrouter_model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "max_tokens": max_tokens,
        "temperature": 0.2,
        "response_format": {"type": "json_schema", "json_schema": {"name": purpose, "strict": True, "schema": schema}},
        "usage": {"include": True},
    }
    headers = {
        "Authorization": f"Bearer {settings.openrouter_api_key}",
        "HTTP-Referer": "https://killscore.hajin.xyz",
        "X-Title": "KillScore",
    }
    started = time.monotonic()
    with httpx.Client(timeout=90) as client:
        res = client.post(OPENROUTER_URL, json=body, headers=headers)
    latency = int((time.monotonic() - started) * 1000)
    if res.status_code != 200:
        log.error("llm_http_error", status=res.status_code, body=res.text[:300])
        raise LLMError(f"openrouter {res.status_code}: {res.text[:200]}")
    data = res.json()
    choice = data["choices"][0]
    text = choice["message"].get("content")
    if not text:
        log.error("llm_empty", finish=choice.get("finish_reason"), native=choice.get("native_finish_reason"), refusal=choice["message"].get("refusal"), raw=json.dumps(data)[:600])
        raise LLMError(f"model returned no content (finish_reason={choice.get('finish_reason')})")
    try:
        content = json.loads(_strip_fences(text))
    except json.JSONDecodeError as exc:
        raise LLMError(f"model returned non-JSON: {text[:200]}") from exc
    usage = data.get("usage", {})
    return LLMResult(
        content=content,
        model=data.get("model", settings.openrouter_model),
        input_tok=usage.get("prompt_tokens", 0),
        output_tok=usage.get("completion_tokens", 0),
        cost_usd=float(usage.get("cost", 0.0) or 0.0),
        latency_ms=latency,
    )


def _strip_fences(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[1] if "\n" in t else t[3:]
        if t.endswith("```"):
            t = t[:-3]
    return t.strip()
