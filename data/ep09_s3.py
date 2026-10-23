# -*- coding: utf-8 -*-
"""Episode 09 -- section 3: windows 17-25. What was measured."""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


# =====================================================================
# W17a -- ROWS. The rig, exactly. The machine.
# =====================================================================
win("rows",
    vo=("the rig, exactly. the operating system: ubuntu twenty four point zero four. "
        "the driver: five nine five point five eight point zero three. "
        "the qwen run used cuda twelve point eight. the muse glimmer run used cuda thirteen."),
    kicker="KV CACHE &middot; THE RIG &middot; THE MACHINE",
    title="THE MACHINE, EXACTLY",
    art="motherboard", art_caption="ONE MACHINE",
    header_at="the rig, exactly",
    art_at="ubuntu twenty four point zero four",
    rows=[
        dict(rank="01", name="OPERATING SYSTEM", val="Ubuntu 24.04", sub="ubuntu", cls="", at="operating system"),
        dict(rank="02", name="DRIVER", val="595.58.03", sub="version", cls="", at="driver"),
        dict(rank="03", name="CUDA, QWEN RUN", val="12.8", sub="toolkit", cls="gold", at="cuda twelve point eight"),
        dict(rank="04", name="CUDA, GLIMMER RUN", val="13", sub="toolkit", cls="", at="cuda thirteen"),
    ],
    closing=dict(t="ONE BUILD, TWO RUNS", c="gold",
                 at="the muse glimmer run used cuda thirteen"),
    source="measured &middot; hardware-corner.net &middot; two benchmark posts, same driver and llama.cpp build &middot; 12 and 17 Aug 2026")


# =====================================================================
# W17b -- NODES. The rig, exactly. The stack.
# =====================================================================
win("nodes",
    vo=("the stack, exactly. runtime: llama.cpp build one five three d three two four "
        "b c. attention: flash attention. offload: full offload. "
        "two runs share that build. cuda twelve point eight on the qwen run. "
        "cuda thirteen on the glimmer run."),
    kicker="KV CACHE &middot; THE RIG &middot; THE STACK",
    title="THE STACK, EXACTLY",
    header_at="the stack, exactly",
    art="chip", art_caption="RUNTIME, ATTENTION, OFFLOAD",
    art_at="one five three d three two four b c",
    chain=[
        dict(t="RUNTIME BUILD", s="llama.cpp 153d324bc", at="runtime: llama.cpp"),
        dict(t="ATTENTION", s="flash attention", at="attention: flash attention"),
        dict(t="OFFLOAD MODE", s="all layers on the card", at="offload: full offload"),
        dict(t="QWEN RUN", s="cuda 12.8, 17 aug 2026", at="cuda twelve point eight on the qwen run"),
        dict(t="GLIMMER RUN", s="cuda 13, 12 aug 2026", at="cuda thirteen on the glimmer run"),
    ],
    closing=dict(t="ONE BUILD, TWO CUDA VERSIONS", c="gold",
                 at="cuda thirteen on the glimmer run"),
    source="measured &middot; hardware-corner.net &middot; llama.cpp 153d324bc in both posts &middot; flash attention, full offload")


# =====================================================================
# W18a -- BARS. The full VRAM curve, the first half.
# =====================================================================
win("bars",
    vo=("the curve so far: qwen three point eight twenty seven billion, on the rtx "
        "thirty ninety. four k, eighteen gigabytes. sixteen k, nineteen. "
        "thirty two k, twenty. all of them on one twenty four gigabyte card."),
    kicker="KV CACHE &middot; MEASURED &middot; QWEN 3.8 27B",
    title="THE CURVE STARTS FLAT",
    art="gauge", art_caption="ONE 24 GB CARD",
    header_at="the curve so far",
    art_at="one twenty four gigabyte card",
    bars=[
        dict(lab="4K", val="18", unit="GB", pct=52.9, cls="", at="four k, eighteen gigabytes"),
        dict(lab="16K", val="19", unit="GB", pct=55.9, cls="", at="sixteen k, nineteen"),
        dict(lab="32K", val="20", unit="GB", pct=58.8, cls="", at="thirty two k, twenty"),
    ],
    scale=34,
    mark=dict(pct=70.59, lab="24 GB CARD"),
    closing=dict(t="ONE CARD, THREE STEPS", c="cyan", at="one twenty four gigabyte card"),
    source="measured &middot; hardware-corner.net &middot; qwen 3.8 27b on an rtx 3090, full offload &middot; llama.cpp 153d324bc")


