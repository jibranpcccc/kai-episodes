# -*- coding: utf-8 -*-
"""
FUSION SPEC — Episode 07 (Prefill), scenes 1-6.

Every visual element carries the phrase it lands on. The builder resolves each
phrase to a REAL spoken word time. If a phrase is not in the script the build
FAILS LOUDLY — there is no silent fallback (EPISODE-RULES.md, bug 3).

Source of every figure:
  Hardware Corner, Muse Glimmer 30B Hardware Requirements and Benchmark Results
  https://www.hardware-corner.net/hardware-for-muse-glimmer-30b-llm/
  Hardware Corner, We Tested Qwen3.8 27B
  https://www.hardware-corner.net/qwen3-8-27b-hardware-tests/
  Ubuntu 24.04, driver 595.58.03, CUDA 12.8, llama.cpp build 153d324bc,
  Flash Attention, full offload. Updated 17 Aug 2026.

On-screen numbers are the TRUNCATED integer of the source value, so the video,
the description and the source table agree digit for digit.
"""

NAME = "BYTE-07-FUSION"

W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


# =====================================================================
# SCENE 1 — HOOK
# =====================================================================
win("hook",
    vo="Okay, so you paste a long document into a local model and nothing happens for "
       "twenty seconds. The model is not broken, and your card is not too slow. You are "
       "watching a number that almost nobody measures, called prefill, and it decides how "
       "the whole thing feels. Token generation is how fast words come out. Prefill is how "
       "long you wait before the first one.",
    lead_in=0.55,
    kicker="PREFILL &middot; THE NUMBER NOBODY MEASURES",
    title="HOW LONG BEFORE THE FIRST WORD",
    sub="one consumer card, one long prompt",
    art="laptop",
    art_caption="THE 20-SECOND WAIT",
    header_at="Okay, so",
    art_at="you paste a long document",
    chips=[
        dict(t="NOTHING HAPPENS FOR 20 SECONDS", c="red",  at="and nothing happens for twenty seconds"),
        dict(t="MODEL IS NOT BROKEN",             c="ghost", at="The model is not broken"),
        dict(t="CARD IS NOT TOO SLOW",            c="ghost", at="and your card is not too slow"),
        dict(t="A NUMBER NOBODY MEASURES",        c="gold", at="a number that almost nobody measures"),
        dict(t="GENERATION = HOW FAST WORDS COME OUT", c="cyan", at="Token generation is how fast words come out"),
        dict(t="PREFILL = HOW LONG YOU WAIT",    c="gold", at="Prefill is how long you wait"),
    ],
    stats=[
        dict(v="4,625", u="T/S", lab="PREFILL &middot; SHORT PROMPT", c="gold", at="called prefill"),
        dict(v="461",   u="T/S", lab="PREFILL &middot; 128K",       c="red",  at="it decides how the whole thing feels"),
    ],
    tape="THE WAIT IS THE PRODUCT",
    tape_at="before the first one")

# =====================================================================
# SCENE 2 — THE SHAPE OF THE CURVE (Glimmer, RTX 5090)
# =====================================================================
win("bars",
    vo="On a five-oh-ninety, Muse Glimmer processes a four K prompt at four thousand six "
       "hundred and twenty-five tokens a second. At sixteen K it is four thousand three "
       "hundred and seventy-three. At sixty-four K it is three thousand six hundred and six. "
       "At one twenty-eight K, two thousand eight hundred and six. At two hundred fifty-six K, "
       "one thousand eight hundred and seventy-four. Long context costs you, but it degrades "
       "gracefully.",
    kicker="RTX 5090 &middot; PROMPT PROCESSING",
    title="MUSE GLIMMER 30B",
    sub="prompt processing, tokens per second",
    art="gpu",
    art_caption="RTX 5090 &middot; 32 GB",
    header_at="On a five-oh-ninety",
    art_at="Muse Glimmer processes",
    bars=[
        dict(lab="4K",    val="4,625", pct=100.0,  cls="",    unit="T/S", at="four thousand six hundred and twenty-five"),
        dict(lab="16K",   val="4,373", pct=94.51,  cls="",    unit="T/S", at="At sixteen K it is four thousand three hundred"),
        dict(lab="64K",   val="3,606", pct=77.97,  cls="",    unit="T/S", at="At sixty-four K it is three thousand six hundred"),
        dict(lab="128K",  val="2,806", pct=60.68,  cls="",    unit="T/S", at="At one twenty-eight K, two thousand eight hundred"),
        dict(lab="256K",  val="1,874", pct=40.52,  cls="red", unit="T/S", at="At two hundred fifty-six K, one thousand eight hundred"),
    ],
    mid=dict(t="LONG CONTEXT COSTS YOU", c="gold", at="Long context costs you"),
    closing=dict(t="DEGRADES GRACEFULLY", c="cyan", at="it degrades gracefully"),
    source="prompt processing (t/s), truncated &middot; hardware-corner.net &middot; llama.cpp 153d324bc")

