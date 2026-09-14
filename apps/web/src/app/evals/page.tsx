import { api } from "@/lib/api";

export const dynamic = "force-dynamic";

interface Results {
  generated_at?: string;
  rows: { metric: string; baseline: string; ablation: string; killscore: string; n: string }[];
  notes?: string[];
  bugs?: { id: string; category: string; baseline: boolean; ablation: boolean | null; killscore: boolean }[];
}

export default async function EvalsPage() {
  let r: Results | null = null;
  try {
    r = await api<Results>("/v1/evals");
  } catch {}
  return (
    <main className="mx-auto max-w-6xl px-4 py-8">
      <h1 className="mb-1 text-xl font-semibold">Evaluation</h1>
      <p className="mb-6 max-w-3xl text-sm text-zinc-500">
        20 copies of a billing module, each with one planted bug, each shipped with an AI-written suite at 100% line coverage.
        Baseline is that suite alone. Ablation is a model reading the code with no execution. KillScore is mutation testing with the same suite.
        Regenerate with <code className="font-mono">make eval</code>.
      </p>
      {!r && <p className="text-sm text-zinc-500">Results have not been generated yet.</p>}
      {r && (
        <>
          <div className="overflow-x-auto rounded-xl border border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
            <table className="w-full text-sm">
              <thead className="text-left text-xs uppercase tracking-wide text-zinc-500">
                <tr><th className="px-4 py-2">Metric</th><th className="px-4 py-2 text-right">AI-written suite (baseline)</th><th className="px-4 py-2 text-right">LLM-only reviewer (ablation)</th><th className="px-4 py-2 text-right font-semibold text-zinc-900 dark:text-zinc-100">KillScore</th><th className="px-4 py-2 text-right">n</th></tr>
              </thead>
              <tbody>
                {r.rows.map((row) => (
                  <tr key={row.metric} className="border-t border-zinc-100 dark:border-zinc-800">
                    <td className="px-4 py-2">{row.metric}</td>
                    <td className="px-4 py-2 text-right font-mono">{row.baseline}</td>
                    <td className="px-4 py-2 text-right font-mono">{row.ablation}</td>
                    <td className="px-4 py-2 text-right font-mono font-semibold">{row.killscore}</td>
                    <td className="px-4 py-2 text-right font-mono text-zinc-500">{row.n}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          {r.bugs && (
            <details className="mt-6 text-sm">
              <summary className="cursor-pointer text-zinc-500">Per-bug breakdown ({r.bugs.length})</summary>
              <div className="mt-3 overflow-x-auto rounded-xl border border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
                <table className="w-full text-sm">
                  <thead className="text-left text-xs uppercase tracking-wide text-zinc-500"><tr><th className="px-4 py-2">Bug</th><th className="px-4 py-2">Category</th><th className="px-4 py-2">Baseline</th><th className="px-4 py-2">Ablation</th><th className="px-4 py-2">KillScore</th></tr></thead>
                  <tbody>
                    {r.bugs.map((b) => (
                      <tr key={b.id} className="border-t border-zinc-100 dark:border-zinc-800">
                        <td className="px-4 py-1.5 font-mono">{b.id}</td><td className="px-4 py-1.5">{b.category}</td>
                        <td className="px-4 py-1.5">{b.baseline ? "caught" : "missed"}</td><td className="px-4 py-1.5">{b.ablation == null ? "—" : b.ablation ? "caught" : "missed"}</td><td className="px-4 py-1.5 font-semibold">{b.killscore ? "caught" : "missed"}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </details>
          )}
          {r.notes && <ul className="mt-6 list-disc pl-5 text-xs text-zinc-500">{r.notes.map((n) => <li key={n}>{n}</li>)}</ul>}
          {r.generated_at && <p className="mt-4 text-xs text-zinc-400">Generated {r.generated_at}</p>}
        </>
      )}
    </main>
  );
}
