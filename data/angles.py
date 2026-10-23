# -*- coding: utf-8 -*-
"""The angle catalogue. One entry is one episode.

Byte Forensics: local AI hardware, one measured argument per episode.
Every entry is a distinct thesis that can be defended from the fact base
(vram, prefill, generation, capacity, latency, cache, lora, papers, quant).
"""
W = []


def angle(aid, thesis, subject, shape, facts, caveat, title):
    W.append(dict(id=aid, thesis=thesis, subject=subject, shape=shape,
                  facts=facts, caveat=caveat, title=title))


# ---------------------------------------------------------------------------
# VRAM / CAPACITY / FIT  (20)
# ---------------------------------------------------------------------------

angle("VRAM-001",
      "A model fits or does not fit before it runs fast, so fit is a binary event with no middle state.",
      "the fit/no-fit boundary",
      "MEASUREMENT",
      ["vram", "capacity"],
      "A model that fits can still be too slow to use; this episode says nothing about tokens per second.",
      "FIT IS A SWITCH, NOT A DIAL")

angle("VRAM-002",
      "The usable VRAM of a card is less than its nameplate capacity by an amount you have to pay for.",
      "nameplate versus usable memory",
      "MEASUREMENT",
      ["vram", "capacity"],
      "The gap is driver and runtime dependent, so the measured figure is for one stack on one card.",
      "THE MEMORY YOU NEVER GET")

angle("VRAM-003",
      "Weights alone fit a card with room to spare and the model still dies, because runtime overhead is charged against the same budget.",
      "weights versus working memory",
      "MEASUREMENT",
      ["vram", "capacity", "cache"],
      "Overhead scales with implementation choices, so one number does not transfer to every runtime.",
      "WEIGHTS FIT. IT STILL CRASHED.")

angle("VRAM-004",
      "The distance between a card's capacity and a model's requirement predicts a spill to disk, and a spill costs far more than the missing gigabytes suggest.",
      "the gap between fit and spill",
      "PARADOX",
      ["vram", "capacity", "generation"],
      "The spill penalty depends on how much of the working set stays resident during a token.",
      "THE MISSING GIGABYTES COST HOURS")

angle("VRAM-005",
      "Adding memory to a machine is worth more than adding a faster card when the workload is the wrong size for the card.",
      "more system memory versus more GPU",
      "COMPARISON",
      ["vram", "capacity", "generation"],
      "Only one configuration was measured; a workload that already fits may reverse the ordering.",
      "MORE RAM BEAT A FASTER CARD")

angle("VRAM-006",
      "Unified memory laptops beat discrete cards on large models because the limit is capacity, not throughput.",
      "Mac-style unified memory against a discrete card",
      "COMPARISON",
      ["vram", "capacity", "generation"],
      "One Apple generation against one NVIDIA generation; memory bandwidth and thermals differ too.",
      "THE LAPTOP WON ON SIZE ALONE")

angle("VRAM-007",
      "A model too large for any single card can be split across two cards with almost no speed penalty, because the split is on layers and the interconnect is fast enough.",
      "splitting a model across two cards",
      "MEASUREMENT",
      ["vram", "capacity", "generation"],
      "This holds only when both cards are the same model and the split is layer-wise, not when each card holds a copy.",
      "TWO CARDS, ONE MODEL, NO WAIT")

angle("VRAM-008",
      "The size of the longest context you can hold scales with the size of the smallest unit you can shrink, so quantizing weights buys context headroom before it buys speed.",
      "weight quantization as context capacity",
      "MATH",
      ["vram", "quant", "cache"],
      "This derives from cache size arithmetic; it says nothing about output quality after quantization.",
      "SHRINK THE WEIGHTS, BUY THE CONTEXT")

angle("VRAM-009",
      "Two models that need the same amount of memory can have wildly different speeds because memory bandwidth is spent on different things.",
      "why equal-fit models do not perform equally",
      "PARADOX",
      ["vram", "generation", "quant"],
      "Bandwidth attribution was inferred from timing, not measured on the bus directly.",
      "SAME MEMORY, DIFFERENT SPEED")

angle("VRAM-010",
      "The card you can afford is the wrong card if your model sits within a gigabyte of the limit, because the card that matters is the one with the memory headroom.",
      "buying against a tight fit",
      "DECISION",
      ["vram", "capacity", "latency"],
      "A second model or a smaller quant would change the purchasing conclusion.",
      "BUY THE HEADROOM, NOT THE FPS")

angle("VRAM-011",
      "Freeing system RAM to make room for a model on a card without dedicated VRAM works, and the cost shows up as latency before it shows up as failure.",
      "shared memory on cards without enough VRAM",
      "MEASUREMENT",
      ["vram", "capacity", "latency"],
      "Tested on one consumer card with one model; dedicated-memory cards behave differently.",
      "SHARED MEMORY IS SLOW MEMORY")

angle("VRAM-012",
      "A model's memory footprint can be reduced by nearly half without touching the weights at all, by shrinking what the runtime keeps resident.",
      "runtime buffers as the first lever",
      "MECHANISM",
      ["vram", "cache", "capacity"],
      "The reduction depends on which runtime features were enabled during the measurement.",
      "THE MEMORY YOU CAN DELETE")

angle("VRAM-013",
      "Running two models at once halves the memory each one gets, so concurrency on one card is a memory decision before it is a scheduling decision.",
      "two concurrent models on one card",
      "MEASUREMENT",
      ["vram", "capacity", "latency"],
      "Both models were small; two large models spill rather than halve cleanly.",
      "TWO MODELS, ONE CARD, HALF EACH")

angle("VRAM-014",
      "The card with the most memory is not the card with the fastest tokens, and the ranking flips depending on which model you load.",
      "capacity ranking versus speed ranking",
      "COMPARISON",
      ["vram", "capacity", "generation"],
      "Only two cards and two model sizes were compared, so the crossover point is indicative.",
      "BIGGEST CARD IS NOT FASTEST CARD")

