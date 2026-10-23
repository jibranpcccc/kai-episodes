# -*- coding: utf-8 -*-
"""Generated from angle KV-009 -- TRUNCATE HISTORY BEFORE BUYING CONTEXT.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py KV-009
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same cache. Picture the key-value ledger. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Read 8,192 tokens again, and it does not move. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="TRUNCATE HISTORY BEFORE BUYING CONTEXT",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Same board",
    art_at="Picture the key-value",
    chips=[{"t": "8,192 TOKENS", "c": "gold", "at": "The key value"}],
    stats=[{"v": "288", "u": "MiB", "lab": "8,192 TOKENS", "c": "red", "at": "Read 8,192 tokens"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="chain",
    vo="The cache figure, read straight off the board. Picture the key-value ledger. The same cache in decimal gigabytes. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="TRUNCATE HISTORY BEFORE BUYING CONTEXT",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="The cache figure",
    art_at="Picture the key-value",
    chain=[{"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about at 767 T/S, taken on trust.", "at": "Time to the"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 2 cards 128K, taken on the board.", "at": "Generation rate on"}],
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

win(
    layout="rows",
    vo="One capacity number, one source, one board. Picture the window and what is in it. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. The same cache held in four bit blocks, at eighteen bytes for every thirty-two values. One method, every row.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="TRUNCATE HISTORY BEFORE BUYING CONTEXT",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="One capacity number",
    art_at="Picture the window",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "gold", "at": "Generation rate on"}, {"rank": "2", "name": "Qwen2.5 3B Instruct", "val": "81 MiB", "sub": "Q4_0 PAYLOAD", "cls": "red", "at": "The same cache"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about cache is a guess. Picture the key-value ledger. The cache for four requests in flight. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="TRUNCATE HISTORY BEFORE BUYING CONTEXT",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Nothing here about",
    art_at="Picture the key-value",
    bars=[{"lab": "Qwen2.5 3B Instruct", "val": "1152", "unit": "MiB", "pct": 100.0, "cls": "red", "at": "The cache for"}, {"lab": "Qwen2.5 3B Instruct", "val": "288", "unit": "MiB", "pct": 100.0, "cls": "red", "at": "The key value"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request &middot; multiplied by the requests in flight",
)

win(
    layout="rail",
    vo="This is the cache of the hardware, not of the brochure. Picture the key-value ledger. The same cache in decimal gigabytes. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="TRUNCATE HISTORY BEFORE BUYING CONTEXT",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="This is the",
    art_at="Picture the key-value",
    rails=[{"lab": "0.302 GB", "val": "0.302", "pct": 100.0, "cls": "red", "at": "The same cache"}, {"lab": "at 767 T/S", "val": "131", "pct": 100.0, "cls": "red", "at": "Time to the"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

win(
    layout="note",
    vo="Measured cache, on this board, in this run. Picture the key-value ledger. One number, one config, one precision. The wait before any word appears, not the total run. A pair of cards never buys speed. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="TRUNCATE HISTORY BEFORE BUYING CONTEXT",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Measured cache, on",
    art_at="Picture the key-value",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "One number, one config, one precision", "at": "One number, one"}, {"t": "The wait before any word appears, not the total run", "at": "The wait before"}, {"t": "A pair of cards never buys speed", "at": "A pair of"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every cache figure here carries its own source. Picture the key-value ledger. On the bench: Qwen2.5 3B Instruct. The cache for two requests in flight. The line reads one thousand one hundred and fifty-two mebibytes, from the same run.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="TRUNCATE HISTORY BEFORE BUYING CONTEXT",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Every cache figure",
    art_at="Picture the key-value",
    name="Qwen2.5 3B Instruct",
    blurb="The cache for two requests in flight",
    meta="4 REQUESTS &middot; 1152 MiB",
    name_at="On the bench",
    blurb_at="The cache for",
    meta_at="The line reads",
    side="right",
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request",
)

win(
    layout="strip",
    vo="The latency number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the cache budget figure, the latency budget figure, the context budget figure.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="TRUNCATE HISTORY BEFORE BUYING CONTEXT",
    header_at="The latency number",
    items=[{"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

NAME = "BYTE-GEN-KV-009"
TITLE = "TRUNCATE HISTORY BEFORE BUYING CONTEXT"
DOC_TITLE = "TRUNCATE HISTORY BEFORE BUYING CONTEXT &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
