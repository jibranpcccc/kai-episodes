# -*- coding: utf-8 -*-
"""
BYTE FORENSICS -- EPISODE 08: VRAM TIERS & MODEL SELECTION (FIRST 1-MINUTE PREVIEW)
===================================================================================
Script word-for-word matching the first 1 minute:
- Window 01 (hook): 27B in 6GB vs 9B in 6GB on an 8GB GPU
- Window 02 (rows): Launching is not working (naive heuristic vs reality gap)
- Window 03 (note): Drive fit != GPU execution (sustained afternoon workload)
- Window 04 (strip): The Four Memory Tiers under a microscope (8GB, 12GB, 16GB, 24GB)
- Window 05 (chain): The Three Ground Rules (no imaginary TPS, no free lunch, VRAM != bandwidth)
"""

DOC_TITLE = "BYTE FORENSICS · WHICH MODEL SHOULD YOU DOWNLOAD?"
NAME = "BYTE-VRAM"
TITLE = "WHICH MODEL SHOULD YOU DOWNLOAD?"
KICKER = "BYTE FORENSICS · EPISODE 08 · 8GB TO 24GB"
SUBTITLE = "the memory budget under a microscope"
VOICE = "en-US-AndrewNeural"
RATE = "+4%"

CHAPTERS = [
    (1, "THE 8GB DILEMMA: 27B VS 9B"),
    (2, "LAUNCHING IS NOT WORKING"),
    (4, "FOUR MEMORY BUDGETS (8GB TO 24GB)"),
]

