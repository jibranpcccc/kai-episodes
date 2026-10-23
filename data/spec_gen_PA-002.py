# -*- coding: utf-8 -*-
"""Generated from angle PA-002 -- THE BASELINE MAY HAVE BEEN SPILLING.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PA-002
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same papers. Picture the paper folder. The LoRA paper's WikiSQL score for the full fine tune. Total VRAM in use with a four thousand token context. Generation rate on a five-oh-ninety with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="THE BASELINE MAY HAVE BEEN SPILLING",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Same board",
    art_at="Picture the paper",
    chips=[{"t": "FT 73.8", "c": "gold", "at": "The LoRA paper's"}, {"t": "4K", "c": "cyan", "at": "Total VRAM in"}],
    stats=[{"v": "74.8", "u": "T/S", "lab": "4K", "c": "cyan", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="chain",
    vo="The papers figure, read straight off the board. Picture the paper folder. The LoRA paper's WikiSQL score for LoRA at rank four. Total VRAM in use with an eight thousand token context. Generation rate on a five-oh-ninety with a sixteen thousand token context.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="THE BASELINE MAY HAVE BEEN SPILLING",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="The papers figure",
    art_at="Picture the paper",
    chain=[{"t": "LO 89.5", "s": "This figure does not establish that a model fits.", "at": "The LoRA paper's"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 8K, taken on trust.", "at": "Total VRAM in"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 16K, taken on the board.", "at": "Generation rate on"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a sixteen thousand token context. Generation rate on a five-oh-ninety with a thirty-two thousand token context. The LoRA paper's MNLI score for LoRA at rank four. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE BASELINE MAY HAVE BEEN SPILLING",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "gold", "at": "Total VRAM in"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "", "at": "Generation rate on"}, {"rank": "3", "name": "GPT-3 175B", "val": "91.7", "sub": "LO 91.7", "cls": "", "at": "The LoRA paper's"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a three thousand ninety with a thirty-two thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE BASELINE MAY HAVE BEEN SPILLING",
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
    title="THE BASELINE MAY HAVE BEEN SPILLING",
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
    title="THE BASELINE MAY HAVE BEEN SPILLING",
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
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Qwen 3.8 27B. Generation rate on a three thousand ninety with a sixty-four thousand token context. The line reads forty-four point five, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE BASELINE MAY HAVE BEEN SPILLING",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Qwen 3.8 27B",
    blurb="Generation rate on a three thousand ninety with a sixty-four thousand token context",
    meta="QLoRA 44.5 &middot; 44.5",
    name_at="On the bench",
    blurb_at="Generation rate on",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the paper budget figure, the vram budget figure, the decode budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE BASELINE MAY HAVE BEEN SPILLING",
    header_at="The vram number",
    items=[{"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="title",
    vo="One claim, one board, one run. A paper that reports a speedup without reporting whether the baseline also spilled to disk has not measured the thing you care about. THE BASELINE MAY HAVE BEEN SPILLING.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE BASELINE MAY HAVE BEEN SPILLING",
    sub="A paper that reports a speedup without reporting whether the baseline also spilled to disk has not measured the thing you care about.",
    art="token_blocks",
    head_at="THE BASELINE MAY HAVE BEEN SPILLING",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="nodes",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with a four thousand token context. The movement in MMLU between the full fine tune and QLoRA. Total VRAM in use with a thirty-two thousand token context.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE BASELINE MAY HAVE BEEN SPILLING",
    header_at="The vram figure",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    art_at="Picture the vram",
    chain=[{"t": "4K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in use with a four"}, {"t": "MMLU", "s": "This figure does not establish a speed.", "at": "The movement in"}, {"t": "32K", "s": "This figure does not establish a fit claim.", "at": "Total VRAM in use with a thirty-two"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-PA-002"
TITLE = "THE BASELINE MAY HAVE BEEN SPILLING"
DOC_TITLE = "THE BASELINE MAY HAVE BEEN SPILLING &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
