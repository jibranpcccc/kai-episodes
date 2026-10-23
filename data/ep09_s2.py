# -*- coding: utf-8 -*-
"""Episode 09 -- section 2: windows 8-16. What the cache actually is."""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


# =====================================================================
# W8 -- GALLERY. Three different things people call memory.
# =====================================================================
win("gallery",
    vo="a model server holds three things people call memory. the weights on disk, "
       "the weights loaded onto the card, and the cache. the first is a file you can "
       "copy. the second is the model, in video memory. the third is scratch, and the "
       "only one that grows while you talk.",
    kicker="KV CACHE &middot; THREE THINGS CALLED MEMORY",
    title="THREE THINGS CALLED MEMORY",
    art="cache_grid", art_caption="ONE GRID, THREE USES",
    header_at="a model server holds",
    art_at="the weights on disk",
    name="THE FILE ON DISK",
    blurb="THE MODEL, IN VIDEO MEMORY",
    meta="AND SCRATCH, THE ONLY ONE THAT GROWS",
    name_at="the first is a file you can copy",
    blurb_at="the second is the model, in video memory",
    meta_at="the only one that grows while you talk",
    side="left",
    source="mechanism &middot; hardware-corner.net &middot; the weights on disk, the "
           "weights in VRAM and the kv cache are separate allocations")

# =====================================================================
# W9 -- NOTE. The cache is not the file.
# =====================================================================
win("note",
    vo="the cache is not the file. it is separate from the weights. it lives "
       "in runtime memory while the conversation runs. how long it lives "
       "depends on the serving system: usually it goes when the process "
       "exits, but llama.cpp can save a slot to disk and reuse it later. "
       "runtime state, not a stored artifact.",
    kicker="KV CACHE &middot; WHAT IT IS",
    title="THE CACHE IS NOT THE FILE",
    art="caveat", art_caption="RUNTIME STATE",
    header_at="the cache is not the file",
    art_at="it is separate from the weights",
    note_head="WHAT THE CACHE IS",
    note_items=[
        dict(t="not the weights", at="it is separate from the weights"),
        dict(t="runtime memory, not the file", at="it lives in runtime memory"),
        dict(t="how long it lives depends on the system",
             at="how long it lives depends on the serving system"),
        dict(t="usually gone when the process exits", at="usually it goes when the process exits"),
        dict(t="some runtimes save or reuse it", at="llama.cpp can save a slot"),
    ],
    tape="SEPARATE FROM THE WEIGHTS &middot; NOT ALWAYS TRANSIENT",
    tape_at="llama.cpp can save a slot to disk and reuse it later",
    source="mechanism &middot; llama.cpp server --slot-save-path, --cache-prompt, --cache-reuse &middot; vllm automatic prefix caching",
    source_at="not a stored artifact")

# =====================================================================
# W10 -- ROWS. What is inside the cache.
# =====================================================================
win("rows",
    vo="inside the cache, every token that has been said leaves a key, and leaves a "
       "value. one vector each, written once per layer. this config has thirty-six "
       "layers, two key-value heads, and a head dimension of one hundred and "
       "twenty-eight. two vectors per token per layer is what gets written.",
    kicker="KV CACHE &middot; WHAT IS INSIDE IT",
    title="WHAT THE CACHE HOLDS",
    art="vram_module", art_caption="KEYS AND VALUES",
    header_at="inside the cache",
    art_at="one vector each",
    rows=[
        dict(rank="01", name="KEY VECTOR", val="1", sub="one per token, per layer",
             cls="gold", at="leaves a key"),
        dict(rank="02", name="VALUE VECTOR", val="1", sub="written beside the key",
             cls="", at="leaves a value"),
        dict(rank="03", name="LAYERS", val="36", sub="each layer keeps its own",
             cls="", at="thirty-six layers"),
        dict(rank="04", name="KV HEADS", val="2", sub="shared by the group query",
             cls="", at="two key-value heads"),
        dict(rank="05", name="HEAD DIM", val="128", sub="numbers across one head",
             cls="", at="one hundred and twenty-eight"),
    ],
    closing=dict(t="two vectors per token, per layer", c="gold",
                 at="two vectors per token per layer"),
    source="derived &middot; qwen2.5 3b instruct config &middot; 36 layers, 2 kv "
           "heads, head dim 128")

