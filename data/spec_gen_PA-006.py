# -*- coding: utf-8 -*-
"""Generated from angle PA-006 -- THE AVERAGE HIDES WHERE IT BREAKS.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PA-006
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same papers. Picture the paper folder. The LoRA paper's WikiSQL score for the full fine tune. The size of the block scale in the four bit format. Generation rate on two sixteen gigabyte cards with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="THE AVERAGE HIDES WHERE IT BREAKS",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Same board",
    art_at="Picture the paper",
    chips=[{"t": "FT 73.8", "c": "gold", "at": "The LoRA paper's"}, {"t": "32 BIT", "c": "cyan", "at": "The size of"}],
    stats=[{"v": "22.5", "u": "T/S", "lab": "2 cards 4K", "c": "red", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="chain",
    vo="The papers figure, read straight off the board. Picture the paper folder. The LoRA paper's WikiSQL score for LoRA at rank four. The overhead the block scales add per weight. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="THE AVERAGE HIDES WHERE IT BREAKS",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="The papers figure",
    art_at="Picture the paper",
    chain=[{"t": "LO 89.5", "s": "This figure does not establish that a model fits.", "at": "The LoRA paper's"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about +0.5 BIT, taken on trust.", "at": "The overhead the"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 2 cards 128K, taken on the board.", "at": "Generation rate on"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="rows",
    vo="One quant number, one source, one board. Picture quantised in blocks. The effective bits per converted weight in the pinned implementation, with the nested scales compressed too. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="THE AVERAGE HIDES WHERE IT BREAKS",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="One quant number",
    art_at="Picture quantised in",
    rows=[{"rank": "1", "name": "Qwen2.5 3B Instruct", "val": "4.127", "sub": "EFFECTIVE", "cls": "gold", "at": "The effective bits"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "red", "at": "Generation rate on"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="the pinned implementation &middot; nested quantization &middot; large tensor average",
)

win(
    layout="bars",
    vo="Nothing here about capacity is a guess. Picture the window and what is in it. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. Generation rate on two sixteen gigabyte cards with a four thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="THE AVERAGE HIDES WHERE IT BREAKS",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="Nothing here about",
    art_at="Picture the window",
    bars=[{"lab": "Qwen 3.8 27B", "val": "38.1", "unit": "T/S", "pct": 100.0, "cls": "red", "at": "Generation rate on one"}, {"lab": "Qwen 3.8 27B", "val": "22.5", "unit": "T/S", "pct": 59.1, "cls": "red", "at": "Generation rate on two"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the capacity of the hardware, not of the brochure. Picture the window and what is in it. Generation rate on two sixteen gigabyte cards with a four thousand token context. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="THE AVERAGE HIDES WHERE IT BREAKS",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="This is the",
    art_at="Picture the window",
    rails=[{"lab": "2 cards 4K", "val": "22.5", "pct": 59.1, "cls": "red", "at": "Generation rate on two sixteen gigabyte cards with a four"}, {"lab": "2 cards 128K", "val": "15.6", "pct": 41.0, "cls": "red", "at": "Generation rate on two sixteen gigabyte cards with a one"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured capacity, on this board, in this run. Picture the window and what is in it. A pair of cards never buys speed. One card is faster than two at the same context. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="THE AVERAGE HIDES WHERE IT BREAKS",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="Measured capacity, on",
    art_at="Picture the window",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "A pair of cards never buys speed", "at": "A pair of"}, {"t": "One card is faster than two at the same context", "at": "One card is"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every capacity figure here carries its own source. Picture the window and what is in it. On the bench: Qwen 3.8 27B. The LoRA paper's WikiSQL score for LoRA at rank four. The line reads zero point five, from the same run.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="THE AVERAGE HIDES WHERE IT BREAKS",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="Every capacity figure",
    art_at="Picture the window",
    name="Qwen 3.8 27B",
    blurb="The LoRA paper's WikiSQL score for LoRA at rank four",
    meta="+0.5 BIT &middot; 0.5",
    name_at="On the bench",
    blurb_at="The LoRA paper's",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The quant number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the paper budget figure, the quant budget figure, the context budget figure.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="THE AVERAGE HIDES WHERE IT BREAKS",
    header_at="The quant number",
    items=[{"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "gguf_blocks", "label": "quant budget", "at": "the quant budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="title",
    vo="One claim, one board, one run. A quantization paper that reports perplexity reports an average, and averages hide the tasks where the degradation concentrates. THE AVERAGE HIDES WHERE IT BREAKS.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="THE AVERAGE HIDES WHERE IT BREAKS",
    sub="A quantization paper that reports perplexity reports an average, and averages hide the tasks where the degradation concentrates.",
    art="context_window",
    head_at="THE AVERAGE HIDES WHERE IT BREAKS",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

NAME = "BYTE-GEN-PA-006"
TITLE = "THE AVERAGE HIDES WHERE IT BREAKS"
DOC_TITLE = "THE AVERAGE HIDES WHERE IT BREAKS &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
