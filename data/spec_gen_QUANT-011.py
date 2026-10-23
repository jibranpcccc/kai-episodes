# -*- coding: utf-8 -*-
"""Generated from angle QUANT-011 -- ADVERTISED SAVINGS ARE A CEILING.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py QUANT-011
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same quant. Picture quantised in blocks. The size of the block scale in the four bit format. Total VRAM in use with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="ADVERTISED SAVINGS ARE A CEILING",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="Same board",
    art_at="Picture quantised in",
    chips=[{"t": "32 BIT", "c": "gold", "at": "The size of"}],
    stats=[{"v": "18", "u": "GB", "lab": "4K", "c": "gold", "at": "Total VRAM in"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="chain",
    vo="The quant figure, read straight off the board. Picture quantised in blocks. The overhead the block scales add per weight. Total VRAM in use with an eight thousand token context. The same cache in decimal gigabytes. The effective bits per converted weight in the pinned implementation, with the nested scales compressed too.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="ADVERTISED SAVINGS ARE A CEILING",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="The quant figure",
    art_at="Picture quantised in",
    chain=[{"t": "+0.5 BIT", "s": "This figure does not establish that a model fits.", "at": "The overhead the"}, {"t": "8K", "s": "This figure does not establish a speed.", "at": "Total VRAM in"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 0.302 GB, taken on trust.", "at": "The same cache"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of EFFECTIVE, taken on the board.", "at": "The effective bits"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a sixteen thousand token context. The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values. Total VRAM in use with a thirty-two thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="ADVERTISED SAVINGS ARE A CEILING",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "gold", "at": "Total VRAM in use with a sixteen"}, {"rank": "2", "name": "Qwen2.5 3B Instruct", "val": "153 MiB", "sub": "Q8_0 PAYLOAD", "cls": "red", "at": "The same cache"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "20 GB", "sub": "32K", "cls": "", "at": "Total VRAM in use with a thirty-two"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about cache is a guess. Picture the key-value ledger. The cache for two requests in flight. Total VRAM in use with a two hundred fifty-six thousand token context. The cache for four requests in flight. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="ADVERTISED SAVINGS ARE A CEILING",
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
    title="ADVERTISED SAVINGS ARE A CEILING",
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
    title="ADVERTISED SAVINGS ARE A CEILING",
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
    vo="Every quant figure here carries its own source. Picture quantised in blocks. On the bench: Qwen2.5 3B Instruct. Total VRAM in use with a four thousand token context. The line reads two hundred and eighty-eight mebibytes, from the same run.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="ADVERTISED SAVINGS ARE A CEILING",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="Every quant figure",
    art_at="Picture quantised in",
    name="Qwen2.5 3B Instruct",
    blurb="Total VRAM in use with a four thousand token context",
    meta="8,192 TOKENS &middot; 288 MiB",
    name_at="On the bench",
    blurb_at="Total VRAM in",
    meta_at="The line reads",
    side="right",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the quant budget figure, the vram budget figure, the cache budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="ADVERTISED SAVINGS ARE A CEILING",
    header_at="The vram number",
    items=[{"key": "gguf_blocks", "label": "quant budget", "at": "the quant budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="title",
    vo="One claim, one board, one run. The gap between quantized and unquantized memory use is larger for the weights than for the whole model, so advertised savings are always an upper bound. ADVERTISED SAVINGS ARE A CEILING.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="ADVERTISED SAVINGS ARE A CEILING",
    sub="The gap between quantized and unquantized memory use is larger for the weights than for the whole model, so advertised savings are always an upper bound.",
    art="kv_cache",
    head_at="ADVERTISED SAVINGS ARE A CEILING",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="nodes",
    vo="The quant figure, read straight off the board. Picture quantised in blocks. The overhead the block scales add per weight. Total VRAM in use with an eight thousand token context. The same cache in decimal gigabytes.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="ADVERTISED SAVINGS ARE A CEILING",
    header_at="The quant figure",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    art_at="Picture quantised in",
    chain=[{"t": "+0.5 BIT", "s": "This figure does not establish that a model fits.", "at": "The overhead the"}, {"t": "8K", "s": "This figure does not establish a speed.", "at": "Total VRAM in"}, {"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

NAME = "BYTE-GEN-QUANT-011"
TITLE = "ADVERTISED SAVINGS ARE A CEILING"
DOC_TITLE = "ADVERTISED SAVINGS ARE A CEILING &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
