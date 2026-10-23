# -*- coding: utf-8 -*-
"""Generated from angle LORA-010 -- ADAPTERS ARE TIED TO THEIR BASE.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py LORA-010
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same lora. Picture the magnifier pass. The layer count of the model. The LoRA paper's WikiSQL score for the full fine tune. Total VRAM in use with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="ADAPTERS ARE TIED TO THEIR BASE",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="Same board",
    art_at="Picture the magnifier",
    chips=[{"t": "LAYERS", "c": "gold", "at": "The layer count"}, {"t": "FT 73.8", "c": "cyan", "at": "The LoRA paper's"}],
    stats=[{"v": "18", "u": "GB", "lab": "4K", "c": "cyan", "at": "Total VRAM in"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="chain",
    vo="The lora figure, read straight off the board. Picture the magnifier pass. The number of key value heads, shared across groups. The LoRA paper's WikiSQL score for LoRA at rank four. Total VRAM in use with an eight thousand token context. The width of one attention head.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="ADAPTERS ARE TIED TO THEIR BASE",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="The lora figure",
    art_at="Picture the magnifier",
    chain=[{"t": "KV HEADS", "s": "This figure does not establish that a model fits.", "at": "The number of"}, {"t": "LO 89.5", "s": "This figure does not establish a speed.", "at": "The LoRA paper's"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 8K, taken on trust.", "at": "Total VRAM in"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of HEAD DIM, taken on the board.", "at": "The width of"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="rows",
    vo="One papers number, one source, one board. Picture the paper folder. The LoRA paper's MNLI score for the full fine tune. Total VRAM in use with a sixteen thousand token context. The hidden width of the model. The LoRA paper's MNLI score for LoRA at rank four. One method, every row.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="ADAPTERS ARE TIED TO THEIR BASE",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="One papers number",
    art_at="Picture the paper",
    rows=[{"rank": "1", "name": "GPT-3 175B", "val": "73.4", "sub": "FT 73.4", "cls": "gold", "at": "The LoRA paper's MNLI score for the"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "", "at": "Total VRAM in"}, {"rank": "3", "name": "Qwen2.5 3B Instruct", "val": "2048", "sub": "HIDDEN", "cls": "", "at": "The hidden width"}, {"rank": "4", "name": "GPT-3 175B", "val": "91.7", "sub": "LO 91.7", "cls": "", "at": "The LoRA paper's MNLI score for LoRA"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="bars",
    vo="Nothing here about lora is a guess. Picture the magnifier pass. The adapter arrays at thirty million trainable values. Total VRAM in use with a four thousand token context. Total VRAM in use with an eight thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="ADAPTERS ARE TIED TO THEIR BASE",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="Nothing here about",
    art_at="Picture the magnifier",
    bars=[{"lab": "Qwen2.5 3B Instruct", "val": "457", "unit": "MiB", "pct": 100.0, "cls": "red", "at": "The adapter arrays"}, {"lab": "Qwen 3.8 27B", "val": "18", "unit": "GB", "pct": 52.9, "cls": "", "at": "Total VRAM in use with a four"}, {"lab": "Qwen 3.8 27B", "val": "18", "unit": "GB", "pct": 52.9, "cls": "", "at": "Total VRAM in use with an"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="derived &middot; 30,000,000 values &middot; 16 bytes each &middot; an upper bound, not the exact count",
)

win(
    layout="rail",
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a one hundred twenty-eight thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="ADAPTERS ARE TIED TO THEIR BASE",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="This is the",
    art_at="Picture the vram",
    rails=[{"lab": "32K", "val": "20", "pct": 58.8, "cls": "", "at": "Total VRAM in use with a thirty-two"}, {"lab": "64K", "val": "22", "pct": 64.7, "cls": "", "at": "Total VRAM in use with a sixty-four"}, {"lab": "128K", "val": "26", "pct": 76.5, "cls": "", "at": "Total VRAM in use with a one"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured vram, on this board, in this run. Picture the vram sticks. Does not fit on a twenty-four gigabyte card at all. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="ADAPTERS ARE TIED TO THEIR BASE",
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
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Qwen 3.8 27B. The added query parameters at rank sixteen. The line reads forty-four point five, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="ADAPTERS ARE TIED TO THEIR BASE",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Qwen 3.8 27B",
    blurb="The added query parameters at rank sixteen",
    meta="QLoRA 44.5 &middot; 44.5",
    name_at="On the bench",
    blurb_at="The added query",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The papers number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the adapter budget figure, the paper budget figure, the vram budget figure.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="ADAPTERS ARE TIED TO THEIR BASE",
    header_at="The papers number",
    items=[{"key": "magnifier", "label": "adapter budget", "at": "the adapter budget figure"}, {"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="title",
    vo="One claim, one board, one run. An adapter tuned for one base model does not transfer to another, so the base is the expensive part of the adapter you keep. ADAPTERS ARE TIED TO THEIR BASE.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="ADAPTERS ARE TIED TO THEIR BASE",
    sub="An adapter tuned for one base model does not transfer to another, so the base is the expensive part of the adapter you keep.",
    art="vram_module",
    head_at="ADAPTERS ARE TIED TO THEIR BASE",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="nodes",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with a four thousand token context. The added value parameters at rank sixteen. The movement in MMLU between the full fine tune and QLoRA.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="ADAPTERS ARE TIED TO THEIR BASE",
    header_at="The vram figure",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    art_at="Picture the vram",
    chain=[{"t": "4K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}, {"t": "VALUE", "s": "This figure does not establish a speed.", "at": "The added value"}, {"t": "MMLU", "s": "This figure does not establish a fit claim.", "at": "The movement in"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-LORA-010"
TITLE = "ADAPTERS ARE TIED TO THEIR BASE"
DOC_TITLE = "ADAPTERS ARE TIED TO THEIR BASE &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
