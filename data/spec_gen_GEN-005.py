# -*- coding: utf-8 -*-
"""Generated from angle GEN-005 -- THE BENCHMARK AND THE CHAT DISAGREE.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py GEN-005
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same generation. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a four thousand token context. Prompt processing rate on a four thousand token prompt. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE BENCHMARK AND THE CHAT DISAGREE",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Same board",
    art_at="Picture the tokens",
    chips=[{"t": "4K", "c": "gold", "at": "Generation rate on"}],
    stats=[{"v": "4625", "u": "T/S", "lab": "4K", "c": "gold", "at": "Prompt processing rate"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="chain",
    vo="The generation figure, read straight off the board. Picture the tokens, one by one. Generation rate on a five-oh-ninety with a sixteen thousand token context. Prompt processing rate on a sixteen thousand token prompt.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE BENCHMARK AND THE CHAT DISAGREE",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="The generation figure",
    art_at="Picture the tokens",
    chain=[{"t": "16K", "s": "This figure does not establish that a model fits.", "at": "Generation rate on"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about 16K, taken on trust.", "at": "Prompt processing rate"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rows",
    vo="One prefill number, one source, one board. Picture the prompt, incoming. Prompt processing rate on a sixty-four thousand token prompt. Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context. Prompt processing rate on a one hundred twenty-eight thousand token prompt. One method, every row.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE BENCHMARK AND THE CHAT DISAGREE",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="One prefill number",
    art_at="Picture the prompt",
    rows=[{"rank": "1", "name": "Muse Glimmer 30B", "val": "3606 T/S", "sub": "64K", "cls": "gold", "at": "Prompt processing rate on a sixty-four"}, {"rank": "2", "name": "Qwen 3.8 27B", "val": "22.8 T/S", "sub": "128K", "cls": "", "at": "Generation rate on"}, {"rank": "3", "name": "Muse Glimmer 30B", "val": "2806 T/S", "sub": "128K", "cls": "", "at": "Prompt processing rate on a one"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about prefill is a guess. Picture the prompt, incoming. Prompt processing rate on a two hundred fifty-six thousand token prompt. Generation rate on a three thousand ninety with a thirty-two thousand token context. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE BENCHMARK AND THE CHAT DISAGREE",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="Nothing here about",
    art_at="Picture the prompt",
    bars=[{"lab": "Muse Glimmer 30B", "val": "1874", "unit": "T/S", "pct": 40.5, "cls": "", "at": "Prompt processing rate"}, {"lab": "Qwen 3.8 27B", "val": "37.0", "unit": "T/S", "pct": 91.8, "cls": "", "at": "Generation rate on"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="rail",
    vo="This is the prefill of the hardware, not of the brochure. Picture the prompt, incoming. Prompt processing rate on a one hundred twenty-eight thousand token prompt. Generation rate on a five-oh-ninety with a four thousand token context. Prompt processing rate on a four thousand token prompt. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE BENCHMARK AND THE CHAT DISAGREE",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="This is the",
    art_at="Picture the prompt",
    rails=[{"lab": "128K", "val": "461", "pct": 12.3, "cls": "", "at": "Prompt processing rate on a one"}, {"lab": "4K", "val": "74.8", "pct": 100.0, "cls": "", "at": "Generation rate on"}, {"lab": "4K", "val": "4625", "pct": 100.0, "cls": "", "at": "Prompt processing rate on a four"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE BENCHMARK AND THE CHAT DISAGREE",
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
    vo="Every generation figure here carries its own source. Picture the tokens, one by one. On the bench: Qwen 3.8 27B. Prompt processing rate on a sixteen thousand token prompt. The line reads one hundred and thirty-one seconds, from the same run.",
    kicker="BYTE FORENSICS &middot; GENERATION",
    title="THE BENCHMARK AND THE CHAT DISAGREE",
    art="token_blocks",
    art_caption="THE TOKENS, ONE BY ONE",
    header_at="Every generation figure",
    art_at="Picture the tokens",
    name="Qwen 3.8 27B",
    blurb="Prompt processing rate on a sixteen thousand token prompt",
    meta="at 767 T/S &middot; 131 s",
    name_at="On the bench",
    blurb_at="Prompt processing rate",
    meta_at="The line reads",
    side="right",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="strip",
    vo="The prefill number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the decode budget figure, the prefill budget figure, the latency budget figure.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE BENCHMARK AND THE CHAT DISAGREE",
    header_at="The prefill number",
    items=[{"key": "token_blocks", "label": "decode budget", "at": "the decode budget figure"}, {"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}],
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="title",
    vo="One claim, one board, one run. Throughput measured with one long prompt is not the throughput you get in a conversation, because batching changes the arithmetic. THE BENCHMARK AND THE CHAT DISAGREE.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE BENCHMARK AND THE CHAT DISAGREE",
    sub="Throughput measured with one long prompt is not the throughput you get in a conversation, because batching changes the arithmetic.",
    art="timer_flat",
    head_at="THE BENCHMARK AND THE CHAT DISAGREE",
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

NAME = "BYTE-GEN-GEN-005"
TITLE = "THE BENCHMARK AND THE CHAT DISAGREE"
DOC_TITLE = "THE BENCHMARK AND THE CHAT DISAGREE &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
