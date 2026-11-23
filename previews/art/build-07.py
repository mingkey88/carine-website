# Builds previews/07-living.html from previews/06-album.html: the flip cards and the four topic sections become one
# held scene ("one picture, lived in"). Run from the repo root: python3 previews/art/build-07.py. It was the working script for the first build; edit 07-living.html directly from now on.
import math, re

SRC, DST = 'previews/06-album.html', 'previews/07-living.html'
s = open(SRC, encoding='utf-8').read()

def cut(text, start, end):
    a = text.index(start); b = text.index(end, a)
    return a, b

# ------------------------------------------------------------------ labels
s = s.replace('Design preview 06 · Album, the site told as an album of memories still to be made.',
              'Design preview 07 · The living picture: design 06 with her four areas told inside one painting.')
s = s.replace('<div class="tag tag--mock">Design preview 06 · not live</div>', '<div class="tag tag--mock">Design preview 07 · not live</div>')

# ------------------------------------------------------------------ the painted arrivals (SVG, in picture pixels 1200 x 750)
def arch_flowers():
    out, cols = [], ['#fffaf2', '#f6c3cd', '#f1a2b3', '#fbe0a2', '#fffaf2', '#f6c3cd']
    for i in range(19):
        t = i / 18.0
        ang = math.pi * (1 - t)                     # left foot, over the top, right foot
        x = 700 + 28 * math.cos(ang) + (3 if i % 2 else -3) * math.sin(ang) * .6
        y = 487 - 69 * math.sin(ang) ** .8 + (2 if i % 3 else -2)
        r = 3.3 + (i * 7 % 5) * .42
        out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="#a8667033" stroke-width=".6"/>' % (x, y, r, cols[i % len(cols)]))
        if i % 2 == 0:
            out.append('<ellipse cx="%.1f" cy="%.1f" rx="3.4" ry="1.6" fill="#55793f" transform="rotate(%d %.1f %.1f)"/>' % (x + 4, y + 3, 30 + i * 17, x + 4, y + 3))
    return ''.join(out)

def bunting():
    p0, p1, p2 = (298, 339), (378, 392), (458, 352)
    out, cols = ['<path d="M%d %d Q%d %d %d %d" fill="none" stroke="#6b4a2e" stroke-width="1"/>' % (p0 + p1 + p2)], ['#fff6e6', '#e9a3ae', '#f1d28a', '#a9c7a0']
    n = 10
    for i in range(n):
        ta, tb = (i + .12) / n, (i + .88) / n
        def q(t):
            return ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0], (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1])
        ax, ay = q(ta); bx, by = q(tb); mx, my = (ax + bx) / 2, (ay + by) / 2 + 13
        out.append('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f Z" fill="%s" stroke="#5b3a2266" stroke-width=".7"/>' % (ax, ay, bx, by, mx, my, cols[i % 4]))
    return ''.join(out)

def fence():
    out, x0, y0, x1, y1 = [], 238.0, 561.0, 506.0, 515.0
    n = 21
    def at(t): return x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
    gate = (11, 12)
    for seg in ((0, 10), (13, 20)):
        (ax, ay), (bx, by) = at(seg[0] / (n - 1.0)), at(seg[1] / (n - 1.0))
        for dy in (-10.5, -4.5):
            out.append('<path d="M%.1f %.1f L%.1f %.1f" fill="none" stroke="#fffaf0" stroke-width="2.4" stroke-linecap="round"/>' % (ax - 2, ay + dy, bx + 2, by + dy))
    for i in range(n):
        if i in gate: continue
        x, y = at(i / (n - 1.0)); h = 15.5 + (i * 5 % 3) * .7
        out.append('<path d="M%.1f %.1f v%.1f l2.6 -3 l2.6 3 v%.1f Z" fill="#fffaf0" stroke="#8a6f5699" stroke-width=".7" stroke-linejoin="round"/>' % (x - 2.6, y, -h, h))
    gx, gy = at(11.5 / (n - 1.0))
    out.append('<path d="M%.1f %.1f v-22" fill="none" stroke="#6b4a2e" stroke-width="2.2" stroke-linecap="round"/><rect x="%.1f" y="%.1f" width="15" height="9.5" rx="4" fill="#c2553f" stroke="#5b3a22" stroke-width=".9"/><path d="M%.1f %.1f v-7 h5" fill="none" stroke="#f0c04b" stroke-width="1.6" stroke-linecap="round"/>' % (gx + 17, gy + 2, gx + 9.5, gy - 30, gx + 22, gy - 26))
    return ''.join(out)

