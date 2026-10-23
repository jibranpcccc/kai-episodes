# -*- coding: utf-8 -*-
"""Generated from angle PF-005 -- QUANTIZATION BUYS YOU THE FIRST WORD.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PF-005
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same quant. Picture quantised in blocks. The size of the block scale in the four bit format. Prompt processing rate on a four thousand token prompt. Generation rate on a five-oh-ninety with a four thousand token context. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="QUANTIZATION BUYS YOU THE FIRST WORD",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="Same board",
    art_at="Picture quantised in",
    chips=[{"t": "32 BIT", "c": "gold", "at": "The size of"}, {"t": "4K", "c": "cyan", "at": "Prompt processing rate"}],
    stats=[{"v": "74.8", "u": "T/S", "lab": "4K", "c": "cyan", "at": "Generation rate on"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="chain",
    vo="The quant figure, read straight off the board. Picture quantised in blocks. The overhead the block scales add per weight. Prompt processing rate on a sixteen thousand token prompt. Generation rate on a five-oh-ninety with a sixteen thousand token context.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="QUANTIZATION BUYS YOU THE FIRST WORD",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="The quant figure",
    art_at="Picture quantised in",
    chain=[{"t": "+0.5 BIT", "s": "This figure does not establish that a model fits.", "at": "The overhead the"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Prompt processing rate"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 16K, taken on the board.", "at": "Generation rate on"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="rows",
    vo="One prefill number, one source, one board. Picture the prompt, incoming. Prompt processing rate on a sixty-four thousand token prompt. Generation rate on a five-oh-ninety with a thirty-two thousand token context. Prompt processing rate on a one hundred twenty-eight thousand token prompt. One method, every row.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="QUANTIZATION BUYS YOU THE FIRST WORD",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="One prefill number",
    art_at="Picture the prompt",
    rows=[{"rank": "1", "name": "Muse Glimmer 30B", "val": "3606 T/S", "sub": "64K", "cls": "gold", "at": "Prompt processing rate on a sixty-four"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "38.0 T/S", "sub": "32K", "cls": "", "at": "Generation rate on"}, {"rank": "3", "name": "Muse Glimmer 30B", "val": "2806 T/S", "sub": "128K", "cls": "", "at": "Prompt processing rate on a one"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about generation is a guess. Picture the tokens, one by one. Generation rate on a three thousand ninety with a thirty-two thousand token context. Prompt processing rate on a one hundred twenty-eight thousand token prompt. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="QUANTIZATION BUYS YOU THE FIRST WORD",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Nothing here about",
    art_at="Picture the tokens",
    bars=[{"lab": "Qwen 3.8 27B", "val": "37.0", "unit": "T/S", "pct": 91.8, "cls": "", "at": "Generation rate on"}, {"lab": "Qwen 3.8 27B", "val": "461", "unit": "T/S", "pct": 12.3, "cls": "", "at": "Prompt processing rate"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the generation of the hardware, not of the brochure. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a four thousand token context. Prompt processing rate on a sixteen thousand token prompt. Generation rate on a five-oh-ninety with a sixteen thousand token context. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="QUANTIZATION BUYS YOU THE FIRST WORD",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="This is the",
    art_at="Picture the tokens",
    rails=[{"lab": "4K", "val": "74.8", "pct": 100.0, "cls": "", "at": "Generation rate on a five-oh-ninety with a four"}, {"lab": "16K", "val": "4373", "pct": 94.5, "cls": "", "at": "Prompt processing rate"}, {"lab": "16K", "val": "52.2", "pct": 69.8, "cls": "", "at": "Generation rate on a five-oh-ninety with a sixteen"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured prefill, on this board, in this run. Picture the prompt, incoming. This figure does not establish that a model fits. This figure does not establish a speed. This figure does not establish a fit claim. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="QUANTIZATION BUYS YOU THE FIRST WORD",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="Measured prefill, on",
    art_at="Picture the prompt",
    note_head="READ THE SMALL PRINT",
    note_items=[{"t": "This figure does not establish that a model fits.", "at": "This figure does not establish that"}, {"t": "This figure does not establish a speed.", "at": "This figure does not establish a speed"}, {"t": "This figure does not establish a fit claim.", "at": "This figure does not establish a fit"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
    source_at="The source sits",
)

win(
    layout="gallery",
    vo="Every prefill figure here carries its own source. Picture the prompt, incoming. On the bench: Muse Glimmer 30B. Generation rate on a five-oh-ninety with a sixteen thousand token context. The line reads four point one two seven, from the same run.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="QUANTIZATION BUYS YOU THE FIRST WORD",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="Every prefill figure",
    art_at="Picture the prompt",
    name="Muse Glimmer 30B",
    blurb="Generation rate on a five-oh-ninety with a sixteen thousand token context",
    meta="EFFECTIVE &middot; 4.127",
    name_at="On the bench",
    blurb_at="Generation rate on",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The prefill number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the quant budget figure, the prefill budget figure, the decode budget figure.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="QUANTIZATION BUYS YOU THE FIRST WORD",
    header_at="The prefill number",
    items=[{"key": "gguf_blocks", "label": "quant budget", "at": "the quant budget figure"}, {"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}, {"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="title",
    vo="One claim, one board, one run. Time to first token falls when the weights are quantized because less data has to be read, so the win is at the start and disappears during generation. QUANTIZATION BUYS YOU THE FIRST WORD.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="QUANTIZATION BUYS YOU THE FIRST WORD",
    sub="Time to first token falls when the weights are quantized because less data has to be read, so the win is at the start and disappears during generation.",
    art="token_blocks",
    head_at="QUANTIZATION BUYS YOU THE FIRST WORD",
    source="the documented bits and bytes route &middot; nested quantization",
)

NAME = "BYTE-GEN-PF-005"
TITLE = "QUANTIZATION BUYS YOU THE FIRST WORD"
DOC_TITLE = "QUANTIZATION BUYS YOU THE FIRST WORD &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