# =====================================================================
# SCENE 3 — THE SAME CARD, A DIFFERENT MODEL (Qwen 3.8)
# =====================================================================
win("rows",
    vo="The same card running Qwen three point eight starts at three thousand seven hundred "
       "and forty-nine at four K. At sixteen K it is eighteen hundred and twenty-five. At "
       "sixty-four K it is seven hundred and seventeen. And at one twenty-eight K it is four "
       "hundred and sixty-one tokens a second. That is the number that makes a long context "
       "chat feel broken.",
    kicker="SAME CARD &middot; DIFFERENT MODEL",
    title="QWEN 3.8 27B",
    sub="prompt processing, tokens per second",
    art="collapse",
    art_caption="PREfill COLLAPSE",
    header_at="The same card running Qwen",
    art_at="starts at three thousand seven hundred",
    rows=[
        dict(rank="01", name="4K",   val="3,749", sub="100% of peak", cls="gold", at="at four K"),
        dict(rank="02", name="16K",  val="1,825", sub="49% of peak",  cls="",    at="At sixteen K it is eighteen hundred and twenty-five"),
        dict(rank="03", name="64K",  val="717",   sub="19% of peak",  cls="red", at="At sixty-four K it is seven hundred and seventeen"),
        dict(rank="04", name="128K", val="461",   sub="12% of peak",  cls="red", at="And at one twenty-eight K"),
    ],
    closing=dict(t="THIS IS WHAT BROKEN FEELS LIKE", c="red", at="That is the number that"),
    source="prompt processing (t/s), truncated &middot; hardware-corner.net &middot; llama.cpp 153d324bc")

# =====================================================================
# SCENE 4 — WHAT IT MEANS IN SECONDS
# =====================================================================
win("rail",
    vo="Turn it into time. A hundred thousand token prompt at forty-six hundred tokens a "
       "second is twenty-two seconds. At eighteen hundred and seventy-four tokens a second it "
       "is fifty-three seconds. And at four hundred and sixty-one tokens a second it is three "
       "minutes and thirty-seven seconds, before the model writes a single word. That is the "
       "whole difference between an assistant and a loading screen.",
    kicker="ONE HUNDRED THOUSAND TOKEN PROMPT",
    title="SAME DOCUMENT, THREE WAITS",
    sub="time before the first word",
    art="clock",
    art_caption="TIME TO FIRST TOKEN",
    header_at="Turn it into time",
    art_at="A hundred thousand token prompt",
    rails=[
        dict(lab="AT 4,625 T/S", val="22 s",  pct=10.1,  cls="",    at="is twenty-two seconds"),
        dict(lab="AT 1,874 T/S", val="53 s",  pct=24.4,  cls="",    at="it is fifty-three seconds"),
        dict(lab="AT 461 T/S",   val="217 s", pct=100.0, cls="red", at="three minutes and thirty-seven seconds"),
    ],
    closing=dict(t="BEFORE THE FIRST WORD", c="red", at="before the model writes a single word"),
    source="100,000 tokens &divide; prompt processing rate &middot; rounded to the second")

# =====================================================================
# SCENE 5 — WHY PREFILL COLLAPSES
# =====================================================================
win("chain",
    vo="Prefill is one big matrix multiplication over the whole prompt, so it scales with "
       "prompt length and it is memory bandwidth bound. The longer the prompt, the more "
       "attention you must compute before the first token. Generation, by contrast, is one "
       "token at a time and barely cares how long the prompt was.",
    kicker="THE MECHANISM",
    title="WHY PREFILL COLLAPSES",
    sub="and why generation does not",
    art="meter",
    art_caption="MEMORY BANDWIDTH",
    header_at="Prefill is one big matrix multiplication",
    art_at="The longer the prompt",
    chain=[
        dict(t="PROMPT",    s="100K tokens",   at="over the whole prompt"),
        dict(t="ONE PASS",  s="every weight",   at="scales with prompt length"),
        dict(t="BANDWIDTH", s="the hard limit", at="it is memory bandwidth bound"),
        dict(t="WAIT",      s="before word one", at="before the first token"),
    ],
    compare=[
        dict(title="PREFILL", body="One pass over the <b>whole prompt</b>. Cost scales with "
                                   "prompt length. <b>Bandwidth bound.</b>", cls="hot", at="the more attention you must compute"),
        dict(title="GENERATION", body="One token at a time. <b>Barely cares</b> how long the "
                                      "prompt was.", cls="good", at="Generation, by contrast"),
    ],
    source="mechanism, not a measurement &middot; llama.cpp prompt processing is bandwidth bound")

# =====================================================================
# SCENE 6 — THE CAVEAT
# =====================================================================
win("note",
    vo="Two notes. These are single GPU measurements with full offload, so a machine that "
       "splits a model across cards will see different prefill behaviour. And a cached prompt "
       "is nearly free on the second run, so the wait you feel is usually the first time only.",
    kicker="BEFORE YOU BUY ANYTHING",
    title="TWO HONEST NOTES",
    sub="what these numbers do not cover",
    art="caveat",
    art_caption="READ THE FINE PRINT",
    header_at="Two notes",
    art_at="These are single GPU measurements",
    note_head="WHAT THIS TEST DOES NOT COVER",
    note_items=[
        dict(t="SINGLE GPU, FULL OFFLOAD ONLY",
             at="with full offload"),
        dict(t="A MODEL SPLIT ACROSS CARDS BEHAVES DIFFERENTLY",
             at="splits a model across cards will see different prefill behaviour"),
        dict(t="A CACHED PROMPT IS NEARLY FREE ON THE SECOND RUN",
             at="nearly free on the second run"),
    ],
    source="single GPU, full offload &middot; llama.cpp 153d324bc",
    source_at="And a cached prompt is",
    tape="FIRST TIME ONLY",
    tape_at="usually the first time only")