angle("VRAM-015",
      "Offloading a small fraction of layers to system RAM can cost more throughput than the whole model is worth, which makes partial offload the worst of both worlds.",
      "partial CPU offload of layers",
      "FAILURE",
      ["vram", "generation", "capacity"],
      "One offload ratio was tested; a smaller fraction may cross a different threshold.",
      "PARTIAL OFFLOAD LOSES BOTH WINS")

angle("VRAM-016",
      "You can shrink the model's memory footprint by changing the context you ask for, which makes context size a hardware variable.",
      "context length as a memory lever",
      "MECHANISM",
      ["vram", "cache", "capacity"],
      "This concerns prefill and generation memory, not attention quality at long range.",
      "ASK FOR LESS, FIT MORE")

angle("VRAM-017",
      "A model that just barely fits leaves no room for the runtime, so the practically useful memory is lower than the theoretical fit point.",
      "the practical fit ceiling",
      "MEASUREMENT",
      ["vram", "capacity", "cache"],
      "The overhead margin was estimated from one runtime; another runtime may differ.",
      "THE FIT POINT IS LOWER THAN IT LOOKS")

angle("VRAM-018",
      "Memory bandwidth, not capacity, is the ceiling on prompt processing speed, so a bigger memory bus speeds up prefill without changing what fits.",
      "bandwidth versus capacity in prefill",
      "MECHANISM",
      ["vram", "prefill", "capacity"],
      "Bus width was compared across two cards of different generations; clock speeds also differ.",
      "BANDWIDTH DRIVES PROMPT SPEED")

angle("VRAM-019",
      "The memory you lose to fragmentation is large enough to change whether a model runs at all, and it grows with the number of separate allocations.",
      "fragmentation as a silent memory cost",
      "FAILURE",
      ["vram", "capacity", "cache"],
      "Fragmentation was measured in one process with one allocator configuration.",
      "THE MEMORY THAT VANISHES")

angle("VRAM-020",
      "A model's size on disk and its size in memory are different numbers, and only the second one decides whether it runs on your card.",
      "disk footprint versus resident footprint",
      "MYTH",
      ["vram", "capacity", "quant"],
      "This separates the two footprints; it does not explain why the on-disk number is so often quoted.",
      "DISK SIZE IS NOT MEMORY SIZE")

# ---------------------------------------------------------------------------
# PREFILL / LATENCY / TIME TO FIRST TOKEN  (15)
# ---------------------------------------------------------------------------

angle("PF-001",
      "Time to first token grows with prompt length roughly linearly, which makes long prompts a latency decision rather than a typing decision.",
      "prompt length versus time to first token",
      "MEASUREMENT",
      ["prefill", "latency"],
      "One context shape was tested; structured prompts with many short chunks behave differently.",
      "LONGER PROMPT, LONGER WAIT")

angle("PF-002",
      "Time to first token is dominated by the prompt being read into the card, not by the model being slow, so a fast card with slow memory still waits.",
      "what the wait before the first word actually is",
      "MECHANISM",
      ["prefill", "latency", "vram"],
      "The split was inferred from timing rather than instrumented at the kernel level.",
      "THE WAIT IS THE PROMPT, NOT THE MODEL")

angle("PF-003",
      "The first token is fast and the rest are slow, because the prompt is computed in parallel while the answer is generated one token at a time.",
      "prefill parallelism versus decode serialization",
      "MECHANISM",
      ["prefill", "generation", "latency"],
      "This describes the shape of the latency curve, not its exact crossover point.",
      "ONE BIG STEP, THEN SMALL STEPS")

angle("PF-004",
      "Doubling the prompt roughly doubles the wait for the first token, which makes long-context features expensive at the front door of every request.",
      "prompt length scaling for prefill",
      "MATH",
      ["prefill", "latency"],
      "Scaling was measured up to one context length; beyond it, attention cost rises faster.",
      "THE WAIT SCALES WITH WHAT YOU SENT")

angle("PF-005",
      "Time to first token falls when the weights are quantized because less data has to be read, so the win is at the start and disappears during generation.",
      "quantization effect on prefill versus decode",
      "MEASUREMENT",
      ["quant", "prefill", "generation"],
      "Measured on one quantization format and one card; kernel support differs elsewhere.",
      "QUANTIZATION BUYS YOU THE FIRST WORD")

angle("PF-006",
      "A long system prompt is re-read on every request, so a cached system prompt can be worth more than a smarter prompt.",
      "repeated prompt cost",
      "DECISION",
      ["prefill", "latency", "cache"],
      "Prefix caching was tested with one repeated prefix; a changing prefix removes the saving.",
      "YOUR SYSTEM PROMPT IS A RECURRING COST")

angle("PF-007",
      "The perceived responsiveness of a model is set by the first token, so shaving prefill changes the experience more than doubling generation speed does.",
      "perceived speed versus measured speed",
      "MYTH",
      ["prefill", "latency", "generation"],
      "This concerns human perception in one chat interface; batch throughput users will disagree.",
      "PERCEIVED SPEED LIVES IN THE PREMILL")

angle("PF-008",
      "A slow prompt processing step can hide behind a fast generation speed, which is why end-to-end time is the only honest latency number.",
      "end-to-end versus component timing",
      "PARADOX",
      ["prefill", "generation", "latency"],
      "Only one model and card pair were profiled end to end.",
      "THE ONLY HONEST LATENCY IS TOTAL TIME")

angle("PF-009",
      "Batch size trades the first token for throughput, and the crossover sits much earlier than the maximum batch size does.",
      "batching and time to first token",
      "MEASUREMENT",
      ["prefill", "generation", "latency"],
      "The crossover was measured for one workload mix; longer outputs move it.",
      "BATCHING BUYS SPEED, NOT PATIENCE")

angle("PF-010",
      "The wait for the first token is short enough to hide only if the prompt is short, so prefill is the difference between a snappy tool and a slow one.",
      "interactive latency thresholds",
      "DECISION",
      ["prefill", "latency"],
      "Thresholds are taste as much as measurement; one interface was used.",
      "PROMPT LENGTH DECIDES IF IT FEELS FAST")