# =====================================================================
# W18b -- ROWS. The full VRAM curve, the steep end.
# =====================================================================
win("rows",
    vo=("the curve steepens. sixty four k, twenty two gigabytes, measured on the card. "
        "one hundred twenty eight k needs twenty six. two hundred fifty six k needs "
        "thirty four. both of those are larger than a twenty four gigabyte card."),
    kicker="KV CACHE &middot; MEASURED &middot; THE STEEP END",
    title="WHERE THE CURVE STEEPENS",
    art="vram_module", art_caption="VRAM AT LENGTH",
    header_at="the curve steepens",
    art_at="sixty four k",
    rows=[
        dict(rank="01", name="64K", val="22 GB", sub="ON THE CARD", cls="",
             at="twenty two gigabytes"),
        dict(rank="02", name="128K", val="26 GB", sub="REQUIRED", cls="red",
             at="one hundred twenty eight k needs twenty six"),
        dict(rank="03", name="256K", val="34 GB", sub="REQUIRED", cls="red",
             at="two hundred fifty six k needs thirty four"),
    ],
    closing=dict(t="NEITHER FITS ON THE CARD", c="red",
                 at="larger than a twenty four gigabyte card"),
    source="measured &middot; hardware-corner.net &middot; qwen 3.8 27b &middot; 64k measured on an rtx 3090 &middot; 128k and 256k are the requirement")


# =====================================================================
# W19 -- NOTE. The curve is not linear.
# =====================================================================
win("note",
    vo=("here is what is bending. the cache itself is linear: twice the tokens, "
        "twice the cache. the weights are a fixed cost, and the runtime takes "
        "its own share. so the early steps look cheap, because the fixed part "
        "hides them, and the late steps look steep. read the marginal cost, "
        "not the total."),
    kicker="KV CACHE &middot; WHAT BENDS",
    title="THE TOTAL BENDS, THE CACHE DOES NOT",
    art="caveat", art_caption="READ THE SLOPE",
    header_at="here is what is bending",
    art_at="the cache itself is linear",
    note_head="WHAT IS ACTUALLY BENDING",
    note_items=[
        dict(t="THE CACHE IS LINEAR IN TOKENS", at="twice the tokens, twice the cache"),
        dict(t="THE WEIGHTS ARE A FIXED COST", at="the weights are a fixed cost"),
        dict(t="THE RUNTIME TAKES ITS OWN SHARE", at="the runtime takes its own share"),
        dict(t="THE EARLY STEPS LOOK CHEAP", at="the early steps look cheap"),
        dict(t="READ THE MARGINAL COST", at="read the marginal cost"),
    ],
    tape="THE TOTAL IS NOT THE CACHE",
    tape_at="not the total",
    source="derived &middot; hardware-corner.net &middot; the cache is linear in cached tokens &middot; the measured curve is weights plus cache plus runtime overhead",
    source_at="not the total")


# =====================================================================
# W20 -- ROWS. Where the knee is.
# =====================================================================
win("rows",
    vo=("these steps cost. four k to sixteen k, one gigabyte. "
        "sixteen to thirty two, one. thirty two to sixty four, two. "
        "sixty four to one hundred twenty eight, four. "
        "one hundred twenty eight to two fifty six, eight gigabytes. "
        "each step doubles the tokens. read them as steps, not a scale."),
    kicker="KV CACHE &middot; THE STEPS",
    title="WHERE THE STEP GROWS",
    art="scales", art_caption="MARGINAL COST",
    header_at="these steps cost",
    art_at="one gigabyte",
    rows=[
        dict(rank="01", name="4K TO 16K", val="1 GB", sub="one step", cls="", at="four k to sixteen k"),
        dict(rank="02", name="16K TO 32K", val="1 GB", sub="still one", cls="", at="sixteen to thirty two"),
        dict(rank="03", name="32K TO 64K", val="2 GB", sub="the step doubles", cls="", at="thirty two to sixty four"),
        dict(rank="04", name="64K TO 128K", val="4 GB", sub="the cache doubles", cls="gold",
             at="sixty four to one hundred twenty eight"),
        dict(rank="05", name="128K TO 256K", val="8 GB", sub="and doubles again", cls="red",
             at="one hundred twenty eight to two fifty six"),
    ],
    closing=dict(t="THE LAST STEP COSTS EIGHT GIGABYTES", c="red", at="eight gigabytes"),
    source="derived &middot; hardware-corner.net &middot; steps of the measured total VRAM curve &middot; the cache inside each step is linear",
    source_at="not a scale")


