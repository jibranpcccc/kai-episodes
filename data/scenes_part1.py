# -*- coding: utf-8 -*-
"""
Scenes 1-24 authoritative visual definitions.
"""

SCENES_1_24 = [
    # Scene 1 (hook)
    {
        "layout": "hook",
        "title": "THE 128,000 TOKEN PROMISE",
        "header_at": "You download a local",
        "art": "context_window",
        "art_at": "promises a context window",
        "art_caption": "ADVERTISED SEQUENCE CAPACITY",
        "chips": [
            {"at": "one hundred and twenty-eight thousand tokens", "c": "cyan", "t": "128K SEQUENCE SPEC"},
            {"at": "That sounds enormous", "c": "hot", "t": "MASSIVE PROMISE"}
        ],
        "stats": [
            {"at": "one hundred and twenty-eight thousand tokens", "c": "cyan", "lab": "ADVERTISED LIMIT", "u": "TOKENS", "v": "128,000"},
            {"at": "That sounds enormous", "c": "gold", "lab": "PERCEIVED CAPACITY", "u": "PROMISE", "v": "ENORMOUS"}
        ],
        "closing": {"at": "That sounds enormous", "c": "gold", "t": "ADVERTISED CAPACITY IS NOT ALLOCATED MEMORY"}
    },
    # Scene 2 (rows)
    {
        "layout": "rows",
        "title": "WHAT 128K PROMISES",
        "header_at": "Enough for a long",
        "art": "folder",
        "art_at": "mountain of code",
        "art_caption": "PROMISED WORKLOAD HORIZONS",
        "rows": [
            {"at": "long report", "cls": "cyan", "name": "LONG REPORT", "rank": "01", "sub": "300+ PAGES", "val": "ANALYSIS"},
            {"at": "mountain of code", "cls": "gold", "name": "MOUNTAIN OF CODE", "rank": "02", "sub": "MULTI-FILE LOGIC", "val": "REPO"},
            {"at": "conversation that never seems to end", "cls": "hot", "name": "ENDLESS CHAT", "rank": "03", "sub": "MULTI-TURN HISTORY", "val": "INFINITE"}
        ],
        "closing": {"at": "paste in a document", "c": "hot", "t": "REAL DATA TRIGGERS THE BOTTLENECK"}
    },
    # Scene 3 (bars)
    {
        "layout": "bars",
        "title": "THE THREE FAILURE MODES",
        "header_at": "Your GPU memory fills",
        "art": "warning",
        "art_at": "GPU memory fills up",
        "art_caption": "THREE HARDWARE & QUALITY BREAKDOWNS",
        "bars": [
            {"at": "GPU memory fills up", "cls": "hot", "lab": "VRAM EXHAUSTION", "pct": 100.0, "unit": "MEMORY", "val": "OOM CRASH"},
            {"at": "first answer takes forever", "cls": "gold", "lab": "FIRST TOKEN DELAY", "pct": 85.0, "unit": "LATENCY", "val": "TIMEOUT"},
            {"at": "confidently misses a detail", "cls": "red", "lab": "ATTENTION FAILURE", "pct": 40.0, "unit": "ACCURACY", "val": "LOST DETAIL"}
        ],
        "closing": {"at": "sitting right there in the text", "c": "gold", "t": "FITTING TOKENS DOES NOT GUARANTEE RECALL"}
    },
    # Scene 4 (rail)
    {
        "layout": "rail",
        "title": "THE ADVERTISED CONTEXT TRAP",
        "header_at": "What happened to those",
        "art": "scales",
        "art_at": "Here is the trap",
        "art_caption": "ADVERTISED SPECIFICATION VS LOCAL RUNTIME",
        "rails": [
            {"at": "one hundred and twenty-eight thousand tokens", "cls": "cyan", "lab": "SPECIFICATION", "val": "128,000 TOKENS"},
            {"at": "run that window efficiently", "cls": "hot", "lab": "SYSTEM REALITY", "val": "INEFFICIENT EXECUTION"}
        ],
        "closing": {"at": "run that window efficiently", "c": "gold", "t": "ADVERTISED SPECIFICATION IS NOT SYSTEM CAPABILITY"}
    },
    # Scene 5 (chain)
    {
        "layout": "chain",
        "title": "CAPACITY IS NOT ACCURACY",
        "header_at": "And even when the",
        "art": "collapse",
        "art_at": "does not guarantee",
        "art_caption": "ATTENTION ACCURACY AT SCALE",
        "chain": [
            {"at": "when the text fits", "t": "1. PHYSICAL STORAGE", "s": "TOKENS FIT IN VRAM"},
            {"at": "does not guarantee", "t": "2. ATTENTION WEIGHTS", "s": "COMPUTE DISTRIBUTION"},
            {"at": "use every part of it correctly", "t": "3. ACCURATE EXTRACTION", "s": "EFFECTIVE RECALL"}
        ],
        "compare": [
            {"at": "when the text fits", "cls": "dim", "title": "PHYSICAL FIT", "body": "VRAM STORES TOKENS"},
            {"at": "use every part of it correctly", "cls": "gold", "title": "EFFECTIVE RECALL", "body": "MODEL EXTRACTS FACT"}
        ],
        "closing": {"at": "use every part of it correctly", "c": "gold", "t": "STORAGE CAPACITY IS NOT RECALL ACCURACY"}
    },
    # Scene 6 (note)
    {
        "layout": "note",
        "title": "TRACING THE LONG PROMPT",
        "header_at": "Today we are following",
        "art": "pipeline",
        "art_at": "following one long prompt",
        "art_caption": "END-TO-END EXECUTION AUDIT",
        "note_head": "THE THREE AUDIT CHOKEPOINTS",
        "note_items": [
            {"at": "model specification", "t": "PUBLISHED MODEL SPECIFICATION & ROPE LIMITS"},
            {"at": "GPU memory", "t": "PHYSICAL VRAM ALLOCATION & KV CACHE FOOTPRINT"},
            {"at": "all the way to the answer", "t": "PREFILL LATENCY & AUTOREGRESSIVE DECODING SPEED"}
        ],
        "closing": {"at": "all the way to the answer", "c": "gold", "t": "FOLLOWING THE DATA FROM PROMPT TO ANSWER"}
    },
    # Scene 7 (strip)
    {
        "layout": "strip",
        "title": "CONTEXT IS NOT PERMANENT MEMORY",
        "header_at": "We will find out",
        "art": "two_die",
        "art_at": "forget the idea",
        "art_caption": "WORKING STATE VS PERSISTENT STORAGE",
        "items": [
            {"at": "what actually runs out", "key": "ram_stick", "label": "VRAM EXHAUSTION", "sub": "PHYSICAL MEMORY BOUND"},
            {"at": "why long conversations slow down", "key": "clock", "label": "LATENCY SPIKE", "sub": "PREFILL QUADRATIC COST"},
            {"at": "context is permanent memory", "key": "folder", "label": "TRANSIENT BUFFER", "sub": "NOT PERMANENT DISK STORAGE"}
        ],
        "closing": {"at": "context is permanent memory", "c": "hot", "t": "CONTEXT DIES WITH THE INFERENCE SESSION"}
    },
    # Scene 8 (nodes)
    {
        "layout": "nodes",
        "title": "WHAT FILLS THE CONTEXT WINDOW",
        "header_at": "A context window is",
        "art": "prompt_stream",
        "art_at": "instructions, prior messages",
        "art_caption": "FIVE WORKING STATE COMPONENTS",
        "chain": [
            {"at": "working information made available", "c": "cyan", "t": "WORKING STATE", "s": "GENERATION SCRATCHPAD"},
            {"at": "instructions, prior messages", "c": "gold", "t": "SYSTEM & CHAT", "s": "PROMPTS & TOOL RESULTS"},
            {"at": "beginning of the model's own response", "c": "hot", "t": "GENERATED OUTPUT", "s": "AUTOREGRESSIVE TOKENS"}
        ],
        "closing": {"at": "model's own response", "c": "gold", "t": "EVERY COMPONENT COMPETES FOR THE SAME WINDOW"}
    },
    # Scene 9 (hook)
    {
        "layout": "hook",
        "title": "A TOKEN IS NOT A WORD",
        "header_at": "A token is not",
        "art": "chip",
        "art_at": "Depending on the tokenizer",
        "art_caption": "TOKENIZER FRAGMENTATION DYNAMICS",
        "chips": [
            {"at": "not necessarily one word", "c": "cyan", "t": "WORD != TOKEN"},
            {"at": "special chat markers", "c": "hot", "t": "SYNTAX & OVERHEAD"}
        ],
        "stats": [
            {"at": "word can be one token", "c": "cyan", "lab": "SIMPLE WORD", "u": "TOKEN", "v": "1"},
            {"at": "several tokens", "c": "gold", "lab": "COMPLEX / CODE", "u": "TOKENS", "v": "2-4"}
        ],
        "closing": {"at": "formatting also count", "c": "gold", "t": "TOKENIZATION EXPANDS TEXT BEYOND WORD COUNTS"}
    },
    # Scene 10 (rows)
    {
        "layout": "rows",
        "title": "THE PAGE COUNT ILLUSION",
        "header_at": "So a one-hundred-page document",
        "art": "folder",
        "art_at": "one-hundred-page document",
        "art_caption": "PAGE COUNT ESTIMATE VS TOKEN REALITY",
        "rows": [
            {"at": "one-hundred-page document", "cls": "cyan", "name": "100-PAGE DOC", "rank": "01", "sub": "PAGE HEURISTIC", "val": "UNRELIABLE"},
            {"at": "reliable token count", "cls": "gold", "name": "RAW TOKENS", "rank": "02", "sub": "CODE / FORMATTING", "val": "HIGH VARIANCE"},
            {"at": "not always yours to spend", "cls": "hot", "name": "INPUT BUDGET", "rank": "03", "sub": "SHARED ALLOWANCE", "val": "CONSTRAINED"}
        ],
        "closing": {"at": "spend on the input", "c": "hot", "t": "PAGE COUNT IS A DANGEROUS TOKEN PROXY"}
    },
    # Scene 11 (bars)
    {
        "layout": "bars",
        "title": "PROMPT VS GENERATION BUDGET",
        "header_at": "In many runtimes, prompt",
        "art": "scales",
        "art_at": "prompt tokens and generated tokens",
        "art_caption": "SHARED CONFIGURED CONTEXT CEILING",
        "bars": [
            {"at": "share the configured context limit", "cls": "cyan", "lab": "INPUT PROMPT", "pct": 80.0, "unit": "TOKENS", "val": "SOURCE"},
            {"at": "leave no room for the answer", "cls": "hot", "lab": "OUTPUT ROOM", "pct": 20.0, "unit": "TOKENS", "val": "NO ANSWER"}
        ],
        "closing": {"at": "no room for the answer", "c": "gold", "t": "INPUT MATERIAL SQUEEZES OUT THE ANSWER SPACE"}
    },
    # Scene 12 (rail)
    {
        "layout": "rail",
        "title": "APPLICATION OUTPUT CEILINGS",
        "header_at": "Separate model or application",
        "art": "context_window",
        "art_at": "Separate model or application output",
        "art_caption": "INDEPENDENT MAX TOKEN BOUNDARIES",
        "rails": [
            {"at": "Separate model or application output", "cls": "hot", "lab": "OUTPUT LIMIT", "val": "MAX TOKENS CAP"},
            {"at": "one-hundred-and-twenty-eight-thousand-token budget", "cls": "cyan", "lab": "TOTAL BUDGET", "val": "128,000 TOKENS"}
        ],
        "closing": {"at": "one-hundred-and-twenty-eight-thousand-token budget", "c": "gold", "t": "APPLICATION LIMITS RESTRICT TOTAL GENERATION"}
    },
    # Scene 13 (chain)
    {
        "layout": "chain",
        "title": "LEAVING ROOM FOR THE ANSWER",
        "header_at": "If you want the",
        "art": "checklist",
        "art_at": "generate eight thousand tokens",
        "art_caption": "RESERVING OUTPUT & SYSTEM OVERHEAD",
        "chain": [
            {"at": "generate eight thousand tokens", "t": "1. GENERATION SPACE", "s": "8,000 OUTPUT TOKENS"},
            {"at": "system prompts", "t": "2. SYSTEM INSTRUCTIONS", "s": "SYSTEM & CHAT TEMPLATES"},
            {"at": "other overhead", "t": "3. PROTOCOL OVERHEAD", "s": "TOOL CALLS & MARKERS"}
        ],
        "compare": [
            {"at": "generate eight thousand tokens", "cls": "gold", "title": "RESERVED OUTPUT", "body": "8,000 TOKENS"},
            {"at": "other overhead", "cls": "dim", "title": "SYSTEM OVERHEAD", "body": "DYNAMIC PADDING"}
        ],
        "closing": {"at": "other overhead", "c": "gold", "t": "ALWAYS RESERVE SPACE BEFORE PASTING DOCUMENTS"}
    },
    # Scene 14 (note)
    {
        "layout": "note",
        "title": "THE FOUR SEPARATE LIMITS",
        "header_at": "One hundred and twenty-eight",
        "art": "warning",
        "art_at": "first of four separate limits",
        "art_caption": "FOUR INDEPENDENT ARCHITECTURAL GATES",
        "note_head": "THE FOUR CONTEXT BOUNDARIES",
        "note_items": [
            {"at": "ceiling, not a promise", "t": "128K IS A CEILING · NOT AN UNCONDITIONAL PROMISE"},
            {"at": "receive a full response", "t": "PASTING 128K PREVENTS ANSWER GENERATION"},
            {"at": "first of four separate limits", "t": "SYSTEM DEPENDS ON 4 INDEPENDENT GATES"}
        ],
        "closing": {"at": "first of four separate limits", "c": "gold", "t": "THE FOUR SEPARATE LIMITS FRAMEWORK"}
    },
    # Scene 15 (strip)
    {
        "layout": "strip",
        "title": "LIMIT 1: THE MODEL ARCHITECTURE",
        "header_at": "The model itself has",
        "art": "model_file",
        "art_at": "supported context configuration",
        "art_caption": "PUBLISHED MODEL ARCHITECTURE & ROPE SETUP",
        "items": [
            {"at": "supported context configuration", "key": "model_file", "label": "MODEL CONFIG", "sub": "CONFIG.JSON LIMIT"},
            {"at": "training setup", "key": "chip", "label": "TRAINING LENGTH", "sub": "PRETRAINED ROPE BASE"},
            {"at": "longer sequences than others", "key": "context_window", "label": "EXTENDED ROPE", "sub": "ADAPTED SEQUENCES"}
        ],
        "closing": {"at": "longer sequences than others", "c": "gold", "t": "MODELS CANNOT EXCEED THEIR ROPE ARCHITECTURE"}
    },
    # Scene 16 (nodes)
    {
        "layout": "nodes",
        "title": "LIMIT 2: RUNTIME SOFTWARE",
        "header_at": "The second limit belongs",
        "art": "laptop",
        "art_at": "software running the model",
        "art_caption": "RUNTIME ENGINE CONTEXT CLAMPING",
        "chain": [
            {"at": "software running the model", "c": "cyan", "t": "INFERENCE ENGINE", "s": "LLAMA.CPP / VLLM / OLLAMA"},
            {"at": "smaller active context", "c": "hot", "t": "ACTIVE CLAMP", "s": "SOFTWARE DOWN-SIZING"},
            {"at": "published maximum", "c": "gold", "t": "PUBLISHED MAX", "s": "IGNORED BY DEFAULT CONFIG"}
        ],
        "closing": {"at": "published maximum", "c": "gold", "t": "LOCAL APPLICATIONS CLAMP ACTIVE CONTEXT SIZES"}
    },
    # Scene 17 (hook)
    {
        "layout": "hook",
        "title": "CONFIGURED CLI ENGINE FLAGS",
        "header_at": "Changing the model file",
        "art": "checklist",
        "art_at": "llama.cpp exposes a context-size",
        "art_caption": "EXPLICIT ENGINE CONTEXT SETTINGS",
        "chips": [
            {"at": "llama.cpp exposes a context-size", "c": "cyan", "t": "LLAMA.CPP: -C FLAG"},
            {"at": "vLLM exposes a maximum model", "c": "gold", "t": "VLLM: --MAX-MODEL-LEN"}
        ],
        "stats": [
            {"at": "llama.cpp exposes a context-size", "c": "cyan", "lab": "LLAMA.CPP CLI", "u": "FLAG", "v": "-c"},
            {"at": "vLLM exposes a maximum model", "c": "gold", "lab": "VLLM CLI", "u": "PARAM", "v": "--max-len"}
        ],
        "closing": {"at": "maximum model length setting", "c": "gold", "t": "MODEL FILES DO NOT OVERRIDE RUNTIME CLI FLAGS"}
    },
    # Scene 18 (rows)
    {
        "layout": "rows",
        "title": "BACKEND MEMORY CONSTRAINTS",
        "header_at": "Both also have other",
        "art": "motherboard",
        "art_at": "configuration and memory constraints",
        "art_caption": "VERSION & BACKEND EXECUTION CONSTRAINTS",
        "rows": [
            {"at": "memory constraints", "cls": "hot", "name": "MEMORY LIMITS", "rank": "01", "sub": "VRAM ALLOCATOR RULES", "val": "BOUNDED"},
            {"at": "exact command names", "cls": "gold", "name": "BACKEND FLAGS", "rank": "02", "sub": "VERSION SPECIFIC", "val": "DIVERGENT"},
            {"at": "backend you are running", "cls": "cyan", "name": "ACTIVE BACKEND", "rank": "03", "sub": "CUDA / METAL / ROCM", "val": "DRIVER"}
        ],
        "closing": {"at": "backend you are running", "c": "gold", "t": "COMMAND FLAGS VARY BY INFERENCE BACKEND"}
    },
    # Scene 19 (bars)
    {
        "layout": "bars",
        "title": "LIMIT 3: PHYSICAL MEMORY",
        "header_at": "The important point is",
        "art": "vram_module",
        "art_at": "third limit is physical memory",
        "art_caption": "WEIGHTS VS ACTIVE EXECUTION MEMORY",
        "bars": [
            {"at": "advertised model limit and the configured", "cls": "cyan", "lab": "RUNTIME LIMIT", "pct": 50.0, "unit": "CONFIG", "val": "DIFFERENT"},
            {"at": "model weights", "cls": "gold", "lab": "STATIC WEIGHTS", "pct": 70.0, "unit": "VRAM", "val": "GGUF FILE"},
            {"at": "file you downloaded", "cls": "hot", "lab": "ACTIVE EXECUTION", "pct": 95.0, "unit": "VRAM", "val": "EXTRA STATE"}
        ],
        "closing": {"at": "file you downloaded", "c": "gold", "t": "RUNNING CONTEXT REQUIRES MORE THAN MODEL WEIGHTS"}
    },
    # Scene 20 (rail)
    {
        "layout": "rail",
        "title": "ENTER THE KEY-VALUE CACHE",
        "header_at": "The memory needed while",
        "art": "kv_cache",
        "art_at": "key-value cache enters the story",
        "art_caption": "TRANSFORMER ATTENTION KEYS & VALUES",
        "rails": [
            {"at": "reads and generates", "cls": "cyan", "lab": "DYNAMIC MEMORY", "val": "READ & GENERATE"},
            {"at": "representations called keys and values", "cls": "gold", "lab": "KV TENSORS", "val": "KEYS & VALUES"}
        ],
        "closing": {"at": "representations called keys and values", "c": "gold", "t": "ATTENTION LAYERS CALCULATE AND STORE KV TENSORS"}
    },
    # Scene 21 (chain)
    {
        "layout": "chain",
        "title": "AVOIDING RECOMPUTATION",
        "header_at": "During autoregressive generation, a",
        "art": "clock",
        "art_at": "recompute the entire past",
        "art_caption": "AUTOREGRESSIVE STATE CACHING",
        "chain": [
            {"at": "autoregressive generation", "t": "1. AUTOREGRESSIVE STEP", "s": "PREDICT TOKEN BY TOKEN"},
            {"at": "saves those representations", "t": "2. SAVE KV STATES", "s": "REUSE PRIOR COMPUTATION"},
            {"at": "recompute the entire past", "t": "3. AVOID RECOMPUTE", "s": "O(1) PER STEP INSTEAD OF O(N)"}
        ],
        "compare": [
            {"at": "saves those representations", "cls": "gold", "title": "CACHED ATTENTION", "body": "REUSE SAVED KV"},
            {"at": "recompute the entire past", "cls": "dim", "title": "NAIVE PASS", "body": "RECOMPUTE ALL PAST"}
        ],
        "closing": {"at": "for every new token", "c": "gold", "t": "KV CACHE EXCHANGES VRAM TO SAVE MASSIVE COMPUTE"}
    },
    # Scene 22 (note)
    {
        "layout": "note",
        "title": "MACHINERY VS WORKING NOTES",
        "header_at": "Think of it as",
        "art": "two_die",
        "art_at": "model weights are the machinery",
        "art_caption": "STATIC WEIGHTS VS DYNAMIC CONVERSATION STATE",
        "note_head": "THE MACHINERY ANALOGY",
        "note_items": [
            {"at": "growing set of working notes", "t": "KV CACHE = GROWING STACK OF SCRATCHPAD NOTES"},
            {"at": "model weights are the machinery", "t": "MODEL WEIGHTS = FIXED HARDWARE MACHINERY"}
        ],
        "closing": {"at": "model weights are the machinery", "c": "gold", "t": "MACHINERY IS STATIC · WORKING NOTES GROW EVERY TOKEN"}
    },
    # Scene 23 (strip)
    {
        "layout": "strip",
        "title": "LONGER SEQUENCES GROW CACHE",
        "header_at": "The key-value cache is",
        "art": "cache_grid",
        "art_at": "longer sequences need more stored",
        "art_caption": "FULL-ATTENTION CONVENTIONAL CACHE GROWTH",
        "items": [
            {"at": "temporary state", "key": "chip", "label": "TEMP STATE", "sub": "CONVERSATION TRACKING"},
            {"at": "full-attention transformer", "key": "kv_cache", "label": "FULL ATTENTION", "sub": "STANDARD ARCHITECTURE"},
            {"at": "more stored key and value data", "key": "ram_stick", "label": "CACHE FOOTPRINT", "sub": "LINEAR TOKENS GROWTH"}
        ],
        "closing": {"at": "more stored key and value data", "c": "gold", "t": "FULL-ATTENTION CACHE SCALES WITH SEQUENCE LENGTH"}
    },
    # Scene 24 (nodes)
    {
        "layout": "nodes",
        "title": "KV CACHE SCALING VARIABLES",
        "header_at": "Cache memory scales with",
        "art": "checklist",
        "art_at": "storage precision, and with how many",
        "art_caption": "THE SIX KV CACHE FOOTPRINT MULTIPLIERS",
        "chain": [
            {"at": "scales with token count", "c": "cyan", "t": "TOKENS & LAYERS", "s": "2 * LAYERS * TOKENS"},
            {"at": "key-value heads and their dimensions", "c": "gold", "t": "HEADS * HEAD DIM", "s": "KV HEADS * 128 DIM"},
            {"at": "storage precision", "c": "hot", "t": "PRECISION * BATCH", "s": "BYTES PER VAL * STREAMS"}
        ],
        "closing": {"at": "how many sequences are being served", "c": "gold", "t": "KV CACHE SCALES ACROSS SIX INDEPENDENT VARIABLES"}
    }
]
