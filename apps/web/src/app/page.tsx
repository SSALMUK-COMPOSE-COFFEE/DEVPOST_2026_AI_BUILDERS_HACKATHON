import { api } from "@/lib/api";
import type { RepoPreset } from "@/lib/types";
import { StartRun } from "@/components/StartRun";

export const dynamic = "force-dynamic";

export default async function Home() {
  let presets: RepoPreset[] = [];
  try {
    presets = await api<RepoPreset[]>("/v1/repos");
  } catch {}

  return (
    <main className="mx-auto max-w-6xl px-4 py-12">
      <section className="mb-12 grid items-center gap-8 md:grid-cols-[1.2fr_1fr]">
        <div>
          <p className="mb-3 font-mono text-xs uppercase tracking-widest text-red-600">Release gate for AI-written tests</p>
          <h1 className="mb-4 text-4xl font-bold leading-tight tracking-tight md:text-5xl">
            100% coverage.<br />31% mutation score.
          </h1>
          <p className="max-w-xl text-lg text-zinc-600 dark:text-zinc-400">
            We flipped <code className="rounded bg-zinc-200 px-1 font-mono text-base dark:bg-zinc-800">&gt;</code> to{" "}
            <code className="rounded bg-zinc-200 px-1 font-mono text-base dark:bg-zinc-800">&gt;=</code> in your payment logic
            and all 47 tests still passed. KillScore mutates only the functions your pull request touched,
            re-runs your own suite against every mutant, and reports the percentage your tests actually killed.
          </p>
        </div>
        <div className="grid grid-cols-2 gap-3">
          <div className="rounded-xl border border-emerald-200 bg-emerald-50 p-5 dark:border-emerald-900 dark:bg-emerald-950/40">
            <p className="text-xs font-medium uppercase tracking-wide text-emerald-700 dark:text-emerald-400">Line coverage</p>
            <p className="mt-1 text-4xl font-bold text-emerald-700 dark:text-emerald-300">100%</p>
            <p className="mt-2 text-xs text-emerald-700/80 dark:text-emerald-400/80">Every line executed. Suite green.</p>
          </div>
          <div className="rounded-xl border border-red-200 bg-red-50 p-5 dark:border-red-900 dark:bg-red-950/40">
            <p className="text-xs font-medium uppercase tracking-wide text-red-700 dark:text-red-400">Mutation score</p>
            <p className="mt-1 text-4xl font-bold text-red-700 dark:text-red-300">31%</p>
            <p className="mt-2 text-xs text-red-700/80 dark:text-red-400/80">7 of 10 planted bugs went unnoticed.</p>
          </div>
        </div>
      </section>

      <StartRun presets={presets} />

      <section className="mt-16 grid gap-6 text-sm text-zinc-600 dark:text-zinc-400 md:grid-cols-3">
        <div>
          <h3 className="mb-1 font-semibold text-zinc-900 dark:text-zinc-100">Deterministic core</h3>
          AST mutation, isolated subprocess execution, exit-code verdicts. No model computes the score.
        </div>
        <div>
          <h3 className="mb-1 font-semibold text-zinc-900 dark:text-zinc-100">Diff-scoped</h3>
          Only functions touched by the PR are mutated. Hours of full-repo mutation become seconds.
        </div>
        <div>
          <h3 className="mb-1 font-semibold text-zinc-900 dark:text-zinc-100">Verified proposals</h3>
          Claude proposes a test for each survivor. You see it only after our runner proves it passes on the original and fails on the mutant.
        </div>
      </section>
    </main>
  );
}