LIFE_SVG = '''<svg class="world__life" viewBox="0 0 1200 750" preserveAspectRatio="none" focusable="false">
              <defs><filter id="wc" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency=".07" numOctaves="2" seed="4" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="2.2"/><feGaussianBlur stdDeviation=".28"/></filter><filter id="soft"><feGaussianBlur stdDeviation="2.4"/></filter></defs>
              <g class="lf lf--1">
                <g class="lf__arch" filter="url(#wc)"><path d="M672 487 C671 441 682 418 700 418 C718 418 729 441 728 487" fill="none" stroke="#5f8246" stroke-width="7.5" stroke-linecap="round"/>''' + arch_flowers() + '''</g>
                <g class="lf__bunt" filter="url(#wc)">''' + bunting() + '''</g>
              </g>
              <g class="lf lf--2">
                <g class="lf__smoke" filter="url(#soft)"><circle cx="157" cy="274" r="6" fill="#fff"/><circle cx="161" cy="258" r="8" fill="#fff"/><circle cx="168" cy="240" r="10" fill="#fff"/></g>
                <g class="lf__fence" filter="url(#wc)">''' + fence() + '''</g>
                <g class="lf__bike" filter="url(#wc)" fill="none" stroke="#39445c" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="392" cy="512" rx="20" ry="2.6" fill="#3a271a2e" stroke="none"/><circle cx="379" cy="501" r="9.5"/><circle cx="405" cy="501" r="9.5"/><path d="M379 501 L388 486 L400 486 L405 501 M388 486 L393 501 L379 501 M393 501 L400 486 M386 482 L391 482 M400 486 L398 479 L403 478" stroke="#b9503a"/></g>
              </g>
              <g class="lf lf--3">
                <ellipse cx="512" cy="509" rx="17" ry="3" fill="#3a271a30"/>
                <g class="lf__swing"><path d="M503 66 L498 491 M521 70 L524 491" fill="none" stroke="#6b4a2e" stroke-width="1.3"/><rect x="494" y="489" width="34" height="5.5" rx="2" fill="#8d5c35" stroke="#5b3a22" stroke-width=".9"/></g>
                <g class="lf__kite"><path d="M760 142 L432 452" fill="none" stroke="#5b3a22" stroke-width=".8" opacity=".5"/><path d="M760 98 L774 120 L760 142 L746 120 Z" fill="#d6543d" stroke="#5b3a22" stroke-width=".9"/><path d="M760 120 L774 120 L760 142 Z" fill="#f0c04b"/><path d="M760 98 L760 142 M746 120 L774 120" fill="none" stroke="#5b3a22" stroke-width=".8"/><path d="M760 142 q9 9 -2 19 t5 21 t-4 18" fill="none" stroke="#d6543d" stroke-width="1.5" stroke-linecap="round"/><path d="M756 160 l5 -3 l1 6 Z M761 181 l5 -2 l0 6 Z" fill="#f0c04b"/></g>
              </g>
              <g class="lf lf--5" filter="url(#wc)" fill="none" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="468" cy="524" rx="30" ry="3" fill="#3a271a2b" stroke="none"/><g stroke="#6b4a2e" stroke-width="4.6"><path d="M450 500 L453 517 M453 513 L466 512 M454 513 L453 522 M465 512 L466 521 M451 507 L465 506"/><path d="M478 496 L481 513 M481 509 L494 508 M482 509 L481 518 M493 508 L494 517 M479 503 L493 502"/></g><g stroke="#fffaf0" stroke-width="3"><path d="M450 500 L453 517 M453 513 L466 512 M454 513 L453 522 M465 512 L466 521 M451 507 L465 506"/><path d="M478 496 L481 513 M481 509 L494 508 M482 509 L481 518 M493 508 L494 517 M479 503 L493 502"/></g></g>
              <g class="lf lf--4">
                <g class="lf__balloon"><path d="M883 150 C883 119 927 119 927 150 C927 164 913 178 910 184 L900 184 C897 178 883 164 883 150 Z" fill="#fff4e2" stroke="#5b3a22" stroke-width="1"/><path d="M896 128 C889 140 891 168 900 184 L905 184 C899 166 899 140 905 127 Z" fill="#e59aa6"/><path d="M905 127 C911 140 911 166 905 184 L910 184 C919 168 921 140 914 128 Z" fill="#8fb7b0"/><path d="M901 184 L902 191 M909 184 L908 191" fill="none" stroke="#5b3a22" stroke-width=".8"/><rect x="900" y="191" width="10" height="8" rx="1.5" fill="#9a6a3c" stroke="#5b3a22" stroke-width=".8"/></g>
              </g>
            </svg>'''

def snap(n, cap):
    return '<li class="snap"><span class="snap__win cornered"><img loading="lazy" decoding="async" src="kit/wc2/snap-%d.webp" alt="" width="480" height="300"></span><span class="snap__cap">%s</span></li>' % (n, cap)

