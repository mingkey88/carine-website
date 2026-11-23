// Takes the four prints for design 07: the live picture, photographed a moment before each shutter.
const { chromium } = require('playwright');
const url = process.argv[2], out = process.argv[3];
process.argv = [process.argv[0], process.argv[1], url, 'x', '1440', '900', '1', 'plain', '2'];
const { open } = require('./scrollqa2.js');
(async () => {
  const b = await chromium.launch(); const ctx = await open(b); const p = await ctx.newPage();
  await p.goto(url, { waitUntil: 'networkidle' }); await p.waitForTimeout(1200);
  await p.addStyleTag({ content: '.world.cornered::before{display:none!important}' });
  const at = [.264, .484, .766, .952];
  for (let i = 0; i < at.length; i++) {
    for (const t of [at[i] - .08, at[i] - .04, at[i] - .01, at[i]]) {
      await p.evaluate(t => { const el = document.getElementById('help'); const top = el.getBoundingClientRect().top + scrollY; scrollTo(0, top + t * (el.offsetHeight - innerHeight)); }, t);
      await p.waitForTimeout(500);
    }
    await p.waitForTimeout(1600);
    await p.evaluate(() => { document.querySelector('.world__tag').style.visibility = 'hidden'; });
    await p.locator('.world__view').screenshot({ path: `${out}/snap-${i + 1}.png` });
    await p.evaluate(() => { document.querySelector('.world__tag').style.visibility = ''; });
  }
  await b.close();
})();
