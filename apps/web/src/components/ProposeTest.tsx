"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { api } from "@/lib/api";
import type { MutantDetail, Proposal } from "@/lib/types";
import { Badge } from "@/components/Badge";

export function ProposeTest({ mutant }: { mutant: MutantDetail }) {
  const router = useRouter();
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [live, setLive] = useState<Proposal | null>(null);
  const proposals = live ? [live, ...mutant.proposals.filter((p) => p.id !== live.id)] : mutant.proposals;

  async function propose() {
    setBusy(true);
    setError(null);
    try {
      const p = await api<Proposal>(`/v1/mutants/${mutant.id}/propose-test`, { method: "POST" });
      setLive(p);
      router.refresh();
    } catch (e) {
      setError(String(e));
    } finally {
      setBusy(false);
    }
  }

  if (mutant.status !== "survived") return null;

  return (
    <section className="mt-10">
      <div className="mb-3 flex items-center justify-between">
        <h2 className="font-semibold">Propose a test that kills this mutant</h2>
        <button
          onClick={propose}
          disabled={busy}
          className="rounded-md bg-zinc-900 px-4 py-2 text-sm font-medium text-white hover:bg-zinc-700 disabled:opacity-50 dark:bg-zinc-100 dark:text-zinc-900"
        >
          {busy ? "Claude drafting → runner verifying…" : "Propose a test"}
        </button>
      </div>
      <p className="mb-4 text-xs text-zinc-500">
        The model never computes the score. The model never marks a mutant killed. The model never edits the code under test.
        A proposed test is shown only after our runner proves it passes on the original and fails on the mutant.
      </p>
      {error && <p className="mb-3 text-sm text-red-600">{error}</p>}
      {proposals.map((p) => (
        <div
          key={p.id}
          className={`mb-4 rounded-xl border p-4 ${
            p.verdict === "verified_kill"
              ? "border-emerald-300 bg-emerald-50 dark:border-emerald-800 dark:bg-emerald-950/30"
              : p.verdict === "rejected"
                ? "border-red-300 bg-red-50 dark:border-red-800 dark:bg-red-950/30"
                : "border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900"
          }`}
        >
          <div className="mb-2 flex flex-wrap items-center gap-3">
            <Badge value={p.verdict} />
            <span className="font-mono text-sm">{p.test_name}</span>
            <span className="ml-auto text-xs text-zinc-500">
              original exit {p.original_exit ?? "?"} · mutant exit {p.mutant_exit ?? "?"}
            </span>
          </div>
          {p.verdict === "rejected" && (
            <p className="mb-2 text-sm font-medium text-red-700 dark:text-red-300">
              REJECTED — proposed test passes on both. It does not kill this mutant. Escalated to human review.
            </p>
          )}
          {p.verdict === "verified_kill" && (
            <p className="mb-2 text-sm font-medium text-emerald-700 dark:text-emerald-300">
              VERIFIED KILL — passes on the original, fails on the mutant. Safe to add to your suite.
            </p>
          )}
          {p.rationale && <p className="mb-2 text-sm text-zinc-600 dark:text-zinc-400">{p.rationale}</p>}
          <pre className="overflow-x-auto rounded-lg bg-zinc-900 p-3 text-xs text-zinc-100">{p.source}</pre>
        </div>
      ))}
    </section>
  );
}
