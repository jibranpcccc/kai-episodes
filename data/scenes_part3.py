# -*- coding: utf-8 -*-
"""
Scenes 49-72 authoritative visual definitions.
"""

SCENES_49_72 = [
    # Scene 49 (hook)
    {
        "layout": "hook",
        "title": "CACHE QUANTIZATION & PREFIX SHARING",
        "header_at": "Cache quantization can save",
        "art": "checklist",
        "art_at": "Prefix caching can reuse work",
        "art_caption": "RUNTIME CACHE OPTIMIZATIONS",
        "chips": [
            {"at": "Cache quantization can save space", "c": "cyan", "t": "CACHE QUANT (Q8 / Q4)"},
            {"at": "Prefix caching can reuse work", "c": "gold", "t": "PREFIX CACHING REUSE"}
        ],
        "stats": [
            {"at": "Cache quantization can save space", "c": "cyan", "lab": "CACHE QUANT", "u": "VRAM", "v": "SAVED"},
            {"at": "Prefix caching can reuse work", "c": "gold", "lab": "PREFIX REUSE", "u": "WORK", "v": "SHARED"}
        ],
        "closing": {"at": "move cache data to other memory", "c": "gold", "t": "OPTIMIZATIONS SAVE VRAM BUT DO NOT ELIMINATE BOUNDS"}
    },
    # Scene 50 (rows)
    {
        "layout": "rows",
        "title": "MAX CONTEXT IS NOT OPTIMAL",
        "header_at": "But none of these",
        "art": "warning",
        "art_at": "largest advertised context into the best",
        "art_caption": "ENGINEERING TRADE-OFF ASSESSMENT",
        "rows": [
            {"at": "none of these features automatically", "cls": "hot", "name": "OPTIMIZATIONS", "rank": "01", "sub": "NO SILVER BULLET", "val": "PARTIAL"},
            {"at": "largest advertised context", "cls": "gold", "name": "MAX CONTEXT", "rank": "02", "sub": "MAXIMUM BOUNDARY", "val": "128K"},
            {"at": "best setting for every task", "cls": "cyan", "name": "TASK SIZING", "rank": "03", "sub": "RIGHT SIZED FIT", "val": "BALANCED"}
        ],
        "closing": {"at": "best setting for every task", "c": "gold", "t": "THE BIGGEST CONTEXT IS NOT ALWAYS THE BEST SETTING"}
    },
    # Scene 51 (bars)
    {
        "layout": "bars",
        "title": "ROPE POSITIONAL SCALING TRAP",
        "header_at": "And there is another",
        "art": "collapse",
        "art_at": "positional-scaling settings is not",
        "art_caption": "ROPE FREQUENCY EXTENSION RISK",
        "bars": [
            {"at": "making the context longer", "cls": "cyan", "lab": "EXTENDED WINDOW", "pct": 100.0, "unit": "ROPE", "val": "EXPANDED"},
            {"at": "model remains accurate at the new", "cls": "hot", "lab": "REASONING QUALITY", "pct": 40.0, "unit": "ACCURACY", "val": "DEGRADED"}
        ],
        "closing": {"at": "change positional parameters", "c": "hot", "t": "STRETCHING ROPE DOES NOT GUARANTEE REASONING QUALITY"}
    },
    # Scene 52 (rail)
    {
        "layout": "rail",
        "title": "TRAINED VS ARTIFICIAL EXTENSION",
        "header_at": "That does not guarantee",
        "art": "scales",
        "art_at": "trained or validated to reason",
        "art_caption": "PRETRAINED COGNITION VS SYNTHETIC STRETCH",
        "rails": [
            {"at": "trained or validated to reason", "cls": "hot", "lab": "TRAINED WINDOW", "val": "VALIDATED LIMIT"},
            {"at": "setting everything to one hundred", "cls": "cyan", "lab": "DEFAULT REFLEX", "val": "BLIND 128K"}
        ],
        "closing": {"at": "one hundred and twenty-eight thousand", "c": "gold", "t": "DO NOT BLINDLY SET RUNTIMES TO 128,000"}
    },
    # Scene 53 (chain)
    {
        "layout": "chain",
        "title": "STEP 1: MODEL VS RUNTIME LIMIT",
        "header_at": "First, find the real",
        "art": "model_file",
        "art_at": "find the real context limit",
        "art_caption": "AUDIT PROTOCOL · GATES 1 & 2",
        "chain": [
            {"at": "find the real context limit", "t": "1. CHECK MODEL SPEC", "s": "EXACT MODEL CONFIG.JSON"},
            {"at": "check the running application's", "t": "2. CHECK RUNTIME CONFIG", "s": "OLLAMA / LLAMA.CPP / VLLM"},
            {"at": "Record both numbers", "t": "3. RECORD BOTH", "s": "NEVER ASSUME THEY AGREE"}
        ],
        "compare": [
            {"at": "find the real context limit", "cls": "cyan", "title": "MODEL SPEC", "body": "PUBLISHED MAX"},
            {"at": "check the running application's", "cls": "gold", "title": "SOFTWARE LIMIT", "body": "CONFIGURED CLI"}
        ],
        "closing": {"at": "software settings agree", "c": "gold", "t": "RECORD BOTH NUMBERS · NEVER ASSUME THEY AGREE"}
    },
    # Scene 54 (note)
    {
        "layout": "note",
        "title": "STEP 2: RUNTIME LOG AUDIT",
        "header_at": "Second, inspect the runtime",
        "art": "motherboard",
        "art_at": "inspect the runtime logs",
        "art_caption": "PHYSICAL ALLOCATION TELEMETRY",
        "note_head": "RUNTIME LOG AUDIT CHECKLIST",
        "note_items": [
            {"at": "where model weights are loaded", "t": "VERIFY WEIGHT PLACEMENT: GPU VRAM VS CPU RAM"},
            {"at": "cache memory is allocated", "t": "RECORD KV CACHE ALLOCATION AND ACTIVE PRECISION"},
            {"at": "placed on the CPU", "t": "CONFIRM WHETHER ANY OFF-LOADING TOUCHED SYSTEM RAM"}
        ],
        "closing": {"at": "placed on the CPU", "c": "gold", "t": "LOGS REVEAL EXACT WEIGHT AND CACHE ALLOCATIONS"}
    },
    # Scene 55 (strip)
    {
        "layout": "strip",
        "title": "STEP 3: REAL WORKLOAD TESTING",
        "header_at": "If your interface hides",
        "art": "checklist",
        "art_at": "test the workload you actually",
        "art_caption": "STEP-WISE LOAD VERIFICATION",
        "items": [
            {"at": "backend logs or supported diagnostics", "key": "checklist", "label": "DIAGNOSTICS", "sub": "CLI LOG STREAM"},
            {"at": "workload you actually care about", "key": "folder", "label": "REAL WORKLOAD", "sub": "REAL USER DATA"},
            {"at": "Start with a modest context", "key": "context_window", "label": "MODEST START", "sub": "8K BASELINE"}
        ],
        "closing": {"at": "Start with a modest context", "c": "gold", "t": "START WITH MODEST CONTEXTS BEFORE SCALING UP"}
    },
    # Scene 56 (nodes)
    {
        "layout": "nodes",
        "title": "STEP-WISE BENCHMARK AUDIT",
        "header_at": "Then increase it in",
        "art": "tok_speed_dial",
        "art_at": "Record available VRAM, the prompt-processing",
        "art_caption": "FOUR SYSTEM TELEMETRY METRICS",
        "chain": [
            {"at": "increase it in steps", "c": "cyan", "t": "INCREMENT STEPS", "s": "8K -> 16K -> 32K -> 64K"},
            {"at": "Record available VRAM", "c": "gold", "t": "VRAM & PREFILL", "s": "MONITOR VRAM & TTFT"},
            {"at": "output generation speed", "c": "hot", "t": "DECODE THROUGHPUT", "s": "TOKENS PER SECOND"}
        ],
        "closing": {"at": "Fourth, test answer quality", "c": "gold", "t": "RECORD VRAM, PREFILL TIME, TTFT, AND DECODE SPEED"}
    },
    # Scene 57 (hook)
    {
        "layout": "hook",
        "title": "STEP 4: NEEDLE IN A HAYSTACK",
        "header_at": "Put one known fact",
        "art": "prompt_stream",
        "art_at": "near the start, one in the middle",
        "art_caption": "THREE-POSITION RECALL VERIFICATION",
        "chips": [
            {"at": "near the start", "c": "cyan", "t": "START NEEDLE"},
            {"at": "one in the middle", "c": "hot", "t": "MIDDLE NEEDLE"}
        ],
        "stats": [
            {"at": "one in the middle", "c": "hot", "lab": "CENTER RECALL", "u": "DEPTH", "v": "MIDDLE"},
            {"at": "one at the end of a document", "c": "gold", "lab": "END RECALL", "u": "DEPTH", "v": "TAIL"}
        ],
        "closing": {"at": "more than one example", "c": "gold", "t": "INDEPENDENTLY VERIFY ACCURACY ACROSS THREE POSITIONS"}
    },
    # Scene 58 (rows)
    {
        "layout": "rows",
        "title": "STEP 5: RESERVE ANSWER SPACE",
        "header_at": "A successful model load",
        "art": "scales",
        "art_at": "reserve space for the answer",
        "art_caption": "INPUT VS OUTPUT TOKEN ACCOUNTING",
        "rows": [
            {"at": "successful comprehension test", "cls": "dim", "name": "MODEL LOAD", "rank": "01", "sub": "VRAM ALLOCATION", "val": "LOADED"},
            {"at": "reserve space for the answer", "cls": "gold", "name": "OUTPUT RESERVE", "rank": "02", "sub": "REQUIRED TOKENS", "val": "RESERVED"},
            {"at": "inserted documents, tool results", "cls": "cyan", "name": "TOTAL INPUT", "rank": "03", "sub": "SYSTEM + TOOLS + DOCS", "val": "COUNTED"}
        ],
        "closing": {"at": "inserted documents, tool results", "c": "gold", "t": "COUNT SYSTEM, DOCS, AND TOOLS BEFORE PASTING"}
    },
    # Scene 59 (bars)
    {
        "layout": "bars",
        "title": "STEP 6: SILENT TRUNCATION & RAG",
        "header_at": "If the application silently",
        "art": "collapse",
        "art_at": "silently truncates older messages",
        "art_caption": "APPLICATION CONTEXT SHIFTING RULES",
        "bars": [
            {"at": "silently truncates older messages", "cls": "hot", "lab": "SILENT EVICTION", "pct": 80.0, "unit": "CHAT", "val": "DISCARDED"},
            {"at": "question whether the model needs", "cls": "gold", "lab": "TARGETED NEED", "pct": 30.0, "unit": "EFFICIENCY", "val": "SUBSET"}
        ],
        "closing": {"at": "needs the whole document at once", "c": "gold", "t": "QUESTION WHETHER THE MODEL NEEDS ALL TEXT AT ONCE"}
    },
    # Scene 60 (rail)
    {
        "layout": "rail",
        "title": "RAG: FOCUSED RETRIEVAL",
        "header_at": "For searching a knowledge",
        "art": "lan_link",
        "art_at": "retrieval-augmented generation, or RAG",
        "art_caption": "RETRIEVAL AUGMENTED GENERATION ARCHITECTURE",
        "rails": [
            {"at": "smaller collection of relevant passages", "cls": "cyan", "lab": "FOCUSED CHUNKS", "val": "TOP-K PASSAGES"},
            {"at": "retrieval-augmented generation, or RAG", "cls": "gold", "lab": "SYSTEM PARADIGM", "val": "RAG PIPELINE"}
        ],
        "closing": {"at": "retrieval-augmented generation, or RAG", "c": "gold", "t": "RETRIEVAL SYSTEM SENDS RELEVANT PASSAGES TO THE MODEL"}
    },
    # Scene 61 (chain)
    {
        "layout": "chain",
        "title": "RETRIEVAL LIMITATIONS",
        "header_at": "It is not a",
        "art": "warning",
        "art_at": "select the wrong passages",
        "art_caption": "RAG FAILURE MODES",
        "chain": [
            {"at": "not a magic cure", "t": "1. NOT A CURE", "s": "RETRIEVAL HAS ERRORS"},
            {"at": "select the wrong passages", "t": "2. WRONG PASSAGE", "s": "EMBEDDING SIMILARITY MISS"},
            {"at": "lose context needed to interpret", "t": "3. CHUNK ISOLATION", "s": "LOST BROADER CONTEXT"}
        ],
        "compare": [
            {"at": "select the wrong passages", "cls": "hot", "title": "RETRIEVAL RISK", "body": "OMITS KEY DETAIL"},
            {"at": "lose context needed to interpret", "cls": "dim", "title": "FRAGMENTATION", "body": "LOSES SYNTACTIC CONTEXT"}
        ],
        "closing": {"at": "interpret a quotation", "c": "hot", "t": "RAG CAN OMIT CRITICAL CONTEXT OR RETRIEVE THE WRONG CHUNKS"}
    },
    # Scene 62 (note)
    {
        "layout": "note",
        "title": "WHEN TO CHOOSE RAG",
        "header_at": "But when the task",
        "art": "folder",
        "art_at": "large collection of documents",
        "art_caption": "CORPUS QA WORKLOAD STRATEGY",
        "note_head": "CORPUS QUESTION-ANSWERING",
        "note_items": [
            {"at": "answering a question from a large", "t": "CORPUS QA: SEARCHING ACROSS HUGE KNOWLEDGE BASES"},
            {"at": "focused retrieval may be more useful", "t": "FOCUSED RETRIEVAL EXCELS OVER GIANT BRUTE FORCE PROMPTS"},
            {"at": "pouring every page into the prompt", "t": "POURING 1000s OF PAGES WASTES VRAM AND SLOWS PREFILL"}
        ],
        "closing": {"at": "pouring every page into the prompt", "c": "gold", "t": "TARGETED RETRIEVAL BEATS POURING ENTIRE LIBRARIES INTO PROMPTS"}
    },
    # Scene 63 (strip)
    {
        "layout": "strip",
        "title": "WHEN GIANT CONTEXT WINS",
        "header_at": "For whole-book editing, complex",
        "art": "context_window",
        "art_at": "whole-book editing, complex cross-document",
        "art_caption": "GLOBAL SYNTHESIS & CROSS-DOC WORKLOADS",
        "items": [
            {"at": "whole-book editing", "key": "model_file", "label": "BOOK EDITING", "sub": "FULL NARRATIVE ARC"},
            {"at": "complex cross-document reasoning", "key": "pipeline", "label": "CROSS-DOC", "sub": "MULTI-FILE LOGIC"},
            {"at": "depend on broad structure", "key": "context_window", "label": "BROAD STRUCTURE", "sub": "GLOBAL DEPENDENCIES"}
        ],
        "closing": {"at": "careful chunking, or multiple passes", "c": "gold", "t": "GLOBAL DEPENDENCIES DEMAND NATIVE CONTEXT OR CHUNKING"}
    },
    # Scene 64 (nodes)
    {
        "layout": "nodes",
        "title": "TASK-DRIVEN ARCHITECTURE",
        "header_at": "The correct strategy depends",
        "art": "scales",
        "art_at": "correct strategy depends on the task",
        "art_caption": "TASK-FIT ARCHITECTURAL SELECTION",
        "chain": [
            {"at": "depends on the task", "c": "cyan", "t": "TASK GOAL", "s": "REASONING OBJECTIVE"},
            {"at": "biggest in a model comparison table", "c": "hot", "t": "MARKETING TABLE", "s": "SPEC HIGHEST NUMBER"},
            {"at": "one final distinction matters", "c": "gold", "t": "FINAL LAW", "s": "TRANSCRIPT VS ACTIVE"}
        ],
        "closing": {"at": "one final distinction matters", "c": "gold", "t": "SELECT SIZES BASED ON WORKLOAD · NOT SPEC TABLES"}
    },
    # Scene 65 (hook)
    {
        "layout": "hook",
        "title": "DISK TRANSCRIPT != ACTIVE CONTEXT",
        "header_at": "Saving a chat transcript",
        "art": "nvme_ssd",
        "art_at": "Saving a chat transcript on disk",
        "art_caption": "PERSISTENT DISK STORAGE VS VRAM STATE",
        "chips": [
            {"at": "transcript on disk", "c": "cyan", "t": "DISK TRANSCRIPT"},
            {"at": "active context", "c": "hot", "t": "VRAM ACTIVE CONTEXT"}
        ],
        "stats": [
            {"at": "transcript on disk", "c": "cyan", "lab": "DISK STORAGE", "u": "LOGS", "v": "PERSIST"},
            {"at": "active context", "c": "gold", "lab": "VRAM STATE", "u": "TOKENS", "v": "ACTIVE"}
        ],
        "closing": {"at": "useful engineering", "c": "gold", "t": "SAVING TRANSCRIPTS TO DISK IS NOT KEEPING THEM IN VRAM"}
    },
    # Scene 66 (rows)
    {
        "layout": "rows",
        "title": "THE FINAL VERDICT: 4 LIMITS",
        "header_at": "But if it isn't",
        "art": "checklist",
        "art_at": "There is a model limit",
        "art_caption": "THE BYTE FORENSICS FOUR LIMITS THEOREM",
        "rows": [
            {"at": "model limit", "cls": "cyan", "name": "1. MODEL LIMIT", "rank": "01", "sub": "ARCHITECTURE & ROPE", "val": "ROPE CONFIG"},
            {"at": "runtime limit", "cls": "gold", "name": "2. RUNTIME LIMIT", "rank": "02", "sub": "LLAMA.CPP -C / VLLM", "val": "ENGINE CONFIG"}
        ],
        "closing": {"at": "runtime limit", "c": "gold", "t": "THE FOUR INDEPENDENT LIMITS FRAMEWORK"}
    },
    # Scene 67 (bars)
    {
        "layout": "bars",
        "title": "HARDWARE VS EFFECTIVE RECALL",
        "header_at": "There is a hardware",
        "art": "scales",
        "art_at": "There is a hardware limit",
        "art_caption": "PHYSICAL MEMORY VS REASONING FIDELITY",
        "bars": [
            {"at": "hardware limit", "cls": "cyan", "lab": "3. HARDWARE LIMIT", "pct": 75.0, "unit": "VRAM", "val": "PHYSICAL"},
            {"at": "effective-use limit", "cls": "gold", "lab": "4. EFFECTIVE USE", "pct": 50.0, "unit": "ACCURACY", "val": "RECALL"}
        ],
        "closing": {"at": "describe a supported capability", "c": "gold", "t": "FOUR NUMBERS DO NOT HAVE TO MATCH"}
    },
    # Scene 68 (rail)
    {
        "layout": "rail",
        "title": "THE FOUR ASSUMPTIONS",
        "header_at": "It does not promise",
        "art": "warning",
        "art_at": "does not promise that your current",
        "art_caption": "THE FOUR LONG-CONTEXT ASSUMPTIONS",
        "rails": [
            {"at": "current GPU has enough memory", "cls": "hot", "lab": "MEMORY", "val": "ENOUGH VRAM"},
            {"at": "interface is configured to use it", "cls": "cyan", "lab": "RUNTIME", "val": "CONFIGURED"},
            {"at": "first answer will arrive quickly", "cls": "gold", "lab": "SPEED", "val": "FAST TTFT"}
        ],
        "closing": {"at": "inside the window will be retrieved", "c": "gold", "t": "128K ADVERTISEMENT GUARANTEES NONE OF THE FOUR"}
    },
    # Scene 69 (chain)
    {
        "layout": "chain",
        "title": "MEASURE THE REAL BOTTLENECK",
        "header_at": "Before buying more hardware",
        "art": "pipeline",
        "art_at": "measure the real bottleneck",
        "art_caption": "SYSTEM DIAGNOSTIC TRIAGE",
        "chain": [
            {"at": "prompt being truncated", "t": "TRUNCATED PROMPT", "s": "INPUT EXCEEDS ALLOCATION"},
            {"at": "cache running out of memory", "t": "CACHE RUNS OUT", "s": "VRAM OOM DURING DECODE"},
            {"at": "prefill taking too long", "t": "PREFILL LATENCY", "s": "COMPUTE TIME TO FIRST TOKEN"}
        ],
        "compare": [
            {"at": "cache running out of memory", "cls": "hot", "title": "HARDWARE BOUND", "body": "VRAM SATURATION"},
            {"at": "prefill taking too long", "cls": "gold", "title": "COMPUTE BOUND", "body": "TTFT DELAY"}
        ],
        "closing": {"at": "prefill taking too long", "c": "gold", "t": "MEASURE THE REAL BOTTLENECK BEFORE BUYING HARDWARE"}
    },
    # Scene 70 (note)
    {
        "layout": "note",
        "title": "SOLVING THE WRONG PROBLEM",
        "header_at": "Or is the answer",
        "art": "collapse",
        "art_at": "answer simply wrong even though",
        "art_caption": "THE COST OF FALSE DIAGNOSIS",
        "note_head": "DIAGNOSTIC ACCURACY",
        "note_items": [
            {"at": "answer simply wrong even though", "t": "HALLUCINATION CAN OCCUR EVEN WHEN ALL EVIDENCE FITS"},
            {"at": "require different solutions", "t": "HARDWARE OOM, TTFT LAG, AND RECALL DEMAND DIFFERENT FIXES"},
            {"at": "cost you hours, money", "t": "FIXING THE WRONG CHOKEPOINT WASTES HARDWARE MONEY AND HOURS"}
        ],
        "closing": {"at": "were trying to improve", "c": "hot", "t": "SOLVING THE WRONG BOTTLENECK COSTS TIME AND MONEY"}
    },
    # Scene 71 (strip)
    {
        "layout": "strip",
        "title": "THE AUDIT INVITATION",
        "header_at": "Tell me the exact",
        "art": "gpu",
        "art_at": "Tell me the exact local model",
        "art_caption": "COMMUNITY FORENSIC BENCHMARK",
        "items": [
            {"at": "exact local model", "key": "model_file", "label": "LOCAL MODEL", "sub": "EXACT WEIGHTS"},
            {"at": "your GPU", "key": "gpu", "label": "YOUR GPU", "sub": "PHYSICAL VRAM POOL"},
            {"at": "context setting you use", "key": "context_window", "label": "CONTEXT CLI", "sub": "ACTIVE PARAMETER"}
        ],
        "closing": {"at": "give the wrong answer", "c": "gold", "t": "DOES IT CRASH, CRAWL, TRUNCATE, OR HALLUCINATE?"}
    },
    # Scene 72 (nodes)
    {
        "layout": "nodes",
        "title": "BYTE FORENSICS LAW",
        "header_at": "This is Byte Forensics",
        "art": "checklist",
        "art_at": "Don't just count the tokens",
        "art_caption": "THE GOLDEN PRINCIPLE OF LOCAL INFERENCE",
        "chain": [
            {"at": "This is Byte Forensics", "c": "cyan", "t": "BYTE FORENSICS", "s": "SYSTEM AUDIT"},
            {"at": "Don't just count the tokens", "c": "hot", "t": "STOP BLIND COUNTING", "s": "MARKETING NUMBERS"},
            {"at": "system can actually use", "c": "gold", "t": "USEFUL TOKENS", "s": "REAL HARDWARE CAPACITY"}
        ],
        "closing": {"at": "system can actually use", "c": "gold", "t": "FIND OUT WHICH TOKENS YOUR SYSTEM CAN ACTUALLY USE"}
    }
]
