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
    # --- active inference status box (replaces old TTFT)
    b.append('<rect x="110" y="300" width="260" height="86" rx="10" fill="rgba(56,217,232,.10)" '
             'stroke="%s" stroke-width="2"/>' % CYAN)
    b.append('<text x="240" y="342" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="20" font-weight="800" fill="%s" letter-spacing="2">SUSTAINED LOAD</text>' % CYAN)
    b.append('<text x="240" y="368" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="12" font-weight="700" fill="%s" letter-spacing="2">'
             'RUNTIME MEMORY ALLOCATION</text>' % GREY)
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




def gpu_tier(cap="8 GB", col=GOLD):
    """A GPU board with prominent tier capacity badge."""
    import math
    b = []
    b.append('<rect x="26" y="26" width="428" height="228" rx="12" fill="rgba(246,246,244,.02)" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="44" y="44" width="392" height="176" rx="8" fill="none" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    for idx, cx in enumerate((120, 360)):
        b.append('<circle cx="%d" cy="132" r="58" fill="rgba(0,0,0,.35)"/>' % cx)
        b.append('<circle cx="%d" cy="132" r="58" fill="none" stroke="%s" stroke-width="2.5"/>'
                 % (cx, INK))
        b.append('<g data-amb="spin" data-amb-speed="0.26" data-amb-k="%d">' % (idx * 3))
        for k in range(7):
            a = k * (2 * math.pi / 7)
            p1 = (cx + 15 * math.cos(a), 132 + 15 * math.sin(a))
            p2 = (cx + 48 * math.cos(a + 0.44), 132 + 48 * math.sin(a + 0.44))
            mx, my = (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            ln = math.hypot(dx, dy) or 1.0
            ctrl = (mx - dy / ln * 9, my + dx / ln * 9)
            b.append('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f" fill="none" stroke="%s" '
                     'stroke-width="8" stroke-linecap="round" opacity=".85"/>'
                     % (p1[0], p1[1], ctrl[0], ctrl[1], p2[0], p2[1], INK))
        b.append('<circle cx="%d" cy="132" r="10" fill="%s"/>' % (cx, col))
        b.append('<circle cx="%d" cy="132" r="4" fill="#0D1110"/>' % cx)
        b.append('</g>')
    # Center capacity badge (prominent, mobile-first legible)
    b.append('<rect x="195" y="104" width="90" height="56" rx="8" fill="rgba(13,17,16,.94)" '
             'stroke="%s" stroke-width="2.5"/>' % col)
    b.append('<text x="240" y="142" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="26" font-weight="900" fill="%s" letter-spacing="1">%s</text>' % (col, cap))
    # PCIe connector
    b.append('<rect x="100" y="254" width="280" height="18" rx="2" fill="%s" opacity=".9"/>' % col)
    b.append('<rect x="196" y="254" width="22" height="18" fill="#0D1110"/>')
    b.append('<rect x="292" y="254" width="22" height="18" fill="#0D1110"/>')
    return _svg("14 14 452 270", "".join(b), "gpu_" + cap.replace(" ", "").lower())


def gpu_8gb(): return gpu_tier("8GB", CYAN)
def gpu_12gb(): return gpu_tier("12GB", GOLD)
def gpu_16gb(): return gpu_tier("16GB", CYAN)
def gpu_24gb(): return gpu_tier("24GB", GOLD)


def vram_stack():
    """Diagram illustrating why passive file size differs from sustained runtime VRAM."""
    b = []
    # ViewBox: 0 0 460 496
    GREEN = "#00F59B"
    
    # =========================================================================
    # 1. TOP: NVMe PASSIVE DISK STORAGE (M.2 2280 FORM FACTOR)
    # =========================================================================
    # Outer NVMe PCB Card
    b.append('<rect x="20" y="12" width="420" height="96" rx="10" fill="rgba(18, 24, 38, 0.96)" '
             'stroke="%s" stroke-width="1.8"/>' % HAIR)
    
    # Gold M.2 contact pins
    for i in range(5):
        b.append('<rect x="%d" y="12" width="5" height="10" rx="1" fill="%s" opacity="0.85"/>' % (34 + i * 8, GOLD))
    b.append('<rect x="76" y="12" width="8" height="14" fill="rgba(18, 24, 38, 0.96)"/>') # M.2 key notch
    for i in range(4):
        b.append('<rect x="%d" y="12" width="5" height="10" rx="1" fill="%s" opacity="0.85"/>' % (86 + i * 8, GOLD))

    # Header row with generous 50px+ gap between label and badge
    b.append('<text x="130" y="27" font-family="FuseMono, monospace" font-size="9.5" font-weight="700" '
             'fill="%s" letter-spacing="1.2">NVME SSD · PASSIVE STORAGE</text>' % GREY)
    b.append('<rect x="338" y="17" width="88" height="18" rx="9" fill="rgba(56,217,232,0.12)" stroke="%s" stroke-width="1"/>' % CYAN)
    b.append('<text x="382" y="29" text-anchor="middle" font-family="FuseMono, monospace" font-size="8.5" font-weight="800" '
             'fill="%s" letter-spacing="0.5">0%% GPU VRAM</text>' % CYAN)

    # Weights file container inside NVMe
    b.append('<rect x="34" y="42" width="392" height="52" rx="6" fill="rgba(56,217,232,0.08)" '
             'stroke="%s" stroke-width="1.5"/>' % CYAN)
    # File icon / NAND flash indicator
    b.append('<rect x="46" y="50" width="34" height="36" rx="4" fill="rgba(56,217,232,0.18)" stroke="%s" stroke-width="1"/>' % CYAN)
    b.append('<text x="63" y="73" text-anchor="middle" font-family="FuseMono, monospace" font-size="11" font-weight="800" fill="%s">SSD</text>' % CYAN)
    
    # Title & Quant detail
    b.append('<text x="90" y="62" font-family="FuseMono, monospace" font-size="12" font-weight="800" fill="%s">PUBLISHED WEIGHTS FILE</text>' % CYAN)
    b.append('<text x="90" y="80" font-family="FuseMono, monospace" font-size="9.5" font-weight="600" fill="%s">Qwen3.8-27B · Unsloth UD-IQ1_S</text>' % INK)
    
    # 6.19 GB Badge
    b.append('<rect x="328" y="50" width="86" height="36" rx="6" fill="rgba(56,217,232,0.22)" stroke="%s" stroke-width="1.2"/>' % CYAN)
    b.append('<text x="371" y="73" text-anchor="middle" font-family="FuseMono, monospace" font-size="14" font-weight="800" fill="%s">6.19 GB</text>' % CYAN)

    # =========================================================================
    # 2. DATA TRANSFER BUS
    # =========================================================================
    b.append('<path d="M230 108 L230 132" stroke="%s" stroke-width="1.8" stroke-dasharray="4 3"/>' % GOLD)
    b.append('<polygon points="225,130 230,139 235,130" fill="%s"/>' % GOLD)
    b.append('<rect x="140" y="112" width="180" height="20" rx="10" fill="#0B0D13" stroke="%s" stroke-width="1.2"/>' % GOLD)
    b.append('<text x="230" y="126" text-anchor="middle" font-family="FuseMono, monospace" font-size="9" font-weight="800" '
             'fill="%s" letter-spacing="1">HOST-TO-DEVICE VRAM LOAD</text>' % GOLD)

    # =========================================================================
    # 3. GPU ACTIVE VRAM EXECUTION CONTAINER
    # =========================================================================
    b.append('<rect x="20" y="142" width="420" height="240" rx="10" fill="rgba(18, 24, 38, 0.96)" '
             'stroke="%s" stroke-width="2"/>' % GOLD)
    
    # Header Row
    b.append('<text x="36" y="168" font-family="FuseMono, monospace" font-size="11" font-weight="800" '
             'fill="%s" letter-spacing="1.5">GPU RUNTIME MEMORY ALLOCATION</text>' % GOLD)
    b.append('<rect x="308" y="155" width="118" height="20" rx="4" fill="rgba(245,197,49,0.15)" stroke="%s" stroke-width="1"/>' % GOLD)
    b.append('<text x="367" y="169" text-anchor="middle" font-family="FuseMono, monospace" font-size="9.5" font-weight="800" '
             'fill="%s" letter-spacing="0.5">8.0 GB VRAM CARD</text>' % GOLD)

    # --- Scenario A: Single Initial Prompt
    b.append('<text x="36" y="194" font-family="FuseMono, monospace" font-size="9.5" font-weight="700" '
             'fill="%s" letter-spacing="1">SCENARIO A: SHORT INITIAL PROMPT</text>' % GREY)
    
    # Bar Container A (width 388)
    b.append('<rect x="36" y="202" width="388" height="34" rx="5" fill="rgba(246,246,244,0.03)" stroke="%s" stroke-width="1"/>' % HAIR)
    # Weights block (270px)
    b.append('<rect x="38" y="204" width="270" height="30" rx="4" fill="rgba(56,217,232,0.22)" stroke="%s" stroke-width="1"/>' % CYAN)
    b.append('<text x="48" y="223" font-family="FuseMono, monospace" font-size="11" font-weight="800" fill="%s">WEIGHTS: 6.19 GB</text>' % CYAN)
    # Runtime context block (62px)
    b.append('<rect x="312" y="204" width="62" height="30" rx="3" fill="rgba(245,197,49,0.22)" stroke="%s" stroke-width="1"/>' % GOLD)
    b.append('<text x="343" y="223" text-anchor="middle" font-family="FuseMono, monospace" font-size="9" font-weight="800" fill="%s">+RUNTIME</text>' % GOLD)
    # Headroom block (48px)
    b.append('<rect x="378" y="204" width="44" height="30" rx="3" fill="rgba(0,245,155,0.08)" stroke="%s" stroke-width="1" stroke-dasharray="3 2"/>' % GREEN)
    b.append('<text x="400" y="223" text-anchor="middle" font-family="FuseMono, monospace" font-size="8.5" font-weight="800" fill="%s">FREE</text>' % GREEN)

    # --- Scenario B: Sustained Workload
    b.append('<text x="36" y="254" font-family="FuseMono, monospace" font-size="9.5" font-weight="700" '
             'fill="%s" letter-spacing="1">SCENARIO B: DEEP CONTEXT & AFTERNOON WORKLOAD</text>' % GOLD)
    
    # Bar Container B (width 388)
    b.append('<rect x="36" y="262" width="388" height="38" rx="5" fill="rgba(245,197,49,0.06)" stroke="%s" stroke-width="1.2"/>' % GOLD)
    # Weights block
    b.append('<rect x="38" y="264" width="270" height="34" rx="4" fill="rgba(56,217,232,0.22)" stroke="%s" stroke-width="1"/>' % CYAN)
    b.append('<text x="48" y="285" font-family="FuseMono, monospace" font-size="11" font-weight="800" fill="%s">WEIGHTS: 6.19 GB</text>' % CYAN)
    # Buffers block
    b.append('<rect x="312" y="264" width="46" height="34" rx="3" fill="rgba(245,197,49,0.22)" stroke="%s" stroke-width="1"/>' % GOLD)
    b.append('<text x="335" y="285" text-anchor="middle" font-family="FuseMono, monospace" font-size="9" font-weight="800" fill="%s">+CTX</text>' % GOLD)
    # Dynamic KV Cache block (fills right up to the 8GB edge)
    b.append('<rect x="362" y="264" width="60" height="34" rx="3" fill="rgba(255,59,48,0.28)" stroke="%s" stroke-width="1.5"/>' % RED)
    b.append('<text x="392" y="278" text-anchor="middle" font-family="FuseMono, monospace" font-size="8.5" font-weight="800" fill="%s">+KV CACHE</text>' % INK)
    b.append('<text x="392" y="291" text-anchor="middle" font-family="FuseMono, monospace" font-size="7.5" font-weight="700" fill="%s">O(L) LINEAR</text>' % RED)

    # Scale indicators
    b.append('<line x1="38" y1="312" x2="422" y2="312" stroke="%s" stroke-width="1" stroke-dasharray="2 3"/>' % HAIR)
    b.append('<text x="38" y="324" font-family="FuseMono, monospace" font-size="8.5" font-weight="700" fill="%s">0.0 GB</text>' % GREY)
    b.append('<text x="230" y="324" text-anchor="middle" font-family="FuseMono, monospace" font-size="8.5" font-weight="700" fill="%s">4.0 GB</text>' % GREY)
    b.append('<text x="422" y="324" text-anchor="end" font-family="FuseMono, monospace" font-size="8.5" font-weight="800" fill="%s">8.0 GB LIMIT</text>' % GOLD)

    # Status callout badge inside GPU container
    b.append('<rect x="36" y="334" width="388" height="36" rx="5" fill="rgba(255,59,48,0.10)" stroke="%s" stroke-width="1.2"/>' % RED)
    b.append('<circle cx="52" cy="352" r="4" fill="%s"/>' % RED)
    b.append('<text x="64" y="348" font-family="FuseMono, monospace" font-size="9" font-weight="800" fill="%s">WORKLOAD EXPANSION EXHAUSTS 8GB HEADROOM</text>' % RED)
    b.append('<text x="64" y="361" font-family="FuseMono, monospace" font-size="8" font-weight="600" fill="%s">Triggers system RAM offloading, severe slowdown, or launch abort</text>' % INK)

    # =========================================================================
    # 4. BOTTOM ARCHITECTURAL TAKEAWAY CARD
    # =========================================================================
    b.append('<rect x="20" y="392" width="420" height="92" rx="8" fill="rgba(18, 24, 38, 0.96)" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    b.append('<text x="230" y="416" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="11" font-weight="800" fill="%s" letter-spacing="1.5">ILLUSTRATIVE RUNTIME PROGRESSION</text>' % GOLD)
    b.append('<text x="230" y="438" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="10" font-weight="600" fill="%s">Active memory expands beyond base file size as conversation deepens</text>' % INK)
    b.append('<text x="230" y="456" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="9" font-weight="700" fill="%s" letter-spacing="0.5">ALLOCATION VARIES BY RUNTIME, CONTEXT DEPTH & OS OVERHEAD</text>' % GREY)
    b.append('<text x="230" y="472" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="8.5" font-weight="600" fill="%s">Disk fit is passive · GPU execution requires active dynamic memory</text>' % FAINT)

    return _svg("0 0 460 496", "".join(b), "vram_stack")


ART = {
    "laptop":  laptop_wait,
    "gpu":     gpu_card,
    "gpu_8gb": gpu_8gb,
    "gpu_12gb": gpu_12gb,
    "gpu_16gb": gpu_16gb,
    "gpu_24gb": gpu_24gb,
    "collapse": collapse_curve,
    "clock":   stopwatch,
    "meter":   bandwidth_meter,
    "caveat":  caveat_mark,
    "vram_stack": vram_stack,
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
