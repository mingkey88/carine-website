# carine-website

Single-page brochure site for Carine Zheng, financial planner with Financial
Alliance, Singapore.

Static HTML, CSS and one small JS file. No build step, no dependencies.

---

## Run it

```sh
open index.html
```

Or, if you want a local server (needed only if you add anything that fetches):

```sh
python3 -m http.server 8000
```

## Deploy it

Upload the folder. Everything is relative and self-contained, so GitHub Pages,
Netlify, Cloudflare Pages, Vercel or plain S3 all work with no configuration.

---

## Before this goes live

**This site is not launch-ready.** Two blockers, both in
[CONTENT-QUERIES.md](CONTENT-QUERIES.md):

1. **Financial Alliance compliance has not signed off.** Carine is a licensed
   representative and MAS rules govern how she advertises. The footer disclaimer
   is placeholder wording written by us, not approved text.
2. **Carine has not approved the copy.** Everything on the page is either taken
   from her public Financial Alliance profile or listed in CONTENT-QUERIES.md as
   needing her confirmation. Three claims from the original brief (mother of
   three, fifteen years' experience, family-protection positioning) were left
   off the page because they could not be verified.

Also outstanding: her portrait, see [ASSETS-TODO.md](ASSETS-TODO.md).

### Search engines are blocked

Because of the above, the site is held back from search in two places:

- `robots.txt` carries `Disallow: /`
- `index.html` carries `<meta name="robots" content="noindex, nofollow">`

Both are needed. `robots.txt` stops well-behaved crawlers fetching the page; the
meta tag is what actually keeps it out of the index if the URL is discovered
some other way, such as a shared link.

**At sign-off:** change `robots.txt` to `Allow: /` and delete the noindex meta
from `index.html`. Until then, the page is safe to share as a link for review
without it turning up in a search for her name.

---

## Files

| Path | What it is |
|---|---|
| `index.html` | The page. Six sections plus nav and footer. |
| `css/styles.css` | Tokens, layout, motion, print styles. |
| `js/main.js` | Scroll reveal and nav state. Nothing else. |
| `assets/fonts/` | EB Garamond and Instrument Sans, self-hosted. |
| `assets/img/` | Empty. Portrait goes here. |
| `DESIGN.md` | Why the page looks the way it does. |
| `CONTENT-QUERIES.md` | What needs Carine's or compliance's sign-off. |
| `ASSETS-TODO.md` | What images are missing and how to drop them in. |

## Notes

- Light mode only. The page stays light even when the reader's system is set to
  dark, and there is no toggle.
- Fonts are self-hosted, so nothing leaves the page at runtime. No analytics, no
  trackers, no CDN calls.
- Contrast was measured against WCAG AA, buttons against 1.4.11 as well. See
  DESIGN.md.
