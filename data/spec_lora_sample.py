# -*- coding: utf-8 -*-
"""
FUSION — EPISODE 08 SAMPLE: "Why a Tiny LoRA Adapter Can Still Fill Your GPU"

A ONE MINUTE sample, built with the engine and the layouts that were approved
100% in BYTE-07-FUSION.html.  Nothing new is invented here:

  * the engine is core/fusion.css + core/fusion.js restored byte for byte out
    of the approved BYTE-07-FUSION.html
  * the layouts are the approved ones only: hook, rows, chain, note
  * the drawings are the library: model_file, superchip, two_die, ram_stick,
    magnifier

The script is the author's, cut to the opening of Act One and the memory
arithmetic of Act Four.  Every number on screen is a number the script says.
"""

import re

NAME = "BYTE-LORA-SAMPLE"
TITLE = "WHY A TINY LoRA ADAPTER CAN STILL FILL YOUR GPU"
KICKER = "BYTE FORENSICS &middot; EPISODE 08"
SUBTITLE = "the adapter is small. the training job is not."

W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


# =====================================================================
# 1  THE PARADOX
# =====================================================================
win("hook",
    vo="Training a tiny adapter can exhaust your GPU. That is the first "
       "distinction to make before fine-tuning a local model. The adapter "
       "file describes the changes you learned, not everything the machine "
       "needed while learning them.",
    kicker="EPISODE 08 &middot; ACT ONE",
    title="TINY ADAPTER, BIG JOB",
    sub="the file is small. the job is not.",
    art="model_file",
    art_caption="MODEL FILE",
    header_at="Training a tiny adapter can exhaust your GPU",
    art_at="Training a tiny adapter can exhaust your GPU",
    chips=[
        dict(t="TRAINING CAN EXHAUST YOUR GPU", c="red",
             at="Training a tiny adapter can exhaust your GPU"),
        dict(t="THE FIRST DISTINCTION TO MAKE", c="cyan",
             at="the first distinction to make"),
        dict(t="THE FILE IS NOT THE JOB", c="ghost",
             at="The adapter file describes the changes you learned"),
    ],
    stats=[
        dict(v="3.69M", u="PARAMS", lab="RANK 16, QUERY AND VALUE ONLY",
             c="gold", at="Training a tiny adapter can exhaust your GPU"),
        dict(v="<30M", u="PARAMS", lab="ALL SEVEN PROJECTIONS TARGETED",
             c="red", at="Training a tiny adapter can exhaust your GPU"),
    ],
    tape="A SMALL RANK IS NOT A SPECIFICATION",
    tape_at="not everything the machine needed while learning them")

# =====================================================================
# 2  THE ARCHITECTURE, SPECIFICALLY
# =====================================================================
win("rows",
    vo="Use an actual architecture. Qwen two point five, three billion, "
       "Instruct has thirty-six layers and a hidden width of two thousand "
       "forty-eight. Its sixteen query heads share only two key and value "
       "heads. Each head is one hundred twenty-eight values wide.",
    kicker="EPISODE 08 &middot; ACT ONE",
    title="QWEN 2.5 3B INSTRUCT",
    art="superchip",
    art_caption="THE SUPERCHIP",
    header_at="Use an actual architecture",
    art_at="Use an actual architecture",
    rows=[
        dict(rank="01", name="LAYERS", val="36", sub="BLOCKS", cls="gold", sent=1),
        dict(rank="02", name="HIDDEN", val="2,048", sub="WIDTH", cls="",
             at="a hidden width of two thousand forty-eight"),
        dict(rank="03", name="QUERY HEADS", val="16", sub="ATTENTION", cls="", sent=2),
        dict(rank="04", name="KV HEADS", val="2", sub="SHARED", cls="red",
             at="share only two key and value heads"),
        dict(rank="05", name="HEAD DIM", val="128", sub="VALUES WIDE", cls="", sent=3),
    ],
    closing=dict(c="gold", t="SO THE VALUE PROJECTION IS 256, NOT 2,048",
                 at="one hundred twenty-eight values wide"),
    source="qwen2.5 3b instruct &middot; architecture")

