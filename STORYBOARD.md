# Storyboard: design 05, "Story"

Design 05 (`previews/05-story.html`) is the watercolour look of design 04, told as
a story you scroll through. It follows the way oryzo.ai, Lusion's showpiece
site, turns each message into something you watch happen and can sometimes play
with. This file records what was taken from Oryzo, what was built from it, and
what still needs Carine's or compliance's sign-off.

It is a preview: not live, and kept out of search like the rest of the site.

Design 06, "Album", is built from this design and has its own file: `STORYBOARD-06.md`.

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
for anything that acts (WhatsApp buttons wear WhatsApp green), ending on night navy. **Build:** 2D, no 3D, no
libraries. Since the second art pass (19 Nov 2026) the pictures are ink-and-watercolour paintings in the style of
Carine's portrait, replacing the stickers that were painted in code; see "Second art pass" below.

| # | Section | Her words | Device | What the scroll does | Play | Length |
|---|---|---|---|---|---|---|
| 1 | Hero | Financial planning for every stage of life. | Words that resolve, then the stages gather | The headline sharpens word by word; the polaroid drops in and is taped; a graduation cap, rings, a key, baby shoes and reading glasses land round her portrait one by one, drift a little with the pointer, and tuck into the polaroid as you scroll on, where section 2's frame shows them one at a time | – | 1 screen |
| 2 | As life changes | Hero paragraph 1 | Frame as window | One polaroid frame holds her portrait, then a graduation cap, rings, a key, baby shoes, reading glasses; the four topic pictures grow and shrink as priorities shift | – | 4.2 |
| 3 | Greater clarity | Hero paragraph 2 | A lens | A landscape with one path through it starts as a blur; a clear patch shows the same painting in focus, then the whole of it clears | Move the lens | 3 |
| 4 | What I can help you with | Heading and line | Kinetic headline, then a contents row | The heading crosses the screen huge, then settles small over four cards, one per topic (picture and her heading); each card jumps to its section | – (the cards are links) | 2.4 |
| 5 | Protecting what matters | Topic 1 | Whole-screen mood | The paper greys, rain falls, the umbrella swings up over the home; the home stays dry | Tap to make it pour | 2.8 |
| 6 | Growing your wealth | Topic 2 | Transformation | A seedling grows into a full-grown leafy plant, one frame of a painted clip per step of scroll | – | 2.8 |
| 7 | Life's milestones | Topic 3 | Sideways filmstrip | Polaroids slide past: marriage, a home, children, other major changes | – | 3 |
| 8 | Later life | Topic 4 | Whole-screen mood | The paper warms to golden hour around one wide painting: a couple, seen from behind, watching the sun set over a bay | – | 2.2 |
| 9 | Making sense of financial planning | Heading, follow row | Frame and filmstrip | The centre polaroid is the one to watch | Swipe or arrows | – |
| 10 | What working together looks like | Quote and three steps | A message, then a loop | Typing dots, then her belief arrives as one message from her; the three steps follow, joined by a dashed line; at the end the line runs back from step 3 to step 1, which is what "regularly" means | – | 3 |
| 11 | Let's talk | Contact copy, details, footer | Picture becomes place | Night falls; a painting of Carine in conversation sits on a cream card; a note field opens WhatsApp with the visitor's words | Type and send | – |

Lengths are in screens of scrolling while the section holds. A HUD at the top
names the chapter and fills a progress line; held sections say "keep scrolling".

## The four interactions

1. **The lens** follows the pointer or a finger over the painting, and drifts on its own otherwise. A finger lifting leaves it in place for about two seconds.
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
- **The plant in "Growing your wealth" (second art pass, 19 Nov 2026).** A seedling grows into a full-grown leafy
  plant beside the line "Making sense of investing and long-term wealth accumulation without unnecessary
  complexity." It is a picture of growth over time, not a promise of returns: nothing is on the plant but leaves (no
  coins, currency, fruit, flowers or rising line) and no figure appears near it. The rain tree painted in the same
  pass appears only as the fourth video placeholder. For Carine's compliance team to clear with that wording beside
  it. Not yet cleared by compliance.
- **The café painting in "Let's talk" (second art pass).** It is an AI-made painting of Carine, drawn from her own
  portrait, talking with a client who is seen only from behind (no face). The same painting is cropped for the
  second video placeholder. **Carine is fine with her likeness being used here** (confirmed by MJ, 19 Nov 2026).
  The painting was redrawn later that day (`5-cafe-v2`) so that she faces the client and is plainly in conversation;
  show her the new one.
  This link is a staging site, not production; raise it again with her compliance team before production.
- **The couple in "Planning for later life"** are seen from behind, with no faces, and stand for no real client.
- **The priority pictures in section 2** resize per life stage to show "different financial priorities". They illustrate the sentence; they are not advice. Compliance should confirm they are comfortable with it.
- **The chat bubbles** are hand-drawn, not WhatsApp's branding, and every bubble is Carine's own copy.
- **The note field** sends nothing anywhere itself; it only opens WhatsApp.
- **Search:** `noindex` on the page, plus the site-wide `Disallow` in `robots.txt`.

---

## Budgets, measured

Measured on 19 Nov 2026 after the second art pass, in headless Chromium against a local copy of the repo: page and
images as stored (not compressed in transit), the three web fonts not counted. The same measure on the page before
the art pass is in the last column.

| | Phone target | Measured | Before the art pass |
|---|---|---|---|
| Before the first screen is usable | 1.5 MB | 705 KB | 548 KB |
| Whole page, phone (390 × 844) | 8 MB | 1.5 MB (1,527 KB) | 920 KB |
| Whole page, laptop (1440 × 900) | 20 MB | 1.7 MB (1,685 KB) | 920 KB |
| Script | 350 KB | about 15 KB inline, no libraries | 14 KB |

