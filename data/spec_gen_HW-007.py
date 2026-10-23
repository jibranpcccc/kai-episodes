# -*- coding: utf-8 -*-
"""Generated from angle HW-007 -- MEMORY SIZE IS THE FIRST QUESTION.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py HW-007
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same vram. Picture the vram sticks. Total VRAM in use with a four thousand token context. Generation rate on two sixteen gigabyte cards with a four thousand token context. The LoRA paper's WikiSQL score for the full fine tune. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="MEMORY SIZE IS THE FIRST QUESTION",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Same board",
    art_at="Picture the vram",
    chips=[{"t": "4K", "c": "gold", "at": "Total VRAM in"}, {"t": "2 cards 4K", "c": "red", "at": "Generation rate on"}],
    stats=[{"v": "73.8", "u": "", "lab": "FT 73.8", "c": "cyan", "at": "The LoRA paper's"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with an eight thousand token context. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context. The LoRA paper's WikiSQL score for LoRA at rank four.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="MEMORY SIZE IS THE FIRST QUESTION",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="The vram figure",
    art_at="Picture the vram",
    chain=[{"t": "8K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 2 cards 128K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of LO 89.5, taken on the board.", "at": "The LoRA paper's"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One capacity number, one source, one board. Picture the window and what is in it. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. The LoRA paper's MNLI score for the full fine tune. One method, every row.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="MEMORY SIZE IS THE FIRST QUESTION",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="One capacity number",
    art_at="Picture the window",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "gold", "at": "Generation rate on"}, {"rank": "2", "name": "GPT-3 175B", "val": "73.4", "sub": "FT 73.4", "cls": "", "at": "The LoRA paper's"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="MEMORY SIZE IS THE FIRST QUESTION",
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
    title="MEMORY SIZE IS THE FIRST QUESTION",
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
    title="MEMORY SIZE IS THE FIRST QUESTION",
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
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Muse Glimmer 30B. The movement in FLAN v2 between the full fine tune and QLoRA. The line reads twenty gigabytes, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="MEMORY SIZE IS THE FIRST QUESTION",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Muse Glimmer 30B",
    blurb="The movement in FLAN v2 between the full fine tune and QLoRA",
    meta="256K &middot; 20 GB",
    name_at="On the bench",
    blurb_at="The movement in",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The capacity number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the vram budget figure, the context budget figure, the paper budget figure.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="MEMORY SIZE IS THE FIRST QUESTION",
    header_at="The capacity number",
    items=[{"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}, {"key": "folder", "label": "paper budget", "at": "the paper budget figure"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. The card's memory size decides which models you can even consider, so it sets the ceiling on what every other feature can do. MEMORY SIZE IS THE FIRST QUESTION.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="MEMORY SIZE IS THE FIRST QUESTION",
    sub="The card's memory size decides which models you can even consider, so it sets the ceiling on what every other feature can do.",
    art="folder",
    head_at="MEMORY SIZE IS THE FIRST QUESTION",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="nodes",
    vo="The papers figure, read straight off the board. Picture the paper folder. The model in the demonstration that made the technique famous. The size of the card in that demonstration. Total VRAM in use with a four thousand token context.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="MEMORY SIZE IS THE FIRST QUESTION",
    header_at="The papers figure",
    art="folder",
    art_caption="THE PAPER FOLDER",
    art_at="Picture the paper",
    chain=[{"t": "MODEL", "s": "This figure does not establish that a model fits.", "at": "The model in"}, {"t": "CARD", "s": "This figure does not establish a speed.", "at": "The size of"}, {"t": "4K", "s": "This figure does not establish a fit claim.", "at": "Total VRAM in"}],
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; 65b on one 48 gb card",
)

NAME = "BYTE-GEN-HW-007"
TITLE = "MEMORY SIZE IS THE FIRST QUESTION"
DOC_TITLE = "MEMORY SIZE IS THE FIRST QUESTION &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
