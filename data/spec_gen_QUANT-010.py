# -*- coding: utf-8 -*-
"""Generated from angle QUANT-010 -- THE BENCHMARK NEVER SHOWS THE DRIFT.

Source of truth: data/angles.py (angle) + data/facts.py (every number).
Regenerate with: python data/make_spec.py QUANT-010
"""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

win(
    layout="hook",
    vo="Same board. Same run. Same quant. Picture quantised in blocks. The size of the block scale in the four bit format. The LoRA paper's WikiSQL score for the full fine tune. Keep the source in view.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="THE BENCHMARK NEVER SHOWS THE DRIFT",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="Same board",
    art_at="Picture quantised in",
    chips=[{"t": "32 BIT", "c": "gold", "at": "The size of"}],
    stats=[{"v": "73.8", "u": "", "lab": "FT 73.8", "c": "gold", "at": "The LoRA paper's"}],
    tape="Keep the source in view.",
    tape_at="Keep the source",
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="chain",
    vo="The quant figure, read straight off the board. Picture quantised in blocks. The overhead the block scales add per weight. The LoRA paper's WikiSQL score for LoRA at rank four. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second.",
    kicker="BYTE FORENSICS &middot; QUANT",
    title="THE BENCHMARK NEVER SHOWS THE DRIFT",
    art="gguf_blocks",
    art_caption="QUANTISED IN BLOCKS",
    header_at="The quant figure",
    art_at="Picture quantised in",
    chain=[{"t": "+0.5 BIT", "s": "This figure does not establish that a model fits.", "at": "The overhead the"}],
    compare=[{"cls": "hot", "title": "THE HEADLINE CLAIM", "body": "The claim about LO 89.5, taken on trust.", "at": "The LoRA paper's"}, {"cls": "good", "title": "WHAT WE MEASURED", "body": "The measurement of at 767 T/S, taken on the board.", "at": "Time to the"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="rows",
    vo="One papers number, one source, one board. Picture the paper folder. The LoRA paper's MNLI score for the full fine tune. The LoRA paper's MNLI score for LoRA at rank four. The QLoRA paper's MMLU score for the full fine tune. The QLoRA paper's MMLU score for QLoRA. One method, every row.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="THE BENCHMARK NEVER SHOWS THE DRIFT",
    art="folder",
    art_caption="THE PAPER FOLDER",
    header_at="One papers number",
    art_at="Picture the paper",
    rows=[{"rank": "1", "name": "GPT-3 175B", "val": "73.4", "sub": "FT 73.4", "cls": "gold", "at": "The LoRA paper's MNLI score for the"}, {"rank": "2", "name": "GPT-3 175B", "val": "91.7", "sub": "LO 91.7", "cls": "", "at": "The LoRA paper's MNLI score for LoRA"}, {"rank": "3", "name": "Llama 7B", "val": "38.4", "sub": "FULL 38.4", "cls": "", "at": "The QLoRA paper's MMLU score for the"}, {"rank": "4", "name": "Llama 7B", "val": "39.0", "sub": "QLoRA 39.0", "cls": "", "at": "The QLoRA paper's MMLU score for QLoRA"}],
    closing={"t": "One method, every row.", "c": "gold", "at": "One method, every"},
    source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results",
)

win(
    layout="bars",
    vo="Nothing here about latency is a guess. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Measured, not a fit claim. No fit claim here.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE BENCHMARK NEVER SHOWS THE DRIFT",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Nothing here about",
    art_at="Picture timing, line",
    bars=[{"lab": "Qwen 3.8 27B", "val": "131", "unit": "s", "pct": 100.0, "cls": "red", "at": "Time to the"}],
    closing={"t": "No fit claim here.", "c": "gold", "at": "No fit claim"},
    mid={"t": "Measured, not a fit claim", "c": "cyan", "at": "Measured, not a"},
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="rail",
    vo="This is the latency of the hardware, not of the brochure. Picture timing, line by line. Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second. Same method, every rail.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE BENCHMARK NEVER SHOWS THE DRIFT",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="This is the",
    art_at="Picture timing, line",
    rails=[{"lab": "at 767 T/S", "val": "131", "pct": 100.0, "cls": "red", "at": "Time to the"}],
    closing={"t": "Same method, every rail.", "c": "cyan", "at": "Same method, every"},
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="note",
    vo="Measured latency, on this board, in this run. Picture timing, line by line. The wait before any word appears, not the total run. Keep the source in view. The source sits at the foot of the window.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE BENCHMARK NEVER SHOWS THE DRIFT",
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
    vo="Every latency figure here carries its own source. Picture timing, line by line. On the bench: Muse Glimmer 30B. The overhead the block scales add per weight. The line reads eighty-nine point five, from the same run.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE BENCHMARK NEVER SHOWS THE DRIFT",
    art="timer_flat",
    art_caption="TIMING, LINE BY LINE",
    header_at="Every latency figure",
    art_at="Picture timing, line",
    name="Muse Glimmer 30B",
    blurb="The overhead the block scales add per weight",
    meta="LO 89.5 &middot; 89.5",
    name_at="On the bench",
    blurb_at="The overhead the",
    meta_at="The line reads",
    side="right",
    source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
)

win(
    layout="strip",
    vo="The papers number does the talking, not the claim. Same conditions for every number that follows. Strip by strip: the quant budget figure, the paper budget figure, the latency budget figure.",
    kicker="BYTE FORENSICS &middot; PAPERS",
    title="THE BENCHMARK NEVER SHOWS THE DRIFT",
    header_at="The papers number",
    items=[{"key": "gguf_blocks", "label": "quant budget", "at": "the quant budget figure"}, {"key": "folder", "label": "paper budget", "at": "the paper budget figure"}, {"key": "timer_flat", "label": "latency budget", "at": "the latency budget figure"}],
    source="the documented bits and bytes route &middot; nested quantization",
)

win(
    layout="title",
    vo="One claim, one board, one run. Quantization is a bargain until the model's output drifts, and the drift is invisible on benchmark scores and obvious in use. THE BENCHMARK NEVER SHOWS THE DRIFT.",
    kicker="BYTE FORENSICS &middot; LATENCY",
    title="THE BENCHMARK NEVER SHOWS THE DRIFT",
    sub="Quantization is a bargain until the model's output drifts, and the drift is invisible on benchmark scores and obvious in use.",
    art="timer_flat",
    head_at="THE BENCHMARK NEVER SHOWS THE DRIFT",
    source="the documented bits and bytes route &middot; nested quantization",
)

NAME = "BYTE-GEN-QUANT-010"
TITLE = "THE BENCHMARK NEVER SHOWS THE DRIFT"
DOC_TITLE = "THE BENCHMARK NEVER SHOWS THE DRIFT &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; GENERATED"
SUBTITLE = "a scaffold from the fact base"
GLOBAL_PROGRESS = False
