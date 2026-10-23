# -*- coding: utf-8 -*-
"""Generated from angle PA-009 -- READ THE PAPER FOR WHAT IS MISSING.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PA-009
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same papers. Picture the paper folder. The LoRA paper's WikiSQL score for the full fine tune. Total VRAM in use with a four thousand token context. Generation rate on two sixteen gigabyte cards with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="READ THE PAPER FOR WHAT IS MISSING",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Same board",
    art_at="Picture the paper",
    chips=[{"t": "FT 73.8", "c": "gold", "at": "The LoRA paper's"}, {"t": "4K", "c": "cyan", "at": "Total VRAM in"}],
    stats=[{"v": "22.5", "u": "T/S", "lab": "2 cards 4K", "c": "red", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="chain",
    vo="The papers figure, read straight off the board. Picture the paper folder. The LoRA paper's WikiSQL score for LoRA at rank four. Total VRAM in use with an eight thousand token context. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="READ THE PAPER FOR WHAT IS MISSING",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="The papers figure",
    art_at="Picture the paper",
    chain=[{"t": "LO 89.5", "s": "This figure does not establish that a model fits.", "at": "The LoRA paper's"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 8K, taken on trust.", "at": "Total VRAM in"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 2 cards 128K, taken on the board.", "at": "Generation rate on"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a sixteen thousand token context. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. The LoRA paper's MNLI score for LoRA at rank four. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="READ THE PAPER FOR WHAT IS MISSING",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "gold", "at": "Total VRAM in"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "red", "at": "Generation rate on"}, {"rank": "3", "name": "GPT-3 175B", "val": "91.7", "sub": "LO 91.7", "cls": "", "at": "The LoRA paper's"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="READ THE PAPER FOR WHAT IS MISSING",
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
    title="READ THE PAPER FOR WHAT IS MISSING",
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
    title="READ THE PAPER FOR WHAT IS MISSING",
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
    vo="Every papers figure here carries its own source. Picture the paper folder. On the bench: Llama 7B. Total VRAM in use with a sixty-four thousand token context. The line reads sixty-five bytes, from the same run.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="READ THE PAPER FOR WHAT IS MISSING",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Every papers figure",
    art_at="Picture the paper",
    name="Llama 7B",
    blurb="Total VRAM in use with a sixty-four thousand token context",
    meta="MODEL &middot; 65 B",
    name_at="On the bench",
    blurb_at="Total VRAM in",
    meta_at="The line reads",
    side="right",
    source="the QLoRA paper &middot; percentage point movement &middot; FLAN v2",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the paper budget figure, the vram budget figure, the context budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="READ THE PAPER FOR WHAT IS MISSING",
    header_at="The vram number",
    items=[{"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="title",
    vo="One claim, one board, one run. The most useful thing about a papers page for a local builder is what it omits, because the omissions are the constraints you will hit. READ THE PAPER FOR WHAT IS MISSING.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="READ THE PAPER FOR WHAT IS MISSING",
    sub="The most useful thing about a papers page for a local builder is what it omits, because the omissions are the constraints you will hit.",
    art="context_window",
    head_at="READ THE PAPER FOR WHAT IS MISSING",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="nodes",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with a two hundred fifty-six thousand token context. The size of the card in that demonstration. The LoRA paper's WikiSQL score for the full fine tune.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="READ THE PAPER FOR WHAT IS MISSING",
    header_at="The vram figure",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    art_at="Picture the vram",
    chain=[{"t": "256K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}, {"t": "CARD", "s": "This figure does not establish a speed.", "at": "The size of"}, {"t": "FT 73.8", "s": "This figure does not establish a fit claim.", "at": "The LoRA paper's"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-PA-009"
TITLE = "READ THE PAPER FOR WHAT IS MISSING"
DOC_TITLE = "READ THE PAPER FOR WHAT IS MISSING &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
