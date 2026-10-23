# -*- coding: utf-8 -*-
"""Generated from angle QUANT-004 -- FOUR BITS COSTS BIG MODELS MORE.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py QUANT-004
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same quant. Picture quantised in blocks. The size of the block scale in the four bit format. The LoRA paper's WikiSQL score for the full fine tune. Generation rate on two sixteen gigabyte cards with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="FOUR BITS COSTS BIG MODELS MORE",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="Same board",
    art_at="Picture quantised in",
    chips=[{"t": "32 BIT", "c": "gold", "at": "The size of"}, {"t": "FT 73.8", "c": "cyan", "at": "The LoRA paper's"}],
    stats=[{"v": "22.5", "u": "T/S", "lab": "2 cards 4K", "c": "red", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="chain",
    vo="The quant figure, read straight off the board. Picture quantised in blocks. The overhead the block scales add per weight. The LoRA paper's WikiSQL score for LoRA at rank four. Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="FOUR BITS COSTS BIG MODELS MORE",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="The quant figure",
    art_at="Picture quantised in",
    chain=[{"t": "+0.5 BIT", "s": "This figure does not establish that a model fits.", "at": "The overhead the"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about LO 89.5, taken on trust.", "at": "The LoRA paper's"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 2 cards 128K, taken on the board.", "at": "Generation rate on"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="rows",
    vo="One papers number, one source, one board. Picture the paper folder. The LoRA paper's MNLI score for the full fine tune. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. The LoRA paper's MNLI score for LoRA at rank four. One method, every row.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="FOUR BITS COSTS BIG MODELS MORE",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="One papers number",
    art_at="Picture the paper",
    rows=[{"rank": "1", "name": "GPT-3 175B", "val": "73.4", "sub": "FT 73.4", "cls": "gold", "at": "The LoRA paper's MNLI score for the"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.1 T/S", "sub": "1 card 128K", "cls": "red", "at": "Generation rate on"}, {"rank": "3", "name": "GPT-3 175B", "val": "91.7", "sub": "LO 91.7", "cls": "", "at": "The LoRA paper's MNLI score for LoRA"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="bars",
    vo="Nothing here about capacity is a guess. Picture the window and what is in it. Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context. Generation rate on two sixteen gigabyte cards with a four thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="FOUR BITS COSTS BIG MODELS MORE",
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
    title="FOUR BITS COSTS BIG MODELS MORE",
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
    title="FOUR BITS COSTS BIG MODELS MORE",
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
    vo="Every capacity figure here carries its own source. Picture the window and what is in it. On the bench: Qwen 3.8 27B. The overhead the block scales add per weight. The line reads eighty-nine point five, from the same run.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="FOUR BITS COSTS BIG MODELS MORE",
    art="context_window",
    art_caption="THE WINDOW AND WHAT IS IN IT",
    header_at="Every capacity figure",
    art_at="Picture the window",
    name="Qwen 3.8 27B",
    blurb="The overhead the block scales add per weight",
    meta="LO 89.5 &middot; 89.5",
    name_at="On the bench",
    blurb_at="The overhead the",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The papers number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the quant budget figure, the paper budget figure, the context budget figure.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="FOUR BITS COSTS BIG MODELS MORE",
    header_at="The papers number",
    items=[{"key": "gguf_blocks", "label": "quant budget", "at": "the quant budget figure"}, {"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "context_window", "label": "context budget", "at": "the context budget figure"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="title",
    vo="One claim, one board, one run. The accuracy cost of quantization is not a single number, because the same bit depth hurts a small model and a large model differently. FOUR BITS COSTS BIG MODELS MORE.",
    kicker="BYTE FORENSICS &middot; CAPACITY",
    title="FOUR BITS COSTS BIG MODELS MORE",
    sub="The accuracy cost of quantization is not a single number, because the same bit depth hurts a small model and a large model differently.",
    art="context_window",
    head_at="FOUR BITS COSTS BIG MODELS MORE",
    source="the documented bits and bytes route &middot; nested quantization",
)

NAME = "BYTE-GEN-QUANT-004"
TITLE = "FOUR BITS COSTS BIG MODELS MORE"
DOC_TITLE = "FOUR BITS COSTS BIG MODELS MORE &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
