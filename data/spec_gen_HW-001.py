# -*- coding: utf-8 -*-
"""Generated from angle HW-001 -- THE CARD IS ITS MEMORY SYSTEM.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py HW-001
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same vram. Picture the vram sticks. Total VRAM in use with a four thousand token context. Generation rate on a five-oh-ninety with a four thousand token context. Total VRAM in use with an eight thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE CARD IS ITS MEMORY SYSTEM",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Same board",
    art_at="Picture the vram",
    chips=[{"t": "4K", "c": "gold", "at": "Total VRAM in use with a four"}, {"t": "4K", "c": "cyan", "at": "Generation rate on"}],
    stats=[{"v": "18", "u": "GB", "lab": "8K", "c": "cyan", "at": "Total VRAM in use with an"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The generation figure, read straight off the board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a sixteen thousand token context. Total VRAM in use with a sixteen thousand token context. Generation rate on a five-oh-ninety with a thirty-two thousand token context.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE CARD IS ITS MEMORY SYSTEM",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="The generation figure",
    art_at="Picture the tokens",
    chain=[{"t": "16K", "s": "This figure does not establish that a model fits.", "at": "Generation rate on a five-oh-ninety with a sixteen"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Total VRAM in"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 32K, taken on the board.", "at": "Generation rate on a five-oh-ninety with a thirty-two"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One generation number, one source, one board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context. Total VRAM in use with a sixty-four thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE CARD IS ITS MEMORY SYSTEM",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="One generation number",
    art_at="Picture the tokens",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "22.8 T/S", "sub": "128K", "cls": "gold", "at": "Generation rate on"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "22 GB", "sub": "64K", "cls": "", "at": "Total VRAM in"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a three thousand ninety with a thirty-two thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE CARD IS ITS MEMORY SYSTEM",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Nothing here about",
    art_at="Picture the tokens",
    bars=[{"lab": "Qwen 3.8 27B", "val": "37.0", "unit": "T/S", "pct": 91.8, "cls": "", "at": "Generation rate on"}, {"lab": "Qwen 3.8 27B", "val": "34", "unit": "GB", "pct": 100.0, "cls": "red", "at": "Total VRAM in"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE CARD IS ITS MEMORY SYSTEM",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="This is the",
    art_at="Picture the vram",
    rails=[{"lab": "32K", "val": "16", "pct": 47.1, "cls": "", "at": "Total VRAM in use with a thirty-two"}, {"lab": "64K", "val": "17", "pct": 50.0, "cls": "", "at": "Total VRAM in use with a sixty-four"}, {"lab": "256K", "val": "20", "pct": 58.8, "cls": "", "at": "Total VRAM in use with a two"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured vram, on this board, in this run. Picture the vram sticks. Does not fit on a twenty-four gigabyte card at all. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE CARD IS ITS MEMORY SYSTEM",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Measured vram, on",
    art_at="Picture the vram",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "Does not fit on a twenty-four gigabyte card at all", "at": "Does not fit"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every generation figure here carries its own source. Picture the tokens, one by one. On the bench: Qwen 3.8 27B. Total VRAM in use with an eight thousand token context. The line reads fifty-two point two tokens per second, from the same run.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE CARD IS ITS MEMORY SYSTEM",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Every generation figure",
    art_at="Picture the tokens",
    name="Qwen 3.8 27B",
    blurb="Total VRAM in use with an eight thousand token context",
    meta="16K &middot; 52.2 T/S",
    name_at="On the bench",
    blurb_at="Total VRAM in",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The generation number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the vram budget figure, the decode budget figure.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE CARD IS ITS MEMORY SYSTEM",
    header_at="The generation number",
    items=[{"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. Two cards with the same memory size and different memory speeds give different token rates, which means the memory subsystem is the card. THE CARD IS ITS MEMORY SYSTEM.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE CARD IS ITS MEMORY SYSTEM",
    sub="Two cards with the same memory size and different memory speeds give different token rates, which means the memory subsystem is the card.",
    art="vram_module",
    head_at="THE CARD IS ITS MEMORY SYSTEM",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-HW-001"
TITLE = "THE CARD IS ITS MEMORY SYSTEM"
DOC_TITLE = "THE CARD IS ITS MEMORY SYSTEM &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
