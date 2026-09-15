const { chromium } = require("playwright");
const path = require("path");
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto("file://" + path.join(__dirname, "slides", "deck.html"));
  await page.waitForTimeout(500);
  await page.pdf({ path: process.argv[2] || "deck.pdf", width: "1920px", height: "1080px", printBackground: true, preferCSSPageSize: true });
  for (let i = 0; i < 10; i++) {
    await page.evaluate((i) => document.querySelectorAll("section")[i].scrollIntoView(), i);
  }
  await browser.close();
})();
