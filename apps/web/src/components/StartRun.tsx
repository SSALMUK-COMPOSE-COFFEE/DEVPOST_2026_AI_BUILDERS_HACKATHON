"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { api } from "@/lib/api";
import type { RepoPreset } from "@/lib/types";

const SAMPLE_SOURCE = `def is_adult(age):
    return age >= 18

def discount(total, percent):
    if percent > 100:
        raise ValueError("bad percent")
    return total * (100 - percent) / 100
`;

const SAMPLE_TESTS = `def test_is_adult():
    assert is_adult(30)
    assert not is_adult(5)

def test_discount():
    assert discount(200, 50) == 100
`;

export function StartRun({ presets }: { presets: RepoPreset[] }) {
  const router = useRouter();
  const [busy, setBusy] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [source, setSource] = useState(SAMPLE_SOURCE);
  const [tests, setTests] = useState(SAMPLE_TESTS);

  async function start(body: Record<string, unknown>, label: string) {
    setBusy(label);
    setError(null);
    try {
      const run = await api<{ id: string }>("/v1/runs", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(body),
      });
      router.push(`/runs/${run.id}`);
    } catch (e) {
      setError(String(e));
      setBusy(null);
    }
  }

  return (
    <div className="grid gap-8 md:grid-cols-2">
      <section className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
        <h2 className="mb-1 font-semibold">Run a demo pull request</h2>
        <p className="mb-4 text-sm text-zinc-500">Diff-scoped. Only the functions the PR touched get mutated.</p>
        <div className="flex flex-col gap-2">
          {presets.length === 0 && <p className="text-sm text-zinc-500">API is not reachable. Presets will appear once it is.</p>}
          {presets.map((p) => (
            <button
              key={p.slug}
              disabled={busy !== null}
              onClick={() => start({ repo_preset: p.slug, diff_only: true }, p.slug)}
              className="flex items-center justify-between rounded-lg border border-zinc-200 px-4 py-3 text-left transition hover:border-zinc-400 disabled:opacity-50 dark:border-zinc-700 dark:hover:border-zinc-500"
            >
              <span>
                <span className="font-mono text-sm">demo/{p.slug}</span>
                <span className="block text-xs text-zinc-500">{p.description}</span>
              </span>
              <span className="text-sm text-zinc-400">{busy === p.slug ? "starting…" : "Run →"}</span>
            </button>
          ))}
        </div>
      </section>

      <section className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
        <h2 className="mb-1 font-semibold">Or paste a function and its tests</h2>
        <p className="mb-4 text-sm text-zinc-500">No login. Runs in an isolated subprocess, 8 s per mutant.</p>
        <label className="mb-1 block text-xs font-medium text-zinc-500">mod.py</label>
        <textarea value={source} onChange={(e) => setSource(e.target.value)} rows={7} spellCheck={false}
          className="mb-3 w-full rounded-md border border-zinc-200 bg-zinc-50 p-2 font-mono text-xs dark:border-zinc-700 dark:bg-zinc-950" />
        <label className="mb-1 block text-xs font-medium text-zinc-500">tests/test_mod.py</label>
        <textarea value={tests} onChange={(e) => setTests(e.target.value)} rows={6} spellCheck={false}
          className="mb-3 w-full rounded-md border border-zinc-200 bg-zinc-50 p-2 font-mono text-xs dark:border-zinc-700 dark:bg-zinc-950" />
        <button
          disabled={busy !== null}
          onClick={() => start({ inline_source: source, inline_tests: tests }, "inline")}
          className="rounded-md bg-zinc-900 px-4 py-2 text-sm font-medium text-white hover:bg-zinc-700 disabled:opacity-50 dark:bg-zinc-100 dark:text-zinc-900"
        >
          {busy === "inline" ? "starting…" : "Mutate and score"}
        </button>
        {error && <p className="mt-3 text-sm text-red-600">{error}</p>}
      </section>
    </div>
  );
}
