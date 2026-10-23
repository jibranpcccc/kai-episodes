# -*- coding: utf-8 -*-
"""Generated from angle LORA-004 -- A SMALL ADAPTER STILL NEEDS A BIG MODEL.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py LORA-004
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same lora. Picture the magnifier pass. The layer count of the model. Total VRAM in use with a four thousand token context. Generation rate on two sixteen gigabyte cards with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="A SMALL ADAPTER STILL NEEDS A BIG MODEL",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="Same board",
    art_at="Picture the magnifier",
    chips=[{"t": "LAYERS", "c": "gold", "at": "The layer count"}, {"t": "4K", "c": "cyan", "at": "Total VRAM in"}],
    stats=[{"v": "22.5", "u": "T/S", "lab": "2 cards 4K", "c": "red", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="chain",
    vo="The lora figure, read straight off the board. Picture the magnifier pass. The number of key value heads, shared across groups. Total VRAM in use with an eight thousand token context. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context. The width of one attention head.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="A SMALL ADAPTER STILL NEEDS A BIG MODEL",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="The lora figure",
    art_at="Picture the magnifier",
    chain=[{"t": "KV HEADS", "s": "This figure does not establish that a model fits.", "at": "The number of"}, {"t": "8K", "s": "This figure does not establish a speed.", "at": "Total VRAM in"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 2 cards 128K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of HEAD DIM, taken on the board.", "at": "The width of"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a sixteen thousand token context. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. The hidden width of the model. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="A SMALL ADAPTER STILL NEEDS A BIG MODEL",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "gold", "at": "Total VRAM in"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "red", "at": "Generation rate on"}, {"rank": "3", "name": "Qwen2.5 3B Instruct", "val": "2048", "sub": "HIDDEN", "cls": "", "at": "The hidden width"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="A SMALL ADAPTER STILL NEEDS A BIG MODEL",
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
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a four thousand token context. Generation rate on two sixteen gigabyte cards with a four thousand token context. Total VRAM in use with an eight thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="A SMALL ADAPTER STILL NEEDS A BIG MODEL",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="This is the",
    art_at="Picture the vram",
    rails=[{"lab": "4K", "val": "18", "pct": 52.9, "cls": "", "at": "Total VRAM in use with a four"}, {"lab": "2 cards 4K", "val": "22.5", "pct": 59.1, "cls": "red", "at": "Generation rate on"}, {"lab": "8K", "val": "18", "pct": 52.9, "cls": "", "at": "Total VRAM in use with an"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured capacity, on this board, in this run. Picture the window and what is in it. A pair of cards never buys speed. One card is faster than two at the same context. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="A SMALL ADAPTER STILL NEEDS A BIG MODEL",
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
    vo="Every lora figure here carries its own source. Picture the magnifier pass. On the bench: Qwen2.5 3B Instruct. Total VRAM in use with a sixty-four thousand token context. The line reads three million four hundred, from the same run.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="A SMALL ADAPTER STILL NEEDS A BIG MODEL",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="Every lora figure",
    art_at="Picture the magnifier",
    name="Qwen2.5 3B Instruct",
    blurb="Total VRAM in use with a sixty-four thousand token context",
    meta="TRAINABLE &middot; 3686400",
    name_at="On the bench",
    blurb_at="Total VRAM in",
    meta_at="The line reads",
    side="right",
    source="derived &middot; rank 16 &middot; qwen2.5 3b instruct",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the adapter budget figure, the vram budget figure, the context budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="A SMALL ADAPTER STILL NEEDS A BIG MODEL",
    header_at="The vram number",
    items=[{"key": "magnifier", "label": "adapter budget", "at": "the adapter budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="title",
    vo="One claim, one board, one run. The adapter's own file size says nothing about the memory it needs at runtime, because the merged weights must still fit. A SMALL ADAPTER STILL NEEDS A BIG MODEL.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="A SMALL ADAPTER STILL NEEDS A BIG MODEL",
    sub="The adapter's own file size says nothing about the memory it needs at runtime, because the merged weights must still fit.",
    art="context_window",
    head_at="A SMALL ADAPTER STILL NEEDS A BIG MODEL",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="nodes",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with a two hundred fifty-six thousand token context. The total trainable parameters with rank sixteen on seven projections. The bytes per trainable value, across the weight, the gradient and the optimizer state.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="A SMALL ADAPTER STILL NEEDS A BIG MODEL",
    header_at="The vram figure",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    art_at="Picture the vram",
    chain=[{"t": "256K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}, {"t": "TRAINABLE", "s": "This figure does not establish a speed.", "at": "The total trainable"}, {"t": "PER VALUE", "s": "This figure does not establish a fit claim.", "at": "The bytes per"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-LORA-004"
TITLE = "A SMALL ADAPTER STILL NEEDS A BIG MODEL"
DOC_TITLE = "A SMALL ADAPTER STILL NEEDS A BIG MODEL &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
