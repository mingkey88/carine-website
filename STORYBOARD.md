# Storyboard: design 05, "Story"

Design 05 (`previews/05-story.html`) is the watercolour look of design 04, told as
a story you scroll through. It follows the way oryzo.ai, Lusion's showpiece
site, turns each message into something you watch happen and can sometimes play
with. This file records what was taken from Oryzo, what was built from it, and
what still needs Carine's or compliance's sign-off.

It is a preview: not live, and kept out of search like the rest of the site.

---

## What we took from Oryzo

Oryzo was scrolled frame by frame on 17 Nov 2026 (the first half; the rest is
from an earlier teardown). The lesson is not its 3D coaster. It is that every
message gets its own device, played by the scroll.

| Device | How Oryzo uses it | What it does for the message |
|---|---|---|
| Examine while one line holds | The coaster turns end over end beside "Isn't just a coaster." | The line has time to land; the motion is the proof |
| Words that resolve as you scroll | "Powered by AI" sharpens out of a blur letter by letter; body copy brightens from grey as you reach it | Reading pace follows scroll pace |
| The punchline walks in | A hand rises to hold it: "We said high five. It heard six." | Claim, then a visual that answers it |
| Whole-screen mood | A rainbow glow pulses round the screen's edges for "AI" | A quality told without words |
| Kinetic headline | "it's wearable" slides across huge behind the object, then shrinks into a label | The statement becomes a caption, making room for the next beat |
| Transformation gag | The coaster arrives in a foil packet that tears open | The object acts the message out |
| Frame as window | A viewfinder stays put while what is inside changes: badge, cap, eye mask, pocket | One frame, many uses |
| Sideways filmstrip | Scrolling down moves a strip sideways; the centre card wipes into the next | A gallery without leaving the story |
| Fake UI as a toy | A prompt bar with a Send button | Play that is also the joke |
| Picture becomes place | A magazine cover's photo becomes the scene you then enter | A transition that means something |
| A lens per claim | Thermal camera for heat, blueprint for roundness, macro and slider for grip | Each claim seen the way that proves it |
| Pacing aids | A % counter, a progress bar, "Scroll to continue", the nav marking the chapter | You always know where you are, and are never trapped |

Underneath all of them: one idea per screen, a device chosen because it shows
that message, one stage and one light throughout, and small, optional play.

**Not taken:** the 3D product, photorealism, the jokes, the joke reviews (there
are no testimonials anywhere on Carine's site), and the weight (Oryzo downloads
about 29 MB).

---

## The page

**In one sentence:** Carine's planning, one message per screen, each one
happening as you scroll, with four you can play with.

**Voice:** warm and plain, as in Rebecca's copy. **Ground:** cream paper, seal red
for anything that acts, ending on night navy. **Build:** 2D on design 04's
watercolour artwork; no 3D, no libraries.

| # | Section | Her words | Device | What the scroll does | Play | Length |
|---|---|---|---|---|---|---|
| 1 | Hero | Financial planning for every stage of life. | Words that resolve | The headline sharpens word by word; the polaroid drops in and is taped | – | 1 screen |
| 2 | As life changes | Hero paragraph 1 | Frame as window | One polaroid frame holds her portrait, then a graduation cap, rings, a key, baby shoes, reading glasses; the four topic stickers grow and shrink as priorities shift | – | 4.2 |
| 3 | Greater clarity | Hero paragraph 2 | A lens | A clear patch over a muddled painting shows the neat path beneath, then the whole painting comes into focus | Move the lens | 3 |
| 4 | What I can help you with | Heading and line | Kinetic headline | The heading crosses the screen huge, then settles with the line and four stickers | – | 1.8 |
| 5 | Protecting what matters | Topic 1 | Whole-screen mood | The paper greys, rain falls, the umbrella opens; the house stays dry | Tap to make it pour | 2.8 |
| 6 | Growing your wealth | Topic 2 | Transformation | A scribbled tangle undoes itself; one clean line grows into a sprout | – | 2.8 |
| 7 | Life's milestones | Topic 3 | Sideways filmstrip | Polaroids slide past: marriage, a home, children, other major changes | – | 3 |
| 8 | Later life | Topic 4 | Whole-screen mood | The paper warms to golden hour as the sun rises over the hills | – | 2.2 |
| 9 | Making sense of financial planning | Heading, follow row | Frame and filmstrip | The centre polaroid is the one to watch | Swipe or arrows | – |
| 10 | What working together looks like | Quote and three steps | A conversation | Her belief, then the steps, arrive as chat bubbles with typing dots; "regularly" draws a loop | – | 3 |
| 11 | Let's talk | Contact copy, details, footer | Picture becomes place | Night falls; a note field opens WhatsApp with the visitor's words | Type and send | – |

