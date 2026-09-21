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

**Colour follows Rebecca's v2 note**, applied 21 September 2026 as a trial
ahead of Carine's answer: espresso brown, navy blue and beige, "for
professionalism and approachability". See CONTENT-QUERIES.md 0.1 for where the
decision stands.

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

Emphasis inside a display line uses the same family's italic (`.hero__title em`,
`.h2 em`), never a second typeface.

Tracking has two values, held as tokens: `--tracking-display` (-0.03em) on
every heading, `--tracking-label` (-0.02em) on the brand marks and credential
values. Body copy on the page is never below 16px; the footer disclaimer is the
one exception at 14px.

All four files are self-hosted in `assets/fonts/` as latin-subset woff2, about
81KB total. No external requests, so the page cannot break because a font CDN is
slow, blocked, or gone.

### Colour: beige, espresso, navy

Three colours, three roles. Each colour does one job and the jobs do not
overlap.

```
--ground        #f6f1e8   beige       canvas
--surface       #ece4d6   beige       panels
--surface-deep  #dfd3c0   sand        icon discs, deeper panels
--ink           #2b1c14   espresso    text
--ink-soft      #5e4a3e   espresso    secondary text
--accent        #1e2a44   navy        everything that acts
--dark          = accent              the one inverted panel
```

**Beige and espresso carry the warmth.** They are the reading pair: espresso on
beige is 14.6:1 and still feels like paper rather than a screen.

**Navy is the one accent, and it only ever means "act" or "watch".** It owns
the buttons, the anchored WhatsApp button, the three step numbers, the four
icon strokes, and the video panel. It appears nowhere as decoration, so when
the eye lands on navy it has landed on something to do. The hero portrait's
navy blazer sits inside the same family, which is a happy accident worth
keeping in mind if the photo is ever reshot.

