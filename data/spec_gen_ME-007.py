# -*- coding: utf-8 -*-
"""Generated from angle ME-007 -- THE USER WAS PART OF THE TIMER.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py ME-007
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same latency. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Prompt processing rate on a four thousand token prompt. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE USER WAS PART OF THE TIMER",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Same board",
    art_at="Picture timing, line",
    chips=[{"t": "at 4,625 T/S", "c": "gold", "at": "Time to the"}],
    stats=[{"v": "4625", "u": "T/S", "lab": "4K", "c": "gold", "at": "Prompt processing rate"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="chain",
    vo="The latency figure, read straight off the board. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Prompt processing rate on a sixteen thousand token prompt. Generation rate on a five-oh-ninety with a sixteen thousand token context.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE USER WAS PART OF THE TIMER",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="The latency figure",
    art_at="Picture timing, line",
    chain=[{"t": "at 767 T/S", "s": "The wait before any word appears, not the total run", "at": "Time to the"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Prompt processing rate"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 16K, taken on the board.", "at": "Generation rate on"}],
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="rows",
    vo="One generation number, one source, one board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a thirty-two thousand token context. Prompt processing rate on a one hundred twenty-eight thousand token prompt. Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE USER WAS PART OF THE TIMER",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="One generation number",
    art_at="Picture the tokens",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "gold", "at": "Generation rate on a five-oh-ninety with a thirty-two"}, {"rank": "2", "name": "Muse Glimmer 30B", "val": "2806 T/S", "sub": "128K", "cls": "", "at": "Prompt processing rate"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "22.8 T/S", "sub": "128K", "cls": "", "at": "Generation rate on a five-oh-ninety with a one"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a three thousand ninety with a four thousand token context. Prompt processing rate on a four thousand token prompt. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE USER WAS PART OF THE TIMER",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Nothing here about",
    art_at="Picture the tokens",
    bars=[{"lab": "Qwen 3.8 27B", "val": "40.3", "unit": "T/S", "pct": 100.0, "cls": "", "at": "Generation rate on"}, {"lab": "Qwen 3.8 27B", "val": "3749", "unit": "T/S", "pct": 100.0, "cls": "", "at": "Prompt processing rate"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the generation of the hardware, not of the brochure. Picture the tokens, one by one. Generation rate on a three thousand ninety with a sixty-four thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE USER WAS PART OF THE TIMER",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="This is the",
    art_at="Picture the tokens",
    rails=[{"lab": "64K", "val": "33.9", "pct": 84.1, "cls": "", "at": "Generation rate on"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE USER WAS PART OF THE TIMER",
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
    vo="Every latency figure here carries its own source. Picture timing, line by line. On the bench: Qwen 3.8 27B. Prompt processing rate on a sixteen thousand token prompt. The line reads fifty-two point two tokens per second, from the same run.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE USER WAS PART OF THE TIMER",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Every latency figure",
    art_at="Picture timing, line",
    name="Qwen 3.8 27B",
    blurb="Prompt processing rate on a sixteen thousand token prompt",
    meta="16K &middot; 52.2 T/S",
    name_at="On the bench",
    blurb_at="Prompt processing rate",
    meta_at="The line reads",
    side="right",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="strip",
    vo="The prefill number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the latency budget figure, the prefill budget figure, the decode budget figure.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE USER WAS PART OF THE TIMER",
    header_at="The prefill number",
    items=[{"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}, {"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}],
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="title",
    vo="One claim, one board, one run. The most common measurement mistake in local AI is reporting an end-to-end number that includes the operator's typing time. THE USER WAS PART OF THE TIMER.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE USER WAS PART OF THE TIMER",
    sub="The most common measurement mistake in local AI is reporting an end-to-end number that includes the operator's typing time.",
    art="token_blocks",
    head_at="THE USER WAS PART OF THE TIMER",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

NAME = "BYTE-GEN-ME-007"
TITLE = "THE USER WAS PART OF THE TIMER"
DOC_TITLE = "THE USER WAS PART OF THE TIMER &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