# =====================================================================
# 3  THE ARITHMETIC
# =====================================================================
win("chain",
    vo="The adapter arithmetic is pleasantly concrete. For a projection with "
       "an input width and an output width, rank times their sum gives the "
       "added parameter count. One small matrix maps the input into the rank, "
       "and the second maps the rank into the output.",
    kicker="EPISODE 08 &middot; ACT ONE",
    title="RANK TIMES THE SUM OF THE WIDTHS",
    art="two_die",
    art_caption="TWO MATRICES",
    header_at="The adapter arithmetic is pleasantly concrete",
    art_at="The adapter arithmetic is pleasantly concrete",
    chain=[
        dict(t="INPUT", s="2048 WIDE", sent=1),
        dict(t="DOWN", s="2048 TO 16", at="rank times their sum"),
        dict(t="UP", s="16 TO 2048", sent=2),
        dict(t="ADDED", s="3,686,400 TOTAL", at="the second maps the rank into the output"),
    ],
    compare=[
        dict(cls="hot", title="FROZEN BASE",
             body="Every weight is kept, and the machine still runs on every example.",
             at="The adapter arithmetic is pleasantly concrete"),
        dict(cls="good", title="THE ADAPTER",
             body="Only this is trained, and it still needs the backward pass.",
             at="One small matrix maps the input into the rank"),
    ],
    source="derived &middot; rank 16, query and value only")

# =====================================================================
# 4  THE ARRAYS THAT COST MEMORY
# =====================================================================
win("rows",
    vo="Assume full-precision adapter weights, full-precision gradients, and "
       "two full-precision Adam moment buffers. That is sixteen bytes per "
       "trainable value. Our exact parameter count then gives about four "
       "hundred fifty-seven mebibytes for those four arrays.",
    kicker="EPISODE 08 &middot; ACT FOUR",
    title="THE ADAPTER ARRAYS",
    art="ram_stick",
    art_caption="SYSTEM MEMORY",
    header_at="Assume full-precision adapter weights",
    art_at="Assume full-precision adapter weights",
    rows=[
        dict(rank="01", name="ADAPTER WEIGHTS", val="4 B", sub="FULL PRECISION", cls="",
             at="full-precision adapter weights"),
        dict(rank="02", name="GRADIENTS", val="4 B", sub="FULL PRECISION", cls="",
             at="full-precision gradients"),
        dict(rank="03", name="ADAM MOMENTS", val="8 B", sub="TWO BUFFERS", cls="",
             at="two full-precision Adam moment buffers"),
        dict(rank="04", name="PER VALUE", val="16 B", sub="DERIVED", cls="",
             sent=1),
        dict(rank="05", name="FOR 30M", val="457 MiB", sub="DERIVED", cls="gold",
             sent=2),
    ],
    closing=dict(c="red", t="AND THAT IS ONLY THE ADAPTER",
                 at="four hundred fifty-seven mebibytes"),
    source="derived &middot; 16 bytes per trainable value")

# =====================================================================
# 5  WHAT THE NUMBER EXCLUDES
# =====================================================================
win("note",
    vo="It excludes the frozen base, saved activations, temporary workspaces, "
       "and anything else the implementation keeps. Calling that subtotal the "
       "required video memory would erase most of the question we came here "
       "to answer.",
    kicker="EPISODE 08 &middot; ACT FOUR",
    title="457 MiB IS NOT VIDEO MEMORY",
    art="magnifier",
    art_caption="READ THE FINE PRINT",
    header_at="It excludes the frozen base",
    art_at="It excludes the frozen base",
    note_head="WHAT THE SUBTOTAL EXCLUDES",
    note_items=[
        dict(t="THE FROZEN BASE", at="It excludes the frozen base"),
        dict(t="SAVED ACTIVATIONS", at="saved activations"),
        dict(t="TEMPORARY WORKSPACES", at="temporary workspaces"),
        dict(t="ANYTHING ELSE THE IMPLEMENTATION KEEPS",
             at="anything else the implementation keeps"),
    ],
    tape="DO NOT CALL IT VIDEO MEMORY",
    tape_at="Calling that subtotal the required video memory",
    source="derived, not measured",
    source_at="Calling that subtotal the required video memory")
