# -*- coding: utf-8 -*-
"""Generated from angle VRAM-020 -- DISK SIZE IS NOT MEMORY SIZE.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py VRAM-020
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same vram. Picture the vram sticks. Total VRAM in use with a four thousand token context. Generation rate on two sixteen gigabyte cards with a four thousand token context. The size of the block scale in the four bit format. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="DISK SIZE IS NOT MEMORY SIZE",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Same board",
    art_at="Picture the vram",
    chips=[{"t": "4K", "c": "gold", "at": "Total VRAM in"}, {"t": "2 cards 4K", "c": "red", "at": "Generation rate on"}],
    stats=[{"v": "32", "u": "", "lab": "32 BIT", "c": "cyan", "at": "The size of"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with an eight thousand token context. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context. The overhead the block scales add per weight.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="DISK SIZE IS NOT MEMORY SIZE",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="The vram figure",
    art_at="Picture the vram",
    chain=[{"t": "8K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 2 cards 128K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of +0.5 BIT, taken on the board.", "at": "The overhead the"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One capacity number, one source, one board. Picture the window and what is in it. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. The effective bits per converted weight in the pinned implementation, with the nested scales compressed too. One method, every row.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="DISK SIZE IS NOT MEMORY SIZE",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="One capacity number",
    art_at="Picture the window",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "gold", "at": "Generation rate on"}, {"rank": "2", "name": "Qwen2.5 3B Instruct", "val": "4.127", "sub": "EFFECTIVE", "cls": "", "at": "The effective bits"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="DISK SIZE IS NOT MEMORY SIZE",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Nothing here about",
    art_at="Picture the vram",
    bars=[{"lab": "Muse Glimmer 30B", "val": "16", "unit": "GB", "pct": 47.1, "cls": "", "at": "Total VRAM in use with a thirty-two"}, {"lab": "Muse Glimmer 30B", "val": "17", "unit": "GB", "pct": 50.0, "cls": "", "at": "Total VRAM in use with a sixty-four"}, {"lab": "Muse Glimmer 30B", "val": "20", "unit": "GB", "pct": 58.8, "cls": "", "at": "Total VRAM in use with a two"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the capacity of the hardware, not of the brochure. Picture the window and what is in it. Generation rate on two sixteen gigabyte cards with a four thousand token context. Total VRAM in use with an eight thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="DISK SIZE IS NOT MEMORY SIZE",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="This is the",
    art_at="Picture the window",
    rails=[{"lab": "2 cards 4K", "val": "22.5", "pct": 59.1, "cls": "red", "at": "Generation rate on"}, {"lab": "8K", "val": "18", "pct": 52.9, "cls": "", "at": "Total VRAM in"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured capacity, on this board, in this run. Picture the window and what is in it. A pair of cards never buys speed. One card is faster than two at the same context. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="DISK SIZE IS NOT MEMORY SIZE",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="Measured capacity, on",
    art_at="Picture the window",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "A pair of cards never buys speed", "at": "A pair of"}, {"t": "One card is faster than two at the same context", "at": "One card is"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every capacity figure here carries its own source. Picture the window and what is in it. On the bench: Qwen 3.8 27B. The overhead the block scales add per weight. The line reads nineteen gigabytes, from the same run.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="DISK SIZE IS NOT MEMORY SIZE",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="Every capacity figure",
    art_at="Picture the window",
    name="Qwen 3.8 27B",
    blurb="The overhead the block scales add per weight",
    meta="16K &middot; 19 GB",
    name_at="On the bench",
    blurb_at="The overhead the",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The capacity number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the vram budget figure, the context budget figure, the quant budget figure.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="DISK SIZE IS NOT MEMORY SIZE",
    header_at="The capacity number",
    items=[{"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}, {"key": "gguf_blocks", "label": "quant budget", "at": "the quant budget figure"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. A model's size on disk and its size in memory are different numbers, and only the second one decides whether it runs on your card. DISK SIZE IS NOT MEMORY SIZE.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="DISK SIZE IS NOT MEMORY SIZE",
    sub="A model's size on disk and its size in memory are different numbers, and only the second one decides whether it runs on your card.",
    art="gguf_blocks",
    head_at="DISK SIZE IS NOT MEMORY SIZE",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-VRAM-020"
TITLE = "DISK SIZE IS NOT MEMORY SIZE"
DOC_TITLE = "DISK SIZE IS NOT MEMORY SIZE &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
