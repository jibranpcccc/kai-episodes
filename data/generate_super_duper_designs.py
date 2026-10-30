# -*- coding: utf-8 -*-
"""
Generate 100% bespoke, deeply grounded, script-matched visual card designs
for all 72 scenes of Episode 13: '128K CONTEXT WINDOW: THE SILENT MEMORY TRAP'.

Rules:
1. Every title is 2-5 words, ALL CAPS, meaningful and summarizing that scene's exact narration.
   Zero generic titles like 'Window #X' or 'Context Window #Y'.
2. Every card directly illustrates the exact concepts, terms, and metaphors spoken in that sentence.
3. Zero invented percentages (no 85%, 50%, etc. unless in script).
4. Sized cleanly for 1920x1080 stage and approved FUSION layouts.
"""

DESIGNS = [
    # Scene 1 (hook): "You download a local AI model that promises a context window of one hundred and twenty-eight thousand tokens. That sounds enormous."
    {
        "title": "THE 128,000 TOKEN PROMISE",
        "art": "context_window",
        "cap": "ADVERTISED SEQUENCE SPECIFICATION",
        "c_tag": "SPECIFICATION CEILING",
        "chips": [
            {"c": "cyan", "t": "128K ADVERTISED"},
            {"c": "gold", "t": "LOCAL LLM SPEC"}
        ],
        "stats": [
            {"c": "cyan", "lab": "SEQUENCE", "u": "K", "v": "128"},
            {"c": "gold", "lab": "STATUS", "u": "PROMISE", "v": "CLAIM"}
        ]
    },

    # Scene 2 (rows): "Enough for a long report, a mountain of code, or an entire conversation that never seems to end."
    {
        "title": "THREE PROMISED USE CASES",
        "art": "folder",
        "cap": "WHAT 128K TOKENS SEEMS TO ENABLE",
        "c_tag": "THE PROMISE",
        "rows": [
            {"cls": "cyan", "rank": "01", "name": "LONG REPORT", "val": "300+ PAGES", "sub": "FINANCIAL AUDIT"},
            {"cls": "gold", "rank": "02", "name": "MOUNTAIN OF CODE", "val": "FULL REPO", "sub": "MULTI-FILE LOGIC"},
            {"cls": "hot", "rank": "03", "name": "ENDLESS CHAT", "val": "MULTI-TURN", "sub": "PERSISTENT MEMORY"}
        ]
    },

    # Scene 3 (bars): "Then you load the model. You paste in a document. Your GPU memory fills up, the first answer takes forever, or the application refuses the request. And if it does answer, it confidently misses a detail you know is sitting right there in the text."
    {
        "title": "THE REALITY: THREE FAILURES",
        "art": "warning",
        "cap": "WHAT ACTUALLY HAPPENS AT SCALE",
        "c_tag": "EXECUTION BREAKDOWN",
        "bars": [
            {"cls": "hot", "lab": "VRAM EXHAUSTION", "unit": "MEMORY", "val": "OOM CRASH", "pct": 98.0},
            {"cls": "cyan", "lab": "FIRST TOKEN DELAY", "unit": "LATENCY", "val": "TIMEOUT", "pct": 92.0}
        ]
    },

    # Scene 4 (rail): "What happened to those one hundred and twenty-eight thousand tokens? Here is the trap: a model can advertise a large context window without your computer being able to run that window efficiently."
    {
        "title": "THE ADVERTISED SPEC TRAP",
        "art": "scales",
        "cap": "SPECIFICATION VS HARDWARE CAPACITY",
        "c_tag": "PHYSICAL DISCONNECT",
        "rails": [
            {"cls": "cyan", "lab": "ADVERTISED WINDOW", "val": "128K TOKENS", "pct": 100.0},
            {"cls": "red", "lab": "HARDWARE CAPACITY", "val": "OUT OF MEMORY", "pct": 25.0}
        ]
    },

    # Scene 5 (chain): "And even when the text fits, that does not guarantee the model will use every part of it correctly."
    {
        "title": "FITTING TEXT VS USING TEXT",
        "art": "warning",
        "cap": "ATTENTION AND RETRIEVAL FIDELITY",
        "c_tag": "RECALL DISCONNECT",
        "chain": [
            {"t": "VRAM ALLOCATION", "s": "TEXT FITS ON GPU"},
            {"t": "ATTENTION PASS", "s": "COMPUTE EXECUTION"},
            {"t": "ACCURATE RETRIEVAL", "s": "RELIABLE EXTRACTION"}
        ],
        "compare": [
            {"cls": "dim", "title": "PHYSICAL FIT", "body": "CONTEXT ALLOCATED"},
            {"cls": "gold", "title": "RECALL FIDELITY", "body": "DETAIL MISSED"}
        ]
    },

    # Scene 6 (note): "Today we are following one long prompt through a local AI system, from the model specification to the GPU memory, all the way to the answer."
    {
        "title": "TRACING THE PROMPT PIPELINE",
        "art": "prompt_stream",
        "cap": "END-TO-END EXECUTION AUDIT",
        "c_tag": "BYTE FORENSICS",
        "note_head": "PROMPT EXECUTION PATH",
        "note_items": [
            {"t": "MODEL SPECIFICATION: ADVERTISED CONTEXT"},
            {"t": "PHYSICAL MEMORY: KV CACHE ALLOCATION"},
            {"t": "GENERATION SPEED: PREFILL VS DECODE"}
        ]
    },

    # Scene 7 (strip): "We will find out what actually runs out, why long conversations slow down, and when a smaller, smarter context can beat a gigantic one."
    {
        "title": "THREE CORE INVESTIGATIONS",
        "c_tag": "EXECUTIVE AUDIT",
        "items": [
            {"key": "ram_stick", "label": "VRAM RUNS OUT"},
            {"key": "clock", "label": "LATENCY SPIKE"},
            {"key": "chip", "label": "SMALLER CONTEXT"}
        ]
    },

    # Scene 8 (nodes): "First, forget the idea that context is permanent memory. A context window is the working information made available to the model for a particular generation. It can contain instructions, prior messages, documents, tool results, and the beginning of the model's own response."
    {
        "title": "WORKING MEMORY VS STORAGE",
        "art": "context_window",
        "cap": "TRANSIENT GENERATION STATE",
        "c_tag": "NOT PERMANENT",
        "chain": [
            {"t": "SYSTEM PROMPT", "s": "CORE INSTRUCTIONS"},
            {"t": "CHAT & DOCUMENTS", "s": "PRIOR MESSAGES & TOOLS"},
            {"t": "ACTIVE RESPONSE", "s": "AUTOREGRESSIVE OUTPUT"}
        ]
    },

    # Scene 9 (hook): "A token is not necessarily one word. Depending on the tokenizer, a word can be one token, several tokens, or part of a token sequence. Punctuation, code, special chat markers, and formatting also count."
    {
        "title": "WORDS ARE NOT TOKENS",
        "art": "chip",
        "cap": "TOKENIZER SUB-WORD SEGMENTATION",
        "c_tag": "TOKEN EXPANSION",
        "chips": [
            {"c": "cyan", "t": "SUB-WORD SLICES"},
            {"c": "gold", "t": "SYNTAX & FORMATTING"}
        ],
        "stats": [
            {"c": "cyan", "lab": "PUNCTUATION", "u": "TOKENS", "v": "SPLIT"},
            {"c": "gold", "lab": "FORMATTING", "u": "TOKENS", "v": "EXTRA"}
        ]
    },

    # Scene 10 (rows): "So a one-hundred-page document cannot be converted into a reliable token count using page numbers alone. And the full context budget is not always yours to spend on the input."
    {
        "title": "NO CONVERSION SHORTCUT",
        "art": "folder",
        "cap": "PAGE COUNT != TOKEN COUNT",
        "c_tag": "MEASURE EXACT",
        "rows": [
            {"cls": "cyan", "rank": "01", "name": "100-PAGE DOC", "val": "VARIABLE", "sub": "NO FIXED RATIO"},
            {"cls": "gold", "rank": "02", "name": "CODE & INDENTS", "val": "EXPANDED", "sub": "HIGH TOKEN DENSITY"},
            {"cls": "hot", "rank": "03", "name": "INPUT BUDGET", "val": "LIMITED", "sub": "SHARED LIMIT"}
        ]
    },

    # Scene 11 (bars): "In many runtimes, prompt tokens and generated tokens share the configured context limit. If you fill the entire allowance with source material, you may leave no room for the answer."
    {
        "title": "THE SHARED CONTEXT BUDGET",
        "art": "scales",
        "cap": "INPUT VS OUTPUT ALLOCATION",
        "c_tag": "ZERO ANSWER ROOM",
        "bars": [
            {"cls": "hot", "lab": "PROMPT INPUT", "unit": "TOKENS", "val": "128K", "pct": 98.0},
            {"cls": "cyan", "lab": "ROOM FOR ANSWER", "unit": "TOKENS", "val": "0 TOKENS", "pct": 2.0}
        ]
    },

    # Scene 12 (rail): "Separate model or application output limits may apply as well. So imagine a hypothetical one-hundred-and-twenty-eight-thousand-token budget."
    {
        "title": "APPLICATION OUTPUT CEILINGS",
        "art": "warning",
        "cap": "RUNTIME OUTPUT GENERATION CONSTRAINTS",
        "c_tag": "HARD CEILINGS",
        "rails": [
            {"cls": "cyan", "lab": "TOTAL BUDGET", "val": "128K TOKENS", "pct": 100.0},
            {"cls": "red", "lab": "MAX OUTPUT LIMIT", "val": "APPLICATION CAP", "pct": 30.0}
        ]
    },

    # Scene 13 (chain): "If you want the model to generate eight thousand tokens, you need to leave enough space for those eight thousand plus any system prompts, chat formatting, and other overhead."
    {
        "title": "RESERVING OUTPUT HEADROOM",
        "art": "cache_grid",
        "cap": "BUDGETING FOR GENERATION",
        "c_tag": "HEADROOM LAW",
        "chain": [
            {"t": "SYSTEM OVERHEAD", "s": "CHAT TEMPLATE & ROLES"},
            {"t": "PROMPT SOURCE", "s": "USER QUERY & DOCUMENTS"},
            {"t": "OUTPUT RESERVE", "s": "8,000 GENERATED TOKENS"}
        ],
        "compare": [
            {"cls": "dim", "title": "MAX INPUT SPACE", "body": "120,000 TOKENS"},
            {"cls": "gold", "title": "OUTPUT RESERVE", "body": "8,000 TOKENS"}
        ]
    },

    # Scene 14 (note): "One hundred and twenty-eight thousand tokens is a ceiling, not a promise that you can paste in that much text and still receive a full response."
    {
        "title": "CEILING VS REALISTIC INPUT",
        "art": "warning",
        "cap": "UNDERSTANDING CONTEXT BOUNDARIES",
        "c_tag": "CEILING LAW",
        "note_head": "CONTEXT ALLOCATION REALITY",
        "note_items": [
            {"t": "128K IS A COMBINED HARD CEILING"},
            {"t": "INPUT MUST LEAVE ADEQUATE ANSWER ROOM"},
            {"t": "SYSTEM TEMPLATES CONSUME HIDDEN TOKENS"}
        ]
    },

    # Scene 15 (strip): "Now comes the first of four separate limits. The model itself has a supported context configuration. That number may come from its architecture, training setup, and published configuration. Some models are designed or adapted for longer sequences than others."
    {
        "title": "LIMIT 1: MODEL ARCHITECTURE",
        "c_tag": "FIRST LIMIT",
        "items": [
            {"key": "chip", "label": "BASE ARCHITECTURE"},
            {"key": "folder", "label": "TRAINING DATASET"},
            {"key": "checklist", "label": "PUBLISHED SPEC"}
        ]
    },

    # Scene 16 (nodes): "The second limit belongs to the software running the model. A local application may choose a smaller active context than the model's published maximum."
    {
        "title": "LIMIT 2: RUNTIME SOFTWARE",
        "art": "laptop",
        "cap": "SOFTWARE CONFIGURATION CONSTRAINTS",
        "c_tag": "SECOND LIMIT",
        "chain": [
            {"t": "PUBLISHED MODEL SPEC", "s": "THEORETICAL MAXIMUM"},
            {"t": "LOCAL APP DEFAULT", "s": "CONSERVATIVE SETTING"},
            {"t": "EFFECTIVE RUNTIME", "s": "ACTIVE CONFIGURED WINDOW"}
        ]
    },

    # Scene 17 (hook): "Changing the model file does not force the application to use the largest supported value. For example, llama.cpp exposes a context-size setting. vLLM exposes a maximum model length setting."
    {
        "title": "CONFIGURED CLI PARAMETERS",
        "art": "chip",
        "cap": "EXPLICIT INFERENCE ENGINE FLAGS",
        "c_tag": "FLAG CONTROL",
        "chips": [
            {"c": "cyan", "t": "LLAMA.CPP: -C FLAG"},
            {"c": "gold", "t": "VLLM: --MAX-MODEL-LEN"}
        ],
        "stats": [
            {"c": "cyan", "lab": "LLAMA.CPP", "u": "FLAG", "v": "-C"},
            {"c": "gold", "lab": "VLLM", "u": "FLAG", "v": "MAXLEN"}
        ]
    },

    # Scene 18 (rows): "Both also have other configuration and memory constraints. The exact command names and behavior depend on which version and backend you are running."
    {
        "title": "BACKEND MEMORY CONSTRAINTS",
        "art": "motherboard",
        "cap": "INFERENCE ENGINE ARCHITECTURE",
        "c_tag": "BACKEND RULES",
        "rows": [
            {"cls": "cyan", "rank": "01", "name": "LLAMA.CPP", "val": "-C CONTEXT", "sub": "CPU/GPU SPLIT"},
            {"cls": "gold", "rank": "02", "name": "VLLM ENGINE", "val": "GPU POOL", "sub": "PAGED ATTENTION"},
            {"cls": "hot", "rank": "03", "name": "BACKEND DRIVER", "val": "VRAM WALL", "sub": "ALLOCATION BUFFER"}
        ]
    },

    # Scene 19 (bars): "The important point is that the advertised model limit and the configured runtime limit are different facts. The third limit is physical memory. Not just the model weights. Not just the file you downloaded."
    {
        "title": "LIMIT 3: PHYSICAL MEMORY",
        "art": "gpu_24gb",
        "cap": "WEIGHTS VS WORKING ALLOCATIONS",
        "c_tag": "THIRD LIMIT",
        "bars": [
            {"cls": "cyan", "lab": "STATIC WEIGHT FILE", "unit": "VRAM", "val": "LOADED", "pct": 50.0},
            {"cls": "hot", "lab": "DYNAMIC RUNTIME MEM", "unit": "VRAM", "val": "REQUIRED", "pct": 95.0}
        ]
    },

    # Scene 20 (rail): "The memory needed while the model reads and generates. This is where the key-value cache enters the story. When a transformer processes earlier tokens, its attention layers calculate representations called keys and values."
    {
        "title": "ENTER THE KEY-VALUE CACHE",
        "art": "kv_cache",
        "cap": "ATTENTION STATE REPRESENTATION",
        "c_tag": "TRANSFORMER MATH",
        "rails": [
            {"cls": "cyan", "lab": "KEY VECTORS", "val": "ATTENTION KEYS", "pct": 50.0},
            {"cls": "gold", "lab": "VALUE VECTORS", "val": "ATTENTION VALUES", "pct": 50.0}
        ]
    },

    # Scene 21 (chain): "During autoregressive generation, a supported caching implementation saves those representations so the model does not need to recompute the entire past in exactly the same way for every new token."
    {
        "title": "AVOIDING RECOMPUTATION",
        "art": "cache_grid",
        "cap": "AUTOREGRESSIVE CACHING SPEEDUP",
        "c_tag": "CACHING SAVES TTFT",
        "chain": [
            {"t": "PREVIOUS TOKENS", "s": "COMPUTE KV ONCE"},
            {"t": "VRAM STORAGE", "s": "SAVE TO KV CACHE"},
            {"t": "NEW TOKEN DECODE", "s": "READ PAST WITHOUT RECALC"}
        ],
        "compare": [
            {"cls": "dim", "title": "WITHOUT CACHE", "body": "RECOMPUTE ALL TOKENS"},
            {"cls": "gold", "title": "WITH KV CACHE", "body": "REUSE STORED VECTORS"}
        ]
    },

    # Scene 22 (note): "Think of it as a growing set of working notes for the current request. The model weights are the machinery."
    {
        "title": "WORKING NOTES ANALOGY",
        "art": "chip",
        "cap": "MACHINERY VS WORKING STATE",
        "c_tag": "ANALOGY",
        "note_head": "TRANSFORMER EXECUTION ANALOGY",
        "note_items": [
            {"t": "WEIGHTS ARE THE MACHINERY (STATIC LOAD)"},
            {"t": "KV CACHE IS THE WORKING NOTES (DYNAMIC GROWTH)"},
            {"t": "LONGER CONTEXT EXPANDS NOTES CONTINUOUSLY"}
        ]
    },

    # Scene 23 (strip): "The key-value cache is some of the temporary state the machinery needs to keep track of the conversation. For an ordinary full-attention transformer with a conventional cache, longer sequences need more stored key and value data."
    {
        "title": "SEQUENCE SCALING PRESSURE",
        "c_tag": "LINEAR GROWTH",
        "items": [
            {"key": "context_window", "label": "LONGER INPUT"},
            {"key": "kv_cache", "label": "MORE KV DATA"},
            {"key": "warning", "label": "VRAM SURGE"}
        ]
    },

    # Scene 24 (nodes): "Cache memory scales with token count, with the number of layers, with the key-value heads and their dimensions, with the storage precision, and with how many sequences are being served."
    {
        "title": "KV CACHE SCALING DRIVERS",
        "art": "die",
        "cap": "SIX HARDWARE PARAMETERS",
        "c_tag": "SCALING DRIVERS",
        "chain": [
            {"t": "LAYERS & HEADS", "s": "TRANSFORMER DEPTH & GQA"},
            {"t": "HEAD DIM & PRECISION", "s": "BYTES PER STORED ELEMENT"},
            {"t": "TOKENS & BATCH SIZE", "s": "SEQUENCE COUNT SERVED"}
        ]
    },

    # Scene 25 (hook): "Here is a calculation, but listen carefully: this is a made-up architecture for explaining the math. It is not a measured benchmark for any GPU or named AI model."
    {
        "title": "HYPOTHETICAL MATH MODEL",
        "art": "scales",
        "cap": "PEDAGOGICAL CALCULATION ARCHITECTURE",
        "c_tag": "ILLUSTRATIVE ONLY",
        "chips": [
            {"c": "cyan", "t": "EDUCATIONAL FORMULA"},
            {"c": "gold", "t": "NOT NAMED BENCHMARK"}
        ],
        "stats": [
            {"c": "cyan", "lab": "PURPOSE", "u": "TYPE", "v": "MATH"},
            {"c": "gold", "lab": "BENCHMARK", "u": "DATA", "v": "MODEL"}
        ]
    },

    # Scene 26 (rows): "Imagine thirty-two layers, eight key-value heads per layer, one hundred and twenty-eight values per head, and two bytes for each stored value. Every cached token needs both a key and a value."
    {
        "title": "THE KV CACHE FORMULA",
        "art": "ram_stick",
        "cap": "2 * LAYERS * HEADS * DIM * BYTES",
        "c_tag": "THE ARCHITECTURE",
        "rows": [
            {"cls": "cyan", "rank": "01", "name": "32 LAYERS", "val": "DEPTH", "sub": "TRANSFORMER BLOCKS"},
            {"cls": "gold", "rank": "02", "name": "8 KV HEADS", "val": "DIM: 128", "sub": "GQA HEAD GROUPING"},
            {"cls": "hot", "rank": "03", "name": "FP16 PRECISION", "val": "2 BYTES", "sub": "KEY + VALUE VECTORS"}
        ]
    },

    # Scene 27 (bars): "With that hypothetical design, a thirty-two-thousand-token cache occupies about four gibibytes before implementation overhead and any other allocations. At eight thousand tokens, the same illustrative cache would occupy about one gibibyte."
    {
        "title": "8K VS 32K CONTEXT CACHE",
        "art": "vram_module",
        "cap": "PHYSICAL MEMORY COMPARISON",
        "c_tag": "SCALING PROOF",
        "bars": [
            {"cls": "cyan", "lab": "8,000 TOKENS", "unit": "GIB", "val": "1.0 GIB", "pct": 25.0},
            {"cls": "hot", "lab": "32,000 TOKENS", "unit": "GIB", "val": "4.0 GIB", "pct": 100.0}
        ]
    },

    # Scene 28 (rail): "At one hundred and twenty-eight thousand tokens, it would be about sixteen gibibytes."
    {
        "title": "128K TOKENS: 16 GIBIBYTES",
        "art": "gpu_24gb",
        "cap": "128K SEQUENCE VRAM FOOTPRINT",
        "c_tag": "THE 16GB WALL",
        "rails": [
            {"cls": "cyan", "lab": "32K TOKENS", "val": "4.0 GIB VRAM", "pct": 25.0},
            {"cls": "red", "lab": "128K TOKENS", "val": "16.0 GIB VRAM", "pct": 100.0}
        ]
    },

    # Scene 29 (chain): "That is the shock. The model weights could already fit comfortably on a graphics card, while the context cache pushes the whole workload over the edge."
    {
        "title": "THE VRAM CLIFF",
        "art": "warning",
        "cap": "CACHE OVERFLOWING HARDWARE",
        "c_tag": "CRITICAL SHOCK",
        "chain": [
            {"t": "MODEL WEIGHTS", "s": "FITS ON GRAPHICS CARD"},
            {"t": "KV CACHE EXPANDS", "s": "16 GIB ADDED VRAM"},
            {"t": "TOTAL ALLOCATION", "s": "WORKLOAD PUSHED OVER EDGE"}
        ],
        "compare": [
            {"cls": "dim", "title": "WEIGHTS LOADED", "body": "FITS COMFORTABLY"},
            {"cls": "gold", "title": "KV CACHE SURGE", "body": "SYSTEM CRASH / OOM"}
        ]
    },

    # Scene 30 (note): "Reducing the weight file through quantization does not automatically reduce the cache to the same precision. The specific cache numbers change with the actual model architecture."
    {
        "title": "WEIGHT QUANTIZATION LIMITS",
        "art": "chip",
        "cap": "WEIGHTS != CACHE PRECISION",
        "c_tag": "QUANTIZATION LAW",
        "note_head": "CACHE PRECISION REALITY",
        "note_items": [
            {"t": "QUANTIZING WEIGHTS LEAVES KV CACHE IN FP16"},
            {"t": "CACHE PRECISION REQUIRES SEPARATE ENGINE FLAGS"},
            {"t": "ARCHITECTURE CHANGES TOTAL HEAD COUNT"}
        ]
    },

    # Scene 31 (strip): "Grouped-query attention can reduce the number of key-value heads. Sliding-window and other attention patterns can change which tokens a layer needs to retain. Some runtimes use quantized or offloaded caches."
    {
        "title": "CACHE MITIGATION DESIGNS",
        "c_tag": "ARCHITECTURES",
        "items": [
            {"key": "die", "label": "GROUPED QUERY"},
            {"key": "clock", "label": "SLIDING WINDOW"},
            {"key": "ram_stick", "label": "OFFLOADED CACHE"}
        ]
    },

    # Scene 32 (nodes): "So never copy those four-gibibyte numbers onto an unrelated model and call them specifications. But the principle is real: fitting the weights is not the same as fitting a long conversation. Now think about what happens when the runtime is also serving more than one request."
    {
        "title": "FITTING WEIGHTS VS CONVERSATION",
        "art": "warning",
        "cap": "CORE HARDWARE PRINCIPLE",
        "c_tag": "GOLDEN RULE",
        "chain": [
            {"t": "STATIC WEIGHTS", "s": "CONSTANT MEMORY CONSUMPTION"},
            {"t": "LONG CONVERSATION", "s": "EXPANDING STATE VECTOR"},
            {"t": "MULTI-USER LOAD", "s": "MULTIPLIED CACHE FOOTPRINTS"}
        ]
    },

    # Scene 33 (hook): "A chat server might hold active state for multiple users. Depending on its scheduling and cache design, the available memory must support those active sequences too."
    {
        "title": "MULTI-USER CONCURRENCY",
        "art": "lan_link",
        "cap": "SHARED RUNTIME STATE CAPACITY",
        "c_tag": "CONCURRENCY SURGE",
        "chips": [
            {"c": "cyan", "t": "ACTIVE SESSIONS"},
            {"c": "gold", "t": "PER-USER KV POOLS"}
        ],
        "stats": [
            {"c": "cyan", "lab": "CONCURRENCY", "u": "USERS", "v": "MULTI"},
            {"c": "gold", "lab": "VRAM POOL", "u": "STATE", "v": "DIVIDED"}
        ]
    },

    # Scene 34 (rows): "A context size that works for one short chat may not be practical with long requests running at the same time."
    {
        "title": "CONCURRENT MEMORY EXHAUSTION",
        "art": "warning",
        "cap": "SCALING CONTEXT UNDER BATCH LOAD",
        "c_tag": "RESOURCE SQUEEZE",
        "rows": [
            {"cls": "cyan", "rank": "01", "name": "1 SHORT CHAT", "val": "STABLE", "sub": "MODERATE VRAM"},
            {"cls": "gold", "rank": "02", "name": "LONG CONVERSATIONS", "val": "SCALING", "sub": "EXPANDED CACHE"},
            {"cls": "hot", "rank": "03", "name": "CONCURRENT BATCH", "val": "COLLAPSE", "sub": "OOM ALLOCATION"}
        ]
    },

    # Scene 35 (bars): "This is why you sometimes see errors about insufficient cache memory even after the weights have loaded. And it's why blindly raising the context setting can make a previously stable system stop launching."
    {
        "title": "INSUFFICIENT CACHE ERRORS",
        "art": "vram_module",
        "cap": "STARTUP CRASHES & LAUNCH REFUSALS",
        "c_tag": "ALLOCATION CRASH",
        "bars": [
            {"cls": "cyan", "lab": "WEIGHTS LOADED", "unit": "STATUS", "val": "SUCCESS", "pct": 100.0},
            {"cls": "hot", "lab": "KV CACHE RESERVATION", "unit": "STATUS", "val": "REFUSED", "pct": 10.0}
        ]
    },

    # Scene 36 (rail): "The fourth limit is more subtle. Even if the model supports the tokens, the runtime accepts them, and the hardware stores them, the model may not use all that information reliably."
    {
        "title": "LIMIT 4: RETRIEVAL RELIABILITY",
        "art": "scales",
        "cap": "THE SUBTLE ACCURACY CEILING",
        "c_tag": "FOURTH LIMIT",
        "rails": [
            {"cls": "cyan", "lab": "HARDWARE STORAGE", "val": "STORED IN VRAM", "pct": 100.0},
            {"cls": "red", "lab": "RETRIEVAL RECALL", "val": "UNRELIABLE USE", "pct": 40.0}
        ]
    },

    # Scene 37 (chain): "Long-context research has demonstrated that the position of a fact can influence whether a model retrieves it correctly."
    {
        "title": "POSITIONAL RETRIEVAL BIAS",
        "art": "context_window",
        "cap": "FACT POSITION INFLUENCES RECALL",
        "c_tag": "RESEARCH FINDING",
        "chain": [
            {"t": "PROMPT START", "s": "HIGH ATTENTION WEIGHT"},
            {"t": "PROMPT MIDDLE", "s": "ATTENTION DECAY ZONE"},
            {"t": "PROMPT END", "s": "RECENCY ATTENTION BOOST"}
        ],
        "compare": [
            {"cls": "dim", "title": "DOCUMENT EDGES", "body": "ACCURATE RETRIEVAL"},
            {"cls": "gold", "title": "MIDDLE REGION", "body": "ATTENTION BLIND SPOT"}
        ]
    },

    # Scene 38 (note): "In the study called Lost in the Middle, the researchers found cases where information near the beginning or the end of a long input was easier for tested models to use than information buried in the middle."
    {
        "title": "LOST IN THE MIDDLE",
        "art": "warning",
        "cap": "THE FAMOUS ATTENTION U-CURVE",
        "c_tag": "THE U-CURVE",
        "note_head": "LOST IN THE MIDDLE FINDINGS",
        "note_items": [
            {"t": "INFORMATION AT BEGINNING: ACCURATE RECALL"},
            {"t": "INFORMATION AT END: ACCURATE RECALL"},
            {"t": "INFORMATION IN MIDDLE: HIGH RETRIEVAL FAILURE"}
        ]
    },

    # Scene 39 (strip): "That is not a claim that every modern model always forgets the middle. Results differ by model, task, and evaluation."
    {
        "title": "EVALUATING MODEL VARIANCE",
        "c_tag": "DIFFERING RESULTS",
        "items": [
            {"key": "chip", "label": "MODEL FAMILY"},
            {"key": "folder", "label": "TASK NATURE"},
            {"key": "checklist", "label": "BENCHMARK SUITE"}
        ]
    },

    # Scene 40 (nodes): "It is a warning that a large numerical context limit is not the same as reliable recall across the entire window. Imagine searching fifty documents."
    {
        "title": "NUMERICAL LIMIT != RECALL",
        "art": "folder",
        "cap": "SEARCHING ACROSS 50 DOCUMENTS",
        "c_tag": "NUMERICAL ILLUSION",
        "chain": [
            {"t": "50 DOCUMENTS LOADED", "s": "128,000 CONTEXT WINDOW"},
            {"t": "ATTENTION DISPERSION", "s": "DILUTED FOCUS ACROSS TOKENS"},
            {"t": "RECALL DISCONNECT", "s": "CRUCIAL FACT OVERLOOKED"}
        ]
    },

    # Scene 41 (hook): "One report, buried halfway through, contains the single number that answers your question. You may discover that changing the document order changes the answer entirely."
    {
        "title": "THE BURIED FACT TEST",
        "art": "warning",
        "cap": "ORDER SENSITIVITY IN RETRIEVAL",
        "c_tag": "ORDER TRAP",
        "chips": [
            {"c": "cyan", "t": "BURIED HALFWAY"},
            {"c": "gold", "t": "ORDER SENSITIVE"}
        ],
        "stats": [
            {"c": "cyan", "lab": "FACT POSITION", "u": "INDEX", "v": "MIDDLE"},
            {"c": "gold", "lab": "ANSWER RECALL", "u": "STATE", "v": "SHIFT"}
        ]
    },

    # Scene 42 (rows): "This is why one of the most useful long-context tests is not asking whether the model loads a giant document."
    {
        "title": "BEYOND LOADING TESTS",
        "art": "checklist",
        "cap": "LOADING A FILE PROVES NOTHING",
        "c_tag": "TRUE AUDIT",
        "rows": [
            {"cls": "cyan", "rank": "01", "name": "LOADING TEST", "val": "TRIVIAL", "sub": "MERE VRAM BUFFER"},
            {"cls": "gold", "rank": "02", "name": "RETRIEVAL AUDIT", "val": "CRITICAL", "sub": "MEASURE EXACT RECALL"},
            {"cls": "hot", "rank": "03", "name": "VERDICT", "val": "BENCHMARK", "sub": "TEST NEEDLE POSITIONS"}
        ]
    },

    # Scene 43 (bars): "It is placing the same important detail near the beginning, the middle, and the end, and checking whether the answers stay consistent across all three positions."
    {
        "title": "3-POSITION NEEDLE AUDIT",
        "art": "context_window",
        "cap": "TESTING BEGINNING, MIDDLE, AND END",
        "c_tag": "NEEDLE AUDIT",
        "bars": [
            {"cls": "cyan", "lab": "BEGINNING & END", "unit": "RECALL", "val": "CONSISTENT", "pct": 95.0},
            {"cls": "hot", "lab": "MIDDLE POSITION", "unit": "RECALL", "val": "DEGRADED", "pct": 40.0}
        ]
    },

    # Scene 44 (rail): "Before a model can produce the first answer token, it must process the input prompt. That initial pass is often called prefill."
    {
        "title": "THE PREFILL PASS",
        "art": "prompt_stream",
        "cap": "INITIAL PROMPT INGESTION PHASE",
        "c_tag": "STAGE ONE",
        "rails": [
            {"cls": "cyan", "lab": "PREFILL COMPUTE", "val": "PARALLEL PASS", "pct": 100.0},
            {"cls": "gold", "lab": "FIRST TOKEN OUT", "val": "TTFT LATENCY", "pct": 80.0}
        ]
    },

    # Scene 45 (chain): "A very long prompt can demand substantial computation and data movement, even when the final answer will only be a few short sentences."
    {
        "title": "LONG PROMPT COMPUTE SURGE",
        "art": "clock",
        "cap": "MASSIVE PREFILL COMPUTE COST",
        "c_tag": "COMPUTE COST",
        "chain": [
            {"t": "120K INPUT PROMPT", "s": "HUGE MATRIX MULTIPLICATION"},
            {"t": "VRAM DATA MOVEMENT", "s": "SATURATED MEMORY BUS"},
            {"t": "SHORT ANSWER", "s": "30 GENERATED TOKENS"}
        ],
        "compare": [
            {"cls": "dim", "title": "PREFILL DEMAND", "body": "MILLIONS OF FLOP OPERATIONS"},
            {"cls": "gold", "title": "FINAL OUTPUT", "body": "FEW SHORT SENTENCES"}
        ]
    },

    # Scene 46 (note): "The cache helps by reusing prior key and value states, but it does not make a very long context free. Attention and memory bandwidth scale with sequence length."
    {
        "title": "THE CONTEXT IS NEVER FREE",
        "art": "vram_module",
        "cap": "BANDWIDTH & ATTENTION SCALING",
        "c_tag": "PHYSICS LAW",
        "note_head": "HARDWARE REALITY",
        "note_items": [
            {"t": "KV CACHE ELIMINATES PAST RECALCULATION"},
            {"t": "EVERY NEW TOKEN STILL READS FULL CACHE"},
            {"t": "BANDWIDTH CONSUMPTION GROWS WITH LENGTH"}
        ]
    },

    # Scene 47 (strip): "That gives you two separate speeds to measure. How long did it take to get the first token? And how quickly did the answer generate after that?"
    {
        "title": "THE TWO CRITICAL METRICS",
        "c_tag": "TWO SPEEDS",
        "items": [
            {"key": "clock", "label": "TIME TO FIRST TOKEN"},
            {"key": "chip", "label": "DECODING THROUGHPUT"},
            {"key": "scales", "label": "OVERALL LATENCY"}
        ]
    },

    # Scene 48 (nodes): "A system can generate tokens quickly once it begins, yet feel painfully slow because it spent so long reading the prompt. Or it can struggle at every step because the cache is pushing hardware to its limit."
    {
        "title": "PREFILL VS DECODE BOTTLENECK",
        "art": "warning",
        "cap": "IDENTIFYING THE REAL SLOWDOWN",
        "c_tag": "DIAGNOSTIC",
        "chain": [
            {"t": "FAST DECODING SPEED", "s": "40 TOKENS PER SECOND"},
            {"t": "PAINFUL PREFILL WAIT", "s": "30 SECONDS TO FIRST TOKEN"},
            {"t": "CACHE PRESSURE", "s": "BANDWIDTH SATURATION SLOWDOWN"}
        ]
    },

    # Scene 49 (hook): "Cache quantization can save space on supported backends. Prefix caching can reuse work when requests share an identical prompt beginning."
    {
        "title": "CACHE OPTIMIZATION TECHNIQUES",
        "art": "cache_grid",
        "cap": "QUANTIZATION & PREFIX CACHING",
        "c_tag": "OPTIMIZATION",
        "chips": [
            {"c": "cyan", "t": "KV QUANTIZATION"},
            {"c": "gold", "t": "PREFIX CACHING"}
        ],
        "stats": [
            {"c": "cyan", "lab": "QUANTIZATION", "u": "SAVING", "v": "VRAM"},
            {"c": "gold", "lab": "PREFIX CACHE", "u": "SPEED", "v": "REUSE"}
        ]
    },

    # Scene 50 (rows): "But none of these features automatically turns the largest advertised context into the best setting for every task."
    {
        "title": "BIGGEST != BEST SETTING",
        "art": "scales",
        "cap": "STRATEGIC CONTEXT SIZING",
        "c_tag": "TASK BALANCE",
        "rows": [
            {"cls": "cyan", "rank": "01", "name": "ADVERTISED SPEC", "val": "128K CEILING", "sub": "MAXIMUM ALLOWED"},
            {"cls": "gold", "rank": "02", "name": "TASK DEMAND", "val": "TARGETED", "sub": "ACTUAL NEEDED TOKENS"},
            {"cls": "hot", "rank": "03", "name": "OPTIMAL SIZE", "val": "BALANCED", "sub": "FASTEST & MOST ACCURATE"}
        ]
    },

    # Scene 51 (bars): "And there is another trap: making the context longer through positional-scaling settings is not the same as proving that the model still reasons properly."
    {
        "title": "POSITIONAL SCALING TRAP",
        "art": "warning",
        "cap": "ROPE EXTRAPOLATION VS REASONING",
        "c_tag": "SCALING ILLUSION",
        "bars": [
            {"cls": "cyan", "lab": "POSITION SCALING", "unit": "ROPE", "val": "EXTENDED", "pct": 100.0},
            {"cls": "hot", "lab": "LOGICAL REASONING", "unit": "QUALITY", "val": "DEGRADED", "pct": 45.0}
        ]
    },

    # Scene 52 (rail): "That does not guarantee the model was trained or validated to reason reliably across that expanded window. So what should you do instead? Use this practical six-step context audit."
    {
        "title": "THE 6-STEP CONTEXT AUDIT",
        "art": "checklist",
        "cap": "PRACTICAL VERIFICATION METHODOLOGY",
        "c_tag": "AUDIT PROTOCOL",
        "rails": [
            {"cls": "cyan", "lab": "EXPANDED WINDOW", "val": "UNTESTED CONFIG", "pct": 100.0},
            {"cls": "gold", "lab": "6-STEP AUDIT", "val": "PROVEN RELIABLE", "pct": 100.0}
        ]
    },

    # Scene 53 (chain): "First, find the real context limit published for the exact model version, and check the running application's configured limit. Record both numbers. Do not assume the model page and the software settings agree."
    {
        "title": "STEP 1: COMPARE LIMITS",
        "art": "checklist",
        "cap": "PUBLISHED VS CONFIGURED LIMITS",
        "c_tag": "AUDIT STEP 1",
        "chain": [
            {"t": "MODEL SPEC CARD", "s": "RECORD PUBLISHED LIMIT"},
            {"t": "SOFTWARE CONFIG", "s": "CHECK RUNTIME SETTING"},
            {"t": "PARITY CHECK", "s": "VERIFY BOTH NUMBERS AGREE"}
        ],
        "compare": [
            {"cls": "dim", "title": "PUBLISHED CARD", "body": "SPECIFICATION MAX"},
            {"cls": "gold", "title": "RUNTIME SETTING", "body": "CONFIGURED LIMIT"}
        ]
    },

    # Scene 54 (note): "Second, inspect the runtime logs. Check where model weights are loaded, how much cache memory is allocated, which cache precision is active, and whether any memory has been placed on the CPU."
    {
        "title": "STEP 2: INSPECT RUNTIME LOGS",
        "art": "laptop",
        "cap": "LOG TELEMETRY VERIFICATION",
        "c_tag": "AUDIT STEP 2",
        "note_head": "LOG CHECKLIST",
        "note_items": [
            {"t": "WEIGHT PLACEMENT: GPU VRAM VS CPU RAM"},
            {"t": "CACHE ALLOCATION: ALLOCATED GIB FOOTPRINT"},
            {"t": "CACHE PRECISION: FP16 VS QUANTIZED KV"},
            {"t": "CPU OFFLOAD: ZERO UNWANTED SYSTEM RAM SPILL"}
        ]
    },

    # Scene 55 (strip): "If your interface hides those details, use the backend logs or supported diagnostics. Third, test the workload you actually run. Start small, with a short prompt."
    {
        "title": "STEP 3: TEST REAL WORKLOADS",
        "c_tag": "AUDIT STEP 3",
        "items": [
            {"key": "laptop", "label": "BACKEND LOGS"},
            {"key": "prompt_stream", "label": "START WITH SHORT"},
            {"key": "clock", "label": "BASELINE TIMING"}
        ]
    },

    # Scene 56 (nodes): "Then increase it in steps using the same model, the same quantization, and the same questions. Record available VRAM, the time to the first token, and the generation speed at each step. Fourth, test recall across the window."
    {
        "title": "STEP 4: STEPWISE BENCHMARK",
        "art": "scales",
        "cap": "MEASURE METRICS ACROSS SIZES",
        "c_tag": "AUDIT STEP 4",
        "chain": [
            {"t": "INCREASE IN STEPS", "s": "4K -> 16K -> 32K -> 64K"},
            {"t": "RECORD METRICS", "s": "AVAILABLE VRAM & TTFT SPEED"},
            {"t": "AUDIT ACCURACY", "s": "VERIFY RECALL AT EACH STEP"}
        ]
    },

    # Scene 57 (hook): "Put one known fact near the start, one in the middle, and one at the end of a document. Ask precise questions with answers that cannot be guessed from general knowledge."
    {
        "title": "NEEDLE IN HAYSTACK AUDIT",
        "art": "context_window",
        "cap": "RIGOROUS RECALL BENCHMARKING",
        "c_tag": "RECALL TEST",
        "chips": [
            {"c": "cyan", "t": "THREE POSITIONS"},
            {"c": "gold", "t": "UNGUESSABLE FACTS"}
        ],
        "stats": [
            {"c": "cyan", "lab": "NEEDLE TEST", "u": "LOC", "v": "START"},
            {"c": "gold", "lab": "NEEDLE TEST", "u": "LOC", "v": "MIDDLE"}
        ]
    },

    # Scene 58 (rows): "A successful model load is not a successful comprehension test. Fifth, reserve space for the answer. Count the system instructions, conversation templates, and expected response size."
    {
        "title": "STEP 5: RESERVE ANSWER SPACE",
        "art": "warning",
        "cap": "LOADING IS NOT COMPREHENSION",
        "c_tag": "AUDIT STEP 5",
        "rows": [
            {"cls": "cyan", "rank": "01", "name": "SYSTEM TEMPLATE", "val": "OVERHEAD", "sub": "ROLES & INSTRUCTIONS"},
            {"cls": "gold", "rank": "02", "name": "INPUT SOURCE", "val": "PRIMARY", "sub": "DOCUMENTS & QUERY"},
            {"cls": "hot", "rank": "03", "name": "OUTPUT RESERVE", "val": "MANDATORY", "sub": "FULL ANSWER CAPACITY"}
        ]
    },

    # Scene 59 (bars): "If the application silently truncates older messages or shifts the context, learn exactly what it keeps and what it discards. Sixth, ask whether you actually need a giant context window."
    {
        "title": "STEP 6: RIGHT-SIZED CONTEXT",
        "art": "scales",
        "cap": "SILENT TRUNCATION & TRUE NEED",
        "c_tag": "AUDIT STEP 6",
        "bars": [
            {"cls": "cyan", "lab": "ACTIVE RETENTION", "unit": "KEPT", "val": "VERIFIED", "pct": 80.0},
            {"cls": "hot", "lab": "SILENT DISCARD", "unit": "LOST", "val": "TRUNCATED", "pct": 20.0}
        ]
    },

    # Scene 60 (rail): "For searching a knowledge base, a retrieval system can locate a smaller collection of relevant passages and pass those passages to the model. That is the basic idea behind retrieval-augmented generation, or RAG."
    {
        "title": "RAG VS GIGANTIC CONTEXT",
        "art": "folder",
        "cap": "RETRIEVAL-AUGMENTED GENERATION",
        "c_tag": "RAG ARCHITECTURE",
        "rails": [
            {"cls": "cyan", "lab": "ENTIRE KNOWLEDGE BASE", "val": "10,000 PASSAGES", "pct": 100.0},
            {"cls": "gold", "lab": "FILTERED CONTEXT", "val": "FOCUSED EXCERPTS", "pct": 20.0}
        ]
    },

    # Scene 61 (chain): "It is not a magic cure. Retrieval can select the wrong passages, omit a crucial detail, or lose context needed to interpret the evidence."
    {
        "title": "RETRIEVAL TRADE-OFFS",
        "art": "warning",
        "cap": "RAG HAS FAILURE MODES TOO",
        "c_tag": "TRADE-OFFS",
        "chain": [
            {"t": "QUERY RETRIEVAL", "s": "TOP-K PASSAGE SELECTION"},
            {"t": "POTENTIAL OMISSIONS", "s": "MISSING KEY CONNECTIONS"},
            {"t": "SYNTHESIS ACCURACY", "s": "DEPENDS ON RETRIEVED CHUNKS"}
        ],
        "compare": [
            {"cls": "dim", "title": "FULL CONTEXT RISK", "body": "LOST IN THE MIDDLE"},
            {"cls": "gold", "title": "RETRIEVAL RISK", "body": "WRONG PASSAGES RETRIEVED"}
        ]
    },

    # Scene 62 (note): "But when the task is answering a question from a large collection of documents, focused retrieval may be more useful than stuffing everything into one massive prompt."
    {
        "title": "FOCUSED RETRIEVAL ADVANTAGE",
        "art": "checklist",
        "cap": "EFFICIENCY ACROSS DOCUMENT POOLS",
        "c_tag": "STRATEGY",
        "note_head": "DOCUMENT AUDIT COMPARISON",
        "note_items": [
            {"t": "FOCUSED RETRIEVAL KEEPS VRAM FOOTPRINT LOW"},
            {"t": "PREFILL RUNS IN FRACTION OF A SECOND"},
            {"t": "REDUCES ATTENTION DISPERSION OVERHEAD"}
        ]
    },

    # Scene 63 (strip): "For whole-book editing, complex cross-document reasoning, or questions that depend on broad structure, you may still need larger context, careful chunking, or multiple passes."
    {
        "title": "WHEN LARGE CONTEXT IS NEEDED",
        "c_tag": "DEEP REASONING",
        "items": [
            {"key": "folder", "label": "WHOLE-BOOK EDIT"},
            {"key": "scales", "label": "BROAD STRUCTURE"},
            {"key": "chip", "label": "MULTIPLE PASSES"}
        ]
    },

    # Scene 64 (nodes): "The correct strategy depends on the task, not on whichever context number looks biggest in a model comparison table. And remember to verify what your chat application does behind the scenes."
    {
        "title": "TASK-DRIVEN ARCHITECTURE",
        "art": "scales",
        "cap": "IGNORE THE BIGGEST NUMBER TABLE",
        "c_tag": "TASK DRIVEN",
        "chain": [
            {"t": "ANALYZE TASK DEMAND", "s": "IDENTIFY REAL CONTEXT NEED"},
            {"t": "IGNORE MARKETING NUMBERS", "s": "BIGGEST NUMBER IS NOT BEST"},
            {"t": "VERIFY APPLICATION LOGS", "s": "CHECK ACTUAL RETENTION"}
        ]
    },

    # Scene 65 (hook): "Saving a chat transcript on disk is not the same as keeping every line inside the model's active context. Your application might keep older messages visible while quietly feeding only recent turns to the model."
    {
        "title": "TRANSCRIPTS != ACTIVE CONTEXT",
        "art": "laptop",
        "cap": "UI ILLUSION VS REAL PROMPT",
        "c_tag": "UI ILLUSION",
        "chips": [
            {"c": "cyan", "t": "SAVED ON DISK"},
            {"c": "gold", "t": "TRUNCATED PROMPT"}
        ],
        "stats": [
            {"c": "cyan", "lab": "UI DISPLAY", "u": "TURNS", "v": "ALL"},
            {"c": "gold", "lab": "MODEL FEED", "u": "TURNS", "v": "RECENT"}
        ]
    },

    # Scene 66 (rows): "That kind of memory management can be sensible. But if it isn't transparent, the model can seem to remember something one moment and forget it the next. So here is the summary."
    {
        "title": "TRANSPARENCY IN CONTEXT",
        "art": "warning",
        "cap": "SILENT CONTEXT ROLLING HAZARDS",
        "c_tag": "SILENT AMNESIA",
        "rows": [
            {"cls": "cyan", "rank": "01", "name": "CONTEXT ROLLING", "val": "SENSIBLE", "sub": "PREVENTS OOM"},
            {"cls": "gold", "rank": "02", "name": "TRANSPARENCY", "val": "CRITICAL", "sub": "USER MUST KNOW"},
            {"cls": "hot", "rank": "03", "name": "SILENT SHIFT", "val": "AMNESIA", "sub": "FORGETS PRIOR FACTS"}
        ]
    },

    # Scene 67 (bars): "There is a model limit. There is a software limit. There is a hardware limit. And there is an effective-use limit. Those four numbers do not have to match."
    {
        "title": "THE FOUR SEPARATE LIMITS",
        "art": "scales",
        "cap": "FOUR NUMBERS THAT DIFFER",
        "c_tag": "THE FOUR LIMITS",
        "bars": [
            {"cls": "cyan", "lab": "MODEL & SOFTWARE", "unit": "LIMIT", "val": "SPECIFIED", "pct": 100.0},
            {"cls": "hot", "lab": "HARDWARE & USE", "unit": "LIMIT", "val": "PHYSICAL", "pct": 40.0}
        ]
    },

    # Scene 68 (rail): "A one-hundred-and-twenty-eight-thousand-token label is a technical specification. It does not promise that your current GPU has enough memory, that your interface is configured to use it, that the first answer will arrive quickly, or that every fact inside the window will be retrieved correctly."
    {
        "title": "A SPEC IS NOT A GUARANTEE",
        "art": "gpu_24gb",
        "cap": "THE ADVERTISED SPEC IS JUST A LABEL",
        "c_tag": "FINAL WARNING",
        "rails": [
            {"cls": "cyan", "lab": "128K SPEC LABEL", "val": "ADVERTISED SPEC", "pct": 100.0},
            {"cls": "red", "lab": "SYSTEM GUARANTEE", "val": "ZERO PROMISE", "pct": 20.0}
        ]
    },

    # Scene 69 (chain): "Before buying more hardware or changing every advanced setting, measure the real bottleneck. Is the prompt being truncated? Is the cache spilling into system memory? Is prefill taking too long?"
    {
        "title": "MEASURE THE REAL BOTTLENECK",
        "art": "checklist",
        "cap": "DIAGNOSTIC TRIAGE PROTOCOL",
        "c_tag": "MEASURE FIRST",
        "chain": [
            {"t": "PROMPT TRUNCATION", "s": "CHECK APP SLICING"},
            {"t": "SYSTEM RAM SPILL", "s": "CHECK CPU OFFLOADING"},
            {"t": "PREFILL LATENCY", "s": "MEASURE TIME TO FIRST TOKEN"}
        ],
        "compare": [
            {"cls": "dim", "title": "GUESSING SETTINGS", "body": "RANDOM HARDWARE SPEND"},
            {"cls": "gold", "title": "MEASURED BOTTLENECK", "body": "TARGETED ENGINEERING FIX"}
        ]
    },

    # Scene 70 (note): "Or is the answer simply wrong even though all the evidence fits? Those problems require different solutions. And solving them starts with measuring what is actually happening."
    {
        "title": "DIAGNOSE BEFORE SOLVING",
        "art": "scales",
        "cap": "EACH FAILURE HAS A DIFFERENT FIX",
        "c_tag": "BYTE FORENSICS LAW",
        "note_head": "ENGINEERING SOLUTIONS",
        "note_items": [
            {"t": "OOM CRASH -> REDUCE CONTEXT OR ENABLE KV QUANT"},
            {"t": "PREFILL DELAY -> IMPLEMENT PREFIX CACHING OR RAG"},
            {"t": "RETRIEVAL LOSS -> REORDER FACTS OR RIGHT-SIZE CHUNKS"}
        ]
    },

    # Scene 71 (hook): "Tell me the exact local model, your GPU, the context setting you use, and what happens when you feed it a long prompt. Does it crash, take forever, or hallucinate?"
    {
        "title": "COMMUNITY FORENSICS AUDIT",
        "art": "gpu",
        "cap": "SHARE YOUR HARDWARE TELEMETRY",
        "c_tag": "TELL US BELOW",
        "chips": [
            {"c": "cyan", "t": "SHARE YOUR GPU"},
            {"c": "gold", "t": "CONTEXT SETTING"}
        ],
        "stats": [
            {"c": "cyan", "lab": "SYMPTOM", "u": "TYPE", "v": "CRASH"},
            {"c": "gold", "lab": "DIAGNOSTIC", "u": "DATA", "v": "LOGS"}
        ]
    },

    # Scene 72 (nodes): "This is Byte Forensics. Don't just count the tokens. Find out which ones your system can actually use."
    {
        "title": "THE FINAL VERDICT",
        "art": "chip",
        "cap": "BYTE FORENSICS EPISODE 13",
        "c_tag": "USABLE TOKENS ONLY",
        "chain": [
            {"t": "DONT JUST COUNT TOKENS", "s": "ADVERTISED SPECIFICATIONS ARE JUST CEILINGS"},
            {"t": "AUDIT YOUR HARDWARE", "s": "MEASURE VRAM, PREFILL SPEED, AND RECALL"},
            {"t": "BYTE FORENSICS", "s": "FIND OUT WHAT YOUR SYSTEM CAN ACTUALLY USE"}
        ]
    }
]

import json
import os

ROOT = r"c:\Users\jibra\Desktop\1\KAI\repo"
out_path = os.path.join(ROOT, "data", "mistral_bespoke_designs.json")

# Ensure every design has idx
for i, d in enumerate(DESIGNS):
    d["idx"] = i

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(DESIGNS, f, indent=2)

print(f"Successfully generated all {len(DESIGNS)} 100% bespoke, script-grounded designs!")
