# -*- coding: utf-8 -*-
"""Generated from angle VRAM-012 -- THE MEMORY YOU CAN DELETE.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py VRAM-012
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same vram. Picture the vram sticks. Total VRAM in use with a four thousand token context. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE MEMORY YOU CAN DELETE",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Same board",
    art_at="Picture the vram",
    chips=[{"t": "4K", "c": "gold", "at": "Total VRAM in"}],
    stats=[{"v": "288", "u": "MiB", "lab": "8,192 TOKENS", "c": "red", "at": "The key value"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with an eight thousand token context. The same cache in decimal gigabytes. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE MEMORY YOU CAN DELETE",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="The vram figure",
    art_at="Picture the vram",
    chain=[{"t": "8K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 0.302 GB, taken on trust.", "at": "The same cache"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 2 cards 128K, taken on the board.", "at": "Generation rate on"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One cache number, one source, one board. Picture the key-value ledger. The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="THE MEMORY YOU CAN DELETE",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="One cache number",
    art_at="Picture the key-value",
    rows=[{"rank": "1", "name": "Qwen2.5 3B Instruct", "val": "153 MiB", "sub": "Q8_0 PAYLOAD", "cls": "gold", "at": "The same cache"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "red", "at": "Generation rate on"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; q8_0 34 bytes per 32 values",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a sixty-four thousand token context. The cache for a single request in flight. Total VRAM in use with a one hundred twenty-eight thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE MEMORY YOU CAN DELETE",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Nothing here about",
    art_at="Picture the vram",
    bars=[{"lab": "Qwen 3.8 27B", "val": "22", "unit": "GB", "pct": 64.7, "cls": "", "at": "Total VRAM in use with a sixty-four"}, {"lab": "Qwen2.5 3B Instruct", "val": "288", "unit": "MiB", "pct": 25.0, "cls": "red", "at": "The cache for"}, {"lab": "Qwen 3.8 27B", "val": "26", "unit": "GB", "pct": 76.5, "cls": "", "at": "Total VRAM in use with a one"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a two hundred fifty-six thousand token context. The cache for four requests in flight. Total VRAM in use with a four thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE MEMORY YOU CAN DELETE",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="This is the",
    art_at="Picture the vram",
    rails=[{"lab": "256K", "val": "34", "pct": 100.0, "cls": "red", "at": "Total VRAM in use with a two"}, {"lab": "4 REQUESTS", "val": "1152", "pct": 100.0, "cls": "red", "at": "The cache for"}, {"lab": "4K", "val": "16", "pct": 47.1, "cls": "", "at": "Total VRAM in use with a four"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured cache, on this board, in this run. Picture the key-value ledger. One number, one config, one precision. A pair of cards never buys speed. Decimal gigabytes, not binary ones. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="THE MEMORY YOU CAN DELETE",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Measured cache, on",
    art_at="Picture the key-value",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "One number, one config, one precision", "at": "One number, one"}, {"t": "A pair of cards never buys speed", "at": "A pair of"}, {"t": "Decimal gigabytes, not binary ones", "at": "Decimal gigabytes, not"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Qwen 3.8 27B. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. The line reads twenty-two point five tokens per second, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE MEMORY YOU CAN DELETE",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Qwen 3.8 27B",
    blurb="The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision",
    meta="2 cards 4K &middot; 22.5 T/S",
    name_at="On the bench",
    blurb_at="The key value",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The cache number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the vram budget figure, the cache budget figure, the context budget figure.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="THE MEMORY YOU CAN DELETE",
    header_at="The cache number",
    items=[{"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. A model's memory footprint can be reduced by nearly half without touching the weights at all, by shrinking what the runtime keeps resident. THE MEMORY YOU CAN DELETE.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="THE MEMORY YOU CAN DELETE",
    sub="A model's memory footprint can be reduced by nearly half without touching the weights at all, by shrinking what the runtime keeps resident.",
    art="context_window",
    head_at="THE MEMORY YOU CAN DELETE",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="nodes",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with an eight thousand token context. The same cache in decimal gigabytes. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE MEMORY YOU CAN DELETE",
    header_at="The vram figure",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    art_at="Picture the vram",
    chain=[{"t": "8K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}, {"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}, {"t": "2 cards 128K", "s": "A pair of cards never buys speed", "at": "Generation rate on"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-VRAM-012"
TITLE = "THE MEMORY YOU CAN DELETE"
DOC_TITLE = "THE MEMORY YOU CAN DELETE &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
