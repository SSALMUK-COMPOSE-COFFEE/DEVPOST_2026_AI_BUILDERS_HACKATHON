"use client";

import { useEffect, useState } from "react";
import { API_URL, api } from "@/lib/api";
import { pct } from "@/lib/format";
import type { RepoPreset, RunSummary } from "@/lib/types";

interface Check {
  run: RunSummary;
  verdict: { passed: boolean; score: number; min_score: number; survivors: number; survivors_in_critical_paths: number; critical_paths: string[]; reasons: string[] };
  github_check: Record<string, unknown>;
}

export function GatePanel({ presets }: { presets: RepoPreset[] }) {
  const [slug, setSlug] = useState(presets[0]?.slug ?? "");
  const [minScore, setMinScore] = useState(0.6);
  const [paths, setPaths] = useState("billing/, auth/");
  const [check, setCheck] = useState<Check | null>(null);
  const [saved, setSaved] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!slug) return;
    api<{ min_score: number; critical_paths: string[] }>(`/v1/gate/${slug}/policy`)
      .then((p) => { setMinScore(p.min_score); setPaths(p.critical_paths.join(", ")); })
      .catch(() => {});
  }, [slug]);

  useEffect(() => {
    if (!slug) return;
    api<Check>(`/v1/gate/${slug}/check?min_score=${minScore}`)
      .then((c) => { setCheck(c); setError(null); })
      .catch(() => { setCheck(null); setError("API unreachable or no completed run for this repository yet."); });
  }, [slug, minScore]);

  async function save() {
    await api(`/v1/gate/${slug}/policy`, {
      method: "PUT",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ min_score: minScore, max_survivors_in_paths: 0, critical_paths: paths.split(",").map((s) => s.trim()).filter(Boolean) }),
    });
    setSaved(true);
    setTimeout(() => setSaved(false), 1500);
  }

  const v = check?.verdict;
  const badgeColor = v ? (v.passed ? "#16a34a" : "#dc2626") : "#71717a";
  const badgeText = v ? `mutation ${pct(v.score)} · ${v.passed ? "passing" : "failing"}` : "no run";

  return (
    <div className="grid gap-8 md:grid-cols-[1fr_1.2fr] [&>section]:min-w-0">
      <section className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
        <h2 className="mb-4 font-semibold">Policy</h2>
        <label className="mb-1 block text-xs font-medium text-zinc-500">Repository</label>
        <select value={slug} onChange={(e) => setSlug(e.target.value)} className="mb-4 w-full rounded-md border border-zinc-200 bg-zinc-50 p-2 text-sm dark:border-zinc-700 dark:bg-zinc-950">
          {presets.map((p) => <option key={p.slug} value={p.slug}>demo/{p.slug}</option>)}
        </select>
        <label className="mb-1 block text-xs font-medium text-zinc-500">Minimum mutation score: <span className="font-mono text-zinc-900 dark:text-zinc-100">{pct(minScore)}</span></label>
        <input type="range" min={0} max={1} step={0.05} value={minScore} onChange={(e) => setMinScore(Number(e.target.value))} className="mb-4 w-full accent-red-600" />
        <label className="mb-1 block text-xs font-medium text-zinc-500">Critical paths (no survivors allowed)</label>
        <input value={paths} onChange={(e) => setPaths(e.target.value)} className="mb-4 w-full rounded-md border border-zinc-200 bg-zinc-50 p-2 font-mono text-sm dark:border-zinc-700 dark:bg-zinc-950" />
        <button onClick={save} className="rounded-md bg-zinc-900 px-4 py-2 text-sm font-medium text-white hover:bg-zinc-700 dark:bg-zinc-100 dark:text-zinc-900">{saved ? "Saved" : "Save policy"}</button>

        <h2 className="mb-2 mt-8 font-semibold">PR badge preview</h2>
        <svg width="230" height="20" role="img" aria-label={badgeText}>
          <rect width="72" height="20" rx="3" fill="#3f3f46" />
          <rect x="72" width="158" height="20" rx="3" fill={badgeColor} />
          <rect x="72" width="6" height="20" fill={badgeColor} />
          <text x="36" y="14" fill="#fff" textAnchor="middle" fontSize="11" fontFamily="Verdana,sans-serif">KillScore</text>
          <text x="151" y="14" fill="#fff" textAnchor="middle" fontSize="11" fontFamily="Verdana,sans-serif">{badgeText}</text>
        </svg>

        {check && (
          <div className="mt-6">
            <a href={`${API_URL}/v1/runs/${check.run.id}/report.pdf`} className="inline-block rounded-md border border-zinc-300 px-4 py-2 text-sm hover:bg-zinc-100 dark:border-zinc-700 dark:hover:bg-zinc-800">
              Export TMMi evidence PDF
            </a>
            <p className="mt-2 text-xs text-zinc-500">SHA-256 over every mutant verdict is embedded in the document.</p>
          </div>
        )}
      </section>

      <section className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
        <h2 className="mb-1 font-semibold">GitHub Checks payload</h2>
        <p className="mb-3 text-xs text-zinc-500">What the merge button sees. Recomputed from the latest completed run.</p>
        {error && <p className="text-sm text-red-600">{error}</p>}
        {v && (
          <div className={`mb-3 rounded-lg p-3 text-sm font-medium ${v.passed ? "bg-emerald-50 text-emerald-800 dark:bg-emerald-950/40 dark:text-emerald-200" : "bg-red-50 text-red-800 dark:bg-red-950/40 dark:text-red-200"}`}>
            {v.passed ? "Gate passed" : `Gate failed: ${v.reasons.join("; ")}`}
          </div>
        )}
        <pre className="overflow-x-auto rounded-lg bg-zinc-900 p-3 text-xs text-zinc-100">{check ? JSON.stringify(check.github_check, null, 2) : "…"}</pre>
      </section>
    </div>
  );
}
