# -*- coding: utf-8 -*-
"""Generated from angle QUANT-012 -- YOU QUANTIZED HALF THE MEMORY BILL.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py QUANT-012
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same quant. Picture quantised in blocks. The size of the block scale in the four bit format. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="YOU QUANTIZED HALF THE MEMORY BILL",
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
    vo="The quant figure, read straight off the board. Picture quantised in blocks. The overhead the block scales add per weight. The same cache in decimal gigabytes. Total VRAM in use with an eight thousand token context. The effective bits per converted weight in the pinned implementation, with the nested scales compressed too.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="YOU QUANTIZED HALF THE MEMORY BILL",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="The quant figure",
    art_at="Picture quantised in",
    chain=[{"t": "+0.5 BIT", "s": "This figure does not establish that a model fits.", "at": "The overhead the"}, {"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 8K, taken on trust.", "at": "Total VRAM in"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of EFFECTIVE, taken on the board.", "at": "The effective bits"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="rows",
    vo="One cache number, one source, one board. Picture the key-value ledger. The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values. Total VRAM in use with a sixteen thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="YOU QUANTIZED HALF THE MEMORY BILL",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="One cache number",
    art_at="Picture the key-value",
    rows=[{"rank": "1", "name": "Qwen2.5 3B Instruct", "val": "153 MiB", "sub": "Q8_0 PAYLOAD", "cls": "gold", "at": "The same cache"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "", "at": "Total VRAM in"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; q8_0 34 bytes per 32 values",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a one hundred twenty-eight thousand token context. The cache for four requests in flight. Total VRAM in use with a two hundred fifty-six thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="YOU QUANTIZED HALF THE MEMORY BILL",
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
    title="YOU QUANTIZED HALF THE MEMORY BILL",
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
    title="YOU QUANTIZED HALF THE MEMORY BILL",
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
    vo="Every quant figure here carries its own source. Picture quantised in blocks. On the bench: Qwen2.5 3B Instruct. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. The line reads eighteen gigabytes, from the same run.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="YOU QUANTIZED HALF THE MEMORY BILL",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="Every quant figure",
    art_at="Picture quantised in",
    name="Qwen2.5 3B Instruct",
    blurb="The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision",
    meta="4K &middot; 18 GB",
    name_at="On the bench",
    blurb_at="The key value",
    meta_at="The line reads",
    side="right",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="strip",
    vo="The cache number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the quant budget figure, the cache budget figure, the vram budget figure.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="YOU QUANTIZED HALF THE MEMORY BILL",
    header_at="The cache number",
    items=[{"key": "gguf_blocks", "label": "quant budget", "at": "the quant budget figure"}, {"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="title",
    vo="One claim, one board, one run. Quantizing the weights while keeping the cache at full precision leaves the second memory bill untouched, so the total savings are smaller than the headline. YOU QUANTIZED HALF THE MEMORY BILL.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="YOU QUANTIZED HALF THE MEMORY BILL",
    sub="Quantizing the weights while keeping the cache at full precision leaves the second memory bill untouched, so the total savings are smaller than the headline.",
    art="vram_module",
    head_at="YOU QUANTIZED HALF THE MEMORY BILL",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="nodes",
    vo="The quant figure, read straight off the board. Picture quantised in blocks. The overhead the block scales add per weight. The same cache in decimal gigabytes. Total VRAM in use with an eight thousand token context.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="YOU QUANTIZED HALF THE MEMORY BILL",
    header_at="The quant figure",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    art_at="Picture quantised in",
    chain=[{"t": "+0.5 BIT", "s": "This figure does not establish that a model fits.", "at": "The overhead the"}, {"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}, {"t": "8K", "s": "This figure does not establish a fit claim.", "at": "Total VRAM in"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

NAME = "BYTE-GEN-QUANT-012"
TITLE = "YOU QUANTIZED HALF THE MEMORY BILL"
DOC_TITLE = "YOU QUANTIZED HALF THE MEMORY BILL &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
