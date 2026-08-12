# Assets needed

The page renders and reads correctly as it stands. One real asset would lift it
considerably, and it is deliberately not faked.

---

## 1. Portrait of Carine (done)

| | |
|---|---|
| **Path** | `assets/img/carine.jpg` + `assets/img/carine.webp` |
| **Size** | 1200 x 1500, 4:5 |
| **Weight** | 124KB JPEG, 50KB WebP |
| **Where** | Hero, right column |

### How it was processed

The supplied original is `Carine Zheng.jpg`: 6083 x 9124, 26.3MB, shot on a Sony
A7R IV at 85mm f/1.4. **The original is not in this repository.** 26MB of binary
does not belong in git, and it is not needed at runtime. Keep it somewhere safe;
you will want it if the crop ever needs redoing.

Steps applied:

1. **Cropped** to `(913, 456) -> (5292, 5930)`, which is 4:5, running from just
   above her head down through the crossed arms. The full-length original loses
   her face at the size this renders (417 x 521 on desktop).
2. **Resized** to 1200 x 1500, Lanczos. That covers 2x retina for the largest
   viewport the slot reaches.
3. **Stripped EXIF.** Removes camera body, serial number and any GPS, and saves
   a few KB.
4. **Exported** JPEG at q82 progressive, plus WebP at q80, served through a
   `<picture>` element so browsers take the smaller file.

Net: 26.3MB to 50KB for most browsers, a 99.8% reduction.

### Notes on the shot itself

- It is a **navy blazer against a white curtain**: cool-toned, where the page is
  warm greige. It reads fine, but it does not have the warm natural light of the
  Halden reference. No colour grading was applied, because altering someone's
  photo is not a change to make unasked. Say the word and I will warm it
  slightly to sit better against the page.
- **Rights are unconfirmed.** Logged in CONTENT-QUERIES.md as query 1.5.

**Never substitute a stock photo or an AI-generated face.** This is a real,
licensed person.

---

## 2. Social share image (optional)

| | |
|---|---|
| **Path** | `assets/img/og.jpg` |
| **Size** | 1200 x 630 |
| **Where** | `og:image` / `twitter:image` meta tags |

The Open Graph tags are in place but carry no image, so links currently unfurl
as text only. Add the file, then add to `<head>`:

```html
<meta property="og:image" content="assets/img/og.jpg">
<meta name="twitter:image" content="assets/img/og.jpg">
```

Also set `og:url` to the real domain once hosting is decided.

---

## 3. Favicon (optional)

`favicon.svg` plus `apple-touch-icon.png` at 180 x 180. A "C" monogram in IBM
Plex Serif, warm off-white (`#f7f7f2`) on the near-black (`#191818`), would match
the nav button.

---

## 4. Photography, beyond the portrait

The design follows the [Halden Miller
template](https://halden-miller.webflow.io/), which is roughly **70%
photography**: 34 images, with every section carried by warm, natural-light
shots. This page currently has none.

It reads as clean and sparse right now. It is not going to reach the reference's
warmth on typography alone. If the budget allows one thing, make it a proper
shoot rather than more design work.

What a session should produce, in priority order:

| Priority | Shot | Where it would go |
|---|---|---|
| 1 | Portrait, 4:5, plain or softly blurred background | Hero, section 1 above |
| 2 | Carine mid-conversation with a client, landscape | Beside "How working together looks" |
| 3 | Working detail: hands, documents, laptop, desk | Between the topic grid and the process |
| 4 | Environmental, wider, in the office | Contact section |

Direction that matches the reference: **natural window light, warm tones, no
harsh flash, no grey studio backdrop, no posed arms-folded corporate stance.**
Candid over formal.

**Do not substitute stock photography.** Lifestyle stock of strangers on an
adviser's site implies they are her clients, which is misleading. The reference
can use it because it openly says "Halden Miller is a fictional consulting
firm". Carine is real.

---

## Already handled

- **Fonts.** IBM Plex Serif, Sans and Mono are self-hosted in `assets/fonts/`
  as latin-subset woff2, about 81KB total. No requests leave the page, so
  nothing breaks offline or behind a corporate proxy.
- **Icons.** None used. Contact details are set typographically, so there is no
  icon library to license or maintain.
