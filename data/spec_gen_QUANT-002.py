# -*- coding: utf-8 -*-
"""Generated from angle QUANT-002 -- FOUR BITS BUYS YOU THE CARD.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py QUANT-002
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same quant. Picture quantised in blocks. The size of the block scale in the four bit format. Total VRAM in use with a four thousand token context. Generation rate on two sixteen gigabyte cards with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="FOUR BITS BUYS YOU THE CARD",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="Same board",
    art_at="Picture quantised in",
    chips=[{"t": "32 BIT", "c": "gold", "at": "The size of"}, {"t": "4K", "c": "cyan", "at": "Total VRAM in"}],
    stats=[{"v": "22.5", "u": "T/S", "lab": "2 cards 4K", "c": "red", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="chain",
    vo="The quant figure, read straight off the board. Picture quantised in blocks. The overhead the block scales add per weight. Total VRAM in use with an eight thousand token context. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="FOUR BITS BUYS YOU THE CARD",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="The quant figure",
    art_at="Picture quantised in",
    chain=[{"t": "+0.5 BIT", "s": "This figure does not establish that a model fits.", "at": "The overhead the"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 8K, taken on trust.", "at": "Total VRAM in"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 2 cards 128K, taken on the board.", "at": "Generation rate on"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a sixteen thousand token context. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. Total VRAM in use with a thirty-two thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="FOUR BITS BUYS YOU THE CARD",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "gold", "at": "Total VRAM in use with a sixteen"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "red", "at": "Generation rate on"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "20 GB", "sub": "32K", "cls": "", "at": "Total VRAM in use with a thirty-two"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="FOUR BITS BUYS YOU THE CARD",
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
    title="FOUR BITS BUYS YOU THE CARD",
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
    title="FOUR BITS BUYS YOU THE CARD",
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
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Qwen 3.8 27B. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context. The line reads four point one two seven, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="FOUR BITS BUYS YOU THE CARD",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Qwen 3.8 27B",
    blurb="Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context",
    meta="EFFECTIVE &middot; 4.127",
    name_at="On the bench",
    blurb_at="Generation rate on",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the quant budget figure, the vram budget figure, the context budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="FOUR BITS BUYS YOU THE CARD",
    header_at="The vram number",
    items=[{"key": "gguf_blocks", "label": "quant budget", "at": "the quant budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="title",
    vo="One claim, one board, one run. Quantizing to four bits roughly halves the weights, so a model that missed the card by a gigabyte now fits. FOUR BITS BUYS YOU THE CARD.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="FOUR BITS BUYS YOU THE CARD",
    sub="Quantizing to four bits roughly halves the weights, so a model that missed the card by a gigabyte now fits.",
    art="context_window",
    head_at="FOUR BITS BUYS YOU THE CARD",
    source="the documented bits and bytes route &middot; nested quantization",
)

NAME = "BYTE-GEN-QUANT-002"
TITLE = "FOUR BITS BUYS YOU THE CARD"
DOC_TITLE = "FOUR BITS BUYS YOU THE CARD &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