LIFE_HTML = '''  <!-- 4 to 8. One picture, lived in. The cottage scene from "Into focus" stays on screen and her four areas happen
       inside it, across one day's light. Each ends with the shutter, and the frame drops out as a print. On the
       still page each area is that print with her words beside it. -->
  <section class="beat life" id="help" data-beat="life" style="--len: 12.5" data-chapter="Behind every photograph">
    <i class="mark" data-chapter="Protecting what matters" style="--at: .085"></i>
    <i class="mark" data-chapter="Growing your wealth" style="--at: .31"></i>
    <i class="mark" data-chapter="Life’s milestones" style="--at: .53"></i>
    <i class="mark" data-chapter="Planning for later life" style="--at: .8"></i>
    <div class="stage">
      <span class="sky" aria-hidden="true"></span>
      <div class="stage__in">
        <div class="life__words">
          <header class="chap chap--intro">
            <p class="kick">behind every photograph</p>
            <h2 class="title">What I can help you with</h2>
            <p class="note behind__sub">Planning for what matters at every stage.</p>
          </header>
          <article class="chap" id="protect" data-chapter="Protecting what matters">
            <p class="kick">whatever the weather</p>
            <h3 class="title topic__title">Protecting what matters</h3>
            <p class="desc">Understanding your insurance, critical illness and income protection needs, including whether your existing coverage still fits your circumstances.</p>
            <button class="pour" type="button">tap to make it pour ☂</button>
          </article>
          <article class="chap" id="grow" data-chapter="Growing your wealth">
            <p class="kick">planted early, tended patiently</p>
            <h3 class="title topic__title">Growing your wealth</h3>
            <p class="desc">Making sense of investing and long-term wealth accumulation without unnecessary complexity.</p>
          </article>
          <article class="chap" id="milestones" data-chapter="Life’s milestones">
            <p class="kick">the days you’ll frame</p>
            <h3 class="title topic__title">Planning around life’s milestones</h3>
            <p class="desc">Preparing financially for marriage, a home, children and other major changes in responsibility.</p>
          </article>
          <article class="chap" id="later" data-chapter="Planning for later life">
            <p class="kick">one day, you’ll look back on all of it</p>
            <h3 class="title topic__title">Planning for later life</h3>
            <p class="desc">Building towards financial independence, retirement and the future you want.</p>
          </article>
        </div>
        <ol class="roll" aria-hidden="true">
          ''' + '\n          '.join([snap(1, 'rain or shine'), snap(2, 'planted early'), snap(3, 'moving-in day'), snap(4, 'golden hour')]) + '''
        </ol>
        <div class="world cornered" aria-hidden="true">
          <div class="world__view">
            <div class="world__cam">
              <img loading="lazy" decoding="async" class="world__base" src="kit/wc2/clarity.webp" srcset="kit/wc2/clarity-760.webp 760w, kit/wc2/clarity.webp 1200w" sizes="(max-width: 900px) 92vw, 820px" alt="" width="1200" height="750">
              <canvas class="world__plant" width="340" height="340"></canvas>
            ''' + LIFE_SVG + '''
              <span class="world__dusk"></span>
              <span class="world__storm"></span>
              <span class="world__clouds"></span>
              <span class="world__sun"></span>
              <i class="world__lit" style="--x: 18.8%; --y: 48.3%"></i>
              <i class="world__lit" style="--x: 22.4%; --y: 48.6%"></i>
              <i class="world__lit" style="--x: 22.3%; --y: 60%"></i>
              <img loading="lazy" decoding="async" class="world__umb" src="kit/wc2/umbrella-air.webp" alt="" width="509" height="462">
            </div>
            <canvas class="world__rain"></canvas>
            <span class="world__tag"></span>
            <span class="world__flash"></span>
          </div>
        </div>
      </div>
      <p class="cue note" aria-hidden="true">keep scrolling ↓</p>
    </div>
  </section>

'''
a, _ = cut(s, '  <!-- Behind every photograph: four prints.', '  <section class="beat behind"')
_, b = cut(s, '  <section class="beat topic later"', '  <!-- 8. Making sense of financial planning')
s = s[:a] + LIFE_HTML + s[b:]

old = '            <ul class="mypage__list"></ul>\n'
assert old in s
kept = ''.join('<li class="stamp"><div class="stamp__win cornered"><img class="is-photo" loading="lazy" decoding="async" src="kit/wc2/snap-%d.webp" alt="" width="480" height="300"></div><p>%s</p></li>' % (i + 1, c) for i, c in enumerate(['rain or shine', 'planted early', 'moving-in day', 'golden hour']))
s = s.replace(old, '            <ul class="mypage__kept" aria-hidden="true">' + kept + '</ul>\n' + old)
old = '.mypage__list:empty { display: none; }\n'
assert old in s
s = s.replace(old, old + '/* The four prints taken on the way down the page are already mounted here; the visitor\'s own are pasted in after them. */\n.mypage__kept { display: flex; flex-wrap: wrap; gap: 14px 16px; list-style: none; margin: 12px 0 0; padding: 0; }\n.mypage__kept .stamp { animation: none; }\n.mypage__kept .stamp__win { aspect-ratio: 16 / 10; }\n')

# ------------------------------------------------------------------ styles
CLOUDS = "url(\\\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='640' height='320'%3E%3Cfilter id='c' x='0' y='0' width='100%25' height='100%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.011 .028' numOctaves='4' seed='11' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .13 0 0 0 0 .17 0 0 0 0 .27 0 0 0 2.6 -.95'/%3E%3C/filter%3E%3Crect width='640' height='320' filter='url(%23c)'/%3E%3C/svg%3E\\\")".replace('\\"', '"')

