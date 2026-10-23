# -*- coding: utf-8 -*-
"""Generated from angle PA-010 -- REPRODUCE IT OR YOU DO NOT KNOW.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PA-010
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same papers. Picture the paper folder. The LoRA paper's WikiSQL score for the full fine tune. Generation rate on a five-oh-ninety with a four thousand token context. Total VRAM in use with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="REPRODUCE IT OR YOU DO NOT KNOW",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Same board",
    art_at="Picture the paper",
    chips=[{"t": "FT 73.8", "c": "gold", "at": "The LoRA paper's"}, {"t": "4K", "c": "cyan", "at": "Generation rate on"}],
    stats=[{"v": "18", "u": "GB", "lab": "4K", "c": "cyan", "at": "Total VRAM in"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="chain",
    vo="The latency figure, read straight off the board. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. The LoRA paper's WikiSQL score for LoRA at rank four.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="REPRODUCE IT OR YOU DO NOT KNOW",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="The latency figure",
    art_at="Picture timing, line",
    chain=[{"t": "at 4,625 T/S", "s": "The wait before any word appears, not the total run", "at": "Time to the"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about LO 89.5, taken on trust.", "at": "The LoRA paper's"}],
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="rows",
    vo="One latency number, one source, one board. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. The LoRA paper's MNLI score for the full fine tune. One method, every row.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="REPRODUCE IT OR YOU DO NOT KNOW",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="One latency number",
    art_at="Picture timing, line",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "131 s", "sub": "at 767 T/S", "cls": "gold", "at": "Time to the"}, {"rank": "2", "name": "GPT-3 175B", "val": "73.4", "sub": "FT 73.4", "cls": "", "at": "The LoRA paper's"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a sixty-four thousand token context. Generation rate on a three thousand ninety with a thirty-two thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="REPRODUCE IT OR YOU DO NOT KNOW",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Nothing here about",
    art_at="Picture the vram",
    bars=[{"lab": "Qwen 3.8 27B", "val": "22", "unit": "GB", "pct": 64.7, "cls": "", "at": "Total VRAM in"}, {"lab": "Qwen 3.8 27B", "val": "37.0", "unit": "T/S", "pct": 91.8, "cls": "", "at": "Generation rate on"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a two hundred fifty-six thousand token context. Total VRAM in use with a four thousand token context. Total VRAM in use with a thirty-two thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="REPRODUCE IT OR YOU DO NOT KNOW",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="This is the",
    art_at="Picture the vram",
    rails=[{"lab": "256K", "val": "34", "pct": 100.0, "cls": "red", "at": "Total VRAM in use with a two"}, {"lab": "4K", "val": "16", "pct": 47.1, "cls": "", "at": "Total VRAM in use with a four"}, {"lab": "32K", "val": "16", "pct": 47.1, "cls": "", "at": "Total VRAM in use with a thirty-two"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. Does not fit on a twenty-four gigabyte card at all. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="REPRODUCE IT OR YOU DO NOT KNOW",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Measured latency, on",
    art_at="Picture timing, line",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "The wait before any word appears, not the total run", "at": "The wait before"}, {"t": "Does not fit on a twenty-four gigabyte card at all", "at": "Does not fit"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every papers figure here carries its own source. Picture the paper folder. On the bench: Llama 7B. Generation rate on a three thousand ninety with a sixty-four thousand token context. The line reads thirty-four gigabytes, from the same run.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="REPRODUCE IT OR YOU DO NOT KNOW",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Every papers figure",
    art_at="Picture the paper",
    name="Llama 7B",
    blurb="Generation rate on a three thousand ninety with a sixty-four thousand token context",
    meta="256K &middot; 34 GB",
    name_at="On the bench",
    blurb_at="Generation rate on",
    meta_at="The line reads",
    side="right",
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; llama 7b on alpaca",
)

win(
    layout="strip",
    vo="The latency number does the talking, not the claim. Strip by strip: the paper budget figure, the decode budget figure, the vram budget figure, the latency budget figure.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="REPRODUCE IT OR YOU DO NOT KNOW",
    header_at="The latency number",
    items=[{"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="title",
    vo="One claim, one board, one run. Reproducing a paper's headline number on your own card is the only way to know whether the result depends on hardware you do not have. REPRODUCE IT OR YOU DO NOT KNOW.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="REPRODUCE IT OR YOU DO NOT KNOW",
    sub="Reproducing a paper's headline number on your own card is the only way to know whether the result depends on hardware you do not have.",
    art="folder",
    head_at="REPRODUCE IT OR YOU DO NOT KNOW",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="nodes",
    vo="The papers figure, read straight off the board. Picture the paper folder. The QLoRA paper's FLAN v2 score for QLoRA. Total VRAM in use with a four thousand token context. The movement in MMLU between the full fine tune and QLoRA.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="REPRODUCE IT OR YOU DO NOT KNOW",
    header_at="The papers figure",
    art="folder",
    art_caption="THE PAPER FOLDER",
    art_at="Picture the paper",
    chain=[{"t": "QLoRA 44.5", "s": "This figure does not establish that a model fits.", "at": "The QLoRA paper's"}, {"t": "4K", "s": "This figure does not establish a speed.", "at": "Total VRAM in"}, {"t": "MMLU", "s": "This figure does not establish a fit claim.", "at": "The movement in"}],
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; llama 7b on alpaca",
)

NAME = "BYTE-GEN-PA-010"
TITLE = "REPRODUCE IT OR YOU DO NOT KNOW"
DOC_TITLE = "REPRODUCE IT OR YOU DO NOT KNOW &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
