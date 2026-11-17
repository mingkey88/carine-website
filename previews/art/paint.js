// Rasterise each .piece in paint.html to a transparent PNG.
// Usage: node paint.js <paint.html> <png-dir>
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const [file, out] = process.argv.slice(2).map(p => path.resolve(p));
const hiDpi = new Set(['umbrella', 'sprout', 'house', 'sunrise', 'teacups', 'sparkle', 'tape-gold', 'tape-blue', 'moon', 'cap', 'rings', 'key', 'shoes', 'glasses', 'briefcase']);

(async () => {
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  for (const scale of [1, 2]) {
    const p = await b.newPage({ viewport: { width: 1800, height: 1200 }, deviceScaleFactor: scale });
    await p.goto('file://' + file);
    await p.addStyleTag({ content: 'body{background:transparent!important}' });
    await p.waitForTimeout(300);
    for (const el of await p.$$('.piece')) {
      const id = await el.getAttribute('id');
      if ((scale === 2) !== hiDpi.has(id)) continue;
      // Paint can bleed past a piece's box, so hide every other piece while this one is captured.
      await p.evaluate(keep => document.querySelectorAll('.piece').forEach(n => { n.style.visibility = n.id === keep ? 'visible' : 'hidden'; }), id);
      await el.screenshot({ path: path.join(out, id + '.png'), omitBackground: true });
    }
    await p.close();
  }
  await b.close();
  console.log(fs.readdirSync(out).filter(f => f.endsWith('.png')).join(' '));
})();
