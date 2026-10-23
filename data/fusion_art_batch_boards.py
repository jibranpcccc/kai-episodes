# -*- coding: utf-8 -*-
"""FUSION ART BATCH — boards. Generated for the Byte Forensics asset library.

Five drawings about PC hardware boards: a bare PCB seen from above, a full ATX
motherboard, a PCIe x16 slot in side elevation, two cards seated in one
motherboard, and a vertical riser card.

Same rules as data/fusion_art.py:
  * a <g> NEVER carries a transform attribute (this batch has no motion at all,
    so it has no <g> wrappers either).
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
def pcb():
    """A bare circuit board from above: rounded rectangle, square component
    footprints, two long connector slots on one edge, via clusters and one
    gold trace."""
    b = []
    # --- the board
    b.append('<rect x="34" y="34" width="392" height="232" rx="12" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- mounting holes, punched through the board
    for hx, hy in ((48, 52), (408, 52), (48, 248), (408, 248)):
        b.append('<circle cx="%d" cy="%d" r="5" fill="#0D1110" stroke="%s" stroke-width="1.5"/>'
                 % (hx, hy, INK))
    # --- two long connector slots on the left edge, with their contact combs
    for sy in (60, 168):
        b.append('<rect x="60" y="%d" width="16" height="92" rx="4" fill="none" '
                 'stroke="%s" stroke-width="3"/>' % (sy, INK))
        for i in range(6):
            b.append('<rect x="63" y="%d" width="10" height="3" rx="1.5" fill="%s" opacity=".55"/>'
                     % (sy + 12 + i * 13, INK))
    # --- component footprints
    b.append('<rect x="96" y="58" width="58" height="58" rx="4" fill="rgba(246,246,244,.03)" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    b.append('<circle cx="106" cy="68" r="3.5" fill="%s"/>' % INK)
    b.append('<rect x="176" y="66" width="30" height="30" rx="3" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    b.append('<rect x="228" y="58" width="44" height="44" rx="4" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    b.append('<rect x="300" y="62" width="26" height="26" rx="3" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    b.append('<rect x="352" y="70" width="38" height="38" rx="4" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    # --- via fields: three clusters of small pads
    for vx, vy in ((178, 108), (190, 108), (202, 108),
                   (178, 120), (190, 120), (202, 120),
                   (252, 208), (264, 208), (276, 208),
                   (252, 220), (264, 220), (276, 220),
                   (356, 186), (368, 186), (356, 198), (368, 198)):
        b.append('<circle cx="%d" cy="%d" r="2.8" fill="%s" opacity=".45"/>' % (vx, vy, INK))
    # --- the one gold trace, leaving the big chip and running to a far pad
    b.append('<path d="M110 116 L110 168 L150 168 L150 240 L372 240" fill="none" stroke="%s" '
             'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>' % GOLD)
    b.append('<circle cx="110" cy="168" r="3.5" fill="%s"/>' % GOLD)
    b.append('<circle cx="372" cy="240" r="5" fill="%s"/>' % GOLD)
    # --- caption, clear of the board
    b.append('<text x="34" y="292" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="700" fill="%s" letter-spacing="3">PCB - TOP VIEW</text>' % GREY)
    return _svg("20.5 20.5 419 287.5", "".join(b), "pcb")


# ==================================================================== scene 2
def motherboard():
    """A full ATX board from above: large rectangle, CPU socket, four DIMM
    slots in a row, a PCIe slot, a chip cluster and I/O ports along the
    bottom edge."""
    b = []
    # --- the board
    b.append('<rect x="30" y="30" width="440" height="352" rx="10" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- mounting holes
    for hx, hy in ((48, 48), (452, 48), (48, 364), (452, 364), (48, 206), (452, 206)):
        b.append('<circle cx="%d" cy="%d" r="5" fill="#0D1110" stroke="%s" stroke-width="1.5"/>'
                 % (hx, hy, INK))
    # --- CPU socket: frame, inner land area and the retention lever
    b.append('<text x="64" y="48" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="2">CPU</text>' % FAINT)
    b.append('<rect x="58" y="58" width="78" height="78" rx="4" fill="rgba(246,246,244,.03)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="72" y="72" width="50" height="50" rx="3" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % GREY)
    b.append('<rect x="139" y="62" width="9" height="70" rx="4" fill="none" '
             'stroke="%s" stroke-width="2.5"/>' % INK)
    # --- chipset heatsink below the socket
    b.append('<rect x="58" y="168" width="96" height="48" rx="4" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="1.5"/>' % GREY)
    # --- four DIMM slots in a row
    for i in range(4):
        sx = 196 + i * 24
        b.append('<rect x="%d" y="46" width="14" height="8" rx="2" fill="%s" opacity=".55"/>'
                 % (sx, INK))
        b.append('<rect x="%d" y="54" width="14" height="142" rx="3" fill="none" '
                 'stroke="%s" stroke-width="1.5"/>' % (sx, INK))
        b.append('<rect x="%d" y="176" width="14" height="7" fill="#0D1110"/>' % sx)
    # --- chip cluster, top right
    for cx, cy in ((330, 62), (372, 62), (414, 62), (330, 104), (372, 104), (414, 104)):
        b.append('<rect x="%d" y="%d" width="30" height="30" rx="3" fill="rgba(246,246,244,.02)" '
                 'stroke="%s" stroke-width="1.5"/>' % (cx, cy, INK))
    # --- the 24 pin power header
    b.append('<rect x="300" y="180" width="44" height="26" rx="3" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    for row in (187, 199):
        for i in range(6):
            b.append('<circle cx="%d" cy="%d" r="2" fill="%s" opacity=".5"/>'
                     % (307 + i * 6.4, row, INK))
    # --- a short secondary slot, drawn dim so the long one stays the subject
    b.append('<rect x="58" y="244" width="110" height="16" rx="3" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % GREY)
    b.append('<rect x="66" y="250" width="94" height="4" rx="2" fill="%s" opacity=".35"/>' % GREY)
    # --- the PCIe x16 slot with its gold contacts
    b.append('<rect x="58" y="288" width="300" height="20" rx="4" fill="none" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="68" y="294" width="280" height="8" rx="2" fill="%s" opacity=".92"/>' % GOLD)
    b.append('<rect x="188" y="294" width="14" height="8" fill="#0D1110"/>')
    b.append('<text x="58" y="330" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="2">PCIe x16</text>' % GREY)
    # --- I/O ports along the bottom edge
    for px, pw in ((58, 34), (96, 26), (126, 34), (164, 26), (194, 40), (238, 26), (268, 34)):
        b.append('<rect x="%d" y="358" width="%d" height="16" rx="2" fill="#0D1110" '
                 'stroke="%s" stroke-width="1.5"/>' % (px, pw, INK))
    # --- caption, clear of the board
    b.append('<text x="30" y="406" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="700" fill="%s" letter-spacing="3">ATX MOTHERBOARD</text>' % GREY)
    return _svg("16.5 16.5 467 405.5", "".join(b), "motherboard")


# ==================================================================== scene 3
def pcie_slot():
    """A PCIe x16 slot in side elevation: a long channel with a gold contact
    strip inside, a retention latch at one end, and a short x1 slot below."""
    b = []
    # --- the x16 body
    b.append('<rect x="36" y="116" width="428" height="62" rx="6" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the channel cut into the top face
    b.append('<path d="M58 116 L58 150 L442 150 L442 116" fill="none" stroke="%s" '
             'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>' % INK)
    # --- the gold contact strip, sitting on the channel floor
    b.append('<rect x="64" y="140" width="372" height="7" rx="2" fill="%s" opacity=".95"/>' % GOLD)
    # --- the retention latch: a clip head over the far end and its stem
    b.append('<rect x="421" y="76" width="26" height="30" rx="4" fill="#0D1110" stroke="%s" '
             'stroke-width="3"/>' % INK)
    b.append('<path d="M434 104 L434 130" stroke="%s" stroke-width="7" stroke-linecap="round"/>'
             % INK)
    b.append('<text x="36" y="104" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="700" fill="%s" letter-spacing="2">PCIe x16</text>' % GREY)
    # --- the short x1 slot below, drawn in ink but dimmer
    b.append('<rect x="36" y="212" width="176" height="42" rx="6" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="2"/>' % INK)
    b.append('<path d="M56 212 L56 240 L192 240 L192 212" fill="none" stroke="%s" '
             'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>' % GREY)
    b.append('<rect x="60" y="232" width="128" height="5" rx="2" fill="%s" opacity=".45"/>' % GREY)
    b.append('<text x="224" y="238" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="2">x1</text>' % FAINT)
    # --- caption, right aligned into the clear space under the long slot
    b.append('<text x="464" y="286" text-anchor="end" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="700" fill="%s" letter-spacing="3">'
             'PCIe SLOT - SIDE VIEW</text>' % GREY)
    return _svg("22.5 62.5 455 239.1", "".join(b), "pcie_slot")


# ==================================================================== scene 4
def dual_slot():
    """Two cards seated in one motherboard: parallel card outlines with a gap,
    a bracket at the left of each, gold connector edges at the bottom."""
    b = []
    # --- the motherboard substrate, dim so the cards read first
    b.append('<rect x="30" y="30" width="440" height="290" rx="10" fill="rgba(246,246,244,.015)" '
             'stroke="%s" stroke-width="2"/>' % GREY)
    # --- a bracket at the left of each card, drawn first so the card edge
    #     closes over the bracket's right edge
    for by, bh in ((46, 126), (178, 126)):
        b.append('<rect x="40" y="%d" width="26" height="%d" rx="3" fill="#0D1110" '
                 'stroke="%s" stroke-width="3"/>' % (by, bh, INK))
        for i in range(3):
            b.append('<rect x="46" y="%d" width="12" height="3" rx="1.5" fill="%s" opacity=".5"/>'
                     % (by + 14 + i * 16, INK))
    # --- the two cards, parallel with a gap between them
    for cy in (62, 190):
        b.append('<rect x="66" y="%d" width="360" height="96" rx="6" fill="rgba(246,246,244,.03)" '
                 'stroke="%s" stroke-width="3"/>' % (cy, INK))
    # --- chips on the right end of each card
    for cy in (84, 212):
        for cx in (306, 346, 386):
            b.append('<rect x="%d" y="%d" width="26" height="26" rx="3" fill="none" '
                     'stroke="%s" stroke-width="1.5"/>' % (cx, cy, GREY))
    # --- the PCIe slots the cards drop into
    for sy in (158, 286):
        b.append('<rect x="72" y="%d" width="348" height="12" rx="2" fill="none" '
                 'stroke="%s" stroke-width="1.5"/>' % (sy, GREY))
    # --- the gold connector edges, hanging into those slots
    for gy in (146, 274):
        b.append('<rect x="80" y="%d" width="332" height="14" rx="2" fill="%s" opacity=".92"/>'
                 % (gy, GOLD))
        b.append('<rect x="116" y="%d" width="14" height="14" fill="#0D1110"/>' % gy)
    # --- caption, clear of the board
    b.append('<text x="30" y="346" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="700" fill="%s" letter-spacing="3">TWO CARDS, ONE BOARD</text>' % GREY)
    return _svg("17 17 466 345", "".join(b), "dual_slot")


# ==================================================================== scene 5
def riser():
    """A vertical riser: a narrow tall board on edge, a short gold PCIe edge
    connector at the bottom, a ribbon connector at the top and a thin gold
    trace running up it."""
    b = []
    # --- the motherboard slab it plugs into
    b.append('<rect x="50" y="302" width="380" height="34" rx="4" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="2"/>' % GREY)
    for hx in (70, 410):
        b.append('<circle cx="%d" cy="319" r="4" fill="#0D1110" stroke="%s" stroke-width="1.5"/>'
                 % (hx, INK))
    # --- the PCIe slot in that slab
    b.append('<rect x="210" y="300" width="76" height="14" rx="2" fill="#0D1110" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the flat ribbon cable leaving the top, leaning over
    b.append('<path d="M230 80 L244 46 L280 46 L266 80 Z" fill="rgba(246,246,244,.04)" '
             'stroke="%s" stroke-width="1.5" stroke-linejoin="round"/>' % INK)
    # --- the riser board itself, standing on edge
    b.append('<rect x="200" y="102" width="96" height="200" rx="5" fill="rgba(246,246,244,.03)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- a small IC on the riser
    b.append('<rect x="206" y="116" width="16" height="16" rx="2" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % INK)
    # --- the ribbon connector on the top edge of the riser
    b.append('<rect x="208" y="78" width="80" height="26" rx="3" fill="#0D1110" stroke="%s" '
             'stroke-width="3"/>' % INK)
    for i in range(8):
        b.append('<rect x="%d" y="84" width="3" height="14" rx="1.5" fill="%s" opacity=".6"/>'
                 % (217 + i * 9, INK))
    # --- the thin gold trace running up the riser
    b.append('<path d="M232 300 L232 266 L268 266 L268 210 L214 210 L214 152 L274 152 '
             'L274 118 L240 118 L240 104" fill="none" stroke="%s" stroke-width="2.5" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % GOLD)
    for vx, vy in ((232, 266), (268, 210), (214, 152), (274, 118)):
        b.append('<circle cx="%d" cy="%d" r="3" fill="%s"/>' % (vx, vy, GOLD))
    # --- the short gold PCIe edge connector, seated in the slot
    b.append('<rect x="222" y="300" width="52" height="14" rx="2" fill="%s" opacity=".92"/>' % GOLD)
    b.append('<rect x="246" y="300" width="14" height="14" fill="#0D1110"/>')
    # --- caption, clear of the board
    b.append('<text x="50" y="362" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="700" fill="%s" letter-spacing="3">VERTICAL RISER</text>' % GREY)
    return _svg("37 33.25 406 345.15", "".join(b), "riser")


ART = {
    "pcb":        pcb,
    "motherboard": motherboard,
    "pcie_slot":  pcie_slot,
    "dual_slot":  dual_slot,
    "riser":      riser,
}
