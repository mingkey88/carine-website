# Design notes

Single-page brochure site for Carine Zheng, financial planner with Financial
Alliance, Singapore.

**Read this first:** what is and is not verified copy is documented in
[CONTENT-QUERIES.md](CONTENT-QUERIES.md). That file gates the launch, not this
one.

---

## The brief, and how it was read

A personal-brand landing page for a licensed financial adviser. Two forces pull
against each other:

- It is a **personal** brand. The stated goal was something bigger than
  "insurance agent", which means the page has to read as authored by a person.
- It is a **regulated** profession. Trust-first constraints outrank decoration,
  and compliance can veto anything on the page.

Resolved as: editorial restraint. Design dials sat at variance 6, motion 4,
density 3. Enough asymmetry and warmth to feel human, not enough to look like it
is selling something.

---

## Deliberate choices, and what was rejected

### Typography: EB Garamond + Instrument Sans

Financial services default to a neutral grotesk. A text serif is the
differentiator here, and it carries the right associations for the work:
considered, literate, patient. That is what long-term planning should feel like.

EB Garamond specifically because it is a genuine publication face rather than a
high-contrast display serif. It holds up at 14px in the footer disclaimer as
well as at 60px in the hero, which matters on a page this text-heavy.

**Rejected:** Fraunces and Instrument Serif, the two display serifs that turn up
in almost every AI-generated "editorial" layout. Also rejected Inter as the body
face for the same reason.

Both fonts are self-hosted in `assets/fonts/` as latin-subset variable woff2,
about 122KB total. No external requests, so the page cannot break because a
font CDN is slow, blocked, or gone.

### Colour: forest, bone, brick

```
--ground  #f4f4ef   bone         page
--ink     #16211c   green-black  text
--forest  #1e4635   deep green   brand, primary button, statement block
--accent  #a63d22   brick        the single accent, page-wide
```

Forest reads as growth and steadiness without being the navy-and-gold uniform
every financial site wears. Brick gives warmth where gold would give
"institution". One accent, locked across every section.

**Rejected:** navy + gold, the category default. Also rejected the warm
beige-and-brass palette that reads as premium-but-generic.

Dark mode is a full token swap under `prefers-color-scheme`, not an
afterthought. Both themes were contrast-audited (below).

### Layout: six sections, six different structures

| Section | Structure |
|---|---|
| Hero | Asymmetric split, 1.15fr text against 0.85fr portrait |
| Who I work with | Full-bleed forest block, the page's one colour inversion |
| What I talk about | Four-cell grid, 7fr/5fr reversing to 5fr/7fr on row two |
| How working together looks | Vertical stack, hanging rules |
| Credentials | Auto-fit definition list |
| Contact | Split, actions against a detail list |

No two sections share a layout family, and there is no left-image/right-text
zigzag anywhere. The four topic cells are not four identical cards: the grid is
asymmetric and two of the four carry a background tint so the block has rhythm.

The forest statement block is the only place the page inverts. That is a
deliberate single colour block giving the page a spine, not alternating themes.

### Motion

One effect: sections fade and rise 18px as they enter view, with small stagger
delays inside grouped content. It exists to sequence the page as a narrative
rather than dumping it all at once. Entry only, never looping, nothing that
moves while you are trying to read.

Driven by `IntersectionObserver`, not scroll listeners. Under
`prefers-reduced-motion: reduce` every element is marked visible immediately,
smooth scrolling is switched off, and the button press translate is removed.

### What is deliberately absent

- **Icons.** Contact details are set typographically. Nothing to license.
- **Stock photography.** A real adviser's page should not be decorated with
  strangers. One real portrait slot, listed in
  [ASSETS-TODO.md](ASSETS-TODO.md).
- **A contact form.** No backend, and a form that silently fails is worse than
  no form. WhatsApp and mailto links work everywhere and land in a place she
  already checks.
- **Testimonials.** None are cleared, and compliance may prohibit them.
- **Scroll cues, eyebrow labels, section numbering, version stamps.** All
  decoration that would work against a trust-first read.

---

## Accessibility

Contrast was measured, not eyeballed. Every text pairing in both themes clears
WCAG AA at 4.5:1:

| | Light | Dark |
|---|---|---|
| Body on ground | 15.01:1 | 15.24:1 |
| Secondary text on ground | 6.88:1 | 8.14:1 |
| Small labels on surface | 4.77:1 | 5.21:1 |
| Primary button label | 9.28:1 | 5.01:1 |
| Ghost button label | 15.01:1 | 15.24:1 |
| Accent link | 5.75:1 | 5.88:1 |

Three token pairs exist because one value could not serve both themes.

**`--rule` and `--rule-control`.** `--rule` draws decorative hairlines and sits
below 3:1 on purpose, which WCAG 1.4.11 permits for decoration.
`--rule-control` draws the ghost button border at 3.19:1 light and 3.24:1 dark,
because that boundary identifies a control.

**`--btn-bg` inverts in dark mode.** The forest fill reads at 9.60:1 as a shape
on bone, but only 2.04:1 on near-black. The label stayed legible, so it passed a
text-only audit while the button itself dissolved into the page. Dark mode uses
a light green fill (`#4e9c79`) with dark text instead: 5.58:1 as a shape, 5.01:1
for the label. Green either way, so the brand holds, but the primary action
actually reads as a button in both themes.

Measured against the *fill*, not just the text. A CTA that nobody recognises as
a CTA is a conversion bug before it is an accessibility one.

Also: skip link, `:focus-visible` rings on the accent colour, semantic landmarks,
labelled nav, `<address>` for the office, and a print stylesheet that drops the
nav and buttons.

---

## Structure

```
index.html            the page
css/styles.css        tokens, layout, motion, print
js/main.js            reveal observer, nav state
assets/fonts/         3 self-hosted woff2, ~122KB
assets/img/           empty, see ASSETS-TODO.md
```

No build step, no dependencies, no package.json. Open `index.html` and it runs.
Deploys to any static host as-is.

---

## Known gaps

1. **Portrait not supplied.** Styled placeholder in the hero. See
   ASSETS-TODO.md.
2. **No `og:image`.** Links currently unfurl as text.
3. **Positioning conflict unresolved.** The four content pillars are
   family-themed; the verified hero copy addresses young working adults. See
   CONTENT-QUERIES.md section 3.
4. **Compliance not obtained.** The footer disclaimer is our wording standing in
   for whatever FAPL requires. This blocks launch.
