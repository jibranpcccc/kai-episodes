# -*- coding: utf-8 -*-
"""Episode 09 -- section 4: windows 26-33. What changes the bill."""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


# =====================================================================
# W26a -- ROWS. Quantising the cache. The fp16 baseline.
# =====================================================================
win("rows",
    vo="The cache does not have to sit in full precision. Sixteen bit, at eight "
       "thousand one hundred and ninety-two tokens, two hundred and eighty-eight "
       "mebibytes, the baseline.",
    kicker="KV CACHE &middot; PRECISION &middot; THE BASELINE",
    title="THE CACHE CAN BE HELD COARSER",
    art="gguf_blocks", art_caption="MIXED PRECISION",
    header_at="The cache does not have to sit in full precision",
    art_at="The cache does not have to sit in full precision",
    rows=[
        dict(rank="01", name="PRECISION", val="FP16", sub="SIXTEEN BIT",
             cls="", at="Sixteen bit"),
        dict(rank="02", name="THE CONTEXT", val="8,192", sub="TOKENS",
             cls="", at="eight thousand one hundred and ninety-two tokens"),
        dict(rank="03", name="CACHE SIZE", val="288", sub="MIB, FP16",
             cls="gold", at="two hundred and eighty-eight mebibytes"),
    ],
    closing=dict(t="THE BASELINE TO BEAT", c="cyan", at="the baseline"),
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens "
           "&middot; fp16 &middot; q8_0 34 bytes per 32 values")

# =====================================================================
# W26b -- NODES. Quantising the cache. The same cache, coarser.
# =====================================================================
win("nodes",
    vo="Same formula, fewer bytes per value. Q eight zero, thirty-four bytes to "
       "thirty-two values, the same cache is a hundred and fifty-three mebibytes. "
       "Precision is a choice.",
    kicker="KV CACHE &middot; PRECISION &middot; THE COARSER CACHE",
    title="SAME FORMULA, FEWER BYTES",
    header_at="Same formula, fewer bytes per value",
    art="die", art_caption="COARSER VALUES",
    art_at="Same formula, fewer bytes per value",
    chain=[
        dict(t="Q8_0 BLOCK", s="34 bytes per 32 values",
             at="thirty-four bytes to thirty-two values"),
        dict(t="CACHE AT Q8_0", s="153 MiB at 8,192 tokens",
             at="a hundred and fifty-three mebibytes"),
    ],
    closing=dict(t="PRECISION IS A CHOICE", c="gold", at="Precision is a choice"),
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens "
           "&middot; fp16 &middot; q8_0 34 bytes per 32 values")

# =====================================================================
# W27a -- BARS. fp16 against q8_0, the measured pair.
# =====================================================================
win("bars",
    vo="Two precisions, eight thousand one hundred and ninety-two tokens. "
       "Sixteen bit, two hundred and eighty-eight mebibytes. Q eight zero, "
       "a hundred and fifty-three, with thirty-four bytes to thirty-two values.",
    kicker="KV CACHE &middot; PRECISION &middot; TWO SIZES",
    title="THE SAME CACHE, TWO SIZES",
    art="scales", art_caption="PRECISION",
    header_at="Two precisions",
    art_at="Two precisions",
    bars=[
        dict(lab="FP16", val="288", unit="MiB", pct=100.0, cls="",
             at="two hundred and eighty-eight mebibytes"),
        dict(lab="Q8_0", val="153", unit="MiB", pct=53.1, cls="",
             at="a hundred and fifty-three"),
    ],
    closing=dict(t="COARSER BLOCKS, SMALLER CACHE", c="cyan",
                 at="thirty-four bytes to thirty-two values"),
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens "
           "&middot; q8_0 34 bytes per 32 values &middot; q4_0 assumed "
           "18 bytes per 32 values")

