# -*- coding: utf-8 -*-
"""
Scenes 25-48 authoritative visual definitions.
"""

SCENES_25_48 = [
    # Scene 25 (hook)
    {
        "layout": "hook",
        "title": "THE HYPOTHETICAL ARCHITECTURE",
        "header_at": "Here is a calculation",
        "art": "caveat",
        "art_at": "made-up architecture for explaining",
        "art_caption": "THEORETICAL PEDAGOGICAL MODEL",
        "chips": [
            {"at": "made-up architecture for explaining", "c": "cyan", "t": "HYPOTHETICAL DESIGN"},
            {"at": "not a measured benchmark", "c": "hot", "t": "MATH EXPLANATION"}
        ],
        "stats": [
            {"at": "made-up architecture for explaining", "c": "cyan", "lab": "MODEL PURPOSE", "u": "EXPLAIN", "v": "MATH"},
            {"at": "not a measured benchmark", "c": "gold", "lab": "NAMED BENCHMARK", "u": "ZERO", "v": "NONE"}
        ],
        "closing": {"at": "named AI model", "c": "gold", "t": "CALCULATION DEMONSTRATES THE SCALING PRINCIPLE"}
    },
    # Scene 26 (rows)
    {
        "layout": "rows",
        "title": "THE FOUR KV VARIABLES",
        "header_at": "Imagine thirty-two layers, eight",
        "art": "cache_grid",
        "art_at": "Every cached token needs",
        "art_caption": "ATTENTION TENSOR SPECIFICATIONS",
        "rows": [
            {"at": "thirty-two layers", "cls": "cyan", "name": "LAYERS", "rank": "01", "sub": "TRANSFORMER BLOCKS", "val": "32"},
            {"at": "eight key-value heads", "cls": "gold", "name": "KV HEADS", "rank": "02", "sub": "GQA HEAD GROUP", "val": "8"},
            {"at": "two bytes for each stored", "cls": "hot", "name": "FP16 PRECISION", "rank": "03", "sub": "128 DIM * 2 BYTES", "val": "2 BYTES"}
        ],
        "closing": {"at": "both a key and a value", "c": "gold", "t": "EVERY TOKEN STORES BOTH KEY AND VALUE TENSORS"}
    },
    # Scene 27 (bars)
    {
        "layout": "bars",
        "title": "8K VS 32K CONTEXT CACHE",
        "header_at": "With that hypothetical design",
        "art": "vram_module",
        "art_at": "thirty-two-thousand-token cache occupies",
        "art_caption": "HYPOTHETICAL KV CACHE FOOTPRINT",
        "bars": [
            {"at": "thirty-two-thousand-token cache occupies", "cls": "gold", "lab": "32K TOKENS CACHE", "pct": 100.0, "unit": "GiB", "val": "4 GiB"},
            {"at": "At eight thousand tokens", "cls": "cyan", "lab": "8K TOKENS CACHE", "pct": 25.0, "unit": "GiB", "val": "1 GiB"}
        ],
        "closing": {"at": "occupy about one gibibyte", "c": "gold", "t": "CACHE SCALES LINEARLY WITH SEQUENCE LENGTH"}
    },
    # Scene 28 (rail)
    {
        "layout": "rail",
        "title": "THE 128K SHOCK: 16 GIB CACHE",
        "header_at": "At one hundred and",
        "art": "vram_module",
        "art_at": "one hundred and twenty-eight thousand tokens",
        "art_caption": "128K SEQUENCE MEMORY EXPLOSION",
        "rails": [
            {"at": "one hundred and twenty-eight thousand tokens", "cls": "cyan", "lab": "128K SEQUENCE", "val": "128K TOKENS"},
            {"at": "about sixteen gibibytes", "cls": "hot", "lab": "KV CACHE FOOTPRINT", "val": "16 GiB VRAM"}
        ],
        "closing": {"at": "about sixteen gibibytes", "c": "hot", "t": "128K CACHE DEMANDS 16 GiB BEFORE WEIGHTS"}
    },
    # Scene 29 (chain)
    {
        "layout": "chain",
        "title": "WEIGHTS FIT · CACHE OOMS",
        "header_at": "That is the shock",
        "art": "collapse",
        "art_at": "pushes the whole workload over",
        "art_caption": "THE SILENT ALLOCATION BREAKDOWN",
        "chain": [
            {"at": "weights could already fit", "t": "1. MODEL WEIGHTS FIT", "s": "GGUF LOADS IN VRAM"},
            {"at": "pushes the whole workload", "t": "2. KV CACHE EXPANDS", "s": "+16 GiB DYNAMIC CACHE"},
            {"at": "over the edge", "t": "3. ALLOCATION OOM", "s": "SYSTEM CRASHES / EVICTS"}
        ],
        "compare": [
            {"at": "weights could already fit", "cls": "dim", "title": "STATIC WEIGHTS", "body": "COMFORTABLE FIT"},
            {"at": "pushes the whole workload", "cls": "hot", "title": "WORKLOAD STATE", "body": "OVER THE EDGE"}
        ],
        "closing": {"at": "over the edge", "c": "hot", "t": "FITTING THE WEIGHTS != FITTING THE CONVERSATION"}
    },
    # Scene 30 (note)
    {
        "layout": "note",
        "title": "QUANTIZATION ASYMMETRY",
        "header_at": "Reducing the weight file",
        "art": "gguf_blocks",
        "art_at": "quantization does not automatically reduce",
        "art_caption": "WEIGHT PRECISION VS CACHE PRECISION",
        "note_head": "ARCHITECTURE-DEPENDENT SCALING",
        "note_items": [
            {"at": "quantization does not automatically", "t": "WEIGHT QUANTIZATION LEAVES KV CACHE IN FP16"},
            {"at": "actual model architecture", "t": "EXACT CACHE NUMBERS VARY BY MODEL DESIGN"},
            {"at": "reduce the number of key-value heads", "t": "GROUPED-QUERY ATTENTION (GQA) CUTS KV HEADS"}
        ],
        "closing": {"at": "number of key-value heads", "c": "gold", "t": "QUANTIZING WEIGHTS DOES NOT AUTOMATICALLY QUANTIZE CACHE"}
    },
    # Scene 31 (strip)
    {
        "layout": "strip",
        "title": "ATTENTION PATTERNS & OFFLOADING",
        "header_at": "Sliding-window and other attention",
        "art": "ram_stick",
        "art_at": "Sliding-window and other attention patterns",
        "art_caption": "ARCHITECTURAL MEMORY OPTIMIZATIONS",
        "items": [
            {"at": "Sliding-window and other attention", "key": "cache_grid", "label": "SLIDING WINDOW", "sub": "BOUNDED KV CACHE"},
            {"at": "quantized or offloaded caches", "key": "ram_stick", "label": "QUANTIZED CACHE", "sub": "Q8_0 / Q4_0 KV"},
            {"at": "call them specifications", "key": "warning", "label": "NO SPEC COPYING", "sub": "MEASURE PER MODEL"}
        ],
        "closing": {"at": "call them specifications", "c": "hot", "t": "NEVER COPY HYPOTHETICAL NUMBERS AS SPECS"}
    },
    # Scene 32 (nodes)
    {
        "layout": "nodes",
        "title": "CONCURRENCY: MULTI-USER PRESSURE",
        "header_at": "But the principle is",
        "art": "lan_link",
        "art_at": "serving more than one request",
        "art_caption": "SHARED RUNTIME KV CACHE ALLOCATION",
        "chain": [
            {"at": "fitting the weights is not the same", "c": "cyan", "t": "WEIGHTS VS CHAT", "s": "FIT CONVERSATION"},
            {"at": "runtime is also serving", "c": "gold", "t": "CONCURRENT CALLS", "s": "N * ACTIVE CONVERSATIONS"},
            {"at": "more than one request", "c": "hot", "t": "MULTIPLIED CACHE", "s": "MEMORY POOL PRESSURE"}
        ],
        "closing": {"at": "more than one request", "c": "gold", "t": "CONCURRENCY MULTIPLIES ACTIVE KV CACHE DEMAND"}
    },
    # Scene 33 (hook)
    {
        "layout": "hook",
        "title": "CHAT SERVER STATE PRESSURE",
        "header_at": "A chat server might",
        "art": "rack_server",
        "art_at": "hold active state for multiple users",
        "art_caption": "CONCURRENT SESSION CACHE SIZING",
        "chips": [
            {"at": "multiple users", "c": "cyan", "t": "MULTI-USER CHAT SERVER"},
            {"at": "support those active sequences", "c": "hot", "t": "CONCURRENT KV STATES"}
        ],
        "stats": [
            {"at": "multiple users", "c": "cyan", "lab": "ACTIVE SESSIONS", "u": "USERS", "v": "MULTI"},
            {"at": "support those active sequences", "c": "gold", "lab": "CACHE REQUIREMENT", "u": "SUM", "v": "N * KV"}
        ],
        "closing": {"at": "support those active sequences too", "c": "gold", "t": "SERVER MEMORY MUST HOLD STATE FOR ALL USERS"}
    },
    # Scene 34 (rows)
    {
        "layout": "rows",
        "title": "SINGLE USER VS CONCURRENCY",
        "header_at": "A context size that",
        "art": "scales",
        "art_at": "works for one short chat",
        "art_caption": "ISOLATED BENCHMARK VS PRODUCTION LOAD",
        "rows": [
            {"at": "one short chat", "cls": "cyan", "name": "SINGLE SHORT CHAT", "rank": "01", "sub": "ISOLATED THREAD", "val": "STABLE"},
            {"at": "long requests running at the same", "cls": "hot", "name": "CONCURRENT LONG", "rank": "02", "sub": "SHARED VRAM POOL", "val": "SATURATED"}
        ],
        "closing": {"at": "running at the same time", "c": "hot", "t": "LONG CONCURRENT REQUESTS CRUSH RUNTIME MEMORY"}
    },
    # Scene 35 (bars)
    {
        "layout": "bars",
        "title": "INSUFFICIENT CACHE ERRORS",
        "header_at": "This is why you",
        "art": "warning",
        "art_at": "insufficient cache memory even after",
        "art_caption": "POST-LOAD RUNTIME ALLOCATION ABORTS",
        "bars": [
            {"at": "insufficient cache memory", "cls": "hot", "lab": "CACHE ALLOCATION", "pct": 100.0, "unit": "ERROR", "val": "OOM ABORT"},
            {"at": "weights have loaded", "cls": "cyan", "lab": "WEIGHTS LOADED", "pct": 60.0, "unit": "VRAM", "val": "SUCCESS"}
        ],
        "closing": {"at": "stop launching", "c": "gold", "t": "BLINDLY RAISING CONTEXT SIZES CRASHES PREVIOUSLY STABLE SYSTEMS"}
    },
    # Scene 36 (rail)
    {
        "layout": "rail",
        "title": "LIMIT 4: EFFECTIVE USE",
        "header_at": "The fourth limit is",
        "art": "question",
        "art_at": "fourth limit is more subtle",
        "art_caption": "THE EFFECTIVE RECALL AND ACCURACY CEILING",
        "rails": [
            {"at": "hardware stores them", "cls": "cyan", "lab": "HARDWARE STATE", "val": "TOKENS STORED"},
            {"at": "use all that information reliably", "cls": "hot", "lab": "MODEL RECALL", "val": "UNRELIABLE USE"}
        ],
        "closing": {"at": "use all that information reliably", "c": "gold", "t": "STORING DATA IN VRAM DOES NOT GUARANTEE RETRIEVAL"}
    },
    # Scene 37 (chain)
    {
        "layout": "chain",
        "title": "POSITION-DEPENDENT RETRIEVAL",
        "header_at": "Long-context research has demonstrated",
        "art": "prompt_stream",
        "art_at": "position of a fact can influence",
        "art_caption": "ATTENTION WEIGHT DISTRIBUTION DEGRADATION",
        "chain": [
            {"at": "Long-context research has demonstrated", "t": "1. EMPIRICAL RESEARCH", "s": "BENCHMARK EVALUATION"},
            {"at": "position of a fact", "t": "2. TOKEN POSITION", "s": "DEPTH IN SEQUENCE"},
            {"at": "retrieves it correctly", "t": "3. RECALL ACCURACY", "s": "SUCCESSFUL EXTRACTION"}
        ],
        "compare": [
            {"at": "position of a fact", "cls": "gold", "title": "START / END", "body": "STRONG RECALL"},
            {"at": "retrieves it correctly", "cls": "dim", "title": "BURIED MIDDLE", "body": "DEGRADED RECALL"}
        ],
        "closing": {"at": "retrieves it correctly", "c": "gold", "t": "WHERE A FACT SITS GOVERNS WHETHER IT IS FOUND"}
    },
    # Scene 38 (note)
    {
        "layout": "note",
        "title": "THE 'LOST IN THE MIDDLE' STUDY",
        "header_at": "In the study called",
        "art": "collapse",
        "art_at": "study called Lost in the Middle",
        "art_caption": "THE CLASSIC LONG-CONTEXT EVALUATION PAPER",
        "note_head": "LOST IN THE MIDDLE FINDINGS",
        "note_items": [
            {"at": "study called Lost in the Middle", "t": "RESEARCH: LIU ET AL. CONTEXT POSITION PAPER"},
            {"at": "beginning or the end of a long", "t": "BEGINNING & END OF PROMPT: HIGH RETRIEVAL ACCURACY"},
            {"at": "buried in the middle", "t": "BURIED IN THE MIDDLE: SHARP RETRIEVAL DEGRADATION"}
        ],
        "closing": {"at": "buried in the middle", "c": "hot", "t": "MODELS ATTEND STRONGLY TO EDGES · FORGET THE CENTER"}
    },
    # Scene 39 (strip)
    {
        "layout": "strip",
        "title": "MODEL & TASK DIVERGENCE",
        "header_at": "That is not a",
        "art": "scales",
        "art_at": "Results differ by model, task",
        "art_caption": "EVALUATION METHODOLOGY NUANCE",
        "items": [
            {"at": "forgets the middle", "key": "warning", "label": "NOT UNIVERSAL", "sub": "MODELS IMPROVING"},
            {"at": "differ by model", "key": "model_file", "label": "MODEL ARCHITECTURE", "sub": "TRAINING RECIPE"},
            {"at": "and evaluation", "key": "checklist", "label": "TASK RIGOR", "sub": "NEEDLE IN HAYSTACK"}
        ],
        "closing": {"at": "task, and evaluation", "c": "gold", "t": "RESULTS VARY BY MODEL ARCHITECTURE AND TASK COMPLEXITY"}
    },
    # Scene 40 (nodes)
    {
        "layout": "nodes",
        "title": "THE FORTY REPORTS EXPERIMENT",
        "header_at": "It is a warning",
        "art": "folder",
        "art_at": "giving a model forty reports",
        "art_caption": "SYNTHETIC POSITION VARIATION TEST",
        "chain": [
            {"at": "large numerical context limit", "c": "cyan", "t": "NUMERICAL LIMIT", "s": "128,000 ADVERTISED"},
            {"at": "reliable recall across the entire", "c": "hot", "t": "ACTUAL RECALL", "s": "UNIFORM EXTRACTION"},
            {"at": "giving a model forty reports", "c": "gold", "t": "40 REPORTS TEST", "s": "DOCUMENT EXPERIMENT"}
        ],
        "closing": {"at": "model forty reports", "c": "gold", "t": "A NUMERICAL LIMIT IS NOT UNIFORM RECALL"}
    },
    # Scene 41 (hook)
    {
        "layout": "hook",
        "title": "ORDER CHANGES THE ANSWER",
        "header_at": "One report, buried halfway",
        "art": "question",
        "art_at": "single number that answers your question",
        "art_caption": "IDENTICAL FACTS · CONFLICTING OUTPUTS",
        "chips": [
            {"at": "buried halfway through", "c": "hot", "t": "BURIED IN THE MIDDLE"},
            {"at": "changing the order of those reports", "c": "cyan", "t": "PERMUTED ORDER"}
        ],
        "stats": [
            {"at": "buried halfway through", "c": "hot", "lab": "MIDDLE RECALL", "u": "CHANCE", "v": "FAILS"},
            {"at": "none of the facts changed", "c": "gold", "lab": "FACT TRUTH", "u": "STATE", "v": "EXACT"}
        ],
        "closing": {"at": "none of the facts changed", "c": "gold", "t": "CHANGING DOCUMENT ORDER ALONE CHANGES THE ANSWER"}
    },
    # Scene 42 (rows)
    {
        "layout": "rows",
        "title": "THE REAL LONG-CONTEXT TEST",
        "header_at": "This is why one",
        "art": "checklist",
        "art_at": "useful long-context tests",
        "art_caption": "RELIABLE EMPIRICAL EVALUATION",
        "rows": [
            {"at": "most useful long-context tests", "cls": "gold", "name": "ACCURACY TEST", "rank": "01", "sub": "FACT RETRIEVAL", "val": "RECALL"},
            {"at": "loads a giant document", "cls": "dim", "name": "NAIVE INGEST", "rank": "02", "sub": "VRAM FIT ONLY", "val": "IRRELEVANT"}
        ],
        "closing": {"at": "loads a giant document", "c": "gold", "t": "SUCCESSFUL LOADING IS NOT PROOF OF COMPREHENSION"}
    },
    # Scene 43 (bars)
    {
        "layout": "bars",
        "title": "THE 3-POSITION AUDIT",
        "header_at": "It is placing the",
        "art": "prompt_stream",
        "art_at": "beginning, the middle, and the end",
        "art_caption": "NEEDLE PLACEMENT DEPTH AUDIT",
        "bars": [
            {"at": "near the beginning", "cls": "cyan", "lab": "DOCUMENT START", "pct": 95.0, "unit": "RECALL", "val": "HIGH"},
            {"at": "the middle", "cls": "hot", "lab": "DOCUMENT MIDDLE", "pct": 45.0, "unit": "RECALL", "val": "DROP"},
            {"at": "and the end", "cls": "cyan", "lab": "DOCUMENT END", "pct": 90.0, "unit": "RECALL", "val": "HIGH"}
        ],
        "closing": {"at": "follow the clock", "c": "gold", "t": "TEST THE SAME DETAIL ACROSS START, MIDDLE, AND END"}
    },
    # Scene 44 (rail)
    {
        "layout": "rail",
        "title": "THE CLOCK: PREFILL LATENCY",
        "header_at": "Before a model can",
        "art": "clock",
        "art_at": "initial pass is often called prefill",
        "art_caption": "PROMPT PROCESSING & EMBEDDING PHASE",
        "rails": [
            {"at": "process the input prompt", "cls": "cyan", "lab": "INITIAL PASS", "val": "PROMPT PROCESSING"},
            {"at": "initial pass is often called prefill", "cls": "gold", "lab": "PHASE NAME", "val": "PREFILL"}
        ],
        "closing": {"at": "prompt processing", "c": "gold", "t": "PREFILL MUST COMPLETE BEFORE FIRST TOKEN CAN EMIT"}
    },
    # Scene 45 (chain)
    {
        "layout": "chain",
        "title": "PREFILL VS DECODING",
        "header_at": "A very long prompt",
        "art": "pipeline",
        "art_at": "decoding: generating output tokens",
        "art_caption": "TWO SEPARATE HARDWARE OPERATING MODES",
        "chain": [
            {"at": "substantial computation and data movement", "t": "1. PREFILL STAGE", "s": "COMPUTE-BOUND MATRIX MULT"},
            {"at": "decoding: generating output tokens", "t": "2. DECODE STAGE", "s": "MEMORY-BOUND KV FETCH"},
            {"at": "one step after another", "t": "3. AUTOREGRESSIVE", "s": "TOKEN BY TOKEN"}
        ],
        "compare": [
            {"at": "substantial computation and data movement", "cls": "hot", "title": "PREFILL", "body": "PARALLEL COMPUTE"},
            {"at": "decoding: generating output tokens", "cls": "cyan", "title": "DECODE", "body": "SEQUENTIAL FETCH"}
        ],
        "closing": {"at": "one step after another", "c": "gold", "t": "LONG PROMPTS REQUIRE ENORMOUS PREFILL WORK"}
    },
    # Scene 46 (note)
    {
        "layout": "note",
        "title": "ATTENTION & MEMORY TRAFFIC",
        "header_at": "The cache helps by",
        "art": "motherboard",
        "art_at": "Attention and memory traffic still",
        "art_caption": "BANDWIDTH SATURATION DURING EXTENDED GENERATION",
        "note_head": "CACHE REALITY CHECKS",
        "note_items": [
            {"at": "reusing prior key and value states", "t": "KV CACHE REUSES PAST STATES · DOES NOT ELIMINATE BANDWIDTH"},
            {"at": "does not make a very long context free", "t": "LONG CONTEXTS DEMAND CONTINUOUS MEMORY TRAFFIC"},
            {"at": "Attention and memory traffic still", "t": "ATTENTION AND BUS SATURATION GROW WITH CONTEXT"}
        ],
        "closing": {"at": "implementations vary", "c": "gold", "t": "REUSING CACHE DOES NOT MAKE EXTENDED CONTEXT FREE"}
    },
    # Scene 47 (strip)
    {
        "layout": "strip",
        "title": "THE TWO SPEEDS TO MEASURE",
        "header_at": "That gives you two",
        "art": "tok_speed_dial",
        "art_at": "two separate speeds to measure",
        "art_caption": "TIME TO FIRST TOKEN VS GENERATION THROUGHPUT",
        "items": [
            {"at": "first token", "key": "clock", "label": "TTFT", "sub": "TIME TO FIRST TOKEN"},
            {"at": "quickly did the answer arrive", "key": "tok_speed_dial", "label": "THROUGHPUT", "sub": "TOKENS PER SECOND"},
            {"at": "generation started", "key": "prompt_stream", "label": "TOTAL LATENCY", "sub": "WALL CLOCK TIME"}
        ],
        "closing": {"at": "generation started", "c": "gold", "t": "MEASURE TIME TO FIRST TOKEN AND DECODE THROUGHPUT SEPARATELY"}
    },
    # Scene 48 (nodes)
    {
        "layout": "nodes",
        "title": "FLASH ATTENTION OPTIMIZATION",
        "header_at": "A system can generate",
        "art": "chip",
        "art_at": "Flash Attention and related kernels",
        "art_caption": "FUSED ATTENTION SRAM OPTIMIZATION",
        "chain": [
            {"at": "generate tokens quickly once it begins", "c": "cyan", "t": "FAST DECODE", "s": "RAPID TOKEN EMISSION"},
            {"at": "spent so long reading the prompt", "c": "hot", "t": "SLOW PREFILL", "s": "UNOPTIMIZED ATTENTION"},
            {"at": "Flash Attention and related kernels", "c": "gold", "t": "FLASHATTENTION", "s": "SRAM TILING KERNELS"}
        ],
        "closing": {"at": "reduce certain memory and computation", "c": "gold", "t": "FLASHATTENTION REDUCES HBM TRAFFIC AND PREFILL DELAY"}
    }
]