# =====================================================================
# W11 -- CHAIN. Prefill writes it, decode reads it.
# =====================================================================
win("chain",
    vo="the cache has two phases. the prompt arrives. prefill reads it and writes the "
       "whole prompt into the cache. then decode reads the cache back, one token at a "
       "time, and extends it by one entry. the file is read-only. the cache is "
       "written again for every token it produces.",
    kicker="KV CACHE &middot; TWO PHASES",
    title="PREFILL WRITES, DECODE READS",
    art="pipeline", art_caption="PROMPT TO OUTPUT",
    header_at="the cache has two phases",
    art_at="one token at a time",
    chain=[
        dict(t="PROMPT", s="tokens arrive", at="the prompt arrives"),
        dict(t="PREFILL", s="read the whole prompt", at="prefill reads"),
        dict(t="CACHE WRITTEN", s="one entry per token",
             at="writes the whole prompt into the cache"),
        dict(t="DECODE", s="one token at a time", at="then decode reads the cache back"),
        dict(t="CACHE READ", s="one more entry",
             at="extends it by one entry"),
    ],
    compare=[
        dict(cls="good", title="THE FILE",
             body="Read-only. It never changes while the model runs.",
             at="the file is read-only"),
        dict(cls="hot", title="THE CACHE",
             body="Written again for every token it produces.",
             at="the cache is written again for every token"),
    ],
    source="mechanism &middot; hardware-corner.net &middot; prefill writes the cache, "
           "decode reads it and extends it")

# =====================================================================
# W12 -- STRIP. The three states a cache is in.
# =====================================================================
win("strip",
    vo="a cache sits in one of three states. it is allocated, the buffer is reserved "
       "but empty. it is filled, every token so far has a key and a value in it. and it "
       "is trimmed, the oldest entries dropped.",
    kicker="KV CACHE &middot; THREE STATES",
    title="THREE STATES A CACHE IS IN",
    header_at="a cache sits in one of three states",
    items=[
        dict(key="token_blocks", label="ALLOCATED", at="it is allocated"),
        dict(key="context_window", label="FILLED", at="it is filled"),
        dict(key="collapse", label="TRIMMED", at="it is trimmed"),
    ],
    closing=dict(t="RESERVED BEFORE IT IS USED", c="gold",
                 at="the oldest entries dropped"),
    source="mechanism &middot; runtime cache lifecycle &middot; allocate, fill, trim "
           "under a fixed budget")

# =====================================================================
# W13 -- ROWS. How a runtime stores it.
# =====================================================================
win("rows",
    vo="a runtime usually keeps the cache in one contiguous buffer on the card. one "
       "row for each layer, with the keys and the values laid out side by side inside "
       "that row. as the conversation grows, the buffer grows with it, and it is "
       "resized on the device while it runs.",
    kicker="KV CACHE &middot; HOW A RUNTIME STORES IT",
    title="ONE BUFFER, ONE ROW PER LAYER",
    art="context_window", art_caption="LAYOUT ON THE CARD",
    header_at="a runtime usually keeps the cache",
    art_at="one contiguous buffer on the card",
    rows=[
        dict(rank="01", name="THE BUFFER", val="1", sub="contiguous, resident on the card",
             cls="gold", at="in one contiguous buffer"),
        dict(rank="02", name="ROWS", val="36", sub="one per layer",
             cls="", at="one row for each layer"),
        dict(rank="03", name="LAYOUT", val="K | V", sub="keys and values side by side",
             cls="", at="keys and the values laid out side by side"),
        dict(rank="04", name="GROWTH", val="+1", sub="one entry appended per token",
             cls="", at="the buffer grows with it"),
    ],
    closing=dict(t="resized on the device, while it runs", c="cyan",
                 at="it is resized on the device while it runs"),
    source="mechanism &middot; hardware-corner.net &middot; llama.cpp build 153d324bc, "
           "flash attention, full offload")

# =====================================================================
# W14a -- BARS. The cache scales with the context, the first half.
# =====================================================================
win("bars",
    vo="the cache scales with the context, linearly. four thousand ninety-six tokens, "
       "one hundred and forty-four mebibytes. eight thousand one hundred and "
       "ninety-two, two hundred and eighty-eight.",
    kicker="KV CACHE &middot; SCALES WITH CONTEXT",
    title="DOUBLE THE TOKENS, DOUBLE THE CACHE",
    art="memory_bank", art_caption="CACHE SIZE BY CONTEXT",
    header_at="the cache scales with the context",
    art_at="linearly",
    bars=[
        dict(lab="4,096 TOKENS", val="144", unit="MiB", pct=12.5, cls="",
             at="four thousand ninety-six tokens"),
        dict(lab="8,192 TOKENS", val="288", unit="MiB", pct=25, cls="",
             at="eight thousand one hundred and ninety-two"),
    ],
    closing=dict(t="THE SCALE IS LINEAR HERE", c="gold",
                 at="two hundred and eighty-eight"),
    source="derived &middot; qwen2.5 3b instruct config at fp16 &middot; 36 layers, "
           "2 kv heads, head dim 128 &middot; not a fit claim")

