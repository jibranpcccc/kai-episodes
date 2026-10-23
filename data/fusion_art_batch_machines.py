# -*- coding: utf-8 -*-
"""
FUSION ART BATCH — machines. Generated for the Byte Forensics asset library.

Five local-AI machines drawn in the same flat line-art grammar as
data/fusion_art.py: no photography, no gradients on strokes, no shadows, no
product-shot perspective, one accent (gold) per drawing.

A <g> NEVER carries a transform attribute. Every drawing is centred in a
tight viewBox with a ~12 unit margin. Gold is the only accent in the file and
it lands once per drawing.
"""
import math

INK = "#F6F6F4"
GOLD = "#F5C531"
CYAN = "#38D9E8"
RED = "#E12A27"
GREY = "rgba(246,246,244,.52)"
FAINT = "rgba(246,246,244,.30)"
HAIR = "rgba(246,246,244,.18)"

BG = "#0D1110"


def _svg(view, body, slug):
    """view is a FULL viewBox: "min-x min-y width height"."""
    return (
        '<svg viewBox="%s" class="art" data-art="%s" '
        'xmlns="http://www.w3.org/2000/svg">%s</svg>' % (view, slug, body)
    )


def _rot(px, py, ang, ox, oy):
    """Rotate a point by `ang` degrees about (ox, oy). Used by the laptop so
    the whole machine can sit at a slight angle without a transform attribute."""
    a = math.radians(ang)
    ca, sa = math.cos(a), math.sin(a)
    dx, dy = px - ox, py - oy
    return (ox + dx * ca - dy * sa, oy + dx * sa + dy * ca)


