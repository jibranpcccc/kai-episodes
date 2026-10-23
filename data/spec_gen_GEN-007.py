# -*- coding: utf-8 -*-
"""Generated from angle GEN-007 -- FEWER TOKENS IS A FASTER ANSWER.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py GEN-007
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same generation. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a four thousand token context. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="FEWER TOKENS IS A FASTER ANSWER",
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
    vo="The latency figure, read straight off the board. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Generation rate on a five-oh-ninety with a thirty-two thousand token context.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="FEWER TOKENS IS A FASTER ANSWER",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="The latency figure",
    art_at="Picture timing, line",
    chain=[{"t": "at 767 T/S", "s": "The wait before any word appears, not the total run", "at": "Time to the"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 32K, taken on trust.", "at": "Generation rate on"}],
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="rows",
    vo="One generation number, one source, one board. Picture the tokens, one by one. Generation rate on a three thousand ninety with a thirty-two thousand token context. Generation rate on a three thousand ninety with a sixty-four thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="FEWER TOKENS IS A FASTER ANSWER",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="One generation number",
    art_at="Picture the tokens",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "37.0 T/S", "sub": "32K", "cls": "gold", "at": "Generation rate on a three thousand ninety with a thirty-two"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "33.9 T/S", "sub": "64K", "cls": "", "at": "Generation rate on a three thousand ninety with a sixty-four"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a sixteen thousand token context. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="FEWER TOKENS IS A FASTER ANSWER",
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
    title="FEWER TOKENS IS A FASTER ANSWER",
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
    title="FEWER TOKENS IS A FASTER ANSWER",
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
    vo="Every latency figure here carries its own source. Picture timing, line by line. On the bench: Muse Glimmer 30B. Generation rate on a five-oh-ninety with a sixteen thousand token context. The line reads one hundred and thirty-one seconds, from the same run.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="FEWER TOKENS IS A FASTER ANSWER",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Every latency figure",
    art_at="Picture timing, line",
    name="Muse Glimmer 30B",
    blurb="Generation rate on a five-oh-ninety with a sixteen thousand token context",
    meta="at 767 T/S &middot; 131 s",
    name_at="On the bench",
    blurb_at="Generation rate on",
    meta_at="The line reads",
    side="right",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

NAME = "BYTE-GEN-GEN-007"
TITLE = "FEWER TOKENS IS A FASTER ANSWER"
DOC_TITLE = "FEWER TOKENS IS A FASTER ANSWER &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
