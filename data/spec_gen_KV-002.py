# -*- coding: utf-8 -*-
"""Generated from angle KV-002 -- CACHE SIZE GROWS WITH DEPTH.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py KV-002
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same cache. Picture the key-value ledger. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Total VRAM in use with a four thousand token context. The same cache in decimal gigabytes. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="CACHE SIZE GROWS WITH DEPTH",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Same board",
    art_at="Picture the key-value",
    chips=[{"t": "8,192 TOKENS", "c": "gold", "at": "The key value"}, {"t": "4K", "c": "cyan", "at": "Total VRAM in"}],
    stats=[{"v": "0.302", "u": "GB", "lab": "0.302 GB", "c": "red", "at": "The same cache"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="chain",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with an eight thousand token context. The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values. Total VRAM in use with a sixteen thousand token context.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="CACHE SIZE GROWS WITH DEPTH",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="The vram figure",
    art_at="Picture the vram",
    chain=[{"t": "8K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in use with an"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about Q8_0 PAYLOAD, taken on trust.", "at": "The same cache"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 16K, taken on the board.", "at": "Total VRAM in use with a sixteen"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. The cache for a single request in flight. Total VRAM in use with a sixty-four thousand token context. The cache for two requests in flight. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="CACHE SIZE GROWS WITH DEPTH",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "20 GB", "sub": "32K", "cls": "gold", "at": "Total VRAM in use with a thirty-two"}, {"rank": "2", "name": "Qwen2.5 3B Instruct", "val": "288 MiB", "sub": "1 REQUEST", "cls": "red", "at": "The cache for a"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "22 GB", "sub": "64K", "cls": "", "at": "Total VRAM in use with a sixty-four"}, {"rank": "4", "name": "Qwen2.5 3B Instruct", "val": "576 MiB", "sub": "2 REQUESTS", "cls": "red", "at": "The cache for two"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a one hundred twenty-eight thousand token context. The cache for four requests in flight. Total VRAM in use with a two hundred fifty-six thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="CACHE SIZE GROWS WITH DEPTH",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Nothing here about",
    art_at="Picture the vram",
    bars=[{"lab": "Qwen 3.8 27B", "val": "26", "unit": "GB", "pct": 76.5, "cls": "", "at": "Total VRAM in use with a one"}, {"lab": "Qwen2.5 3B Instruct", "val": "1152", "unit": "MiB", "pct": 100.0, "cls": "red", "at": "The cache for"}, {"lab": "Qwen 3.8 27B", "val": "34", "unit": "GB", "pct": 100.0, "cls": "red", "at": "Total VRAM in use with a two"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="CACHE SIZE GROWS WITH DEPTH",
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
    title="CACHE SIZE GROWS WITH DEPTH",
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
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Qwen 3.8 27B. The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values. The line reads nineteen gigabytes, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="CACHE SIZE GROWS WITH DEPTH",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Qwen 3.8 27B",
    blurb="The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values",
    meta="16K &middot; 19 GB",
    name_at="On the bench",
    blurb_at="The same cache",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the cache budget figure, the vram budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="CACHE SIZE GROWS WITH DEPTH",
    header_at="The vram number",
    items=[{"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="title",
    vo="One claim, one board, one run. Cache memory scales with the number of layers as well as the context, so a model with fewer layers holds a smaller cache for the same context. CACHE SIZE GROWS WITH DEPTH.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="CACHE SIZE GROWS WITH DEPTH",
    sub="Cache memory scales with the number of layers as well as the context, so a model with fewer layers holds a smaller cache for the same context.",
    art="kv_cache",
    head_at="CACHE SIZE GROWS WITH DEPTH",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

NAME = "BYTE-GEN-KV-002"
TITLE = "CACHE SIZE GROWS WITH DEPTH"
DOC_TITLE = "CACHE SIZE GROWS WITH DEPTH &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
