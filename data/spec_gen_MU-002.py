# -*- coding: utf-8 -*-
"""Generated from angle MU-002 -- THE SLOT IS THE BOTTLENECK.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py MU-002
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same vram. Picture the vram sticks. Total VRAM in use with a four thousand token context. Generation rate on a five-oh-ninety with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE SLOT IS THE BOTTLENECK",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Same board",
    art_at="Picture the vram",
    chips=[{"t": "4K", "c": "gold", "at": "Total VRAM in"}],
    stats=[{"v": "74.8", "u": "T/S", "lab": "4K", "c": "gold", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with an eight thousand token context. Generation rate on a five-oh-ninety with a sixteen thousand token context. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE SLOT IS THE BOTTLENECK",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="The vram figure",
    art_at="Picture the vram",
    chain=[{"t": "8K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of at 767 T/S, taken on the board.", "at": "Time to the"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One generation number, one source, one board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a thirty-two thousand token context. Total VRAM in use with a thirty-two thousand token context. Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE SLOT IS THE BOTTLENECK",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="One generation number",
    art_at="Picture the tokens",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "gold", "at": "Generation rate on a five-oh-ninety with a thirty-two"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "20 GB", "sub": "32K", "cls": "", "at": "Total VRAM in"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "22.8 T/S", "sub": "128K", "cls": "", "at": "Generation rate on a five-oh-ninety with a one"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a three thousand ninety with a four thousand token context. Total VRAM in use with a one hundred twenty-eight thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE SLOT IS THE BOTTLENECK",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Nothing here about",
    art_at="Picture the tokens",
    bars=[{"lab": "Qwen 3.8 27B", "val": "40.3", "unit": "T/S", "pct": 100.0, "cls": "", "at": "Generation rate on"}, {"lab": "Qwen 3.8 27B", "val": "26", "unit": "GB", "pct": 76.5, "cls": "", "at": "Total VRAM in"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the generation of the hardware, not of the brochure. Picture the tokens, one by one. Generation rate on a three thousand ninety with a sixty-four thousand token context. Total VRAM in use with a four thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE SLOT IS THE BOTTLENECK",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="This is the",
    art_at="Picture the tokens",
    rails=[{"lab": "64K", "val": "33.9", "pct": 84.1, "cls": "", "at": "Generation rate on"}, {"lab": "4K", "val": "16", "pct": 47.1, "cls": "", "at": "Total VRAM in"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. Does not fit on a twenty-four gigabyte card at all. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE SLOT IS THE BOTTLENECK",
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
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Qwen 3.8 27B. Generation rate on a five-oh-ninety with a four thousand token context. The line reads twenty-two seconds, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE SLOT IS THE BOTTLENECK",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Qwen 3.8 27B",
    blurb="Generation rate on a five-oh-ninety with a four thousand token context",
    meta="at 4,625 T/S &middot; 22 s",
    name_at="On the bench",
    blurb_at="Generation rate on",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The generation number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the vram budget figure, the decode budget figure, the latency budget figure.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE SLOT IS THE BOTTLENECK",
    header_at="The generation number",
    items=[{"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. When a layer is offloaded to system RAM, the token waits for the PCIe link, which is why offload turns a fast card into a slow machine. THE SLOT IS THE BOTTLENECK.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE SLOT IS THE BOTTLENECK",
    sub="When a layer is offloaded to system RAM, the token waits for the PCIe link, which is why offload turns a fast card into a slow machine.",
    art="timer_flat",
    head_at="THE SLOT IS THE BOTTLENECK",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="nodes",
    vo="The vram figure, read straight off the board. Picture the vram sticks. Total VRAM in use with an eight thousand token context. Generation rate on a five-oh-ninety with a sixteen thousand token context. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="THE SLOT IS THE BOTTLENECK",
    header_at="The vram figure",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    art_at="Picture the vram",
    chain=[{"t": "8K", "s": "This figure does not establish that a model fits.", "at": "Total VRAM in"}, {"t": "16K", "s": "This figure does not establish a speed.", "at": "Generation rate on"}, {"t": "at 767 T/S", "s": "The wait before any word appears, not the total run", "at": "Time to the"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-MU-002"
TITLE = "THE SLOT IS THE BOTTLENECK"
DOC_TITLE = "THE SLOT IS THE BOTTLENECK &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