W = [
    {
        "layout": "hook",
        "vo": "A twenty-seven-billion-parameter AI model can now come in a file barely larger than six gigabytes. And a nine-billion-parameter model can take almost the same amount of space. So if your graphics card has eight gigabytes of video memory, which one should you download?",
        "kicker": "THE LOCAL AI VRAM PARADOX",
        "title": "27B IN 6GB · THE DOWNLOAD PARADOX",
        "art": "gpu",
        "art_caption": "HARDWARE CAPACITY VS WEIGHT SIZE",
        "header_at": "A twenty-seven-billion-parameter AI model",
        "art_at": "A twenty-seven-billion-parameter AI model",
        "stats": [
            {"v": "27B", "u": "PARAM", "lab": "1-BIT COMPRESSION", "c": "gold", "at": "barely larger than six gigabytes"},
            {"v": "9B", "u": "PARAM", "lab": "4-BIT QUANT", "c": "dim", "at": "almost the same amount of space"}
        ],
        "chips": [
            {"c": "gold", "t": "8GB VRAM BASELINE", "at": "eight gigabytes of video memory"},
            {"c": "hot", "t": "WHICH ONE TO DOWNLOAD?", "at": "which one should you download"}
        ],
        "closing": {"c": "gold", "t": "SAME DISK SIZE · RADICALLY DIFFERENT REALITY", "at": "which one should you download"},
        "source": "empirical model release data · 27B 1-bit vs 9B 4-bit GGUF",
        "source_at": "which one should you download"
    },
    {
        "layout": "rows",
        "vo": "The obvious answer is the bigger model. More parameters, more intelligence, same memory. Except that answer skips the part that determines whether your local AI setup is genuinely useful, or just technically capable of launching.",
        "kicker": "THE COMMON TRAP",
        "title": "LAUNCHING IS NOT WORKING",
        "art": "question",
        "art_caption": "THE FALSE PROMISE OF PARAMETER SQUEEZING",
        "header_at": "The obvious answer is the bigger model",
        "art_at": "The obvious answer is the bigger model",
        "rows": [
            {"rank": "01", "name": "ASSUMED LOGIC", "val": "MORE PARAMS", "sub": "NAIVE HEURISTIC", "cls": "", "at": "The obvious answer is the bigger model"},
            {"rank": "02", "name": "THE REALITY GAP", "val": "SKIPS RUNTIME", "sub": "IGNORES WORKING MEMORY", "cls": "gold", "at": "Except that answer skips the part"},
            {"rank": "03", "name": "VERDICT CRITERION", "val": "GENUINE USE", "sub": "NOT BARE LAUNCHING", "cls": "red", "at": "genuinely useful, or just technically"}
        ],
        "closing": {"c": "gold", "t": "TECHNICALLY LAUNCHING != GENUINELY USEFUL", "at": "capable of launching"},
        "source": "inference runtime architecture · memory overhead beyond weights",
        "source_at": "capable of launching"
    },
    {
        "layout": "note",
        "vo": "Because a model file fitting on your drive is not the same as a model running comfortably on your GPU. And a model producing one impressive answer is not the same as handling your actual workload all afternoon.",
        "kicker": "THE TWO GOLDEN RULES",
        "title": "DRIVE FIT != GPU EXECUTION",
        "art": "laptop",
        "art_caption": "SUSTAINED LOAD VS SINGLE-SHOT DEMOS",
        "header_at": "Because a model file fitting on your drive",
        "art_at": "Because a model file fitting on your drive",
        "note_head": "TWO CRITICAL DISTINCTIONS",
        "note_items": [
            {"t": "A MODEL FILE ON NVME IS PASSIVE STORAGE", "at": "fitting on your drive"},
            {"t": "GPU EXECUTION REQUIRES ACTIVE RUNTIME ALLOCATION", "at": "running comfortably on your GPU"},
            {"t": "ONE CHERRY-PICKED ANSWER IS NOT A WORKLOAD", "at": "one impressive answer"}
        ],
        "tape": "SUSTAINED WORKLOAD IS THE TEST",
        "tape_at": "handling your actual workload",
        "closing": {"c": "gold", "t": "TEST THE AFTERNOON · NOT THE FIRST PROMPT", "at": "all afternoon"},
        "source": "operational reality · sustained inference stability",
        "source_at": "all afternoon"
    },
    {
        "layout": "strip",
        "vo": "Today we're putting four common memory budgets under a microscope: eight, twelve, sixteen, and twenty-four gigabytes of VRAM. We'll use real published model files, check where their memory goes, and build a practical decision rule for each class.",
        "kicker": "FOUR TIERS UNDER THE MICROSCOPE",
        "title": "THE FOUR MEMORY TIERS",
        "header_at": "Today we're putting four common memory budgets",
        "items": [
            {"label": "8GB & 12GB ENTRY/MID", "key": "chip", "at": "eight, twelve, sixteen"},
            {"label": "16GB HEAVY EXPERIMENT", "key": "vram_module", "at": "sixteen, and twenty-four"},
            {"label": "24GB FULL WORKHORSE", "key": "gpu", "at": "twenty-four gigabytes of VRAM"}
        ],
        "closing": {"c": "gold", "t": "PRACTICAL DECISION RULES FOR EVERY TIER", "at": "decision rule for each class"},
        "source": "evaluation framework · 8GB, 12GB, 16GB, and 24GB",
        "source_at": "decision rule for each class"
    },
    {
        "layout": "chain",
        "vo": "No imaginary token-per-second scores. No assumption that a compressed model automatically performs like its full-precision parent. And no pretending that every GPU with the same memory capacity behaves the same way.",
        "kicker": "THE THREE GROUND RULES",
        "title": "THE RULES OF THIS AUDIT",
        "art": "checklist",
        "art_caption": "REPRODUCIBLE METHODOLOGY",
        "header_at": "No imaginary token-per-second scores",
        "art_at": "No imaginary token-per-second scores",
        "chain": [
            {"t": "NO IMAGINARY SCORES", "s": "REAL FILES ONLY", "at": "No imaginary token-per-second"},
            {"t": "QUANT LOSS IS REAL", "s": "NO FREE LUNCH", "at": "compressed model automatically performs"},
            {"t": "VRAM != BANDWIDTH", "s": "BUS VARIANCES", "at": "same memory capacity behaves"}
        ],
        "compare": [
            {"title": "BENCHMARK ILLUSIONS", "cls": "hot", "body": "Theoretical tokens-per-second without context depth or memory pressure.", "at": "token-per-second scores"},
            {"title": "EMPIRICAL METHOD", "cls": "good", "body": "Real published weights, exact quantization sizes, physical memory allocations.", "at": "pretending that every GPU"}
        ],
        "closing": {"c": "gold", "t": "MEASURED PHYSICAL BEHAVIOR OVER SPEC SHEETS", "at": "same way"},
        "source": "benchmark integrity protocol · zero synthetic numbers",
        "source_at": "same way"
    }
]
