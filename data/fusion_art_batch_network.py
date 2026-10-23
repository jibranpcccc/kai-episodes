# -*- coding: utf-8 -*-
"""FUSION ART BATCH — network. Generated for the Byte Forensics asset library.

Four drawings about local networking hardware: a home router, a rack switch,
a crossed-out cloud and a local link between two machines.

Same rules as data/fusion_art.py:
  * a <g> NEVER carries a transform attribute.
  * one accent colour per drawing (GOLD), used sparingly. The cloud adds RED
    for the cross that marks "not local".
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
def router():
    """A home router from the front: flat wide body, two antennas, a row of
    LAN ports along the front and one gold status LED."""
    b = []
    # --- the two antennas, drawn first so the opaque body cuts them off clean
    for x in (128, 372):
        b.append('<path d="M%d 184 L%d 60" stroke="%s" stroke-width="7" '
                 'stroke-linecap="round"/>' % (x, x, INK))
    # --- the body
    b.append('<rect x="70" y="176" width="360" height="112" rx="12" fill="#0D1110" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the recessed front band the ports sit in
    b.append('<rect x="92" y="232" width="316" height="36" rx="7" fill="rgba(246,246,244,.04)" '
             'stroke="%s" stroke-width="1.5"/>' % HAIR)
    # --- six LAN ports along the front
    for i in range(6):
        x = 119 + i * 46
        b.append('<rect x="%d" y="243" width="32" height="20" rx="3" fill="#0D1110" '
                 'stroke="%s" stroke-width="1.5"/>' % (x, INK))
        b.append('<rect x="%d" y="255" width="12" height="6" rx="1" fill="%s" opacity=".55"/>'
                 % (x + 10, GREY))
    # --- the gold status LED, the one accent. The halo is a ring, not a disc:
    #     a filled disc at this opacity reads as a dull olive blob.
    b.append('<circle cx="110" cy="202" r="13" fill="none" stroke="%s" '
             'stroke-width="2" opacity=".35"/>' % GOLD)
    b.append('<circle cx="110" cy="202" r="7" fill="%s"/>' % GOLD)
    b.append('<text x="134" y="207" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="2">PWR</text>' % FAINT)
    # --- the gateway address, dim, in the clear space on the right
    b.append('<text x="408" y="207" text-anchor="end" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">'
             '192.168.1.1</text>' % FAINT)
    return _svg("58 44.5 384 255.5", "".join(b), "router")


# ==================================================================== scene 2
def switch():
    """A rack switch: thin wide chassis, eight numbered ports with a link
    light under each, rack ears on both ends."""
    b = []
    # --- the rack ears, drawn first so the chassis covers their inner edge
    for x in (56, 496):
        b.append('<rect x="%d" y="150" width="48" height="52" rx="6" fill="#0D1110" '
                 'stroke="%s" stroke-width="3"/>' % (x, INK))
    # --- the chassis
    b.append('<rect x="100" y="136" width="400" height="80" rx="8" fill="#0D1110" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- eight numbered ports, each with a link light under it
    for i in range(8):
        x = 122 + i * 46
        cx = x + 17
        if i == 0:
            b.append('<rect x="%d" y="150" width="34" height="30" rx="3" fill="#0D1110" '
                     'stroke="%s" stroke-width="2"/>' % (x, GOLD))
        else:
            b.append('<rect x="%d" y="150" width="34" height="30" rx="3" fill="#0D1110" '
                     'stroke="%s" stroke-width="1.5"/>' % (x, GREY))
        b.append('<text x="%d" y="170" text-anchor="middle" font-family="FuseMono, monospace" '
                 'font-size="13" font-weight="800" fill="%s" letter-spacing="1">%d</text>'
                 % (cx, INK, i + 1))
        if i == 0:
            b.append('<circle cx="%d" cy="194" r="9" fill="none" stroke="%s" '
                     'stroke-width="2" opacity=".4"/>' % (cx, GOLD))
            b.append('<circle cx="%d" cy="194" r="5" fill="%s"/>' % (cx, GOLD))
        else:
            b.append('<circle cx="%d" cy="194" r="3.5" fill="%s" opacity=".7"/>' % (cx, GREY))
    # --- the screw holes in the rack ears
    for cx in (79, 521):
        b.append('<circle cx="%d" cy="176" r="9" fill="#0D1110" stroke="%s" '
                 'stroke-width="1.5"/>' % (cx, INK))
    # --- captions, above the chassis, clear of everything
    b.append('<text x="100" y="124" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="3">SWITCH</text>' % FAINT)
    b.append('<text x="500" y="124" text-anchor="end" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="3">8 PORTS</text>' % FAINT)
    return _svg("46 102 508 126", "".join(b), "switch")


# ==================================================================== scene 3
def cloud():
    """A cloud drawn as one continuous line: three arcs and a flat base, the
    way a cloud is actually built. A gold download arrow sits inside it and a
    small red cross runs through the arrow: the cloud is not local."""
    b = []
    # --- the cloud outline, one continuous path.
    #     left bump (r52, centre 108/196) -> main hump (r84, centre 230/150)
    #     -> right bump (r66, centre 352/182) -> flat base back to the start.
    b.append('<path d="M60 160 C32 160 20 142 24 120 C28 100 46 88 66 90 '
             'C76 62 118 56 132 80 C146 58 190 60 198 90 '
             'C218 84 240 100 240 122 C258 128 262 156 240 160 L60 160 Z" '
             'fill="none" stroke="%s" stroke-width="3" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % INK)
    # --- the gold arrow, pointing down
    b.append('<path d="M140 74 L140 122" stroke="%s" stroke-width="9" '
             'stroke-linecap="round"/>' % GOLD)
    b.append('<path d="M126 108 L140 126 L154 108" fill="none" stroke="%s" '
             'stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>' % GOLD)
    # --- the red cross. A dark knockout underneath, so it cuts the arrow
    #     cleanly instead of letting gold show through the red.
    x = 'M124 88 L156 116 M156 88 L124 116'
    b.append('<path d="%s" fill="none" stroke="#0D1110" stroke-width="12" '
             'stroke-linecap="round"/>' % x)
    b.append('<path d="%s" fill="none" stroke="%s" stroke-width="6" '
             'stroke-linecap="round"/>' % (x, RED))
    # --- caption
    b.append('<text x="237" y="44" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="3">REMOTE</text>' % FAINT)
    return _svg("44 22 386 238", "".join(b), "cloud")


# ==================================================================== scene 4
def lan_link():
    """A local link: a machine on the left, a solid gold cable, a second
    machine on the right, a plug at each end of the cable."""
    b = []
    # --- the two machines
    b.append('<rect x="40" y="86" width="150" height="150" rx="12" fill="#0D1110" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="364" y="86" width="150" height="150" rx="12" fill="#0D1110" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the plug at each end of the cable
    b.append('<rect x="186" y="146" width="30" height="28" rx="4" fill="#0D1110" '
             'stroke="%s" stroke-width="2.5"/>' % INK)
    b.append('<rect x="338" y="146" width="30" height="28" rx="4" fill="#0D1110" '
             'stroke="%s" stroke-width="2.5"/>' % INK)
    # --- the solid gold cable, run over the plug mouths so it reads as seated
    b.append('<path d="M200 160 L354 160" stroke="%s" stroke-width="7" '
             'stroke-linecap="round"/>' % GOLD)
    # --- the packet riding the cable
    b.append('<g data-amb="pulse" data-amb-k="0" data-amb-speed="1.2">')
    b.append('<circle cx="277" cy="160" r="7" fill="%s" stroke="#0D1110" stroke-width="3"/>' % INK)
    b.append('</g>')
    # --- the machine labels
    b.append('<text x="115" y="146" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="700" fill="%s" letter-spacing="3">HOST</text>' % GREY)
    b.append('<text x="439" y="146" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="700" fill="%s" letter-spacing="3">GPU BOX</text>' % GREY)
    # --- vents
    for cx in (115, 439):
        for i, w in enumerate((80, 54)):
            b.append('<rect x="%d" y="%d" width="%d" height="5" rx="2.5" fill="%s" opacity=".25"/>'
                     % (cx - w // 2, 166 + i * 12, w, INK))
    # --- caption, in the clear space under the cable
    b.append('<text x="277" y="212" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="3">LOCAL LINK</text>' % FAINT)
    return _svg("28 74 498 174", "".join(b), "lan_link")
