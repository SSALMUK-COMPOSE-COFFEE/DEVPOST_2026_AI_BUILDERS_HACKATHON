import Link from "next/link";
import { api } from "@/lib/api";
import type { MutantSummary } from "@/lib/types";
import { Badge } from "@/components/Badge";

export const dynamic = "force-dynamic";

export default async function MutantsPage({ params, searchParams }: { params: Promise<{ id: string }>; searchParams: Promise<{ status?: string }> }) {
  const { id } = await params;
  const { status } = await searchParams;
  const q = status ? `?status=${status}` : "";
  const mutants = await api<MutantSummary[]>(`/v1/runs/${id}/mutants${q}`);
  return (
    <main className="mx-auto max-w-6xl px-4 py-8">
      <div className="mb-1 text-sm text-zinc-500">
        <Link href={`/runs/${id}`} className="hover:underline">Run {id}</Link> / mutants
      </div>
      <div className="mb-6 flex items-center gap-4">
        <h1 className="text-xl font-semibold">{status ?? "all"} mutants <span className="text-zinc-400">({mutants.length})</span></h1>
        <nav className="flex gap-3 text-sm text-zinc-500">
          {["survived", "killed", "timeout", "error"].map((s) => (
            <Link key={s} href={`/runs/${id}/mutants?status=${s}`} className={s === status ? "font-semibold text-zinc-900 dark:text-zinc-100" : "hover:underline"}>{s}</Link>
          ))}
          <Link href={`/runs/${id}/mutants`} className={!status ? "font-semibold text-zinc-900 dark:text-zinc-100" : "hover:underline"}>all</Link>
        </nav>
      </div>
      <div className="overflow-x-auto rounded-xl border border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
        <table className="w-full text-sm">
          <thead className="text-left text-xs uppercase tracking-wide text-zinc-500">
            <tr><th className="px-4 py-2">Status</th><th className="px-4 py-2">Function</th><th className="px-4 py-2">Line</th><th className="px-4 py-2">Mutation</th><th className="px-4 py-2">Operator</th></tr>
          </thead>
          <tbody>
            {mutants.map((m) => (
              <tr key={m.id} className="border-t border-zinc-100 hover:bg-zinc-50 dark:border-zinc-800 dark:hover:bg-zinc-800/50">
                <td className="px-4 py-2"><Badge value={m.status} /></td>
                <td className="px-4 py-2 font-mono"><Link href={`/runs/${id}/mutants/${m.id}`} className="hover:underline">{m.function}</Link></td>
                <td className="px-4 py-2 font-mono text-zinc-500">{m.line}</td>
                <td className="px-4 py-2 font-mono">{m.description}</td>
                <td className="px-4 py-2 text-zinc-500">{m.operator}</td>
              </tr>
            ))}
            {mutants.length === 0 && <tr><td colSpan={5} className="px-4 py-8 text-center text-zinc-500">Nothing here.</td></tr>}
          </tbody>
        </table>
      </div>
    </main>
  );
}
