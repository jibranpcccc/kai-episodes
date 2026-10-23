# -*- coding: utf-8 -*-
"""Generated from angle ME-012 -- A NUMBER WITHOUT SETUP IS A RUMOR.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py ME-012
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same papers. Picture the paper folder. The LoRA paper's WikiSQL score for the full fine tune. Total VRAM in use with a four thousand token context. The size of the block scale in the four bit format. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="A NUMBER WITHOUT SETUP IS A RUMOR",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Same board",
    art_at="Picture the paper",
    chips=[{"t": "FT 73.8", "c": "gold", "at": "The LoRA paper's"}, {"t": "4K", "c": "cyan", "at": "Total VRAM in"}],
    stats=[{"v": "32", "u": "", "lab": "32 BIT", "c": "cyan", "at": "The size of"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="chain",
    vo="The cache figure, read straight off the board. Picture the key-value ledger. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. The LoRA paper's WikiSQL score for LoRA at rank four. Total VRAM in use with an eight thousand token context.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="A NUMBER WITHOUT SETUP IS A RUMOR",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="The cache figure",
    art_at="Picture the key-value",
    chain=[{"t": "8,192 TOKENS", "s": "One number, one config, one precision", "at": "The key value"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about LO 89.5, taken on trust.", "at": "The LoRA paper's"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 8K, taken on the board.", "at": "Total VRAM in"}],
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="rows",
    vo="One cache number, one source, one board. Picture the key-value ledger. The same cache in decimal gigabytes. The LoRA paper's MNLI score for the full fine tune. Total VRAM in use with a sixteen thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="A NUMBER WITHOUT SETUP IS A RUMOR",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="One cache number",
    art_at="Picture the key-value",
    rows=[{"rank": "1", "name": "Qwen2.5 3B Instruct", "val": "0.302 GB", "sub": "0.302 GB", "cls": "gold", "at": "The same cache"}, {"rank": "2", "name": "GPT-3 175B", "val": "73.4", "sub": "FT 73.4", "cls": "", "at": "The LoRA paper's"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "", "at": "Total VRAM in"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

win(
    layout="bars",
    vo="Nothing here about cache is a guess. Picture the key-value ledger. The cache for two requests in flight. Total VRAM in use with a two hundred fifty-six thousand token context. The cache for four requests in flight. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="A NUMBER WITHOUT SETUP IS A RUMOR",
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
    title="A NUMBER WITHOUT SETUP IS A RUMOR",
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
    title="A NUMBER WITHOUT SETUP IS A RUMOR",
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
    vo="Every papers figure here carries its own source. Picture the paper folder. On the bench: Llama 7B. Total VRAM in use with a two hundred fifty-six thousand token context. The line reads one thousand one hundred and fifty-two mebibytes, from the same run.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="A NUMBER WITHOUT SETUP IS A RUMOR",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Every papers figure",
    art_at="Picture the paper",
    name="Llama 7B",
    blurb="Total VRAM in use with a two hundred fifty-six thousand token context",
    meta="4 REQUESTS &middot; 1152 MiB",
    name_at="On the bench",
    blurb_at="Total VRAM in",
    meta_at="The line reads",
    side="right",
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; llama 7b on alpaca",
)

win(
    layout="strip",
    vo="The cache number does the talking, not the claim. Strip by strip: the paper budget figure, the vram budget figure, the quant budget figure, the cache budget figure.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="A NUMBER WITHOUT SETUP IS A RUMOR",
    header_at="The cache number",
    items=[{"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "gguf_blocks", "label": "quant budget", "at": "the quant budget figure"}, {"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="title",
    vo="One claim, one board, one run. A number copied from a benchmark without the model, the quant, the card and the context is a rumor, and this channel treats it as one. A NUMBER WITHOUT SETUP IS A RUMOR.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="A NUMBER WITHOUT SETUP IS A RUMOR",
    sub="A number copied from a benchmark without the model, the quant, the card and the context is a rumor, and this channel treats it as one.",
    art="folder",
    head_at="A NUMBER WITHOUT SETUP IS A RUMOR",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="nodes",
    vo="The papers figure, read straight off the board. Picture the paper folder. The QLoRA paper's FLAN v2 score for QLoRA. Total VRAM in use with a four thousand token context. The movement in MMLU between the full fine tune and QLoRA.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="A NUMBER WITHOUT SETUP IS A RUMOR",
    header_at="The papers figure",
    art="folder",
    art_caption="THE PAPER FOLDER",
    art_at="Picture the paper",
    chain=[{"t": "QLoRA 44.5", "s": "This figure does not establish that a model fits.", "at": "The QLoRA paper's"}, {"t": "4K", "s": "This figure does not establish a speed.", "at": "Total VRAM in"}, {"t": "MMLU", "s": "This figure does not establish a fit claim.", "at": "The movement in"}],
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; llama 7b on alpaca",
)

NAME = "BYTE-GEN-ME-012"
TITLE = "A NUMBER WITHOUT SETUP IS A RUMOR"
DOC_TITLE = "A NUMBER WITHOUT SETUP IS A RUMOR &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
