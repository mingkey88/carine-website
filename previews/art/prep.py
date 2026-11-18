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
from PIL import Image, ImageFilter
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


def ground(rgba):
    """Where a plant meets the ground: x of the trunk at its base, as fractions of the trimmed picture."""
    a = rgba[..., 3] > 40
    h, w = a.shape
    band = a[int(h * 0.80):int(h * 0.90)]  # just above the grass, where only the stem or trunk is
    xs = np.where(band.any(axis=0))[0]
    # the trunk is the densest run of columns in that band
    col = band.sum(axis=0)
    cx = float((col * np.arange(w)).sum() / max(col.sum(), 1))
    return round(cx / w, 4)


# 6: six life-stage objects, three across and two down
for name, cell in zip(['cap', 'rings', 'key', 'shoes', 'glasses', 'briefcase'], cells(load('6-objects.png'), 3, 2)):
    save(trim(unmultiply(cell)), name, cap=380)

# 7: the four planning pictures, two by two
for name, cell in zip(['umbrella', 'sprout', 'house', 'sunset'], cells(load('7-icons.png'), 2, 2)):
    # The home is solid inside (soft only at its edge): it stands in front of the umbrella in "Protecting what matters".
    t = trim(scene(cell, feather=10, holes=120) if name == 'house' else unmultiply(cell))
    if name == 'umbrella':
        save(t, 'umbrella-full', cap=560)  # the source for umbrella-air below; not used by the page
    save(t, name, cap={'house': 560, 'umbrella': 260}.get(name, 320))

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

# 1, 2, 3: the tree's life, for "Growing your wealth"
grow = {}
for name, cell in zip(['g2-sapling', 'g3-young', 'g4-half'], cells(load('3-stages.png'), 3, 1)):
    t = trim(unmultiply(cell))
    save(t, name, cap=640)
    grow[name] = {'gx': ground(t), 'h': t.shape[0], 'w': t.shape[1]}
for name, file in (('g1-seedling', '2-seedling.png'), ('g5-tree', '1-tree.png')):
    t = trim(unmultiply(load(file)))
    save(t, name, cap=880)
    grow[name] = {'gx': ground(t), 'h': t.shape[0], 'w': t.shape[1]}
report['_grow'] = grow

# 4, 5: scenes keep their own soft edge; white becomes paper
later, cafe = trim(scene(load('4-later-life.png')), pad=4), trim(scene(load('5-cafe.png')), pad=4)
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

# Video placeholders: 16:10 crops of 4, 5, 8 and the tree (on paper)
crop_to(load('4-later-life.png'), json.loads(os.environ.get('BOXV1', '[330, 190, 1290, 790]')), (640, 400), name='v1', q=76)
crop_to(load('5-cafe.png'), json.loads(os.environ.get('BOXV2', '[520, 75, 1450, 656]')), (640, 400), name='v2', q=76)
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
