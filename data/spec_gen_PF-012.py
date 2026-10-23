# -*- coding: utf-8 -*-
"""Generated from angle PF-012 -- FIRST TOKEN TELLS YOU WHICH CARD.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PF-012
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same prefill. Picture the prompt, incoming. Prompt processing rate on a four thousand token prompt. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="FIRST TOKEN TELLS YOU WHICH CARD",
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
    vo="The prefill figure, read straight off the board. Picture the prompt, incoming. Prompt processing rate on a sixteen thousand token prompt. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Total VRAM in use with an eight thousand token context.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="FIRST TOKEN TELLS YOU WHICH CARD",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="The prefill figure",
    art_at="Picture the prompt",
    chain=[{"t": "16K", "s": "This figure does not establish that a model fits.", "at": "Prompt processing rate"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about at 767 T/S, taken on trust.", "at": "Time to the"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 8K, taken on the board.", "at": "Total VRAM in"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a sixteen thousand token context. Prompt processing rate on a one hundred twenty-eight thousand token prompt. Total VRAM in use with a thirty-two thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="FIRST TOKEN TELLS YOU WHICH CARD",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "gold", "at": "Total VRAM in use with a sixteen"}, {"rank": "2", "name": "Muse Glimmer 30B", "val": "2806 T/S", "sub": "128K", "cls": "", "at": "Prompt processing rate"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "20 GB", "sub": "32K", "cls": "", "at": "Total VRAM in use with a thirty-two"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a sixty-four thousand token context. Prompt processing rate on a four thousand token prompt. Total VRAM in use with a one hundred twenty-eight thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="FIRST TOKEN TELLS YOU WHICH CARD",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Nothing here about",
    art_at="Picture the vram",
    bars=[{"lab": "Qwen 3.8 27B", "val": "22", "unit": "GB", "pct": 64.7, "cls": "", "at": "Total VRAM in use with a sixty-four"}, {"lab": "Qwen 3.8 27B", "val": "3749", "unit": "T/S", "pct": 100.0, "cls": "", "at": "Prompt processing rate"}, {"lab": "Qwen 3.8 27B", "val": "26", "unit": "GB", "pct": 76.5, "cls": "", "at": "Total VRAM in use with a one"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the vram of the hardware, not of the brochure. Picture the vram sticks. Total VRAM in use with a two hundred fifty-six thousand token context. Total VRAM in use with a four thousand token context. Total VRAM in use with a thirty-two thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="FIRST TOKEN TELLS YOU WHICH CARD",
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
    title="FIRST TOKEN TELLS YOU WHICH CARD",
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
    vo="Every prefill figure here carries its own source. Picture the prompt, incoming. On the bench: Muse Glimmer 30B. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. The line reads eighteen gigabytes, from the same run.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="FIRST TOKEN TELLS YOU WHICH CARD",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="Every prefill figure",
    art_at="Picture the prompt",
    name="Muse Glimmer 30B",
    blurb="Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second",
    meta="4K &middot; 18 GB",
    name_at="On the bench",
    blurb_at="Time to the",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The latency number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the prefill budget figure, the latency budget figure, the vram budget figure.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="FIRST TOKEN TELLS YOU WHICH CARD",
    header_at="The latency number",
    items=[{"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. The same model gives different first-token waits on different cards, so the card choice is a latency choice before it is a capacity choice. FIRST TOKEN TELLS YOU WHICH CARD.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="FIRST TOKEN TELLS YOU WHICH CARD",
    sub="The same model gives different first-token waits on different cards, so the card choice is a latency choice before it is a capacity choice.",
    art="vram_module",
    head_at="FIRST TOKEN TELLS YOU WHICH CARD",
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="nodes",
    vo="The prefill figure, read straight off the board. Picture the prompt, incoming. Prompt processing rate on a sixteen thousand token prompt. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Total VRAM in use with an eight thousand token context.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="FIRST TOKEN TELLS YOU WHICH CARD",
    header_at="The prefill figure",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    art_at="Picture the prompt",
    chain=[{"t": "16K", "s": "This figure does not establish that a model fits.", "at": "Prompt processing rate"}, {"t": "at 767 T/S", "s": "The wait before any word appears, not the total run", "at": "Time to the"}, {"t": "8K", "s": "This figure does not establish a fit claim.", "at": "Total VRAM in"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-PF-012"
TITLE = "FIRST TOKEN TELLS YOU WHICH CARD"
DOC_TITLE = "FIRST TOKEN TELLS YOU WHICH CARD &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
