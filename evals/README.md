# evals

Twenty planted bugs, three columns, one command.

```
make eval            # full run: baseline + LLM ablation + KillScore + verified proposals
make eval-fast       # --no-llm: deterministic columns only, ~1 minute
```

- `fixtures/billing.py`: pure-Python billing module.
- `fixtures/tests/test_billing.py`: implementation-derived suite, 100% line and branch coverage, representative values only.
- `fixtures/bugs.yaml`: 20 bugs as exact string patches, 9 categories.
- `gen.py`: stamps out `out/repos/bug_XX/` with each patch applied.
- `run.py`: baseline (does the suite go red?), ablation (can the model name the buggy function?), KillScore (diff-scoped mutation run on the buggy function), then verified test proposals on the base fixture and a re-score.

Outputs land in `out/RESULTS.md` and `out/results.json`. LLM results are cached in `out/ablation.json` and `out/proposals.json`.
