# -*- coding: utf-8 -*-
"""
THE FACT BASE
=============
Every measurable fact about the Byte Forensics niche, in one place, with its
provenance attached.

This is the file that makes a hundred unique scripts possible without
re-researching the same hardware for every one of them. A script chooses an
angle and a slice of these facts; it never invents a number.

Each record carries:
    id        stable key, used by the scaffold generator
    topic     the bucket it belongs to, used to slice a fact set for an angle
    model     which model the figure belongs to
    card      which hardware the figure was measured on
    label     what the row or bar is called on screen
    value     the number
    unit      the unit printed next to it on screen
    pct       the bar fill percentage, proportional to the value
    claim     the sentence the narration can say about it
    source    the source line printed at the foot of the window
    caveat    what the figure does NOT establish, if anything

SOURCES
    hardware-corner.net, We Tested Qwen3.8 27B
        https://www.hardware-corner.net/qwen3-8-27b-hardware-tests/
    hardware-corner.net, Muse Glimmer 30B Hardware Requirements and Benchmarks
        https://www.hardware-corner.net/hardware-for-muse-glimmer-30b-llm/
    rig for both measured sets: Ubuntu 24.04, driver 595.58.03, CUDA 12.8,
    llama.cpp build 153d324bc, Flash Attention, full offload. Updated 17 Aug 2026.

    The LoRA paper: arXiv 2106.09685
    The QLoRA paper: arXiv 2305.14314
    Qwen2.5 3B Instruct: 36 layers, 2 KV heads, head dim 128, hidden 2048,
        16 query heads, FFN 8192, tied embeddings.

MEASURED means measured on that rig. DERIVED means computed from a config
that is stated on screen. A record is never both, and a derived record always
names the formula.
"""

# --------------------------------------------------------------------- rigs
RIG = "measured &middot; hardware-corner.net &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload"

RIG_QWEN = "measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload"

RIG_GLIMMER = "measured &middot; hardware-corner.net &middot; muse glimmer 30b &middot; llama.cpp 153d324bc &middot; ubuntu 24.04 &middot; cuda 12.8 &middot; flash attention &middot; full offload"

