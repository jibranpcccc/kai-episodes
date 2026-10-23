# -*- coding: utf-8 -*-
"""Generated from angle PF-011 -- STARTUP IS SLOW. INFERENCE ISN'T..

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PF-011
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same latency. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Total VRAM in use with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="STARTUP IS SLOW. INFERENCE ISN'T.",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Same board",
    art_at="Picture timing, line",
    chips=[{"t": "at 4,625 T/S", "c": "gold", "at": "Time to the"}],
    stats=[{"v": "18", "u": "GB", "lab": "4K", "c": "gold", "at": "Total VRAM in"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="chain",
    vo="The latency figure, read straight off the board. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Total VRAM in use with an eight thousand token context. Prompt processing rate on a sixteen thousand token prompt.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="STARTUP IS SLOW. INFERENCE ISN'T.",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="The latency figure",
    art_at="Picture timing, line",
    chain=[{"t": "at 767 T/S", "s": "The wait before any word appears, not the total run", "at": "Time to the"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 8K, taken on trust.", "at": "Total VRAM in"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 16K, taken on the board.", "at": "Prompt processing rate"}],
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="rows",
    vo="One prefill number, one source, one board. Picture the prompt, incoming. Prompt processing rate on a sixty-four thousand token prompt. Total VRAM in use with a thirty-two thousand token context. Prompt processing rate on a one hundred twenty-eight thousand token prompt. One method, every row.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="STARTUP IS SLOW. INFERENCE ISN'T.",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="One prefill number",
    art_at="Picture the prompt",
    rows=[{"rank": "1", "name": "Muse Glimmer 30B", "val": "3606 T/S", "sub": "64K", "cls": "gold", "at": "Prompt processing rate on a sixty-four"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "20 GB", "sub": "32K", "cls": "", "at": "Total VRAM in"}, {"rank": "3", "name": "Muse Glimmer 30B", "val": "2806 T/S", "sub": "128K", "cls": "", "at": "Prompt processing rate on a one"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about prefill is a guess. Picture the prompt, incoming. Prompt processing rate on a two hundred fifty-six thousand token prompt. Total VRAM in use with a one hundred twenty-eight thousand token context. Prompt processing rate on a four thousand token prompt. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="STARTUP IS SLOW. INFERENCE ISN'T.",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="Nothing here about",
    art_at="Picture the prompt",
    bars=[{"lab": "Muse Glimmer 30B", "val": "1874", "unit": "T/S", "pct": 40.5, "cls": "", "at": "Prompt processing rate on a two"}, {"lab": "Qwen 3.8 27B", "val": "26", "unit": "GB", "pct": 76.5, "cls": "", "at": "Total VRAM in"}, {"lab": "Qwen 3.8 27B", "val": "3749", "unit": "T/S", "pct": 100.0, "cls": "", "at": "Prompt processing rate on a four"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the prefill of the hardware, not of the brochure. Picture the prompt, incoming. Prompt processing rate on a one hundred twenty-eight thousand token prompt. Total VRAM in use with a four thousand token context. Total VRAM in use with a thirty-two thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="STARTUP IS SLOW. INFERENCE ISN'T.",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="This is the",
    art_at="Picture the prompt",
    rails=[{"lab": "128K", "val": "461", "pct": 12.3, "cls": "", "at": "Prompt processing rate"}, {"lab": "4K", "val": "16", "pct": 47.1, "cls": "", "at": "Total VRAM in use with a four"}, {"lab": "32K", "val": "16", "pct": 47.1, "cls": "", "at": "Total VRAM in use with a thirty-two"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. Does not fit on a twenty-four gigabyte card at all. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="STARTUP IS SLOW. INFERENCE ISN'T.",
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
    vo="Every latency figure here carries its own source. Picture timing, line by line. On the bench: Muse Glimmer 30B. Total VRAM in use with a four thousand token context. The line reads four thousand six hundred and twenty-five tokens per second, from the same run.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="STARTUP IS SLOW. INFERENCE ISN'T.",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Every latency figure",
    art_at="Picture timing, line",
    name="Muse Glimmer 30B",
    blurb="Total VRAM in use with a four thousand token context",
    meta="4K &middot; 4625 T/S",
    name_at="On the bench",
    blurb_at="Total VRAM in",
    meta_at="The line reads",
    side="right",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the latency budget figure, the vram budget figure, the prefill budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="STARTUP IS SLOW. INFERENCE ISN'T.",
    header_at="The vram number",
    items=[{"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}],
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="title",
    vo="One claim, one board, one run. Disk residency at model load makes startup slow, but it does not affect the wait for the first token once the model is resident. STARTUP IS SLOW. INFERENCE ISN'T.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="STARTUP IS SLOW. INFERENCE ISN'T.",
    sub="Disk residency at model load makes startup slow, but it does not affect the wait for the first token once the model is resident.",
    art="prompt_stream",
    head_at="STARTUP IS SLOW. INFERENCE ISN'T.",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="nodes",
    vo="The latency figure, read straight off the board. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Total VRAM in use with an eight thousand token context. Prompt processing rate on a sixteen thousand token prompt.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="STARTUP IS SLOW. INFERENCE ISN'T.",
    header_at="The latency figure",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    art_at="Picture timing, line",
    chain=[{"t": "at 767 T/S", "s": "The wait before any word appears, not the total run", "at": "Time to the"}, {"t": "8K", "s": "This figure does not establish a speed.", "at": "Total VRAM in"}, {"t": "16K", "s": "This figure does not establish a fit claim.", "at": "Prompt processing rate"}],
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

NAME = "BYTE-GEN-PF-011"
TITLE = "STARTUP IS SLOW. INFERENCE ISN'T."
DOC_TITLE = "STARTUP IS SLOW. INFERENCE ISN'T. &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
