"use client";

import Link from "next/link";
import { useEffect, useMemo, useRef, useState } from "react";
import { API_URL } from "@/lib/api";
import { ms, pct, usd } from "@/lib/format";
import type { MutantSummary, RunSummary, Target, Verdict } from "@/lib/types";

const TILE: Record<Verdict, string> = {
  pending: "bg-zinc-200 dark:bg-zinc-800",
  killed: "bg-emerald-500",
  survived: "bg-red-500",
  timeout: "bg-zinc-400 dark:bg-zinc-600",
  error: "bg-amber-400",
};

interface Props {
  initial: RunSummary & { targets: Target[] };
  initialMutants: MutantSummary[];
  replay: boolean;
}

export function RunLive({ initial, initialMutants, replay }: Props) {
  const [run, setRun] = useState<RunSummary>(initial);
  const [mutants, setMutants] = useState<MutantSummary[]>(initialMutants);
  const [flipped, setFlipped] = useState<Set<string>>(new Set());
  const [elapsed, setElapsed] = useState(0);
  const startedAt = useRef(Date.now());

  useEffect(() => {
    const live = replay || initial.status === "queued" || initial.status === "running";
    if (!live) return;
    const es = new EventSource(`${API_URL}/v1/runs/${initial.id}/events${replay ? "?replay=true" : ""}`);
    es.addEventListener("snapshot", (e) => {
      const d = JSON.parse((e as MessageEvent).data);
      setMutants(d.mutants);
      setRun((r) => ({ ...r, status: d.status, baseline_passed: d.baseline_passed, line_coverage: d.line_coverage, total: d.total }));
    });
    es.addEventListener("status", (e) => setRun((r) => ({ ...r, status: JSON.parse((e as MessageEvent).data).status })));
    es.addEventListener("baseline", (e) => {
      const d = JSON.parse((e as MessageEvent).data);
      setRun((r) => ({ ...r, baseline_passed: d.passed, line_coverage: d.line_coverage }));
    });
    es.addEventListener("mutants", (e) => {
      const d = JSON.parse((e as MessageEvent).data);
      setMutants(d.items.map((m: MutantSummary) => ({ ...m, status: "pending" as Verdict, cluster: null })));
      setRun((r) => ({ ...r, total: d.total }));
    });
    es.addEventListener("mutant", (e) => {
      const d = JSON.parse((e as MessageEvent).data);
      setMutants((ms) => ms.map((m) => (m.id === d.id ? { ...m, status: d.verdict } : m)));
      setFlipped((s) => new Set(s).add(d.id));
      setRun((r) => ({ ...r, [d.verdict]: (r[d.verdict as keyof RunSummary] as number) + 1 }));
    });
    es.addEventListener("done", (e) => {
      const d = JSON.parse((e as MessageEvent).data);
      setRun((r) => ({ ...r, ...d, status: "done" }));
      es.close();
    });
    es.addEventListener("failed", (e) => {
      const d = JSON.parse((e as MessageEvent).data);
      setRun((r) => ({ ...r, status: "failed", error_message: d.error }));
      es.close();
    });
    es.onerror = () => es.close();
    return () => es.close();
  }, [initial.id, initial.status, replay]);

  useEffect(() => {
    if (run.status === "done" || run.status === "failed") return;
    const t = setInterval(() => setElapsed(Date.now() - startedAt.current), 200);
    return () => clearInterval(t);
  }, [run.status]);

  const judged = run.killed + run.survived + run.timeout + run.error;
  const liveScore = useMemo(() => {
    const denom = judged - run.error;
    return denom > 0 ? run.killed / denom : null;
  }, [judged, run.killed, run.error]);
  const score = run.status === "done" ? run.mutation_score : liveScore;

  const groups = useMemo(() => {
    const g = new Map<string, MutantSummary[]>();
    for (const m of mutants) {
      const k = `${m.file}::${m.function}`;
      g.set(k, [...(g.get(k) ?? []), m]);
    }
    return [...g.entries()];
  }, [mutants]);

  return (
    <div>
      <div className="sticky top-0 z-10 -mx-4 mb-8 border-b border-zinc-200 bg-zinc-50/95 px-4 py-4 backdrop-blur dark:border-zinc-800 dark:bg-zinc-950/95">
        <div className="mx-auto grid max-w-6xl grid-cols-2 gap-4 md:grid-cols-6">
          <Stat label="Line coverage" value={pct(run.line_coverage)} tone="ok" />
          <Stat label="Mutation score" value={pct(score)} tone={score != null && score < 0.6 ? "bad" : "ok"} />
          <Stat label="Progress" value={`${judged} / ${run.total}`} />
          <Stat label="Elapsed" value={run.status === "done" ? ms(run.duration_ms) : ms(elapsed)} />
          <Stat label="LLM cost" value={usd(run.cost_usd)} />
          <Stat label="Status" value={run.status} tone={run.status === "failed" ? "bad" : undefined} />
        </div>
      </div>

      {run.status === "failed" && (
        <pre className="mb-6 overflow-x-auto rounded-lg border border-red-300 bg-red-50 p-4 text-xs text-red-800 dark:border-red-900 dark:bg-red-950/40 dark:text-red-200">{run.error_message}</pre>
      )}

      {initial.targets.length > 0 && (
        <p className="mb-6 text-sm text-zinc-500">
          Diff touched {initial.targets.length} function{initial.targets.length > 1 ? "s" : ""}:{" "}
          {initial.targets.map((t) => (
            <code key={t.name} className="mr-2 rounded bg-zinc-200 px-1 font-mono text-xs dark:bg-zinc-800">{t.name}</code>
          ))}
        </p>
      )}

      {groups.length === 0 && run.status !== "failed" && (
        <p className="text-sm text-zinc-500">Running baseline suite and generating mutants…</p>
      )}

      <div className="grid gap-6 md:grid-cols-2">
        {groups.map(([key, list]) => {
          const [file, fn] = key.split("::");
          const survivors = list.filter((m) => m.status === "survived").length;
          return (
            <section key={key} className="rounded-xl border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
              <div className="mb-3 flex flex-wrap items-baseline justify-between gap-x-3">
                <h3 className="font-mono text-sm">
                  <span className="text-zinc-400">{file}::</span>{fn}
                </h3>
                <span className={`shrink-0 text-xs ${survivors ? "text-red-600" : "text-zinc-400"}`}>{survivors} survived / {list.length}</span>
              </div>
              <div className="flex flex-wrap gap-1.5">
                {list.map((m) => (
                  <Link
                    key={m.id}
                    href={`/runs/${run.id}/mutants/${m.id}`}
                    title={`line ${m.line}: ${m.description} → ${m.status}`}
                    className={`h-7 w-7 rounded-sm ${TILE[m.status]} ${flipped.has(m.id) ? "tile-flip" : ""} transition hover:ring-2 hover:ring-zinc-400`}
                  />
                ))}
              </div>
            </section>
          );
        })}
      </div>

      <div className="mt-8 flex flex-wrap gap-4 text-xs text-zinc-500">
        <Legend color={TILE.killed} label="killed" />
        <Legend color={TILE.survived} label="survived" />
        <Legend color={TILE.timeout} label="timeout — not counted as a kill" />
        <Legend color={TILE.error} label="error — excluded from denominator" />
      </div>
    </div>
  );
}

function Stat({ label, value, tone }: { label: string; value: string; tone?: "ok" | "bad" }) {
  const color = tone === "bad" ? "text-red-600 dark:text-red-400" : tone === "ok" ? "text-emerald-700 dark:text-emerald-400" : "";
  return (
    <div>
      <p className="text-[11px] uppercase tracking-wide text-zinc-500">{label}</p>
      <p className={`font-mono text-xl font-semibold ${color}`}>{value}</p>
    </div>
  );
}

function Legend({ color, label }: { color: string; label: string }) {
  return (
    <span className="flex items-center gap-1.5">
      <span className={`inline-block h-3 w-3 rounded-sm ${color}`} />
      {label}
    </span>
  );
}
