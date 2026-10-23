# -*- coding: utf-8 -*-
"""Generated from angle GEN-001 -- TOKENS PER SECOND IS NOT A CARD NUMBER.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py GEN-001
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same generation. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a four thousand token context. Total VRAM in use with a four thousand token context. Generation rate on a five-oh-ninety with a sixteen thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="TOKENS PER SECOND IS NOT A CARD NUMBER",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Same board",
    art_at="Picture the tokens",
    chips=[{"t": "4K", "c": "gold", "at": "Generation rate on a five-oh-ninety with a four"}, {"t": "4K", "c": "cyan", "at": "Total VRAM in"}],
    stats=[{"v": "52.2", "u": "T/S", "lab": "16K", "c": "cyan", "at": "Generation rate on a five-oh-ninety with a sixteen"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with an eight thousand token context. Generation rate on a five-oh-ninety with a thirty-two thousand token context. Total VRAM in use with a sixteen thousand token context.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TOKENS PER SECOND IS NOT A CARD NUMBER",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="The vram figure",
    art_at="Picture the vram",
    chain=[{"t": "8K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in use with an"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 32K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 16K, taken on the board.", "at": "Total VRAM in use with a sixteen"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Generation rate on a three thousand ninety with a four thousand token context. Total VRAM in use with a sixty-four thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TOKENS PER SECOND IS NOT A CARD NUMBER",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "20 GB", "sub": "32K", "cls": "gold", "at": "Total VRAM in use with a thirty-two"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "40.3 T/S", "sub": "4K", "cls": "", "at": "Generation rate on"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "22 GB", "sub": "64K", "cls": "", "at": "Total VRAM in use with a sixty-four"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a one hundred twenty-eight thousand token context. Generation rate on a three thousand ninety with a sixty-four thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TOKENS PER SECOND IS NOT A CARD NUMBER",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Nothing here about",
    art_at="Picture the vram",
    bars=[{"lab": "Qwen 3.8 27B", "val": "26", "unit": "GB", "pct": 76.5, "cls": "", "at": "Total VRAM in"}, {"lab": "Qwen 3.8 27B", "val": "33.9", "unit": "T/S", "pct": 84.1, "cls": "", "at": "Generation rate on"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TOKENS PER SECOND IS NOT A CARD NUMBER",
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
    title="TOKENS PER SECOND IS NOT A CARD NUMBER",
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
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Qwen 3.8 27B. Generation rate on a five-oh-ninety with a sixteen thousand token context. The line reads eighteen gigabytes, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TOKENS PER SECOND IS NOT A CARD NUMBER",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Qwen 3.8 27B",
    blurb="Generation rate on a five-oh-ninety with a sixteen thousand token context",
    meta="8K &middot; 18 GB",
    name_at="On the bench",
    blurb_at="Generation rate on",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the decode budget figure, the vram budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TOKENS PER SECOND IS NOT A CARD NUMBER",
    header_at="The vram number",
    items=[{"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. Tokens per second is a function of model size and memory bandwidth, and card marketing numbers describe neither of those. TOKENS PER SECOND IS NOT A CARD NUMBER.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="TOKENS PER SECOND IS NOT A CARD NUMBER",
    sub="Tokens per second is a function of model size and memory bandwidth, and card marketing numbers describe neither of those.",
    art="token_blocks",
    head_at="TOKENS PER SECOND IS NOT A CARD NUMBER",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-GEN-001"
TITLE = "TOKENS PER SECOND IS NOT A CARD NUMBER"
DOC_TITLE = "TOKENS PER SECOND IS NOT A CARD NUMBER &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
