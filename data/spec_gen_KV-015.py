# -*- coding: utf-8 -*-
"""Generated from angle KV-015 -- A LONG PROMPT PAYS TWICE.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py KV-015
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same cache. Picture the key-value ledger. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Prompt processing rate on a four thousand token prompt. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="A LONG PROMPT PAYS TWICE",
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
    vo="The cache figure, read straight off the board. Picture the key-value ledger. The same cache in decimal gigabytes. Prompt processing rate on a sixteen thousand token prompt. Generation rate on a five-oh-ninety with a sixteen thousand token context.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="A LONG PROMPT PAYS TWICE",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="The cache figure",
    art_at="Picture the key-value",
    chain=[{"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Prompt processing rate"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 16K, taken on the board.", "at": "Generation rate on"}],
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

win(
    layout="rows",
    vo="One prefill number, one source, one board. Picture the prompt, incoming. Prompt processing rate on a sixty-four thousand token prompt. Generation rate on a five-oh-ninety with a thirty-two thousand token context. The same cache held in four bit blocks, at eighteen bytes for every thirty-two values. One method, every row.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="A LONG PROMPT PAYS TWICE",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="One prefill number",
    art_at="Picture the prompt",
    rows=[{"rank": "1", "name": "Muse Glimmer 30B", "val": "3606 T/S", "sub": "64K", "cls": "gold", "at": "Prompt processing rate"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "", "at": "Generation rate on"}, {"rank": "3", "name": "Qwen2.5 3B Instruct", "val": "81 MiB", "sub": "Q4_0 PAYLOAD", "cls": "red", "at": "The same cache"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context. The cache for a single request in flight. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="A LONG PROMPT PAYS TWICE",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Nothing here about",
    art_at="Picture the tokens",
    bars=[{"lab": "Qwen 3.8 27B", "val": "22.8", "unit": "T/S", "pct": 30.5, "cls": "", "at": "Generation rate on"}, {"lab": "Qwen2.5 3B Instruct", "val": "288", "unit": "MiB", "pct": 25.0, "cls": "red", "at": "The cache for"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the cache of the hardware, not of the brochure. Picture the key-value ledger. The cache for two requests in flight. Prompt processing rate on a four thousand token prompt. Generation rate on a three thousand ninety with a thirty-two thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="A LONG PROMPT PAYS TWICE",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="This is the",
    art_at="Picture the key-value",
    rails=[{"lab": "2 REQUESTS", "val": "576", "pct": 50.0, "cls": "red", "at": "The cache for"}, {"lab": "4K", "val": "3749", "pct": 100.0, "cls": "", "at": "Prompt processing rate"}, {"lab": "32K", "val": "37.0", "pct": 91.8, "cls": "", "at": "Generation rate on"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request &middot; multiplied by the requests in flight",
)

win(
    layout="note",
    vo="Measured cache, on this board, in this run. Picture the key-value ledger. One number, one config, one precision. Decimal gigabytes, not binary ones. A rounded cache changes what the model reads back. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="A LONG PROMPT PAYS TWICE",
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
    vo="Every cache figure here carries its own source. Picture the key-value ledger. On the bench: Qwen2.5 3B Instruct. Prompt processing rate on a four thousand token prompt. The line reads seventy-four point eight tokens per second, from the same run.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="A LONG PROMPT PAYS TWICE",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Every cache figure",
    art_at="Picture the key-value",
    name="Qwen2.5 3B Instruct",
    blurb="Prompt processing rate on a four thousand token prompt",
    meta="4K &middot; 74.8 T/S",
    name_at="On the bench",
    blurb_at="Prompt processing rate",
    meta_at="The line reads",
    side="right",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="strip",
    vo="The prefill number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the cache budget figure, the prefill budget figure, the decode budget figure.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="A LONG PROMPT PAYS TWICE",
    header_at="The prefill number",
    items=[{"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="title",
    vo="One claim, one board, one run. The cache is what makes a long prompt pay twice, once in prefill and again in every generated token that follows. A LONG PROMPT PAYS TWICE.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="A LONG PROMPT PAYS TWICE",
    sub="The cache is what makes a long prompt pay twice, once in prefill and again in every generated token that follows.",
    art="token_blocks",
    head_at="A LONG PROMPT PAYS TWICE",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="nodes",
    vo="The cache figure, read straight off the board. Picture the key-value ledger. The same cache in decimal gigabytes. Prompt processing rate on a sixteen thousand token prompt. Generation rate on a five-oh-ninety with a sixteen thousand token context.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="A LONG PROMPT PAYS TWICE",
    header_at="The cache figure",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    art_at="Picture the key-value",
    chain=[{"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}, {"t": "16K", "s": "This figure does not establish a speed.", "at": "Prompt processing rate"}, {"t": "16K", "s": "This figure does not establish a fit claim.", "at": "Generation rate on"}],
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

NAME = "BYTE-GEN-KV-015"
TITLE = "A LONG PROMPT PAYS TWICE"
DOC_TITLE = "A LONG PROMPT PAYS TWICE &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
