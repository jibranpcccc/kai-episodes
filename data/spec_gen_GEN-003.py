# -*- coding: utf-8 -*-
"""Generated from angle GEN-003 -- HALVING BITS DID NOT HALVE THE WAIT.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py GEN-003
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same quant. Picture quantised in blocks. The size of the block scale in the four bit format. Generation rate on a five-oh-ninety with a four thousand token context. The overhead the block scales add per weight. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="HALVING BITS DID NOT HALVE THE WAIT",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="Same board",
    art_at="Picture quantised in",
    chips=[{"t": "32 BIT", "c": "gold", "at": "The size of"}, {"t": "4K", "c": "cyan", "at": "Generation rate on"}],
    stats=[{"v": "0.5", "u": "", "lab": "+0.5 BIT", "c": "cyan", "at": "The overhead the"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="chain",
    vo="The generation figure, read straight off the board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a sixteen thousand token context. The effective bits per converted weight in the pinned implementation, with the nested scales compressed too. Generation rate on a five-oh-ninety with a thirty-two thousand token context.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="HALVING BITS DID NOT HALVE THE WAIT",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="The generation figure",
    art_at="Picture the tokens",
    chain=[{"t": "16K", "s": "This figure does not establish that a model fits.", "at": "Generation rate on a five-oh-ninety with a sixteen"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about EFFECTIVE, taken on trust.", "at": "The effective bits"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 32K, taken on the board.", "at": "Generation rate on a five-oh-ninety with a thirty-two"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One generation number, one source, one board. Picture the tokens, one by one. Generation rate on a three thousand ninety with a four thousand token context. Generation rate on a three thousand ninety with a thirty-two thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="HALVING BITS DID NOT HALVE THE WAIT",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="One generation number",
    art_at="Picture the tokens",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "40.3 T/S", "sub": "4K", "cls": "gold", "at": "Generation rate on a three thousand ninety with a four"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "37.0 T/S", "sub": "32K", "cls": "", "at": "Generation rate on a three thousand ninety with a thirty-two"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a three thousand ninety with a four thousand token context. Generation rate on a three thousand ninety with a thirty-two thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="HALVING BITS DID NOT HALVE THE WAIT",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Nothing here about",
    art_at="Picture the tokens",
    bars=[{"lab": "Qwen 3.8 27B", "val": "40.3", "unit": "T/S", "pct": 100.0, "cls": "", "at": "Generation rate on a three thousand ninety with a four"}, {"lab": "Qwen 3.8 27B", "val": "37.0", "unit": "T/S", "pct": 91.8, "cls": "", "at": "Generation rate on a three thousand ninety with a thirty-two"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the generation of the hardware, not of the brochure. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a sixteen thousand token context. Generation rate on a five-oh-ninety with a thirty-two thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="HALVING BITS DID NOT HALVE THE WAIT",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="This is the",
    art_at="Picture the tokens",
    rails=[{"lab": "16K", "val": "52.2", "pct": 69.8, "cls": "", "at": "Generation rate on a five-oh-ninety with a sixteen"}, {"lab": "32K", "val": "38.0", "pct": 50.8, "cls": "", "at": "Generation rate on a five-oh-ninety with a thirty-two"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured generation, on this board, in this run. Picture the tokens, one by one. This figure does not establish that a model fits. This figure does not establish a speed. This figure does not establish a fit claim. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="HALVING BITS DID NOT HALVE THE WAIT",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Measured generation, on",
    art_at="Picture the tokens",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "This figure does not establish that a model fits.", "at": "This figure does not establish that"}, {"t": "This figure does not establish a speed.", "at": "This figure does not establish a speed"}, {"t": "This figure does not establish a fit claim.", "at": "This figure does not establish a fit"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every generation figure here carries its own source. Picture the tokens, one by one. On the bench: Qwen 3.8 27B. The overhead the block scales add per weight. The line reads fifty-two point two tokens per second, from the same run.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="HALVING BITS DID NOT HALVE THE WAIT",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Every generation figure",
    art_at="Picture the tokens",
    name="Qwen 3.8 27B",
    blurb="The overhead the block scales add per weight",
    meta="16K &middot; 52.2 T/S",
    name_at="On the bench",
    blurb_at="The overhead the",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-GEN-003"
TITLE = "HALVING BITS DID NOT HALVE THE WAIT"
DOC_TITLE = "HALVING BITS DID NOT HALVE THE WAIT &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
