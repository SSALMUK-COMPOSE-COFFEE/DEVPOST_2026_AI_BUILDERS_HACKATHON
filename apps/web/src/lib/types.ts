export type RunStatus = "queued" | "running" | "done" | "failed";
export type Verdict = "pending" | "killed" | "survived" | "timeout" | "error";

export interface RunSummary {
  id: string;
  repo: string | null;
  status: RunStatus;
  diff_only: boolean;
  baseline_passed: number;
  line_coverage: number | null;
  mutation_score: number | null;
  total: number;
  killed: number;
  survived: number;
  timeout: number;
  error: number;
  duration_ms: number | null;
  cost_usd: number;
  error_message: string | null;
  created_at: string | null;
  finished_at: string | null;
}

export interface Target {
  file: string;
  name: string;
  line_start: number;
  line_end: number;
}

export interface MutantSummary {
  id: string;
  key: string;
  file: string;
  function: string;
  operator: string;
  line: number;
  description: string;
  status: Verdict;
  cluster: string | null;
}

export interface Proposal {
  id: string;
  test_name: string;
  source: string;
  rationale: string;
  verdict: "pending" | "verified_kill" | "rejected" | "error";
  original_exit: number | null;
  mutant_exit: number | null;
  created_at: string;
}

export interface MutantDetail extends MutantSummary {
  run: RunSummary;
  original_source: string;
  mutant_source: string;
  executions: { phase: string; exit_code: number | null; duration_ms: number; stdout_tail: string }[];
  proposals: Proposal[];
}

export interface RepoPreset {
  slug: string;
  description: string;
  runs: number;
}
