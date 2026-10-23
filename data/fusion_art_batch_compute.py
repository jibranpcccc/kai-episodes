# -*- coding: utf-8 -*-
"""
FUSION ART BATCH - compute. Generated for the Byte Forensics asset library.

Five flat line-art drawings of the silicon itself: the package, the die,
the wafer it was cut from, a two-die package, and a GPU+CPU superchip.

Same rules as the contract: ONE accent (GOLD) per drawing, no transform on
any <g>, a tight viewBox with the drawing centred, nothing overlapping,
and motion only where a part would really move. Nothing in this batch
moves, so there are no ambient hooks at all.
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
def chip():
    """A processor package from directly above: substrate, die, core, pin 1."""
    b = []
    # --- the substrate
    b.append('<rect x="120" y="60" width="280" height="280" rx="14" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="136" y="76" width="248" height="248" rx="10" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    # --- the pin comb: fine pins off the top and bottom edges
    for i in range(16):
        b.append('<rect x="%d" y="38" width="5" height="22" rx="1" fill="%s" opacity=".45"/>'
                 % (152 + i * 14, INK))
        b.append('<rect x="%d" y="340" width="5" height="22" rx="1" fill="%s" opacity=".45"/>'
                 % (152 + i * 14, INK))
    # --- the die, and the core inside it
    b.append('<rect x="170" y="110" width="180" height="180" rx="4" fill="none" '
             'stroke="%s" stroke-width="2"/>' % INK)
    b.append('<rect x="210" y="150" width="100" height="100" rx="3" fill="rgba(246,246,244,.05)" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    b.append('<text x="260" y="205" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">CORE</text>' % GREY)
    # --- pin 1: the one gold thing
    b.append('<path d="M170 110 L192 110 L170 132 Z" fill="%s"/>' % GOLD)
    return _svg("108 26 304 348", "".join(b), "chip")


# ==================================================================== scene 2
def die():
    """A silicon die up close: core blocks, a memory strip, a gold label."""
    b = []
    # --- the die
    b.append('<rect x="96" y="56" width="316" height="304" rx="10" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the core block, cut into a 4 x 4 grid
    b.append('<rect x="108" y="80" width="232" height="208" rx="4" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    for r in range(4):
        for c in range(4):
            b.append('<rect x="%d" y="%d" width="48" height="44" rx="2" fill="none" '
                     'stroke="%s" stroke-width="1.5" opacity=".7"/>'
                     % (116 + c * 56, 88 + r * 52, INK))
    # --- the memory strip down the right edge, cut into four packages
    b.append('<rect x="352" y="80" width="48" height="208" rx="4" fill="%s" opacity=".9"/>' % GOLD)
    for y in (134, 188, 242):
        b.append('<rect x="356" y="%d" width="40" height="4" fill="#0D1110"/>' % y)
    # --- the gold label, printed on the die
    b.append('<rect x="108" y="300" width="116" height="32" rx="4" fill="%s"/>' % GOLD)
    b.append('<text x="166" y="322" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="800" fill="#0D1110" letter-spacing="2">DIE 01</text>')
    return _svg("84 44 340 328", "".join(b), "die")


# ==================================================================== scene 3
def wafer():
    """A silicon wafer from above: the flat, a grid of dies, a few good ones."""
    CX, CY, R = 200.0, 200.0, 150.0
    b = []
    # --- the wafer: a circle with a flat cut out of the bottom
    flat_y = CY + R - 14
    half = math.sqrt(R * R - (flat_y - CY) ** 2)
    x0, x1 = CX - half, CX + half
    b.append('<path d="M%.1f %.1f A%.0f %.0f 0 1 1 %.1f %.1f L%.1f %.1f Z" '
             'fill="rgba(246,246,244,.02)" stroke="%s" stroke-width="3" '
             'stroke-linejoin="round"/>'
             % (x0, flat_y, R, R, x1, flat_y, x0, flat_y, INK))
    # --- the dies cut across the wafer, a few of them good
    pitch, cell, good = 30, 21, set([(-3, 1), (0, -2), (2, 0), (1, 3), (-1, -1)])
    for i in range(-4, 5):
        for j in range(-4, 5):
            # only the dies that sit wholly on the wafer
            if math.hypot(pitch * abs(i) + cell / 2.0, pitch * abs(j) + cell / 2.0) > R - 4:
                continue
            x = CX + i * pitch - cell / 2.0
            y = CY + j * pitch - cell / 2.0
            if (i, j) in good:
                b.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="1" fill="%s"/>'
                         % (x, y, cell, cell, GOLD))
            else:
                b.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="1" fill="none" '
                         'stroke="%s" stroke-width="1.5" opacity=".55"/>'
                         % (x, y, cell, cell, INK))
    # --- the arrow that points at the flat
    b.append('<path d="M200 392 L200 354" fill="none" stroke="%s" stroke-width="2.5" '
             'stroke-linecap="round"/>' % GREY)
    b.append('<path d="M190 364 L200 352 L210 364" fill="none" stroke="%s" stroke-width="2.5" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % GREY)
    b.append('<text x="218" y="384" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="2">FLAT</text>' % GREY)
    return _svg("38 38 324 366", "".join(b), "wafer")


# ==================================================================== scene 4
def two_die():
    """Two dies in one package, joined across the gap by a gold trace."""
    b = []
    # --- the package
    b.append('<rect x="56" y="64" width="388" height="232" rx="12" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the two dies, each cut into a 3 x 3 grid
    for dx in (96, 286):
        b.append('<rect x="%d" y="96" width="118" height="136" rx="4" fill="none" '
                 'stroke="%s" stroke-width="2"/>' % (dx, INK))
        for r in range(3):
            for c in range(3):
                b.append('<rect x="%d" y="%d" width="28" height="34" rx="2" fill="none" '
                         'stroke="%s" stroke-width="1.5" opacity=".7"/>'
                         % (dx + 12 + c * 35, 108 + r * 39, INK))
    # --- the trace that bridges the gap
    b.append('<path d="M214 164 L286 164" fill="none" stroke="%s" stroke-width="3" '
             'stroke-linecap="round"/>' % GOLD)
    # --- which die is which
    b.append('<text x="155" y="262" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">DIE A</text>' % GREY)
    b.append('<text x="345" y="262" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">DIE B</text>' % GREY)
    return _svg("44 52 412 256", "".join(b), "two_die")


# ==================================================================== scene 5
def superchip():
    """An RTX die and a CPU die in one package, bridged by a gold bar."""
    b = []
    # --- the package
    b.append('<rect x="56" y="84" width="400" height="236" rx="12" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the memory stacks along the top edge
    for i in range(5):
        b.append('<rect x="%d" y="104" width="56" height="30" rx="3" fill="%s" opacity=".85"/>'
                 % (92 + i * 68, GOLD))
    # --- the GPU die, a fine grid of blocks
    b.append('<rect x="80" y="156" width="152" height="128" rx="4" fill="none" '
             'stroke="%s" stroke-width="2"/>' % INK)
    for r in range(4):
        for c in range(4):
            b.append('<rect x="%d" y="%d" width="25" height="20" rx="2" fill="none" '
                     'stroke="%s" stroke-width="1.5" opacity=".7"/>'
                     % (92 + c * 34, 168 + r * 28, INK))
    # --- the CPU die, a few big blocks
    b.append('<rect x="280" y="156" width="152" height="128" rx="4" fill="none" '
             'stroke="%s" stroke-width="2"/>' % INK)
    for r in range(2):
        for c in range(2):
            b.append('<rect x="%d" y="%d" width="59" height="48" rx="3" fill="none" '
                     'stroke="%s" stroke-width="1.5" opacity=".7"/>'
                     % (292 + c * 69, 168 + r * 56, INK))
    # --- the interconnect bar, bridging the two dies
    b.append('<rect x="226" y="200" width="60" height="40" rx="8" fill="%s"/>' % GOLD)
    # --- which die is which
    b.append('<text x="156" y="308" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="800" fill="%s" letter-spacing="2">GPU</text>' % GREY)
    b.append('<text x="356" y="308" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="800" fill="%s" letter-spacing="2">CPU</text>' % GREY)
    return _svg("44 72 424 260", "".join(b), "superchip")
