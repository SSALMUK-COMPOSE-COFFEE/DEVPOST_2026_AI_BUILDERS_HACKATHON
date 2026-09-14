import Link from "next/link";
import { api } from "@/lib/api";
import { ms, pct } from "@/lib/format";
import type { RunSummary } from "@/lib/types";
import { Badge } from "@/components/Badge";

export const dynamic = "force-dynamic";

export default async function RunsPage() {
  let runs: RunSummary[] = [];
  try {
    runs = await api<RunSummary[]>("/v1/runs?limit=50");
  } catch {}
  return (
    <main className="mx-auto max-w-6xl px-4 py-8">
      <h1 className="mb-6 text-xl font-semibold">Runs</h1>
      <div className="overflow-x-auto rounded-xl border border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
        <table className="w-full text-sm">
          <thead className="text-left text-xs uppercase tracking-wide text-zinc-500">
            <tr>
              <th className="px-4 py-2">Run</th><th className="px-4 py-2">Repo</th><th className="px-4 py-2">Status</th>
              <th className="px-4 py-2 text-right">Coverage</th><th className="px-4 py-2 text-right">Mutation</th>
              <th className="px-4 py-2 text-right">Survived</th><th className="px-4 py-2 text-right">Duration</th><th className="px-4 py-2">Started</th>
            </tr>
          </thead>
          <tbody>
            {runs.map((r) => (
              <tr key={r.id} className="border-t border-zinc-100 hover:bg-zinc-50 dark:border-zinc-800 dark:hover:bg-zinc-800/50">
                <td className="px-4 py-2 font-mono"><Link href={`/runs/${r.id}`} className="hover:underline">{r.id}</Link></td>
                <td className="px-4 py-2 font-mono text-zinc-500">{r.repo ? `demo/${r.repo}` : "playground"}</td>
                <td className="px-4 py-2"><Badge value={r.status} /></td>
                <td className="px-4 py-2 text-right font-mono">{pct(r.line_coverage)}</td>
                <td className={`px-4 py-2 text-right font-mono ${r.mutation_score != null && r.mutation_score < 0.6 ? "text-red-600" : ""}`}>{pct(r.mutation_score)}</td>
                <td className="px-4 py-2 text-right font-mono">{r.survived} / {r.total}</td>
                <td className="px-4 py-2 text-right font-mono">{ms(r.duration_ms)}</td>
                <td className="px-4 py-2 text-zinc-500">{r.created_at ? new Date(r.created_at).toLocaleString() : ""}</td>
              </tr>
            ))}
            {runs.length === 0 && <tr><td colSpan={8} className="px-4 py-8 text-center text-zinc-500">No runs yet. Start one from the home page.</td></tr>}
          </tbody>
        </table>
      </div>
    </main>
  );
}
