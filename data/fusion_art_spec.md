# FUSION ART LIBRARY — style contract

**Every drawing in this library must obey this file.** It exists so the assets
look like one channel instead of fifty different ones.

Read `data/fusion_art.py` first. The six drawings already in it (`laptop`,
`gpu`, `collapse`, `clock`, `meter`, `caveat`) are the **gold standard**. Match
their code style, their level of detail and their discipline exactly.

---

## 1. The look

Flat line art on near-black. **No photography. No gradients on strokes. No
shadows. No 3D perspective.** One accent colour per drawing, plus ink and dim.

This is the visual grammar of KAI (`@kaiexplainsYT`) and RepoChad
(`@repochad`) — the two channels this is modelled on. Both draw hardware as
clean 2D line work, never as a rendered product shot.

| Token | Value | Use |
|---|---|---|
| `INK` | `#F6F6F4` | the main outline colour, near-white but never `#FFFFFF` |
| `GOLD` | `#F5C531` | the ONE accent per drawing. The thing the eye must land on. |
| `CYAN` | `#38D9E8` | second accent, only if the drawing genuinely needs two |
| `RED` | `#E12A27` | only for "wrong", "cost", "hot", "danger" |
| `GREY` | `rgba(246,246,244,.52)` | secondary text, inactive parts |
| `FAINT` | `rgba(246,246,244,.30)` | tertiary text, axis labels |
| `HAIR` | `rgba(246,246,244,.18)` | inner rules, panel borders, dividers |

Pick **one** accent (usually `GOLD`) and use it sparingly — a gold detail, a
gold fill on one element, a gold label. The rest is ink and dim. A drawing with
gold, cyan and red all over looks like nothing.

---

## 2. Hard rules

These are the rules that were broken and fixed during Episode 07. Do not break
them again.

1. **A `<g>` NEVER carries a `transform` attribute.** If you animate
   `style.transform` on an element that *has* a transform attribute, the
   element collapses to the top-left. Motion belongs on HTML wrappers, or on
   `<g>` elements with no transform attribute.
2. **Nothing overlaps anything it should not.** Labels never touch a line, a
   curve or another label. If a shape covers part of another, the covered part
   is either omitted from the path or the front shape is opaque over it.
3. **The viewBox is TIGHT around the content.** Compute the real bounds of
   what you draw and use `viewBox="min-x min-y width height"` with about a 12
   unit margin. A loose viewBox makes the drawing shrink inside its panel.
   *The viewBox string is used verbatim — never prefix it with `0 0`.*
4. **The drawing is centred in its viewBox.** Left margin ≈ right margin.
5. **Every drawing must read at thumbnail size.** If a detail only works at
   100%, cut it.

---

## 3. Geometry rules

- Main outline: `stroke-width="3"`, `stroke-linecap="round"`,
  `stroke-linejoin="round"`.
- Secondary / inner detail: `stroke-width="1.5"`.
- A filled shape that must read as solid: `fill="<colour>"` with
  `stroke="none"`.
- A "hole" cut out of a filled shape: use the background colour
  `fill="#0D1110"` — never `fill="none"`.
- Corners: `rx="8"` to `rx="14"` for panels, `rx="2"` to `rx="4"` for small
  parts, `rx="5"` to `rx="8"` for buttons.
- Text: `font-family="FuseMono, monospace"`, `font-weight="700"` or `800`,
  `letter-spacing="2"` to `4"`, `fill` = `INK` / `GREY` / `FAINT` / the accent.
  Text sizes: `13` tertiary, `15`–`17` labels, `26`–`58` for a big number.
- Big numbers: `font-weight="800"`, `letter-spacing="1"`.

---

## 4. Motion hooks

Anything that moves gets a `<g>` wrapper:

```python
b.append('<g data-amb="spin" data-amb-speed="0.26" data-amb-k="0">'
         '...blades or hands...'
         '</g>')
b.append('<g data-amb="pulse" data-amb-k="1" data-amb-speed="1.4">'
         '...a marker that breathes...'
         '</g>')
b.append('<g data-amb="blink">'
         '...a cursor...'
         '</g>')
```

- `spin` — rotate. `data-amb-speed` is a factor on 132 deg/s: `0.1` is slow and
  heavy, `0.3` is a fast fan, `0.5` is frantic. `data-amb-k` offsets the
  starting angle so two fans are not in lockstep.
  **If the part pivots somewhere other than its own bounding-box centre**, add
  `data-amb-box="view-box"` and `data-amb-origin="<x>px <y>px"` in the
  drawing's own viewBox units.
