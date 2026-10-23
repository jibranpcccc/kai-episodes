# -*- coding: utf-8 -*-
"""
FUSION — 30-SECOND HIGH-DENSITY EDITION
"Why a Tiny LoRA Adapter Can Still Fill Your GPU"
Built with the updated FUSION engine, layouts, and vector art library.
"""

NAME = "BYTE-LORA-30S"
TITLE = "WHY A TINY LoRA ADAPTER CAN STILL FILL YOUR GPU"
DOC_TITLE = "WHY A TINY LoRA ADAPTER CAN STILL FILL YOUR GPU · BYTE FORENSICS"
KICKER = "BYTE FORENSICS · EPISODE 08"
SUBTITLE = "the adapter is small. the training job is not."
TAIL = 2.51

W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


# =====================================================================
# 1  THE PARADOX (HOOK) ~12.0s
# =====================================================================
win("hook",
    vo="Training a tiny adapter can exhaust your GPU. That is the first "
       "distinction to make before fine-tuning a local model. The adapter "
       "file describes the changes you learned, not everything the machine "
       "needed while learning them.",
    kicker="EPISODE 08 · ACT ONE",
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
# 2  THE ARCHITECTURE, SPECIFICALLY (ROWS) ~15.1s
# =====================================================================
win("rows",
    vo="Use an actual architecture. Qwen two point five, three billion, "
       "Instruct has thirty-six layers and a hidden width of two thousand "
       "forty-eight. Its sixteen query heads share only two key and value "
       "heads. Each head is one hundred twenty-eight values wide.",
    kicker="EPISODE 08 · ACT ONE",
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
    source="qwen2.5 3b instruct · architecture")
