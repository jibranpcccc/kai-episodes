# -*- coding: utf-8 -*-
"""
FUSION ART — the reusable drawing library for Byte Forensics.

Flat line art on near-black, the way KAI and RepoChad draw hardware.
No photography, no gradients, one accent colour per drawing.

These are the REUSABLE assets: every episode pulls from this file, so each
drawing has to hold up at 1x and at thumbnail size.

RULES FOR THIS FILE
  * a <g> NEVER carries a transform attribute. Animating style.transform on
    an element that HAS one collapses it to the top-left (HANDOFF.md, bugs
    paid for). The motion groups below are clean on purpose.
  * every moving part is wrapped in <g data-amb="...">:
        spin   rotate  - data-amb-speed, and data-amb-box=view-box +
                       data-amb-origin for parts that pivot off their own bbox
        pulse  opacity - data-amb-k sets the phase, so a row of them breathes
                       in sequence
        blink  opacity - a cursor waiting
  * nothing overlaps anything else. Labels get their own clear space.
  * every drawing is centred in its viewBox.
"""

import os

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
def laptop_wait():
    """Laptop with a long document on screen, a caret waiting, and the clock."""
    b = []
    # --- lid
    b.append('<rect x="70" y="18" width="340" height="218" rx="14" fill="none" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="88" y="36" width="304" height="182" rx="5" fill="rgba(56,217,232,.05)" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    # --- the pasted document. The last line is short and the caret sits at its
    #     end, so the read is "the model is still chewing on this".
    lines = [(252, .50), (274, .44), (260, .46), (280, .38),
             (244, .34), (268, .26), (146, .22)]
    for i, (w, o) in enumerate(lines):
        b.append('<rect x="104" y="%d" width="%d" height="6" rx="3" fill="%s" opacity="%.2f"/>'
                 % (56 + i * 22, w, INK, o))
    # --- the caret, blinking forever, at the end of the last line
    b.append('<g data-amb="blink">'
             '<rect x="258" y="180" width="11" height="22" rx="1" fill="%s"/></g>' % GOLD)
    # --- base: same width as the lid at the hinge, tapering to the front edge
    b.append('<path d="M70 236 L410 236 L404 264 L76 264 Z" fill="none" stroke="%s" '
             'stroke-width="3" stroke-linejoin="round"/>' % INK)
    b.append('<rect x="196" y="243" width="88" height="8" rx="4" fill="%s" opacity=".45"/>' % INK)
    # --- the clock
    b.append('<rect x="120" y="300" width="240" height="86" rx="10" fill="rgba(245,197,49,.10)" '
             'stroke="%s" stroke-width="2"/>' % GOLD)
    b.append('<text x="240" y="366" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="58" font-weight="800" fill="%s" letter-spacing="3">00:20</text>' % GOLD)
    b.append('<text x="240" y="432" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="17" font-weight="700" fill="%s" letter-spacing="4">'
             'TIME TO FIRST TOKEN</text>' % GREY)
    return _svg("58 6 364 442", "".join(b), "laptop")


# ==================================================================== scene 2
def gpu_card():
    """A GPU in flat line art. Two fans that keep turning, a real PCIe edge."""
    import math
    b = []
    # --- shroud
    b.append('<rect x="26" y="26" width="428" height="228" rx="12" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="44" y="44" width="392" height="176" rx="8" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    for idx, cx in enumerate((140, 340)):
        b.append('<circle cx="%d" cy="130" r="64" fill="rgba(0,0,0,.30)"/>' % cx)
        b.append('<circle cx="%d" cy="130" r="64" fill="none" stroke="%s" stroke-width="3"/>'
                 % (cx, INK))
        b.append('<g data-amb="spin" data-amb-speed="0.26" data-amb-k="%d">' % (idx * 3))
        # seven broad blades
        for k in range(7):
            a = k * (2 * math.pi / 7)
            p1 = (cx + 17 * math.cos(a), 130 + 17 * math.sin(a))
            p2 = (cx + 54 * math.cos(a + 0.44), 130 + 54 * math.sin(a + 0.44))
            mx, my = (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            ln = math.hypot(dx, dy) or 1.0
            ctrl = (mx - dy / ln * 11, my + dx / ln * 11)
            b.append('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f" fill="none" stroke="%s" '
                     'stroke-width="9" stroke-linecap="round" opacity=".85"/>'
                     % (p1[0], p1[1], ctrl[0], ctrl[1], p2[0], p2[1], INK))
        b.append('<circle cx="%d" cy="130" r="11" fill="%s"/>' % (cx, GOLD))
        b.append('<circle cx="%d" cy="130" r="4" fill="#0D1110"/>' % cx)
        b.append('</g>')
    # --- PCIe edge: one solid bar with two full-height key notches
    b.append('<rect x="100" y="254" width="280" height="18" rx="2" fill="%s" opacity=".9"/>' % GOLD)
    b.append('<rect x="196" y="254" width="22" height="18" fill="#0D1110"/>')
    b.append('<rect x="292" y="254" width="22" height="18" fill="#0D1110"/>')
    return _svg("14 14 452 270", "".join(b), "gpu")


# ==================================================================== scene 3
def collapse_curve():
    """Prefill collapsing as context grows. Legend, axes and labels, no
    collisions."""
    pts = [(74, 62), (214, 96), (350, 176), (462, 238)]
    labs = ["4K", "16K", "64K", "128K"]
    b = []
    # --- legend, two rows in the clear space top right
    b.append('<path d="M252 20 L286 20" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % RED)
    b.append('<text x="296" y="26" font-family="FuseMono, monospace" font-size="16" '
             'font-weight="800" fill="%s" letter-spacing="2">PREFILL</text>' % RED)
    b.append('<path d="M252 42 L286 42" stroke="%s" stroke-width="3" stroke-dasharray="7 6" '
             'stroke-linecap="round"/>' % CYAN)
    b.append('<text x="296" y="48" font-family="FuseMono, monospace" font-size="16" '
             'font-weight="800" fill="%s" letter-spacing="2">GENERATION</text>' % CYAN)
    # --- axes
    b.append('<path d="M58 56 L58 252 L468 252" fill="none" stroke="%s" stroke-width="2" '
             'opacity=".45"/>' % INK)
    b.append('<text x="58" y="46" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="2">TOKENS/S</text>' % FAINT)
    # --- generation, the graceful one
    b.append('<path d="M58 50 L214 66 L350 106 L462 152" fill="none" stroke="%s" stroke-width="3" '
             'stroke-dasharray="7 7" stroke-linecap="round" opacity=".8"/>' % CYAN)
    # --- prefill, the one that collapses
    d = "M" + " L".join("%.1f %.1f" % (x, y) for x, y in pts)
    b.append('<path d="%s" fill="none" stroke="%s" stroke-width="4.5" stroke-linecap="round" '
             'stroke-linejoin="round"/>' % (d, RED))
    for i, (x, y) in enumerate(pts):
        b.append('<g data-amb="pulse" data-amb-k="%d" data-amb-speed="1.25">' % i)
        # data-draw-delay: the dot appears exactly as the line reaches it
        b.append('<circle cx="%d" cy="%d" r="9" fill="%s" data-draw-delay="%s"/>'
                 % (x, y, RED, ["0.0", "0.30", "0.66", "1.02"][i]))
        b.append('</g>')
        b.append('<text x="%d" y="276" text-anchor="middle" font-family="FuseMono, monospace" '
                 'font-size="17" font-weight="700" fill="%s" letter-spacing="2">%s</text>'
                 % (x, INK, labs[i]))
    b.append('<text x="58" y="302" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="2">CONTEXT</text>' % FAINT)
    return _svg("48 8 462 308", "".join(b), "collapse")


# ==================================================================== scene 4
def stopwatch():
    """A wait timer. The hand sweeps; the arc shows how much is already gone."""
    import math
    CX, CY = 150, 166          # the dial sits low, so the viewBox has no dead band
    b = []
    # --- crown: a button on a short stem, touching the dial
    b.append('<rect x="134" y="42" width="32" height="24" rx="3" fill="none" stroke="%s" '
             'stroke-width="3"/>' % INK)
    b.append('<rect x="112" y="22" width="76" height="24" rx="8" fill="none" stroke="%s" '
             'stroke-width="3"/>' % INK)
    # --- dial
    b.append('<circle cx="%d" cy="%d" r="104" fill="none" stroke="%s" stroke-width="3"/>'
             % (CX, CY, INK))
    b.append('<circle cx="%d" cy="%d" r="86" fill="none" stroke="%s" stroke-width="1.5" '
             'opacity=".40"/>' % (CX, CY, INK))
    # --- elapsed arc: 42% of the dial, starting at 12 o'clock, clockwise
    a0 = -90.0
    a1 = a0 + 0.42 * 360.0
    x1 = CX + 86 * math.cos(math.radians(a1))
    y1 = CY + 86 * math.sin(math.radians(a1))
    b.append('<path d="M%d %d A86 86 0 0 1 %.1f %.1f" fill="none" stroke="%s" '
             'stroke-width="11" stroke-linecap="round" opacity=".92"/>' % (CX, CY - 86, x1, y1, RED))
    b.append('<path d="M%d %d L%d %d" stroke="%s" stroke-width="4" stroke-linecap="round" '
             'opacity=".85"/>' % (CX, CY, CX, CY - 86, RED))
    b.append('<circle cx="%d" cy="%d" r="8" fill="%s"/>' % (CX, CY, INK))
    # --- the hand, sweeping. The sweep is BOUNDED: a clock hand that turns
    # all the way round reads as a spinning toy, not a dial reading a value.
    b.append('<g data-amb="sway" data-amb-box="view-box" data-amb-origin="150px 166px" '
             'data-amb-amp="14" data-amb-speed="0.5" data-amb-k="0">')
    b.append('<path d="M%d %d L198 192" stroke="%s" stroke-width="4.5" stroke-linecap="round"/>'
             % (CX, CY, GOLD))
    b.append('</g>')
    # --- the prompt, filling up
    b.append('<text x="286" y="92" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="800" fill="%s" letter-spacing="2">PROMPT</text>' % GREY)
    for i, (w, o) in enumerate([(184, .55), (184, .34), (184, .20)]):
        b.append('<rect x="286" y="%d" width="%d" height="16" rx="4" fill="%s" opacity="%.2f"/>'
                 % (108 + i * 30, w, INK, o))
    b.append('<text x="286" y="230" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="800" fill="%s" letter-spacing="2">STILL LOADING</text>' % FAINT)
    return _svg("36 12 444 268", "".join(b), "clock")


# ==================================================================== scene 5
def bandwidth_meter():
    """Memory bus. The peak marker has to be unmissable."""
    b = []
    b.append('<text x="34" y="40" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="800" fill="%s" letter-spacing="3">BANDWIDTH</text>' % GREY)
    # --- the bus
    b.append('<rect x="34" y="132" width="412" height="40" rx="7" fill="rgba(56,217,232,.05)" '
             'stroke="%s" stroke-width="2"/>' % CYAN)
    for i in range(13):
        b.append('<rect x="%d" y="138" width="18" height="28" rx="2" fill="%s" opacity="%s"/>'
                 % (46 + i * 30, CYAN, ".85" if i < 6 else ".16"))
    # --- the peak, unmistakable
    b.append('<g data-amb="pulse" data-amb-k="0" data-amb-speed="1.6">')
    b.append('<path d="M196 104 L196 200" stroke="%s" stroke-width="4" stroke-dasharray="8 7" '
             'stroke-linecap="round"/>' % GOLD)
    b.append('<path d="M186 116 L196 104 L206 116" fill="none" stroke="%s" stroke-width="4" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % GOLD)
    b.append('</g>')
    b.append('<g data-amb="pulse" data-amb-k="1" data-amb-speed="1.6">')
    b.append('<text x="196" y="92" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="800" fill="%s" letter-spacing="2">THE LIMIT</text>' % GOLD)
    b.append('</g>')
    # --- read direction
    b.append('<path d="M34 236 L446 236 M432 228 L446 236 L432 244" fill="none" stroke="%s" '
             'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" opacity=".55"/>' % INK)
    b.append('<text x="34" y="262" font-family="FuseMono, monospace" font-size="14" '
             'font-weight="700" fill="%s" letter-spacing="2">READ EVERY WEIGHT</text>' % GREY)
    b.append('<text x="446" y="262" text-anchor="end" font-family="FuseMono, monospace" '
             'font-size="14" font-weight="700" fill="%s" letter-spacing="2">ONE PASS</text>' % INK)
    return _svg("24 20 432 252", "".join(b), "meter")


# ==================================================================== scene 6
def caveat_mark():
    """A document under a magnifying glass. Look before you buy.

    The document outline is drawn as two subpaths so the right edge is OMITTED
    where the lens covers it. A closed rect would show its edge through the
    glass and read as a mistake."""
    b = []
    # --- the document: outline, with the lens-hidden section of the right
    #     edge left out (glass spans y 145..259 at x 306)
    b.append('<path d="M96 34 Q96 24 106 24 H296 Q306 24 306 34 V145 '
             'M306 259 V278 Q306 288 296 288 H106 Q96 288 96 278 V34" fill="none" '
             'stroke="%s" stroke-width="3" stroke-linecap="round"/>' % INK)
    b.append('<rect x="118" y="48" width="96" height="9" rx="4" fill="%s" opacity=".62"/>' % INK)
    for i, w in enumerate([162, 166, 148, 166, 120]):
        b.append('<rect x="118" y="%d" width="%d" height="7" rx="3" fill="%s" opacity=".32"/>'
                 % (80 + i * 26, w, INK))
    # --- the glass, in front
    b.append('<circle cx="296" cy="202" r="58" fill="rgba(13,17,16,.98)" stroke="%s" '
             'stroke-width="4"/>' % GOLD)
    b.append('<path d="M336 242 L380 286" stroke="%s" stroke-width="9" stroke-linecap="round"/>' % GOLD)
    b.append('<path d="M272 202 L290 222 L324 180" fill="none" stroke="%s" stroke-width="7" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % GOLD)
    return _svg("86 14 304 284", "".join(b), "caveat")


ART = {
    "laptop":  laptop_wait,
    "gpu":     gpu_card,
    "collapse": collapse_curve,
    "clock":   stopwatch,
    "meter":   bandwidth_meter,
    "caveat":  caveat_mark,
}


# ==================================================================== LIBRARY
# Every drawing in a fusion_art_batch_*.py is merged into ART here, so the
# whole library is available as one dict and every episode pulls from one
# place. The batch files stay separate so they can be edited independently.
def _load_batches():
    import glob
    import importlib
    here = os.path.dirname(os.path.abspath(__file__))
    for path in sorted(glob.glob(os.path.join(here, "fusion_art_batch_*.py"))):
        mod = os.path.splitext(os.path.basename(path))[0]
        try:
            m = importlib.import_module(mod)
        except Exception as e:
            print("FUSION ART: batch %s failed to import: %s" % (mod, e))
            continue
        for name in dir(m):
            if name.startswith("_") or not name.islower():
                continue
            fn = getattr(m, name)
            if callable(fn) and name not in ART:
                ART[name] = fn
    return ART


_load_batches()
