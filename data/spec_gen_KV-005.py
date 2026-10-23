# -*- coding: utf-8 -*-
"""Generated from angle KV-005 -- THE WINDOW IS NOT THE WORKING SET.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py KV-005
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same cache. Picture the key-value ledger. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Generation rate on two sixteen gigabyte cards with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="THE WINDOW IS NOT THE WORKING SET",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Same board",
    art_at="Picture the key-value",
    chips=[{"t": "8,192 TOKENS", "c": "gold", "at": "The key value"}],
    stats=[{"v": "22.5", "u": "T/S", "lab": "2 cards 4K", "c": "red", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="chain",
    vo="The cache figure, read straight off the board. Picture the key-value ledger. The same cache in decimal gigabytes. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context. Prompt processing rate on a sixteen thousand token prompt.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="THE WINDOW IS NOT THE WORKING SET",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="The cache figure",
    art_at="Picture the key-value",
    chain=[{"t": "0.302 GB", "s": "Decimal gigabytes, not binary ones", "at": "The same cache"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 2 cards 128K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 16K, taken on the board.", "at": "Prompt processing rate"}],
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

win(
    layout="rows",
    vo="One capacity number, one source, one board. Picture the window and what is in it. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. Prompt processing rate on a sixty-four thousand token prompt. One method, every row.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="THE WINDOW IS NOT THE WORKING SET",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="One capacity number",
    art_at="Picture the window",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "gold", "at": "Generation rate on"}, {"rank": "2", "name": "Muse Glimmer 30B", "val": "3606 T/S", "sub": "64K", "cls": "", "at": "Prompt processing rate"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about cache is a guess. Picture the key-value ledger. The cache for a single request in flight. Prompt processing rate on a two hundred fifty-six thousand token prompt. The cache for two requests in flight. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="THE WINDOW IS NOT THE WORKING SET",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Nothing here about",
    art_at="Picture the key-value",
    bars=[{"lab": "Qwen2.5 3B Instruct", "val": "288", "unit": "MiB", "pct": 25.0, "cls": "red", "at": "The cache for a"}, {"lab": "Muse Glimmer 30B", "val": "1874", "unit": "T/S", "pct": 40.5, "cls": "", "at": "Prompt processing rate"}, {"lab": "Qwen2.5 3B Instruct", "val": "576", "unit": "MiB", "pct": 50.0, "cls": "red", "at": "The cache for two"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request",
)

win(
    layout="rail",
    vo="This is the cache of the hardware, not of the brochure. Picture the key-value ledger. The cache for four requests in flight. Prompt processing rate on a one hundred twenty-eight thousand token prompt. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="THE WINDOW IS NOT THE WORKING SET",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="This is the",
    art_at="Picture the key-value",
    rails=[{"lab": "4 REQUESTS", "val": "1152", "pct": 100.0, "cls": "red", "at": "The cache for"}, {"lab": "128K", "val": "461", "pct": 12.3, "cls": "", "at": "Prompt processing rate"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request &middot; multiplied by the requests in flight",
)

win(
    layout="note",
    vo="Measured cache, on this board, in this run. Picture the key-value ledger. One number, one config, one precision. A pair of cards never buys speed. Decimal gigabytes, not binary ones. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="THE WINDOW IS NOT THE WORKING SET",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Measured cache, on",
    art_at="Picture the key-value",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "One number, one config, one precision", "at": "One number, one"}, {"t": "A pair of cards never buys speed", "at": "A pair of"}, {"t": "Decimal gigabytes, not binary ones", "at": "Decimal gigabytes, not"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every capacity figure here carries its own source. Picture the window and what is in it. On the bench: Qwen 3.8 27B. Prompt processing rate on a sixteen thousand token prompt. The line reads one hundred and fifty-three mebibytes, from the same run.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="THE WINDOW IS NOT THE WORKING SET",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="Every capacity figure",
    art_at="Picture the window",
    name="Qwen 3.8 27B",
    blurb="Prompt processing rate on a sixteen thousand token prompt",
    meta="Q8_0 PAYLOAD &middot; 153 MiB",
    name_at="On the bench",
    blurb_at="Prompt processing rate",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The capacity number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the cache budget figure, the context budget figure, the prefill budget figure.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="THE WINDOW IS NOT THE WORKING SET",
    header_at="The capacity number",
    items=[{"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}, {"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="title",
    vo="One claim, one board, one run. The working-set claim is arithmetic; it does not test how much cache the runtime reserves. THE WINDOW IS NOT THE WORKING SET.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE WINDOW IS NOT THE WORKING SET",
    sub="The working-set claim is arithmetic; it does not test how much cache the runtime reserves.",
    art="prompt_stream",
    head_at="THE WINDOW IS NOT THE WORKING SET",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

NAME = "BYTE-GEN-KV-005"
TITLE = "THE WINDOW IS NOT THE WORKING SET"
DOC_TITLE = "THE WINDOW IS NOT THE WORKING SET &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
