# -*- coding: utf-8 -*-
"""FUSION ART BATCH — symbols. Generated for the Byte Forensics asset library."""

INK = "#F6F6F4"
GOLD = "#F5C531"
CYAN = "#38D9E8"
RED = "#E12A27"
GREY = "rgba(246,246,244,.52)"
FAINT = "rgba(246,246,244,.30)"
HAIR = "rgba(246,246,244,.18)"


def _svg(view, body, slug):
    return ('<svg viewBox="%s" class="art" data-art="%s" '
            'xmlns="http://www.w3.org/2000/svg">%s</svg>' % (view, slug, body))


def magnifier():
    """A magnifying glass on its own."""
    b = []
    b.append('<circle cx="120" cy="120" r="64" fill="none" stroke="%s" stroke-width="3"/>' % GOLD)
    b.append('<path d="M165 165 L225 225" stroke="%s" stroke-width="14" '
             'stroke-linecap="round"/>' % GOLD)
    b.append('<path d="M86 98 A48 48 0 0 1 124 76" fill="none" stroke="%s" '
             'stroke-width="4" stroke-linecap="round" opacity=".30"/>' % INK)
    return _svg("44 44 200 200", "".join(b), "magnifier")


def warning():
    """A warning triangle."""
    b = []
    b.append('<path d="M120 34 L214 200 L26 200 Z" fill="none" stroke="%s" '
             'stroke-width="3" stroke-linejoin="round"/>' % GOLD)
    b.append('<path d="M120 98 L120 142" stroke="%s" stroke-width="12" '
             'stroke-linecap="round"/>' % GOLD)
    b.append('<circle cx="120" cy="170" r="8" fill="%s"/>' % GOLD)
    return _svg("14 22 212 198", "".join(b), "warning")


def checklist():
    """A clipboard with three rows, one ticked."""
    b = []
    b.append('<path d="M110 40 H83 A13 13 0 0 0 70 53 V237 A13 13 0 0 0 83 250 '
             'H217 A13 13 0 0 0 230 237 V53 A13 13 0 0 0 217 40 H190" fill="none" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="110" y="20" width="80" height="28" rx="9" fill="none" '
             'stroke="%s" stroke-width="3"/>' % INK)
    b.append('<rect x="94" y="104" width="26" height="26" rx="4" fill="%s"/>' % GOLD)
    b.append('<path d="M99 117 L105 123 L115 111" fill="none" stroke="#0D1110" '
             'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    for y in (154, 204):
        b.append('<rect x="94" y="%d" width="26" height="26" rx="4" fill="none" '
                 'stroke="%s" stroke-width="1.5"/>' % (y, INK))
    for y in (110, 160, 210):
        b.append('<rect x="136" y="%d" width="76" height="8" rx="4" fill="%s" '
                 'opacity=".38"/>' % (y, INK))
    return _svg("58 8 184 254", "".join(b), "checklist")


def price_tag():
    """A price tag with a string and a value."""
    b = []
    b.append('<path d="M72 90 L104 46 L220 46 L220 134 L104 134 Z" fill="none" '
             'stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % INK)
    b.append('<circle cx="82" cy="90" r="8" fill="none" stroke="%s" stroke-width="3"/>' % INK)
    b.append('<path d="M74 90 C54 90 42 76 46 56" fill="none" stroke="%s" '
             'stroke-width="3" stroke-linecap="round"/>' % GOLD)
    b.append('<path d="M120 70 L186 70" stroke="%s" stroke-width="14" '
             'stroke-linecap="round"/>' % GOLD)
    b.append('<path d="M120 106 L162 106" stroke="%s" stroke-width="10" '
             'stroke-linecap="round" opacity=".45"/>' % INK)
    return _svg("30 34 202 112", "".join(b), "price_tag")


def scales():
    """A balance scale, the left pan sitting lower."""
    b = []
    b.append('<path d="M92 212 L148 212 L158 234 L82 234 Z" fill="none" stroke="%s" '
             'stroke-width="3" stroke-linejoin="round"/>' % INK)
    b.append('<path d="M120 64 L120 212" stroke="%s" stroke-width="4" '
             'stroke-linecap="round"/>' % INK)
    b.append('<path d="M30 64 L210 64" stroke="%s" stroke-width="5" '
             'stroke-linecap="round"/>' % INK)
    b.append('<path d="M60 64 L60 130" stroke="%s" stroke-width="2"/>' % FAINT)
    b.append('<path d="M158 64 L158 108" stroke="%s" stroke-width="2"/>' % FAINT)
    b.append('<path d="M32 130 L88 130 L80 154 L40 154 Z" fill="%s" opacity=".9"/>' % GOLD)
    b.append('<path d="M130 108 L186 108 L178 130 L138 130 Z" fill="none" stroke="%s" '
             'stroke-width="2"/>' % INK)
    return _svg("18 48 204 198", "".join(b), "scales")


def question():
    """A question mark inside a circle."""
    b = []
    b.append('<circle cx="120" cy="120" r="78" fill="none" stroke="%s" stroke-width="3"/>' % INK)
    b.append('<path d="M90 100 C90 70 150 70 150 100 C150 120 120 124 120 144" fill="none" '
             'stroke="%s" stroke-width="12" stroke-linecap="round"/>' % GOLD)
    b.append('<circle cx="120" cy="172" r="9" fill="%s"/>' % GOLD)
    return _svg("30 30 180 180", "".join(b), "question")
