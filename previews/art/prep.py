# Second art pass for design 05: turn the generated paintings in gen/ into the WebP files the page uses.
# Usage (from previews/art): python3 -I prep.py gen ../kit/wc2 gen-sheet.jpg
#
# White becomes transparency by "un-multiplying" it: each pixel keeps exactly the ink that was laid over
# white paper, so soft watercolour edges and shadows fade into whatever paper sits behind them, with no
# threshold and no halo. Grids are cut on the white gaps between items, then trimmed.
import json
import os
import sys

import numpy as np
from PIL import Image, ImageChops, ImageFilter
from scipy import ndimage as ndi

src, out, sheet_out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
PAPER = (244, 234, 214)
WHITE = 250.0  # the generator's "pure white" is 252 to 255 with a little grain; treat 250 and up as paper
report = {}


def load(name):
    return np.asarray(Image.open(os.path.join(src, name)).convert('RGB')).astype(np.float32)


def unmultiply(rgb):
    c = np.clip(rgb * (255.0 / WHITE), 0, 255)
    a = 1.0 - c.min(axis=2) / 255.0
    a = np.where(a < 0.02, 0.0, a)
    safe = np.maximum(a, 1e-4)[..., None]
    col = np.clip((c - (1.0 - a[..., None]) * 255.0) / safe, 0, 255)
    col = np.where(a[..., None] > 0, col, 255.0)
    return np.dstack([col, a * 255.0]).round().astype(np.uint8)


def trim(rgba, pad=10):
    ys, xs = np.where(rgba[..., 3] > 8)
    y0, y1 = max(ys.min() - pad, 0), min(ys.max() + pad + 1, rgba.shape[0])
    x0, x1 = max(xs.min() - pad, 0), min(xs.max() + pad + 1, rgba.shape[1])
    return rgba[y0:y1, x0:x1]


def scene(rgb, feather=40, holes=0):
    """A painting that keeps its own soft edge: solid inside, un-multiplied only where it meets the paper.
    With holes set, patches of bare paper inside the picture bigger than that many pixels are let through too."""
    full = unmultiply(rgb).astype(np.float32)
    a_un = full[..., 3] / 255.0
    lab, n = ndi.label(rgb.min(axis=2) > 236)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    if holes:
        area = ndi.sum(np.ones_like(lab), lab, range(1, n + 1))
        edge |= {i + 1 for i, v in enumerate(area) if v >= holes}
    # e runs from 1 at the paper to 0 once `feather` pixels inside the painting, so pale washes near the edge let
    # the ground through (no white fringe on a coloured ground) while the middle of the picture stays solid.
    dist = ndi.distance_transform_edt(~np.isin(lab, list(edge)))
    e = 1 - np.clip(dist / feather, 0, 1)
    e = ndi.gaussian_filter(e * e * (3 - 2 * e), 1.5)
    a = a_un * e + (1 - e)
    c = np.clip(rgb * (255.0 / WHITE), 0, 255)
    col = np.clip((c - (1.0 - a[..., None]) * 255.0) / np.maximum(a, 1e-4)[..., None], 0, 255)
    col = np.where(a[..., None] > 0, col, 255.0)
    return np.dstack([col, a * 255.0]).round().astype(np.uint8)


def save(rgba, name, cap=None, q=76):
    im = Image.fromarray(rgba, 'RGBA' if rgba.shape[2] == 4 else 'RGB')
    if cap and max(im.size) > cap:
        im.thumbnail((cap, cap), Image.LANCZOS)
    dst = os.path.join(out, name + '.webp')
    im.save(dst, 'WEBP', quality=q, alpha_quality=60, method=6)
    report[name] = {'w': im.size[0], 'h': im.size[1], 'kb': round(os.path.getsize(dst) / 1024, 1)}
    return im


def runs(mask_1d):
    out_, start = [], None
    for i, v in enumerate(mask_1d):
        if v and start is None:
            start = i
        if not v and start is not None:
            out_.append((start, i - 1))
            start = None
    if start is not None:
        out_.append((start, len(mask_1d) - 1))
    return out_