Secondary text on the navy panel is tinted from navy (`--on-dark-soft`
#b7bccb), not a generic grey, so it reads as the same material. Anything
translucent on the panel (the carousel scrollbar, the tile edges) is beige at
low alpha for the same reason: a tinted grey there reads as a fourth hue.

The anchored WhatsApp button rides over the navy panel on phones and tablets,
so it carries a 2px beige keyline and a two-tone focus ring, either half of
which shows against whichever ground is behind it.

This answers the "more feminine" brief without reaching for pink. The softness
comes from beige, 16px corners and a delicate serif; navy keeps the authority
a financial planner needs.

### Shape

One scale, three steps, no exceptions:

- **16px** on large surfaces: portrait, topic panels, video panel, credentials
- **8px** on small elements and focus rings
- **pill** on buttons

### Layout: six sections, six different structures

| Section | Structure |
|---|---|
| Hero | Asymmetric split, 1.15fr text against 0.85fr portrait, one button |
| What I can help you with | Four equal columns, each an icon disc over a heading over text |
| Making sense of financial planning | Inverted dark panel, the page's one tonal inversion. Centred heading, video carousel (CSS scroll-snap, no script), centred row of social icons |
| What working together looks like | Three numbered steps in a row on one rule, reading left to right |
| Let's talk | Split, one button against a detail list |
| Regulatory and professional information | Greige panel, auto-fit definition list |

Rebecca's v2 notes (21 Sep 2026) set the help cells and the steps horizontal,
asked for icons on both the cells and the socials, centred the video heading,
cut the nav links and secondary buttons, and added an anchored WhatsApp
button. The header is now the brand mark alone and no longer sticky, because
the anchored button carries the call to action on every scroll position.

Section order and copy follow Rebecca's "Carine's website - v1" document. The
dark panel moved from the old "Who I work with" statement to the video section,
because saturated YouTube thumbnails sit better inside a dark frame than on
greige.

Until the videos arrive the carousel holds four placeholder tiles, numbered in
the mono label style and carrying the page's only drawn icon, a play mark. It
is a stand-in for YouTube's own player chrome and goes with the tiles.

No two sections share a layout family, and there is no left-image/right-text
zigzag anywhere.

### Icons

Two kinds, both inline SVG in a sprite at the top of the body, so nothing is
fetched:

- **Four line icons** for the help cells: shield with a tick, rising line, flag,
  sunrise. Drawn on a 24-unit grid at a 1.5 stroke with round joins, so they
  read as one set. They sit in a deeper-greige disc.
- **Brand marks** for WhatsApp and the five social platforms, from Simple Icons
  (CC0), filled in the panel's off-white at 22px inside a 44px hit area.

The play mark on the placeholder video tiles goes with the tiles.

### Responsive behaviour

Breakpoints are content-driven, not device-driven:

| Point | What changes |
|---|---|
| ≤400px | The two hero and contact buttons go full width, one under the other |
| ≤860px | Everything becomes one column and is **centred**: hero, help cells (two across from 600px), dark panel, steps with their numbers on the axis, contact, credentials, footer. Portrait centred at 400px. Measures keep their max-width and sit on the axis |
| ≤900px | Contact detail rows stack their label over the value |
| ≥861px | Desktop composition: asymmetric hero, four help columns, three steps in a row, two-column contact, left-aligned text |

One stack point rather than four. Phones and tablets in portrait get the
centred column; tablets in landscape and up get the desktop composition. The
anchored WhatsApp button sits bottom-right at every width, inset from the
safe area on notched phones.

Text links that are one line tall carry an invisible `::after` that extends
their hit area to 44px without moving the row. Safe-area insets are folded
into the gutter for notched phones.

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

- **Icons on the contact details.** Those stay typographic; the icon set is
  reserved for the help cells and the social row.
- **Stock photography.** A real adviser's page should not be decorated with
  strangers. See the gap below.
- **A contact form.** No backend, and a form that silently fails is worse than
  no form. WhatsApp and mailto links land in a place she already checks.
- **Testimonials and trust metrics.** None are real, and compliance may
  prohibit them.
- **Scroll cues, pill eyebrows, version stamps.** All decoration that would
  work against a trust-first read. The step numbers are the one exception:
  they are a sequence, and the number tells the reader where they are in it.

---

## Accessibility

Contrast is measured against the *rendered* page, not against the token values,
by walking every text node, resolving its true background through transparent
ancestors, and applying the correct threshold for its size and weight.

Token pairs, measured at the palette change on 21 September 2026:

| | Ratio | Required |
|---|---|---|
| Espresso on beige canvas | 14.60:1 | 4.5:1 |
| Secondary espresso on canvas / panel / sand | 7.39 / 6.59 / 5.63 | 4.5:1 |
| Mono labels on sand | 4.57:1 | 4.5:1 |
| Beige text on the navy panel | 12.70:1 | 4.5:1 |
| Tinted secondary text on navy | 7.53:1 | 4.5:1 |
| Tile labels on the placeholder tiles | 5.64:1 | 4.5:1 |
| Button label on navy | 12.70:1 | 4.5:1 |
| Navy button as a shape on beige | 12.70:1 | 3:1 |
| Navy icon strokes on the sand disc | 9.67:1 | 3:1 |
| Step rule (`--rule-control`) on beige | 3.68:1 | 3:1 |

Two divider tokens exist for a reason. `--rule` draws decorative hairlines and
sits below 3:1 on purpose, which WCAG 1.4.11 permits for decoration.
`--rule-control` draws the steps rule at 3.68:1, because that line is part of
the step sequence the reader is meant to follow.

Buttons are measured against the *fill* as well as the text. A CTA that nobody
recognises as a CTA is a conversion bug before it is an accessibility one.

Also: skip link (fixed, so it never yanks the page to the top), `<main
tabindex="-1">` so the skip actually moves focus in Safari and Firefox,
`:focus-visible` rings that switch to off-white inside the dark panel, semantic
landmarks, labelled nav, `<address>` for the office, a visually hidden "(opens
in a new tab)" on every external link, and a print stylesheet that drops the
nav and buttons and converts the dark panel to outlined black on white.

---

## Structure

```
index.html            the page
css/styles.css        tokens, layout, motion, print
js/main.js            reveal observer
assets/fonts/         4 self-hosted woff2, ~81KB
assets/img/           hero portrait
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
3. **Video section is empty.** The carousel is built but has no videos and the
   follow row has only LinkedIn. It will read as a sparse dark block until
   Carine supplies links. See CONTENT-QUERIES.md section 4.
4. **Compliance not obtained.** The footer disclaimer is our wording standing in
   for whatever FAPL requires. This blocks launch.