LIFE_CSS = '''/* 4 to 8. One picture, lived in ---------------------------------------------------------------------------
   Still page (no script, or reduced motion): her heading, then each area as a print with her words beside it.
   The live scene (.world) is not shown and none of its pictures are fetched. */
.life .stage__in { display: grid; grid-template-columns: minmax(0, 250px) minmax(0, 1fr); gap: clamp(26px, 5vh, 46px) clamp(20px, 4vw, 44px); align-items: center; max-width: 880px; }
.life__words, .roll { display: contents; }
.roll { list-style: none; }
.chap--intro { grid-column: 1 / -1; grid-row: 1; text-align: center; }
.behind__sub { font-size: 1.4rem; margin-top: 10px; }
.life .chap:not(.chap--intro) { grid-column: 2; }
.life .chap:nth-child(2), .snap:nth-child(1) { grid-row: 2; }
.life .chap:nth-child(3), .snap:nth-child(2) { grid-row: 3; }
.life .chap:nth-child(4), .snap:nth-child(3) { grid-row: 4; }
.life .chap:nth-child(5), .snap:nth-child(4) { grid-row: 5; }
.life .topic__title { margin-bottom: 14px; font-size: clamp(2rem, 1.25rem + 2.1vw, 3.3rem); }
.snap { grid-column: 1; display: block; padding: 8px 8px 0; background: var(--card); box-shadow: var(--shadow-card); }
.snap:nth-child(odd) { --r: -1.6deg; rotate: -1.6deg; }
.snap:nth-child(even) { --r: 1.4deg; rotate: 1.4deg; }
.snap__win { --cs: 14px; display: block; aspect-ratio: 16 / 10; background: #eedcc0; }
.snap__win img { display: block; width: 100%; height: 100%; object-fit: cover; }
.snap__cap { display: block; padding: 7px 2px 9px; font: 400 1rem/1.15 var(--f-hand); color: var(--ink-soft); text-align: center; }
.world, .mark, .pour { display: none; }

/* Motion: the words sit in one place and change with the chapter; the picture is held beside them; the prints
   taken so far collect in a row underneath. Everything below is driven by numbers the scroll writes on the
   section: --storm --open --gold --lit --planted --a1 to --a4 (the four arrivals) --flash, and --s/--e per print. */
.motion .life { --storm: 0; --open: 0; --gold: 0; --lit: 0; --planted: 0; --a1: 0; --a2: 0; --a3: 0; --a4: 0; --a5: 0; --flash: 0; --in: 0; --drift: 0; }
.motion .life .sky { position: absolute; inset: 0; z-index: 0; background: linear-gradient(180deg, #f6d6a400 0%, #f6d6a4 16%, #f2c690 52%, #f4ead600 100%); opacity: calc(var(--gold) * .9); }
.motion .mark { display: block; position: absolute; left: 0; width: 1px; height: 1px; pointer-events: none; top: calc((var(--at) * (var(--len) - 1) + .45) * 100vh); top: calc((var(--at) * (var(--len) - 1) + .45) * 100svh); }
.motion .life .stage__in { max-width: 1240px; grid-template-columns: minmax(0, .44fr) minmax(0, 1fr); grid-template-rows: minmax(0, 1fr) auto; gap: 18px clamp(24px, 3.4vw, 54px); align-items: stretch; }
.motion .life__words { display: grid; grid-column: 1; grid-row: 1; align-content: center; min-height: 0; }
.motion .life .chap { grid-area: 1 / 1; align-self: center; text-align: left; opacity: 0; transform: translateY(16px); transition: opacity .4s ease, transform .5s var(--ease); pointer-events: none; }
.motion .life .chap.is-on { opacity: 1; transform: none; pointer-events: auto; transition-delay: .12s; }
.motion .chap--intro .title { font-size: clamp(2.3rem, 1.4rem + 2.6vw, 3.9rem); }
.motion .pour { display: inline-flex; align-items: center; gap: 8px; margin-top: 22px; padding: 10px 18px; border-radius: 999px; border: 1.5px dashed var(--ink-soft); background: #fffaf0b3; color: var(--ink); font: 400 1.1rem/1 var(--f-hand); cursor: pointer; }
.motion .pour:hover { background: var(--card); }
.motion .life .chap:not(.is-on) .pour { visibility: hidden; }
.motion .roll { display: grid; grid-column: 1; grid-row: 2; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; align-self: end; margin: 0; padding: 0 0 4px; }
.motion .snap { grid-column: auto; grid-row: auto; padding: 5px 5px 0; rotate: none; transform-origin: 0 0; opacity: clamp(0, calc(var(--s, 0) * 9), 1); transform: translate(calc((1 - var(--e, 0)) * var(--dx, 0px)), calc((1 - var(--e, 0)) * var(--dy, 0px))) scale(calc(1 + (1 - var(--e, 0)) * (var(--k, 1) - 1))) rotate(calc(var(--e, 0) * var(--r))); z-index: 6; position: relative; will-change: transform; }
.motion .snap__win { --cs: 9px; }
/* While a print is in the air it is the picture itself: its caption and corners arrive once it has landed. */
.motion .snap__cap, .motion .snap__win.cornered::before { opacity: clamp(0, calc((var(--e, 0) - .9) * 12), 1); }
.motion .snap { background: rgb(255 250 240 / clamp(0, calc((var(--e, 0) - .5) * 3), 1)); box-shadow: 0 14px 30px -14px rgb(40 25 10 / calc(clamp(0, (var(--e, 0) - .5) * 3, 1) * .45)); }
.motion .snap__win { box-shadow: 0 calc((1 - var(--e, 0)) * 30px) calc((1 - var(--e, 0)) * 50px) -18px rgb(40 25 10 / calc((1 - var(--e, 0)) * .6)); }
.motion .snap__cap { padding: 5px 0 6px; font-size: clamp(.68rem, .4rem + .5vw, .86rem); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.motion .world { display: block; grid-column: 2; grid-row: 1 / span 2; align-self: center; justify-self: center; --cs: 30px; position: relative; width: min(100%, calc((100vh - var(--hud) - 120px) * 1.6)); width: min(100%, calc((100svh - var(--hud) - 120px) * 1.6)); aspect-ratio: 16 / 10; border: 10px solid var(--card); border-radius: 4px; background: #f2e8d4; box-shadow: var(--shadow-card); scale: calc(.86 + var(--in) * .14); opacity: calc(.35 + var(--in) * .65); cursor: pointer; }
.world__view { position: absolute; inset: 0; overflow: hidden; }
.world__cam { position: absolute; inset: 0; transform-origin: 0 0; will-change: transform; }
.world__cam > * { position: absolute; }
.world__base { inset: 0; width: 100%; height: 100%; object-fit: cover; filter: saturate(calc(1 - var(--storm) * .45)) brightness(calc(1 - var(--storm) * .1)); }
/* The growth clip, cut out, standing in the foreground grass */
.world__plant { left: 60.5%; top: 97.5%; width: 22%; height: auto; aspect-ratio: 1; translate: -50% -96.5%; opacity: var(--planted); }
/* The four arrivals, drawn in the picture's own pixels */
.world__life { inset: 0; width: 100%; height: 100%; overflow: visible; }
.lf--1 { opacity: var(--a1); } .lf--2 { opacity: var(--a2); } .lf--3 { opacity: var(--a3); } .lf--4 { opacity: var(--a4); } .lf--5 { opacity: var(--a5); }
.lf--5 { transform-box: fill-box; transform-origin: 50% 100%; transform: translate(-24px, -3px) scale(1.4); }
.lf__arch { transform-box: fill-box; transform-origin: 50% 100%; transform: scale(1.18, calc((.4 + var(--a1) * .6) * 1.18)); }
.lf__kite { transform: translate(calc((1 - var(--a3)) * 90px), calc((1 - var(--a3)) * 40px)); }
.lf__balloon { transform-box: view-box; transform-origin: 905px 160px; transform: translateY(calc((1 - var(--a4)) * 70px)) scale(1.45); }
.lf__smoke { opacity: .62; }
.lf__swing { transform-box: view-box; transform-origin: 512px 66px; animation: sway 3.4s ease-in-out infinite alternate; }
.lf__kite > * { transform-box: view-box; transform-origin: 760px 120px; animation: bob 4.4s ease-in-out infinite alternate; }
.lf__balloon > * { animation: drift 11s ease-in-out infinite alternate; }
.lf__smoke circle { animation: puff 4.5s ease-out infinite; }
.lf__smoke circle:nth-child(2) { animation-delay: -1.5s; } .lf__smoke circle:nth-child(3) { animation-delay: -3s; }
@keyframes sway { from { transform: rotate(-2deg); } to { transform: rotate(2deg); } }
@keyframes bob { from { transform: translate(-4px, 3px) rotate(-5deg); } to { transform: translate(5px, -4px) rotate(4deg); } }
@keyframes drift { from { transform: translate(-8px, 4px); } to { transform: translate(12px, -6px); } }
@keyframes puff { from { transform: translate(0, 10px) scale(.6); opacity: 0; } 25% { opacity: 1; } to { transform: translate(14px, -26px) scale(1.5); opacity: 0; } }
/* Weather and light are laid over the one painting, so nothing can drift out of line and nothing extra is fetched. */
.world__storm { inset: 0; background: linear-gradient(180deg, #232d49 0%, #36435a 55%, #485260 100%); mix-blend-mode: multiply; opacity: calc(var(--storm) * .86);
  -webkit-mask-image: radial-gradient(ellipse 30% 34% at 21.5% 53%, #0000 0, #0000 calc(var(--open) * 52%), #000 calc(var(--open) * 100% + .4%));
  mask-image: radial-gradient(ellipse 30% 34% at 21.5% 53%, #0000 0, #0000 calc(var(--open) * 52%), #000 calc(var(--open) * 100% + .4%)); }
.world__clouds { left: -12%; right: -12%; top: 0; height: 64%; background: CLOUDS 0 0 / 55% 100% repeat-x; opacity: var(--storm); transform: translateX(calc(var(--drift) * -7%)); -webkit-mask-image: linear-gradient(#000 35%, #0000); mask-image: linear-gradient(#000 35%, #0000); }
.world__dusk { inset: 0; background: radial-gradient(95% 85% at 90% 40%, #ffd493 0%, #ffa466 38%, #b0627a 78%, #6d4a78 100%); mix-blend-mode: multiply; opacity: calc(var(--gold) * .78); }
.world__sun { left: 90%; top: 40.5%; width: 46%; aspect-ratio: 1; translate: -50% -50%; background: radial-gradient(closest-side, #fff6cf 0%, #ffd27e99 26%, #ff9d5c33 58%, #ff9d5c00 100%); mix-blend-mode: screen; opacity: calc(var(--gold) * .9); }
.world__lit { left: var(--x); top: var(--y); width: 5.4%; aspect-ratio: 1; translate: -50% -50%; border-radius: 50%; background: radial-gradient(closest-side, #ffe2a0 0%, #ffbf5cb3 38%, #ffb04d00 100%); mix-blend-mode: screen; opacity: var(--lit); }
/* The umbrella swings up from its handle and opens over the home; under it the storm is kept off. */
.world__umb { left: 3%; top: 12.5%; width: 37.5%; height: auto; transform-origin: 85% 96%; opacity: clamp(0, calc(var(--open) * 4), 1); transform: rotate(calc((1 - var(--open)) * 26deg)) scale(calc(.5 + .5 * var(--open))); }
.world__rain { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; }
.world__tag { position: absolute; left: 14px; bottom: 12px; padding: 5px 13px 4px; border-radius: 3px; background: var(--card); box-shadow: 0 2px 6px #28190a40; font: 400 1.1rem/1.2 var(--f-hand); color: var(--ink); rotate: -1.5deg; opacity: 0; translate: 0 8px; transition: opacity .3s ease, translate .4s var(--ease); }
.world__tag.is-on { opacity: 1; translate: none; }
.world__flash { position: absolute; inset: 0; background: #fffdf5; opacity: var(--flash); pointer-events: none; }

'''.replace('CLOUDS', CLOUDS)
a, _ = cut(s, '/* Behind every photograph: four prints, and each turns over', '.behind .stage__in')
_, b = cut(s, '/* 7. Later life: the paper warms to golden hour', '/* 8. Videos: a frame in the middle')
s = s[:a] + LIFE_CSS + s[b:]

