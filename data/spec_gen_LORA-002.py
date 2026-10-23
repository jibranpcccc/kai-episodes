# -*- coding: utf-8 -*-
"""Generated from angle LORA-002 -- SWITCHING ADAPTERS COSTS A MODEL LOAD.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py LORA-002
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same lora. Picture the magnifier pass. The layer count of the model. Total VRAM in use with a four thousand token context. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="SWITCHING ADAPTERS COSTS A MODEL LOAD",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="Same board",
    art_at="Picture the magnifier",
    chips=[{"t": "LAYERS", "c": "gold", "at": "The layer count"}, {"t": "4K", "c": "cyan", "at": "Total VRAM in"}],
    stats=[{"v": "22", "u": "s", "lab": "at 4,625 T/S", "c": "red", "at": "Time to the"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="chain",
    vo="The lora figure, read straight off the board. Picture the magnifier pass. The number of key value heads, shared across groups. Total VRAM in use with an eight thousand token context. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="SWITCHING ADAPTERS COSTS A MODEL LOAD",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    header_at="The lora figure",
    art_at="Picture the magnifier",
    chain=[{"t": "KV HEADS", "s": "This figure does not establish that a model fits.", "at": "The number of"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 8K, taken on trust.", "at": "Total VRAM in"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of at 767 T/S, taken on the board.", "at": "Time to the"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="rows",
    vo="One vram number, one source, one board. Picture the vram sticks. Total VRAM in use with a sixteen thousand token context. The hidden width of the model. Total VRAM in use with a thirty-two thousand token context. The feed forward width of the model. One method, every row.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="SWITCHING ADAPTERS COSTS A MODEL LOAD",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="One vram number",
    art_at="Picture the vram",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "19 GB", "sub": "16K", "cls": "gold", "at": "Total VRAM in use with a sixteen"}, {"rank": "2", "name": "Qwen2.5 3B Instruct", "val": "2048", "sub": "HIDDEN", "cls": "", "at": "The hidden width"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "20 GB", "sub": "32K", "cls": "", "at": "Total VRAM in use with a thirty-two"}, {"rank": "4", "name": "Qwen2.5 3B Instruct", "val": "8192", "sub": "FFN", "cls": "", "at": "The feed forward"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about vram is a guess. Picture the vram sticks. Total VRAM in use with a sixty-four thousand token context. Total VRAM in use with a two hundred fifty-six thousand token context. The adapter arrays at thirty million trainable values. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="SWITCHING ADAPTERS COSTS A MODEL LOAD",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Nothing here about",
    art_at="Picture the vram",
    bars=[{"lab": "Muse Glimmer 30B", "val": "17", "unit": "GB", "pct": 50.0, "cls": "", "at": "Total VRAM in use with a sixty-four"}, {"lab": "Muse Glimmer 30B", "val": "20", "unit": "GB", "pct": 58.8, "cls": "", "at": "Total VRAM in use with a two"}, {"lab": "Qwen2.5 3B Instruct", "val": "457", "unit": "MiB", "pct": 100.0, "cls": "red", "at": "The adapter arrays"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the latency of the hardware, not of the brochure. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Total VRAM in use with an eight thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="SWITCHING ADAPTERS COSTS A MODEL LOAD",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="This is the",
    art_at="Picture timing, line",
    rails=[{"lab": "at 4,625 T/S", "val": "22", "pct": 17.0, "cls": "red", "at": "Time to the"}, {"lab": "8K", "val": "18", "pct": 52.9, "cls": "", "at": "Total VRAM in"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. Does not fit on a twenty-four gigabyte card at all. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="SWITCHING ADAPTERS COSTS A MODEL LOAD",
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
    vo="Every vram figure here carries its own source. Picture the vram sticks. On the bench: Muse Glimmer 30B. The total trainable parameters with rank sixteen on the query and value projections only. The line reads twenty gigabytes, from the same run.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="SWITCHING ADAPTERS COSTS A MODEL LOAD",
    art="vram_module",
    art_caption="THE VRAM STICKS",
    header_at="Every vram figure",
    art_at="Picture the vram",
    name="Muse Glimmer 30B",
    blurb="The total trainable parameters with rank sixteen on the query and value projections only",
    meta="256K &middot; 20 GB",
    name_at="On the bench",
    blurb_at="The total trainable",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The vram number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the adapter budget figure, the vram budget figure, the latency budget figure.",
    kicker="BYTE FORENSICS &middot; VRAM",
    title="SWITCHING ADAPTERS COSTS A MODEL LOAD",
    header_at="The vram number",
    items=[{"key": "magnifier", "label": "adapter budget", "at": "the adapter budget figure"}, {"key": "vram_module", "label": "vram budget", "at": "the vram budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}],
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="title",
    vo="One claim, one board, one run. Loading two adapters for the same base doubles the switch cost, because the base model is the expensive part and it is loaded either way. SWITCHING ADAPTERS COSTS A MODEL LOAD.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="SWITCHING ADAPTERS COSTS A MODEL LOAD",
    sub="Loading two adapters for the same base doubles the switch cost, because the base model is the expensive part and it is loaded either way.",
    art="timer_flat",
    head_at="SWITCHING ADAPTERS COSTS A MODEL LOAD",
    source="derived &middot; qwen2.5 3b instruct &middot; architecture",
)

win(
    layout="nodes",
    vo="The lora figure, read straight off the board. Picture the magnifier pass. The total trainable parameters with rank sixteen on seven projections. The bytes per trainable value, across the weight, the gradient and the optimizer state. The adapter arrays at thirty million trainable values.",
    kicker="BYTE FORENSICS &middot; LORA",
    title="SWITCHING ADAPTERS COSTS A MODEL LOAD",
    header_at="The lora figure",
    art="magnifier",
    art_caption="THE MAGNIFIER PASS",
    art_at="Picture the magnifier",
    chain=[{"t": "TRAINABLE", "s": "This figure does not establish that a model fits.", "at": "The total trainable"}, {"t": "PER VALUE", "s": "This figure does not establish a speed.", "at": "The bytes per"}, {"t": "AT 30M", "s": "An upper bound. The exact count for this model is twenty-five million, and that gives three hundred and eighty-two mebibytes", "at": "The adapter arrays"}],
    source="derived &middot; rank 16 &middot; seven projections targeted &middot; qwen2.5 3b instruct",
)

NAME = "BYTE-GEN-LORA-002"
TITLE = "SWITCHING ADAPTERS COSTS A MODEL LOAD"
DOC_TITLE = "SWITCHING ADAPTERS COSTS A MODEL LOAD &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
