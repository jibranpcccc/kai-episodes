# -*- coding: utf-8 -*-
"""Generated from angle KV-014 -- CACHE QUANTIZATION IS NOT FREE.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py KV-014
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same quant. Picture quantised in blocks. The size of the block scale in the four bit format. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="CACHE QUANTIZATION IS NOT FREE",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="Same board",
    art_at="Picture quantised in",
    chips=[{"t": "32 BIT", "c": "gold", "at": "The size of"}],
    stats=[{"v": "288", "u": "MiB", "lab": "8,192 TOKENS", "c": "red", "at": "The key value"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="chain",
    vo="The quant figure, read straight off the board. Picture quantised in blocks. The overhead the block scales add per weight. The same cache in decimal gigabytes. Generation rate on a five-oh-ninety with a sixteen thousand token context.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="CACHE QUANTIZATION IS NOT FREE",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="The quant figure",
    art_at="Picture quantised in",
    chain=[{"t": "+0.5 BIT", "s": "This figure does not establish that a model fits.", "at": "The overhead the"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 0.302 GB, taken on trust.", "at": "The same cache"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 16K, taken on the board.", "at": "Generation rate on"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="rows",
    vo="One cache number, one source, one board. Picture the key-value ledger. The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values. Generation rate on a five-oh-ninety with a thirty-two thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="CACHE QUANTIZATION IS NOT FREE",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="One cache number",
    art_at="Picture the key-value",
    rows=[{"rank": "1", "name": "Qwen2.5 3B Instruct", "val": "153 MiB", "sub": "Q8_0 PAYLOAD", "cls": "gold", "at": "The same cache"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "", "at": "Generation rate on"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; q8_0 34 bytes per 32 values",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a three thousand ninety with a thirty-two thousand token context. The cache for four requests in flight. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="CACHE QUANTIZATION IS NOT FREE",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Nothing here about",
    art_at="Picture the tokens",
    bars=[{"lab": "Qwen 3.8 27B", "val": "37.0", "unit": "T/S", "pct": 91.8, "cls": "", "at": "Generation rate on"}, {"lab": "Qwen2.5 3B Instruct", "val": "1152", "unit": "MiB", "pct": 100.0, "cls": "red", "at": "The cache for"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the generation of the hardware, not of the brochure. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a four thousand token context. The same cache in decimal gigabytes. Generation rate on a five-oh-ninety with a sixteen thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="CACHE QUANTIZATION IS NOT FREE",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="This is the",
    art_at="Picture the tokens",
    rails=[{"lab": "4K", "val": "74.8", "pct": 100.0, "cls": "", "at": "Generation rate on a five-oh-ninety with a four"}, {"lab": "0.302 GB", "val": "0.302", "pct": 100.0, "cls": "red", "at": "The same cache"}, {"lab": "16K", "val": "52.2", "pct": 69.8, "cls": "", "at": "Generation rate on a five-oh-ninety with a sixteen"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured cache, on this board, in this run. Picture the key-value ledger. One number, one config, one precision. Decimal gigabytes, not binary ones. A rounded cache changes what the model reads back. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="CACHE QUANTIZATION IS NOT FREE",
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
    vo="Every cache figure here carries its own source. Picture the key-value ledger. On the bench: Qwen2.5 3B Instruct. Generation rate on a five-oh-ninety with a sixteen thousand token context. The line reads four point one two seven, from the same run.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="CACHE QUANTIZATION IS NOT FREE",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Every cache figure",
    art_at="Picture the key-value",
    name="Qwen2.5 3B Instruct",
    blurb="Generation rate on a five-oh-ninety with a sixteen thousand token context",
    meta="EFFECTIVE &middot; 4.127",
    name_at="On the bench",
    blurb_at="Generation rate on",
    meta_at="The line reads",
    side="right",
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

win(
    layout="strip",
    vo="The cache number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the quant budget figure, the cache budget figure, the decode budget figure.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="CACHE QUANTIZATION IS NOT FREE",
    header_at="The cache number",
    items=[{"key": "gguf_blocks", "label": "quant budget", "at": "the quant budget figure"}, {"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="title",
    vo="One claim, one board, one run. Cache quantization has a different cost profile from weight quantization, because the cache is touched on every token rather than once per request. CACHE QUANTIZATION IS NOT FREE.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="CACHE QUANTIZATION IS NOT FREE",
    sub="Cache quantization has a different cost profile from weight quantization, because the cache is touched on every token rather than once per request.",
    art="token_blocks",
    head_at="CACHE QUANTIZATION IS NOT FREE",
    source="the documented bits and bytes route &middot; nested quantization",
)

NAME = "BYTE-GEN-KV-014"
TITLE = "CACHE QUANTIZATION IS NOT FREE"
DOC_TITLE = "CACHE QUANTIZATION IS NOT FREE &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
