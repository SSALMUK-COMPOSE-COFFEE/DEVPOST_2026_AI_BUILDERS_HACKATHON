from datetime import datetime, timezone
from html import escape

from killscore.models import Mutant, Repo, Run

CSS = """
@page { size: A4; margin: 18mm; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 10.5pt; color: #111; }
h1 { font-size: 20pt; margin: 0 0 2mm; }
h2 { font-size: 12pt; margin: 8mm 0 2mm; border-bottom: 1px solid #ccc; padding-bottom: 1mm; }
.sub { color: #666; font-size: 9pt; }
.kpi { display: flex; gap: 6mm; margin: 5mm 0; }
.kpi div { border: 1px solid #ddd; border-radius: 3px; padding: 3mm 4mm; min-width: 30mm; }
.kpi b { display: block; font-size: 16pt; }
.pass { color: #0a7a3a; } .fail { color: #b3261e; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; }
th, td { border-bottom: 1px solid #e5e5e5; padding: 1.2mm 2mm; text-align: left; }
th { background: #f4f4f4; }
code { font-family: Menlo, monospace; font-size: 8.5pt; }
.foot { margin-top: 8mm; font-size: 8pt; color: #666; word-break: break-all; }
"""


def render_html(repo: Repo | None, run: Run, verdict: dict, mutants: list[Mutant], sha256: str) -> str:
    survivors = [m for m in mutants if m.status == "survived"]
    status = "PASS" if verdict["passed"] else "FAIL"
    cls = "pass" if verdict["passed"] else "fail"
    rows = "".join(
        f"<tr><td><code>{escape(m.file)}</code></td><td><code>{escape(m.function)}</code></td><td>{m.line}</td><td><code>{escape(m.description)}</code></td><td>{escape(m.operator)}</td></tr>"
        for m in survivors
    )
    cov = f"{run.line_coverage:.0%}" if run.line_coverage is not None else "n/a"
    score = f"{(run.mutation_score or 0):.0%}"
    return f"""<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<h1>KillScore evidence record</h1>
<p class="sub">Repository <b>{escape(repo.slug if repo else 'playground')}</b> · run <code>{run.id}</code> · generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}</p>
<div class="kpi">
  <div><span>Gate</span><b class="{cls}">{status}</b></div>
  <div><span>Mutation score</span><b>{score}</b></div>
  <div><span>Line coverage</span><b>{cov}</b></div>
  <div><span>Mutants</span><b>{run.total}</b></div>
  <div><span>Survived</span><b>{run.survived}</b></div>
</div>
<h2>1. Test process (TMMi PA 2.4 / 3.4 mapping)</h2>
<p>Diff-scoped mutation testing was executed against the functions changed in the pull request. Each mutant was executed in an isolated subprocess with an {8}-second timeout. A mutant is <i>killed</i> when the existing suite exits non-zero, <i>survived</i> when the suite passes, and <i>timeout</i> when it exceeds the limit. Timeouts are not counted as kills. Mutation score = killed / (total − error).</p>
<h2>2. Gate policy</h2>
<p>Minimum mutation score: <b>{verdict['min_score']:.0%}</b>. Maximum surviving mutants in critical paths: <b>{verdict.get('max_survivors', 0)}</b>. Critical paths: <code>{escape(', '.join(verdict['critical_paths']) or '—')}</code>.</p>
<p>Verdict: <b class="{cls}">{status}</b>{(' — ' + escape('; '.join(verdict['reasons']))) if verdict['reasons'] else ''}</p>
<h2>3. Surviving mutants ({len(survivors)})</h2>
<table><thead><tr><th>File</th><th>Function</th><th>Line</th><th>Mutation</th><th>Operator</th></tr></thead><tbody>{rows or '<tr><td colspan="5">None</td></tr>'}</tbody></table>
<h2>4. Execution summary</h2>
<table><tbody>
<tr><th>Baseline tests passed</th><td>{run.baseline_passed}</td></tr>
<tr><th>Killed / survived / timeout / error</th><td>{run.killed} / {run.survived} / {run.timeout} / {run.error}</td></tr>
<tr><th>Duration</th><td>{(run.duration_ms or 0) / 1000:.1f} s</td></tr>
<tr><th>LLM calls</th><td>Model output never contributed to the score. Proposed tests were verified by execution before display.</td></tr>
<tr><th>Started / finished</th><td>{run.created_at:%Y-%m-%d %H:%M:%S} UTC / {run.finished_at:%Y-%m-%d %H:%M:%S} UTC</td></tr>
</tbody></table>
<p class="foot">Evidence hash (SHA-256 over run id, timestamps, counts, verdict and every mutant verdict): <code>{sha256}</code></p>
</body></html>"""


def render_pdf(html: str) -> bytes:
    from weasyprint import HTML

    return HTML(string=html).write_pdf()