# =====================================================================
# W27b -- ROWS. q4_0, with the assumption stated.
# =====================================================================
win("rows",
    vo="Q four zero, eighty-one mebibytes, with eighteen bytes to thirty-two "
       "values. That size is assumed. The cache is quantised by the runtime, so "
       "read the assumption, not the label.",
    kicker="KV CACHE &middot; PRECISION &middot; THE COARSEST &middot; THE ASSUMPTION",
    title="THE SMALLEST SIZE, AND ITS ASSUMPTION",
    art="wafer", art_caption="COARSEST, ASSUMED",
    header_at="Q four zero",
    art_at="Q four zero",
    rows=[
        dict(rank="01", name="Q4_0 CACHE", val="81", sub="MIB, 8,192 TOKENS",
             cls="red", at="eighty-one mebibytes"),
        dict(rank="02", name="Q4_0 BLOCK", val="18", sub="BYTES PER 32 VALUES",
             cls="", at="eighteen bytes to thirty-two values"),
        dict(rank="03", name="THE ASSUMPTION", val="STATED", sub="NOT MEASURED",
             cls="", at="size is assumed"),
    ],
    closing=dict(t="READ THE ASSUMPTION, NOT THE LABEL", c="gold",
                 at="read the assumption, not the label"),
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens "
           "&middot; q8_0 34 bytes per 32 values &middot; q4_0 assumed "
           "18 bytes per 32 values")

# =====================================================================
# W28 -- NOTE. Quantisation is not free. It changes what you read back.
# =====================================================================
win("note",
    vo="But a smaller cache is not the same answer. Quantising the cache "
       "rounds the keys and values, so the model reads back something slightly "
       "different from what it wrote. Same tokens, same weights, different "
       "output. Whether the runtime will do it at all is a build setting, "
       "not a format.",
    kicker="KV CACHE &middot; WHAT THE SMALLER CACHE COSTS",
    title="A SMALLER CACHE IS NOT THE SAME ANSWER",
    art="caveat", art_caption="READ THE FINE PRINT",
    header_at="But a smaller cache is not the same answer",
    art_at="But a smaller cache is not the same answer",
    note_head="WHAT A SMALLER CACHE COSTS YOU",
    note_items=[
        dict(t="THE KEYS AND VALUES ARE ROUNDED",
             at="Quantising the cache rounds the keys and values"),
        dict(t="THE MODEL READS BACK SOMETHING DIFFERENT",
             at="the model reads back something slightly different"),
        dict(t="SAME TOKENS, SAME WEIGHTS, DIFFERENT OUTPUT",
             at="Same tokens, same weights, different output"),
        dict(t="IT IS A BUILD SETTING, NOT A FORMAT",
             at="is a build setting, not a format"),
    ],
    tape="CHECK THE ROUNDING, NOT THE SIZE",
    tape_at="not a format",
    source="mechanism &middot; a quantised kv cache stores rounded keys and "
           "values &middot; the cache type is a runtime build setting",
    source_at="not a format")

# =====================================================================
# W29 -- ROWS. The workspace and the activations, kept live during a pass.
# =====================================================================
win("rows",
    vo="The cache is only part of the bill. While the model answers, the "
       "runtime keeps a workspace live: the activations for the current layer, "
       "the attention scores it is still computing, and the logits waiting at "
       "the end. That workspace scales with the batch and the sequence. The "
       "file does not.",
    kicker="KV CACHE &middot; THE WORKSPACE",
    title="THE WORKSPACE IS THE OTHER HALF",
    art="chip", art_caption="ONE MODEL, ONE FORMULA",
    header_at="The cache is only part of the bill",
    art_at="The cache is only part of the bill",
    rows=[
        dict(rank="01", name="THE WORKSPACE", val="LIVE", sub="DURING THE PASS",
             cls="gold", at="keeps a workspace live"),
        dict(rank="02", name="ACTIVATIONS", val="ACTIVE",
             sub="THE CURRENT LAYER", cls="",
             at="the activations for the current layer"),
        dict(rank="03", name="ATTENTION SCORES", val="IN FLIGHT",
             sub="THE SCRATCH BUFFER", cls="",
             at="the attention scores it is still computing"),
        dict(rank="04", name="LOGITS", val="WAITING", sub="AT THE END", cls="",
             at="the logits waiting at the end"),
        dict(rank="05", name="SCALES WITH", val="BATCH", sub="AND SEQUENCE",
             cls="red", at="scales with the batch and the sequence"),
        dict(rank="06", name="THE FILE", val="FIXED", sub="DOES NOT SCALE",
             cls="", at="The file does not"),
    ],
    closing=dict(t="THE FILE IS NOT THE BILL", c="gold",
                 at="The file does not"),
    source="mechanism &middot; activations and attention scratch scale with "
           "batch and sequence, not with the file")

