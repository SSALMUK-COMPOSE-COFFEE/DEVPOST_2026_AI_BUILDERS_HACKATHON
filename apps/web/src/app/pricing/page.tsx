import Script from "next/script";

const TABLE_ID = process.env.NEXT_PUBLIC_STRIPE_PRICING_TABLE_ID;
const PK = process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY;

const TIERS = [
  { name: "Free", price: "$0", unit: "forever", items: ["Unlimited public repos", "200 mutants per run", "No merge gate"] },
  { name: "Team", price: "$99", unit: "per month", items: ["5 private repos", "PR merge gate", "Slack alerts", "2,000 mutants per run"], featured: true },
  { name: "Business", price: "$399", unit: "per month", items: ["Unlimited repos", "TMMi evidence PDF", "SSO", "Self-hosted runner"] },
];

export default function PricingPage() {
  return (
    <main className="mx-auto max-w-6xl px-4 py-8">
      <h1 className="mb-1 text-xl font-semibold">Pricing</h1>
      <p className="mb-8 text-sm text-zinc-500">Priced per repository, not per seat. The person who presses merge should not need a budget line.</p>
      {TABLE_ID && PK ? (
        <>
          <Script src="https://js.stripe.com/v3/pricing-table.js" strategy="afterInteractive" />
          {/* @ts-expect-error custom element */}
          <stripe-pricing-table pricing-table-id={TABLE_ID} publishable-key={PK}></stripe-pricing-table>
        </>
      ) : (
        <div className="grid gap-4 md:grid-cols-3">
          {TIERS.map((t) => (
            <div key={t.name} className={`rounded-xl border p-6 ${t.featured ? "border-red-400 bg-white shadow-sm dark:border-red-700 dark:bg-zinc-900" : "border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900"}`}>
              <h2 className="font-semibold">{t.name}</h2>
              <p className="mt-2 text-3xl font-bold">{t.price} <span className="text-sm font-normal text-zinc-500">{t.unit}</span></p>
              <ul className="mt-4 space-y-1 text-sm text-zinc-600 dark:text-zinc-400">{t.items.map((i) => <li key={i}>· {i}</li>)}</ul>
              <button className={`mt-6 w-full rounded-md px-4 py-2 text-sm font-medium ${t.featured ? "bg-red-600 text-white hover:bg-red-500" : "border border-zinc-300 hover:bg-zinc-100 dark:border-zinc-700 dark:hover:bg-zinc-800"}`}>
                {t.name === "Free" ? "Start free" : "Start 14-day trial"}
              </button>
            </div>
          ))}
        </div>
      )}
      <p className="mt-6 text-xs text-zinc-400">Billing integration is not live yet. Nothing is charged.</p>
    </main>
  );
}
