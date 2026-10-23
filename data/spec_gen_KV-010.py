# -*- coding: utf-8 -*-
"""Generated from angle KV-010 -- CONTEXT NUMBERS ARE NOT COMPARABLE.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py KV-010
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same cache. Picture the key-value ledger. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Generation rate on two sixteen gigabyte cards with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="CONTEXT NUMBERS ARE NOT COMPARABLE",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Same board",
    art_at="Picture the key-value",
    chips=[{"t": "8,192 TOKENS", "c": "gold", "at": "The key value"}],
    stats=[{"v": "22.5", "u": "T/S", "lab": "2 cards 4K", "c": "red", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="chain",
    vo="The cache figure, read straight off the board. Picture the key-value ledger. The same cache in decimal gigabytes. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context. The LoRA paper's WikiSQL score for LoRA at rank four.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="CONTEXT NUMBERS ARE NOT COMPARABLE",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="The cache figure",
    art_at="Picture the key-value",
    chain=[{"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 2 cards 128K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of LO 89.5, taken on the board.", "at": "The LoRA paper's"}],
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

win(
    layout="rows",
    vo="One capacity number, one source, one board. Picture the window and what is in it. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. The LoRA paper's MNLI score for the full fine tune. One method, every row.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="CONTEXT NUMBERS ARE NOT COMPARABLE",
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
    vo="Nothing here about capacity is a guess. Picture the window and what is in it. Generation rate on two sixteen gigabyte cards with a four thousand token context. The same cache in decimal gigabytes. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="CONTEXT NUMBERS ARE NOT COMPARABLE",
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
    title="CONTEXT NUMBERS ARE NOT COMPARABLE",
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
    title="CONTEXT NUMBERS ARE NOT COMPARABLE",
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
    vo="Every papers figure here carries its own source. Picture the paper folder. On the bench: Llama 65B. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. The line reads twenty-two point five tokens per second, from the same run.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="CONTEXT NUMBERS ARE NOT COMPARABLE",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Every papers figure",
    art_at="Picture the paper",
    name="Llama 65B",
    blurb="The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision",
    meta="2 cards 4K &middot; 22.5 T/S",
    name_at="On the bench",
    blurb_at="The key value",
    meta_at="The line reads",
    side="right",
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; 65b on one 48 gb card",
)

win(
    layout="strip",
    vo="The capacity number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the cache budget figure, the context budget figure, the paper budget figure.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="CONTEXT NUMBERS ARE NOT COMPARABLE",
    header_at="The capacity number",
    items=[{"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}, {"key": "folder", "label": "paper budget", "at": "the paper budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="title",
    vo="One claim, one board, one run. A model with a smaller advertised window can be the better local choice if its cache is smaller per token, so context numbers are not comparable across models. CONTEXT NUMBERS ARE NOT COMPARABLE.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="CONTEXT NUMBERS ARE NOT COMPARABLE",
    sub="A model with a smaller advertised window can be the better local choice if its cache is smaller per token, so context numbers are not comparable across models.",
    art="folder",
    head_at="CONTEXT NUMBERS ARE NOT COMPARABLE.",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="nodes",
    vo="The papers figure, read straight off the board. Picture the paper folder. The LoRA paper's WikiSQL score for the full fine tune. The same cache in decimal gigabytes. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="CONTEXT NUMBERS ARE NOT COMPARABLE",
    header_at="The papers figure",
    art="folder",
    art_caption="THE PAPER FOLDER",
    art_at="Picture the paper",
    chain=[{"t": "FT 73.8", "s": "This figure does not establish that a model fits.", "at": "The LoRA paper's"}, {"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}, {"t": "2 cards 128K", "s": "A pair of cards never buys speed", "at": "Generation rate on"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

NAME = "BYTE-GEN-KV-010"
TITLE = "CONTEXT NUMBERS ARE NOT COMPARABLE"
DOC_TITLE = "CONTEXT NUMBERS ARE NOT COMPARABLE &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
