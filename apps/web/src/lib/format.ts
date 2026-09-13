export const pct = (v: number | null | undefined) => (v == null ? "—" : `${Math.round(v * 100)}%`);
export const ms = (v: number | null | undefined) => (v == null ? "—" : v < 1000 ? `${v} ms` : `${(v / 1000).toFixed(1)} s`);
export const usd = (v: number | null | undefined) => (v == null ? "—" : `$${v.toFixed(v < 0.1 ? 3 : 2)}`);