angle("PF-011",
      "Disk residency at model load makes startup slow, but it does not affect the wait for the first token once the model is resident.",
      "load time versus inference latency",
      "COMPARISON",
      ["latency", "vram", "prefill"],
      "Startup and steady state were measured separately with a warm cache.",
      "STARTUP IS SLOW. INFERENCE ISN'T.")

angle("PF-012",
      "The same model gives different first-token waits on different cards, so the card choice is a latency choice before it is a capacity choice.",
      "first-token latency across cards",
      "COMPARISON",
      ["prefill", "latency", "vram"],
      "Two cards only; driver versions were not controlled.",
      "FIRST TOKEN TELLS YOU WHICH CARD")

angle("PF-013",
      "Trimming a prompt to its essential sentences cuts the wait more than any hardware change available to most people.",
      "prompt trimming as the cheapest speedup",
      "DECISION",
      ["prefill", "latency", "generation"],
      "Quality loss from trimming was not scored in this episode.",
      "CUT THE PROMPT BEFORE BUYING THE CARD")

angle("PF-014",
      "Prefill time is spent reading weights as well as processing tokens, so a larger model can have a slower first token even on a faster card.",
      "weight reads inside prefill",
      "MECHANISM",
      ["prefill", "vram", "generation"],
      "Weight read and token work were not separated with hardware counters.",
      "THE FIRST TOKEN PAYS FOR THE WEIGHTS")

angle("PF-015",
      "A long context that is never used still costs a full prefill, so history you do not need is billed every time you press enter.",
      "cost of irrelevant context",
      "MATH",
      ["prefill", "cache", "latency"],
      "This is an arithmetic argument about token counts; it ignores any benefit of the history.",
      "UNUSED HISTORY STILL COSTS YOU")

# ---------------------------------------------------------------------------
# GENERATION THROUGHPUT  (12)
# ---------------------------------------------------------------------------

angle("GEN-001",
      "Tokens per second is a function of model size and memory bandwidth, and card marketing numbers describe neither of those.",
      "throughput from size and bandwidth",
      "MECHANISM",
      ["generation", "vram"],
      "The relation was fitted on one family of models; newer architectures deviate.",
      "TOKENS PER SECOND IS NOT A CARD NUMBER")

angle("GEN-002",
      "A model that fits entirely in memory generates faster than the same model split across system RAM, because the disk path dominates every token.",
      "resident versus spilled generation speed",
      "MEASUREMENT",
      ["generation", "vram", "capacity"],
      "Compared one split configuration; partial residency falls between the two.",
      "SPILLING MAKES EVERY TOKEN SLOW")

angle("GEN-003",
      "Halving the weight precision does not halve the tokens per second, so quantization is bought for fit and for reach, not for a two-times speed-up.",
      "quantization speed-up is sublinear",
      "PARADOX",
      ["quant", "generation"],
      "One quantization family was tested; some formats and kernels do scale better.",
      "HALVING BITS DID NOT HALVE THE WAIT")

angle("GEN-004",
      "The largest model on a card is not the fastest model on that card, and the fastest one is often small enough that the big card is wasted.",
      "model size versus throughput on one card",
      "COMPARISON",
      ["generation", "vram", "capacity"],
      "Three model sizes on one card; a different card would reorder them.",
      "THE BIGGEST MODEL IS THE SLOWEST")

angle("GEN-005",
      "Throughput measured with one long prompt is not the throughput you get in a conversation, because batching changes the arithmetic.",
      "single-stream versus batched throughput",
      "PARADOX",
      ["generation", "prefill", "latency"],
      "Batch composition was uniform; mixed-length batches behave differently.",
      "THE BENCHMARK AND THE CHAT DISAGREE")

angle("GEN-006",
      "Generation speed is set by the memory read per token, which means the number of layers you run off the CPU divides your speed.",
      "cost of a layer offload per token",
      "MATH",
      ["generation", "vram", "capacity"],
      "The linear model assumes layers offload cleanly; runtime behavior differs.",
      "EVERY OFFLOADED LAYER DIVIDES THE SPEED")

angle("GEN-007",
      "You can get a faster answer by asking for fewer tokens, and the relationship is close enough to arithmetic to plan around.",
      "output length versus time to complete",
      "MATH",
      ["generation", "latency"],
      "Assumes a steady token rate after the first token; longer contexts add cache reads.",
      "FEWER TOKENS IS A FASTER ANSWER")

angle("GEN-008",
      "Two cards of the same generation produce nearly the same token rate, so generation speed scales with what each card can do, not with how many you have.",
      "single-card rate versus card count",
      "COMPARISON",
      ["generation", "vram"],
      "Two identical cards measured; mixed or older cards are not covered.",
      "TWO IDENTICAL CARDS, SAME RATE EACH")

angle("GEN-009",
      "The tokens per second figure that feels fast is not the one that matters when you are paying per token, because price and speed scale independently.",
      "speed versus price per token",
      "COST",
      ["generation", "capacity", "vram"],
      "Pricing snapshots change; the episode should date its figures.",
      "FAST DOES NOT MEAN CHEAP")

angle("GEN-010",
      "Throughput collapses at long context because every generated token pays for reading a large cache, which makes the cost of context a tax on output.",
      "context length penalty on generation",
      "MECHANISM",
      ["generation", "cache", "latency"],
      "Measured with one cache implementation; quantized caches behave differently.",
      "LONG CONTEXT TAXES EVERY TOKEN")

angle("GEN-011",
      "Running a model on a machine where the OS also needs memory produces slower tokens than the card's rating, because the card is not getting the whole machine.",
      "host contention on generation speed",
      "FAILURE",
      ["generation", "vram", "capacity"],
      "The background workload was one desktop session; heavier contention would be worse.",
      "YOUR BROWSER IS STEALING TOKENS")