# =====================================================================
# W14b -- ROWS. The cache scales with the context, the second half.
# =====================================================================
win("rows",
    vo="the scale continues. sixteen thousand three hundred and eighty-four, five "
       "hundred and seventy-six. thirty-two thousand seven hundred and sixty-eight, "
       "one thousand one hundred and fifty-two. derived, not measured.",
    kicker="KV CACHE &middot; SCALES WITH CONTEXT &middot; THE LONG END",
    title="AND IT KEEPS DOUBLING",
    art="context_window", art_caption="THE LONGER HALF",
    header_at="the scale continues",
    art_at="five hundred and seventy-six",
    rows=[
        dict(rank="01", name="16,384 TOKENS", val="576", sub="MiB, fp16", cls="",
             at="sixteen thousand three hundred and eighty-four"),
        dict(rank="02", name="32,768 TOKENS", val="1,152", sub="MiB, fp16", cls="red",
             at="thirty-two thousand seven hundred and sixty-eight"),
    ],
    closing=dict(t="DERIVED, NOT MEASURED", c="cyan", at="derived, not measured"),
    source="derived &middot; qwen2.5 3b instruct config at fp16 &middot; 36 layers, "
           "2 kv heads, head dim 128 &middot; not a fit claim")

# =====================================================================
# W15 -- NODES. The cost of the next token.
# =====================================================================
win("nodes",
    vo="the cost of the next token is the whole cache, and the bill is read-side. it "
       "reads every key and value back, attends across all of them, and appends one "
       "more entry at the end. the read grows, the write stays at one.",
    kicker="KV CACHE &middot; THE COST OF THE NEXT TOKEN",
    title="THE WHOLE CACHE, EVERY TOKEN",
    art="pipeline", art_caption="READ, ATTEND, APPEND",
    header_at="the cost of the next token",
    art_at="it reads every key and value back",
    chain=[
        dict(t="READ THE CACHE", s="every key and value", at="the whole cache"),
        dict(t="ATTEND OVER IT", s="across all of them", at="attends across all of them"),
        dict(t="WRITE ONE MORE ENTRY", s="one entry appended",
             at="appends one more entry at the end"),
    ],
    closing=dict(t="THE WRITE IS CHEAP, THE READ IS NOT", c="gold",
                 at="the write stays at one"),
    source="measured &middot; hardware-corner.net &middot; qwen 3.8 27b on an rtx 3090 &middot; generation throughput falls as the context grows")

# =====================================================================
# W16 -- HOOK. The second bill.
# =====================================================================
win("hook",
    vo="so here is the second bill. the weights are the first bill, they sit and do "
       "not move. the cache is the second bill: it grows with every token, charged to "
       "the card while you talk. two hundred and eighty-eight mebibytes at eight "
       "thousand one hundred and ninety-two tokens.",
    kicker="KV CACHE &middot; THE SECOND BILL",
    title="THE SECOND BILL",
    art="prompt_stream", art_caption="WEIGHTS THEN CACHE",
    header_at="here is the second bill",
    art_at="the cache is the second bill",
    chips=[
        dict(t="THE WEIGHTS SIT, THEY DO NOT GROW", c="gold",
             at="the weights are the first bill"),
        dict(t="THE CACHE GROWS WITH EVERY TOKEN", c="red",
             at="it grows with every token"),
        dict(t="IT IS CHARGED TO THE CARD", c="cyan",
             at="charged to the card while you talk"),
    ],
    stats=[
        dict(v="288", u="MiB", lab="CACHE AT 8,192 TOKENS", c="gold",
             at="two hundred and eighty-eight mebibytes"),
    ],
    tape="THE WEIGHTS SIT STILL &middot; THE CACHE DOES NOT",
    tape_at="two hundred and eighty-eight mebibytes at eight thousand one hundred "
            "and ninety-two tokens",
    source="derived &middot; qwen2.5 3b instruct config at 8,192 tokens fp16 &middot; "
           "not a fit claim",
    source_at="two hundred and eighty-eight mebibytes at eight thousand one hundred "
              "and ninety-two tokens")