# =====================================================================
# W30 -- CHAIN. What stays live during one forward pass.
# =====================================================================
win("chain",
    vo="One forward pass keeps a few things live. The weights are read from "
       "the card. The activations for the layer in front are written. The "
       "attention scores are computed and thrown away. The cache is read and "
       "extended. The weights do not change, and only the cache grows with "
       "the conversation.",
    kicker="KV CACHE &middot; ONE FORWARD PASS",
    title="WHAT IS LIVE AT THE SAME TIME",
    art="pipeline", art_caption="THE PASS",
    header_at="One forward pass keeps a few things live",
    art_at="One forward pass keeps a few things live",
    chain=[
        dict(t="WEIGHTS", s="read from the card",
             at="The weights are read from the card"),
        dict(t="TENSORS", s="activations, written",
             at="The activations for the layer in front are written"),
        dict(t="SCORES", s="computed, then dropped",
             at="The attention scores are computed and thrown away"),
        dict(t="CACHE", s="read and extended",
             at="The cache is read and extended"),
    ],
    compare=[
        dict(cls="good", title="THE WEIGHTS",
             body="They are read on every token, and they are the same size "
                  "whether the answer is short or long.",
             at="The weights do not change"),
        dict(cls="hot", title="THE CACHE",
             body="It is the one thing that keeps growing, and the length of "
                  "the conversation is the only thing that controls it.",
             at="only the cache grows with the conversation"),
    ],
    source="mechanism &middot; a transformer forward pass holds weights, "
           "activations, attention scratch and the kv cache at once")

