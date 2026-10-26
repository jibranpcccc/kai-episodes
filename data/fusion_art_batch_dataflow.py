# -*- coding: utf-8 -*-
"""
FUSION ART BATCH — dataflow. Generated for the Byte Forensics asset library.

Five drawings on the data path: the prompt, the tokens it is cut into, the
context window they live in, the KV cache, and the pipeline they run through.

Same grammar as fusion_art.py:
  * flat line art on near-black, no gradients, no shadows, no 3D
  * ONE accent per drawing (GOLD), used sparingly
  * a <g> NEVER carries a transform attribute
  * every moving part is wrapped in <g data-amb="...">
  * nothing overlaps anything it should not
  * the viewBox is tight around the real content, and the drawing is centred
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


# ==================================================================== dataflow 1
def prompt_stream():
    """A long prompt being typed, line by line. The caret waits at the end."""
    b = []
    # --- the page
    b.append('<rect x="24" y="20" width="372" height="250" rx="10" '
             'fill="rgba(246,246,244,.02)" stroke="%s" stroke-width="3"/>' % INK)
    # --- the text: every line shorter than the one above it, the last one
    #     brightest because it is the one the caret is sitting at the end of
    lines = [(340, .28), (322, .32), (304, .36), (286, .40), (268, .46),
             (250, .52), (232, .60), (196, .72), (146, .90)]
    for i, (w, o) in enumerate(lines):
        b.append('<rect x="40" y="%d" width="%d" height="7" rx="3.5" fill="%s" opacity="%.2f"/>'
                 % (40 + i * 24, w, INK, o))
    # --- the caret, blinking forever, at the end of the last line
    b.append('<g data-amb="blink">'
             '<rect x="191" y="224" width="10" height="22" rx="1" fill="%s"/></g>' % GOLD)
    return _svg("12 8 396 274", "".join(b), "prompt_stream")


# ==================================================================== dataflow 2
def token_blocks():
    """30-day billed usage telemetry audit log."""
    b = []
    b.append('<text x="40" y="28" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="800" fill="%s" letter-spacing="3">30-DAY USAGE LOG</text>' % GREY)
    # --- 30 day blocks representing a calendar month of logs
    for i in range(15):
        b.append('<rect x="%d" y="52" width="18" height="20" rx="2" fill="%s" opacity="%s"/>'
                 % (40 + i * 22, GOLD if i % 4 == 0 else INK, ".75" if i % 4 == 0 else ".35"))
    # --- the bracket, spanning the whole row
    b.append('<g data-amb="pulse" data-amb-k="0" data-amb-speed="1.4">')
    b.append('<path d="M40 88 L40 102 L370 102 L370 88" fill="none" stroke="%s" '
             'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>' % GOLD)
    b.append('</g>')
    # --- description
    b.append('<text x="205" y="130" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="800" fill="%s" letter-spacing="2">BILLED USAGE AUDIT</text>'
             % GOLD)
    return _svg("28 5 356 137", "".join(b), "token_blocks")


# ==================================================================== dataflow 3
def context_window():
    """The context window: the used half packed with tokens, the free half empty."""
    b = []
    b.append('<text x="40" y="30" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="800" fill="%s" letter-spacing="3">CONTEXT WINDOW</text>' % GREY)
    # --- the frame
    b.append('<rect x="40" y="52" width="480" height="156" rx="12" fill="none" '
             'stroke="%s" stroke-width="3"/>' % INK)
    # --- the used half, packed to the boundary
    for r in range(6):
        for c in range(10):
            b.append('<rect x="%d" y="%d" width="18" height="18" rx="2" fill="%s" opacity=".50"/>'
                     % (54 + c * 22, 64 + r * 22, INK))
    # --- the boundary between used and free
    b.append('<path d="M280 56 L280 204" fill="none" stroke="%s" stroke-width="3" '
             'stroke-linecap="round"/>' % GOLD)
    # --- what each half is
    b.append('<text x="40" y="234" font-family="FuseMono, monospace" font-size="13" '
             'font-weight="700" fill="%s" letter-spacing="2">USED</text>' % GREY)
    b.append('<text x="520" y="234" text-anchor="end" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">REMAINING</text>'
             % GREY)
    return _svg("28 7 504 240", "".join(b), "context_window")


# ==================================================================== dataflow 4
def kv_cache():
    """A KV cache: a grid of slots, read on the way in, written on the way out."""
    b = []
    b.append('<text x="270" y="32" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="15" font-weight="800" fill="%s" letter-spacing="4">KV CACHE</text>' % GREY)
    # --- the cache itself
    b.append('<rect x="150" y="60" width="240" height="152" rx="14" '
             'fill="rgba(246,246,244,.02)" stroke="%s" stroke-width="3"/>' % INK)
    # --- the cells inside it
    for r in range(4):
        for c in range(7):
            b.append('<rect x="%d" y="%d" width="22" height="20" rx="2" fill="%s" opacity=".32"/>'
                     % (175 + c * 28, 87 + r * 26, INK))
    # --- read: the gold arrow coming in from the left, head clear of the grid
    b.append('<path d="M44 136 L126 136" fill="none" stroke="%s" stroke-width="3" '
             'stroke-linecap="round"/>' % GOLD)
    b.append('<path d="M126 126 L138 136 L126 146" fill="none" stroke="%s" stroke-width="3" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % GOLD)
    b.append('<text x="85" y="120" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="3">READ</text>' % GREY)
    # --- write: the gold arrow leaving on the right, head clear of the grid
    b.append('<path d="M402 136 L484 136" fill="none" stroke="%s" stroke-width="3" '
             'stroke-linecap="round"/>' % GOLD)
    b.append('<path d="M484 126 L496 136 L484 146" fill="none" stroke="%s" stroke-width="3" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % GOLD)
    b.append('<text x="449" y="120" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="3">WRITE</text>' % GREY)
    return _svg("32 9 476 215", "".join(b), "kv_cache")


# ==================================================================== dataflow 5
def pipeline():
    """Automated document processing pipeline: four stages, retry & validation."""
    b = []
    b.append('<text x="40" y="32" font-family="FuseMono, monospace" font-size="15" '
             'font-weight="800" fill="%s" letter-spacing="3">DOCUMENT PIPELINE</text>' % GREY)
    # --- the four stages
    stages = [("DOCUMENTS", "INGEST"), ("BATCH QUEUE", "API CALLS"),
              ("STRUCTURED", "OUTPUTS"), ("VALIDATION", "RETRY GATE")]
    for i, (name, sub) in enumerate(stages):
        x = 40 + i * 168
        last = (i == 3)
        b.append('<rect x="%d" y="56" width="112" height="120" rx="12" fill="none" '
                 'stroke="%s" stroke-width="3"/>' % (x, GOLD if last else INK))
        b.append('<text x="%d" y="108" text-anchor="middle" font-family="FuseMono, monospace" '
                 'font-size="14" font-weight="800" fill="%s" letter-spacing="2">%s</text>'
                 % (x + 56, INK, name))
        b.append('<text x="%d" y="134" text-anchor="middle" font-family="FuseMono, monospace" '
                 'font-size="12" font-weight="700" fill="%s" letter-spacing="2">%s</text>'
                 % (x + 56, FAINT, sub))
    # --- the arrows, sitting in the gaps and never touching a box
    for i in range(3):
        x = 152 + i * 168
        b.append('<path d="M%d 116 L%d 116" fill="none" stroke="%s" stroke-width="2.5" '
                 'stroke-linecap="round"/>' % (x + 10, x + 34, INK))
        b.append('<path d="M%d 108 L%d 116 L%d 124" fill="none" stroke="%s" stroke-width="2.5" '
                 'stroke-linecap="round" stroke-linejoin="round"/>'
                 % (x + 34, x + 46, x + 34, INK))
    b.append('<text x="348" y="206" text-anchor="middle" font-family="FuseMono, monospace" '
             'font-size="13" font-weight="700" fill="%s" letter-spacing="2">'
             'AUTOMATED EVENING PIPELINE</text>' % FAINT)
    return _svg("28 9 640 212", "".join(b), "pipeline")


DATA_FLOW_ART = {
    "prompt_stream":   prompt_stream,
    "token_blocks":    token_blocks,
    "context_window":  context_window,
    "kv_cache":        kv_cache,
    "pipeline":        pipeline,
}
