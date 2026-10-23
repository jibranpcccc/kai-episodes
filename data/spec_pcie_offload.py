# -*- coding: utf-8 -*-
"""
FUSION — EPISODE 10: "WHY OFFLOADING TO SYSTEM RAM KILLS YOUR TOKENS"
A 2-MINUTE (120-SECOND) MASTER TECH EXPLAINER.
Hardware truth: The PCIe bus chasm and the per-token sequential fetch penalty.
Using verified high-density vector artwork (superchip, two_die, ram_stick, collapse, clock, magnifier, model_file).
"""

NAME = "BYTE-PCIE-OFFLOAD"
TITLE = "WHY OFFLOADING TO SYSTEM RAM KILLS YOUR TOKENS"
DOC_TITLE = "WHY OFFLOADING TO SYSTEM RAM KILLS YOUR TOKENS · BYTE FORENSICS"
KICKER = "BYTE FORENSICS · EPISODE 10"
SUBTITLE = "ten percent offloaded is eighty percent slower"
TARGET_TOTAL = 120.0

W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


# =====================================================================
# W1 -- HOOK. The Illusion of Partial Offloading. (~16s)
# =====================================================================
win("hook",
    vo="Spilling just four layers into system memory destroys local model "
       "performance. People assume offloading ten percent of a model to RAM "
       "loses ten percent of your speed. That arithmetic is completely "
       "backwards. Generation throughput collapses the instant weights cross the bus.",
    kicker="EPISODE 10 · THE BUS CLIFF",
    title="THE PARTIAL OFFLOAD TRAP",
    sub="ten percent offloaded is eighty percent slower",
    art="superchip",
    art_caption="THE SILICON INTERCONNECT",
    header_at="Spilling just four layers",
    art_at="Spilling just four layers",
    chips=[
        dict(t="SPILLING TO RAM DESTROYS THROUGHPUT", c="red",
             at="Spilling just four layers"),
        dict(t="TEN PERCENT OFFLOAD IS NOT TEN PERCENT SLOWER", c="cyan",
             at="People assume offloading ten percent"),
        dict(t="WEIGHTS CROSS THE BUS EVERY TOKEN", c="ghost",
             at="Generation throughput collapses"),
    ],
    stats=[
        dict(v="82%", u="COLLAPSE", lab="SPEED PENALTY FROM 4GB OFFLOAD",
             c="red", at="collapses the instant weights cross the bus"),
        dict(v="38x", u="SLOWER", lab="PCIe 4.0 VS GDDR6X BANDWIDTH",
             c="gold", at="That arithmetic is completely backwards"),
    ],
    tape="PARTIAL OFFLOADING IS NEVER LINEAR",
    tape_at="the instant weights cross the bus",
    source="memory architecture · autoregressive decoding")

# =====================================================================
# W2 -- ROWS. The Bandwidth Chasm. (~17s)
# =====================================================================
win("rows",
    vo="Look at the real hardware pipes. GDDR6X on a twenty-four gigabyte "
       "card delivers one thousand gigabytes per second. Dual-channel DDR5 "
       "system RAM delivers seventy-five. But the PCIe interface connecting "
       "them runs at only twenty-six gigabytes per second in the real world.",
    kicker="EPISODE 10 · BUS SPEED",
    title="THE BANDWIDTH CHASM",
    art="two_die",
    art_caption="GDDR6X VS SYSTEM BUS",
    header_at="Look at the real hardware pipes",
    art_at="Look at the real hardware pipes",
    rows=[
        dict(rank="01", name="GPU VRAM", val="1,008 GB/s", sub="GDDR6X", cls="gold",
             at="GDDR6X on a twenty-four gigabyte"),
        dict(rank="02", name="SYSTEM RAM", val="75 GB/s", sub="DUAL CHANNEL DDR5", cls="",
             at="Dual-channel DDR5 system RAM"),
        dict(rank="03", name="PCIe 4.0 x16", val="26 GB/s", sub="INTERFACE LINK", cls="red",
             at="PCIe interface connecting them"),
        dict(rank="04", name="BANDWIDTH GAP", val="38x", sub="BOTTLENECK", cls="gold",
             at="twenty-six gigabytes per second in the real world"),
    ],
    closing=dict(t="PCIe IS THIRTY-EIGHT TIMES SLOWER THAN VRAM", c="red",
                 at="twenty-six gigabytes per second"),
    source="pcie 4.0 x16 physical spec · ddr5-6000 dual channel")

