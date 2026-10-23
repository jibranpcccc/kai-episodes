# -*- coding: utf-8 -*-
"""Generated from angle LORA-001 -- TINY FILE, FULL-SIZE FOOTPRINT.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py LORA-001
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same lora. Picture the magnifier pass. The layer count of the model. Total VRAM in use with a four thousand token context. Generation rate on a five-oh-ninety with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="TINY FILE, FULL-SIZE FOOTPRINT",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="Same board",
    art_at="Picture the magnifier",
    chips=[{"t": "LAYERS", "c": "gold", "at": "The layer count"}, {"t": "4K", "c": "cyan", "at": "Total VRAM in"}],
    stats=[{"v": "74.8", "u": "T/S", "lab": "4K", "c": "cyan", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="chain",
    vo="The lora figure, read straight off the board. Picture the magnifier pass. The number of key value heads, shared across groups. Total VRAM in use with an eight thousand token context. Generation rate on a five-oh-ninety with a sixteen thousand token context. The width of one attention head.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="TINY FILE, FULL-SIZE FOOTPRINT",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="The lora figure",
    art_at="Picture the magnifier",
    chain=[{"t": "KV HEADS", "s": "This figure does not establish that a model fits.", "at": "The number of"}, {"t": "8K", "s": "This figure does not establish a speed.", "at": "Total VRAM in"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of HEAD DIM, taken on the board.", "at": "The width of"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a sixteen thousand token context. Generation rate on a five-oh-ninety with a thirty-two thousand token context. The hidden width of the model. Total VRAM in use with a thirty-two thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TINY FILE, FULL-SIZE FOOTPRINT",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "gold", "at": "Total VRAM in use with a sixteen"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "", "at": "Generation rate on"}, {"rank": "3", "name": "Qwen2.5 3B Instruct", "val": "2048", "sub": "HIDDEN", "cls": "", "at": "The hidden width"}, {"rank": "4", "name": "Qwen 3.8 27B", "val": "20 GB", "sub": "32K", "cls": "", "at": "Total VRAM in use with a thirty-two"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a three thousand ninety with a thirty-two thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="TINY FILE, FULL-SIZE FOOTPRINT",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Nothing here about",
    art_at="Picture the tokens",
    bars=[{"lab": "Qwen 3.8 27B", "val": "37.0", "unit": "T/S", "pct": 91.8, "cls": "", "at": "Generation rate on"}, {"lab": "Qwen 3.8 27B", "val": "34", "unit": "GB", "pct": 100.0, "cls": "red", "at": "Total VRAM in"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TINY FILE, FULL-SIZE FOOTPRINT",
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
    vo="Measured vram, on this board, in this run. Picture the vram sticks. Does not fit on a twenty-four gigabyte card at all. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TINY FILE, FULL-SIZE FOOTPRINT",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Measured vram, on",
    art_at="Picture the vram",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "Does not fit on a twenty-four gigabyte card at all", "at": "Does not fit"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every generation figure here carries its own source. Picture the tokens, one by one. On the bench: Qwen 3.8 27B. The added query parameters at rank sixteen. The line reads sixteen gigabytes, from the same run.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="TINY FILE, FULL-SIZE FOOTPRINT",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Every generation figure",
    art_at="Picture the tokens",
    name="Qwen 3.8 27B",
    blurb="The added query parameters at rank sixteen",
    meta="4K &middot; 16 GB",
    name_at="On the bench",
    blurb_at="The added query",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the adapter budget figure, the vram budget figure, the decode budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="TINY FILE, FULL-SIZE FOOTPRINT",
    header_at="The vram number",
    items=[{"key": "magnifier", "label": "adapter budget", "at": "the adapter budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="title",
    vo="One claim, one board, one run. A LoRA adapter is small enough to store in minutes but runs at the speed and memory cost of the base model it modifies. TINY FILE, FULL-SIZE FOOTPRINT.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="TINY FILE, FULL-SIZE FOOTPRINT",
    sub="A LoRA adapter is small enough to store in minutes but runs at the speed and memory cost of the base model it modifies.",
    art="token_blocks",
    head_at="TINY FILE, FULL-SIZE FOOTPRINT",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="nodes",
    vo="The lora figure, read straight off the board. Picture the magnifier pass. The added value parameters at rank sixteen. Total VRAM in use with a thirty-two thousand token context. The added parameters in one layer at rank sixteen.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="TINY FILE, FULL-SIZE FOOTPRINT",
    header_at="The lora figure",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    art_at="Picture the magnifier",
    chain=[{"t": "VALUE", "s": "This figure does not establish that a model fits.", "at": "The added value"}, {"t": "32K", "s": "This figure does not establish a speed.", "at": "Total VRAM in"}, {"t": "PER LAYER", "s": "This figure does not establish a fit claim.", "at": "The added parameters"}],
    source="derived &middot; rank 16 &middot; qwen2.5 3b instruct",
)

NAME = "BYTE-GEN-LORA-001"
TITLE = "TINY FILE, FULL-SIZE FOOTPRINT"
DOC_TITLE = "TINY FILE, FULL-SIZE FOOTPRINT &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
