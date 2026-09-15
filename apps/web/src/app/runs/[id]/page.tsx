import Link from "next/link";
import { api } from "@/lib/api";
import type { MutantSummary, RunSummary, Target } from "@/lib/types";
import { RunLive } from "@/components/RunLive";

export const dynamic = "force-dynamic";

export default async function RunPage({ params, searchParams }: { params: Promise<{ id: string }>; searchParams: Promise<{ replay?: string }> }) {
  const { id } = await params;
  const { replay } = await searchParams;
  let run: (RunSummary & { targets: Target[] }) | null = null;
  let mutants: MutantSummary[] = [];
  try {
    run = await api<RunSummary & { targets: Target[] }>(`/v1/runs/${id}`);
    mutants = await api<MutantSummary[]>(`/v1/runs/${id}/mutants`);
  } catch {}

  if (!run) {
    return (
      <main className="mx-auto max-w-6xl px-4 py-16 text-center">
        <h1 className="mb-2 text-xl font-semibold">Run not available</h1>
        <p className="mb-6 text-sm text-zinc-500">
          No run named <span className="font-mono">{id}</span>, or the API is unreachable.
        </p>
        <Link href="/runs" className="text-sm text-zinc-500 underline hover:text-zinc-900 dark:hover:text-zinc-100">Back to all runs</Link>
      </main>
    );
  }

  return (
    <main className="mx-auto max-w-6xl px-4 py-8">
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <h1 className="text-xl font-semibold">
          Run <span className="font-mono text-zinc-500">{run.id}</span>
          {run.repo && <span className="ml-2 font-mono text-sm text-zinc-500">demo/{run.repo}</span>}
        </h1>
        <div className="flex gap-3 text-sm">
          <Link href={`/runs/${id}/mutants?status=survived`} className="text-zinc-500 hover:underline">Survivors</Link>
          {run.status === "done" && !replay && (
            <Link href={`/runs/${id}?replay=1`} className="text-zinc-500 hover:underline">Replay</Link>
          )}
        </div>
      </div>
      <RunLive initial={run} initialMutants={mutants} replay={replay === "1"} />
    </main>
  );
}