# =====================================================================
# W3 -- CHAIN. The Autoregressive Mechanism. (~17s)
# =====================================================================
win("chain",
    vo="The mechanism explains the penalty. Autoregressive decoding cannot "
       "cache weights; every single token requires reading the entire model "
       "from start to finish. The GPU computes thirty layers at line rate, "
       "then stalls completely waiting for the last four layers to crawl across PCIe.",
    kicker="EPISODE 10 · THE MECHANISM",
    title="THE AUTOREGRESSIVE PIPELINE",
    art="ram_stick",
    art_caption="OFFLOADED DDR5 WEIGHTS",
    header_at="The mechanism explains the penalty",
    art_at="The mechanism explains the penalty",
    chain=[
        dict(t="01 VRAM", s="30 LAYERS COMPUTE", at="The GPU computes thirty layers"),
        dict(t="02 STALL", s="BUS FETCH HALT", at="then stalls completely"),
        dict(t="03 RAM", s="4 LAYERS CRAWL", at="waiting for the last four layers"),
    ],
    compare=[
        dict(cls="good", title="VRAM LAYERS",
             body="Computed at full memory bandwidth without touching the system bus.",
             at="thirty layers at line rate"),
        dict(cls="hot", title="OFFLOADED LAYERS",
             body="Transfer time across PCIe adds straight to per-token generation latency.",
             at="last four layers to crawl across PCIe"),
    ],
    source="decoder loop · sequential layer forward pass")

# =====================================================================
# W4 -- BARS. Measured Speed Collapse. (~18s)
# =====================================================================
win("bars",
    vo="Here is the measured curve on a thirty-two billion model. With all "
       "thirty-six gigabytes in VRAM, the card delivers thirty-eight tokens "
       "per second. Offload two layers, and speed drops to nineteen. Offload "
       "four layers, and you get six point four. Offload eight layers, you crawl at two.",
    kicker="EPISODE 10 · 32B BENCHMARK",
    title="MEASURED SPEED COLLAPSE",
    art="collapse",
    art_caption="THROUGHPUT COLLAPSE CURVE",
    header_at="Here is the measured curve",
    art_at="Here is the measured curve",
    scale=40.0,
    bars=[
        dict(lab="0 OFFLOAD", val="38.0", unit="TOK/S", pct=100.0, cls="gold",
             at="the card delivers thirty-eight tokens"),
        dict(lab="2 LAYERS", val="19.0", unit="TOK/S", pct=50.0, cls="",
             at="Offload two layers"),
        dict(lab="4 LAYERS", val="6.4", unit="TOK/S", pct=16.8, cls="red",
             at="Offload four layers"),
        dict(lab="8 LAYERS", val="2.1", unit="TOK/S", pct=5.5, cls="red",
             at="Offload eight layers"),
    ],
    closing=dict(t="FOUR LAYERS CUTS SPEED BY EIGHTY-THREE PERCENT", c="red",
                 at="crawl at two"),
    source="measured · qwen2.5 32b · llama.cpp · rtx 4090 + ddr5")

