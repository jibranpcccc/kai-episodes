# -*- coding: utf-8 -*-
"""
EPISODE 09 -- THE SHARED PLAN
=============================
Every agent that writes a section of this episode reads this file and nothing
else about the channel. It carries the voice, the layout and art assignment,
the numbers, and the code contract.

  BYTE FORENSICS -- EPISODE 09
  "WHY A LONGER CONTEXT COSTS YOU MORE MEMORY"
  the cache is a second bill

WINDOW MAP (38 windows, matching BYTE-LORA's length)
-----------------------------------------------------
  #   act  layout    art key            subject
  1   1    hook      kv_cache          the conversation outlives the card
  2   1    chain     cache_grid        every token adds two vectors
  3   1    rows      chip              the arithmetic: 288 MiB
  4   1    bars      gauge             measured VRAM by context
  5   1    rail      timer_flat        prefill rate by context
  6   1    note      magnifier         a cache size is not a memory plan
  7   1    rows      checklist        measure the cache, then buy the card
  8   2    gallery   cache_grid        three different things called memory
  9   2    note      caveat            the cache is not the file
  10  2    rows      vram_module       what is inside the cache
  11  2    chain     pipeline          prefill writes it, decode reads it
  12  2    strip     token_blocks      the three states a cache is in
                              context_window
                              collapse
  13  2    rows      context_window    how a runtime stores it
  14  2    bars      memory_bank       cache size across model sizes
  15  2    nodes     pipeline          the cost of the next token
  16  2    hook      prompt_stream     the second bill
  17  3    rows      motherboard      the rig, exactly
  18  3    bars      gauge             the full VRAM curve
  19  3    note      caveat            the curve is not linear
  20  3    rows      scales            where the knee is
  21  3    bars      gpu               two models, one card
  22  3    strip     vram_module       what each card size holds
                              sodimm
                              ram_stick
  23  3    rail      clock             time to first token
  24  3    note      clock             what a throughput number hides
  25  3    title     token_blocks      ACT BREAK: the part people quote wrong
  26  4    rows      gguf_blocks       quantising the cache
  27  4    bars      scales            fp16 against q8_0 against q4_0
  28  4    note      caveat            quantisation changes what you read back
  29  4    rows      chip              the workspace and the activations
  30  4    chain     pipeline          what stays live during a forward pass
  31  4    bars      gpu               batch size against memory
  32  4    note      collapse          offload, page and spill
  33  4    nodes     memory_bank       what actually moves the number
  34  5    rows      checklist         the checklist
  35  5    nodes     pipeline          the order of operations
  36  5    bars      vram_module       what each card size holds
  37  5    hook      question          the behaviour you want
  38  5    note      caveat            the verdict

  No two consecutive windows share a layout. Windows 1-7 are already written
  in data/spec_ep09_kv.py -- do not rewrite them.

THE VOICE
---------
Declarative. Evidence first. Deliberately hedged. The channel's signature move
is the refusal to over-claim, voiced as a recurring pair of sentences that
bookend a window.

  "A cache size is still not a memory plan."
  "Frozen weights are not permission to delete the learning process."

Rules:
  * Every number on screen is a number the script says out loud, in words.
    Screen shows digits, the voice says the number.
  * Never claim a fit. Ever. Say "measured", "derived", "not a fit claim".
  * Non-jargon metaphors: the bill, the recipe, the line, the floor, the knee.
  * Sentences are short declaratives, then a longer clause-chained one.
  * Lower-case sentence openers are occasionally used: "the cache is a second
    bill", "the only number that is free".
  * No hype. No "amazing", "insane", "game-changing". The channel's register
    is a careful engineer reading a measurement out loud.

THE SPINE
---------
  Act 1  the paradox        (1-7)    the conversation outlives the card
  Act 2  what it is         (8-16)   the cache is not the file
  Act 3  what was measured  (17-25)  the curve, honestly
  Act 4  what changes it    (26-33)  precision, workspace, batch, offload
  Act 5  what you can do    (34-38)  measure, then buy

THE NUMBER BANK -- use these, cite them, do not invent others
-------------------------------------------------------------
MEASURED -- hardware-corner.net, We Tested Qwen3.8 27B
           https://www.hardware-corner.net/qwen3-8-27b-hardware-tests/
MEASURED -- hardware-corner.net, Muse Glimmer 30B Hardware Requirements and
           Benchmark Results
           https://www.hardware-corner.net/hardware-for-muse-glimmer-30b-llm/
RIG for both: Ubuntu 24.04, driver 595.58.03, CUDA 12.8, llama.cpp build
     153d324bc, Flash Attention, full offload. Updated 17 Aug 2026.

  Qwen 3.8 27B, VRAM in use, one 24 GB card, full offload:
      4K = 18 GB      16K = 19 GB     32K = 20 GB
     64K = 22 GB     128K = 26 GB    256K = 34 GB  (does not fit on 24 GB)
  Muse Glimmer 30B, prompt processing rate (t/s):
      4K = 4,625      16K = 4,373      64K = 3,606
    128K = 2,806     256K = 1,874
  Qwen 3.8 27B, prompt processing rate (t/s):
      4K prompt = 3,749      128K prompt = 461
  Muse Glimmer 30B vs Qwen 3.8 27B, VRAM by context, same 24 GB card:
      4K   = 16 GB vs 18 GB      32K  = 16 GB vs 20 GB
     64K   = 17 GB vs 22 GB     256K  = 20 GB vs 34 GB
  Generation throughput (t/s) on a 5090, Qwen 3.8 27B:
      4K = 74.8   16K = 52.2   32K = 38.0   128K = 22.8
  Generation throughput (t/s) on a 3090, Qwen 3.8 27B:
      4K = 40.3   32K = 37.0   64K = 33.9
  Two 16 GB cards vs one 24 GB card, generation (t/s):
      2 cards 4K = 22.5   2 cards 128K = 15.6   1 card 128K = 38.1
  Time to first token, 100K prompt:
      at 4,625 t/s = 22 s        at 767 t/s = 131 s

DERIVED -- Qwen2.5 3B Instruct config: 36 layers, 2 KV heads, head dim 128.
  cache bytes = layers x 2 (K,V) x kv_heads x head_dim x bytes_per_value x tokens
      8,192 tokens, fp16 (2 B) = 288 MiB = 0.302 GB
      8,192 tokens, Q8_0 (34 B per 32 values) = 153 MiB
  25,067,520 params at rank 16 on seven projections (the LoRA episode's number)
      25,067,520 x 16 B = 382.5 MiB

DERIVED -- general cache sizing:
  cache scales LINEARLY with token count
  cache scales LINEARLY with layer count
  cache scales LINEARLY with head_dim
  cache scales with kv_heads (GQA shares them)

  If any figure is not in this bank, derive it from the bank and say so on the
  source line with the word "derived". Do not state an unverified figure as
  measured, and do not quote a paper without naming it in the source line.

THE CODE CONTRACT
-----------------
Each section is a module data/ep09_sN.py that looks exactly like this:

    # -*- coding: utf-8 -*-
    W = []

    def win(layout, vo, **data):
        W.append(dict(layout=layout, vo=vo, **data))

    win("rows",
        vo="The narration for this window, spoken out loud in words.",
        kicker="KV CACHE &middot; THE ARITHMETIC",
        title="THE HEADLINE, ALL CAPS",
        art="chip", art_caption="ONE MODEL, ONE FORMULA",
        header_at="a phrase that is in this vo, word for word",
        art_at="another phrase that is in this vo",
        rows=[
            dict(rank="01", name="LAYERS", val="36", sub="BLOCKS", cls="gold",
                 at="thirty-six layers"),
        ],
        closing=dict(t="A CLOSING CHIP", c="gold", at="a phrase in this vo"),
        source="derived &middot; qwen2.5 3b instruct &middot; 36 layers")

  The anchor rules -- these are enforced by the builder and they WILL fail the
  build if broken:
    * every `at` must be an exact substring of that window's own `vo`
      (case-insensitive). An anchor that is not in the script raises.
    * elements must be listed in the order the script says them, because the
      builder sorts arrivals by word time and the DOM order is the visual
      order. If the script says A then B, list A then B.
    * a phrase used as an anchor must be UNIQUE enough in the vo to resolve
      to the right word. If it appears twice, quote more of it.
    * do NOT reuse a phrase that is a substring of the window's `header_at`.
      That is what pushed two BYTE-LORA reveals 1.77 s late.

  Layout field reference:
    hook      kicker title art art_caption header_at art_at
              chips[]  = {t, c(gold|red|cyan|ghost), at}
              stats[]  = {v, u, lab, c(gold|red|cyan), at}
              tape     tape_at
              source   (optional) source_at (optional)
    rows      kicker title art art_caption header_at art_at
              rows[]   = {rank, name, val, sub, cls(gold|red|""), at}
              closing  = {t, c, at}      source
    bars      kicker title art art_caption header_at art_at
              bars[]   = {lab, val, unit, pct, cls(""|red), at}
              closing  = {t, c, at}      mid  source
              `unit` is printed next to the value. NEVER leave it off and
              NEVER invent one. If the value has no unit, say nothing.
              `pct` is the bar fill as a percentage. Make it proportional to
              the value so the bar length always means the number.
    rail      kicker title art art_caption header_at art_at
              rails[]  = {lab, val("NUMBER UNIT"), pct, cls(""|red), at}
              closing  = {t, c, at}      source
    chain     kicker title art art_caption header_at art_at
              chain[]  = {t, s, at}
              compare[]= {cls(hot|good), title, body, at}
              source   (REQUIRED for chain)
    note      kicker title art art_caption header_at art_at
              note_head
              note_items[] = {t, at}
              tape     tape_at   source   source_at
    gallery   kicker title art art_caption header_at art_at
              name     blurb    meta
              name_at  blurb_at meta_at
              side ("left" flips the art to the other side)
    strip     kicker title header_at
              items[]  = {key(art key), label, at}
    title     kicker title sub art head_at
    nodes     kicker title header_at art art_at
              chain[]  = {t, s, at}

  `cls` on rows: "" (default), "gold" (highlights + adds row--mark),
  "red" (warning). On bars/rail: "" or "red".

THE WINDOW BUDGET
-----------------
  * 26 to 52 words of narration per window (a window is 10-19 seconds)
  * NO window over 19 seconds
  * every window closes on a beat, so no window ends on a frozen screen
  * the last element in a window must land within the last ~2 seconds of it
"""
