const STYLES: Record<string, string> = {
  killed: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900/50 dark:text-emerald-200",
  survived: "bg-red-100 text-red-800 dark:bg-red-900/50 dark:text-red-200",
  timeout: "bg-zinc-200 text-zinc-700 dark:bg-zinc-800 dark:text-zinc-300",
  error: "bg-amber-100 text-amber-800 dark:bg-amber-900/50 dark:text-amber-200",
  pending: "bg-zinc-100 text-zinc-500 dark:bg-zinc-800",
  verified_kill: "bg-emerald-600 text-white",
  rejected: "bg-red-600 text-white",
  done: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900/50 dark:text-emerald-200",
  running: "bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-200",
  queued: "bg-zinc-100 text-zinc-600 dark:bg-zinc-800",
  failed: "bg-red-100 text-red-800 dark:bg-red-900/50 dark:text-red-200",
};

export function Badge({ value, className = "" }: { value: string; className?: string }) {
  return (
    <span className={`inline-block rounded px-2 py-0.5 font-mono text-xs font-semibold uppercase tracking-wide ${STYLES[value] ?? STYLES.pending} ${className}`}>
      {value.replace("_", " ")}
    </span>
  );
}
