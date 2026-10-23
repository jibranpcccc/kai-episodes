# -*- coding: utf-8 -*-
"""Generated from angle PF-014 -- THE FIRST TOKEN PAYS FOR THE WEIGHTS.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PF-014
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same prefill. Picture the prompt, incoming. Prompt processing rate on a four thousand token prompt. Total VRAM in use with a four thousand token context. Generation rate on a five-oh-ninety with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE FIRST TOKEN PAYS FOR THE WEIGHTS",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="Same board",
    art_at="Picture the prompt",
    chips=[{"t": "4K", "c": "gold", "at": "Prompt processing rate"}, {"t": "4K", "c": "cyan", "at": "Total VRAM in"}],
    stats=[{"v": "74.8", "u": "T/S", "lab": "4K", "c": "cyan", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The prefill figure, read straight off the board. Picture the prompt, incoming. Prompt processing rate on a sixteen thousand token prompt. Total VRAM in use with an eight thousand token context. Generation rate on a five-oh-ninety with a sixteen thousand token context. Prompt processing rate on a sixty-four thousand token prompt.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE FIRST TOKEN PAYS FOR THE WEIGHTS",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="The prefill figure",
    art_at="Picture the prompt",
    chain=[{"t": "16K", "s": "This figure does not establish that a model fits.", "at": "Prompt processing rate on a sixteen"}, {"t": "8K", "s": "This figure does not establish a speed.", "at": "Total VRAM in"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 64K, taken on the board.", "at": "Prompt processing rate on a sixty-four"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a sixteen thousand token context. Generation rate on a five-oh-ninety with a thirty-two thousand token context. Prompt processing rate on a one hundred twenty-eight thousand token prompt. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE FIRST TOKEN PAYS FOR THE WEIGHTS",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "gold", "at": "Total VRAM in"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "", "at": "Generation rate on"}, {"rank": "3", "name": "Muse Glimmer 30B", "val": "2806 T/S", "sub": "128K", "cls": "", "at": "Prompt processing rate"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context. Prompt processing rate on a two hundred fifty-six thousand token prompt. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE FIRST TOKEN PAYS FOR THE WEIGHTS",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Nothing here about",
    art_at="Picture the tokens",
    bars=[{"lab": "Qwen 3.8 27B", "val": "22.8", "unit": "T/S", "pct": 30.5, "cls": "", "at": "Generation rate on"}, {"lab": "Muse Glimmer 30B", "val": "1874", "unit": "T/S", "pct": 40.5, "cls": "", "at": "Prompt processing rate"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the prefill of the hardware, not of the brochure. Picture the prompt, incoming. Prompt processing rate on a four thousand token prompt. Total VRAM in use with a one hundred twenty-eight thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE FIRST TOKEN PAYS FOR THE WEIGHTS",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="This is the",
    art_at="Picture the prompt",
    rails=[{"lab": "4K", "val": "3749", "pct": 100.0, "cls": "", "at": "Prompt processing rate"}, {"lab": "128K", "val": "26", "pct": 76.5, "cls": "", "at": "Total VRAM in"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured vram, on this board, in this run. Picture the vram sticks. Does not fit on a twenty-four gigabyte card at all. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE FIRST TOKEN PAYS FOR THE WEIGHTS",
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
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Qwen 3.8 27B. Generation rate on a three thousand ninety with a sixty-four thousand token context. The line reads sixteen gigabytes, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE FIRST TOKEN PAYS FOR THE WEIGHTS",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Qwen 3.8 27B",
    blurb="Generation rate on a three thousand ninety with a sixty-four thousand token context",
    meta="4K &middot; 16 GB",
    name_at="On the bench",
    blurb_at="Generation rate on",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the prefill budget figure, the vram budget figure, the decode budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE FIRST TOKEN PAYS FOR THE WEIGHTS",
    header_at="The vram number",
    items=[{"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. Prefill time is spent reading weights as well as processing tokens, so a larger model can have a slower first token even on a faster card. THE FIRST TOKEN PAYS FOR THE WEIGHTS.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE FIRST TOKEN PAYS FOR THE WEIGHTS",
    sub="Prefill time is spent reading weights as well as processing tokens, so a larger model can have a slower first token even on a faster card.",
    art="token_blocks",
    head_at="THE FIRST TOKEN PAYS FOR THE WEIGHTS",
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="nodes",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with a thirty-two thousand token context. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE FIRST TOKEN PAYS FOR THE WEIGHTS",
    header_at="The vram figure",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    art_at="Picture the vram",
    chain=[{"t": "32K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in use with a thirty-two"}, {"t": "64K", "s": "This figure does not establish a speed.", "at": "Total VRAM in use with a sixty-four"}, {"t": "256K", "s": "This figure does not establish a fit claim.", "at": "Total VRAM in use with a two"}],
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-PF-014"
TITLE = "THE FIRST TOKEN PAYS FOR THE WEIGHTS"
DOC_TITLE = "THE FIRST TOKEN PAYS FOR THE WEIGHTS &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
