# -*- coding: utf-8 -*-
"""Generated from angle PA-005 -- SCORES DO NOT MEAN MUCH AT 32K.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PA-005
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same papers. Picture the paper folder. The LoRA paper's WikiSQL score for the full fine tune. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="SCORES DO NOT MEAN MUCH AT 32K",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Same board",
    art_at="Picture the paper",
    chips=[{"t": "FT 73.8", "c": "gold", "at": "The LoRA paper's"}],
    stats=[{"v": "288", "u": "MiB", "lab": "8,192 TOKENS", "c": "red", "at": "The key value"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="chain",
    vo="The papers figure, read straight off the board. Picture the paper folder. The LoRA paper's WikiSQL score for LoRA at rank four. The same cache in decimal gigabytes. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="SCORES DO NOT MEAN MUCH AT 32K",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="The papers figure",
    art_at="Picture the paper",
    chain=[{"t": "LO 89.5", "s": "This figure does not establish that a model fits.", "at": "The LoRA paper's"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 0.302 GB, taken on trust.", "at": "The same cache"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 2 cards 128K, taken on the board.", "at": "Generation rate on"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="rows",
    vo="One cache number, one source, one board. Picture the key-value ledger. The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="SCORES DO NOT MEAN MUCH AT 32K",
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
    vo="Nothing here about capacity is a guess. Picture the window and what is in it. Generation rate on two sixteen gigabyte cards with a four thousand token context. The same cache in decimal gigabytes. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="SCORES DO NOT MEAN MUCH AT 32K",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="Nothing here about",
    art_at="Picture the window",
    bars=[{"lab": "Qwen 3.8 27B", "val": "22.5", "unit": "T/S", "pct": 59.1, "cls": "red", "at": "Generation rate on"}, {"lab": "Qwen2.5 3B Instruct", "val": "0.302", "unit": "GB", "pct": 100.0, "cls": "red", "at": "The same cache"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the capacity of the hardware, not of the brochure. Picture the window and what is in it. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="SCORES DO NOT MEAN MUCH AT 32K",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="This is the",
    art_at="Picture the window",
    rails=[{"lab": "1 card 128K", "val": "38.1", "pct": 100.0, "cls": "red", "at": "Generation rate on"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured cache, on this board, in this run. Picture the key-value ledger. One number, one config, one precision. A pair of cards never buys speed. Decimal gigabytes, not binary ones. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="SCORES DO NOT MEAN MUCH AT 32K",
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
    vo="Every papers figure here carries its own source. Picture the paper folder. On the bench: Llama 65B. The LoRA paper's WikiSQL score for the full fine tune. The line reads two hundred and eighty-eight mebibytes, from the same run.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="SCORES DO NOT MEAN MUCH AT 32K",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Every papers figure",
    art_at="Picture the paper",
    name="Llama 65B",
    blurb="The LoRA paper's WikiSQL score for the full fine tune",
    meta="8,192 TOKENS &middot; 288 MiB",
    name_at="On the bench",
    blurb_at="The LoRA paper's",
    meta_at="The line reads",
    side="right",
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; 65b on one 48 gb card",
)

win(
    layout="strip",
    vo="The cache number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the paper budget figure, the cache budget figure, the context budget figure.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="SCORES DO NOT MEAN MUCH AT 32K",
    header_at="The cache number",
    items=[{"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="title",
    vo="One claim, one board, one run. Reported quality scores on multiple-choice benchmarks do not predict behavior on the long prompts where context length matters. SCORES DO NOT MEAN MUCH AT 32K.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="SCORES DO NOT MEAN MUCH AT 32K",
    sub="Reported quality scores on multiple-choice benchmarks do not predict behavior on the long prompts where context length matters.",
    art="context_window",
    head_at="SCORES DO NOT MEAN MUCH AT 32K",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="nodes",
    vo="The capacity figure, read straight off the board. Picture the window and what is in it. Generation rate on two sixteen gigabyte cards with a four thousand token context. The LoRA paper's WikiSQL score for LoRA at rank four. The same cache in decimal gigabytes.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="SCORES DO NOT MEAN MUCH AT 32K",
    header_at="The capacity figure",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    art_at="Picture the window",
    chain=[{"t": "2 cards 4K", "s": "A pair of cards never buys speed", "at": "Generation rate on"}, {"t": "LO 89.5", "s": "This figure does not establish a speed.", "at": "The LoRA paper's"}, {"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-PA-005"
TITLE = "SCORES DO NOT MEAN MUCH AT 32K"
DOC_TITLE = "SCORES DO NOT MEAN MUCH AT 32K &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