# responsive: drop the old sections' overrides, add the scene's
for old in ['  .ms-text { grid-template-columns: 1fr; }\n', '  .flips { grid-template-columns: repeat(2, minmax(0, 1fr)); max-width: 640px; }\n', '  .later .stage__in { align-content: center; }\n',
            '  .motion .scene { width: min(100%, 40vh); width: min(100%, 40svh); }\n', '  .behind .title { font-size: 2.1rem; }\n', '  .behind__sub { font-size: 1.15rem; margin-top: 6px; }\n',
            '  .flips { gap: 12px; margin-top: 16px; }\n', '  .flip__front { padding: 8px 8px 0; }\n', '  .flip__win { aspect-ratio: 3 / 2; }\n', '  .flip__cap { padding: 6px 2px 8px; font-size: .96rem; }\n',
            '  .flip__back { gap: 5px; padding: 2px 10px 12px; }\n', '  .flip__name { font-size: 1.14rem; }\n', '  .flip__desc { font-size: .86rem; line-height: 1.32; }\n', '  .motion .flip__back { padding: 10px 11px 12px; }\n',
            '  .motion .flip__name { padding-bottom: 6px; }\n', '  .motion .behind__hint { margin-top: 10px; font-size: 1rem; }\n', '  .topic .stage__in { gap: 14px; }\n', '  .topic__title { margin-bottom: 8px; }\n',
            '  .motion .pour { margin-top: 14px; }\n', '  .ms-card { width: clamp(170px, 52vw, 230px); }\n', '  .motion .flip__desc { display: none; }\n', '  .motion .flip__back { text-align: center; }\n',
            '  .motion .flip__name { padding-bottom: 0; border-bottom: 0; font-size: 1.24rem; }\n', '  .motion .scene { width: min(100%, 34vh); width: min(100%, 34svh); }\n']:
    assert old in s, old
    s = s.replace(old, '')
