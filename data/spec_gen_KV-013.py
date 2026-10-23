# -*- coding: utf-8 -*-
"""Generated from angle KV-013 -- MAXIMUM CONTEXT IS A MEMORY CLAIM.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py KV-013
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same cache. Picture the key-value ledger. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. The LoRA paper's WikiSQL score for the full fine tune. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="MAXIMUM CONTEXT IS A MEMORY CLAIM",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Same board",
    art_at="Picture the key-value",
    chips=[{"t": "8,192 TOKENS", "c": "gold", "at": "The key value"}],
    stats=[{"v": "73.8", "u": "", "lab": "FT 73.8", "c": "gold", "at": "The LoRA paper's"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="chain",
    vo="The cache figure, read straight off the board. Picture the key-value ledger. The same cache in decimal gigabytes. The LoRA paper's WikiSQL score for LoRA at rank four. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="MAXIMUM CONTEXT IS A MEMORY CLAIM",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="The cache figure",
    art_at="Picture the key-value",
    chain=[{"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about LO 89.5, taken on trust.", "at": "The LoRA paper's"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 2 cards 128K, taken on the board.", "at": "Generation rate on"}],
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

win(
    layout="rows",
    vo="One papers number, one source, one board. Picture the paper folder. The LoRA paper's MNLI score for the full fine tune. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="MAXIMUM CONTEXT IS A MEMORY CLAIM",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="One papers number",
    art_at="Picture the paper",
    rows=[{"rank": "1", "name": "GPT-3 175B", "val": "73.4", "sub": "FT 73.4", "cls": "gold", "at": "The LoRA paper's"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "red", "at": "Generation rate on"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="bars",
    vo="Nothing here about capacity is a guess. Picture the window and what is in it. Generation rate on two sixteen gigabyte cards with a four thousand token context. The same cache in decimal gigabytes. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="MAXIMUM CONTEXT IS A MEMORY CLAIM",
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
    title="MAXIMUM CONTEXT IS A MEMORY CLAIM",
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
    title="MAXIMUM CONTEXT IS A MEMORY CLAIM",
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
    vo="Every papers figure here carries its own source. Picture the paper folder. On the bench: Llama 65B. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. The line reads seventy-three point eight, from the same run.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="MAXIMUM CONTEXT IS A MEMORY CLAIM",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Every papers figure",
    art_at="Picture the paper",
    name="Llama 65B",
    blurb="The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision",
    meta="FT 73.8 &middot; 73.8",
    name_at="On the bench",
    blurb_at="The key value",
    meta_at="The line reads",
    side="right",
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; 65b on one 48 gb card",
)

win(
    layout="strip",
    vo="The papers number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the cache budget figure, the paper budget figure, the context budget figure.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="MAXIMUM CONTEXT IS A MEMORY CLAIM",
    header_at="The papers number",
    items=[{"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="title",
    vo="One claim, one board, one run. The advertised maximum context is a hardware statement about memory, not a claim that the model will attend to all of it. MAXIMUM CONTEXT IS A MEMORY CLAIM.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="MAXIMUM CONTEXT IS A MEMORY CLAIM",
    sub="The advertised maximum context is a hardware statement about memory, not a claim that the model will attend to all of it.",
    art="context_window",
    head_at="MAXIMUM CONTEXT IS A MEMORY CLAIM",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="nodes",
    vo="The capacity figure, read straight off the board. Picture the window and what is in it. Generation rate on two sixteen gigabyte cards with a four thousand token context. The same cache in decimal gigabytes. The LoRA paper's WikiSQL score for LoRA at rank four.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="MAXIMUM CONTEXT IS A MEMORY CLAIM",
    header_at="The capacity figure",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    art_at="Picture the window",
    chain=[{"t": "2 cards 4K", "s": "A pair of cards never buys speed", "at": "Generation rate on"}, {"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}, {"t": "LO 89.5", "s": "This figure does not establish a fit claim.", "at": "The LoRA paper's"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-KV-013"
TITLE = "MAXIMUM CONTEXT IS A MEMORY CLAIM"
DOC_TITLE = "MAXIMUM CONTEXT IS A MEMORY CLAIM &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
