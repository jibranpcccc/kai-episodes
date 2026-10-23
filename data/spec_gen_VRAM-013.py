# -*- coding: utf-8 -*-
"""Generated from angle VRAM-013 -- TWO MODELS, ONE CARD, HALF EACH.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py VRAM-013
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same vram. Picture the vram sticks. Total VRAM in use with a four thousand token context. Generation rate on two sixteen gigabyte cards with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TWO MODELS, ONE CARD, HALF EACH",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Same board",
    art_at="Picture the vram",
    chips=[{"t": "4K", "c": "gold", "at": "Total VRAM in"}],
    stats=[{"v": "22.5", "u": "T/S", "lab": "2 cards 4K", "c": "red", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with an eight thousand token context. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TWO MODELS, ONE CARD, HALF EACH",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="The vram figure",
    art_at="Picture the vram",
    chain=[{"t": "8K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 2 cards 128K, taken on trust.", "at": "Generation rate on"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One capacity number, one source, one board. Picture the window and what is in it. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. Total VRAM in use with a thirty-two thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="TWO MODELS, ONE CARD, HALF EACH",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="One capacity number",
    art_at="Picture the window",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "gold", "at": "Generation rate on"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "20 GB", "sub": "32K", "cls": "", "at": "Total VRAM in"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a two hundred fifty-six thousand token context. Total VRAM in use with a four thousand token context. Total VRAM in use with a thirty-two thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TWO MODELS, ONE CARD, HALF EACH",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Nothing here about",
    art_at="Picture the vram",
    bars=[{"lab": "Qwen 3.8 27B", "val": "34", "unit": "GB", "pct": 100.0, "cls": "red", "at": "Total VRAM in use with a two"}, {"lab": "Muse Glimmer 30B", "val": "16", "unit": "GB", "pct": 47.1, "cls": "", "at": "Total VRAM in use with a four"}, {"lab": "Muse Glimmer 30B", "val": "16", "unit": "GB", "pct": 47.1, "cls": "", "at": "Total VRAM in use with a thirty-two"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a two hundred fifty-six thousand token context. Total VRAM in use with a four thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TWO MODELS, ONE CARD, HALF EACH",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="This is the",
    art_at="Picture the vram",
    rails=[{"lab": "256K", "val": "20", "pct": 58.8, "cls": "", "at": "Total VRAM in use with a two"}, {"lab": "4K", "val": "18", "pct": 52.9, "cls": "", "at": "Total VRAM in use with a four"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured capacity, on this board, in this run. Picture the window and what is in it. A pair of cards never buys speed. The wait before any word appears, not the total run. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="TWO MODELS, ONE CARD, HALF EACH",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="Measured capacity, on",
    art_at="Picture the window",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "A pair of cards never buys speed", "at": "A pair of"}, {"t": "The wait before any word appears, not the total run", "at": "The wait before"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every latency figure here carries its own source. Picture timing, line by line. On the bench: Qwen 3.8 27B. Total VRAM in use with a sixteen thousand token context. The line reads thirty-eight point one tokens per second, from the same run.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="TWO MODELS, ONE CARD, HALF EACH",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Every latency figure",
    art_at="Picture timing, line",
    name="Qwen 3.8 27B",
    blurb="Total VRAM in use with a sixteen thousand token context",
    meta="1 card 128K &middot; 38.1 T/S",
    name_at="On the bench",
    blurb_at="Total VRAM in",
    meta_at="The line reads",
    side="right",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="strip",
    vo="The capacity number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the vram budget figure, the context budget figure, the latency budget figure.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="TWO MODELS, ONE CARD, HALF EACH",
    header_at="The capacity number",
    items=[{"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. Running two models at once halves the memory each one gets, so concurrency on one card is a memory decision before it is a scheduling decision. TWO MODELS, ONE CARD, HALF EACH.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="TWO MODELS, ONE CARD, HALF EACH",
    sub="Running two models at once halves the memory each one gets, so concurrency on one card is a memory decision before it is a scheduling decision.",
    art="timer_flat",
    head_at="TWO MODELS, ONE CARD, HALF EACH",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-VRAM-013"
TITLE = "TWO MODELS, ONE CARD, HALF EACH"
DOC_TITLE = "TWO MODELS, ONE CARD, HALF EACH &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
