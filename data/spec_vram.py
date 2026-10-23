# -*- coding: utf-8 -*-
"""
BYTE FORENSICS -- EPISODE 09: VRAM TIERS & MODEL SELECTION (FIRST 1-MINUTE PREVIEW)
===================================================================================
Script word-for-word matching the first 1 minute:
- Window 01 (hook): 27B in 6GB vs 9B in 6GB on an 8GB GPU (exact published download sizes)
- Window 02 (rows): Launching is not working (naive heuristic vs reality gap)
- Window 03 (note): Drive fit != GPU execution (VRAM runtime allocation breakdown stack)
- Window 04 (strip): The Four Memory Tiers under a microscope (8GB, 12GB, 16GB, 24GB distinct)
- Window 05 (chain): The Three Ground Rules (no imaginary TPS, extreme quant loss, VRAM != bandwidth)
"""

DOC_TITLE = "BYTE FORENSICS · EPISODE 09 · WHICH MODEL SHOULD YOU DOWNLOAD?"
NAME = "BYTE-VRAM"
TITLE = "WHICH MODEL SHOULD YOU DOWNLOAD?"
KICKER = "BYTE FORENSICS · EPISODE 09 · 8GB TO 24GB"
SUBTITLE = "the memory budget under a microscope"
VOICE = "en-US-AndrewNeural"
RATE = "+4%"

