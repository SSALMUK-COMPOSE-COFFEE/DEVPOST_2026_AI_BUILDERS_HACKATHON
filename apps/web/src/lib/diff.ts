export type DiffLine = { kind: "same" | "add" | "del"; text: string; oldNo?: number; newNo?: number };

export function lineDiff(a: string, b: string): DiffLine[] {
  const x = a.split("\n");
  const y = b.split("\n");
  const n = x.length;
  const m = y.length;
  const dp: number[][] = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0));
  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) {
      dp[i][j] = x[i] === y[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
    }
  }
  const out: DiffLine[] = [];
  let i = 0;
  let j = 0;
  while (i < n && j < m) {
    if (x[i] === y[j]) {
      out.push({ kind: "same", text: x[i], oldNo: i + 1, newNo: j + 1 });
      i++;
      j++;
    } else if (dp[i + 1][j] >= dp[i][j + 1]) {
      out.push({ kind: "del", text: x[i], oldNo: i + 1 });
      i++;
    } else {
      out.push({ kind: "add", text: y[j], newNo: j + 1 });
      j++;
    }
  }
  while (i < n) out.push({ kind: "del", text: x[i++], oldNo: i });
  while (j < m) out.push({ kind: "add", text: y[j++], newNo: j });
  return out;
}

export function focusWindow(lines: DiffLine[], context = 6): DiffLine[] {
  const idx = lines.map((l, i) => (l.kind === "same" ? -1 : i)).filter((i) => i >= 0);
  if (idx.length === 0) return lines;
  const lo = Math.max(0, idx[0] - context);
  const hi = Math.min(lines.length, idx[idx.length - 1] + context + 1);
  return lines.slice(lo, hi);
}