s = s.replace('.pages .stage__in, .clarity .stage__in, .topic .stage__in, .together .stage__in { grid-template-columns: 1fr; align-content: start; }',
              '.pages .stage__in, .clarity .stage__in, .together .stage__in { grid-template-columns: 1fr; align-content: start; }')
old = '  .talk__art { width: min(420px, 92%); order: 2; }\n}\n@media (max-width: 760px) {'
assert old in s
s = s.replace(old, '''  .talk__art { width: min(420px, 92%); order: 2; }
  /* The living picture: the painting on top, her words under it, the prints along the bottom */
  .motion .life .stage__in { grid-template-columns: minmax(0, 1fr); grid-template-rows: auto minmax(0, 1fr) auto; gap: 14px; }
  .motion .world { grid-column: 1; grid-row: 1; width: min(100%, 640px, calc((100vh - var(--hud) - 350px) * 1.6)); width: min(100%, 640px, calc((100svh - var(--hud) - 350px) * 1.6)); }
  .motion .life__words { grid-row: 2; align-content: start; }
  .motion .life .chap { align-self: start; }
  .motion .roll { grid-row: 3; max-width: 520px; }
}
@media (max-width: 760px) {''')
old = '  .together .stage__in { grid-template-rows: auto minmax(0, 1fr); gap: 20px; }\n'
assert old in s
s = s.replace(old, '''  .life .stage__in { grid-template-columns: minmax(0, 118px) minmax(0, 1fr); gap: 26px 16px; }
  .life .topic__title { margin-bottom: 8px; font-size: 1.75rem; }
  .life .desc { font-size: .95rem; line-height: 1.45; }
  .behind__sub { font-size: 1.15rem; margin-top: 6px; }
  .snap__cap { font-size: .82rem; }
  .motion .chap--intro .title { font-size: 2.1rem; }
  .motion .world { --cs: 18px; border-width: 6px; }
  .motion .pour { margin-top: 10px; padding: 8px 14px; font-size: 1rem; }
  .motion .roll { gap: 8px; margin-right: 72px; }
  .motion .life .stage { padding-bottom: 84px; }
  .motion .snap { padding: 4px 4px 0; }
  .world__tag { left: 8px; bottom: 8px; font-size: .95rem; }
''' + old)

