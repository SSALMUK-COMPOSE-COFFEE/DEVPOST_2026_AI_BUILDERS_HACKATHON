import { api } from "@/lib/api";
import type { RepoPreset } from "@/lib/types";
import { GatePanel } from "@/components/GatePanel";

export const dynamic = "force-dynamic";

export default async function GatePage() {
  let presets: RepoPreset[] = [];
  try {
    presets = await api<RepoPreset[]>("/v1/repos");
  } catch {}
  return (
    <main className="mx-auto max-w-6xl px-4 py-8">
      <h1 className="mb-1 text-xl font-semibold">Merge gate</h1>
      <p className="mb-6 text-sm text-zinc-500">Codecov and SonarQube measure whether code ran. This measures whether tests can disprove it.</p>
      <GatePanel presets={presets} />
    </main>
  );
}
