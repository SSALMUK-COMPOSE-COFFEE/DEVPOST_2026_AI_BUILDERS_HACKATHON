import Link from "next/link";

export function Nav() {
  return (
    <header className="border-b border-zinc-200 dark:border-zinc-800">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3">
        <Link href="/" className="flex items-center gap-2 font-semibold tracking-tight">
          <span className="inline-block h-2.5 w-2.5 rounded-sm bg-red-500" />
          KillScore
        </Link>
        <nav className="flex gap-5 text-sm text-zinc-600 dark:text-zinc-400">
          <Link href="/runs" className="hover:text-zinc-900 dark:hover:text-zinc-100">Runs</Link>
          <Link href="/gate" className="hover:text-zinc-900 dark:hover:text-zinc-100">Gate</Link>
          <Link href="/evals" className="hover:text-zinc-900 dark:hover:text-zinc-100">Evals</Link>
          <Link href="/pricing" className="hover:text-zinc-900 dark:hover:text-zinc-100">Pricing</Link>
        </nav>
      </div>
    </header>
  );
}
