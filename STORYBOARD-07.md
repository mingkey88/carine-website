# Storyboard: design 07, "The living picture"

Design 07 (`previews/07-living.html`) is design 06 with its middle rebuilt. Design 06 is unchanged, so Carine can
compare the two. Everything in `STORYBOARD-06.md` still applies to the parts that are the same: the cover, the
album that opens, plan-model-picture, the videos row, "What working together looks like", and "Start your album".

Built and pushed to the staging link on 23 Nov 2026. A preview: not production.

---

## The idea

In design 06, "Into focus" ends on the painted cottage, and then the page drops it and goes back to small cut-outs
on blank paper. The visitor watches a life being planned and never sees it lived.

In design 07 the cottage stays on screen and her four areas happen inside it, across one day's light. Each ends
with a shutter click and the frame drops out as a print. The four prints are waiting on "your first page" at the
end, beside the pages the visitor chooses.

It replaces five sections of design 06 (the four prints that turned over, and the four topic sections) with one
held scene of about twelve screens.

## The scene

| # | Chapter | Her words (unchanged) | What the scroll does | Camera | Print |
|---|---|---|---|---|---|
| – | Step in | "What I can help you with", "Planning for what matters at every stage." | The framed painting settles into place | Whole picture | – |
| 1 | Protecting what matters | Topic 1 | Storm cloud rolls over, the colour drains, rain falls, the windows light up; an umbrella swings up over the home and it is bright and dry under it; the storm passes | Moves in on the house | rain or shine |
| 2 | Growing your wealth | Topic 2 | A sapling appears on the stream bank and grows, one frame per step of scroll | Moves in on the bank | planted early |
| 3 | Planning around life's milestones | Topic 3 | Four arrivals, each labelled with her own word: a flower arch on the bridge and bunting on the veranda (marriage); a picket fence, a mailbox, a bicycle and chimney smoke (a home); a swing from the big tree and a kite (children); a hot-air balloon over the far hills (other major changes) | Visits each in turn | moving-in day |
| 4 | Planning for later life | Topic 4 | The light turns to golden hour, the windows glow, two garden chairs are on the lawn | Moves in on the house, then out | golden hour |

"Tap to make it pour" still works during the storm, on the button or on the picture. Nothing needs it.

The header names each chapter as it plays. Links to `#protect`, `#grow`, `#milestones` and `#later` land on that
chapter of the scene (checked: each opens with the right words showing).

## Wording

No wording of hers changed. Her four descriptions now appear once each, not twice. Nothing new was written: the
four print captions ("rain or shine", "planted early", "moving-in day", "golden hour") and the four topic kickers
were already Draft in design 06; "marriage", "a home", "children", "other major changes" are her own words from
topic 3. "tap a photo to turn it over" is gone with the prints that turned.

## Compliance notes (in addition to design 06's)

- **A life shown over time is a picture, not a promise.** The scene shows a storm, a plant, some arrivals and an
  evening. The words beside it are hers and say "planning", "preparing" and "building towards". Compliance should
  see the whole scene play and confirm it reads as illustration.
- **No people at all** are in the scene: not a couple, not a child, not a client. Marriage is an arch of flowers;
  children are a swing and a kite; later life is two empty chairs.
- **Weather only** for protection: no illness, accident or loss.
- **The plant is the same plant as designs 05 and 06**: leaves only, no coins, fruit or figures.
- **"Your first page" now starts with four prints on it.** They are the site's illustrations, not the visitor's
  data; nothing about the visitor is stored or sent until they press the WhatsApp button, as before.

## Art, and what is still to make

**No new paintings and no video were made for this build.** The plan was about eight "same picture, but…" edits in
ChatGPT and one Flow clip (Omni 1.2 Flash) of a tree growing in the scene. On the afternoon of 23 Nov the Chrome
link dropped and the built-in browser was not signed in to ChatGPT, so neither could be reached. The scene was
built from what was already in the repo:

- **The one cottage painting** (`clarity.webp`) is the only base. Storm, cloud, dusk, sun and lit windows are
  layers of colour laid over it in CSS, so nothing can drift out of line.
- **The umbrella** is the design-05 painting (`umbrella-air.webp`).
- **The plant** is the design-05 growth clip, cut out with a proper matte so it can stand in the meadow
  (`kit/wc2/grow-a/`, 28 frames, made by `prep.py`).
- **The arrivals** (arch, bunting, fence, mailbox, bicycle, smoke, swing, kite, balloon, chairs) are drawn in SVG
  through a watercolour filter. They are the weakest art on the page: flatter than the painting they sit in.
- **The four prints** are photographs of the live scene (`previews/art/bake-snaps.js`).

To finish it properly, in this order: (1) the Flow clip of a sapling growing into a tree on the stream bank,
replacing the leafy plant; (2) painted versions of the arrivals, as edits of the cottage painting; (3) a painted
storm and a painted dusk, if the colour layers look too digital beside real paint.

## How it is built

One held section (`.life`, 12.5 screens). The scroll gives one number, 0 to 1, and a single function reads its own
stretches of it and writes about a dozen CSS variables on the section (`--storm`, `--open`, `--gold`, `--lit`,
`--planted`, `--a1` to `--a5`, `--flash`). The picture's layers read those variables. A small table of camera
positions pans and zooms inside the frame. Only the rain runs on the clock.

A print's flight from the picture to its place in the row is measured, not guessed: on layout the script works
out how far and how much smaller each print's window is than the picture, and the print starts exactly over it.

With reduced motion or no JavaScript there is no scene. The section is her heading and then each area as its
print with her words beside it; the live picture's files are not fetched.

`previews/art/build-07.py` is the script that made the first version of the file from design 06.

## Tested, and not

Tested on 23 Nov 2026 in headless Chromium against a local copy:

- The scene frame by frame at 1440 × 900; stills at 1024 × 768, 390 × 664 and 390 × 844.
- Scripted checks at 1440 × 900, 1024 × 768 and 390 × 664: exactly one chapter's words showing at five points
  down the scene, and the header naming the same chapter; the picture and the words inside the screen each time;
  the pour button reachable during the storm; all four prints landed and on screen at the end, and gone again
  after scrolling back to the top; every picture loaded; the four anchors present; no sideways scroll; no errors.
- The full page end to end at 1440 × 900 and 390 × 664, with reduced motion, and with JavaScript off.

Not tested: real phones, in-app browsers, a throttled connection, frame rate (the scene stacks several blended
layers and should be watched on an older phone), a keyboard-only pass, a screen reader, and the WhatsApp chooser
in design 07 (its code is unchanged from design 06, but the 32 checks from that build were not re-run).
