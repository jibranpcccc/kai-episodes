# -*- coding: utf-8 -*-
"""Generated from angle LORA-005 -- MERGE IT AND THE OVERHEAD DISAPPEARS.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py LORA-005
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same lora. Picture the magnifier pass. The layer count of the model. Generation rate on a five-oh-ninety with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="MERGE IT AND THE OVERHEAD DISAPPEARS",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="Same board",
    art_at="Picture the magnifier",
    chips=[{"t": "LAYERS", "c": "gold", "at": "The layer count"}],
    stats=[{"v": "74.8", "u": "T/S", "lab": "4K", "c": "gold", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="chain",
    vo="The lora figure, read straight off the board. Picture the magnifier pass. The number of key value heads, shared across groups. Generation rate on a five-oh-ninety with a sixteen thousand token context. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="MERGE IT AND THE OVERHEAD DISAPPEARS",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="The lora figure",
    art_at="Picture the magnifier",
    chain=[{"t": "KV HEADS", "s": "This figure does not establish that a model fits.", "at": "The number of"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of at 767 T/S, taken on the board.", "at": "Time to the"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="rows",
    vo="One generation number, one source, one board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a thirty-two thousand token context. The hidden width of the model. Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="MERGE IT AND THE OVERHEAD DISAPPEARS",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="One generation number",
    art_at="Picture the tokens",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "gold", "at": "Generation rate on a five-oh-ninety with a thirty-two"}, {"rank": "2", "name": "Qwen2.5 3B Instruct", "val": "2048", "sub": "HIDDEN", "cls": "", "at": "The hidden width"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "22.8 T/S", "sub": "128K", "cls": "", "at": "Generation rate on a five-oh-ninety with a one"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about latency is a guess. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="MERGE IT AND THE OVERHEAD DISAPPEARS",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Nothing here about",
    art_at="Picture timing, line",
    bars=[{"lab": "Muse Glimmer 30B", "val": "22", "unit": "s", "pct": 17.0, "cls": "red", "at": "Time to the"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="rail",
    vo="This is the generation of the hardware, not of the brochure. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context. Generation rate on a three thousand ninety with a four thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="MERGE IT AND THE OVERHEAD DISAPPEARS",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="This is the",
    art_at="Picture the tokens",
    rails=[{"lab": "128K", "val": "22.8", "pct": 30.5, "cls": "", "at": "Generation rate on a five-oh-ninety"}, {"lab": "4K", "val": "40.3", "pct": 100.0, "cls": "", "at": "Generation rate on a three"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="MERGE IT AND THE OVERHEAD DISAPPEARS",
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
    vo="Every lora figure here carries its own source. Picture the magnifier pass. On the bench: Qwen2.5 3B Instruct. The bytes per trainable value, across the weight, the gradient and the optimizer state. The line reads four hundred and fifty-seven mebibytes, from the same run.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="MERGE IT AND THE OVERHEAD DISAPPEARS",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="Every lora figure",
    art_at="Picture the magnifier",
    name="Qwen2.5 3B Instruct",
    blurb="The bytes per trainable value, across the weight, the gradient and the optimizer state",
    meta="AT 30M &middot; 457 MiB",
    name_at="On the bench",
    blurb_at="The bytes per",
    meta_at="The line reads",
    side="right",
    source="derived &middot; rank 16 &middot; seven projections targeted &middot; qwen2.5 3b instruct",
)

win(
    layout="strip",
    vo="The generation number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the adapter budget figure, the decode budget figure, the latency budget figure.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="MERGE IT AND THE OVERHEAD DISAPPEARS",
    header_at="The generation number",
    items=[{"key": "magnifier", "label": "adapter budget", "at": "the adapter budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="title",
    vo="One claim, one board, one run. Merging the adapter into the base weights before serving removes the adapter overhead at runtime, which makes offline use faster than live use. MERGE IT AND THE OVERHEAD DISAPPEARS.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="MERGE IT AND THE OVERHEAD DISAPPEARS",
    sub="Merging the adapter into the base weights before serving removes the adapter overhead at runtime, which makes offline use faster than live use.",
    art="timer_flat",
    head_at="MERGE IT AND THE OVERHEAD DISAPPEARS",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="nodes",
    vo="The lora figure, read straight off the board. Picture the magnifier pass. The parameters in the tied embedding matrix. The tied embedding matrix in decimal gigabytes, in full precision. The layer count of the model.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="MERGE IT AND THE OVERHEAD DISAPPEARS",
    header_at="The lora figure",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    art_at="Picture the magnifier",
    chain=[{"t": "TIED", "s": "This figure does not establish that a model fits.", "at": "The parameters in"}, {"t": "TENSOR", "s": "This figure does not establish a speed.", "at": "The tied embedding matrix in"}, {"t": "LAYERS", "s": "This figure does not establish a fit claim.", "at": "The layer count"}],
    source="derived &middot; 151,936 rows &times; 2,048 wide &middot; qwen2.5 3b instruct",
)

NAME = "BYTE-GEN-LORA-005"
TITLE = "MERGE IT AND THE OVERHEAD DISAPPEARS"
DOC_TITLE = "MERGE IT AND THE OVERHEAD DISAPPEARS &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
