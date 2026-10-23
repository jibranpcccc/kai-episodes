# -*- coding: utf-8 -*-
"""Generated from angle PA-001 -- A BENCHMARK NUMBER WITHOUT SETUP.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PA-001
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same papers. Picture the paper folder. The LoRA paper's WikiSQL score for the full fine tune. Generation rate on a five-oh-ninety with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="A BENCHMARK NUMBER WITHOUT SETUP",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Same board",
    art_at="Picture the paper",
    chips=[{"t": "FT 73.8", "c": "gold", "at": "The LoRA paper's"}],
    stats=[{"v": "74.8", "u": "T/S", "lab": "4K", "c": "gold", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="chain",
    vo="The papers figure, read straight off the board. Picture the paper folder. The LoRA paper's WikiSQL score for LoRA at rank four. Generation rate on a five-oh-ninety with a sixteen thousand token context. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="A BENCHMARK NUMBER WITHOUT SETUP",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="The papers figure",
    art_at="Picture the paper",
    chain=[{"t": "LO 89.5", "s": "This figure does not establish that a model fits.", "at": "The LoRA paper's"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of at 767 T/S, taken on the board.", "at": "Time to the"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="rows",
    vo="One generation number, one source, one board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a thirty-two thousand token context. The LoRA paper's MNLI score for LoRA at rank four. Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="A BENCHMARK NUMBER WITHOUT SETUP",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="One generation number",
    art_at="Picture the tokens",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "gold", "at": "Generation rate on a five-oh-ninety with a thirty-two"}, {"rank": "2", "name": "GPT-3 175B", "val": "91.7", "sub": "LO 91.7", "cls": "", "at": "The LoRA paper's"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "22.8 T/S", "sub": "128K", "cls": "", "at": "Generation rate on a five-oh-ninety with a one"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a sixteen thousand token context. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="A BENCHMARK NUMBER WITHOUT SETUP",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Nothing here about",
    art_at="Picture the tokens",
    bars=[{"lab": "Qwen 3.8 27B", "val": "52.2", "unit": "T/S", "pct": 69.8, "cls": "", "at": "Generation rate on"}, {"lab": "Qwen 3.8 27B", "val": "131", "unit": "s", "pct": 100.0, "cls": "red", "at": "Time to the"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the generation of the hardware, not of the brochure. Picture the tokens, one by one. Generation rate on a three thousand ninety with a four thousand token context. Generation rate on a three thousand ninety with a thirty-two thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="A BENCHMARK NUMBER WITHOUT SETUP",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="This is the",
    art_at="Picture the tokens",
    rails=[{"lab": "4K", "val": "40.3", "pct": 100.0, "cls": "", "at": "Generation rate on a three thousand ninety with a four"}, {"lab": "32K", "val": "37.0", "pct": 91.8, "cls": "", "at": "Generation rate on a three thousand ninety with a thirty-two"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="A BENCHMARK NUMBER WITHOUT SETUP",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Measured latency, on",
    art_at="Picture timing, line",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "The wait before any word appears, not the total run", "at": "The wait before"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every papers figure here carries its own source. Picture the paper folder. On the bench: Llama 65B. The size of the card in that demonstration. The line reads seventy-three point eight, from the same run.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="A BENCHMARK NUMBER WITHOUT SETUP",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Every papers figure",
    art_at="Picture the paper",
    name="Llama 65B",
    blurb="The size of the card in that demonstration",
    meta="FT 73.8 &middot; 73.8",
    name_at="On the bench",
    blurb_at="The size of",
    meta_at="The line reads",
    side="right",
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; 65b on one 48 gb card",
)

win(
    layout="strip",
    vo="The generation number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the paper budget figure, the decode budget figure, the latency budget figure.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="A BENCHMARK NUMBER WITHOUT SETUP",
    header_at="The generation number",
    items=[{"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="title",
    vo="One claim, one board, one run. A paper's reported tokens per second are a property of a specific configuration, so the number is meaningless without its hardware and batch size. A BENCHMARK NUMBER WITHOUT SETUP.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="A BENCHMARK NUMBER WITHOUT SETUP",
    sub="A paper's reported tokens per second are a property of a specific configuration, so the number is meaningless without its hardware and batch size.",
    art="timer_flat",
    head_at="A BENCHMARK NUMBER WITHOUT SETUP",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="nodes",
    vo="The generation figure, read straight off the board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a four thousand token context. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="A BENCHMARK NUMBER WITHOUT SETUP",
    header_at="The generation figure",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    art_at="Picture the tokens",
    chain=[{"t": "4K", "s": "This figure does not establish that a model fits.", "at": "Generation rate on"}, {"t": "at 4,625 T/S", "s": "The wait before any word appears, not the total run", "at": "Time to the"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-PA-001"
TITLE = "A BENCHMARK NUMBER WITHOUT SETUP"
DOC_TITLE = "A BENCHMARK NUMBER WITHOUT SETUP &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
