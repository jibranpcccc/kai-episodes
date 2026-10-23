# -*- coding: utf-8 -*-
"""Episode 09 -- section 5: windows 34-38. The measurement you can take."""
W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


# =====================================================================
# W34 -- ROWS. The checklist.
# =====================================================================
win("rows",
    vo="Before you buy anything, write down five lines. The context you will "
       "really send. The model you will run. The precision of the weights. "
       "The precision of the cache. And the headroom left for the workspace. "
       "Each one is a decision, and each one moves the bill.",
    kicker="KV CACHE &middot; THE CHECKLIST",
    title="WHAT TO WRITE DOWN BEFORE YOU BUY",
    art="checklist", art_caption="THE CHECKLIST",
    header_at="Before you buy anything",
    art_at="Before you buy anything",
    rows=[
        dict(rank="01", name="CONTEXT", val="YOU SEND", sub="THE REAL NUMBER", cls="gold",
             at="The context you will really send"),
        dict(rank="02", name="MODEL", val="YOU RUN", sub="SHAPE, NOT PARAMS", cls="",
             at="The model you will run"),
        dict(rank="03", name="WEIGHTS", val="PRECISION", sub="THE FILE", cls="",
             at="The precision of the weights"),
        dict(rank="04", name="CACHE", val="PRECISION", sub="THE SECOND BILL", cls="",
             at="The precision of the cache"),
        dict(rank="05", name="HEADROOM", val="THE REST", sub="WORKSPACE AND ACTIVATIONS", cls="",
             at="And the headroom left for the workspace"),
    ],
    closing=dict(t="FIVE LINES, NOT A FEELING", c="gold", at="each one moves the bill"),
    source="the method &middot; measure before you buy")

# =====================================================================
# W35 -- NODES. The order of operations.
# =====================================================================
win("nodes",
    vo="Measure in this order. The weights, because that is the file you can "
       "size before you load anything. The cache, because that is the part "
       "that moves with the prompt. The workspace, because that is the part "
       "nobody prices. Then, and only then, the card.",
    kicker="KV CACHE &middot; THE ORDER",
    title="MEASURE IN THIS ORDER",
    art="pipeline", art_caption="THE ORDER",
    header_at="Measure in this order",
    art_at="Measure in this order",
    chain=[
        dict(t="WEIGHTS", s="the file on disk", at="The weights, because"),
        dict(t="CACHE", s="it moves with the prompt", at="The cache, because"),
        dict(t="WORKSPACE", s="nobody prices it", at="The workspace, because"),
        dict(t="THE CARD", s="now you can pick one", at="Then, and only then, the card"),
    ],
    source="the method &middot; measure the parts before the card")

# =====================================================================
# W36 -- BARS. The measured curve read as a card, not a graph.
# =====================================================================
win("bars",
    vo="A twenty-four gigabyte card holds four K at eighteen gigabytes, "
       "leaving six for everything else. Sixteen K costs nineteen, so five "
       "are left. Sixty-four K costs twenty-two, so two are left. One "
       "twenty-eight K needs twenty-six, two more than the card has. it does "
       "not fit at all.",
    kicker="KV CACHE &middot; WHAT FITS",
    title="THE SAME CARD, AND LESS ROOM EVERY STEP",
    art="vram_module", art_caption="VRAM ON A 24 GB CARD",
    header_at="A twenty-four gigabyte card",
    art_at="A twenty-four gigabyte card",
    bars=[
        dict(lab="4K",    val="18", unit="GB", pct=52.9, cls="",    at="holds four K at eighteen gigabytes"),
        dict(lab="16K",   val="19", unit="GB", pct=55.9, cls="",    at="Sixteen K costs nineteen"),
        dict(lab="64K",   val="22", unit="GB", pct=64.7, cls="",    at="Sixty-four K costs twenty-two"),
        dict(lab="128K",  val="26", unit="GB", pct=76.5, cls="red", at="One twenty-eight K needs twenty-six"),
    ],
    scale=34,
    mark=dict(pct=70.59, lab="24 GB CARD"),
    closing=dict(t="AT 128K IT DOES NOT FIT", c="red",
                 at="it does not fit at all"),
    source="derived &middot; hardware-corner.net &middot; qwen3.8 27b &middot; 24 gb card &middot; 128k is a requirement above the card, not a fit")

# =====================================================================
# W37 -- HOOK. The real question, before the arithmetic.
# =====================================================================
win("hook",
    vo="Before you size a cache, decide what the model is for. A "
       "classification on a short document does not need a window. A long "
       "document that must be answered in one piece does. The context is the "
       "requirement, and the bill follows the requirement.",
    kicker="KV CACHE &middot; THE REAL QUESTION",
    title="WHAT IS THE MODEL ACTUALLY FOR",
    art="question", art_caption="THE QUESTION",
    header_at="Before you size a cache",
    art_at="Before you size a cache",
    chips=[
        dict(t="A SHORT DOCUMENT NEEDS NO WINDOW", c="cyan",
             at="A classification on a short document"),
        dict(t="A LONG DOCUMENT NEEDS ALL OF IT", c="gold",
             at="A long document that must be answered"),
        dict(t="THE CONTEXT IS THE REQUIREMENT", c="red",
             at="The context is the requirement"),
    ],
    stats=[
        dict(v="1", u="CONTEXT", lab="YOU CHOOSE EVERY TIME", c="gold",
             at="The context is the requirement"),
        dict(v="0", u="GUESSES", lab="AFTER THE MEASUREMENT", c="cyan",
             at="The context is the requirement"),
    ],
    tape="SIZE THE JOB, THEN THE CARD",
    tape_at="the bill follows the requirement",
    source="the requirement &middot; measure the job, not the model")

# =====================================================================
# W38 -- NOTE. The verdict. The last window of the episode.
# =====================================================================
win("note",
    vo="The verdict is plain. The weights are what you downloaded. The cache "
       "is what the conversation costs. Neither number replaces the other, and "
       "neither one is a fit claim. Measure the cache at the length you will "
       "really use, and buy for that.",
    kicker="KV CACHE &middot; THE VERDICT",
    title="THE CACHE IS THE SECOND BILL",
    art="caveat", art_caption="THE VERDICT",
    header_at="The verdict is plain",
    art_at="The verdict is plain",
    note_head="WHAT TO TAKE AWAY",
    note_items=[
        dict(t="THE WEIGHTS ARE THE FILE, THE CACHE IS THE CONVERSATION",
             at="The weights are what you downloaded"),
        dict(t="NEITHER NUMBER IS A FIT CLAIM",
             at="neither one is a fit claim"),
        dict(t="MEASURE AT THE LENGTH YOU WILL REALLY USE",
             at="Measure the cache at the length"),
    ],
    tape="THE SECOND BILL IS THE ONE YOU CAN MEASURE",
    tape_at="buy for that",
    source="the verdict &middot; measure the cache before you buy",
    source_at="buy for that")
