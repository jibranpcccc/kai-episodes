# -*- coding: utf-8 -*-
"""Generated from angle KV-006 -- SPEED DROPS WHERE THE CACHE FILLS.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py KV-006
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same cache. Picture the key-value ledger. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Generation rate on a five-oh-ninety with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="SPEED DROPS WHERE THE CACHE FILLS",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Same board",
    art_at="Picture the key-value",
    chips=[{"t": "8,192 TOKENS", "c": "gold", "at": "The key value"}],
    stats=[{"v": "74.8", "u": "T/S", "lab": "4K", "c": "gold", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="chain",
    vo="The cache figure, read straight off the board. Picture the key-value ledger. The same cache in decimal gigabytes. Generation rate on a five-oh-ninety with a sixteen thousand token context. Total VRAM in use with an eight thousand token context.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="SPEED DROPS WHERE THE CACHE FILLS",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="The cache figure",
    art_at="Picture the key-value",
    chain=[{"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 8K, taken on the board.", "at": "Total VRAM in"}],
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

win(
    layout="rows",
    vo="One generation number, one source, one board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a thirty-two thousand token context. Total VRAM in use with a sixteen thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="SPEED DROPS WHERE THE CACHE FILLS",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="One generation number",
    art_at="Picture the tokens",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "gold", "at": "Generation rate on"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "", "at": "Total VRAM in"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. The cache for a single request in flight. Generation rate on a three thousand ninety with a four thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="SPEED DROPS WHERE THE CACHE FILLS",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Nothing here about",
    art_at="Picture the vram",
    bars=[{"lab": "Qwen 3.8 27B", "val": "20", "unit": "GB", "pct": 58.8, "cls": "", "at": "Total VRAM in"}, {"lab": "Qwen2.5 3B Instruct", "val": "288", "unit": "MiB", "pct": 25.0, "cls": "red", "at": "The cache for"}, {"lab": "Qwen 3.8 27B", "val": "40.3", "unit": "T/S", "pct": 100.0, "cls": "", "at": "Generation rate on"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the cache of the hardware, not of the brochure. Picture the key-value ledger. The cache for two requests in flight. Generation rate on a three thousand ninety with a thirty-two thousand token context. Total VRAM in use with a one hundred twenty-eight thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="SPEED DROPS WHERE THE CACHE FILLS",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="This is the",
    art_at="Picture the key-value",
    rails=[{"lab": "2 REQUESTS", "val": "576", "pct": 50.0, "cls": "red", "at": "The cache for"}, {"lab": "32K", "val": "37.0", "pct": 91.8, "cls": "", "at": "Generation rate on"}, {"lab": "128K", "val": "26", "pct": 76.5, "cls": "", "at": "Total VRAM in"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request &middot; multiplied by the requests in flight",
)

win(
    layout="note",
    vo="Measured cache, on this board, in this run. Picture the key-value ledger. One number, one config, one precision. Decimal gigabytes, not binary ones. A rounded cache changes what the model reads back. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="SPEED DROPS WHERE THE CACHE FILLS",
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
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Muse Glimmer 30B. Total VRAM in use with a thirty-two thousand token context. The line reads seventeen gigabytes, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="SPEED DROPS WHERE THE CACHE FILLS",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Muse Glimmer 30B",
    blurb="Total VRAM in use with a thirty-two thousand token context",
    meta="64K &middot; 17 GB",
    name_at="On the bench",
    blurb_at="Total VRAM in",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The generation number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the cache budget figure, the decode budget figure, the vram budget figure.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="SPEED DROPS WHERE THE CACHE FILLS",
    header_at="The generation number",
    items=[{"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="title",
    vo="One claim, one board, one run. Once the cache fills the card, generation stops being compute-bound and becomes memory-bound, so the speed penalty appears at a context threshold. SPEED DROPS WHERE THE CACHE FILLS.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="SPEED DROPS WHERE THE CACHE FILLS",
    sub="Once the cache fills the card, generation stops being compute-bound and becomes memory-bound, so the speed penalty appears at a context threshold.",
    art="vram_module",
    head_at="SPEED DROPS WHERE THE CACHE FILLS",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="nodes",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with a two hundred fifty-six thousand token context. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="SPEED DROPS WHERE THE CACHE FILLS",
    header_at="The vram figure",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    art_at="Picture the vram",
    chain=[{"t": "256K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}, {"t": "8,192 TOKENS", "s": "One number, one config, one precision", "at": "The key value"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-KV-006"
TITLE = "SPEED DROPS WHERE THE CACHE FILLS"
DOC_TITLE = "SPEED DROPS WHERE THE CACHE FILLS &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
