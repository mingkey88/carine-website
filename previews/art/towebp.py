# Convert painted PNGs to WebP and make a contact sheet on the paper colour.
# Usage: python3 -I towebp.py <png-dir> <webp-dir> <sheet.jpg>
import os
import sys
from PIL import Image

png_dir, webp_dir, sheet_out = sys.argv[1:4]
os.makedirs(webp_dir, exist_ok=True)
tiles = []
for f in sorted(os.listdir(png_dir)):
    if not f.endswith('.png'):
        continue
    name = f[:-4]
    im = Image.open(os.path.join(png_dir, f)).convert('RGBA')
    # Stickers display at about 150px; keep 2x of that, not the 600px they were painted at.
    cap = {'umbrella': 340, 'sprout': 340, 'house': 340, 'sunrise': 340, 'moon': 360, 'sparkle': 240, 'tape-gold': 280, 'tape-blue': 280, 'teacups': 680, 'cap': 340, 'rings': 340, 'key': 340, 'shoes': 340, 'glasses': 340, 'briefcase': 340, 'sun': 420}.get(name)
    if cap:
        im.thumbnail((cap, cap), Image.LANCZOS)
    q = 72 if name in ('bloom', 'route', 'messy', 'hills') else 80
    dst = os.path.join(webp_dir, name + '.webp')
    im.save(dst, 'WEBP', quality=q, method=6)
    print(f"{name:10s} {im.size[0]}x{im.size[1]}  {os.path.getsize(dst) // 1024}KB")
    if name != 'paper':
        tiles.append(im)

W, gap = 1600, 16
x = y = rowh = 0
placed = []
for im in tiles:
    t = im.copy()
    t.thumbnail((520, 360))
    if x + t.width > W:
        x, y, rowh = 0, y + rowh + gap, 0
    placed.append((t, x, y))
    x += t.width + gap
    rowh = max(rowh, t.height)
sheet = Image.new('RGB', (W, y + rowh), (244, 234, 214))
for t, px, py in placed:
    sheet.paste(t, (px, py), t)
sheet.save(sheet_out, quality=85)
