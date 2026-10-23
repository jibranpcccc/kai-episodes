# -*- coding: utf-8 -*-
"""FUSION ART BATCH — meters. Generated for the Byte Forensics asset library.

Flat line art on near-black, one accent per drawing. Same grammar as
fusion_art.py: no <g> carries a transform attribute, every moving part sits in
a <g data-amb="...">, and every viewBox is tight around the real content.
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


def gauge():
    """A semicircular speedometer. The needle sweeps, the top right is danger."""
    CX, CY = 170, 190
    R_OUT, R_IN = 128, 88
    b = []

    def pt(r, deg):
        a = math.radians(deg)
        return CX + r * math.cos(a), CY + r * math.sin(a)

    # --- the rim
    b.append('<path d="M%d %d A%d %d 0 0 1 %d %d" fill="none" stroke="%s" '
             'stroke-width="3" stroke-linecap="round"/>'
             % (CX - R_OUT, CY, R_OUT, R_OUT, CX + R_OUT, CY, INK))
    # --- the inner arc
    b.append('<path d="M%d %d A%d %d 0 0 1 %d %d" fill="none" stroke="%s" '
             'stroke-width="1.5" stroke-linecap="round" opacity=".40"/>'
             % (CX - R_IN, CY, R_IN, R_IN, CX + R_IN, CY, INK))
    # --- the flat bottom of the dial
    b.append('<path d="M%d %d L%d %d" fill="none" stroke="%s" stroke-width="1.5" '
             'stroke-linecap="round" opacity=".30"/>'
             % (CX - R_OUT, CY, CX + R_OUT, CY, INK))
    # --- nine ticks, each one longer than the last
    for i in range(9):
        a = 200 + 17.5 * i
        x0, y0 = pt(94, a)
        x1, y1 = pt(104 + 2 * i, a)
        b.append('<path d="M%.1f %.1f L%.1f %.1f" fill="none" stroke="%s" '
                 'stroke-width="3" stroke-linecap="round"/>' % (x0, y0, x1, y1, INK))
    # --- the danger zone, laid over the last three ticks
    zx0, zy0 = pt(114, 305)
    zx1, zy1 = pt(114, 340)
    b.append('<path d="M%.1f %.1f A114 114 0 0 1 %.1f %.1f" fill="none" stroke="%s" '
             'stroke-width="8" stroke-linecap="round" opacity=".92"/>'
             % (zx0, zy0, zx1, zy1, RED))
    # --- the needle, sweeping. It pivots on the dial centre, not on its own box.
    # The sweep is BOUNDED: the dial only spans 200..340 degrees, so a full
    # 360 spin would carry the needle under the arc and off the drawing.
    b.append('<g data-amb="sway" data-amb-box="view-box" data-amb-origin="%dpx %dpx" '
             'data-amb-amp="24" data-amb-speed="0.45" data-amb-k="0">' % (CX, CY))
    nx, ny = pt(100, 297)
    b.append('<path d="M%d %d L%.1f %.1f" fill="none" stroke="%s" stroke-width="5" '
             'stroke-linecap="round"/>' % (CX, CY, nx, ny, GOLD))
    b.append('</g>')
    # --- the hub
    b.append('<circle cx="%d" cy="%d" r="11" fill="%s"/>' % (CX, CY, GOLD))
    b.append('<circle cx="%d" cy="%d" r="4.5" fill="%s"/>' % (CX, CY, BG))
    # --- the label
    b.append('<text x="%d" y="234" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="700" fill="%s" letter-spacing="4">LOAD</text>'
             % (CX, GREY))
    return _svg("28 48 284 202", "".join(b), "gauge")


def tok_speed_dial():
    """A 270 degree dial reading tokens per second. The gap at the bottom holds
    the unit, the badge in the middle holds the live number."""
    CX, CY = 170, 170
    R = 118
    b = []

    def pt(r, deg):
        a = math.radians(deg)
        return CX + r * math.cos(a), CY + r * math.sin(a)

    # --- the track: 270 degrees, open at the bottom
    x0, y0 = pt(R, 135)
    x1, y1 = pt(R, 405)
    b.append('<path d="M%.1f %.1f A%d %d 0 1 1 %.1f %.1f" fill="none" stroke="%s" '
             'stroke-width="3" stroke-linecap="round"/>' % (x0, y0, R, R, x1, y1, INK))
    # --- the inner arc
    x0, y0 = pt(86, 135)
    x1, y1 = pt(86, 405)
    b.append('<path d="M%.1f %.1f A86 86 0 1 1 %.1f %.1f" fill="none" stroke="%s" '
             'stroke-width="1.5" stroke-linecap="round" opacity=".40"/>'
             % (x0, y0, x1, y1, INK))
    # --- eleven ticks across the sweep
    for i in range(11):
        a = 135 + 27.0 * i
        tx0, ty0 = pt(94, a)
        tx1, ty1 = pt(110, a)
        b.append('<path d="M%.1f %.1f L%.1f %.1f" fill="none" stroke="%s" '
                 'stroke-width="3" stroke-linecap="round"/>' % (tx0, ty0, tx1, ty1, INK))
    # --- the needle, sweeping about the dial centre. The sweep is BOUNDED:
    # the dial only spans 135..405 degrees, so a full 360 spin would carry the
    # needle out of the arc and off the drawing.
    b.append('<g data-amb="sway" data-amb-box="view-box" data-amb-origin="%dpx %dpx" '
             'data-amb-amp="30" data-amb-speed="0.45" data-amb-k="0">' % (CX, CY))
    nx, ny = pt(104, 315)
    b.append('<path d="M%d %d L%.1f %.1f" fill="none" stroke="%s" stroke-width="5" '
             'stroke-linecap="round"/>' % (CX, CY, nx, ny, GOLD))
    b.append('</g>')
    # --- the number badge, sitting over the pivot
    b.append('<circle cx="%d" cy="%d" r="32" fill="%s" stroke="%s" stroke-width="2.5"/>'
             % (CX, CY, BG, GOLD))
    b.append('<text x="%d" y="%d" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="22" font-weight="800" fill="%s" letter-spacing="1">142</text>'
             % (CX, CY + 8, GOLD))
    # --- the unit, in the gap
    b.append('<text x="%d" y="236" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="700" fill="%s" letter-spacing="3">TOKENS/S</text>'
             % (CX, GREY))
    return _svg("38 38 264 229", "".join(b), "tok_speed_dial")


def cost_dial():
    """A cost dial. One quarter of the spend, in gold. The rest is quiet."""
    CX, CY, R = 160, 150, 100
    b = []
    up = (CX, CY - R)
    right = (CX + R, CY)
    down = (CX, CY + R)
    left = (CX - R, CY)
    # --- the three quiet quarters
    for a, c in ((right, down), (down, left), (left, up)):
        b.append('<path d="M%d %d L%d %d A%d %d 0 0 1 %d %d Z" fill="%s" opacity=".14"/>'
                 % (CX, CY, a[0], a[1], R, R, c[0], c[1], RED))
    # --- the quarter that is paid for
    b.append('<path d="M%d %d L%d %d A%d %d 0 0 1 %d %d Z" fill="%s"/>'
             % (CX, CY, up[0], up[1], R, R, right[0], right[1], GOLD))
    # --- the ring and the cross
    b.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="3"/>'
             % (CX, CY, R, INK))
    b.append('<path d="M%d %d L%d %d M%d %d L%d %d" fill="none" stroke="%s" '
             'stroke-width="2" stroke-linecap="round" opacity=".40"/>'
             % (up[0], up[1], down[0], down[1], left[0], left[1], right[0], right[1], INK))
    # --- the currency mark, on a hub that hides the cross
    b.append('<circle cx="%d" cy="%d" r="22" fill="%s" stroke="%s" stroke-width="2"/>'
             % (CX, CY, BG, INK))
    b.append('<text x="%d" y="%d" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="21" font-weight="800" fill="%s" letter-spacing="1">$</text>'
             % (CX, CY + 7, GOLD))
    # --- the label under the dial
    b.append('<text x="%d" y="292" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="700" fill="%s" letter-spacing="3">COST PER HOUR</text>'
             % (CX, GREY))
    return _svg("46 36 228 272", "".join(b), "cost_dial")


def timer_flat():
    """A flat timer bar, filling from the left, with a flag at the fill edge."""
    X0, X1, Y0, Y1 = 40, 440, 124, 180
    EDGE = 201                     # 40 per cent of the inner span
    b = []
    # --- the bar
    b.append('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="rgba(246,246,244,.04)" '
             'stroke="%s" stroke-width="3"/>' % (X0, Y0, X1 - X0, Y1 - Y0, INK))
    # --- the fill
    b.append('<rect x="%d" y="%d" width="%d" height="%d" rx="4" fill="%s"/>'
             % (46, 128, EDGE - 46, 48, GOLD))
    # --- ticks along the top
    for i in range(10):
        tx = 52 + 42 * i
        b.append('<path d="M%d 106 L%d 116" fill="none" stroke="%s" stroke-width="2" '
                 'stroke-linecap="round"/>' % (tx, tx, FAINT))
    # --- the flag, planted at the fill edge
    b.append('<g data-amb="pulse" data-amb-k="0" data-amb-speed="1.4">')
    b.append('<path d="M%d %d L%d 86" fill="none" stroke="%s" stroke-width="3" '
             'stroke-linecap="round"/>' % (EDGE, Y0, EDGE, GOLD))
    b.append('<path d="M%d 86 L%d 96 L%d 106 Z" fill="%s"/>' % (EDGE, EDGE + 28, EDGE, GOLD))
    b.append('</g>')
    # --- the captions
    b.append('<text x="%d" y="208" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="3">ELAPSED</text>' % (X0, FAINT))
    b.append('<text x="%d" y="208" text-anchor="end" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="800" fill="%s" letter-spacing="2">00:20</text>'
             % (X1, INK))
    return _svg("26 72 428 152", "".join(b), "timer_flat")