Lengths are in screens of scrolling while the section holds. A HUD at the top
names the chapter and fills a progress line; held sections say "keep scrolling".

## The four interactions

1. **The lens** follows the pointer or a finger over the painting, and drifts on its own otherwise.
2. **Pour** (button or a tap on the scene) makes it rain harder for a few seconds; the umbrella holds.
3. **Videos** swipe sideways, or step with the arrows.
4. **The note** opens `wa.me/6583893356` with the visitor's text already typed.
   Nothing is stored. Without JavaScript the form still submits to WhatsApp.

None is needed to reach the end of the page.

---

## Wording that is new (Draft)

For Carine and compliance to approve or replace. Everything else is Rebecca's v1.

- "financial planner · Singapore" (hero eyebrow, also on design 04)
- "or scroll to begin", "keep scrolling"
- "move the lens over the painting", "tap to make it pour"
- Chapter names in the HUD; all are her headings except "Greater clarity" and "As life changes", which are lifted from her paragraphs
- "Your note (optional)", the placeholder "Hi Carine,", and "Opens WhatsApp with your note. Nothing is saved on this page."
- "Video 01 · coming soon" (placeholder)

## Compliance notes

- **No figures anywhere.** Growth is a plant, not a chart, coins or a percentage, so nothing reads as a promise of returns.
- **The priority stickers in section 2** resize per life stage to show "different financial priorities". They illustrate the sentence; they are not advice. Compliance should confirm they are comfortable with it.
- **The chat bubbles** are hand-drawn, not WhatsApp's branding, and every bubble is Carine's own copy.
- **The note field** sends nothing anywhere itself; it only opens WhatsApp.
- **Search:** `noindex` on the page, plus the site-wide `Disallow` in `robots.txt`.

---

## Budgets, measured

| | Phone target | Measured |
|---|---|---|
| Before the first screen is usable | 1.5 MB | 292 KB (page and four images), plus fonts |
| Whole page | 8 MB | 834 KB: a 69 KB page and 25 images loaded once each, the ones below the hero lazily |
| Script | 350 KB | 14 KB inline, no libraries |

The rain is drawn on a canvas only while that section is on screen.

## Fallbacks

- **Reduced motion, or no JavaScript:** the page renders as a finished still
  page, every section in its end state, nothing animating.
- **Held sections never trap:** they are plain scroll distance with a sticky stage.
- **WhatsApp** is one tap away at every point, from the anchored button.

## How it is built

- One file, `previews/05-story.html`, with images in `previews/kit/`.
- Each held section is a tall block with a sticky stage. Its scroll position
  becomes one progress value from 0 to 1, written as a CSS variable, and a small
  handler per section maps that to what moves.
- The artwork is painted in code: SVG shapes through watercolour filters, captured
  in Chromium and saved as WebP. Sources are in `previews/art/`:
  `node paint.js paint.html <png-dir>`, then
  `python3 towebp.py <png-dir> <webp-dir> <sheet.jpg>` (Playwright and Pillow).

## Tested, and not

Tested in headless Chromium at 1440 × 900 and 390 × 844: a frame-by-frame scroll
through every section, no horizontal scrolling, no script errors, all four
interactions, the reduced-motion still page, and every line of the v1 copy present.

Not yet tested: real phones (iPhone Safari and an older Android), a keyboard-only
pass, and a screen reader.
