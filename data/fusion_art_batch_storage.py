# -*- coding: utf-8 -*-
"""FUSION ART BATCH — storage. Generated for the Byte Forensics asset library.

Five drawings about where the bytes actually live: an NVMe stick, a spinning
hard disk, a model file on disk, a GGUF packed in mixed bit precision, and a
folder a download lands in.

Same rules as data/fusion_art.py:
  * a <g> NEVER carries a transform attribute.
  * one accent colour per drawing (GOLD), used sparingly.
  * viewBox is tight around the content with a 12 unit margin, and the
    drawing is centred inside it.
  * every function returns _svg(...) and nothing else.
"""
import math

INK = "#F6F6F4"
GOLD = "#F5C531"
CYAN = "#38D9E8"
RED = "#E12A27"
GREY = "rgba(246,246,244,.52)"
FAINT = "rgba(246,246,244,.30)"
HAIR = "rgba(246,246,244,.18)"


def _svg(view, body, slug):
    """view is a FULL viewBox: "min-x min-y width height"."""
    return (
        '<svg viewBox="%s" class="art" data-art="%s" '
        'xmlns="http://www.w3.org/2000/svg">%s</svg>' % (view, slug, body)
    )


# ==================================================================== scene 1
def nvme_ssd():
    """An M.2 NVMe stick: long narrow PCB, controller chip at one end, NAND
    mid-board, gold edge connector at the far end."""
    b = []
    # --- the PCB
    b.append('<rect x="40" y="88" width="390" height="118" rx="8" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the mounting hole at the free end
    b.append('<circle cx="58" cy="147" r="7" fill="#0D1110" stroke="%s" stroke-width="1.5"/>' % INK)
    # --- the controller chip: one square, near the free end
    b.append('<rect x="82" y="112" width="80" height="80" rx="4" fill="rgba(246,246,244,.03)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="94" y="124" width="56" height="56" rx="3" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    # --- the NAND package: mid-board, and wider than the controller
    b.append('<rect x="186" y="112" width="112" height="80" rx="4" fill="rgba(246,246,244,.03)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    for i in range(3):
        b.append('<rect x="200" y="%d" width="84" height="6" rx="3" fill="%s" opacity=".30"/>'
                 % (126 + i * 14, INK))
    # --- two passives, so the board is not a blank slab
    b.append('<rect x="316" y="136" width="14" height="12" rx="2" fill="%s" opacity=".28"/>' % INK)
    b.append('<rect x="338" y="136" width="14" height="12" rx="2" fill="%s" opacity=".28"/>' % INK)
    # --- the gold edge connector at the far end, with one key notch
    b.append('<rect x="430" y="104" width="44" height="86" rx="3" fill="%s" opacity=".92"/>' % GOLD)
    b.append('<rect x="446" y="164" width="12" height="26" fill="#0D1110"/>')
    # --- captions, all in clear air
    b.append('<text x="40" y="58" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="800" fill="%s" letter-spacing="3">NVMe SSD</text>' % GREY)
    b.append('<text x="474" y="58" text-anchor="end" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">M.2</text>' % FAINT)
    # --- the two part labels, ticked off from under the board so no line
    #     touches the board edge
    b.append('<path d="M122 212 L122 219" stroke="%s" stroke-width="1.5" opacity=".55"/>' % GREY)
    b.append('<text x="122" y="236" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">CTRL</text>' % FAINT)
    b.append('<path d="M242 212 L242 219" stroke="%s" stroke-width="1.5" opacity=".55"/>' % GREY)
    b.append('<text x="242" y="236" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">NAND</text>' % FAINT)
    return _svg("28 32 458 220", "".join(b), "nvme_ssd")


# ==================================================================== scene 2
def hdd():
    """A spinning hard disk: the platter is a real disc, the actuator arm
    reaches the centre hub, and the connector block sits on the back edge."""
    PX, PY = 424.0, 112.0      # the actuator pivot, top right
    HX, HY = 236.0, 200.0      # the centre hub
    b = []
    # --- the connector block on the back edge, drawn first so the body edge
    #     closes it off
    b.append('<rect x="180" y="44" width="140" height="30" rx="3" fill="rgba(246,246,244,.05)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    for i in range(7):
        b.append('<path d="M%d 52 L%d 66" stroke="%s" stroke-width="1.5" opacity=".55"/>'
                 % (198 + i * 18, 198 + i * 18, GREY))
    # --- the body
    b.append('<rect x="36" y="76" width="428" height="252" rx="14" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the platter: a real disc, so the arm can be drawn over it
    b.append('<circle cx="%d" cy="%d" r="100" fill="#0D1110" stroke="%s" stroke-width="3"/>'
             % (int(HX), int(HY), INK))
    b.append('<circle cx="%d" cy="%d" r="74" fill="none" stroke="%s" stroke-width="1.5"/>'
             % (int(HX), int(HY), HAIR))
    # --- the actuator arm: a tapered bar from the pivot to the hub
    dx, dy = HX - PX, HY - PY
    ln = math.hypot(dx, dy)
    ux, uy = dx / ln, dy / ln
    nx, ny = -uy, ux
    wp, wh = 11.0, 6.0
    tx, ty = HX - ux * 12.0, HY - uy * 12.0
    b.append('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z" fill="#0D1110" '
             'stroke="%s" stroke-width="2.5" stroke-linejoin="round"/>'
             % (PX + nx * wp, PY + ny * wp, PX - nx * wp, PY - ny * wp,
                tx - nx * wh, ty - ny * wh, tx + nx * wh, ty + ny * wh, INK))
    # --- the pivot boss, opaque over the arm end
    b.append('<circle cx="%d" cy="%d" r="13" fill="#0D1110" stroke="%s" stroke-width="2.5"/>'
             % (int(PX), int(PY), INK))
    # --- the head, resting on the centre hub. This is the one gold thing.
    b.append('<circle cx="%d" cy="%d" r="14" fill="%s"/>' % (int(HX), int(HY), GOLD))
    b.append('<circle cx="%d" cy="%d" r="5" fill="#0D1110"/>' % (int(HX), int(HY)))
    # --- captions in clear air above the drive
    b.append('<text x="36" y="30" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="800" fill="%s" letter-spacing="3">HARD DRIVE</text>' % GREY)
    b.append('<text x="464" y="30" text-anchor="end" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">SPINNING</text>' % FAINT)
    return _svg("24 6 452 334", "".join(b), "hdd")


# ==================================================================== scene 3
def model_file():
    """A model file on disk: a document with a folded corner, a gold file-type
    label and a small size badge."""
    b = []
    # --- the page, with the top right corner cut away for the fold
    b.append('<path d="M112 44 Q112 36 120 36 L320 36 L380 96 L380 320 Q380 328 372 328 '
             'L120 328 Q112 328 112 320 Z" fill="rgba(246,246,244,.02)" stroke="%s" '
             'stroke-width="3" stroke-linejoin="round"/>' % INK)
    # --- the folded flap over the cut corner
    b.append('<path d="M320 36 L380 96 L320 96 Z" fill="rgba(246,246,244,.10)" stroke="%s" '
             'stroke-width="2" stroke-linejoin="round"/>' % INK)
    # --- the gold file-type label
    b.append('<rect x="140" y="62" width="92" height="30" rx="6" fill="%s"/>' % GOLD)
    b.append('<text x="186" y="83" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="800" fill="#0D1110" letter-spacing="2">GGUF</text>')
    # --- the body text of the document
    for i, w in enumerate([200, 216, 190, 216, 160]):
        b.append('<rect x="140" y="%d" width="%d" height="7" rx="3.5" fill="%s" opacity=".30"/>'
                 % (124 + i * 28, w, INK))
    # --- the size badge, bottom right, clear of every line above it.
    #     A size ladder, not a number: nothing in the library may claim a
    #     figure it cannot trace to a source.
    b.append('<rect x="232" y="268" width="120" height="30" rx="15" fill="rgba(246,246,244,.04)" '
             'stroke="%s" stroke-width="1.5"/>' % FAINT)
    for k, h in enumerate([8, 13, 18]):
        b.append('<rect x="%d" y="%d" width="6" height="%d" rx="2" fill="%s" opacity="%s"/>'
                 % (248 + k * 12, 290 - h, h, INK, ".70" if k == 2 else ".38"))
    return _svg("100 24 292 316", "".join(b), "model_file")


# ==================================================================== scene 4
def gguf_blocks():
    """A GGUF packed in mixed bit precision: a tray of blocks, the biggest
    ones gold."""
    b = []
    # --- the tray
    b.append('<rect x="40" y="48" width="420" height="256" rx="14" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="54" y="62" width="392" height="228" rx="9" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    # --- the two biggest blocks: full precision, and the only gold
    b.append('<rect x="76" y="84" width="88" height="88" rx="6" fill="%s"/>' % GOLD)
    b.append('<text x="120" y="137" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="26" font-weight="800" fill="#0D1110" letter-spacing="1">F32</text>')
    b.append('<rect x="180" y="84" width="88" height="88" rx="6" fill="%s"/>' % GOLD)
    b.append('<text x="224" y="137" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="26" font-weight="800" fill="#0D1110" letter-spacing="1">F16</text>')
    # --- the mid blocks: quantised
    b.append('<rect x="288" y="84" width="64" height="64" rx="5" fill="rgba(246,246,244,.05)" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    b.append('<text x="320" y="123" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="20" font-weight="800" fill="%s" letter-spacing="1">Q8</text>' % INK)
    b.append('<rect x="368" y="84" width="48" height="48" rx="5" fill="rgba(246,246,244,.05)" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    b.append('<text x="392" y="114" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="800" fill="%s" letter-spacing="1">Q4</text>' % INK)
    # --- the middle row: quantised blocks of mixed sizes, sitting on one line
    for x, w, h, lab in [(76, 44, 42, "Q5"), (132, 64, 30, "Q6"), (208, 36, 42, "Q3"),
                         (256, 52, 48, "Q2"), (320, 40, 32, "Q4"), (372, 44, 42, "Q6")]:
        y = 240 - h
        b.append('<rect x="%d" y="%d" width="%d" height="%d" rx="4" fill="rgba(246,246,244,.05)" '
                 'stroke="%s" stroke-width="1.5"/>' % (x, y, w, h, INK))
        b.append('<text x="%d" y="%d" text-anchor="middle" font-family="FuseMono, monospace" '
                 'font-size="13" font-weight="700" fill="%s" letter-spacing="1">%s</text>'
                 % (x + w // 2, y + h // 2 + 5, GREY, lab))
    # --- the row of tiny blocks: the packed tail of the file
    for x, w in [(76, 24), (108, 36), (152, 16), (176, 44), (228, 28),
                 (264, 48), (320, 22), (350, 34), (392, 24)]:
        b.append('<rect x="%d" y="256" width="%d" height="24" rx="3" fill="%s" opacity=".30"/>'
                 % (x, w, INK))
    # --- captions above the tray
    b.append('<text x="40" y="30" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="800" fill="%s" letter-spacing="3">MIXED PRECISION</text>' % GREY)
    b.append('<text x="460" y="30" text-anchor="end" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">ONE FILE</text>' % FAINT)
    return _svg("28 6 444 310", "".join(b), "gguf_blocks")


# ==================================================================== scene 5
def folder():
    """A folder a download lands in: an open folder, a file poking out of it
    and a gold download arrow above."""
    b = []
    # --- the back of the folder, open at the bottom. No bottom edge, because
    #     the front flap covers that part of it.
    b.append('<path d="M84 152 L84 104 Q84 88 100 88 L156 88 L180 110 L452 110 '
             'Q468 110 468 126 L468 152" fill="none" stroke="%s" stroke-width="3" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % INK)

    # --- the file, tilted as it pokes out of the pocket. The points are
    #     rotated by hand, because a <g> may never carry a transform.
    CX, CY = 276.0, 200.0      # the sheet's bottom centre, buried in the pocket
    HW, HH = 36.0, 130.0
    TH = math.radians(-8.0)
    ca, sa = math.cos(TH), math.sin(TH)

    def rp(lx, ly):
        """a point on the tilted sheet"""
        return (CX + lx * ca - ly * sa, CY + lx * sa + ly * ca)

    def poly(pts):
        return "M" + " L".join("%.1f %.1f" % p for p in pts) + " Z"

    def bar(lx1, ly1, lx2, ly2, t):
        """a bar on the tilted sheet, given its two ends"""
        dx, dy = lx2 - lx1, ly2 - ly1
        ln = math.hypot(dx, dy)
        nx, ny = -dy / ln * t / 2.0, dx / ln * t / 2.0
        return poly([rp(lx1 + nx, ly1 + ny), rp(lx2 + nx, ly2 + ny),
                     rp(lx2 - nx, ly2 - ny), rp(lx1 - nx, ly1 - ny)])

    b.append('<path d="%s" fill="#0D1110" stroke="%s" stroke-width="3" '
             'stroke-linejoin="round"/>'
             % (poly([rp(-HW, -HH), rp(HW, -HH), rp(HW, 0.0), rp(-HW, 0.0)]), INK))
    b.append('<path d="%s" fill="%s" opacity=".30"/>' % (bar(-24, -96, 24, -96, 6), INK))
    b.append('<path d="%s" fill="%s" opacity=".30"/>' % (bar(-24, -74, 6, -74, 6), INK))

    # --- the front flap, opaque, so the file is tucked inside it
    b.append('<path d="M84 152 L468 152 L456 244 L96 244 Z" fill="#0D1110" stroke="%s" '
             'stroke-width="3" stroke-linejoin="round"/>' % INK)
    # --- the gold download arrow, breathing above the folder
    b.append('<g data-amb="pulse" data-amb-k="0" data-amb-speed="1.5">')
    b.append('<path d="M276 14 L276 46" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % GOLD)
    b.append('<path d="M256 26 L276 48 L296 26" fill="none" stroke="%s" stroke-width="6" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % GOLD)
    b.append('</g>')
    # --- caption, below the folder and clear of it
    b.append('<text x="276" y="276" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="800" fill="%s" letter-spacing="3">SAVED TO DISK</text>' % GREY)
    return _svg("72 -1 408 293", "".join(b), "folder")