# ------------------------------------------------------------------- facts
FACTS = [
    # ---- total VRAM in use, Qwen 3.8 27B, one 24 GB card ----------------
    dict(id="vram.qwen38.4k", topic="vram", model="Qwen 3.8 27B",
         card="24 GB", label="4K", value=18, unit="GB", pct=52.9,
         claim="Total VRAM in use with a four thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="vram.qwen38.8k", topic="vram", model="Qwen 3.8 27B",
         card="24 GB", label="8K", value=18, unit="GB", pct=52.9,
         claim="Total VRAM in use with an eight thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="vram.qwen38.16k", topic="vram", model="Qwen 3.8 27B",
         card="24 GB", label="16K", value=19, unit="GB", pct=55.9,
         claim="Total VRAM in use with a sixteen thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="vram.qwen38.32k", topic="vram", model="Qwen 3.8 27B",
         card="24 GB", label="32K", value=20, unit="GB", pct=58.8,
         claim="Total VRAM in use with a thirty-two thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="vram.qwen38.64k", topic="vram", model="Qwen 3.8 27B",
         card="24 GB", label="64K", value=22, unit="GB", pct=64.7,
         claim="Total VRAM in use with a sixty-four thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="vram.qwen38.128k", topic="vram", model="Qwen 3.8 27B",
         card="24 GB", label="128K", value=26, unit="GB", pct=76.5,
         claim="Total VRAM in use with a one hundred twenty-eight thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="vram.qwen38.256k", topic="vram", model="Qwen 3.8 27B",
         card="24 GB", label="256K", value=34, unit="GB", pct=100.0,
         claim="Total VRAM in use with a two hundred fifty-six thousand token context",
         source=RIG_QWEN,
         caveat="Does not fit on a twenty-four gigabyte card at all"),

    # ---- total VRAM in use, Muse Glimmer 30B, same card -------------------
    dict(id="vram.glimmer.4k", topic="vram", model="Muse Glimmer 30B",
         card="24 GB", label="4K", value=16, unit="GB", pct=47.1,
         claim="Total VRAM in use with a four thousand token context",
         source=RIG_GLIMMER, caveat=""),
    dict(id="vram.glimmer.32k", topic="vram", model="Muse Glimmer 30B",
         card="24 GB", label="32K", value=16, unit="GB", pct=47.1,
         claim="Total VRAM in use with a thirty-two thousand token context",
         source=RIG_GLIMMER, caveat=""),
    dict(id="vram.glimmer.64k", topic="vram", model="Muse Glimmer 30B",
         card="24 GB", label="64K", value=17, unit="GB", pct=50.0,
         claim="Total VRAM in use with a sixty-four thousand token context",
         source=RIG_GLIMMER, caveat=""),
    dict(id="vram.glimmer.256k", topic="vram", model="Muse Glimmer 30B",
         card="24 GB", label="256K", value=20, unit="GB", pct=58.8,
         claim="Total VRAM in use with a two hundred fifty-six thousand token context",
         source=RIG_GLIMMER, caveat=""),

    # ---- prompt processing, prefill, Muse Glimmer 30B --------------------
    dict(id="prefill.glimmer.4k", topic="prefill", model="Muse Glimmer 30B",
         card="24 GB", label="4K", value=4625, unit="T/S", pct=100.0,
         claim="Prompt processing rate on a four thousand token prompt",
         source=RIG_GLIMMER, caveat=""),
    dict(id="prefill.glimmer.16k", topic="prefill", model="Muse Glimmer 30B",
         card="24 GB", label="16K", value=4373, unit="T/S", pct=94.5,
         claim="Prompt processing rate on a sixteen thousand token prompt",
         source=RIG_GLIMMER, caveat=""),
    dict(id="prefill.glimmer.64k", topic="prefill", model="Muse Glimmer 30B",
         card="24 GB", label="64K", value=3606, unit="T/S", pct=78.0,
         claim="Prompt processing rate on a sixty-four thousand token prompt",
         source=RIG_GLIMMER, caveat=""),
    dict(id="prefill.glimmer.128k", topic="prefill", model="Muse Glimmer 30B",
         card="24 GB", label="128K", value=2806, unit="T/S", pct=60.7,
         claim="Prompt processing rate on a one hundred twenty-eight thousand token prompt",
         source=RIG_GLIMMER, caveat=""),
    dict(id="prefill.glimmer.256k", topic="prefill", model="Muse Glimmer 30B",
         card="24 GB", label="256K", value=1874, unit="T/S", pct=40.5,
         claim="Prompt processing rate on a two hundred fifty-six thousand token prompt",
         source=RIG_GLIMMER, caveat=""),

    # ---- prompt processing, prefill, Qwen 3.8 27B ------------------------
    dict(id="prefill.qwen38.4k", topic="prefill", model="Qwen 3.8 27B",
         card="24 GB", label="4K", value=3749, unit="T/S", pct=100.0,
         claim="Prompt processing rate on a four thousand token prompt",
         source=RIG_QWEN, caveat=""),
    dict(id="prefill.qwen38.128k", topic="prefill", model="Qwen 3.8 27B",
         card="24 GB", label="128K", value=461, unit="T/S", pct=12.3,
         claim="Prompt processing rate on a one hundred twenty-eight thousand token prompt",
         source=RIG_QWEN, caveat=""),

    # ---- generation throughput, Qwen 3.8 27B -----------------------------
    dict(id="gen.5090.4k", topic="generation", model="Qwen 3.8 27B",
         card="RTX 5090 24 GB", label="4K", value=74.8, unit="T/S", pct=100.0,
         claim="Generation rate on a five-oh-ninety with a four thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="gen.5090.16k", topic="generation", model="Qwen 3.8 27B",
         card="RTX 5090 24 GB", label="16K", value=52.2, unit="T/S", pct=69.8,
         claim="Generation rate on a five-oh-ninety with a sixteen thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="gen.5090.32k", topic="generation", model="Qwen 3.8 27B",
         card="RTX 5090 24 GB", label="32K", value=38.0, unit="T/S", pct=50.8,
         claim="Generation rate on a five-oh-ninety with a thirty-two thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="gen.5090.128k", topic="generation", model="Qwen 3.8 27B",
         card="RTX 5090 24 GB", label="128K", value=22.8, unit="T/S", pct=30.5,
         claim="Generation rate on a five-oh-ninety with a one hundred twenty-eight thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="gen.3090.4k", topic="generation", model="Qwen 3.8 27B",
         card="RTX 3090 24 GB", label="4K", value=40.3, unit="T/S", pct=100.0,
         claim="Generation rate on a three thousand ninety with a four thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="gen.3090.32k", topic="generation", model="Qwen 3.8 27B",
         card="RTX 3090 24 GB", label="32K", value=37.0, unit="T/S", pct=91.8,
         claim="Generation rate on a three thousand ninety with a thirty-two thousand token context",
         source=RIG_QWEN, caveat=""),
    dict(id="gen.3090.64k", topic="generation", model="Qwen 3.8 27B",
         card="RTX 3090 24 GB", label="64K", value=33.9, unit="T/S", pct=84.1,
         claim="Generation rate on a three thousand ninety with a sixty-four thousand token context",
         source=RIG_QWEN, caveat=""),

    # ---- two cards against one card -------------------------------------
    dict(id="cards.2x16.4k", topic="capacity", model="Qwen 3.8 27B",
         card="2 x 16 GB", label="2 cards 4K", value=22.5, unit="T/S", pct=59.1,
         claim="Generation rate on two sixteen gigabyte cards with a four thousand token context",
         source=RIG_QWEN, caveat="A pair of cards never buys speed"),
    dict(id="cards.2x16.128k", topic="capacity", model="Qwen 3.8 27B",
         card="2 x 16 GB", label="2 cards 128K", value=15.6, unit="T/S", pct=41.0,
         claim="Generation rate on two sixteen gigabyte cards with a one hundred twenty-eight thousand token context",
         source=RIG_QWEN, caveat="A pair of cards never buys speed"),
    dict(id="cards.1x24.128k", topic="capacity", model="Qwen 3.8 27B",
         card="1 x 24 GB", label="1 card 128K", value=38.1, unit="T/S", pct=100.0,
         claim="Generation rate on one twenty-four gigabyte card with a one hundred twenty-eight thousand token context",
         source=RIG_QWEN, caveat="One card is faster than two at the same context"),

    # ---- time to first token --------------------------------------------
    dict(id="ttft.fast.100k", topic="latency", model="Muse Glimmer 30B",
         card="24 GB", label="at 4,625 T/S", value=22, unit="s", pct=17.0,
         claim="Time to the first word for a hundred thousand token prompt at four thousand six hundred and twenty-five tokens a second",
         source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
         caveat="The wait before any word appears, not the total run"),
    dict(id="ttft.slow.100k", topic="latency", model="Qwen 3.8 27B",
         card="24 GB", label="at 767 T/S", value=131, unit="s", pct=100.0,
         claim="Time to the first word for a hundred thousand token prompt at seven hundred and sixty-seven tokens a second",
         source="derived &middot; 100,000 tokens &divide; prompt processing rate &middot; rounded to the second",
         caveat="The wait before any word appears, not the total run"),

    # ---- the KV cache, derived from a stated config ---------------------
    dict(id="cache.qwen25.fp16.8k", topic="cache", model="Qwen2.5 3B Instruct",
         card="", label="8,192 TOKENS", value=288, unit="MiB", pct=100.0,
         claim="The key value cache of a three billion model at eight thousand one hundred and ninety-two tokens, in full precision",
         source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16",
         caveat="One number, one config, one precision"),
    dict(id="cache.qwen25.fp16.8k.gb", topic="cache", model="Qwen2.5 3B Instruct",
         card="", label="0.302 GB", value=0.302, unit="GB", pct=100.0,
         claim="The same cache in decimal gigabytes",
         source="derived &middot; 288 MiB &middot; 301,989,888 bytes &middot; qwen2.5 3b instruct &middot; fp16",
         caveat="Decimal gigabytes, not binary ones"),
    dict(id="cache.qwen25.q8.8k", topic="cache", model="Qwen2.5 3B Instruct",
         card="", label="Q8_0 PAYLOAD", value=153, unit="MiB", pct=53.1,
         claim="The same cache held in eight bit blocks, at thirty-four bytes for every thirty-two values",
         source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; q8_0 34 bytes per 32 values",
         caveat="A rounded cache changes what the model reads back"),
    dict(id="cache.qwen25.q4.8k", topic="cache", model="Qwen2.5 3B Instruct",
         card="", label="Q4_0 PAYLOAD", value=81, unit="MiB", pct=28.1,
         claim="The same cache held in four bit blocks, at eighteen bytes for every thirty-two values",
         source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; q4_0 18 bytes per 32 values &middot; assumed block shape",
         caveat="The four bit block size is an assumption stated on screen, not a measured figure"),
    dict(id="cache.batch.1", topic="cache", model="Qwen2.5 3B Instruct",
         card="", label="1 REQUEST", value=288, unit="MiB", pct=25.0,
         claim="The cache for a single request in flight",
         source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request",
         caveat="Mechanism, not measurement"),
    dict(id="cache.batch.2", topic="cache", model="Qwen2.5 3B Instruct",
         card="", label="2 REQUESTS", value=576, unit="MiB", pct=50.0,
         claim="The cache for two requests in flight",
         source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request &middot; multiplied by the requests in flight",
         caveat="Mechanism, not measurement"),
    dict(id="cache.batch.4", topic="cache", model="Qwen2.5 3B Instruct",
         card="", label="4 REQUESTS", value=1152, unit="MiB", pct=100.0,
         claim="The cache for four requests in flight",
         source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request &middot; multiplied by the requests in flight",
         caveat="Mechanism, not measurement"),

    # ---- the LoRA arithmetic --------------------------------------------
    dict(id="lora.layers", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="LAYERS", value=36, unit="", pct=None,
         claim="The layer count of the model",
         source="derived &middot; qwen2.5 3b instruct &middot; architecture", caveat=""),
    dict(id="lora.kvheads", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="KV HEADS", value=2, unit="", pct=None,
         claim="The number of key value heads, shared across groups",
         source="derived &middot; qwen2.5 3b instruct &middot; architecture", caveat=""),
    dict(id="lora.headdim", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="HEAD DIM", value=128, unit="", pct=None,
         claim="The width of one attention head",
         source="derived &middot; qwen2.5 3b instruct &middot; architecture", caveat=""),
    dict(id="lora.hidden", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="HIDDEN", value=2048, unit="", pct=None,
         claim="The hidden width of the model",
         source="derived &middot; qwen2.5 3b instruct &middot; architecture", caveat=""),
    dict(id="lora.ffn", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="FFN", value=8192, unit="", pct=None,
         claim="The feed forward width of the model",
         source="derived &middot; qwen2.5 3b instruct &middot; architecture", caveat=""),
    dict(id="lora.qheads", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="QUERY HEADS", value=16, unit="", pct=None,
         claim="The number of query heads",
         source="derived &middot; qwen2.5 3b instruct &middot; architecture", caveat=""),
    dict(id="lora.valueout", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="VALUE OUTPUT", value=256, unit="", pct=None,
         claim="The value projection output width, not the hidden width",
         source="derived &middot; qwen2.5 3b instruct &middot; architecture", caveat=""),
    dict(id="lora.qv.65536", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="QUERY", value=65536, unit="", pct=None,
         claim="The added query parameters at rank sixteen",
         source="derived &middot; rank 16 &middot; qwen2.5 3b instruct", caveat=""),
    dict(id="lora.qv.36864", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="VALUE", value=36864, unit="", pct=None,
         claim="The added value parameters at rank sixteen",
         source="derived &middot; rank 16 &middot; qwen2.5 3b instruct", caveat=""),
    dict(id="lora.perlayer", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="PER LAYER", value=102400, unit="", pct=None,
         claim="The added parameters in one layer at rank sixteen",
         source="derived &middot; rank 16 &middot; qwen2.5 3b instruct", caveat=""),
    dict(id="lora.total.qv", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="TRAINABLE", value=3686400, unit="", pct=None,
         claim="The total trainable parameters with rank sixteen on the query and value projections only",
         source="derived &middot; rank 16 &middot; query and value only &middot; no trained biases", caveat=""),
    dict(id="lora.total.seven", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="TRAINABLE", value=25067520, unit="", pct=None,
         claim="The total trainable parameters with rank sixteen on seven projections",
         source="derived &middot; rank 16 &middot; seven projections targeted &middot; qwen2.5 3b instruct", caveat=""),
    dict(id="lora.arrays.16b", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="PER VALUE", value=16, unit="B", pct=None,
         claim="The bytes per trainable value, across the weight, the gradient and the optimizer state",
         source="derived &middot; 16 bytes per trainable value &middot; fp32 weight, gradient and two optimizer moments", caveat=""),
    dict(id="lora.arrays.30m", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="AT 30M", value=457, unit="MiB", pct=100.0,
         claim="The adapter arrays at thirty million trainable values",
         source="derived &middot; 30,000,000 values &middot; 16 bytes each &middot; an upper bound, not the exact count",
         caveat="An upper bound. The exact count for this model is twenty-five million, and that gives three hundred and eighty-two mebibytes"),
    dict(id="lora.tied.311m", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="TIED", value=311, unit="M", pct=None,
         claim="The parameters in the tied embedding matrix",
         source="derived &middot; 151,936 rows &times; 2,048 wide &middot; qwen2.5 3b instruct", caveat=""),
    dict(id="lora.tied.1.245gb", topic="lora", model="Qwen2.5 3B Instruct",
         card="", label="TENSOR", value=1.245, unit="GB", pct=None,
         claim="The tied embedding matrix in decimal gigabytes, in full precision",
         source="derived &middot; tensor arithmetic, not an allocation measurement", caveat=""),

    # ---- the papers ------------------------------------------------------
    dict(id="paper.lora.73.8", topic="papers", model="GPT-3 175B",
         card="", label="FT 73.8", value=73.8, unit="", pct=None,
         claim="The LoRA paper's WikiSQL score for the full fine tune",
         source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results", caveat=""),
    dict(id="paper.lora.89.5", topic="papers", model="GPT-3 175B",
         card="", label="LO 89.5", value=89.5, unit="", pct=None,
         claim="The LoRA paper's WikiSQL score for LoRA at rank four",
         source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results", caveat=""),
    dict(id="paper.lora.73.4", topic="papers", model="GPT-3 175B",
         card="", label="FT 73.4", value=73.4, unit="", pct=None,
         claim="The LoRA paper's MNLI score for the full fine tune",
         source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results", caveat=""),
    dict(id="paper.lora.91.7", topic="papers", model="GPT-3 175B",
         card="", label="LO 91.7", value=91.7, unit="", pct=None,
         claim="The LoRA paper's MNLI score for LoRA at rank four",
         source="the LoRA paper &middot; arXiv 2106.09685 &middot; task specific results", caveat=""),
    dict(id="paper.qlora.38.4", topic="papers", model="Llama 7B",
         card="", label="FULL 38.4", value=38.4, unit="", pct=None,
         claim="The QLoRA paper's MMLU score for the full fine tune",
         source="the QLoRA paper &middot; arXiv 2305.14314 &middot; llama 7b on alpaca", caveat=""),
    dict(id="paper.qlora.39.0", topic="papers", model="Llama 7B",
         card="", label="QLoRA 39.0", value=39.0, unit="", pct=None,
         claim="The QLoRA paper's MMLU score for QLoRA",
         source="the QLoRA paper &middot; arXiv 2305.14314 &middot; llama 7b on alpaca", caveat=""),
    dict(id="paper.qlora.45.6", topic="papers", model="Llama 7B",
         card="", label="FULL 45.6", value=45.6, unit="", pct=None,
         claim="The QLoRA paper's FLAN v2 score for the full fine tune",
         source="the QLoRA paper &middot; arXiv 2305.14314 &middot; llama 7b on alpaca", caveat=""),
    dict(id="paper.qlora.44.5", topic="papers", model="Llama 7B",
         card="", label="QLoRA 44.5", value=44.5, unit="", pct=None,
         claim="The QLoRA paper's FLAN v2 score for QLoRA",
         source="the QLoRA paper &middot; arXiv 2305.14314 &middot; llama 7b on alpaca", caveat=""),
    dict(id="paper.qlora.delta.mmlu", topic="papers", model="Llama 7B",
         card="", label="MMLU", value=0.6, unit="pp", pct=None,
         claim="The movement in MMLU between the full fine tune and QLoRA",
         source="the QLoRA paper &middot; percentage point movement &middot; 5-shot MMLU", caveat=""),
    dict(id="paper.qlora.delta.flan", topic="papers", model="Llama 7B",
         card="", label="FLAN V2", value=-1.1, unit="pp", pct=None,
         claim="The movement in FLAN v2 between the full fine tune and QLoRA",
         source="the QLoRA paper &middot; percentage point movement &middot; FLAN v2", caveat=""),
    dict(id="paper.demo.65b", topic="papers", model="Llama 65B",
         card="48 GB", label="MODEL", value=65, unit="B", pct=None,
         claim="The model in the demonstration that made the technique famous",
         source="the QLoRA paper &middot; arXiv 2305.14314 &middot; 65b on one 48 gb card", caveat=""),
    dict(id="paper.demo.48gb", topic="papers", model="Llama 65B",
         card="48 GB", label="CARD", value=48, unit="GB", pct=None,
         claim="The size of the card in that demonstration",
         source="the QLoRA paper &middot; arXiv 2305.14314 &middot; 65b on one 48 gb card", caveat=""),

    # ---- quantization of the weights -------------------------------------
    dict(id="quant.nf4.32bit", topic="quant", model="Qwen2.5 3B Instruct",
         card="", label="32 BIT", value=32, unit="", pct=None,
         claim="The size of the block scale in the four bit format",
         source="the documented bits and bytes route &middot; nested quantization", caveat=""),
    dict(id="quant.nf4.0.5bit", topic="quant", model="Qwen2.5 3B Instruct",
         card="", label="+0.5 BIT", value=0.5, unit="", pct=None,
         claim="The overhead the block scales add per weight",
         source="the documented bits and bytes route &middot; nested quantization", caveat=""),
    dict(id="quant.nf4.4127", topic="quant", model="Qwen2.5 3B Instruct",
         card="", label="EFFECTIVE", value=4.127, unit="", pct=None,
         claim="The effective bits per converted weight in the pinned implementation, with the nested scales compressed too",
         source="the pinned implementation &middot; nested quantization &middot; large tensor average", caveat=""),
]

# ------------------------------------------------------------------ helpers
def by_topic(*topics):
    """Every fact in the given topics, in file order."""
    out = [f for f in FACTS if f["topic"] in topics]
    return out


def by_id(*ids):
    """Specific facts by id."""
    index = {f["id"]: f for f in FACTS}
    return [index[i] for i in ids]


def topic_list():
    seen = []
    for f in FACTS:
        if f["topic"] not in seen:
            seen.append(f["topic"])
    return seen


if __name__ == "__main__":
    print("%d facts across %d topics" % (len(FACTS), len(topic_list())))
    for t in topic_list():
        n = len(by_topic(t))
        print("  %-12s %d" % (t, n))
    bad = [f["id"] for f in FACTS if not f.get("source")]
    if bad:
        print("FACTS WITH NO SOURCE:", bad)
    else:
        print("every fact carries a source")
