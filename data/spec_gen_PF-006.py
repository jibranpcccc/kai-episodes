# -*- coding: utf-8 -*-
"""Generated from angle PF-006 -- YOUR SYSTEM PROMPT IS A RECURRING COST.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PF-006
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same prefill. Picture the prompt, incoming. Prompt processing rate on a four thousand token prompt. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="YOUR SYSTEM PROMPT IS A RECURRING COST",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="Same board",
    art_at="Picture the prompt",
    chips=[{"t": "4K", "c": "gold", "at": "Prompt processing rate"}],
    stats=[{"v": "22", "u": "s", "lab": "at 4,625 T/S", "c": "red", "at": "Time to the"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The prefill figure, read straight off the board. Picture the prompt, incoming. Prompt processing rate on a sixteen thousand token prompt. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. The same cache in decimal gigabytes.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="YOUR SYSTEM PROMPT IS A RECURRING COST",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="The prefill figure",
    art_at="Picture the prompt",
    chain=[{"t": "16K", "s": "This figure does not establish that a model fits.", "at": "Prompt processing rate"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about at 767 T/S, taken on trust.", "at": "Time to the"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 0.302 GB, taken on the board.", "at": "The same cache"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One cache number, one source, one board. Picture the key-value ledger. The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values. Prompt processing rate on a one hundred twenty-eight thousand token prompt. One method, every row.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="YOUR SYSTEM PROMPT IS A RECURRING COST",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="One cache number",
    art_at="Picture the key-value",
    rows=[{"rank": "1", "name": "Qwen2.5 3B Instruct", "val": "153 MiB", "sub": "Q8_0 PAYLOAD", "cls": "gold", "at": "The same cache"}, {"rank": "2", "name": "Muse Glimmer 30B", "val": "2806 T/S", "sub": "128K", "cls": "", "at": "Prompt processing rate"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; q8_0 34 bytes per 32 values",
)

win(
    layout="bars",
    vo="Nothing here about cache is a guess. Picture the key-value ledger. The cache for a single request in flight. Prompt processing rate on a four thousand token prompt. The cache for two requests in flight. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="YOUR SYSTEM PROMPT IS A RECURRING COST",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Nothing here about",
    art_at="Picture the key-value",
    bars=[{"lab": "Qwen2.5 3B Instruct", "val": "288", "unit": "MiB", "pct": 25.0, "cls": "red", "at": "The cache for a"}, {"lab": "Qwen 3.8 27B", "val": "3749", "unit": "T/S", "pct": 100.0, "cls": "", "at": "Prompt processing rate"}, {"lab": "Qwen2.5 3B Instruct", "val": "576", "unit": "MiB", "pct": 50.0, "cls": "red", "at": "The cache for two"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request",
)

win(
    layout="rail",
    vo="This is the cache of the hardware, not of the brochure. Picture the key-value ledger. The cache for four requests in flight. Prompt processing rate on a four thousand token prompt. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="YOUR SYSTEM PROMPT IS A RECURRING COST",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="This is the",
    art_at="Picture the key-value",
    rails=[{"lab": "4 REQUESTS", "val": "1152", "pct": 100.0, "cls": "red", "at": "The cache for"}, {"lab": "4K", "val": "4625", "pct": 100.0, "cls": "", "at": "Prompt processing rate"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request &middot; multiplied by the requests in flight",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. One number, one config, one precision. Decimal gigabytes, not binary ones. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="YOUR SYSTEM PROMPT IS A RECURRING COST",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Measured latency, on",
    art_at="Picture timing, line",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "The wait before any word appears, not the total run", "at": "The wait before"}, {"t": "One number, one config, one precision", "at": "One number, one"}, {"t": "Decimal gigabytes, not binary ones", "at": "Decimal gigabytes, not"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every cache figure here carries its own source. Picture the key-value ledger. On the bench: Qwen2.5 3B Instruct. Prompt processing rate on a sixty-four thousand token prompt. The line reads one hundred and fifty-three mebibytes, from the same run.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="YOUR SYSTEM PROMPT IS A RECURRING COST",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Every cache figure",
    art_at="Picture the key-value",
    name="Qwen2.5 3B Instruct",
    blurb="Prompt processing rate on a sixty-four thousand token prompt",
    meta="Q8_0 PAYLOAD &middot; 153 MiB",
    name_at="On the bench",
    blurb_at="Prompt processing rate",
    meta_at="The line reads",
    side="right",
    source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
)

win(
    layout="strip",
    vo="The latency number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the prefill budget figure, the latency budget figure, the cache budget figure.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="YOUR SYSTEM PROMPT IS A RECURRING COST",
    header_at="The latency number",
    items=[{"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}, {"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. A long system prompt is re-read on every request, so a cached system prompt can be worth more than a smarter prompt. YOUR SYSTEM PROMPT IS A RECURRING COST.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="YOUR SYSTEM PROMPT IS A RECURRING COST",
    sub="A long system prompt is re-read on every request, so a cached system prompt can be worth more than a smarter prompt.",
    art="kv_cache",
    head_at="YOUR SYSTEM PROMPT IS A RECURRING COST",
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-PF-006"
TITLE = "YOUR SYSTEM PROMPT IS A RECURRING COST"
DOC_TITLE = "YOUR SYSTEM PROMPT IS A RECURRING COST &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