angle("GEN-012",
      "The fastest configuration for one user is not the fastest configuration for ten, because throughput scales with the machine rather than with the queue.",
      "single-user speed versus multi-user throughput",
      "DECISION",
      ["generation", "latency", "capacity"],
      "Ten concurrent streams were simulated on one card; separate cards change the answer.",
      "ONE USER'S FAST IS TEN USERS' QUEUE")

# ---------------------------------------------------------------------------
# KV CACHE / CONTEXT LENGTH  (15)
# ---------------------------------------------------------------------------

angle("KV-001",
      "The KV cache is the second memory bill, because prompt processing may be free in memory and the cache is charged for every token kept.",
      "the KV cache as a second memory consumer",
      "MECHANISM",
      ["cache", "vram", "capacity"],
      "One model family was profiled; cache size depends on architecture.",
      "THE CACHE IS THE SECOND BILL")

angle("KV-002",
      "Cache memory scales with the number of layers as well as the context, so a model with fewer layers holds a smaller cache for the same context.",
      "cache size versus layer count",
      "MATH",
      ["cache", "vram"],
      "The scaling ignores any architecture that shares or compresses cache.",
      "CACHE SIZE GROWS WITH DEPTH")

angle("KV-003",
      "Doubling the context roughly doubles the cache, which is why a long-context feature costs memory twice: once for the prompt and once for the cache.",
      "context doubling and cache growth",
      "MATH",
      ["cache", "vram", "capacity"],
      "Measured to the model's maximum context; beyond it, behavior changes.",
      "LONGER CONTEXT, DOUBLE THE MEMORY")

angle("KV-004",
      "Quantizing the cache frees enough memory to double the usable context, which makes cache quantization the cheapest context extension available.",
      "quantized cache versus longer context",
      "COMPARISON",
      ["quant", "cache", "vram"],
      "Quality impact of quantized cache was not evaluated in this episode.",
      "QUANTIZE THE CACHE, DOUBLE THE WINDOW")

angle("KV-005",
      "A 32k context does not mean you can keep 32k tokens of conversation, because the cache grows while the prompt is still being processed.",
      "context limit versus realistic working set",
      "MYTH",
      ["cache", "capacity", "prefill"],
      "The working-set claim is arithmetic; it does not test how much cache the runtime reserves.",
      "THE WINDOW IS NOT THE WORKING SET")

angle("KV-006",
      "Once the cache fills the card, generation stops being compute-bound and becomes memory-bound, so the speed penalty appears at a context threshold.",
      "the cache-full threshold",
      "MEASUREMENT",
      ["cache", "generation", "vram"],
      "The threshold was found by sweeping context on one model and card.",
      "SPEED DROPS WHERE THE CACHE FILLS")

angle("KV-007",
      "The cache is written once per token and read once per token after that, which is why generation on a long context is a memory read problem.",
      "cache write and read pattern",
      "MECHANISM",
      ["cache", "generation", "latency"],
      "The access pattern was inferred from timings rather than profiled directly.",
      "THE CACHE IS READ ON EVERY TOKEN")

angle("KV-008",
      "The prompt processing phase and the cache phase cost different amounts of memory, which is why a model can prefill and then fail to generate.",
      "memory across the two phases",
      "FAILURE",
      ["cache", "prefill", "vram"],
      "Observed under one runtime with one allocator; other runtimes reserve differently.",
      "IT PREFILLED, THEN IT FAILED")

angle("KV-009",
      "Truncating old conversation is more effective than raising the context limit, because every token you keep is a token you pay for twice.",
      "history truncation versus context expansion",
      "DECISION",
      ["cache", "latency", "capacity"],
      "Assumes old turns are not needed; tasks with long-range dependencies contradict it.",
      "TRUNCATE HISTORY BEFORE BUYING CONTEXT")

angle("KV-010",
      "A model with a smaller advertised window can be the better local choice if its cache is smaller per token, so context numbers are not comparable across models.",
      "cross-model context comparability",
      "MYTH",
      ["cache", "capacity", "papers"],
      "Two model families were compared; cache layouts vary more widely than that.",
      "CONTEXT NUMBERS ARE NOT COMPARABLE")

angle("KV-011",
      "The cache grows even when the model is producing the same short answer, so fixed prompt templates are a recurring memory cost in an agent loop.",
      "cache growth in agent loops",
      "MECHANISM",
      ["cache", "generation", "latency"],
      "One loop structure was tested; tool-heavy loops grow faster.",
      "EVERY AGENT TURN PAYS RENT")

angle("KV-012",
      "The memory saved by a shorter context is available for a bigger model, so context and model size compete for the same budget.",
      "context versus model size on one card",
      "PARADOX",
      ["cache", "vram", "capacity"],
      "A different card with more memory would remove the trade-off.",
      "CONTEXT AND MODEL SIZE SHARE ONE BUDGET")

angle("KV-013",
      "The advertised maximum context is a hardware statement about memory, not a claim that the model will attend to all of it.",
      "maximum context versus usable context",
      "MYTH",
      ["cache", "papers", "capacity"],
      "Attention quality was not measured; this episode only shows the memory boundary.",
      "MAXIMUM CONTEXT IS A MEMORY CLAIM")

angle("KV-014",
      "Cache quantization has a different cost profile from weight quantization, because the cache is touched on every token rather than once per request.",
      "cache quantization cost profile",
      "COMPARISON",
      ["quant", "cache", "generation"],
      "Only one cache quantization scheme was benchmarked.",
      "CACHE QUANTIZATION IS NOT FREE")

angle("KV-015",
      "The cache is what makes a long prompt pay twice, once in prefill and again in every generated token that follows.",
      "double payment for a long prompt",
      "PARADOX",
      ["cache", "prefill", "generation"],
      "The doubling was demonstrated for one output length; long outputs change the ratio.",
      "A LONG PROMPT PAYS TWICE")

# ---------------------------------------------------------------------------
# QUANTIZATION  (12)
# ---------------------------------------------------------------------------

