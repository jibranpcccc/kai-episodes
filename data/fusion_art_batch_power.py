# -*- coding: utf-8 -*-
"""FUSION ART BATCH — power. Generated for the Byte Forensics asset library.

Power and cooling hardware in the same flat line art as fusion_art.py:
one accent per drawing, no transform attributes on any <g>, tight and
centred viewBoxes, ambient motion only where the part would really move.
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


def _blade(cx, cy, a, r0, r1, sweep=0.44, bow=11.0):
    """One curved fan blade: a quadratic from the hub out to the tip."""
    p1 = (cx + r0 * math.cos(a), cy + r0 * math.sin(a))
    p2 = (cx + r1 * math.cos(a + sweep), cy + r1 * math.sin(a + sweep))
    mx, my = (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    ln = math.hypot(dx, dy) or 1.0
    ctrl = (mx - dy / ln * bow, my + dx / ln * bow)
    return 'M%.1f %.1f Q%.1f %.1f %.1f %.1f' % (p1[0], p1[1], ctrl[0], ctrl[1], p2[0], p2[1])


def _hexfield(x0, y0, x1, y1, r=18.0):
    """A honeycomb lattice as one path, so the vent panel is a single stroke."""
    h = math.sqrt(3.0) * r
    step = 1.5 * r
    d = []
    i = 0
    while True:
        cx = x0 + r + i * step
        if cx - r > x1:
            break
        j = 0
        while True:
            cy = y0 + h / 2.0 + j * h + (h / 2.0 if i % 2 else 0.0)
            if cy - h / 2.0 > y1:
                break
            pts = []
            for k in range(6):
                ang = math.radians(60 * k)
                pts.append("%.1f %.1f" % (cx + r * math.cos(ang), cy + r * math.sin(ang)))
            d.append("M" + " L".join(pts) + " Z")
            j += 1
        i += 1
    return " ".join(d)


# ==================================================================== scene 1
_psu_seq = 0

def psu():
    """A power supply unit: fan grille over a honeycomb vent, socket and cables."""
    global _psu_seq
    _psu_seq += 1
    vent_id = "psu-vent-%d" % _psu_seq
    b = []
    # --- the case
    b.append('<rect x="54" y="54" width="420" height="200" rx="10" fill="none" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the honeycomb vent panel. The lattice is clipped so it stops dead at
    #     the panel edge instead of spilling over the case.
    b.append('<defs><clipPath id="%s"><rect x="70" y="70" width="388" '
             'height="168" rx="6"/></clipPath></defs>' % vent_id)
    b.append('<g clip-path="url(#%s)">' % vent_id)
    b.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.5"/>'
             % (_hexfield(70, 70, 458, 238), HAIR))
    b.append('</g>')
    b.append('<rect x="70" y="70" width="388" height="168" rx="6" fill="none" '
             'stroke="%s" stroke-width="1.5" opacity=".55"/>' % HAIR)
    # --- the fan, seen through the wire grille
    cx, cy = 264, 154
    b.append('<circle cx="%d" cy="%d" r="76" fill="rgba(9,12,11,.82)" stroke="%s" '
             'stroke-width="3"/>' % (cx, cy, INK))
    for k in range(5):
        b.append('<path d="%s" fill="none" stroke="%s" stroke-width="12" '
                 'stroke-linecap="round" opacity=".38"/>'
                 % (_blade(cx, cy, k * (2 * math.pi / 5), 20, 64, 0.50, 9.0), INK))
    for r in (58, 38):
        b.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" '
                 'stroke-width="1.5" opacity=".5"/>' % (cx, cy, r, INK))
    for k in range(8):
        a = k * math.pi / 4
        b.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="1.5" '
                 'opacity=".45" stroke-linecap="round"/>'
                 % (cx + 16 * math.cos(a), cy + 16 * math.sin(a),
                    cx + 74 * math.cos(a), cy + 74 * math.sin(a), INK))
    # --- the hub: the one gold thing
    b.append('<circle cx="%d" cy="%d" r="15" fill="%s"/>' % (cx, cy, GOLD))
    b.append('<circle cx="%d" cy="%d" r="5.5" fill="#0D1110"/>' % (cx, cy))
    # --- the AC inlet on the left edge
    b.append('<rect x="26" y="134" width="28" height="40" rx="5" fill="#0D1110" '
             'stroke="%s" stroke-width="3"/>' % INK)
    for px in (30, 39, 48):
        b.append('<rect x="%d" y="146" width="4" height="16" rx="1" fill="%s" '
                 'opacity=".75"/>' % (px, INK))
    # --- the cable bundle leaving the right
    for d, px, py in (("M474 102 C 512 102 528 78 566 78", 566, 68),
                       ("M474 148 C 516 148 534 150 574 150", 574, 140),
                       ("M474 194 C 508 194 522 220 556 220", 556, 210)):
        b.append('<path d="%s" fill="none" stroke="%s" stroke-width="3" '
                 'stroke-linecap="round"/>' % (d, INK))
        b.append('<rect x="%d" y="%d" width="28" height="20" rx="4" fill="#0D1110" '
                 'stroke="%s" stroke-width="3"/>' % (px, py, INK))
    # --- the label
    b.append('<text x="264" y="284" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="700" fill="%s" letter-spacing="3">POWER SUPPLY</text>'
             % GREY)
    return _svg("14 42 600 259", "".join(b), "psu")


# ==================================================================== scene 2
def heat_sink():
    """A finned heatsink: sixteen fins over a gold vapour chamber."""
    b = []
    # --- the vapour chamber, sitting behind the fins
    b.append('<rect x="62" y="118" width="423.5" height="46" rx="3" fill="%s" '
             'opacity=".92"/>' % GOLD)
    # --- sixteen fins. They are filled with the page colour so the chamber
    #     only shows in the gaps between them.
    for i in range(16):
        fx = 62 + i * 27.5
        b.append('<rect x="%.1f" y="58" width="11" height="156" rx="3" fill="#0D1110" '
                 'stroke="%s" stroke-width="3"/>' % (fx, INK))
    # --- the base plate
    b.append('<rect x="40" y="214" width="470" height="32" rx="4" fill="none" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the labels
    b.append('<text x="40" y="284" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="700" fill="%s" letter-spacing="3">HEATSINK</text>' % GREY)
    b.append('<text x="510" y="284" text-anchor="end" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="700" fill="%s" letter-spacing="3">VAPOUR CHAMBER</text>'
             % GOLD)
    return _svg("28 46 494 254", "".join(b), "heat_sink")


# ==================================================================== scene 3
def fan():
    """A single cooling fan: seven blades on a gold hub, four screw holes."""
    CX, CY = 250, 200
    b = []
    # --- the shroud
    b.append('<circle cx="%d" cy="%d" r="125" fill="rgba(246,246,244,.02)" stroke="%s" '
             'stroke-width="3"/>' % (CX, CY, INK))
    b.append('<circle cx="%d" cy="%d" r="112" fill="none" stroke="%s" stroke-width="1.5"/>'
             % (CX, CY, HAIR))
    # --- the blades and the hub, on the spin
    b.append('<g data-amb="spin" data-amb-speed="0.30" data-amb-k="0">')
    # An invisible ring keeps the group's bounding box square about the hub,
    # so the spin pivots on the hub instead of wobbling around it.
    b.append('<circle cx="%d" cy="%d" r="104" fill="none" stroke="none"/>' % (CX, CY))
    for k in range(7):
        b.append('<path d="%s" fill="none" stroke="%s" stroke-width="11" '
                 'stroke-linecap="round" opacity=".85"/>'
                 % (_blade(CX, CY, k * (2 * math.pi / 7), 20, 104), INK))
    b.append('<circle cx="%d" cy="%d" r="16" fill="%s"/>' % (CX, CY, GOLD))
    b.append('<circle cx="%d" cy="%d" r="6" fill="#0D1110"/>' % (CX, CY))
    b.append('</g>')
    # --- the mounting frame and its four corner holes
    b.append('<rect x="100" y="50" width="300" height="300" rx="8" fill="none" '
             'stroke="%s" stroke-width="2.5" opacity=".55"/>' % INK)
    for hx, hy in ((132, 82), (368, 82), (132, 318), (368, 318)):
        b.append('<circle cx="%d" cy="%d" r="10" fill="none" stroke="%s" '
                 'stroke-width="2" opacity=".7"/>' % (hx, hy, INK))
        b.append('<circle cx="%d" cy="%d" r="3.5" fill="%s" opacity=".5"/>' % (hx, hy, INK))
    return _svg("88 38 324 324", "".join(b), "fan")


# ==================================================================== scene 4
def cooler():
    """A tower air cooler: gold heatpipes up an angled fin stack, fan clipped on."""
    b = []
    pipes = (146, 186, 226, 266)
    x0, x1 = 120, 300          # the stack runs from the left edge to the fan
    rise = 14                  # the plates are angled, so each one steps up
    # --- thirteen angled fin plates. Each line is cut where a pipe comes
    #     through it, so the pipe is never crossed by a plate.
    for i in range(13):
        y0 = 86 + i * 12
        segs = [(x0, x1)]
        for px in pipes:
            lo, hi = px - 11, px + 11
            cut = []
            for a, c in segs:
                if hi <= a or lo >= c:
                    cut.append((a, c))
                else:
                    if a < lo:
                        cut.append((a, lo))
                    if hi < c:
                        cut.append((hi, c))
            segs = cut
        for a, c in segs:
            ya = y0 - rise * (a - x0) / float(x1 - x0)
            yc = y0 - rise * (c - x0) / float(x1 - x0)
            b.append('<path d="M%d %.1f L%d %.1f" stroke="%s" stroke-width="1.5" '
                     'stroke-linecap="round" opacity=".62"/>' % (a, ya, c, yc, INK))
    # --- the edges of the stack
    b.append('<path d="M120 86 L300 72 M120 230 L300 216" stroke="%s" stroke-width="2.5" '
             'stroke-linecap="round"/>' % INK)
    b.append('<path d="M120 86 L120 230 M300 72 L300 216" stroke="%s" stroke-width="2.5" '
             'stroke-linecap="round"/>' % INK)
    # --- four heatpipes rising out of the base. They are drawn over the stack
    #     so no plate edge crosses a pipe.
    for px in pipes:
        b.append('<path d="M%d 258 L%d 64" fill="none" stroke="%s" stroke-width="10" '
                 'stroke-linecap="round"/>' % (px, px, GOLD))
    # --- the base plate. It is opaque, so the pipes stop at its top edge.
    b.append('<rect x="104" y="248" width="216" height="34" rx="4" fill="#0D1110" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the fan, clipped to the front of the tower
    b.append('<rect x="284" y="92" width="140" height="140" rx="6" fill="#0D1110" '
             'stroke="%s" stroke-width="2.5"/>' % INK)
    for k in range(5):
        b.append('<path d="%s" fill="none" stroke="%s" stroke-width="10" '
                 'stroke-linecap="round" opacity=".50"/>'
                 % (_blade(354, 162, k * (2 * math.pi / 5), 16, 50, 0.50, 8.0), INK))
    b.append('<circle cx="354" cy="162" r="56" fill="none" stroke="%s" stroke-width="2"/>' % INK)
    b.append('<circle cx="354" cy="162" r="13" fill="#0D1110" stroke="%s" stroke-width="2"/>' % INK)
    # --- the two clips that grip the tower
    for y in (110, 204):
        b.append('<rect x="278" y="%d" width="42" height="13" rx="4" fill="#0D1110" '
                 'stroke="%s" stroke-width="2"/>' % (y, INK))
    # --- the callout on the pipes
    b.append('<path d="M270 62 L298 52" stroke="%s" stroke-width="1.5" '
             'stroke-linecap="round"/>' % FAINT)
    b.append('<text x="306" y="56" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="2">HEATPIPES</text>' % GOLD)
    b.append('<text x="264" y="312" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="700" fill="%s" letter-spacing="3">TOWER COOLER</text>'
             % GREY)
    return _svg("92 35 344 293", "".join(b), "cooler")


# ==================================================================== scene 5
def power_rails():
    """A power delivery diagram: one input bar splitting into three rails."""
    b = []
    # --- the input
    b.append('<rect x="60" y="52" width="26" height="208" rx="4" fill="%s"/>' % RED)
    b.append('<text x="73" y="40" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">INPUT</text>' % RED)
    # --- the three rails. The thick one is the one that matters, so it is gold.
    b.append('<rect x="86" y="84" width="294" height="16" rx="8" fill="%s"/>' % GOLD)
    b.append('<rect x="86" y="147" width="294" height="10" rx="5" fill="%s" opacity=".85"/>' % INK)
    b.append('<rect x="86" y="209" width="294" height="6" rx="3" fill="%s" opacity=".55"/>' % INK)
    # --- the loads at the end of each rail
    b.append('<rect x="380" y="76" width="32" height="32" rx="3" fill="none" '
             'stroke="%s" stroke-width="2.5"/>' % GOLD)
    b.append('<rect x="380" y="136" width="32" height="32" rx="3" fill="none" '
             'stroke="%s" stroke-width="2"/>' % INK)
    b.append('<rect x="380" y="196" width="32" height="32" rx="3" fill="none" '
             'stroke="%s" stroke-width="2"/>' % INK)
    # --- the load names
    b.append('<text x="424" y="97" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="700" fill="%s" letter-spacing="2">GPU</text>' % GOLD)
    b.append('<text x="424" y="157" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="700" fill="%s" letter-spacing="2">CPU</text>' % INK)
    b.append('<text x="424" y="217" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="700" fill="%s" letter-spacing="2">SSD</text>' % GREY)
    return _svg("37 18 435 222", "".join(b), "power_rails")
