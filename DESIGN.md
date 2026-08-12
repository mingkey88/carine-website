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

Resolved as: editorial restraint. Enough warmth and asymmetry to feel human, not
enough to look like it is selling something.

### Reference

The visual language follows the [Halden Miller Webflow
template](https://halden-miller.webflow.io/), supplied as a reference. What was
taken from it: the warm neutral palette, the IBM Plex superfamily, the 16px
radius on large surfaces, small uppercase mono labels, and a single inverted
dark block.

What was **not** taken: its "Trusted by 500+ clients (4.9/5)" row. That is
fabricated social proof, and there is nothing real to put in its place.

The page is **light only, by request**. `color-scheme: light` is declared so
that form controls, scrollbars and browser chrome also stay light for readers
whose system is set to dark, rather than framing the page in a theme it was not
designed for.

---

## Deliberate choices

### Typography: the IBM Plex superfamily

Three faces from one family, which is where the reference gets its coherence:

| Role | Face | Notes |
|---|---|---|
| Display | IBM Plex Serif 400 | Tracking `-0.03em`, line-height `1.1` |
| Body | IBM Plex Sans 400-600 | Variable |
| Micro-labels | IBM Plex Mono 400 | 11px, uppercase, `0.11em` tracking |

The mono is doing real work, not decoration: it sets the small uppercase `<dt>`
labels in the credentials and contact lists. That is the reference's texture,
and it comes from labelling actual data rather than from pill eyebrows stacked
above every section heading.

Emphasis inside a display line uses the same family's italic (`.display em`),
never a second typeface.

All four files are self-hosted in `assets/fonts/` as latin-subset woff2, about
81KB total. No external requests, so the page cannot break because a font CDN is
slow, blocked, or gone.

### Colour: warm neutral, no accent

```
--ground        #f7f7f2   warm off-white   page
--surface       #efede7   warm greige      panels
--surface-deep  #e1dcd5   deeper greige    alternating panels
--ink           #191818   warm near-black  text
--dark          #191818                    the one inverted block
```

There is **no chromatic accent anywhere**. That is the point of the reference and
it is what makes it work: the warmth comes from the greige tints and, once it
exists, from the photography. Adding a colour accent would fight both.

This also answers the "more feminine" brief without reaching for pink. The
softness comes from warm greige, 16px corners, and a delicate serif. For someone
asking clients to trust her with protection and retirement decisions, that holds
authority in a way blush would not.

### Shape

One scale, three steps, no exceptions:

- **16px** on large surfaces: portrait, topic panels, statement block, credentials
- **8px** on small elements and focus rings
- **pill** on buttons

### Layout: six sections, six different structures

| Section | Structure |
|---|---|
| Hero | Asymmetric split, 1.15fr text against 0.85fr portrait |
| Who I work with | Inverted dark panel, the page's one tonal inversion |
| What I talk about | Four-cell grid, 7fr/5fr reversing to 5fr/7fr on row two |
| How working together looks | Vertical stack, hanging rules |
| Credentials | Greige panel, auto-fit definition list |
| Contact | Split, actions against a detail list |

No two sections share a layout family, and there is no left-image/right-text
zigzag anywhere. The four topic cells are not four identical cards: the grid is
asymmetric and two of the four sit a step deeper in tone, on the diagonal.

### Motion

One effect: sections fade and rise 18px as they enter view, with small stagger
delays inside grouped content. It exists to sequence the page as a narrative
rather than dumping it all at once. Entry only, never looping, nothing that
moves while you are trying to read.

Driven by `IntersectionObserver`, not scroll listeners, at `threshold: 0` so an
element taller than the viewport can never get stuck hidden. The hidden state is
scoped to a `.js` class set before first paint, so if the script fails the
content is simply visible.

Under `prefers-reduced-motion: reduce` every element is marked visible
immediately, smooth scrolling is switched off, and the button press translate is
removed.

### What is deliberately absent

- **Icons.** Contact details are set typographically. Nothing to license.
- **Stock photography.** A real adviser's page should not be decorated with
  strangers. See the gap below.
- **A contact form.** No backend, and a form that silently fails is worse than
  no form. WhatsApp and mailto links land in a place she already checks.
- **Testimonials and trust metrics.** None are real, and compliance may
  prohibit them.
- **Scroll cues, pill eyebrows, section numbering, version stamps.** All
  decoration that would work against a trust-first read.

---

## Accessibility

Contrast is measured against the *rendered* page, not against the token values,
by walking every text node, resolving its true background through transparent
ancestors, and applying the correct threshold for its size and weight.

Latest run: **50 text nodes checked, 0 failures.**

| | Ratio | Required |
|---|---|---|
| Body on ground | 16.49:1 | 4.5:1 |
| Secondary text on ground | 6.56:1 | 4.5:1 |
| Mono labels on deep greige | 4.71:1 | 4.5:1 |
| Text on the dark panel | 16.49:1 | 4.5:1 |
| Primary button label | 16.49:1 | 4.5:1 |
| Primary button as a shape | 16.49:1 | 3:1 |
| Ghost button border | 3.51:1 | 3:1 |

Two divider tokens exist for a reason. `--rule` draws decorative hairlines and
sits below 3:1 on purpose, which WCAG 1.4.11 permits for decoration.
`--rule-control` draws the ghost button border at 3.51:1, because that boundary
identifies a control.

Buttons are measured against the *fill* as well as the text. A CTA that nobody
recognises as a CTA is a conversion bug before it is an accessibility one.

Also: skip link, `:focus-visible` rings, semantic landmarks, labelled nav,
`<address>` for the office, and a print stylesheet that drops the nav and
buttons and converts the dark panel to outlined black on white.

---

## Structure

```
index.html            the page
css/styles.css        tokens, layout, motion, print
js/main.js            reveal observer, nav state
assets/fonts/         4 self-hosted woff2, ~81KB
assets/img/           empty, see ASSETS-TODO.md
```

No build step, no dependencies, no package.json. Open `index.html` and it runs.
Deploys to any static host as-is.

---

## Known gaps

1. **Photography beyond the hero.** The hero portrait is now in place. But the
   reference is roughly 70% photography and every one of its sections is
   carried by warm natural-light imagery, where this page has exactly one
   photo. The remaining three sections would each benefit from one. Shot list
   and art direction are in ASSETS-TODO.md.
2. **No `og:image`.** Links currently unfurl as text.
3. **Positioning conflict unresolved.** The four content pillars are
   family-themed; the verified hero copy addresses young working adults. See
   CONTENT-QUERIES.md section 3.
4. **Compliance not obtained.** The footer disclaimer is our wording standing in
   for whatever FAPL requires. This blocks launch.