def cuts(mask_1d, n, length):
    """Cut positions for n items: the middles of the n - 1 widest white gaps."""
    r = runs(mask_1d)
    gaps = sorted(((r[i + 1][0] - r[i][1], (r[i][1] + r[i + 1][0]) // 2) for i in range(len(r) - 1)), reverse=True)
    assert len(gaps) >= n - 1, (len(gaps), n)
    return [0] + sorted(mid for _, mid in gaps[:n - 1]) + [length]


def cells(rgb, cols, rows):
    """Cut a grid on the middles of its white gaps, row by row."""
    ink = rgb.min(axis=2) < 244
    ycuts = cuts(ink.sum(axis=1) > 2, rows, rgb.shape[0])
    out_ = []
    for r in range(rows):
        band = rgb[ycuts[r]:ycuts[r + 1]]
        xcuts = cuts((band.min(axis=2) < 244).sum(axis=0) > 2, cols, rgb.shape[1])
        for c in range(cols):
            out_.append(band[:, xcuts[c]:xcuts[c + 1]])
    return out_


# 6: six life-stage objects, three across and two down
for name, cell in zip(['cap', 'rings', 'key', 'shoes', 'glasses', 'briefcase'], cells(load('6-objects.png'), 3, 2)):
    save(trim(unmultiply(cell)), name, cap=380)

# 7: the four planning pictures, two by two
for name, cell in zip(['umbrella', 'sprout', 'house', 'sunset'], cells(load('7-icons.png'), 2, 2)):
    # The home is solid inside (soft only at its edge): it stands in front of the umbrella in "Protecting what matters".
    t = trim(scene(cell, feather=10, holes=120) if name == 'house' else unmultiply(cell))
    if name == 'umbrella':
        save(t, 'umbrella-full', cap=560)  # the source for umbrella-air below; not used by the page
    save(t, name, cap={'house': 560}.get(name, 400))

# The umbrella again without its ground shadow, for where it is held up over the home
u = np.asarray(Image.open(os.path.join(out, 'umbrella-full.webp')).convert('RGBA')).astype(np.float32)
os.remove(os.path.join(out, 'umbrella-full.webp'))
del report['umbrella-full']
hh = u.shape[0]
wood = (u[..., 0] > u[..., 2] + 25) & (u[..., 3] > 60)
lab, n = ndi.label(wood)
wood = lab == (1 + int(np.argmax(ndi.sum(wood, lab, range(1, n + 1)))))  # the handle is the biggest warm shape
wood = np.clip(ndi.gaussian_filter(ndi.binary_dilation(wood, iterations=2).astype(np.float32), 1.2) * 1.6, 0, 1)
rows = (np.arange(hh) / hh)[:, None]
fade = np.clip((0.835 - rows) / 0.04, 0, 1)
cloth = (u[..., 2] > u[..., 0] + 8) & (u[..., 3] > 150)
cloth = ndi.gaussian_filter(ndi.binary_dilation(cloth, iterations=5).astype(np.float32), 1.5)
faint = np.where(rows > 0.74, cloth, 1.0)  # below here only the cloth and the handle stay; the wash of shadow goes
u[..., 3] *= np.maximum(fade * np.clip(faint * 1.4, 0, 1), wood)
save(trim(u.round().astype(np.uint8), pad=6), 'umbrella-air')

# 9: "Growing your wealth" plays the Flow clip (seedling to full-grown plant) as a short image sequence.
# Only the growing part is kept (the first 3.3 seconds; the clip then holds still), cut to a square around the
# plant. Frames stay opaque on pure white: the page lays them over the paper with mix-blend-mode: multiply, which
# keeps them about a third of the size of see-through frames.
import glob
import shutil
import subprocess
import tempfile

FRAMES, LAST, BOX9, SIDE = 56, 80, (330, 100, 930, 700), 600
tmp = tempfile.mkdtemp()
subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-i', os.path.join(src, '9-growth.mp4'),
                '-frames:v', str(LAST + 1), os.path.join(tmp, 'f%03d.png')], check=True)
shots = sorted(glob.glob(os.path.join(tmp, '*.png')))
os.makedirs(os.path.join(out, 'grow'), exist_ok=True)
film_kb = 0
for n in range(FRAMES):
    f = np.asarray(Image.open(shots[round(n * LAST / (FRAMES - 1))]).convert('RGB')).astype(np.float32)
    f = f[BOX9[1]:BOX9[3], BOX9[0]:BOX9[2]]
    f = np.clip(f * (255.0 / 246.0), 0, 255)  # the clip's white is about 251 with a little noise; make it pure white
    dst = os.path.join(out, 'grow', 'f%02d.webp' % n)
    Image.fromarray(f.round().astype(np.uint8), 'RGB').resize((SIDE, SIDE), Image.LANCZOS).save(dst, 'WEBP', quality=72, method=6)
    film_kb += os.path.getsize(dst) / 1024
shutil.rmtree(tmp)
report['grow/ (%d frames)' % FRAMES] = {'w': SIDE, 'h': SIDE, 'kb': round(film_kb, 1)}
# The still page (reduced motion, no JavaScript) shows the finished plant, cut from the clip's end-frame painting.
save(trim(unmultiply(load('9-plant-endframe.png'))), 'plant', cap=640)

# 4, 5: scenes keep their own soft edge; white becomes paper
later, cafe = trim(scene(load('4-later-life.png')), pad=4), trim(scene(load('5-cafe-v2.png')), pad=4)
save(later, 'later', cap=1400, q=74)
save(later, 'later-800', cap=800, q=74)
save(cafe, 'cafe', cap=1000, q=76)
save(cafe, 'cafe-640', cap=640, q=76)


def crop_to(rgb, box, size, q=80, name=None, blur=0, fog=0.0):
    x0, y0, x1, y1 = box
    im = Image.fromarray(rgb[y0:y1, x0:x1].round().astype(np.uint8), 'RGB').resize(size, Image.LANCZOS)
    if blur:
        im = im.filter(ImageFilter.GaussianBlur(blur))
    if fog:
        im = Image.blend(im, Image.new('RGB', im.size, (236, 228, 214)), fog)
    dst = os.path.join(out, name + '.webp')
    im.save(dst, 'WEBP', quality=q, method=6)
    report[name] = {'w': im.size[0], 'h': im.size[1], 'kb': round(os.path.getsize(dst) / 1024, 1)}
    return im


# 8: the clear picture fills its frame (16:10, cut from inside the painted area); the muddle is the same
# crop, blurred and fogged, so the lens lines up with it.
BOX8 = json.loads(os.environ.get('BOX8', '[128, 104, 1424, 914]'))
clarity = load('8-clarity.png')
crop_to(clarity, BOX8, (1200, 750), name='clarity', q=74)
crop_to(clarity, BOX8, (760, 475), name='clarity-760', q=74)
crop_to(clarity, BOX8, (480, 300), q=60, name='clarity-muddle', blur=9, fog=0.34)

# Design 07: a tree grows in the cottage scene. The Flow clip (seedling to rain tree on white, the first 3.3 seconds
# are the growth) is cut into frames, and each gets a real matte so it can stand in the meadow: anything with colour
# in it is solid, and only the soft edge and the ground wash are see-through. (Multiply, as used on plain paper in
# designs 05 and 06, would let the meadow show through the leaves.)
def matte(rgb, soft=46.0):
    a = np.clip((255.0 - rgb.min(axis=2)) / soft, 0, 1)
    aa = np.maximum(a, 1e-3)[..., None]
    colour = np.clip((rgb - (1 - a[..., None]) * 255.0) / aa, 0, 255)
    return np.dstack([colour, a * 255.0]).round().astype(np.uint8)

TREE_CLIP, TREE_N = os.path.join(src, '13-tree-growth.mp4'), 30
if os.path.exists(TREE_CLIP):
    import glob, subprocess, tempfile
    tmp = tempfile.mkdtemp()
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', TREE_CLIP, '-vf', 'crop=840:600:220:100', os.path.join(tmp, '%03d.png')], check=True)
    stills = sorted(glob.glob(os.path.join(tmp, '*.png')))
    os.makedirs(os.path.join(out, 'tree'), exist_ok=True)
    for n in range(TREE_N):
        still = stills[round(n * (len(stills) - 1) / (TREE_N - 1))]
        frame = np.clip(np.asarray(Image.open(still).convert('RGB')).astype(np.float32) * 255 / 244, 0, 255)
        cut = Image.fromarray(matte(frame), 'RGBA').resize((434, 310), Image.LANCZOS)
        cut.save(os.path.join(out, 'tree', 't%02d.webp' % n), 'WEBP', quality=68, alpha_quality=70, method=6)

# Design 07: the things that arrive in the scene. '14-lived-in.png' is the cottage painting with them painted in;
# ChatGPT drew it over the original, so the two line up to the pixel. Each arrival is lifted out as a soft-edged
# patch (shapes below are in the 1200 x 750 crop) and laid back over the original, so it can arrive on its own.
LIVED = os.path.join(src, '14-lived-in.png')
if os.path.exists(LIVED):
    from PIL import ImageDraw
    x0, y0, x1, y1 = BOX8
    lived = Image.fromarray(load('14-lived-in.png')[y0:y1, x0:x1].round().astype(np.uint8), 'RGB').resize((1200, 750), Image.LANCZOS)
    def patch(name, shapes, feather=9, holes=()):
        m = Image.new('L', (1200, 750), 0); d = ImageDraw.Draw(m)
        for kind, xy, *w in shapes:
            if kind == 'e': d.ellipse(xy, fill=255)
            elif kind == 'r': d.rounded_rectangle(xy, 14, fill=255)
            else: d.line(xy, fill=255, width=w[0])
        m = m.filter(ImageFilter.GaussianBlur(feather))
        if holes:
            h = Image.new('L', (1200, 750), 255); dh = ImageDraw.Draw(h)
            for xy in holes: dh.rectangle(xy, fill=0)
            m = ImageChops.multiply(m, h.filter(ImageFilter.GaussianBlur(2.5)))
        box = m.point(lambda v: 255 if v > 3 else 0).getbbox()
        im = lived.copy(); im.putalpha(m); im = im.crop(box)
        os.makedirs(os.path.join(out, 'life'), exist_ok=True)
        dst = os.path.join(out, 'life', name + '.webp')
        im.save(dst, 'WEBP', quality=78, alpha_quality=80, method=6)
        report['life/' + name] = {'w': im.size[0], 'h': im.size[1], 'kb': round(os.path.getsize(dst) / 1024, 1),
                                  'css': '--x: %.2f%%; --y: %.2f%%; --w: %.2f%%' % (box[0] / 12.0, box[1] / 7.5, (box[2] - box[0]) / 12.0)}
    patch('arch', [('e', (540, 386, 696, 518))])
    patch('bunting', [('r', (236, 414, 376, 452))], feather=6)
    patch('home', [('r', (-30, 490, 424, 556)), ('e', (368, 452, 448, 520))], feather=7, holes=[(103, 470, 117, 570), (147, 470, 163, 570)])
    patch('swing', [('r', (84, 138, 184, 596))], feather=8)
    patch('kite', [('e', (702, 76, 802, 190)), ('l', (735, 165, 462, 478), 9)], feather=6)
    patch('balloon', [('e', (808, 243, 860, 307))], feather=6)
    patch('chairs', [('e', (446, 462, 544, 522))], feather=7)

# Design 06: the same cottage as a blueprint and as a white model. ChatGPT redrew them over the painting, so the
# same crop keeps all three lined up to the pixel and one can turn into the next.
for original, stage in (('11-blueprint.png', 'plan'), ('12-model.png', 'model')):
    if os.path.exists(os.path.join(src, original)):
        picture = load(original)
        crop_to(picture, BOX8, (1200, 750), name=stage, q=70)
        crop_to(picture, BOX8, (760, 475), name=stage + '-760', q=70)

# Video placeholders: 16:10 crops of 4, 5, 8 and the tree (on paper)
crop_to(load('4-later-life.png'), json.loads(os.environ.get('BOXV1', '[330, 190, 1290, 790]')), (640, 400), name='v1', q=76)
crop_to(load('5-cafe-v2.png'), json.loads(os.environ.get('BOXV2', '[230, 80, 1430, 830]')), (640, 400), name='v2', q=76)
crop_to(clarity, json.loads(os.environ.get('BOXV3', '[330, 300, 1290, 900]')), (640, 400), name='v3', q=76)
tree = Image.fromarray(trim(unmultiply(load('1-tree.png')), pad=40), 'RGBA')
bg = Image.new('RGB', (1120, 700), (246, 236, 216))
tree.thumbnail((1000, 640), Image.LANCZOS)
bg.paste(tree, ((1120 - tree.width) // 2, 700 - tree.height - 10), tree)
bg = bg.resize((640, 400), Image.LANCZOS)
bg.save(os.path.join(out, 'v4.webp'), 'WEBP', quality=76, method=6)
report['v4'] = {'w': 640, 'h': 400, 'kb': round(os.path.getsize(os.path.join(out, 'v4.webp')) / 1024, 1)}

# Contact sheet on the paper colour, to check edges for halos
tiles = []
for f in sorted(os.listdir(out)):
    if f.endswith('.webp'):
        t = Image.open(os.path.join(out, f)).convert('RGBA')
        t.thumbnail((380, 300))
        tiles.append(t)
W, gap, x, y, rowh, placed = 1600, 18, 0, 0, 0, []
for t in tiles:
    if x + t.width > W:
        x, y, rowh = 0, y + rowh + gap, 0
    placed.append((t, x, y))
    x += t.width + gap
    rowh = max(rowh, t.height)
sheet = Image.new('RGB', (W, y + rowh), PAPER)
for t, px, py in placed:
    sheet.paste(t, (px, py), t)
sheet.save(sheet_out, quality=86)

total = sum(v['kb'] for k, v in report.items() if not k.startswith('_'))
for k, v in report.items():
    print(k, v)
print('total KB', round(total, 1))