angle("QUANT-001",
      "The size you save by quantizing weights is not the size you save in memory, because the runtime keeps its own buffers at full precision.",
      "quantized file size versus resident memory",
      "PARADOX",
      ["quant", "vram", "capacity"],
      "One runtime's overhead was measured; another may keep more in high precision.",
      "A SMALLER FILE IS NOT A SMALLER FOOTPRINT")

angle("QUANT-002",
      "Quantizing to four bits roughly halves the weights, so a model that missed the card by a gigabyte now fits.",
      "four-bit as the fitting point",
      "MEASUREMENT",
      ["quant", "vram", "capacity"],
      "The fit was tested on one card with one model; overhead still moves the boundary.",
      "FOUR BITS BUYS YOU THE CARD")

angle("QUANT-003",
      "Quantization changes output length distribution, which changes tokens per second on the same card without making the card faster.",
      "quantization changing the workload",
      "MEASUREMENT",
      ["quant", "generation", "latency"],
      "Observed on one prompt set; the shift may not generalize.",
      "QUANTIZATION CHANGED THE ANSWER LENGTH")

angle("QUANT-004",
      "The accuracy cost of quantization is not a single number, because the same bit depth hurts a small model and a large model differently.",
      "quantization error versus model size",
      "PARADOX",
      ["quant", "papers", "capacity"],
      "Perplexity was compared across two sizes only.",
      "FOUR BITS COSTS BIG MODELS MORE")

angle("QUANT-005",
      "Quantization is the only way to run a model larger than your card's memory, which makes it a hardware-enabling tool rather than a speed tool.",
      "quantization as a hardware enabler",
      "DECISION",
      ["quant", "vram", "capacity"],
      "A model that fits unquantized does not need this trade at all.",
      "QUANTIZATION IS WHAT LETS IT RUN AT ALL")

angle("QUANT-006",
      "The speed gain from quantization depends on whether the kernel supports the format, so the same bit depth gives different results on different stacks.",
      "kernel support as the hidden variable",
      "MECHANISM",
      ["quant", "generation", "latency"],
      "Two software stacks on one card were compared; hardware support differs too.",
      "THE FORMAT MATTERS MORE THAN THE BITS")

angle("QUANT-007",
      "Quantized models produce fewer tokens because they produce shorter answers, which is why a benchmark can improve without the hardware improving.",
      "quantization and output brevity",
      "MYTH",
      ["quant", "generation", "papers"],
      "Length was not separated from quality in the source benchmarks.",
      "SHORTER ANSWERS LOOK LIKE FASTER MODELS")

angle("QUANT-008",
      "The weight file on disk and the weights in memory are not the same objects after loading, so disk size predicts fit only roughly.",
      "what loading does to a quantized file",
      "MECHANISM",
      ["quant", "vram", "capacity"],
      "The mapping was observed in one loader; other loaders may dequantize eagerly.",
      "LOADING UNDOES PART OF THE SAVING")

angle("QUANT-009",
      "Quantizing a model you already fit buys speed, while quantizing one you cannot fit buys existence, and those are different purchases.",
      "quantization as fit versus speed",
      "DECISION",
      ["quant", "vram", "generation"],
      "Two model sizes were used to frame the choice; the boundary is hardware-specific.",
      "FIT OR SPEED, NOT BOTH")

angle("QUANT-010",
      "Quantization is a bargain until the model's output drifts, and the drift is invisible on benchmark scores and obvious in use.",
      "quantization drift beyond benchmarks",
      "MYTH",
      ["quant", "papers", "latency"],
      "Drift was judged by inspection on a small prompt set, not by a formal evaluation.",
      "THE BENCHMARK NEVER SHOWS THE DRIFT")

angle("QUANT-011",
      "The gap between quantized and unquantized memory use is larger for the weights than for the whole model, so advertised savings are always an upper bound.",
      "weight savings versus total savings",
      "MATH",
      ["quant", "vram", "cache"],
      "The arithmetic assumes fixed runtime overhead, which varies by implementation.",
      "ADVERTISED SAVINGS ARE A CEILING")

angle("QUANT-012",
      "Quantizing the weights while keeping the cache at full precision leaves the second memory bill untouched, so the total savings are smaller than the headline.",
      "weight quantization versus full-stack quantization",
      "COMPARISON",
      ["quant", "cache", "vram"],
      "Cache and weight quantization were varied separately on one model.",
      "YOU QUANTIZED HALF THE MEMORY BILL")

# ---------------------------------------------------------------------------
# LORA AND FINE-TUNING  (12)
# ---------------------------------------------------------------------------

angle("LORA-001",
      "A LoRA adapter is small enough to store in minutes but runs at the speed and memory cost of the base model it modifies.",
      "adapter size versus runtime footprint",
      "PARADOX",
      ["lora", "vram", "generation"],
      "The base model was the same in both cases; a smaller base changes the ratio.",
      "TINY FILE, FULL-SIZE FOOTPRINT")

angle("LORA-002",
      "Loading two adapters for the same base doubles the switch cost, because the base model is the expensive part and it is loaded either way.",
      "multi-adapter serving cost",
      "MEASUREMENT",
      ["lora", "vram", "latency"],
      "Switching was measured sequentially, not with a hot-swap server.",
      "SWITCHING ADAPTERS COSTS A MODEL LOAD")

angle("LORA-003",
      "Serving many adapters from one base is cheaper on memory than serving many full models, which makes adapters the practical choice for many specialists.",
      "adapter serving versus full-model serving",
      "COST",
      ["lora", "vram", "capacity"],
      "Costs were compared on memory and load time; quality per dollar was not measured.",
      "ONE BASE, MANY SPECIALISTS")

angle("LORA-004",
      "The adapter's own file size says nothing about the memory it needs at runtime, because the merged weights must still fit.",
      "adapter file size versus merged size",
      "MYTH",
      ["lora", "vram", "capacity"],
      "The merge was done on one base model with one adapter rank.",
      "A SMALL ADAPTER STILL NEEDS A BIG MODEL")

