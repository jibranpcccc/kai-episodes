# -*- coding: utf-8 -*-
"""Generated from angle QUANT-007 -- SHORTER ANSWERS LOOK LIKE FASTER MODELS.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py QUANT-007
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same quant. Picture quantised in blocks. The size of the block scale in the four bit format. Generation rate on a five-oh-ninety with a four thousand token context. The LoRA paper's WikiSQL score for the full fine tune. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="SHORTER ANSWERS LOOK LIKE FASTER MODELS",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="Same board",
    art_at="Picture quantised in",
    chips=[{"t": "32 BIT", "c": "gold", "at": "The size of"}, {"t": "4K", "c": "cyan", "at": "Generation rate on"}],
    stats=[{"v": "73.8", "u": "", "lab": "FT 73.8", "c": "cyan", "at": "The LoRA paper's"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="chain",
    vo="The quant figure, read straight off the board. Picture quantised in blocks. The overhead the block scales add per weight. Generation rate on a five-oh-ninety with a sixteen thousand token context. The LoRA paper's WikiSQL score for LoRA at rank four.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="SHORTER ANSWERS LOOK LIKE FASTER MODELS",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="The quant figure",
    art_at="Picture quantised in",
    chain=[{"t": "+0.5 BIT", "s": "This figure does not establish that a model fits.", "at": "The overhead the"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Generation rate on"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of LO 89.5, taken on the board.", "at": "The LoRA paper's"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="rows",
    vo="One generation number, one source, one board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a thirty-two thousand token context. The LoRA paper's MNLI score for the full fine tune. Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context. One method, every row.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="SHORTER ANSWERS LOOK LIKE FASTER MODELS",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="One generation number",
    art_at="Picture the tokens",
    rows=[{"rank": "1", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "gold", "at": "Generation rate on a five-oh-ninety with a thirty-two"}, {"rank": "2", "name": "GPT-3 175B", "val": "73.4", "sub": "FT 73.4", "cls": "", "at": "The LoRA paper's"}, {"rank": "3", "name": "Qwen 3.8 27B", "val": "22.8 T/S", "sub": "128K", "cls": "", "at": "Generation rate on a five-oh-ninety with a one"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a three thousand ninety with a four thousand token context. Generation rate on a three thousand ninety with a thirty-two thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="SHORTER ANSWERS LOOK LIKE FASTER MODELS",
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
    title="SHORTER ANSWERS LOOK LIKE FASTER MODELS",
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
    vo="Measured papers, on this board, in this run. Picture the paper folder. This figure does not establish that a model fits. This figure does not establish a speed. This figure does not establish a fit claim. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="SHORTER ANSWERS LOOK LIKE FASTER MODELS",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Measured papers, on",
    art_at="Picture the paper",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "This figure does not establish that a model fits.", "at": "This figure does not establish that"}, {"t": "This figure does not establish a speed.", "at": "This figure does not establish a speed"}, {"t": "This figure does not establish a fit claim.", "at": "This figure does not establish a fit"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the QLoRA paper &middot; percentage point movement &middot; 5-shot MMLU",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every papers figure here carries its own source. Picture the paper folder. On the bench: Llama 65B. The size of the block scale in the four bit format. The line reads seventy-four point eight tokens per second, from the same run.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="SHORTER ANSWERS LOOK LIKE FASTER MODELS",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Every papers figure",
    art_at="Picture the paper",
    name="Llama 65B",
    blurb="The size of the block scale in the four bit format",
    meta="4K &middot; 74.8 T/S",
    name_at="On the bench",
    blurb_at="The size of",
    meta_at="The line reads",
    side="right",
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; 65b on one 48 gb card",
)

win(
    layout="strip",
    vo="The generation number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the quant budget figure, the decode budget figure, the paper budget figure.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="SHORTER ANSWERS LOOK LIKE FASTER MODELS",
    header_at="The generation number",
    items=[{"key": "gguf_blocks", "label": "quant budget", "at": "the quant budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}, {"key": "folder", "label": "paper budget", "at": "the paper budget figure"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="title",
    vo="One claim, one board, one run. Quantized models produce fewer tokens because they produce shorter answers, which is why a benchmark can improve without the hardware improving. SHORTER ANSWERS LOOK LIKE FASTER MODELS.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="SHORTER ANSWERS LOOK LIKE FASTER MODELS",
    sub="Quantized models produce fewer tokens because they produce shorter answers, which is why a benchmark can improve without the hardware improving.",
    art="folder",
    head_at="SHORTER ANSWERS LOOK LIKE FASTER MODELS",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="nodes",
    vo="The papers figure, read straight off the board. Picture the paper folder. The LoRA paper's WikiSQL score for the full fine tune. The overhead the block scales add per weight. Generation rate on a five-oh-ninety with a sixteen thousand token context.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="SHORTER ANSWERS LOOK LIKE FASTER MODELS",
    header_at="The papers figure",
    art="folder",
    art_caption="THE PAPER FOLDER",
    art_at="Picture the paper",
    chain=[{"t": "FT 73.8", "s": "This figure does not establish that a model fits.", "at": "The LoRA paper's"}, {"t": "+0.5 BIT", "s": "This figure does not establish a speed.", "at": "The overhead the"}, {"t": "16K", "s": "This figure does not establish a fit claim.", "at": "Generation rate on"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

NAME = "BYTE-GEN-QUANT-007"
TITLE = "SHORTER ANSWERS LOOK LIKE FASTER MODELS"
DOC_TITLE = "SHORTER ANSWERS LOOK LIKE FASTER MODELS &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
