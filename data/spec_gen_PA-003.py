# -*- coding: utf-8 -*-
"""Generated from angle PA-003 -- THE MEAN HIDES THE WAIT.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py PA-003
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same papers. Picture the paper folder. The LoRA paper's WikiSQL score for the full fine tune. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="THE MEAN HIDES THE WAIT",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Same board",
    art_at="Picture the paper",
    chips=[{"t": "FT 73.8", "c": "gold", "at": "The LoRA paper's"}],
    stats=[{"v": "22", "u": "s", "lab": "at 4,625 T/S", "c": "red", "at": "Time to the"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="chain",
    vo="The papers figure, read straight off the board. Picture the paper folder. The LoRA paper's WikiSQL score for LoRA at rank four. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Prompt processing rate on a sixteen thousand token prompt.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="THE MEAN HIDES THE WAIT",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="The papers figure",
    art_at="Picture the paper",
    chain=[{"t": "LO 89.5", "s": "This figure does not establish that a model fits.", "at": "The LoRA paper's"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about at 767 T/S, taken on trust.", "at": "Time to the"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of 16K, taken on the board.", "at": "Prompt processing rate"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="rows",
    vo="One prefill number, one source, one board. Picture the prompt, incoming. Prompt processing rate on a sixty-four thousand token prompt. The LoRA paper's MNLI score for LoRA at rank four. Prompt processing rate on a one hundred twenty-eight thousand token prompt. One method, every row.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE MEAN HIDES THE WAIT",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="One prefill number",
    art_at="Picture the prompt",
    rows=[{"rank": "1", "name": "Muse Glimmer 30B", "val": "3606 T/S", "sub": "64K", "cls": "gold", "at": "Prompt processing rate on a sixty-four"}, {"rank": "2", "name": "GPT-3 175B", "val": "91.7", "sub": "LO 91.7", "cls": "", "at": "The LoRA paper's"}, {"rank": "3", "name": "Muse Glimmer 30B", "val": "2806 T/S", "sub": "128K", "cls": "", "at": "Prompt processing rate on a one"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="bars",
    vo="Nothing here about latency is a guess. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Prompt processing rate on a sixteen thousand token prompt. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE MEAN HIDES THE WAIT",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Nothing here about",
    art_at="Picture timing, line",
    bars=[{"lab": "Qwen 3.8 27B", "val": "131", "unit": "s", "pct": 100.0, "cls": "red", "at": "Time to the"}, {"lab": "Muse Glimmer 30B", "val": "4373", "unit": "T/S", "pct": 94.5, "cls": "", "at": "Prompt processing rate"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="rail",
    vo="This is the prefill of the hardware, not of the brochure. Picture the prompt, incoming. Prompt processing rate on a two hundred fifty-six thousand token prompt. Prompt processing rate on a four thousand token prompt. Prompt processing rate on a one hundred twenty-eight thousand token prompt. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE MEAN HIDES THE WAIT",
    art="prompt_stream",
    art_caption="THE PROMPT, INCOMING",
    header_at="This is the",
    art_at="Picture the prompt",
    rails=[{"lab": "256K", "val": "1874", "pct": 40.5, "cls": "", "at": "Prompt processing rate on a two"}, {"lab": "4K", "val": "3749", "pct": 100.0, "cls": "", "at": "Prompt processing rate on a four"}, {"lab": "128K", "val": "461", "pct": 12.3, "cls": "", "at": "Prompt processing rate on a one"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE MEAN HIDES THE WAIT",
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
    vo="Every papers figure here carries its own source. Picture the paper folder. On the bench: Llama 65B. The size of the card in that demonstration. The line reads seventy-three point eight, from the same run.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="THE MEAN HIDES THE WAIT",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="Every papers figure",
    art_at="Picture the paper",
    name="Llama 65B",
    blurb="The size of the card in that demonstration",
    meta="FT 73.8 &middot; 73.8",
    name_at="On the bench",
    blurb_at="The size of",
    meta_at="The line reads",
    side="right",
    source="the QLoRA paper &middot; arXiv 2305.14314 &middot; 65b on one 48 gb card",
)

win(
    layout="strip",
    vo="The latency number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the paper budget figure, the latency budget figure, the prefill budget figure.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE MEAN HIDES THE WAIT",
    header_at="The latency number",
    items=[{"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}, {"key": "prompt_stream", "label": "prefill budget", "at": "the prefill budget figure"}],
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="title",
    vo="One claim, one board, one run. Latency reported as a mean hides the tail, and on local hardware the tail is the difference between a working tool and an abandoned one. THE MEAN HIDES THE WAIT.",
    kicker="BYTE FORENSICS &middot; PREFILL",
    title="THE MEAN HIDES THE WAIT",
    sub="Latency reported as a mean hides the tail, and on local hardware the tail is the difference between a working tool and an abandoned one.",
    art="prompt_stream",
    head_at="THE MEAN HIDES THE WAIT",
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="nodes",
    vo="The latency figure, read straight off the board. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second. Prompt processing rate on a four thousand token prompt.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE MEAN HIDES THE WAIT",
    header_at="The latency figure",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    art_at="Picture timing, line",
    chain=[{"t": "at 4,625 T/S", "s": "The wait before any word appears, not the total run", "at": "Time to the"}, {"t": "4K", "s": "This figure does not establish a speed.", "at": "Prompt processing rate"}],
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

NAME = "BYTE-GEN-PA-003"
TITLE = "THE MEAN HIDES THE WAIT"
DOC_TITLE = "THE MEAN HIDES THE WAIT &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