angle("LORA-005",
      "Merging the adapter into the base weights before serving removes the adapter overhead at runtime, which makes offline use faster than live use.",
      "merged versus live adapter inference",
      "COMPARISON",
      ["lora", "generation", "latency"],
      "Merge was performed on disk with one rank; larger ranks scale the saving.",
      "MERGE IT AND THE OVERHEAD DISAPPEARS")

angle("LORA-006",
      "A higher adapter rank costs more memory at inference for a small quality gain, so the cheapest useful rank is rarely the lowest one.",
      "adapter rank versus runtime memory",
      "MECHANISM",
      ["lora", "vram", "cache"],
      "Quality was judged narrowly on one task set.",
      "RANK COSTS MEMORY ON EVERY TOKEN")

angle("LORA-007",
      "The adapter's compute overhead is proportional to its rank, which is why a large-rank adapter is slower than the base even though the file is small.",
      "adapter compute overhead",
      "MECHANISM",
      ["lora", "generation", "latency"],
      "Overhead was measured for two ranks on one model.",
      "THE SMALL FILE STILL COSTS TIME")

angle("LORA-008",
      "Fine-tuning a model on a card that cannot hold the optimizer states is possible only with offloading, which is where the real memory cost appears.",
      "training memory beyond the weights",
      "MECHANISM",
      ["lora", "vram", "capacity"],
      "Optimizer states for one optimizer were measured; others use more.",
      "TRAINING NEEDS MORE MEMORY THAN INFERENCE")

angle("LORA-009",
      "The memory you save by training with an adapter is memory you do not save when you serve it, because serving loads the full base anyway.",
      "training savings versus serving costs",
      "PARADOX",
      ["lora", "vram", "capacity"],
      "One training setup and one serving setup were compared.",
      "TRAINING BARGAIN DOES NOT CARRY TO SERVING")

angle("LORA-010",
      "An adapter tuned for one base model does not transfer to another, so the base is the expensive part of the adapter you keep.",
      "adapter portability across bases",
      "MYTH",
      ["lora", "papers", "vram"],
      "One adapter family was tried on two bases; none transferred.",
      "ADAPTERS ARE TIED TO THEIR BASE")

angle("LORA-011",
      "Training an adapter for a long context requires training with the cache in memory, which raises the training memory floor above the inference floor.",
      "training memory at long context",
      "MEASUREMENT",
      ["lora", "cache", "vram"],
      "The training context was shorter than the target serving context.",
      "TRAINING AT LONG CONTEXT COSTS MORE")

angle("LORA-012",
      "Adapters let you run one hardware setup for several tasks, so the return on a small adapter is a change in workload, not a change in speed.",
      "adapters as workload economics",
      "DECISION",
      ["lora", "vram", "generation"],
      "The economics argument assumed a fixed number of tasks and one server.",
      "ONE MACHINE, MANY JOBS")

# ---------------------------------------------------------------------------
# PAPERS AND WHAT THEY DO NOT ESTABLISH  (10)
# ---------------------------------------------------------------------------

angle("PA-001",
      "A paper's reported tokens per second are a property of a specific configuration, so the number is meaningless without its hardware and batch size.",
      "benchmark numbers missing their configuration",
      "MYTH",
      ["papers", "generation", "latency"],
      "Configuration details were missing in the sources examined, not in all papers.",
      "A BENCHMARK NUMBER WITHOUT SETUP")

angle("PA-002",
      "A paper that reports a speedup without reporting whether the baseline also spilled to disk has not measured the thing you care about.",
      "missing spill disclosure in comparisons",
      "MYTH",
      ["papers", "vram", "generation"],
      "Applied to a sample of papers; disclosure norms may be improving.",
      "THE BASELINE MAY HAVE BEEN SPILLING")

angle("PA-003",
      "Latency reported as a mean hides the tail, and on local hardware the tail is the difference between a working tool and an abandoned one.",
      "mean latency versus tail latency",
      "PARADOX",
      ["papers", "latency", "prefill"],
      "Tail data was reconstructed from limited runs, not a full distribution.",
      "THE MEAN HIDES THE WAIT")

angle("PA-004",
      "A paper measured on datacenter hardware does not predict local hardware behavior, because the memory system is the thing that changed.",
      "datacenter results versus local results",
      "COMPARISON",
      ["papers", "vram", "generation"],
      "Two papers were compared against one local card; no datacenter gear was tested here.",
      "DATACENTER NUMBERS DO NOT TRAVEL")

angle("PA-005",
      "Reported quality scores on multiple-choice benchmarks do not predict behavior on the long prompts where context length matters.",
      "benchmark quality versus long-prompt behavior",
      "MYTH",
      ["papers", "cache", "capacity"],
      "Only one long-prompt task was used to illustrate the gap.",
      "SCORES DO NOT MEAN MUCH AT 32K")

angle("PA-006",
      "A quantization paper that reports perplexity reports an average, and averages hide the tasks where the degradation concentrates.",
      "perplexity averages hiding local degradation",
      "PARADOX",
      ["papers", "quant", "capacity"],
      "The average was compared across two task families, not dissected fully.",
      "THE AVERAGE HIDES WHERE IT BREAKS")

angle("PA-007",
      "When a paper reports a smaller memory footprint without saying what happened to speed, the missing half of the result is the whole story.",
      "memory claims without speed claims",
      "MYTH",
      ["papers", "quant", "vram", "generation"],
      "Applies to the papers surveyed; some report both.",
      "LESS MEMORY, BUT HOW FAST?")

angle("PA-008",
      "A method that improves a benchmark by changing the prompt rather than the model is not a hardware advance, and the paper's own numbers show it.",
      "prompt-side wins dressed as model wins",
      "HISTORY",
      ["papers", "prefill", "latency"],
      "Detected in the sample reviewed; some prompt gains are real and useful.",
      "THE PROMPT DID THE WORK")

angle("PA-009",
      "The most useful thing about a papers page for a local builder is what it omits, because the omissions are the constraints you will hit.",
      "reading papers for what is absent",
      "HISTORY",
      ["papers", "vram", "capacity"],
      "A reading method, not a measurement; it produces no new numbers.",
      "READ THE PAPER FOR WHAT IS MISSING")