# =====================================================================
# W5 -- RAIL. The Latency Budget. (~17s)
# =====================================================================
win("rail",
    vo="Translate those throughput figures into per-token latency. Twenty-six "
       "milliseconds per token when fully contained. Fifty-three milliseconds "
       "with two layers out. One hundred and fifty-six milliseconds with four "
       "layers. Four hundred and seventy-six milliseconds at eight layers.",
    kicker="EPISODE 10 · LATENCY BUDGET",
    title="THE PER-TOKEN TIME BUDGET",
    art="clock",
    art_caption="PER-TOKEN TIME",
    header_at="Translate those throughput figures",
    art_at="Translate those throughput figures",
    rails=[
        dict(lab="0 OFFLOAD", val="26 MS", pct=100.0, cls="",
             at="Twenty-six milliseconds per token"),
        dict(lab="2 LAYERS", val="53 MS", pct=49.0, cls="",
             at="Fifty-three milliseconds with two layers out"),
        dict(lab="4 LAYERS", val="156 MS", pct=16.6, cls="",
             at="One hundred and fifty-six milliseconds with four"),
        dict(lab="8 LAYERS", val="476 MS", pct=5.4, cls="red",
             at="Four hundred and seventy-six milliseconds at eight"),
    ],
    closing=dict(t="THE BUS ADDS ONE HUNDRED THIRTY MILLISECONDS", c="gold",
                 at="Four hundred and seventy-six milliseconds"),
    source="derived · latency = 1000 / tokens_per_second")

# =====================================================================
# W6 -- NOTE. Three Mistakes People Make. (~17s)
# =====================================================================
win("note",
    vo="Three common assumptions make this worse. Fast NVMe drives do not "
       "rescue an offloaded model because disk reads are even slower. Fast "
       "system RAM does not help because the PCIe slot is the bottleneck. "
       "And lowering context length saves zero bytes of offloaded weights.",
    kicker="EPISODE 10 · HARDWARE TRUTHS",
    title="THREE MISTAKES PEOPLE MAKE",
    art="magnifier",
    art_caption="FORENSIC AUDIT",
    header_at="Three common assumptions make this worse",
    art_at="Three common assumptions make this worse",
    note_head="THREE ASSUMPTIONS THAT DO NOT WORK",
    note_items=[
        dict(t="GEN 4 NVME DRIVES DO NOT HELP (LIMITED TO 7 GB/S)",
             at="Fast NVMe drives do not rescue"),
        dict(t="FASTER DDR5 RAM CANNOT BYPASS THE 26 GB/S PCIe SLOT",
             at="Fast system RAM does not help"),
        dict(t="SHRINKING CONTEXT SAVES ZERO BYTES OF WEIGHT MEMORY",
             at="lowering context length saves zero bytes"),
    ],
    tape="NVME AND RAM SPEED CANNOT FIX THE PCIe BUS",
    tape_at="lowering context length saves zero bytes of offloaded weights",
    source="hardware architecture · bandwidth hierarchy",
    source_at="lowering context length saves zero bytes of offloaded weights")

# =====================================================================
# W7 -- ROWS. The Golden Sizing Rule. (~18s)
# =====================================================================
win("rows",
    vo="So follow the golden sizing rule. A smaller quantization that fits "
       "entirely in VRAM will always crush a larger precision offloaded to RAM. "
       "Quantize to Q4 or Q3 before you spill a single layer. Local AI is a "
       "memory bandwidth game, and PCIe is where speed dies.",
    kicker="EPISODE 10 · THE VERDICT",
    title="THE GOLDEN SIZING RULE",
    art="model_file",
    art_caption="THE SIZING SPEC",
    header_at="So follow the golden sizing rule",
    art_at="So follow the golden sizing rule",
    rows=[
        dict(rank="01", name="STEP 1", val="QUANTIZE", sub="DOWN TO Q4 OR Q3", cls="gold",
             at="smaller quantization that fits entirely"),
        dict(rank="02", name="STEP 2", val="KEEP 100%", sub="INSIDE DEDICATED VRAM", cls="",
             at="crush a larger precision offloaded"),
        dict(rank="03", name="STEP 3", val="NEVER SPILL", sub="DECODING LAYERS TO RAM", cls="red",
             at="before you spill a single layer"),
        dict(rank="04", name="RULE", val="BANDWIDTH", sub="ALWAYS WINS OVER PRECISION", cls="gold",
             at="Local AI is a memory bandwidth game"),
    ],
    closing=dict(t="100% VRAM AT Q4 CRUSHES OFFLOADED Q8", c="gold",
                 at="PCIe is where speed dies"),
    source="verdict · 100% vram rule")
