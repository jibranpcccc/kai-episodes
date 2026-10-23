# -*- coding: utf-8 -*-
"""Generated from angle MU-006 -- TWO CARDS, ONE MEMORY BUS.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py MU-006
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same vram. Picture the vram sticks. Total VRAM in use with a four thousand token context. Generation rate on a five-oh-ninety with a four thousand token context. Generation rate on two sixteen gigabyte cards with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TWO CARDS, ONE MEMORY BUS",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Same board",
    art_at="Picture the vram",
    chips=[{"t": "4K", "c": "gold", "at": "Total VRAM in"}, {"t": "4K", "c": "cyan", "at": "Generation rate on a"}],
    stats=[{"v": "22.5", "u": "T/S", "lab": "2 cards 4K", "c": "red", "at": "Generation rate on two"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with an eight thousand token context. Generation rate on a five-oh-ninety with a sixteen thousand token context. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TWO CARDS, ONE MEMORY BUS",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="The vram figure",
    art_at="Picture the vram",
    chain=[{"t": "8K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Generation rate on a"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 2 cards 128K, taken on the board.", "at": "Generation rate on two"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One generation number, one source, one board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a thirty-two thousand token context. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="TWO CARDS, ONE MEMORY BUS",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="One generation number",
    art_at="Picture the tokens",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "gold", "at": "Generation rate on a"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "red", "at": "Generation rate on one"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a sixty-four thousand token context. Generation rate on a three thousand ninety with a four thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TWO CARDS, ONE MEMORY BUS",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Nothing here about",
    art_at="Picture the vram",
    bars=[{"lab": "Qwen 3.8 27B", "val": "22", "unit": "GB", "pct": 64.7, "cls": "", "at": "Total VRAM in"}, {"lab": "Qwen 3.8 27B", "val": "40.3", "unit": "T/S", "pct": 100.0, "cls": "", "at": "Generation rate on"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a two hundred fifty-six thousand token context. Generation rate on a three thousand ninety with a sixty-four thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TWO CARDS, ONE MEMORY BUS",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="This is the",
    art_at="Picture the vram",
    rails=[{"lab": "256K", "val": "34", "pct": 100.0, "cls": "red", "at": "Total VRAM in"}, {"lab": "64K", "val": "33.9", "pct": 84.1, "cls": "", "at": "Generation rate on"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured capacity, on this board, in this run. Picture the window and what is in it. A pair of cards never buys speed. One card is faster than two at the same context. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="TWO CARDS, ONE MEMORY BUS",
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
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Qwen 3.8 27B. Generation rate on a five-oh-ninety with a four thousand token context. The line reads twenty-two point five tokens per second, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TWO CARDS, ONE MEMORY BUS",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Qwen 3.8 27B",
    blurb="Generation rate on a five-oh-ninety with a four thousand token context",
    meta="2 cards 4K &middot; 22.5 T/S",
    name_at="On the bench",
    blurb_at="Generation rate on",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The generation number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the vram budget figure, the decode budget figure, the context budget figure.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="TWO CARDS, ONE MEMORY BUS",
    header_at="The generation number",
    items=[{"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. A second card in the same machine shares the host memory bus, so it adds capacity without adding bandwidth when the workload is memory-bound. TWO CARDS, ONE MEMORY BUS.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="TWO CARDS, ONE MEMORY BUS",
    sub="A second card in the same machine shares the host memory bus, so it adds capacity without adding bandwidth when the workload is memory-bound.",
    art="context_window",
    head_at="TWO CARDS, ONE MEMORY BUS",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="nodes",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with an eight thousand token context. Generation rate on a five-oh-ninety with a sixteen thousand token context. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TWO CARDS, ONE MEMORY BUS",
    header_at="The vram figure",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    art_at="Picture the vram",
    chain=[{"t": "8K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}, {"t": "16K", "s": "This figure does not establish a speed.", "at": "Generation rate on a"}, {"t": "2 cards 128K", "s": "A pair of cards never buys speed", "at": "Generation rate on two"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-MU-006"
TITLE = "TWO CARDS, ONE MEMORY BUS"
DOC_TITLE = "TWO CARDS, ONE MEMORY BUS &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
