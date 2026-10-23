# -*- coding: utf-8 -*-
"""Generated from angle PF-004 -- THE WAIT SCALES WITH WHAT YOU SENT.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PF-004
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same prefill. Picture the prompt, incoming. Prompt processing rate on a four thousand token prompt. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE WAIT SCALES WITH WHAT YOU SENT",
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
    vo="The latency figure, read straight off the board. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Prompt processing rate on a sixty-four thousand token prompt. Prompt processing rate on a one hundred twenty-eight thousand token prompt.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE WAIT SCALES WITH WHAT YOU SENT",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="The latency figure",
    art_at="Picture timing, line",
    chain=[{"t": "at 767 T/S", "s": "The wait before any word appears, not the total run", "at": "Time to the"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 64K, taken on trust.", "at": "Prompt processing rate on a sixty-four"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 128K, taken on the board.", "at": "Prompt processing rate on a one"}],
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="rows",
    vo="One prefill number, one source, one board. Picture the prompt, incoming. Prompt processing rate on a four thousand token prompt. Prompt processing rate on a one hundred twenty-eight thousand token prompt. Prompt processing rate on a four thousand token prompt. One method, every row.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE WAIT SCALES WITH WHAT YOU SENT",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="One prefill number",
    art_at="Picture the prompt",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "3749 T/S", "sub": "4K", "cls": "gold", "at": "Prompt processing rate on a four thousand token prompt. Prompt"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "461 T/S", "sub": "128K", "cls": "", "at": "processing rate on a one"}, {"rank": "3", "name": "Muse Glimmer 30B", "val": "4625 T/S", "sub": "4K", "cls": "", "at": "Prompt processing rate on a four thousand token prompt. One"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "method, every row"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about prefill is a guess. Picture the prompt, incoming. Prompt processing rate on a sixteen thousand token prompt. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE WAIT SCALES WITH WHAT YOU SENT",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="Nothing here about",
    art_at="Picture the prompt",
    bars=[{"lab": "Muse Glimmer 30B", "val": "4373", "unit": "T/S", "pct": 94.5, "cls": "", "at": "Prompt processing rate"}, {"lab": "Qwen 3.8 27B", "val": "131", "unit": "s", "pct": 100.0, "cls": "red", "at": "Time to the"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the prefill of the hardware, not of the brochure. Picture the prompt, incoming. Prompt processing rate on a two hundred fifty-six thousand token prompt. Prompt processing rate on a four thousand token prompt. Prompt processing rate on a one hundred twenty-eight thousand token prompt. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE WAIT SCALES WITH WHAT YOU SENT",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="This is the",
    art_at="Picture the prompt",
    rails=[{"lab": "256K", "val": "1874", "pct": 40.5, "cls": "", "at": "Prompt processing rate on a two"}, {"lab": "4K", "val": "3749", "pct": 100.0, "cls": "", "at": "Prompt processing rate on a four"}, {"lab": "128K", "val": "461", "pct": 12.3, "cls": "", "at": "Prompt processing rate on a one"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE WAIT SCALES WITH WHAT YOU SENT",
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
    vo="Every latency figure here carries its own source. Picture timing, line by line. On the bench: Muse Glimmer 30B. Prompt processing rate on a sixteen thousand token prompt. The line reads one hundred and thirty-one seconds, from the same run.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE WAIT SCALES WITH WHAT YOU SENT",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Every latency figure",
    art_at="Picture timing, line",
    name="Muse Glimmer 30B",
    blurb="Prompt processing rate on a sixteen thousand token prompt",
    meta="at 767 T/S &middot; 131 s",
    name_at="On the bench",
    blurb_at="Prompt processing rate",
    meta_at="The line reads",
    side="right",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

NAME = "BYTE-GEN-PF-004"
TITLE = "THE WAIT SCALES WITH WHAT YOU SENT"
DOC_TITLE = "THE WAIT SCALES WITH WHAT YOU SENT &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