# =====================================================================
# W31a -- ROWS. Batch size against memory. One request.
# =====================================================================
win("rows",
    vo="Batch size multiplies. Two independent requests in flight do not share one "
       "cache: each has its own keys and its own values. one request is two hundred "
       "and eighty-eight mebibytes, at eight thousand one hundred and ninety two "
       "tokens in sixteen bit. two in flight is twice that.",
    kicker="KV CACHE &middot; BATCH SIZE &middot; ONE REQUEST",
    title="ONE CACHE PER REQUEST",
    art="gpu", art_caption="THE CARD",
    header_at="Batch size multiplies",
    art_at="do not share one cache",
    rows=[
        dict(rank="01", name="ONE REQUEST", val="288", sub="MIB",
             cls="gold", at="one request is two hundred and eighty-eight"),
        dict(rank="02", name="THE CONTEXT", val="8,192", sub="TOKENS, 16 BIT",
             cls="", at="eight thousand one hundred and ninety two tokens"),
        dict(rank="03", name="TWO IN FLIGHT", val="576", sub="NO PREFIX REUSE",
             cls="", at="two in flight is twice that"),
    ],
    closing=dict(t="THE FIGURE IS PER REQUEST", c="cyan",
                 at="two in flight is twice that"),
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request, assuming no prefix is reused")

# =====================================================================
# W31b -- BARS. Batch size against memory. Two and four requests.
# =====================================================================
win("bars",
    vo="Two in flight, five hundred and seventy-six mebibytes. Four in flight, "
       "one thousand one hundred and fifty-two. that is the arithmetic for "
       "independent requests, and that is mechanism, not measurement. "
       "a runtime with prefix caching can reuse a shared prefix. "
       "v l l m does that when the feature is on.",
    kicker="KV CACHE &middot; BATCH SIZE &middot; MORE REQUESTS",
    title="THE ARITHMETIC, WITH NO REUSE",
    art="vram_module", art_caption="TWO AND FOUR AT ONCE",
    header_at="Two in flight",
    art_at="Two in flight",
    bars=[
        dict(lab="2 REQUESTS", val="576", unit="MiB", pct=50.0, cls="",
             at="five hundred and seventy-six"),
        dict(lab="4 REQUESTS", val="1,152", unit="MiB", pct=100.0, cls="red",
             at="one thousand one hundred and fifty-two"),
    ],
    mid=dict(t="DERIVED, NOT MEASURED", c="gold",
             at="that is mechanism, not measurement"),
    closing=dict(t="A SHARED PREFIX CAN BE REUSED", c="cyan",
                 at="v l l m does that when the feature is on"),
    source="derived &middot; qwen2.5 3b instruct &middot; 8,192 tokens &middot; 288 MiB per request, no prefix reuse &middot; vllm automatic prefix caching",
    source_at="v l l m does that when the feature is on")

# =====================================================================
# W32 -- NOTE. Offload, page and spill. What it costs when the cache will
# not fit, measured on two cards against one.
# =====================================================================
win("note",
    vo="The cache does not fit. The runtime pages it to memory, or spills to disk. "
       "It comes back across the bus, the wait is paid every token. "
       "at sixty four K, same model and context: the rtx forty "
       "ninety, thirty-eight point four one tokens a second. two sixteen "
       "gigabyte cards, eighteen point five.",
    kicker="KV CACHE &middot; WHEN IT DOES NOT FIT",
    title="PAGE IT, OR SPILL IT",
    art="collapse", art_caption="THE COLLAPSE",
    header_at="The cache does not fit",
    art_at="The cache does not fit",
    note_head="WHAT THE RUNTIME DOES INSTEAD",
    note_items=[
        dict(t="PAGE IT TO SYSTEM MEMORY", at="pages it to memory"),
        dict(t="SPILL IT TO DISK", at="spills to disk"),
        dict(t="PAY THE WAIT ACROSS THE BUS", at="comes back across the bus"),
        dict(t="SAME MODEL, SAME CONTEXT", at="same model and context"),
        dict(t="RTX 4090, 24 GB, 38.41 T/S",
             at="thirty-eight point four one"),
        dict(t="2× RTX 5060 TI, 18.50 T/S", at="eighteen point five"),
    ],
    tape="SPLITTING THE BILL IS NOT FREE",
    tape_at="eighteen point five",
    source="measured &middot; hardware-corner.net &middot; qwen 3.8 27b at 64k &middot; generation t/s: rtx 4090 38.41, 2× rtx 5060 ti 18.50",
    source_at="eighteen point five")

# =====================================================================
# W33 -- NODES. The summary. What actually moves the number.
# =====================================================================
win("nodes",
    vo="So what moves the number. The precision the cache is held in. The "
       "workspace a pass keeps live. The batch size. Paging and spilling. And "
       "the context length, the only one you control.",
    kicker="KV CACHE &middot; WHAT MOVES THE NUMBER",
    title="WHAT ACTUALLY MOVES THE NUMBER",
    art="memory_bank", art_caption="THE BANK",
    header_at="So what moves the number",
    art_at="So what moves the number",
    chain=[
        dict(t="PRECISION", s="of the cache",
             at="The precision the cache is held in"),
        dict(t="WORKSPACE", s="kept live per pass",
             at="The workspace a pass keeps live"),
        dict(t="BATCH", s="requests in flight", at="The batch size"),
        dict(t="OFFLOAD", s="paged or spilled", at="Paging and spilling"),
        dict(t="CONTEXT", s="the one you control",
             at="the context length"),
    ],
    closing=dict(t="CONTEXT LENGTH IS YOUR INPUT", c="gold",
                 at="the only one you control"),
    source="mechanism &middot; cache precision, forward pass workspace, batch "
           "size and offload &middot; the context length is the input you "
           "control")