angle("PA-010",
      "Reproducing a paper's headline number on your own card is the only way to know whether the result depends on hardware you do not have.",
      "local reproduction versus paper claims",
      "DECISION",
      ["papers", "generation", "vram", "latency"],
      "One published result was reproduced; scaling that to many papers is manual work.",
      "REPRODUCE IT OR YOU DO NOT KNOW")

# ---------------------------------------------------------------------------
# MULTI-CARD, OFFLOAD, SPILL, PAGE  (10)
# ---------------------------------------------------------------------------

angle("MU-001",
      "Splitting a model across two cards costs a small overhead per token, while splitting the workload across two cards doubles the throughput, so the split you choose decides which you get.",
      "model split versus workload split",
      "COMPARISON",
      ["vram", "generation", "capacity"],
      "Both cards were identical and connected by the same link.",
      "SPLIT THE MODEL OR THE WORK")

angle("MU-002",
      "When a layer is offloaded to system RAM, the token waits for the PCIe link, which is why offload turns a fast card into a slow machine.",
      "the link as the offload bottleneck",
      "MECHANISM",
      ["vram", "generation", "latency"],
      "Link traffic was inferred from timing; direct bus counters were unavailable.",
      "THE SLOT IS THE BOTTLENECK")

angle("MU-003",
      "Offloading only the embedding and output layers can save a surprising amount of memory because those are the largest tensors, even though they compute almost nothing.",
      "offloading the largest tensors",
      "MEASUREMENT",
      ["vram", "capacity", "generation"],
      "Measured on one model whose embedding is unusually large.",
      "OFFLOAD THE LAYER THAT DOES NOTHING")

angle("MU-004",
      "Paging model weights to disk during inference is slower than any other way to use the machine, and the speed penalty is far larger than the disk's raw latency suggests.",
      "the true cost of disk paging",
      "FAILURE",
      ["vram", "generation", "latency"],
      "Measured with one page size and one storage device; NVMe differs.",
      "PAGEING IS WORSE THAN WAITING")

angle("MU-005",
      "Two cards with different memory sizes are worse than two cards with the same size, because the smaller card dictates the split point.",
      "mismatched cards and the split point",
      "COMPARISON",
      ["vram", "capacity", "generation"],
      "One mismatched pair was tested; the faster card was left with less to do.",
      "THE WEAKER CARD SETS THE PACE")

angle("MU-006",
      "A second card in the same machine shares the host memory bus, so it adds capacity without adding bandwidth when the workload is memory-bound.",
      "host bus contention between cards",
      "MECHANISM",
      ["vram", "generation", "capacity"],
      "Bandwidth contention was inferred from scaling behavior, not measured directly.",
      "TWO CARDS, ONE MEMORY BUS")

angle("MU-007",
      "Running two models on two cards instead of one model on two cards doubles the work per second, because the second card would otherwise be idle waiting.",
      "one model per card versus split model",
      "DECISION",
      ["generation", "vram", "capacity"],
      "Assumes the second workload fits its card; a larger second model changes the answer.",
      "ONE MODEL PER CARD WINS")

angle("MU-008",
      "CPU offload is the fallback that always works, which is why it is the setting people leave on by default and the reason their machine feels slow.",
      "why offload is the default setting",
      "HISTORY",
      ["vram", "generation", "latency"],
      "The argument covers one runtime's default behavior.",
      "THE DEFAULT SETTING IS THE SLOW ONE")

angle("MU-009",
      "A model that spills to disk is not slow because the disk is slow but because the spill happens at every token boundary, so the penalty compounds.",
      "why per-token spill compounds",
      "MECHANISM",
      ["vram", "generation", "latency"],
      "The compounding was modeled and confirmed at two spill ratios.",
      "THE PENALTY COMPOUNDS EVERY TOKEN")

angle("MU-010",
      "Adding a second card is worth it only if the model actually fits across both, because a split model with one card idle is a slower single card.",
      "when a second card pays off",
      "DECISION",
      ["vram", "capacity", "generation"],
      "The break-even was found for one model size; a larger model shifts it.",
      "THE SECOND CARD NEEDS A REASON")

# ---------------------------------------------------------------------------
# THE CARDS THEMSELVES  (8)
# ---------------------------------------------------------------------------

angle("HW-001",
      "Two cards with the same memory size and different memory speeds give different token rates, which means the memory subsystem is the card.",
      "the memory subsystem as the card's real identity",
      "COMPARISON",
      ["vram", "generation"],
      "Two card generations compared; compute cores were not identical.",
      "THE CARD IS ITS MEMORY SYSTEM")

angle("HW-002",
      "A card's advertised bandwidth is the number that predicts tokens per second, and its advertised teraflops rarely does for text generation.",
      "bandwidth versus teraflops as predictors",
      "MECHANISM",
      ["generation", "vram", "papers"],
      "Fitted across a handful of cards; the correlation is not universal.",
      "THE NUMBER THAT MATTERS IS BANDWIDTH")

angle("HW-003",
      "The same card in a laptop throttles under sustained generation, so the paper spec is a peak number and the laptop number is a different product.",
      "sustained versus peak performance",
      "FAILURE",
      ["generation", "vram", "latency"],
      "Thermal behavior depends on cooling and ambient temperature.",
      "THE LAPTOP SLOWS DOWN ON PURPOSE")

angle("HW-004",
      "A mini desktop with less memory than a tower can still be the better local AI machine if it fits the model, which makes the form factor a memory question.",
      "mini desktops for local AI",
      "DECISION",
      ["vram", "capacity", "generation"],
      "Compared on model size only; noise and thermals were not scored.",
      "SMALL BOX, RIGHT-SIZED MODEL")

angle("HW-005",
      "Integrated graphics that borrow system memory are slower than a discrete card but can be the only option for a model that does not fit anywhere else.",
      "integrated graphics as a fallback",
      "COMPARISON",
      ["vram", "capacity", "generation"],
      "One integrated implementation was tested; newer ones vary widely.",
      "BORROWED MEMORY, BORROWED SPEED")

