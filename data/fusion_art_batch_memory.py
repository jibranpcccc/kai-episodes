# -*- coding: utf-8 -*-
"""FUSION ART BATCH — memory. Generated for the Byte Forensics asset library.

Five drawings about RAM: a desktop DIMM, a laptop SO-DIMM, stacked VRAM,
a populated memory bank and a cache array.

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
def ram_stick():
    """A desktop DDR DIMM seen from the side: long ink-outline board, eight
    chips, a gold contact edge with one key notch, a small gold label."""
    b = []
    # --- the eight memory chips, standing on the board. Drawn first so the
    #     board edge caps their bases.
    for i in range(8):
        x = 84 + i * 48
        b.append('<rect x="%d" y="84" width="40" height="56" rx="3" fill="rgba(246,246,244,.02)" '
                 'stroke="%s" stroke-width="1.5"/>' % (x, INK))
        b.append('<rect x="%d" y="102" width="16" height="4" rx="2" fill="%s" opacity=".30"/>'
                 % (x + 12, INK))
    # --- the gold contact edge, under the board
    b.append('<rect x="20" y="174" width="460" height="16" rx="2" fill="%s" opacity=".92"/>' % GOLD)
    # --- the key notch: a gap in the gold, cut back to the background
    b.append('<rect x="176" y="176" width="22" height="14" fill="#0D1110"/>')
    # --- the board itself
    b.append('<rect x="20" y="140" width="460" height="34" rx="3" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the small gold label at the end of the board
    b.append('<rect x="28" y="148" width="46" height="18" rx="2" fill="none" stroke="%s" '
             'stroke-width="1.5"/>' % GOLD)
    b.append('<rect x="36" y="153" width="30" height="3" rx="1.5" fill="%s"/>' % GOLD)
    b.append('<rect x="36" y="159" width="16" height="3" rx="1.5" fill="%s"/>' % GOLD)
    return _svg("6.5 70.5 487 133", "".join(b), "ram_stick")


# ==================================================================== scene 2
def sodimm():
    """A laptop SO-DIMM: shorter board, four chips, one smaller notch in the
    contact edge."""
    b = []
    # --- the four chips
    for i in range(4):
        x = 113 + i * 62
        b.append('<rect x="%d" y="92" width="48" height="48" rx="3" fill="rgba(246,246,244,.02)" '
                 'stroke="%s" stroke-width="1.5"/>' % (x, INK))
        b.append('<rect x="%d" y="106" width="18" height="4" rx="2" fill="%s" opacity=".30"/>'
                 % (x + 15, INK))
    # --- the gold contact edge
    b.append('<rect x="60" y="170" width="340" height="15" rx="2" fill="%s" opacity=".92"/>' % GOLD)
    # --- the single small notch
    b.append('<rect x="214" y="172" width="18" height="13" fill="#0D1110"/>')
    # --- the board
    b.append('<rect x="60" y="140" width="340" height="30" rx="3" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the small gold label
    b.append('<rect x="70" y="147" width="38" height="16" rx="2" fill="none" stroke="%s" '
             'stroke-width="1.5"/>' % GOLD)
    b.append('<rect x="77" y="152" width="24" height="3" rx="1.5" fill="%s"/>' % GOLD)
    b.append('<rect x="77" y="158" width="12" height="3" rx="1.5" fill="%s"/>' % GOLD)
    return _svg("46.5 78.5 367 118.5", "".join(b), "sodimm")


# ==================================================================== scene 3
def vram_module():
    """Stacked VRAM: two slim boards, chips facing outward, bridged by a gold
    pin interconnect."""
    b = []
    # --- chips on the top board, and chips on the bottom board facing away
    for i in range(4):
        x = 90 + i * 76
        b.append('<rect x="%d" y="36" width="52" height="28" rx="3" fill="rgba(246,246,244,.02)" '
                 'stroke="%s" stroke-width="1.5"/>' % (x, INK))
        b.append('<rect x="%d" y="46" width="18" height="4" rx="2" fill="%s" opacity=".28"/>'
                 % (x + 17, INK))
        b.append('<rect x="%d" y="212" width="52" height="28" rx="3" fill="rgba(246,246,244,.02)" '
                 'stroke="%s" stroke-width="1.5"/>' % (x, INK))
        b.append('<rect x="%d" y="222" width="18" height="4" rx="2" fill="%s" opacity=".28"/>'
                 % (x + 17, INK))
    # --- the two boards, each with an inner edge so the slab is not empty
    b.append('<rect x="36" y="64" width="388" height="44" rx="4" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="50" y="74" width="360" height="24" rx="3" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    b.append('<rect x="36" y="168" width="388" height="44" rx="4" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="50" y="178" width="360" height="24" rx="3" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    # --- the gold interconnect: a comb of pins bridging the gap between them
    for i in range(9):
        x = 131 + i * 24
        b.append('<rect x="%d" y="108" width="6" height="60" rx="2" fill="%s"/>' % (x, GOLD))
    return _svg("22.5 22.5 415 231", "".join(b), "vram_module")


# ==================================================================== scene 4
def memory_bank():
    """A tall memory bank of eight slots. One slot is live and gold, the rest
    sit dim."""
    b = []
    # --- the frame
    b.append('<rect x="120" y="40" width="280" height="380" rx="10" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- captions, above the frame, clear of everything
    b.append('<text x="120" y="28" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="3">MEMORY BANK</text>' % FAINT)
    b.append('<text x="400" y="28" text-anchor="end" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="3">8 SLOTS</text>' % FAINT)
    # --- the eight slots. Slot 5 is the live one.
    for i in range(8):
        y = 67 + i * 42
        if i == 4:
            b.append('<rect x="150" y="%d" width="220" height="32" rx="4" fill="rgba(245,197,49,.14)" '
                     'stroke="%s" stroke-width="3"/>' % (y, GOLD))
            b.append('<rect x="164" y="%d" width="14" height="14" rx="2" fill="%s"/>' % (y + 9, GOLD))
            b.append('<rect x="188" y="%d" width="52" height="7" rx="3.5" fill="%s"/>' % (y + 12, GOLD))
        else:
            b.append('<rect x="150" y="%d" width="220" height="32" rx="4" fill="none" '
                     'stroke="%s" stroke-width="1.5"/>' % (y, HAIR))
            b.append('<rect x="164" y="%d" width="14" height="14" rx="2" fill="none" '
                     'stroke="%s" stroke-width="1.5"/>' % (y + 9, GREY))
            b.append('<rect x="188" y="%d" width="52" height="7" rx="3.5" fill="%s" opacity=".45"/>'
                     % (y + 12, GREY))
        # --- the key notch at the end of every chip
        b.append('<rect x="350" y="%d" width="10" height="16" fill="#0D1110"/>' % (y + 8))
    return _svg("106.5 6 307 427.5", "".join(b), "memory_bank")


# ==================================================================== scene 5
def cache_grid():
    """An 8 x 4 cache array with a diagonal band of live gold cells."""
    b = []
    # --- captions above the array
    b.append('<text x="38" y="46" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="3">L2 / L3 CACHE</text>' % FAINT)
    b.append('<text x="462" y="46" text-anchor="end" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="3">8 X 4</text>' % FAINT)
    # --- the array. The band runs from the top right to the bottom left.
    for r in range(4):
        for c in range(8):
            x = 38 + c * 54
            y = 70 + r * 46
            if c + 2 * r in (6, 7):
                b.append('<rect x="%d" y="%d" width="46" height="38" rx="3" fill="%s"/>' % (x, y, GOLD))
            else:
                b.append('<rect x="%d" y="%d" width="46" height="38" rx="3" fill="rgba(246,246,244,.02)" '
                         'stroke="%s" stroke-width="1.5"/>' % (x, y, HAIR))
    return _svg("24.5 24 449.5 234", "".join(b), "cache_grid")