# =====================================================================
# W21a -- BARS. Two models, one card, the short contexts.
# =====================================================================
win("bars",
    vo=("two models, one twenty four gigabyte card: muse glimmer thirty billion, "
        "qwen three point eight twenty seven billion. "
        "four k: sixteen against eighteen. thirty two k: sixteen against twenty."),
    kicker="KV CACHE &middot; TWO MODELS &middot; ONE CARD",
    title="ONE CARD, TWO MODELS",
    art="gpu", art_caption="TWO MODELS, ONE CARD",
    header_at="two models, one twenty four gigabyte card",
    art_at="muse glimmer thirty billion",
    bars=[
        dict(lab="4K GLIMMER", val="16", unit="GB", pct=47.1, cls="", at="four k: sixteen"),
        dict(lab="4K QWEN", val="18", unit="GB", pct=52.9, cls="", at="against eighteen"),
        dict(lab="32K GLIMMER", val="16", unit="GB", pct=47.1, cls="", at="thirty two k: sixteen"),
        dict(lab="32K QWEN", val="20", unit="GB", pct=58.8, cls="", at="sixteen against twenty"),
    ],
    closing=dict(t="THE GAP IS FOUR GIGABYTES", c="gold", at="against twenty"),
    source="measured &middot; hardware-corner.net &middot; two benchmark posts &middot; muse glimmer 30b from the 12 aug post, qwen 3.8 27b from the 17 aug post &middot; rtx 3090, one 24 gb card")


# =====================================================================
# W21b -- ROWS. Two models, one card, the long contexts.
# =====================================================================
win("rows",
    vo=("the same card, longer context. sixty four k: seventeen against twenty two. "
        "two hundred fifty six k: twenty against thirty four. "
        "and the smaller model carries the bigger bill."),
    kicker="KV CACHE &middot; TWO MODELS &middot; THE LONG END",
    title="THE GAP AT THE LONG END",
    art="scales", art_caption="TWO BILLS, ONE CARD",
    header_at="the same card, longer context",
    art_at="against twenty two",
    rows=[
        dict(rank="01", name="64K GLIMMER", val="17 GB", sub="REQUIRED", cls="",
             at="sixty four k: seventeen"),
        dict(rank="02", name="64K QWEN", val="22 GB", sub="ON THE CARD", cls="",
             at="twenty two"),
        dict(rank="03", name="256K GLIMMER", val="20 GB", sub="REQUIRED", cls="",
             at="two hundred fifty six k: twenty"),
        dict(rank="04", name="256K QWEN", val="34 GB", sub="OVER THE CARD",
             cls="red", at="against thirty four"),
    ],
    closing=dict(t="SMALLER MODEL, BIGGER BILL", c="gold",
                 at="the smaller model carries the bigger bill"),
    source="measured &middot; hardware-corner.net &middot; two benchmark posts &middot; muse glimmer 30b from the 12 aug post, qwen 3.8 27b from the 17 aug post &middot; rtx 3090, one 24 gb card")


