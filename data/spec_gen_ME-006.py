# -*- coding: utf-8 -*-
"""Generated from angle ME-006 -- ONE BOARD, TWO DIFFERENT JOBS.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py ME-006
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same papers. Picture the paper folder. The LoRA paper's WikiSQL score for the full fine tune. Prompt processing rate on a four thousand token prompt. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="ONE BOARD, TWO DIFFERENT JOBS",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Same board",
    art_at="Picture the paper",
    chips=[{"t": "FT 73.8", "c": "gold", "at": "The LoRA paper's"}],
    stats=[{"v": "4625", "u": "T/S", "lab": "4K", "c": "gold", "at": "Prompt processing rate"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="chain",
    vo="The papers figure, read straight off the board. Picture the paper folder. The LoRA paper's WikiSQL score for LoRA at rank four. Prompt processing rate on a sixteen thousand token prompt. The same cache in decimal gigabytes. The LoRA paper's MNLI score for the full fine tune.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="ONE BOARD, TWO DIFFERENT JOBS",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="The papers figure",
    art_at="Picture the paper",
    chain=[{"t": "LO 89.5", "s": "This figure does not establish that a model fits.", "at": "The LoRA paper's WikiSQL"}, {"t": "16K", "s": "This figure does not establish a speed.", "at": "Prompt processing rate"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 0.302 GB, taken on trust.", "at": "The same cache"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of FT 73.4, taken on the board.", "at": "The LoRA paper's MNLI"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="rows",
    vo="One prefill number, one source, one board. Picture the prompt, incoming. Prompt processing rate on a sixty-four thousand token prompt. The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values. The LoRA paper's MNLI score for LoRA at rank four. One method, every row.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="ONE BOARD, TWO DIFFERENT JOBS",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="One prefill number",
    art_at="Picture the prompt",
    rows=[{"rank": "1", "name": "Muse Glimmer 30B", "val": "3606 T/S", "sub": "64K", "cls": "gold", "at": "Prompt processing rate"}, {"rank": "2", "name": "Qwen2.5 3B Instruct", "val": "153 MiB", "sub": "Q8_0 PAYLOAD", "cls": "red", "at": "The same cache"}, {"rank": "3", "name": "GPT-3 175B", "val": "91.7", "sub": "LO 91.7", "cls": "", "at": "The LoRA paper's"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about cache is a guess. Picture the key-value ledger. The cache for two requests in flight. Prompt processing rate on a one hundred twenty-eight thousand token prompt. The cache for four requests in flight. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="ONE BOARD, TWO DIFFERENT JOBS",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="Nothing here about",
    art_at="Picture the key-value",
    bars=[{"lab": "Qwen2.5 3B Instruct", "val": "576", "unit": "MiB", "pct": 50.0, "cls": "red", "at": "The cache for two"}, {"lab": "Qwen 3.8 27B", "val": "461", "unit": "T/S", "pct": 12.3, "cls": "", "at": "Prompt processing rate"}, {"lab": "Qwen2.5 3B Instruct", "val": "1152", "unit": "MiB", "pct": 100.0, "cls": "red", "at": "The cache for four"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request &middot; multiplied by the requests in flight",
)

win(
    layout="rail",
    vo="This is the cache of the hardware, not of the brochure. Picture the key-value ledger. The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision. Prompt processing rate on a sixteen thousand token prompt. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="ONE BOARD, TWO DIFFERENT JOBS",
    art="kv_cache",
    art_caption="THE KEY-VALUE LEDGER",
    header_at="This is the",
    art_at="Picture the key-value",
    rails=[{"lab": "8,192 TOKENS", "val": "288", "pct": 100.0, "cls": "red", "at": "The key value"}, {"lab": "16K", "val": "4373", "pct": 94.5, "cls": "", "at": "Prompt processing rate"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
)

win(
    layout="note",
    vo="Measured cache, on this board, in this run. Picture the key-value ledger. One number, one config, one precision. Decimal gigabytes, not binary ones. A rounded cache changes what the model reads back. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="ONE BOARD, TWO DIFFERENT JOBS",
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
    vo="Every papers figure here carries its own source. Picture the paper folder. On the bench: Llama 7B. The movement in MMLU between the full fine tune and QLoRA. The line reads minus one point one percentage points, from the same run.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="ONE BOARD, TWO DIFFERENT JOBS",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Every papers figure",
    art_at="Picture the paper",
    name="Llama 7B",
    blurb="The movement in MMLU between the full fine tune and QLoRA",
    meta="FLAN V2 &middot; -1.1 pp",
    name_at="On the bench",
    blurb_at="The movement in",
    meta_at="The line reads",
    side="right",
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; llama 7b on alpaca",
)

win(
    layout="strip",
    vo="The prefill number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the paper budget figure, the prefill budget figure, the cache budget figure.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="ONE BOARD, TWO DIFFERENT JOBS",
    header_at="The prefill number",
    items=[{"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}, {"key": "kv_cache", "label": "cache budget", "at": "the cache budget figure"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="title",
    vo="One claim, one board, one run. A model scored on short questions and a model scored on long documents are not being measured on the same axis, so the leaderboard mixes two problems. ONE BOARD, TWO DIFFERENT JOBS.",
    kicker="BYTE FORENSICS &middot; CACHE",
    title="ONE BOARD, TWO DIFFERENT JOBS",
    sub="A model scored on short questions and a model scored on long documents are not being measured on the same axis, so the leaderboard mixes two problems.",
    art="kv_cache",
    head_at="ONE BOARD, TWO DIFFERENT JOBS",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="nodes",
    vo="The papers figure, read straight off the board. Picture the paper folder. The model in the demonstration that made the technique famous. The size of the card in that demonstration. The LoRA paper's WikiSQL score for the full fine tune.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="ONE BOARD, TWO DIFFERENT JOBS",
    header_at="The papers figure",
    art="folder",
    art_caption="THE PAPER FOLDER",
    art_at="Picture the paper",
    chain=[{"t": "MODEL", "s": "This figure does not establish that a model fits.", "at": "The model in"}, {"t": "CARD", "s": "This figure does not establish a speed.", "at": "The size of"}, {"t": "FT 73.8", "s": "This figure does not establish a fit claim.", "at": "The LoRA paper's"}],
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; 65b on one 48 gb card",
)

NAME = "BYTE-GEN-ME-006"
TITLE = "ONE BOARD, TWO DIFFERENT JOBS"
DOC_TITLE = "ONE BOARD, TWO DIFFERENT JOBS &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
