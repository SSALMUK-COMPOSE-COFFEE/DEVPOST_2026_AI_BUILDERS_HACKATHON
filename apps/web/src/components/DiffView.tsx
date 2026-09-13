import { focusWindow, lineDiff } from "@/lib/diff";

export function DiffView({ original, mutant, full = false }: { original: string; mutant: string; full?: boolean }) {
  const lines = lineDiff(original, mutant);
  const shown = full ? lines : focusWindow(lines);
  return (
    <div className="overflow-x-auto rounded-lg border border-zinc-200 bg-white font-mono text-xs dark:border-zinc-800 dark:bg-zinc-900">
      <table className="w-full border-collapse">
        <tbody>
          {shown.map((l, i) => (
            <tr
              key={i}
              className={
                l.kind === "add"
                  ? "bg-red-50 text-red-900 dark:bg-red-950/50 dark:text-red-200"
                  : l.kind === "del"
                    ? "bg-emerald-50 text-emerald-900 dark:bg-emerald-950/50 dark:text-emerald-200"
                    : ""
              }
            >
              <td className="w-10 select-none border-r border-zinc-100 px-2 text-right text-zinc-400 dark:border-zinc-800">{l.oldNo ?? ""}</td>
              <td className="w-10 select-none border-r border-zinc-100 px-2 text-right text-zinc-400 dark:border-zinc-800">{l.newNo ?? ""}</td>
              <td className="w-5 select-none px-1 text-zinc-400">{l.kind === "add" ? "+" : l.kind === "del" ? "-" : " "}</td>
              <td className="whitespace-pre px-2">{l.text}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
