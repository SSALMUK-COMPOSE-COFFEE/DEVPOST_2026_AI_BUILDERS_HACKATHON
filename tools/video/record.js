const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const SITE = "https://killscore.hajin.xyz";
const API = "https://killscore-api.hajin.xyz";
const REC = path.join(__dirname, "rec");
const SLIDES = "file://" + path.join(__dirname, "slides");
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function getJson(url) {
  const res = await fetch(url);
  return res.json();
}

async function glide(page, x, y, steps = 25) {
  await page.mouse.move(x, y, { steps });
}

async function clickText(page, text, opts = {}) {
  const el = page.getByText(text, { exact: false }).first();
  const box = await el.boundingBox();
  if (box) await glide(page, box.x + box.width / 2, box.y + box.height / 2);
  await sleep(300);
  await el.click(opts);
}

const scenes = {
  hook: async (page) => {
    await page.goto(`${SLIDES}/hook.html`);
    await sleep(9000);
  },
  intro: async (page) => {
    await page.goto(`${SLIDES}/intro.html`);
    await sleep(11000);
  },
  live: async (page) => {
    await page.goto(`${SITE}/`);
    await sleep(2500);
    await glide(page, 400, 470);
    await sleep(600);
    await clickText(page, "demo/billing-api");
    await page.waitForURL(/\/runs\//, { timeout: 20000 });
    await sleep(500);
    for (let i = 0; i < 120; i++) {
      const status = await page.locator("text=done").count();
      if (status > 0) break;
      await sleep(250);
    }
    await sleep(4000);
    await glide(page, 200, 300);
    await sleep(2500);
  },
  survivor: async (page, ctx) => {
    await page.goto(`${SITE}/runs/${ctx.liveRun}`);
    await sleep(1500);
    await clickText(page, "Survivors");
    await page.waitForURL(/mutants\?status=survived/);
    await sleep(2500);
    const first = page.locator("tbody tr a").first();
    const box = await first.boundingBox();
    await glide(page, box.x + 20, box.y + 10);
    await sleep(400);
    await first.click();
    await page.waitForURL(/mutants\/[a-f0-9]+$/);
    await sleep(4500);
    await page.mouse.wheel(0, 260);
    await sleep(3500);
    const btn = page.getByRole("button", { name: "Propose a test" });
    const bb = await btn.boundingBox();
    await glide(page, bb.x + bb.width / 2, bb.y + bb.height / 2);
    await sleep(500);
    await btn.click();
    await page.getByText(/VERIFIED KILL|REJECTED/).first().waitFor({ timeout: 90000 });
    await sleep(800);
    await page.mouse.wheel(0, 300);
    await sleep(6000);
  },
  rejected: async (page, ctx) => {
    await page.goto(`${SITE}/runs/${ctx.rejRun}/mutants/${ctx.rejMutant}`);
    await sleep(1500);
    await page.getByText("REJECTED").first().scrollIntoViewIfNeeded();
    await sleep(6500);
    await page.goto(`${SITE}/runs/${ctx.authRun}`);
    await sleep(3000);
    const tile = page.locator(`a[href$="/mutants/${ctx.timeoutMutant}"]`).first();
    const tb = await tile.boundingBox();
    await glide(page, tb.x + tb.width / 2, tb.y + tb.height / 2);
    await sleep(1800);
    await tile.click();
    await page.waitForURL(/mutants\//);
    await sleep(5000);
  },
  arch: async (page) => {
    await page.goto(`${SLIDES}/arch.html`);
    await sleep(12000);
  },
  evals: async (page) => {
    await page.goto(`${SITE}/evals`);
    await sleep(1500);
    await glide(page, 640, 300);
    await sleep(8000);
    await page.mouse.wheel(0, 200);
    await sleep(6000);
  },
  gate: async (page) => {
    await page.goto(`${SITE}/gate`);
    await sleep(3500);
    const slider = page.locator('input[type="range"]');
    const sb = await slider.boundingBox();
    await glide(page, sb.x + sb.width * 0.6, sb.y + sb.height / 2);
    await page.mouse.down();
    await glide(page, sb.x + sb.width * 0.8, sb.y + sb.height / 2, 20);
    await page.mouse.up();
    await sleep(2500);
    await page.goto(`${SITE}/pricing`);
    await sleep(4000);
  },
  end: async (page) => {
    await page.goto(`${SLIDES}/end.html`);
    await sleep(5000);
  },
};

(async () => {
  const wanted = process.argv.slice(2);
  const names = wanted.length ? wanted : Object.keys(scenes);
  const runs = await getJson(`${API}/v1/runs?limit=50`);
  const ctx = {
    liveRun: null,
    rejRun: process.env.REJ_RUN,
    rejMutant: process.env.REJ_MUTANT,
    authRun: runs.find((r) => r.repo === "auth-tokens" && r.status === "done")?.id,
  };
  if (ctx.authRun) {
    const ms = await getJson(`${API}/v1/runs/${ctx.authRun}/mutants?status=timeout`);
    ctx.timeoutMutant = ms[0]?.id;
  }
  fs.mkdirSync(REC, { recursive: true });
  const browser = await chromium.launch();
  for (const name of names) {
    const slide = ["hook", "intro", "arch", "end"].includes(name);
    const context = await browser.newContext({
      viewport: slide ? { width: 1920, height: 1080 } : { width: 1280, height: 720 },
      recordVideo: { dir: REC, size: slide ? { width: 1920, height: 1080 } : { width: 1280, height: 720 } },
      colorScheme: "light",
    });
    const page = await context.newPage();
    const t0 = Date.now();
    try {
      await scenes[name](page, ctx);
      if (name === "live") ctx.liveRun = page.url().split("/runs/")[1].split(/[/?]/)[0];
    } catch (e) {
      console.error(`scene ${name} failed:`, e.message);
    }
    const video = page.video();
    await context.close();
    const p = await video.path();
    fs.renameSync(p, path.join(REC, `${name}.webm`));
    console.log(`${name}: ${((Date.now() - t0) / 1000).toFixed(1)}s`);
  }
  fs.writeFileSync(path.join(REC, "ctx.json"), JSON.stringify(ctx, null, 2));
  await browser.close();
})();
