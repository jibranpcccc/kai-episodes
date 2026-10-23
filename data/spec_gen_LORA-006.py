# -*- coding: utf-8 -*-
"""Generated from angle LORA-006 -- RANK COSTS MEMORY ON EVERY TOKEN.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py LORA-006
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same lora. Picture the magnifier pass. The layer count of the model. Total VRAM in use with a four thousand token context. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="RANK COSTS MEMORY ON EVERY TOKEN",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="Same board",
    art_at="Picture the magnifier",
    chips=[{"t": "LAYERS", "c": "gold", "at": "The layer count"}, {"t": "4K", "c": "cyan", "at": "Total VRAM in"}],
    stats=[{"v": "288", "u": "MiB", "lab": "8,192 TOKENS", "c": "red", "at": "The key value"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="chain",
    vo="The lora figure, read straight off the board. Picture the magnifier pass. The number of key value heads, shared across groups. Total VRAM in use with an eight thousand token context. The same cache in decimal gigabytes. The width of one attention head.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="RANK COSTS MEMORY ON EVERY TOKEN",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="The lora figure",
    art_at="Picture the magnifier",
    chain=[{"t": "KV HEADS", "s": "This figure does not establish that a model fits.", "at": "The number of"}, {"t": "8K", "s": "This figure does not establish a speed.", "at": "Total VRAM in"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 0.302 GB, taken on trust.", "at": "The same cache"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of HEAD DIM, taken on the board.", "at": "The width of"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a sixteen thousand token context. The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values. The hidden width of the model. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="RANK COSTS MEMORY ON EVERY TOKEN",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "gold", "at": "Total VRAM in"}, {"rank": "2", "name": "Qwen2.5 3B Instruct", "val": "153 MiB", "sub": "Q8_0 PAYLOAD", "cls": "red", "at": "The same cache"}, {"rank": "3", "name": "Qwen2.5 3B Instruct", "val": "2048", "sub": "HIDDEN", "cls": "", "at": "The hidden width"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about cache is a guess. Picture the key-value ledger. The cache for two requests in flight. Total VRAM in use with a two hundred fifty-six thousand token context. The cache for four requests in flight. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="RANK COSTS MEMORY ON EVERY TOKEN",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Nothing here about",
    art_at="Picture the key-value",
    bars=[{"lab": "Qwen2.5 3B Instruct", "val": "576", "unit": "MiB", "pct": 50.0, "cls": "red", "at": "The cache for two"}, {"lab": "Qwen 3.8 27B", "val": "34", "unit": "GB", "pct": 100.0, "cls": "red", "at": "Total VRAM in"}, {"lab": "Qwen2.5 3B Instruct", "val": "1152", "unit": "MiB", "pct": 100.0, "cls": "red", "at": "The cache for four"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request &middot; multiplied by the requests in flight",
)

win(
    layout="rail",
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="RANK COSTS MEMORY ON EVERY TOKEN",
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
    vo="Measured cache, on this board, in this run. Picture the key-value ledger. One number, one config, one precision. Decimal gigabytes, not binary ones. A rounded cache changes what the model reads back. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="RANK COSTS MEMORY ON EVERY TOKEN",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Measured cache, on",
    art_at="Picture the key-value",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "One number, one config, one precision", "at": "One number, one"}, {"t": "Decimal gigabytes, not binary ones", "at": "Decimal gigabytes, not"}, {"t": "A rounded cache changes what the model reads back", "at": "A rounded cache"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every lora figure here carries its own source. Picture the magnifier pass. On the bench: Qwen2.5 3B Instruct. Total VRAM in use with a four thousand token context. The line reads thirty-six thousand eight hundred and sixty-four, from the same run.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="RANK COSTS MEMORY ON EVERY TOKEN",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="Every lora figure",
    art_at="Picture the magnifier",
    name="Qwen2.5 3B Instruct",
    blurb="Total VRAM in use with a four thousand token context",
    meta="VALUE &middot; 36864",
    name_at="On the bench",
    blurb_at="Total VRAM in",
    meta_at="The line reads",
    side="right",
    source="derived &middot; rank 16 &middot; qwen2.5 3b instruct",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the adapter budget figure, the vram budget figure, the cache budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="RANK COSTS MEMORY ON EVERY TOKEN",
    header_at="The vram number",
    items=[{"key": "magnifier", "label": "adapter budget", "at": "the adapter budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="title",
    vo="One claim, one board, one run. A higher adapter rank costs more memory at inference for a small quality gain, so the cheapest useful rank is rarely the lowest one. RANK COSTS MEMORY ON EVERY TOKEN.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="RANK COSTS MEMORY ON EVERY TOKEN",
    sub="A higher adapter rank costs more memory at inference for a small quality gain, so the cheapest useful rank is rarely the lowest one.",
    art="kv_cache",
    head_at="RANK COSTS MEMORY ON EVERY TOKEN",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="nodes",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. The added parameters in one layer at rank sixteen. Total VRAM in use with a sixty-four thousand token context.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="RANK COSTS MEMORY ON EVERY TOKEN",
    header_at="The vram figure",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    art_at="Picture the vram",
    chain=[{"t": "32K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in use with a thirty-two"}, {"t": "PER LAYER", "s": "This figure does not establish a speed.", "at": "The added parameters"}, {"t": "64K", "s": "This figure does not establish a fit claim.", "at": "Total VRAM in use with a sixty-four"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-LORA-006"
TITLE = "RANK COSTS MEMORY ON EVERY TOKEN"
DOC_TITLE = "RANK COSTS MEMORY ON EVERY TOKEN &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
