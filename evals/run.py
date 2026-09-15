import argparse
import json
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from killscore.runner import IGNORE, _pytest, run as mutation_run

from evals.gen import generate, load_bugs

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"

FAMILIES = {
    "tier_boundary": {"compare", "int_const"},
    "ge_to_gt": {"compare"},
    "rounding": {"compare", "int_const", "return_none", "negate_if"},
    "and_or": {"boolop"},
    "none_check": {"negate_if", "compare", "return_none"},
    "early_return_inversion": {"negate_if", "return_none", "bool_const"},
    "date_window": {"compare", "int_const"},
    "wrong_default": {"compare", "int_const", "bool_const"},
    "exception_swallow": {"swallow_except", "return_none"},
}

ABLATION_SCHEMA = {
    "type": "object",
    "properties": {
        "has_bug": {"type": "boolean"},
        "location": {"type": "string"},
        "explanation": {"type": "string"},
    },
    "required": ["has_bug", "location", "explanation"],
    "additionalProperties": False,
}

ABLATION_SYSTEM = """You are a senior code reviewer. You are shown a Python billing module and its test suite, which passes with 100% line coverage.
Decide whether the module contains a logic bug that the tests fail to catch. If yes, name the function that contains it in `location`.
Be precise: only report has_bug=true when you can point at a specific incorrect line."""


def baseline_catches(repo: Path) -> bool:
    proc = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"], cwd=repo, capture_output=True, text=True, timeout=60)
    return proc.returncode != 0


def killscore_run(repo: Path, bug: dict) -> dict:
    started = time.monotonic()
    scope = {"billing.py": {bug["function"]}}
    caught_by_suite = False
    try:
        result = mutation_run(repo, only_functions=scope, workers=8, timeout=8)
    except RuntimeError:
        caught_by_suite = True
        result = mutation_run(ROOT / "fixtures", only_functions=scope, workers=8, timeout=8)
    elapsed_ms = int((time.monotonic() - started) * 1000)
    verdict = {e.mutant_id: e.verdict for e in result.executions}
    survivors = [m for m in result.mutants if verdict.get(m.id) == "survived"]
    in_function = [m for m in survivors if m.function == bug["function"]]
    family = FAMILIES[bug["category"]]
    matched = [m for m in in_function if m.operator in family]
    return {
        "detected": caught_by_suite or bool(matched),
        "caught_by_suite": caught_by_suite,
        "any_survivor_in_function": bool(in_function),
        "total": result.total,
        "killed": result.killed,
        "survived": result.survived,
        "timeout": result.timeout,
        "error": result.error,
        "score": result.score,
        "line_coverage": result.line_coverage,
        "duration_ms": elapsed_ms,
        "survivors_in_function": [f"{m.id} {m.description}" for m in in_function],
    }


def ablation(repo: Path, bug: dict, cache: dict) -> dict:
    if bug["id"] in cache:
        return cache[bug["id"]]
    from killscore.llm import LLMError, chat_json

    module = (repo / "billing.py").read_text()
    tests = (repo / "tests" / "test_billing.py").read_text()
    user = f"=== billing.py ===\n{module}\n\n=== tests/test_billing.py ===\n{tests}\n"
    try:
        res = chat_json(ABLATION_SYSTEM, user, ABLATION_SCHEMA, "review", max_tokens=24000)
        content = res.content
        entry = {
            "has_bug": bool(content.get("has_bug")),
            "location": content.get("location", ""),
            "explanation": content.get("explanation", ""),
            "cost_usd": res.cost_usd,
            "latency_ms": res.latency_ms,
            "detected": bool(content.get("has_bug")) and bug["function"] in content.get("location", ""),
        }
    except LLMError as exc:
        return {"has_bug": False, "location": "", "explanation": f"error: {exc}", "cost_usd": 0.0, "latency_ms": 0, "detected": False}
    cache[bug["id"]] = entry
    return entry


def _verify(test_code: str, original: str, mutated: str, index: int) -> tuple[int | None, int | None]:
    codes = []
    for module_source in (original, mutated):
        with tempfile.TemporaryDirectory(prefix="ks-eval-prop-") as tmp:
            work = Path(tmp) / "repo"
            shutil.copytree(ROOT / "fixtures", work, ignore=IGNORE)
            (work / "billing.py").write_text(module_source)
            (work / "tests" / f"test_proposed_{index}.py").write_text(test_code)
            code, _, _ = _pytest(work, 16, [f"tests/test_proposed_{index}.py"])
            codes.append(code)
    return codes[0], codes[1]