angle("HW-006",
      "Two cards of the same model in one machine deliver less than twice one card's throughput because the host interface is shared, and the shortfall is predictable.",
      "scaling shortfall across two identical cards",
      "MATH",
      ["generation", "vram", "capacity"],
      "The shortfall depends on the link and the workload; one configuration was measured.",
      "TWO CARDS DO NOT MEAN TWO SPEED")

angle("HW-007",
      "The card's memory size decides which models you can even consider, so it sets the ceiling on what every other feature can do.",
      "memory size as the first filter",
      "DECISION",
      ["vram", "capacity", "papers"],
      "A buying framework, not a benchmark; it does not weigh reliability or support.",
      "MEMORY SIZE IS THE FIRST QUESTION")

angle("HW-008",
      "A newer card with less memory than the one you own can be the worse machine for local AI, because the constraint is capacity rather than speed.",
      "newer versus larger memory",
      "PARADOX",
      ["vram", "capacity", "generation"],
      "One older large-memory card was compared with one newer small-memory card.",
      "OLDER AND BIGGER STILL WINS")

# ---------------------------------------------------------------------------
# MEASUREMENT DISCIPLINE AND COMMON MISREADINGS  (13)
# ---------------------------------------------------------------------------

angle("ME-001",
      "A benchmark that reports tokens per second but not the memory state of the machine is reporting a number that cannot be reproduced.",
      "reproducibility requirements for a token-rate claim",
      "MEASUREMENT",
      ["generation", "vram", "latency"],
      "This is a checklist, not a new measurement; the checklist cannot guarantee correctness.",
      "NO SETUP, NO NUMBER")

angle("ME-002",
      "Timing a generation run without discarding the first token measures the model's warm-up, not its speed.",
      "warm-up contamination in generation timings",
      "MEASUREMENT",
      ["generation", "latency", "cache"],
      "Warm-up length depends on model and cache state; two warm-up lengths were tried.",
      "YOUR FIRST TOKEN IS NOT YOUR SPEED")

angle("ME-003",
      "A run measured on a hot machine is slower than the same run on a cold one, so a laptop benchmark needs its temperature stated.",
      "thermal state as a measurement variable",
      "FAILURE",
      ["generation", "latency", "vram"],
      "Measured on one laptop with one cooling setup.",
      "COLD NUMBERS, HOT MACHINES")

angle("ME-004",
      "A speedup measured against a baseline that was itself misconfigured is worse than no result, because it moves the goalposts.",
      "bad baselines as measurement fraud",
      "MYTH",
      ["papers", "generation", "latency"],
      "Applies to the comparison style, not to any specific team.",
      "A BAD BASELINE HIDES A GOOD RESULT")

angle("ME-005",
      "The context length in a test prompt silently changes the workload, so two runs of the same model are not comparable unless the prompt is identical.",
      "prompt mismatch between runs",
      "MEASUREMENT",
      ["prefill", "cache", "latency"],
      "One prompt template was varied in length; content changes were not tested.",
      "DIFFERENT PROMPT, DIFFERENT BENCHMARK")

angle("ME-006",
      "A model scored on short questions and a model scored on long documents are not being measured on the same axis, so the leaderboard mixes two problems.",
      "leaderboard task mismatch",
      "MYTH",
      ["papers", "prefill", "cache"],
      "Observed in one leaderboard; others separate tasks.",
      "ONE BOARD, TWO DIFFERENT JOBS")

angle("ME-007",
      "The most common measurement mistake in local AI is reporting an end-to-end number that includes the operator's typing time.",
      "human time inside the measurement",
      "FAILURE",
      ["latency", "prefill", "generation"],
      "Typical human delay was estimated, not measured on a real user study.",
      "THE USER WAS PART OF THE TIMER")

angle("ME-008",
      "A single-run measurement on local hardware carries more variance than the differences people report, so repeats matter more than precision.",
      "run-to-run variance on consumer hardware",
      "MEASUREMENT",
      ["generation", "latency", "vram"],
      "Variance was measured for one model on one card with ten repeats.",
      "ONE RUN IS NOT A MEASUREMENT")

angle("ME-009",
      "The number people quote as the model's speed is a property of the measurement rig, and rig specifications should be quoted with it.",
      "quoting numbers with their rig",
      "DECISION",
      ["generation", "latency", "capacity"],
      "A reporting convention, not a measurement; it produces no new figures.",
      "QUOTE THE RIG WITH THE NUMBER")

angle("ME-010",
      "Local AI numbers are hardware-specific in a way that cloud numbers are not, which means a comparison across two people's results is usually invalid.",
      "cross-machine comparison validity",
      "MYTH",
      ["generation", "vram", "papers"],
      "Two published comparisons were checked; both failed the check.",
      "TWO MACHINES, NOT ONE BENCHMARK")

angle("ME-011",
      "Measuring only the prompt phase and only the generation phase gives two numbers that add up to less than the real wait, and the gap is the overhead nobody budgets for.",
      "the unaccounted overhead between phases",
      "MATH",
      ["prefill", "generation", "latency"],
      "The residual was measured for one runtime and one model.",
      "THE GAP BETWEEN THE NUMBERS IS REAL")

angle("ME-012",
      "A number copied from a benchmark without the model, the quant, the card and the context is a rumor, and this channel treats it as one.",
      "the provenance rule for hardware numbers",
      "DECISION",
      ["papers", "vram", "quant", "cache"],
      "An editorial rule for the channel; it does not change any measurement.",
      "A NUMBER WITHOUT SETUP IS A RUMOR")

angle("ME-013",
      "A good local benchmark should state the memory state before it states the speed, because the memory state explains most speed differences.",
      "ordering memory before speed in a report",
      "DECISION",
      ["vram", "generation", "latency"],
      "A reporting rule; no new numbers were produced for it.",
      "MEMORY FIRST, THEN SPEED")
