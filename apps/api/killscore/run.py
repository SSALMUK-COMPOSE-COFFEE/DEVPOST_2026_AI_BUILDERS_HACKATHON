import sys
import time
from pathlib import Path

from killscore.runner import run
from killscore.settings import settings

COLORS = {"killed": "\033[32m", "survived": "\033[31m", "timeout": "\033[90m", "error": "\033[33m"}
RESET = "\033[0m"


def main(argv: list[str]) -> int:
    if len(argv) < 1:
        print("usage: python -m killscore.run <repo-path>")
        return 2
    repo = Path(argv[0])
    started = time.monotonic()

    def on_event(kind: str, data: dict):
        if kind == "baseline":
            cov = data["line_coverage"]
            print(f"baseline: {data['passed']} passed, line coverage {cov:.0%}" if cov is not None else f"baseline: {data['passed']} passed")
        elif kind == "mutants":
            print(f"generated {data['total']} mutants")
        elif kind == "mutant":
            c = COLORS[data["verdict"]]
            print(f"  {c}{data['verdict']:<8}{RESET} {data['id']}  ({data['duration_ms']} ms)")

    result = run(repo, workers=settings.runner_workers, timeout=settings.mutant_timeout_sec, on_event=on_event)
    elapsed = time.monotonic() - started
    print()
    print(f"mutation score {result.score:.0%} ({result.killed}/{result.total - result.error} killed, {result.survived} survived, {result.timeout} timeout, {result.error} error) in {elapsed:.1f}s")
    survivors = [m for m in result.mutants if any(e.mutant_id == m.id and e.verdict == "survived" for e in result.executions)]
    if survivors:
        print()
        print("survivors:")
        for m in survivors:
            print(f"  {m.id:<40} line {m.line:<4} {m.description}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