# =====================================================================
# W22 -- STRIP. What each card size holds.
# =====================================================================
win("strip",
    vo=("three ways to hold a model, sixty four k. "
        "the rtx forty ninety, twenty four gigabytes: thirty eight point four one "
        "per second. two sixteen gigabyte cards, thirty two together: "
        "eighteen point five. the m five max, unified memory: eighteen point two. "
        "generation numbers, not fit claims."),
    kicker="KV CACHE &middot; THE HARDWARE &middot; QWEN 3.8 27B",
    title="WHAT THE CARD HOLDS",
    header_at="three ways to hold a model",
    items=[
        dict(key="vram_module", label="RTX 4090 &middot; 24 GB", at="the rtx forty ninety"),
        dict(key="sodimm", label="2&times; RTX 5060 Ti &middot; 32 GB", at="two sixteen gigabyte cards"),
        dict(key="ram_stick", label="M5 MAX &middot; UNIFIED MEMORY", at="the m five max"),
    ],
    closing=dict(t="THE CARDS ARE NOT INTERCHANGEABLE", c="gold",
                 at="not fit claims"),
    source="measured &middot; hardware-corner.net &middot; qwen 3.8 27b at 64k &middot; generation t/s: rtx 4090 38.41, 2&times; rtx 5060 ti 18.50, m5 max 128 gb unified 18.2")


# =====================================================================
# W23 -- RAIL. Time to first token.
# =====================================================================
win("rail",
    vo=("the wait before the first token. a hundred thousand token prompt on the rtx "
        "fifty ninety, at four thousand six hundred and twenty five tokens a second, "
        "takes twenty two seconds. same card, same model, at one thousand eight "
        "hundred and seventy four tokens a second, takes fifty three. "
        "speed and latency are not the same."),
    kicker="KV CACHE &middot; LATENCY",
    title="TIME TO FIRST TOKEN",
    art="clock", art_caption="100K PROMPT",
    header_at="the wait before the first token",
    art_at="takes twenty two seconds",
    rails=[
        dict(lab="4,625 T/S", val="22 S", pct=41.5, cls="",
             at="four thousand six hundred and twenty five tokens a second"),
        dict(lab="1,874 T/S", val="53 S", pct=100.0, cls="red",
             at="one thousand eight hundred and seventy four tokens a second"),
    ],
    closing=dict(t="FIRST TOKEN, THEN THROUGHPUT", c="gold",
                 at="speed and latency are not the same"),
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b on an rtx 5090 &middot; 100k prompt at the 4k and 256k prefill rates")


# =====================================================================
# W24 -- NOTE. What a throughput number hides.
# =====================================================================
win("note",
    vo=("a throughput number hides the wait. tokens per second is not latency. "
        "the wait happens before the first token, and a benchmark chart does not show it. "
        "a fast card can still feel slow. the same context, a different wait. "
        "the wait is the part you feel."),
    kicker="KV CACHE &middot; THE HIDDEN PART",
    title="WHAT A RATE HIDES",
    art="clock", art_caption="THE WAIT",
    header_at="a throughput number hides the wait",
    art_at="a benchmark chart does not show it",
    note_head="WHAT A TOKENS-PER-SECOND NUMBER HIDES",
    note_items=[
        dict(t="T/S IS NOT LATENCY", at="tokens per second is not latency"),
        dict(t="THE WAIT IS BEFORE THE FIRST TOKEN", at="the wait happens before the first token"),
        dict(t="A FAST CARD CAN STILL FEEL SLOW", at="a fast card can still feel slow"),
        dict(t="THE SAME CONTEXT, A DIFFERENT WAIT", at="the same context"),
    ],
    tape="READ THE WAIT, NOT THE RATE",
    tape_at="the part you feel",
    source="derived &middot; hardware-corner.net &middot; latency read from the time to first token measurements",
    source_at="a different wait")


# =====================================================================
# W25 -- TITLE. Act break, the part people quote wrong.
# =====================================================================
win("title",
    vo=("here is the part people quote wrong. a longer context is only slower, "
        "but it is also a larger memory bill. the next act is about what changes the bill."),
    kicker="ACT BREAK &middot; KV CACHE",
    title="THE PART PEOPLE QUOTE WRONG",
    sub="a longer context is also a larger memory bill",
    art="token_blocks",
    head_at="here is the part people quote wrong",
    closing=dict(t="NOT ONLY SLOWER", c="gold",
                 at="it is also a larger memory bill"),
    tape="WHAT CHANGES THE BILL",
    tape_at="the next act is about what changes the bill",
    source="measured &middot; hardware-corner.net &middot; rtx 3090, rtx 4090, rtx 5090, 2&times; rtx 5060 ti, m5 max, gb10 &middot; section three, what was measured",
    source_at="the next act is about what changes the bill")
