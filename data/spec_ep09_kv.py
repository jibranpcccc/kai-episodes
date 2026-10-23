# -*- coding: utf-8 -*-
"""
EPISODE 09 (KV CACHE) -- OPENING CLIP
======================================
The first two minutes of Episode 09. Same pipeline, same design system, same
voice as BYTE-LORA. This file grows into the full episode.

  data/spec_ep09_kv.py  ->  data/fusion_build.py  ->  BYTE-EP09-KV.html

THE ANGLE
    The KV cache is a second bill. The weights never move; the cache grows with
    every token you send, and it is the reason a card that was fine five
    minutes ago stops being fine.

THE SPINE (the channel's shape)
    hook -> mechanism -> the arithmetic -> what was measured -> what the wait
    costs -> the boundary of the number -> the method

THE RULES THIS FILE KEEPT
    * every window closes on a beat, so no window ends on a frozen screen
    * no two consecutive windows share a layout
    * every window carries a source with a checkable identifier
    * a unit on screen is stated here, never guessed by the builder
    * every number on screen is a number the script says out loud
    * elements are listed in the order the script says them, because the
      builder sorts arrivals by word time and the DOM order is the visual order

FIGURES AND WHERE THEY COME FROM
    hardware-corner.net, We Tested Qwen3.8 27B
        https://www.hardware-corner.net/qwen3-8-27b-hardware-tests/
    hardware-corner.net, Muse Glimmer 30B Hardware Requirements and Benchmarks
        https://www.hardware-corner.net/hardware-for-muse-glimmer-30b-llm/
    rig for both: Ubuntu 24.04, driver 595.58.03, CUDA 12.8,
    llama.cpp build 153d324bc, Flash Attention, full offload. Updated 17 Aug 2026.
    The KV cache arithmetic is derived from the Qwen2.5 3B Instruct config:
    36 layers, 2 KV heads, head dim 128, fp16.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

NAME = "BYTE-EP09-KV"
TITLE = "WHY A LONGER CONTEXT COSTS YOU MORE MEMORY"
DOC_TITLE = "WHY A LONGER CONTEXT COSTS YOU MORE MEMORY &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; EPISODE 09"
SUBTITLE = "the cache is a second bill"

W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


# =====================================================================
# W1 -- HOOK. The paradox: the conversation outlives the card.
# =====================================================================
win("hook",
    vo="A model can hold a conversation its card can no longer afford. "
       "Nothing was added. No weight changed. The context grew, and the cache "
       "grew with it. That second bill is the one nobody quotes.",
    kicker="KV CACHE &middot; THE SECOND BILL",
    title="THE CONVERSATION OUTLIVES THE CARD",
    art="kv_cache", art_caption="KEYS AND VALUES",
    header_at="A model can hold",
    art_at="A model can hold",
    chips=[
        dict(t="THE WEIGHTS NEVER MOVE", c="gold",
             at="No weight changed"),
        dict(t="THE ONLY INPUT YOU CONTROL IS THE LENGTH", c="ghost",
             at="The context grew"),
        dict(t="THE CACHE GROWS WITH EVERY TOKEN", c="red",
             at="the cache grew with it"),
        dict(t="A LONGER PROMPT IS A BIGGER BILL", c="cyan",
             at="That second bill"),
    ],
    stats=[
        dict(v="288 MiB", u="CACHE", lab="FP16, 8,192 TOKENS", c="gold",
             at="the cache grew with it"),
        dict(v="0", u="NEW WEIGHTS", lab="SAME CARD, SAME MODEL", c="cyan",
             at="the cache grew with it"),
    ],
    tape="THE SECOND BILL IS THE ONE NOBODY QUOTES",
    tape_at="nobody quotes",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128")

# =====================================================================
# W2 -- CHAIN. The mechanism, in three steps.
# =====================================================================
win("chain",
    vo="The mechanism is simple enough to hold. Each token arrives, every "
       "attention layer writes a key and a value into the cache, and every "
       "layer after that reads them back. The cache fills while the weights "
       "sit still.",
    kicker="KV CACHE &middot; HOW IT FILLS",
    title="EVERY TOKEN ADDS TWO VECTORS",
    art="cache_grid", art_caption="THE CACHE",
    header_at="The mechanism is simple",
    art_at="The mechanism is simple",
    chain=[
        dict(t="TOKEN", s="it arrives", at="Each token arrives"),
        dict(t="KEY", s="it is written in", at="writes a key and a value"),
        dict(t="VALUE", s="every layer reads it back", at="reads them back"),
    ],
    compare=[
        dict(cls="hot", title="THE CACHE",
             body="It holds one key and one value per layer per token, and it "
                  "does not let go until the request ends.",
             at="The cache fills"),
        dict(cls="good", title="THE WEIGHTS",
             body="They do not change while the model answers. They are the "
                  "same size at one token and at a hundred thousand.",
             at="The weights sit still"),
    ],
    source="mechanism &middot; transformer key value cache")

# =====================================================================
# W3 -- ROWS. The arithmetic, from a real config.
# =====================================================================
win("rows",
    vo="Take a three billion model with thirty-six layers, two key value "
       "heads and a head width of one hundred and twenty-eight. Two bytes for "
       "every number. Multiply by eight thousand one hundred and ninety-two "
       "tokens and the cache is two hundred and eighty-eight mebibytes. Zero "
       "point three zero two gigabytes.",
    kicker="KV CACHE &middot; THE ARITHMETIC",
    title="THE BILL, TOKEN BY TOKEN",
    art="chip", art_caption="ONE MODEL, ONE FORMULA",
    header_at="Take a three billion model",
    art_at="Take a three billion model",
    rows=[
        dict(rank="01", name="LAYERS", val="36", sub="BLOCKS", cls="gold",
             at="thirty-six layers"),
        dict(rank="02", name="KV HEADS", val="2", sub="SHARED", cls="",
             at="two key value heads"),
        dict(rank="03", name="HEAD WIDTH", val="128", sub="VALUES", cls="",
             at="one hundred and twenty-eight"),
        dict(rank="04", name="BYTES EACH", val="2", sub="FP16", cls="",
             at="Two bytes for every number"),
        dict(rank="05", name="TOKENS", val="8,192", sub="IN THE REQUEST", cls="",
             at="eight thousand one hundred and ninety-two"),
        dict(rank="06", name="CACHE TOTAL", val="288 MiB", sub="0.302 GB", cls="gold",
             at="two hundred and eighty-eight mebibytes"),
    ],
    closing=dict(t="THE WEIGHTS NEVER MOVED", c="gold",
                 at="Zero point three zero two gigabytes"),
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; head dim 128 &middot; fp16")

# =====================================================================
# W4 -- BARS. What was actually measured. One card, one model, one variable.
# =====================================================================
win("bars",
    vo="Now the measured curve. Eighteen gigabytes at four K. Nineteen at "
       "sixteen. Twenty-two at sixty-four. Those three ran on a twenty-four "
       "gigabyte card. At one twenty-eight K the requirement is twenty-six "
       "gigabytes. At two fifty-six, thirty-four. Both are larger than that "
       "card, so neither ran on it.",
    kicker="KV CACHE &middot; MEASURED &middot; QWEN 3.8 27B",
    title="THE FILE DOES NOT MOVE, THE CACHE DOES",
    art="gauge", art_caption="VRAM BY CONTEXT",
    header_at="Now the measured curve",
    art_at="Now the measured curve",
    bars=[
        dict(lab="4K",    val="18", unit="GB", pct=52.9,  cls="",    at="Eighteen gigabytes at four K"),
        dict(lab="16K",   val="19", unit="GB", pct=55.9,  cls="",    at="Nineteen at sixteen"),
        dict(lab="64K",   val="22", unit="GB", pct=64.7,  cls="",    at="Twenty-two at sixty-four"),
        dict(lab="128K",  val="26", unit="GB", pct=76.5,  cls="red", at="At one twenty-eight K"),
        dict(lab="256K",  val="34", unit="GB", pct=100.0, cls="red", at="At two fifty-six, thirty-four"),
    ],
    scale=34,
    mark=dict(pct=70.59, lab="24 GB CARD"),
    closing=dict(t="TWO ROWS NEED MORE THAN THE CARD", c="red",
                 at="so neither ran on it"),
    source="measured &middot; hardware-corner.net &middot; qwen3.8 27b &middot; 4k-64k measured on an rtx 3090 &middot; 128k-256k are the requirement, above the card")

# =====================================================================
# W5 -- RAIL. The same growth, paid in time instead of memory.
# =====================================================================
win("rail",
    vo="Prefill is the wait before the first word. Muse Glimmer, "
       "rtx fifty ninety. Four thousand six hundred and "
       "twenty-five tokens a second. Four thousand three hundred and "
       "seventy-three at sixteen. Three thousand six hundred and "
       "six at sixty-four. One thousand eight hundred and seventy-four at two "
       "fifty-six.",
    kicker="KV CACHE &middot; THE WAIT",
    title="THE CARD IS NOT SLOWER, THE PROMPT IS BIGGER",
    art="timer_flat", art_caption="GLIMMER 30B ON THE RTX 5090",
    header_at="Prefill is the wait",
    art_at="Prefill is the wait",
    rails=[
        dict(lab="4K",    val="4,625 T/S", pct=100.0, cls="",    at="four thousand six hundred and twenty-five"),
        dict(lab="16K",   val="4,373 T/S", pct=94.5,  cls="",    at="Four thousand three hundred and seventy-three"),
        dict(lab="64K",   val="3,606 T/S", pct=78.0,  cls="",    at="Three thousand six hundred and six"),
        dict(lab="256K",  val="1,874 T/S", pct=40.5,  cls="red", at="One thousand eight hundred and seventy-four"),
    ],
    closing=dict(t="THE CARD IS NOT SLOWER", c="red",
                 at="at two fifty-six"),
    source="measured &middot; hardware-corner.net &middot; muse glimmer 30b on an rtx 5090 &middot; a separate run, cuda 13")

# =====================================================================
# W6 -- NOTE. The boundary of the number. The channel's signature move.
# =====================================================================
win("note",
    vo="A cache size is still not a memory plan. Which precision the cache is "
       "held in. Whether the runtime keeps the whole thing resident or pages "
       "it out. How much room the weights and the workspace still need. None "
       "of that is in the formula.",
    kicker="KV CACHE &middot; THE BOUNDARY",
    title="A CACHE SIZE IS NOT A MEMORY PLAN",
    art="magnifier", art_caption="THE CACHE",
    header_at="A cache size is still",
    art_at="A cache size is still",
    note_head="THREE THINGS THE FORMULA DOES NOT TELL YOU",
    note_items=[
        dict(t="WHICH PRECISION THE CACHE IS HELD IN",
             at="Which precision the cache is held in"),
        dict(t="WHETHER THE RUNTIME PAGES IT OUT OR KEEPS IT RESIDENT",
             at="keeps the whole thing resident or pages it out"),
        dict(t="HOW MUCH ROOM THE WEIGHTS AND THE WORKSPACE STILL NEED",
             at="the weights and the workspace still need"),
    ],
    tape="THE FORMULA IS A FLOOR, NOT A FIT",
    tape_at="None of that is in the formula",
    source="the boundary of the calculation",
    source_at="None of that is in the formula")

# =====================================================================
# W7 -- ROWS. The method, and the verdict.
# =====================================================================
win("rows",
    vo="So the order matters. Decide the context you will actually send. "
       "Measure the cache at that length, in the precision you will run. Check "
       "what is left after the weights and the workspace. Only then does the "
       "card number mean anything. The context is the input you control.",
    kicker="KV CACHE &middot; THE ORDER",
    title="MEASURE THE CACHE, THEN BUY THE CARD",
    art="checklist", art_caption="THE ORDER",
    header_at="So the order matters",
    art_at="So the order matters",
    rows=[
        dict(rank="01", name="DECIDE", val="THE CONTEXT", sub="YOU WILL REALLY SEND", cls="gold",
             at="Decide the context you will actually send"),
        dict(rank="02", name="MEASURE", val="THE CACHE", sub="AT THAT LENGTH", cls="",
             at="Measure the cache at that length"),
        dict(rank="03", name="CHECK", val="THE HEADROOM", sub="AFTER THE WEIGHTS", cls="",
             at="Check what is left after the weights"),
        dict(rank="04", name="THEN", val="BUY THE CARD", sub="ON THAT NUMBER", cls="gold",
             at="Only then does the card number"),
    ],
    closing=dict(t="THE CONTEXT IS THE INPUT YOU CONTROL", c="gold",
                 at="The context is the input you control"),
    source="the method &middot; measure before you buy")