# ==================================================================== machine 1
def mini_pc():
    """A small square mini PC: power button, two front ports, a vent column."""
    b = []
    # --- the case, square and rounded, seen straight from the front
    b.append('<rect x="120" y="48" width="200" height="200" rx="14" fill="none" '
             'stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % INK)
    # --- power button, top left of the front face
    b.append('<circle cx="150" cy="78" r="9" fill="none" stroke="%s" stroke-width="1.5" '
             'opacity=".75"/>' % INK)
    b.append('<path d="M150 71 L150 78" stroke="%s" stroke-width="1.5" '
             'stroke-linecap="round" opacity=".75"/>' % INK)
    # --- two front ports, one USB-A and one USB-C, on the same line
    b.append('<rect x="138" y="148" width="22" height="10" rx="2" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    b.append('<rect x="168" y="150" width="14" height="6" rx="3" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    # --- the vent column, down the right side of the face
    for i in range(6):
        b.append('<rect x="252" y="%d" width="44" height="7" rx="3.5" fill="%s" '
                 'opacity=".30"/>' % (84 + i * 26, INK))
    # --- the one gold thing: a short status light
    b.append('<rect x="138" y="194" width="32" height="6" rx="3" fill="%s"/>' % GOLD)
    return _svg("108 36 224 224", "".join(b), "mini_pc")


# ==================================================================== machine 2
def tower_pc():
    """A mid-tower: glass side panel with the GPU inside, front grille, bays."""
    b = []
    # --- the case, tall and narrow so it reads as a tower and not a screen
    b.append('<rect x="100" y="20" width="220" height="340" rx="10" fill="none" '
             'stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % INK)
    # --- the glass side panel
    b.append('<rect x="114" y="36" width="126" height="310" rx="8" fill="none" '
             'stroke="%s" stroke-width="1.5" opacity=".40"/>' % INK)
    # --- the GPU, seen through the glass: a shroud with one fan in it
    b.append('<rect x="136" y="78" width="92" height="78" rx="6" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    b.append('<circle cx="182" cy="117" r="23" fill="none" stroke="%s" '
             'stroke-width="1.5" opacity=".55"/>' % INK)
    for k in range(7):
        a = k * (2 * math.pi / 7)
        b.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="1.5" '
                 'opacity=".28" stroke-linecap="round"/>'
                 % (182 + 6 * math.cos(a), 117 + 6 * math.sin(a),
                    182 + 19 * math.cos(a + 0.44), 117 + 19 * math.sin(a + 0.44), INK))
    b.append('<circle cx="182" cy="117" r="4" fill="%s" opacity=".80"/>' % INK)
    # --- the one gold thing: the PCIe edge of the card, keyed like the real one
    b.append('<rect x="122" y="90" width="14" height="54" rx="2" fill="%s"/>' % GOLD)
    b.append('<rect x="122" y="106" width="8" height="6" fill="%s"/>' % BG)
    b.append('<rect x="122" y="124" width="8" height="6" fill="%s"/>' % BG)
    # --- the CPU heatsink below it
    b.append('<rect x="136" y="182" width="76" height="78" rx="8" fill="none" '
             'stroke="%s" stroke-width="1.5" opacity=".45"/>' % INK)
    for x in (152, 168, 184, 200):
        b.append('<path d="M%d 196 L%d 244" stroke="%s" stroke-width="1.5" '
                 'opacity=".30" stroke-linecap="round"/>' % (x, x, HAIR))
    # --- the PSU, a flat slab across the bottom of the panel
    b.append('<rect x="126" y="286" width="100" height="34" rx="4" fill="%s" '
             'opacity=".10" stroke="%s" stroke-width="1.5"/>' % (INK, HAIR))
    # --- the front panel: power button and two front USB ports
    b.append('<circle cx="280" cy="54" r="9" fill="none" stroke="%s" '
             'stroke-width="1.5"/>' % INK)
    b.append('<rect x="254" y="80" width="20" height="8" rx="2" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    b.append('<rect x="278" y="80" width="20" height="8" rx="2" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    # --- the front grille
    for i in range(8):
        y = 112 + i * 17
        b.append('<path d="M250 %d L310 %d" stroke="%s" stroke-width="1.5" '
                 'stroke-linecap="round" opacity=".38"/>' % (y, y, INK))
    # --- the drive bays
    for i in range(3):
        b.append('<rect x="250" y="%d" width="60" height="22" rx="3" fill="none" '
                 'stroke="%s" stroke-width="1.5"/>' % (254 + i * 30, INK))
    return _svg("88 8 244 364", "".join(b), "tower_pc")


# ==================================================================== machine 3
def rack_server():
    """A 2U rack server: rack ears, screw holes, a row of drive bays."""
    b = []
    # --- the chassis, wide and shallow, ears included
    b.append('<rect x="58" y="76" width="404" height="136" rx="6" fill="none" '
             'stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % INK)
    # --- the seams where the rack ears meet the body
    b.append('<path d="M90 76 L90 212 M430 76 L430 212" fill="none" stroke="%s" '
             'stroke-width="1.5" opacity=".55"/>' % INK)
    # --- screw holes, both sides
    for cx in (74, 446):
        for cy in (96, 192):
            b.append('<circle cx="%d" cy="%d" r="4.5" fill="%s" stroke="%s" '
                     'stroke-width="1.5"/>' % (cx, cy, BG, INK))
    # --- the status LEDs, one gold and three dim
    b.append('<circle cx="118" cy="89" r="4" fill="%s"/>' % GOLD)
    for cx in (134, 150, 166):
        b.append('<circle cx="%d" cy="89" r="4" fill="%s" opacity=".55"/>' % (cx, INK))
    # --- the drive bays
    for i in range(8):
        x = 108 + i * 38
        b.append('<rect x="%d" y="104" width="32" height="88" rx="3" fill="none" '
                 'stroke="%s" stroke-width="1.5"/>' % (x, INK))
        b.append('<rect x="%d" y="116" width="14" height="3" rx="1.5" fill="%s" '
                 'opacity=".35"/>' % (x + 9, INK))
    return _svg("46 64 428 160", "".join(b), "rack_server")


# ==================================================================== machine 4
def mac_mini():
    """A small rounded cube on two feet, two front ports, a soft base line."""
    b = []
    # --- the body: a low, wide slab
    b.append('<rect x="116" y="84" width="248" height="92" rx="13" fill="none" '
             'stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % INK)
    # --- the seam between the top cover and the base
    b.append('<path d="M132 106 L348 106" stroke="%s" stroke-width="1.5" '
             'stroke-linecap="round" opacity=".38"/>' % INK)
    # --- the one gold thing: a small status LED in the top band
    b.append('<circle cx="340" cy="94" r="4" fill="%s"/>' % GOLD)
    # --- two front ports
    b.append('<rect x="138" y="146" width="22" height="9" rx="2" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    b.append('<circle cx="176" cy="150" r="5" fill="none" stroke="%s" '
             'stroke-width="1.5"/>' % INK)
    # --- the two feet
    for x in (144, 296):
        b.append('<rect x="%d" y="176" width="42" height="28" rx="4" fill="none" '
                 'stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % (x, INK))
    # --- the base line. A line, not a shadow.
    b.append('<path d="M100 204 L380 204" stroke="%s" stroke-width="1.5" '
             'stroke-linecap="round"/>' % HAIR)
    return _svg("88 72 304 144", "".join(b), "mac_mini")


# ==================================================================== machine 5
def laptop_closed():
    """A closed laptop at a slight angle: lid, base slab, gold latch."""
    ANG, PX, PY = -5.0, 150.0, 170.0

    def P(px, py):
        x, y = _rot(px, py, ANG, PX, PY)
        return "%.1f %.1f" % (x, y)

    b = []
    # --- the lid: rounded top corners, square where it meets the base
    b.append('<path d="M%s A14 14 %.1f 0 1 %s L%s A14 14 %.1f 0 1 %s L%s L%s Z" '
             'fill="none" stroke="%s" stroke-width="3" stroke-linecap="round" '
             'stroke-linejoin="round"/>'
             % (P(0, 14), ANG, P(14, 0), P(286, 0), ANG, P(300, 14),
                P(300, 170), P(0, 170), INK))
    # --- the base slab under it: rounded front corners
    b.append('<path d="M%s L%s L%s A8 8 %.1f 0 1 %s L%s A8 8 %.1f 0 1 %s Z" '
             'fill="none" stroke="%s" stroke-width="3" stroke-linecap="round" '
             'stroke-linejoin="round"/>'
             % (P(0, 170), P(300, 170), P(300, 188), ANG, P(292, 196),
                P(8, 196), ANG, P(0, 188), INK))
    # --- the one gold thing: the latch notch cut into the front edge
    b.append('<path d="M%s L%s L%s L%s Z" fill="%s" stroke="none"/>'
             % (P(140, 196), P(143, 183), P(157, 183), P(160, 196), GOLD))
    return _svg("-25 -23 338 243", "".join(b), "laptop_closed")


ART = {
    "mini_pc":       mini_pc,
    "tower_pc":      tower_pc,
    "rack_server":   rack_server,
    "mac_mini":      mac_mini,
    "laptop_closed": laptop_closed,
}