def proposals_stage(cap: int = 35) -> dict:
    from killscore.llm import LLMError, chat_json
    from killscore.proposals import SCHEMA, SYSTEM

    fixtures = ROOT / "fixtures"
    before = mutation_run(fixtures, workers=8, timeout=8)
    verdict = {e.mutant_id: e.verdict for e in before.executions}
    survivors = [m for m in before.mutants if verdict.get(m.id) == "survived"][:cap]
    original = (fixtures / "billing.py").read_text()
    tests = (fixtures / "tests" / "test_billing.py").read_text()
    cache_path = OUT / "proposals.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}

    def one(item):
        index, m = item
        if m.id in cache:
            return m.id, cache[m.id]
        user = (
            f"MUTANT ID: {m.id}\nFILE: billing.py\nFUNCTION: {m.function}\nMUTATION: {m.description}\n\n"
            f"=== ORIGINAL billing.py ===\n{original}\n\n=== MUTANT billing.py ===\n{m.source}\n\n"
            f"=== EXISTING TESTS ===\n# tests/test_billing.py\n{tests}\n"
        )
        entry = {"mutant": m.id, "function": m.function, "description": m.description}
        try:
            res = chat_json(SYSTEM, user, SCHEMA, "propose_test", max_tokens=16000)
            entry.update(cost_usd=res.cost_usd, latency_ms=res.latency_ms, test_name=res.content.get("test_name", ""), test_code=res.content.get("test_code", ""))
            if res.content.get("targets_mutant_id") != m.id:
                entry.update(verdict="rejected", reason="cited wrong mutant id")
            else:
                o, mu = _verify(entry["test_code"], original, m.source, index)
                entry.update(original_exit=o, mutant_exit=mu)
                entry["verdict"] = "verified_kill" if (o == 0 and mu == 1) else "rejected"
        except LLMError as exc:
            entry.update(verdict="error", reason=str(exc), cost_usd=0.0, latency_ms=0, test_code="")
        return m.id, entry

    with ThreadPoolExecutor(max_workers=4) as pool:
        for mid, entry in pool.map(one, list(enumerate(survivors))):
            cache[mid] = entry
            print(f"  proposal {mid:<40} {entry['verdict']}", flush=True)
    cache_path.write_text(json.dumps(cache, indent=2))

    after_dir = OUT / "fixtures_after"
    if after_dir.exists():
        shutil.rmtree(after_dir)
    shutil.copytree(fixtures, after_dir, ignore=IGNORE)
    verified = [e for e in cache.values() if e.get("verdict") == "verified_kill"]
    for i, e in enumerate(verified):
        (after_dir / "tests" / f"test_proposed_{i}.py").write_text(e["test_code"])
    after = mutation_run(after_dir, workers=8, timeout=8)
    proposed = [e for e in cache.values() if e.get("verdict") in {"verified_kill", "rejected"}]
    return {
        "before_score": before.score,
        "after_score": after.score,
        "before_total": before.total,
        "before_survived": before.survived,
        "after_survived": after.survived,
        "proposed": len(proposed),
        "verified": len(verified),
        "cost_usd": sum(e.get("cost_usd", 0.0) for e in cache.values()),
        "p50_latency_ms": sorted(e.get("latency_ms", 0) for e in proposed)[len(proposed) // 2] if proposed else None,
    }


def pct(v: float | None) -> str:
    return "—" if v is None else f"{round(v * 100)}%"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-llm", action="store_true")
    parser.add_argument("--no-propose", action="store_true")
    args = parser.parse_args()

    wall = time.monotonic()
    OUT.mkdir(exist_ok=True)
    repos = generate()
    bugs = load_bugs()
    cache_path = OUT / "ablation.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}

    rows = []
    for repo, bug in zip(repos, bugs):
        base = baseline_catches(repo)
        ks = killscore_run(repo, bug)
        abl = None if args.no_llm else ablation(repo, bug, cache)
        rows.append({"bug": bug, "baseline_detected": base, "killscore": ks, "ablation": abl})
        flag = lambda v: "✓" if v else "·"
        print(f"{bug['id']} {bug['category']:<24} baseline {flag(base)}  ablation {flag(abl['detected']) if abl else '-'}  killscore {flag(ks['detected'])}  score {pct(ks['score'])}  {ks['duration_ms']} ms", flush=True)
        if not args.no_llm:
            cache_path.write_text(json.dumps(cache, indent=2))

    n = len(rows)
    base_n = sum(r["baseline_detected"] for r in rows)
    ks_n = sum(r["killscore"]["detected"] for r in rows)
    abl_n = sum(r["ablation"]["detected"] for r in rows) if not args.no_llm else None
    total = sum(r["killscore"]["total"] for r in rows)
    killed = sum(r["killscore"]["killed"] for r in rows)
    errors = sum(r["killscore"]["error"] for r in rows)
    score = killed / (total - errors) if total - errors else 0.0
    coverage = statistics.mean(r["killscore"]["line_coverage"] or 0 for r in rows)
    durations = sorted(r["killscore"]["duration_ms"] for r in rows)
    p50 = durations[len(durations) // 2]
    p95 = durations[min(len(durations) - 1, int(len(durations) * 0.95))]
    abl_cost = statistics.mean(r["ablation"]["cost_usd"] for r in rows) if not args.no_llm else None
    abl_lat = sorted(r["ablation"]["latency_ms"] for r in rows) if not args.no_llm else None

    prop = None if (args.no_llm or args.no_propose) else proposals_stage()

    abl_col = lambda v: "—" if v is None else v
    abl_lat_str = None if abl_lat is None else f"{abl_lat[len(abl_lat)//2]/1000:.1f}s / {abl_lat[min(len(abl_lat)-1,int(len(abl_lat)*0.95))]/1000:.1f}s"
    if prop:
        score_ks = f"{pct(prop['before_score'])} → {pct(prop['after_score'])} after adding verified tests"
        score_base = pct(prop["before_score"])
        score_n = f"{prop['before_total']} mutants"
    else:
        score_ks = f"{pct(score)} reported, {sum(r['killscore']['survived'] for r in rows)} survivors surfaced"
        score_base = pct(score)
        score_n = f"{total} mutants"
    ks_cost = "$0.000 (deterministic)" if not prop else f"$0.000 scoring · ${prop['cost_usd'] / max(prop['proposed'], 1):.3f} per proposed test"
    metrics = [
        ("Planted bugs detected", f"{base_n} / {n}", abl_col(abl_n if abl_n is None else f"{abl_n} / {n}"), f"{ks_n} / {n}", str(n)),
        ("Mutation score", score_base, "—", score_ks, score_n),
        ("Line coverage", pct(coverage), "—", pct(coverage), "—"),
        ("Proposed tests verified", "—", "—", "—" if not prop else f"{pct(prop['verified'] / prop['proposed']) if prop['proposed'] else '—'} ({prop['verified']} / {prop['proposed']})", "—" if not prop else str(prop["proposed"])),
        ("Tests shown without proof", "—", "—", "0 (structurally impossible)", "—"),
        ("p50 / p95 per run", "—", abl_col(abl_lat_str), f"{p50/1000:.1f}s / {p95/1000:.1f}s", str(n)),
        ("LLM cost per run", "—", abl_col(None if abl_cost is None else f"${abl_cost:.3f}"), ks_cost, str(n)),
    ]
    table = ["| Metric | AI-written suite (baseline) | LLM-only reviewer (ablation) | KillScore | n |", "| --- | --- | --- | --- | --- |"]
    table += [f"| {m} | {b} | {a} | {k} | {nn} |" for m, b, a, k, nn in metrics]
    md = "\n".join(table)
    print()
    print(md)
    elapsed = time.monotonic() - wall
    print(f"\nwall time {elapsed:.0f}s")

    (OUT / "RESULTS.md").write_text(
        "# Eval results\n\n"
        f"20 planted bugs in `evals/fixtures/billing.py`, declared in `evals/fixtures/bugs.yaml`. "
        "Detection rule for KillScore: the buggy function has at least one surviving mutant whose operator family matches the bug category "
        "(see `FAMILIES` in `evals/run.py`). Baseline: the AI-written suite fails on the buggy repo. "
        "Ablation: the model is shown module + tests and must name the buggy function.\n\n"
        + md
        + f"\n\nGenerated by `make eval` in {elapsed:.0f}s.\n"
    )
    total_cost = (sum(r["ablation"]["cost_usd"] for r in rows) if not args.no_llm else 0.0) + (prop["cost_usd"] if prop else 0.0)
    print(f"total LLM cost ${total_cost:.3f}")
    (OUT / "results.json").write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "n": n,
        "baseline_detected": base_n,
        "ablation_detected": abl_n,
        "killscore_detected": ks_n,
        "killscore_any_survivor_in_function": sum(r["killscore"]["any_survivor_in_function"] for r in rows),
        "mutation_score": score,
        "total_mutants": total,
        "line_coverage": coverage,
        "p50_ms": p50,
        "p95_ms": p95,
        "ablation_cost_usd_per_run": abl_cost,
        "proposals": prop,
        "total_llm_cost_usd": total_cost,
        "wall_time_s": elapsed,
        "rows": [{"metric": m, "baseline": b, "ablation": a, "killscore": k, "n": nn} for m, b, a, k, nn in metrics],
        "bugs": [{"id": r["bug"]["id"], "category": r["bug"]["category"], "function": r["bug"]["function"], "description": r["bug"]["description"], "baseline": r["baseline_detected"], "ablation": None if r["ablation"] is None else r["ablation"]["detected"], "killscore": r["killscore"]["detected"]} for r in rows],
        "notes": [
            "Runs are diff-scoped to the function the planted bug touched, as a PR gate would be.",
            "KillScore detection: the suite is red (gate blocks) or the buggy function has a surviving mutant in the bug's operator family.",
            "Ablation: the model sees module + tests and must name the buggy function; scored by function name match.",
            "Mutation score after: verified proposed tests appended to the base fixture and the whole module re-scored.",
            "A timeout is never counted as a kill.",
        ],
        "details": rows,
    }, indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
