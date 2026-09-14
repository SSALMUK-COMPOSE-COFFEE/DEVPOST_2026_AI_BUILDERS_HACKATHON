import Link from "next/link";
import { api } from "@/lib/api";
import { ms } from "@/lib/format";
import type { MutantDetail, MutantSummary } from "@/lib/types";
import { Badge } from "@/components/Badge";
import { DiffView } from "@/components/DiffView";
import { ProposeTest } from "@/components/ProposeTest";

export const dynamic = "force-dynamic";

export default async function MutantPage({ params }: { params: Promise<{ id: string; k: string }> }) {
  const { id, k } = await params;
  const m = await api<MutantDetail>(`/v1/mutants/${k}`);
  const siblings = await api<MutantSummary[]>(`/v1/runs/${id}/mutants`, undefined);
  const survivors = siblings.filter((s) => s.status === "survived");
  const pos = survivors.findIndex((s) => s.id === k);
  const prev = pos > 0 ? survivors[pos - 1] : null;
  const next = pos >= 0 && pos < survivors.length - 1 ? survivors[pos + 1] : null;
  const exec = m.executions.find((e) => e.phase === "mutant");

  return (
    <main className="mx-auto max-w-6xl px-4 py-8">
      <div className="mb-1 text-sm text-zinc-500">
        <Link href={`/runs/${id}`} className="hover:underline">Run {id}</Link> / mutant
      </div>
      <div className="mb-6 flex flex-wrap items-center justify-between gap-3">
        <h1 className="font-mono text-lg">
          <span className="text-zinc-400">{m.file}::</span>{m.function}
          <span className="ml-3 text-sm text-zinc-500">line {m.line}</span>
        </h1>
        <div className="flex items-center gap-3">
          <Badge value={m.status} />
          {pos >= 0 && (
            <span className="text-sm text-zinc-500">
              survivor {pos + 1} / {survivors.length}
              {prev && <Link className="ml-3 hover:underline" href={`/runs/${id}/mutants/${prev.id}`}>← prev</Link>}
              {next && <Link className="ml-3 hover:underline" href={`/runs/${id}/mutants/${next.id}`}>next →</Link>}
            </span>
          )}
        </div>
      </div>

      {m.status === "survived" && (
        <div className="mb-6 rounded-xl border border-red-200 bg-red-50 p-5 dark:border-red-900 dark:bg-red-950/40">
          <p className="text-2xl font-bold text-red-700 dark:text-red-300">
            {m.run.baseline_passed} tests still passed.
          </p>
          <p className="mt-1 text-sm text-red-800/80 dark:text-red-300/80">
            We changed <code className="font-mono">{m.description}</code> in <code className="font-mono">{m.function}</code> and the suite did not notice.
            No model decided that. A subprocess ran your tests and read exit code {exec?.exit_code ?? "?"} in {ms(exec?.duration_ms)}.
          </p>
        </div>
      )}
      {m.status === "timeout" && (
        <div className="mb-6 rounded-xl border border-zinc-300 bg-zinc-100 p-5 dark:border-zinc-700 dark:bg-zinc-900">
          <p className="text-xl font-bold">Timed out after {ms(exec?.duration_ms)}.</p>
          <p className="mt-1 text-sm text-zinc-600 dark:text-zinc-400">A timeout is not a kill. Counting it as one would inflate our own score, so it stays in the denominator and out of the numerator.</p>
        </div>
      )}

      <h2 className="mb-2 text-sm font-semibold text-zinc-500">Original → mutant ({m.operator}: {m.description})</h2>
      <DiffView original={m.original_source} mutant={m.mutant_source} />

      {exec && (
        <details className="mt-4 text-sm">
          <summary className="cursor-pointer text-zinc-500">pytest output tail</summary>
          <pre className="mt-2 overflow-x-auto rounded-lg bg-zinc-900 p-3 text-xs text-zinc-100">{exec.stdout_tail || "(empty)"}</pre>
        </details>
      )}

      <ProposeTest mutant={m} />
    </main>
  );
}