- `pulse` — opacity 0.60→1.00. `data-amb-k` sets the phase, so a row of
  markers breathes in sequence.
- `blink` — a cursor waiting.

Use ambient motion only where the object would really move: fans, hands,
indicators, cursors, live meters. A screw does not spin.

**Reading order matters.** The sketch-on animation staggers shapes by their
position in the drawing, so a marker must not appear before the line that
leads to it. If a marker sits on a line, give it an explicit delay:

```python
'<circle cx="120" cy="80" r="9" fill="%s" data-draw-delay="0.42"/>' % RED
```

`data-draw-delay` is in **seconds** from the start of the sketch.

---

## 5. Code template

```python
def my_drawing():
    """One line saying what it is."""
    b = []
    # --- the main body
    b.append('<rect x="40" y="30" width="240" height="120" rx="10" fill="none" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- inner detail
    b.append('<rect x="56" y="46" width="208" height="88" rx="6" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    # --- the one gold thing
    b.append('<circle cx="160" cy="90" r="16" fill="%s"/>' % GOLD)
    # --- a label
    b.append('<text x="160" y="180" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="700" fill="%s" letter-spacing="3">LABEL</text>' % GREY)
    return _svg("30 20 260 172", "".join(b), "my_drawing")
```

`_svg(view, body, slug)` takes the **full viewBox string** and wraps the body.

---

## 6. Checklist before you return

- [ ] One accent colour, used sparingly
- [ ] No `transform` attribute on any `<g>`
- [ ] No overlapping labels or lines
- [ ] viewBox is tight and centred
- [ ] Reads at 200px wide
- [ ] Stroke widths: 3 main, 1.5 detail
- [ ] Rounded line caps and joins
- [ ] Text uses `FuseMono, monospace` with letter-spacing
- [ ] Ambient hooks only on parts that would really move
- [ ] The function returns `_svg(...)` and nothing else

---

## 7. Output format

**Write ONE file per batch.** Do not edit `fusion_art.py` — the coordinator
merges them. Each file must contain:

```python
# -*- coding: utf-8 -*-
"""FUSION ART BATCH — <name>. Generated for the Byte Forensics asset library."""
import math

INK = "#F6F6F6"
...
```

with the palette constants, a `_svg` helper, and the batch's functions. The
coordinator imports the functions from your file and adds them to the registry.

**Verify your own work before returning.** Render every drawing you wrote to a
PNG at a large size, LOOK at the PNG, and fix what you see. Use this helper:

```python
import sys, os
sys.path.insert(0, r"C:\Users\jibra\Desktop\1\KAI\data")
from playwright.sync_api import sync_playwright
from fusion_art_batch_x import my_func

cells = "".join('<div class="c"><div class="lab">%s</div>%s</div>' % (n, f())
                for n, f in [("my_drawing", my_func)])
html = ('<!doctype html><meta charset="utf-8"><style>'
        '@font-face{font-family:"FuseMono";src:url("file:///C:/Users/jibra/Desktop/1/KAI/core/fonts/JetBrainsMono-Bold.ttf");font-weight:700}'
        'html,body{margin:0;background:#0D1110;font-family:FuseMono,monospace}'
        '.wrap{display:flex;flex-wrap:wrap}'
        '.c{width:900px;height:620px;position:relative;display:flex;align-items:center;'
        'justify-content:center;border:1px solid #1b2321;box-sizing:border-box}'
        '.c svg{width:860px;height:580px;overflow:visible}'
        '.lab{position:absolute;left:10px;top:8px;color:#F5C531;font-size:13px;'
        'letter-spacing:.2em;text-transform:uppercase;z-index:9}'
        '</style><div class="wrap">' + cells + '</div>')
open(r"C:\Users\jibra\Desktop\1\KAI\proof\_batch.html", "w", encoding="utf-8").write(html)
with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page(viewport={"width": 1800, "height": 620 * ((len(cells)//900) + 1)})
    pg.goto("file:///C:/Users/jibra/Desktop/1/KAI/proof/_batch.html", wait_until="load")
    pg.wait_for_timeout(800)
    pg.screenshot(path=r"C:\Users\jibra\Desktop\1\KAI\proof\_batch.png", full_page=True)
    br.close()
print("rendered")
```

Then **read the PNG back** with the read tool and look at it. Iterate until
every drawing is right. A drawing you did not look at is not finished.