# ------------------------------------------------------------------ script
a, _ = cut(s, '  /* Behind every photograph: the scroll turns the four prints over', '  (function () {\n    var b = $(\'#help\')')
_, b = cut(s, '  /* 7. Later life ---', '  /* 9. Working together')
LIFE_JS = r'''  /* 4 to 8. One picture, lived in. The scroll is one number, p, from 0 to 1 across the whole scene; everything
     here reads its own stretch of it. Rain is the only part that runs on the clock. ------------------------- */
  (function () {
    var b = $('#help'), world = $('.world', b), view = $('.world__view', b), cam = $('.world__cam', b);
    var chaps = $$('.chap', b), snaps = $$('.snap', b), tag = $('.world__tag', b), umb = $('.world__umb', b);
    var START = [0, .085, .31, .53, .8, 1.2];              // where each chapter's words come on
    var SHOT = [.276, .496, .776, .962];                  // the shutter, once per area
    var TAGS = [[.545, 'marriage'], [.61, 'a home'], [.675, 'children'], [.735, 'other major changes'], [.772, '']];
    // The camera inside the picture: [p, zoom, where it looks across, where it looks down]
    var CAM = [[0, 1, .5, .5], [.09, 1, .5, .5], [.15, 1.3, .25, .5], [.262, 1.3, .25, .5], [.3, 1, .5, .5], [.325, 1, .5, .5], [.37, 1.26, .6, .8], [.482, 1.26, .6, .8],
      [.52, 1, .5, .5], [.54, 1, .5, .5], [.565, 1.34, .58, .62], [.6, 1.34, .58, .62], [.63, 1.34, .27, .56], [.665, 1.34, .27, .56], [.695, 1.1, .5, .4], [.725, 1.1, .52, .38],
      [.748, 1.12, .7, .3], [.762, 1, .5, .5], [.8, 1, .5, .5], [.845, 1.28, .36, .6], [.895, 1.28, .36, .6], [.945, 1, .5, .5], [1, 1.07, .62, .46]];
    function ease(t) { return t * t * (3 - 2 * t); }
    function set(name, v) { b.style.setProperty(name, v.toFixed(3)); }

    // --- the growth clip, cut out: one frame per step of scroll
    var plant = $('.world__plant', b), pctx = plant.getContext('2d'), N = 28, frames = [], want = 0, shown = -1, started = false;
    function drawPlant() {
      var i = -1;
      for (var d = 0; d < N && i < 0; d++) {
        if (frames[want - d] && frames[want - d].ok) i = want - d;
        else if (frames[want + d] && frames[want + d].ok) i = want + d;
      }
      if (i < 0 || i === shown) return;
      shown = i;
      pctx.clearRect(0, 0, plant.width, plant.height);
      pctx.drawImage(frames[i], 0, 0, plant.width, plant.height);
    }
    function loadFrame(i) {
      if (frames[i]) return;
      var im = frames[i] = new Image();
      im.onload = function () { im.ok = true; drawPlant(); };
      im.src = 'kit/wc2/grow-a/g' + (i < 10 ? '0' : '') + i + '.webp';
    }
    function startPlant() {
      if (started) return;
      started = true;
      var i;
      loadFrame(want);
      for (i = 0; i < N; i += 4) loadFrame(i);
      for (i = 0; i < N; i++) loadFrame(i);
    }

    // --- rain, in the picture's frame; it stops on the open umbrella
    var canvas = $('.world__rain', b), ctx = canvas.getContext('2d');
    var drops = [], wet = 0, storm = 0, open = 0, pourUntil = 0, running = false, last = 0;
    var dpr = Math.min(1.5, window.devicePixelRatio || 1);
    var CANOPY = [[.03, .6], [.06, .485], [.1, .396], [.18, .277], [.26, .201], [.34, .13], [.42, .08], [.5, .045], [.58, .019], [.66, .015], [.74, .024], [.82, .048], [.9, .08], [.95, .115], [.975, .15]];
    function canopyTop(fx) {
      if (fx < CANOPY[0][0] || fx > CANOPY[CANOPY.length - 1][0]) return -1;
      for (var k = 1; k < CANOPY.length; k++) {
        if (fx <= CANOPY[k][0]) return lerp(CANOPY[k - 1][1], CANOPY[k][1], (fx - CANOPY[k - 1][0]) / (CANOPY[k][0] - CANOPY[k - 1][0]));
      }
      return -1;
    }
    function spawn(d, anywhere) {
      d = d || {};
      d.x = Math.random() * canvas.width * 1.15 - canvas.width * .1;
      d.y = anywhere ? Math.random() * canvas.height : -Math.random() * 40 * dpr;
      d.v = (700 + Math.random() * 500) * dpr; d.l = (10 + Math.random() * 13) * dpr;
      return d;
    }
    function loop(t) {
      if (!running) return;
      var dt = Math.min(.05, (t - last) / 1000 || .016); last = t;
      var pour = t < pourUntil;
      var aim = clamp(storm * (pour ? 2.2 : 1) + (pour ? .6 : 0), 0, 2.2);
      wet += (aim - wet) * Math.min(1, dt * 3);
      var vr = view.getBoundingClientRect(), ur = umb.getBoundingClientRect();
      var ux = (ur.left - vr.left) * dpr, uw = ur.width * dpr, uy = (ur.top - vr.top) * dpr, uh = ur.height * dpr;
      var count = Math.round(170 * wet * Math.min(1, canvas.width / (700 * dpr) + .35));
      while (drops.length < count) drops.push(spawn(null, true));
      if (drops.length > count) drops.length = count;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      if (count) {
        ctx.strokeStyle = 'rgba(226, 236, 248, .62)'; ctx.lineWidth = 1.2 * dpr; ctx.lineCap = 'round';
        ctx.beginPath();
        for (var i = 0; i < drops.length; i++) {
          var d = drops[i];
          d.y += d.v * dt; d.x += d.v * .12 * dt;
          var stop = canvas.height + 20, top = open > .85 ? canopyTop((d.x - ux) / uw) : -1;
          if (top >= 0) stop = uy + top * uh;
          if (d.y > stop) { spawn(d); continue; }
          ctx.moveTo(d.x, d.y); ctx.lineTo(d.x - d.l * .12, d.y - d.l);
        }
        ctx.stroke();
      }
      requestAnimationFrame(loop);
    }
    function pour() { if (storm > .3) pourUntil = performance.now() + 2800; }

    // --- layout: the rain's canvas, and how far each print has to travel from the picture to its place in the row
    function layout() {
      canvas.width = Math.round(view.clientWidth * dpr); canvas.height = Math.round(view.clientHeight * dpr);
      var wr = world.getBoundingClientRect(), sc = wr.width / (world.offsetWidth || 1);   // undo the picture's own entrance scale
      var cx = wr.left + wr.width / 2, cy = wr.top + wr.height / 2, w = view.clientWidth, h = view.clientHeight;
      snaps.forEach(function (sn) {
        var keep = sn.style.transform; sn.style.transform = 'none';
        var win = $('.snap__win', sn), r = win.getBoundingClientRect(), lr = sn.getBoundingClientRect();
        sn.style.transform = keep;
        var k = w / r.width;
        sn.style.setProperty('--k', k.toFixed(4));
        sn.style.setProperty('--dx', (cx - w / 2 - lr.left - (r.left - lr.left) * k).toFixed(1) + 'px');
        sn.style.setProperty('--dy', (cy - h / 2 - lr.top - (r.top - lr.top) * k).toFixed(1) + 'px');
      });
      if (sc && b._p !== undefined) run(b._p);
    }

    function run(p) {
      var i, k;
      // words: one chapter at a time
      for (k = 0; k < chaps.length; k++) chaps[k].classList.toggle('is-on', p >= START[k] - (k ? 0 : 1) && p < START[k + 1] - .014);
      set('--in', ease(ramp(p, -.001, .05)));
      // 1 weather: the storm comes over, the umbrella opens, the storm passes
      storm = ease(ramp(p, .1, .15)) * (1 - ease(ramp(p, .278, .306)));
      open = ease(ramp(p, .168, .215)) * (1 - ease(ramp(p, .286, .31)));
      set('--storm', storm); set('--open', open); set('--drift', ramp(p, .09, .31));
      // 2 growth: a sapling is planted, then grows
      set('--planted', ramp(p, .328, .35));
      want = Math.round(ramp(p, .352, .486) * (N - 1));
      if (started) drawPlant();
      // 3 milestones: four arrivals, one for each of her words
      var a2 = ease(ramp(p, .618, .652));
      set('--a1', ease(ramp(p, .553, .588))); set('--a2', a2); set('--a3', ease(ramp(p, .682, .716))); set('--a4', ease(ramp(p, .737, .764)));
      var label = '';
      for (i = 0; i < TAGS.length; i++) if (p >= TAGS[i][0]) label = TAGS[i][1];
      if (label) tag.textContent = label;
      tag.classList.toggle('is-on', !!label);
      // 4 later life: the light turns gold
      var gold = ease(ramp(p, .81, .95));
      set('--a5', ease(ramp(p, .825, .86)));
      set('--gold', gold);
      set('--lit', Math.max(storm * .95, gold, a2 * .45));
      // the shutter, and the print it leaves
      var flash = 0;
      for (i = 0; i < SHOT.length; i++) {
        flash = Math.max(flash, 1 - Math.abs(p - SHOT[i]) / .007);
        var t = ramp(p, SHOT[i], SHOT[i] + .024);
        snaps[i].style.setProperty('--s', t.toFixed(3));
        snaps[i].style.setProperty('--e', (1 - Math.pow(1 - t, 3)).toFixed(4));
      }
      set('--flash', clamp(flash, 0, 1) * .85);
      // the camera
      for (i = 1; i < CAM.length - 1 && p > CAM[i][0]; i++);
      var A = CAM[i - 1], B = CAM[i], u = ease(ramp(p, A[0], B[0]));
      var z = lerp(A[1], B[1], u), fx = lerp(A[2], B[2], u), fy = lerp(A[3], B[3], u), w = view.clientWidth, h = view.clientHeight;
      var tx = clamp(w / 2 - fx * w * z, w - w * z, 0), ty = clamp(h / 2 - fy * h * z, h - h * z, 0);
      cam.style.transform = 'translate(' + tx.toFixed(1) + 'px,' + ty.toFixed(1) + 'px) scale(' + z.toFixed(4) + ')';
    }

    if (motion) {
      $('.pour', b).addEventListener('click', pour);
      world.addEventListener('pointerdown', pour);
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting && !running) { running = true; last = performance.now(); requestAnimationFrame(loop); }
          else if (!e.isIntersecting) { running = false; }
        });
      }).observe(b);
      new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) startPlant(); }); }, { rootMargin: '100% 0px' }).observe(b);
    }
    handlers.life = run;
    handlers.life.layout = layout;
  })();

'''
s = s[:a] + LIFE_JS + s[b:]

# the header's chapter names: markers down the tall section when it moves, the articles themselves when it does not
old = "  var beats = $$('[data-beat]');\n"
assert old in s
s = s.replace(old, '''  // The living picture is one tall section. With motion it carries a marker per chapter for the header to read;
  // without, the four articles are ordinary blocks down the page and name themselves.
  $$('.life .mark').forEach(function (m) { if (!motion) m.parentNode.removeChild(m); });
  // (the ids of the four articles are moved to the markers too: see 07-living.html)
  if (motion) $$('.life .chap[data-chapter]').forEach(function (c) { c.removeAttribute('data-chapter'); });
''' + old)

open(DST, 'w', encoding='utf-8').write(s)
print('written', len(s))
