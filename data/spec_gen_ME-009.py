# -*- coding: utf-8 -*-
"""Generated from angle ME-009 -- QUOTE THE RIG WITH THE NUMBER.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py ME-009
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same generation. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a four thousand token context. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="QUOTE THE RIG WITH THE NUMBER",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Same board",
    art_at="Picture the tokens",
    chips=[{"t": "4K", "c": "gold", "at": "Generation rate on"}],
    stats=[{"v": "22", "u": "s", "lab": "at 4,625 T/S", "c": "red", "at": "Time to the"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The generation figure, read straight off the board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a sixteen thousand token context. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="QUOTE THE RIG WITH THE NUMBER",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="The generation figure",
    art_at="Picture the tokens",
    chain=[{"t": "16K", "s": "This figure does not establish that a model fits.", "at": "Generation rate on"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about at 767 T/S, taken on trust.", "at": "Time to the"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One capacity number, one source, one board. Picture the window and what is in it. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="QUOTE THE RIG WITH THE NUMBER",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="One capacity number",
    art_at="Picture the window",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "gold", "at": "Generation rate on one"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "22.8 T/S", "sub": "128K", "cls": "", "at": "Generation rate on a"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a three thousand ninety with a sixty-four thousand token context. Generation rate on a five-oh-ninety with a four thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="QUOTE THE RIG WITH THE NUMBER",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Nothing here about",
    art_at="Picture the tokens",
    bars=[{"lab": "Qwen 3.8 27B", "val": "33.9", "unit": "T/S", "pct": 84.1, "cls": "", "at": "Generation rate on a three"}, {"lab": "Qwen 3.8 27B", "val": "74.8", "unit": "T/S", "pct": 100.0, "cls": "", "at": "Generation rate on a five-oh-ninety"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the generation of the hardware, not of the brochure. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a sixteen thousand token context. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="QUOTE THE RIG WITH THE NUMBER",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="This is the",
    art_at="Picture the tokens",
    rails=[{"lab": "16K", "val": "52.2", "pct": 69.8, "cls": "", "at": "Generation rate on"}, {"lab": "at 767 T/S", "val": "131", "pct": 100.0, "cls": "red", "at": "Time to the"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. A pair of cards never buys speed. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="QUOTE THE RIG WITH THE NUMBER",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Measured latency, on",
    art_at="Picture timing, line",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "The wait before any word appears, not the total run", "at": "The wait before"}, {"t": "A pair of cards never buys speed", "at": "A pair of"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every generation figure here carries its own source. Picture the tokens, one by one. On the bench: Qwen 3.8 27B. Generation rate on a three thousand ninety with a thirty-two thousand token context. The line reads thirty-three point nine tokens per second, from the same run.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="QUOTE THE RIG WITH THE NUMBER",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Every generation figure",
    art_at="Picture the tokens",
    name="Qwen 3.8 27B",
    blurb="Generation rate on a three thousand ninety with a thirty-two thousand token context",
    meta="64K &middot; 33.9 T/S",
    name_at="On the bench",
    blurb_at="Generation rate on",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The latency number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the decode budget figure, the latency budget figure, the context budget figure.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="QUOTE THE RIG WITH THE NUMBER",
    header_at="The latency number",
    items=[{"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-ME-009"
TITLE = "QUOTE THE RIG WITH THE NUMBER"
DOC_TITLE = "QUOTE THE RIG WITH THE NUMBER &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