On the staging link (GitHub Pages) on 19 Nov 2026, in Chrome at 1654 × 928 on a 2x screen, as transferred and with
fonts: 683 KB before the first screen is usable (a 20 KB page, 589 KB of pictures, 74 KB of fonts) and 1.9 MB after a
full scroll (84 requests, none failed). A 2x screen takes the larger copy of each painting, so this is the heavy case.

The growth clip is 56 frames (391 KB in all), fetched when "Growing your wealth" is one screen away. The rain is
drawn on a canvas only while that section is on screen. With JavaScript off, browsers ignore lazy loading, so every
picture loads up front (about 1.3 MB); the page still reads from the first screen.

## Fallbacks

- **Reduced motion, or no JavaScript:** the page renders as a finished still
  page, every section in its end state, nothing animating.
- **Held sections never trap:** they are plain scroll distance with a sticky stage.
- **WhatsApp** is one tap away at every point, from the anchored button.

## How it is built

- One file, `previews/05-story.html`, with images in `previews/kit/` (`kit/wc2/` for the second art pass; the
  colour wash behind the hero portrait and the two tapes are still from `kit/wc/`).
- Each held section is a tall block with a sticky stage. Its scroll position
  becomes one progress value from 0 to 1, written as a CSS variable, and a small
  handler per section maps that to what moves.
- The hero's objects stack three motions on separate CSS properties so they never fight: the arrival animates
  `transform`, the pointer drift and the tuck-away on scroll move `translate` and `scale`, and the resting tilt is
  `rotate`. With reduced motion or no JavaScript they rest in place.
- "Growing your wealth" draws the clip's frames to a canvas by scroll progress. The frames are opaque on white and
  are multiplied onto the paper. A pinned stage is its own layer, so multiply cannot reach the page's paper behind
  it: the scene carries the same paper itself (`--grain`).

## Second art pass (19 Nov 2026)

The first set of pictures was painted in code and read as child-like beside Carine's portrait. They were replaced
with eight paintings made in ChatGPT (one chat, her portrait as the style reference) and one 8-second clip made in
Google Flow (Frames to Video, 16:9, 720p, **Omni 1.2 Flash**, seedling as the start frame and the full-grown plant
as the end frame). The prompts are in `previews/art/ART-BRIEF-05.md`.

- **Originals:** `previews/art/gen/` (`1-tree` to `8-clarity`, `9-growth.mp4`, `9-plant-endframe.png`). Never
  overwritten; a correction gets `-v2` (`5-cafe-v2` is the café painting on the page). `10-money-tree.png` is a
  proposed new end for the growth clip (a braided money tree, leaves only); not on the page yet.
- **Export:** from `previews/art`, `python3 -I prep.py gen ../kit/wc2 gen-sheet.jpg` (Pillow, NumPy, SciPy and
  ffmpeg). It turns white into transparency without a threshold, so soft edges and shadows survive; cuts the
  object and topic grids apart on their white gaps; keeps the scenes solid in the middle and soft at the edge; makes
  the blurred copy of the landscape for the lens; and cuts the growing part of the clip (its first 3.3 seconds)
  into 56 square frames.
- **Changed sections:** hero (sparkle sticker removed, tape calmed, the five life-stage objects added round the
  portrait), 2 to 8 and 11 in the table above, and the
  video placeholders (crops of the later-life, café and landscape paintings, and the rain tree).
- **Not used:** the three in-between tree stages (`3-stages`) and the seedling still (`2-seedling`), which were
  for building the growth from stills; the clip does that job.
- The earlier art sources (`paint.html`, `paint.js`, `towebp.py`) made the `kit/wc/` pictures; only the hero wash
  and the tapes from that set are still on the page.

## Tested, and not

Tested on 19 Nov 2026 in headless Chromium against a local copy: a frame-by-frame scroll through every section at
1440 × 900, 390 × 844 and 320 × 640 with no horizontal scrolling, no script errors and no failed requests; all four
interactions at laptop and phone size (the lens with a mouse, a tap and a finger drag; pour, with nothing landing
under the umbrella; the video row by arrows and by swipe; the note, with and without text, opening the right
WhatsApp link); each of the four topic cards jumping to its section; the reduced-motion page and the page with JavaScript off; and every line of the v1 copy, link,
phone number and address unchanged from before the art pass. After the push, the staging link was opened in Chrome
(1654 × 928) and scrolled end to end: no failed requests, no broken pictures, no console errors, no sideways scroll,
and the growth clip played; it was also opened at 500 px wide in a second browser.

"What working together looks like" was redrawn on 22 Nov 2026 (the stray repeat mark became a loop through the three
steps; her belief is the only chat bubble; no wording changed). Checked at 1440 × 900, 1280 × 720, 1024 × 768,
820 × 1180, 412 × 780, 390 × 844 and 390 × 664, where the whole card fits, and with reduced motion and JavaScript off.
The old version squeezed its bubbles and cut their last lines at 390 px as well as 320 px; that is fixed.

Known: on screens about 640 px tall or less (375 × 548, 360 × 640, 320 × 568) the finished card is taller than the
space under the heading, so by step 3 her opening line, and on the smallest part of step 1, has slid up out of the
top of the card, the way older messages do in a chat. Nothing is cut mid-line; scrolling back brings it down again.

Not yet tested: real phones (iPhone Safari and an older Android), the in-app browsers of Instagram, Facebook and
WhatsApp, a throttled connection, frame rate, a keyboard-only pass, and a screen reader.