CHAPTERS = [
    (1, "THE 8GB DILEMMA: 27B VS 9B"),
    (2, "LAUNCHING IS NOT WORKING"),
    (4, "THE FOUR VRAM TIERS (8GB TO 24GB)"),
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
            {
                "v": "27B",
                "u": "Qwen3.8 · 6.19 GB",
                "lab": "DOWNLOAD SIZE (UD-IQ1_S)",
                "c": "gold",
                "at": "twenty-seven-billion-parameter"
            },
            {
                "v": "9B",
                "u": "Qwen3.5 · 5.68 GB",
                "lab": "DOWNLOAD SIZE (Q4_K_M)",
                "c": "dim",
                "at": "nine-billion-parameter"
            }
        ],
        "chips": [
            {"c": "gold", "t": "8GB VRAM BASELINE", "at": "eight gigabytes of video memory"},
            {"c": "hot", "t": "WHICH ONE TO DOWNLOAD?", "at": "which one should you download"}
        ],
        "closing": {
            "c": "gold",
            "t": "DOWNLOAD SIZE != RUNTIME VRAM REQUIREMENT",
            "at": "which one should you download"
        },
        "source": "published Hugging Face GGUF repository sizes (Unsloth) · download sizes, not runtime VRAM",
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
            {
                "rank": "01",
                "name": "ASSUMED LOGIC",
                "val": "MORE PARAMS",
                "sub": "NAIVE HEURISTIC: BIGGER = SMARTER",
                "cls": "",
                "at": "The obvious answer is the bigger model"
            },
            {
                "rank": "02",
                "name": "THE REALITY GAP",
                "val": "SKIPS RUNTIME",
                "sub": "IGNORES WORKING MEMORY & KV CACHE",
                "cls": "gold",
                "at": "Except that answer skips the part"
            },
            {
                "rank": "03",
                "name": "VERDICT CRITERION",
                "val": "SUSTAINED USE",
                "sub": "CAPABLE OF LAUNCHING != GENUINELY USEFUL",
                "cls": "red",
                "at": "genuinely useful, or just technically"
            }
        ],
        "closing": {
            "c": "gold",
            "t": "TECHNICALLY LAUNCHING != GENUINELY USEFUL",
            "at": "capable of launching"
        },
        "source": "inference runtime architecture · memory overhead beyond weights",
        "source_at": "capable of launching"
    },
    {
        "layout": "note",
        "vo": "Because a model file fitting on your drive is not the same as a model running comfortably on your GPU. And a model producing one impressive answer is not the same as handling your actual workload all afternoon.",
        "kicker": "STORAGE VS EXECUTION",
        "title": "DRIVE FIT != GPU EXECUTION",
        "art": "vram_stack",
        "art_caption": "DRIVE FILE VS RUNTIME VRAM OVERHEAD",
        "header_at": "Because a model file fitting on your drive",
        "art_at": "Because a model file fitting on your drive",
        "note_head": "TWO CRITICAL DISTINCTIONS",
        "note_items": [
            {
                "t": "NVME DISK STORAGE IS PASSIVE: WEIGHT FILE CONSUMES 0 GPU CYCLES",
                "at": "fitting on your drive"
            },
            {
                "t": "GPU EXECUTION REQUIRES ACTIVE RUNTIME: WEIGHTS + KV CACHE + CUDA BUFFERS",
                "at": "running comfortably on your GPU"
            },
            {
                "t": "ONE CHERRY-PICKED ANSWER IS NOT A WORKLOAD ALL AFTERNOON",
                "at": "one impressive answer"
            }
        ],
        "tape": "TEST SUSTAINED WORKLOADS · NOT FIRST TOKENS",
        "tape_at": "handling your actual workload",
        "closing": {
            "c": "gold",
            "t": "TEST THE AFTERNOON · NOT A SINGLE PROMPT",
            "at": "all afternoon"
        },
        "source": "operational inference reality · context expansion & buffer requirements",
        "source_at": "all afternoon"
    },
    {
        "layout": "strip",
        "vo": "Today we're putting four common memory budgets under a microscope: eight, twelve, sixteen, and twenty-four gigabytes of VRAM. We'll use real published model files, check where their memory goes, and build a practical decision rule for each class.",
        "kicker": "FOUR MEMORY BUDGETS UNDER THE MICROSCOPE",
        "title": "THE FOUR VRAM TIERS",
        "header_at": "Today we're putting four common memory budgets",
        "items": [
            {
                "label": "8GB · ENTRY TIER",
                "key": "chip",
                "at": "eight"
            },
            {
                "label": "12GB · MID-RANGE SWEET SPOT",
                "key": "vram_module",
                "at": "twelve"
            },
            {
                "label": "16GB · EXPERIMENT TIER",
                "key": "dual_slot",
                "at": "sixteen"
            },
            {
                "label": "24GB · WORKHORSE TIER",
                "key": "gpu",
                "at": "twenty-four"
            }
        ],
        "closing": {
            "c": "gold",
            "t": "PRACTICAL DECISION RULES FOR EVERY BUDGET",
            "at": "decision rule for each class"
        },
        "source": "memory tier evaluation framework · 8GB, 12GB, 16GB, and 24GB published files",
        "source_at": "decision rule for each class"
    },
    {
        "layout": "chain",
        "vo": "No imaginary token-per-second scores. No assumption that a compressed model automatically performs like its full-precision parent. And no pretending that every GPU with the same memory capacity behaves the same way.",
        "kicker": "THE THREE GROUND RULES",
        "title": "THE RULES OF THIS AUDIT",
        "art": "checklist",
        "art_caption": "METHODOLOGICAL INTEGRITY",
        "header_at": "No imaginary token-per-second scores",
        "art_at": "No imaginary token-per-second scores",
        "chain": [
            {
                "t": "NO IMAGINARY SCORES",
                "s": "REAL PUBLISHED WEIGHTS ONLY",
                "at": "No imaginary token-per-second"
            },
            {
                "t": "EXTREME QUANT LOSS",
                "s": "1-BIT COMPRESSION DEGRADES REASONING",
                "at": "compressed model automatically performs"
            },
            {
                "t": "VRAM != BANDWIDTH",
                "s": "CAPACITY DOES NOT EQUAL SPEED",
                "at": "same memory capacity behaves"
            }
        ],
        "compare": [
            {
                "title": "BENCHMARK ILLUSIONS",
                "cls": "hot",
                "body": "Theoretical speed claims ignoring context depth and memory saturation.",
                "at": "token-per-second scores"
            },
            {
                "title": "EMPIRICAL METHOD",
                "cls": "good",
                "body": "Documented weights, exact quantizations, and verified memory footprints.",
                "at": "pretending that every GPU"
            }
        ],
        "closing": {
            "c": "gold",
            "t": "OBSERVED HARDWARE REALITY OVER SPEC SHEETS",
            "at": "same way"
        },
        "source": "audit protocol · published files & documented memory footprints",
        "source_at": "same way"
    }
]
