# -*- coding: utf-8 -*-
"""Generated from angle KV-008 -- IT PREFILLED, THEN IT FAILED.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py KV-008
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same cache. Picture the key-value ledger. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Prompt processing rate on a four thousand token prompt. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="IT PREFILLED, THEN IT FAILED",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Same board",
    art_at="Picture the key-value",
    chips=[{"t": "8,192 TOKENS", "c": "gold", "at": "The key value"}],
    stats=[{"v": "4625", "u": "T/S", "lab": "4K", "c": "gold", "at": "Prompt processing rate"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="chain",
    vo="The cache figure, read straight off the board. Picture the key-value ledger. The same cache in decimal gigabytes. Prompt processing rate on a sixteen thousand token prompt. Total VRAM in use with an eight thousand token context. The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="IT PREFILLED, THEN IT FAILED",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="The cache figure",
    art_at="Picture the key-value",
    chain=[{"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache in"}, {"t": "16K", "s": "This figure does not establish a speed.", "at": "Prompt processing rate"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 8K, taken on trust.", "at": "Total VRAM in"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of Q8_0 PAYLOAD, taken on the board.", "at": "The same cache held"}],
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

win(
    layout="rows",
    vo="One prefill number, one source, one board. Picture the prompt, incoming. Prompt processing rate on a sixty-four thousand token prompt. Total VRAM in use with a sixteen thousand token context. The same cache held in four bit blocks, at eighteen bytes for every thirty-two values. One method, every row.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="IT PREFILLED, THEN IT FAILED",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="One prefill number",
    art_at="Picture the prompt",
    rows=[{"rank": "1", "name": "Muse Glimmer 30B", "val": "3606 T/S", "sub": "64K", "cls": "gold", "at": "Prompt processing rate"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "", "at": "Total VRAM in"}, {"rank": "3", "name": "Qwen2.5 3B Instruct", "val": "81 MiB", "sub": "Q4_0 PAYLOAD", "cls": "red", "at": "The same cache"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. The cache for a single request in flight. Prompt processing rate on a two hundred fifty-six thousand token prompt. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="IT PREFILLED, THEN IT FAILED",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Nothing here about",
    art_at="Picture the vram",
    bars=[{"lab": "Qwen 3.8 27B", "val": "20", "unit": "GB", "pct": 58.8, "cls": "", "at": "Total VRAM in"}, {"lab": "Qwen2.5 3B Instruct", "val": "288", "unit": "MiB", "pct": 25.0, "cls": "red", "at": "The cache for"}, {"lab": "Muse Glimmer 30B", "val": "1874", "unit": "T/S", "pct": 40.5, "cls": "", "at": "Prompt processing rate"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the cache of the hardware, not of the brochure. Picture the key-value ledger. The cache for two requests in flight. Prompt processing rate on a four thousand token prompt. Total VRAM in use with a one hundred twenty-eight thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="IT PREFILLED, THEN IT FAILED",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="This is the",
    art_at="Picture the key-value",
    rails=[{"lab": "2 REQUESTS", "val": "576", "pct": 50.0, "cls": "red", "at": "The cache for"}, {"lab": "4K", "val": "3749", "pct": 100.0, "cls": "", "at": "Prompt processing rate"}, {"lab": "128K", "val": "26", "pct": 76.5, "cls": "", "at": "Total VRAM in"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request &middot; multiplied by the requests in flight",
)

win(
    layout="note",
    vo="Measured cache, on this board, in this run. Picture the key-value ledger. One number, one config, one precision. Decimal gigabytes, not binary ones. A rounded cache changes what the model reads back. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="IT PREFILLED, THEN IT FAILED",
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
    title="IT PREFILLED, THEN IT FAILED",
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
    vo="The prefill number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the cache budget figure, the prefill budget figure, the vram budget figure.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="IT PREFILLED, THEN IT FAILED",
    header_at="The prefill number",
    items=[{"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="title",
    vo="One claim, one board, one run. The prompt processing phase and the cache phase cost different amounts of memory, which is why a model can prefill and then fail to generate. IT PREFILLED, THEN IT FAILED.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="IT PREFILLED, THEN IT FAILED",
    sub="The prompt processing phase and the cache phase cost different amounts of memory, which is why a model can prefill and then fail to generate.",
    art="vram_module",
    head_at="IT PREFILLED, THEN IT FAILED",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="nodes",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with a two hundred fifty-six thousand token context. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="IT PREFILLED, THEN IT FAILED",
    header_at="The vram figure",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    art_at="Picture the vram",
    chain=[{"t": "256K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}, {"t": "8,192 TOKENS", "s": "One number, one config, one precision", "at": "The key value"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-KV-008"
TITLE = "IT PREFILLED, THEN IT FAILED"
DOC_TITLE = "IT PREFILLED, THEN IT FAILED &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
