# -*- coding: utf-8 -*-
"""
FUSION — EPISODE 08, FULL: "Why a Tiny LoRA Adapter Can Still Fill Your GPU"

The author's full script, built with the engine and layouts approved 100% in
BYTE-07-FUSION.html (core/fusion.css + core/fusion.js, restored byte for byte).

  * layouts used: hook, rows, strip, chain, note, nodes, gallery, bars, rail,
    title -- every layout in the library, and no two windows in a row share
    one, so the composition never repeats.
  * no act cards, no "ACT ONE" labels. The kicker is topical, the way the
    approved episode's kicker is topical.
  * the drawings come from the whole library.
  * every number on screen is a number the script says, in words.
  * every window carries a source you can look up.
"""

import re

NAME = "BYTE-LORA-FINAL"
TITLE = "WHY A TINY LoRA ADAPTER CAN STILL FILL YOUR GPU"
KICKER = "BYTE FORENSICS &middot; EPISODE 08"
SUBTITLE = "the adapter is small. the training job is not."

W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


# =====================================================================
# THE PARADOX, PART ONE
# =====================================================================
win("hook",
    vo="Training a tiny adapter can exhaust your GPU. That is the first "
       "distinction to make before fine-tuning a local model. Three point six "
       "nine million trainable parameters for query and value alone, or "
       "twenty-nine point nine three million when all seven projections are targeted.",
    kicker="LoRA &middot; THE TINY FILE",
    title="TINY ADAPTER, BIG JOB",
    sub="the file is small. the job is not.",
    art="model_file",
    art_caption="MODEL FILE",
    header_at="Training a tiny adapter can exhaust your GPU",
    art_at="Training a tiny adapter can exhaust your GPU",
    chips=[
        dict(t="THE FIRST DISTINCTION TO MAKE", c="cyan",
             at="That is the first distinction to make"),
        dict(t="THREE POINT SIX NINE MILLION", c="gold",
             at="Three point six nine million trainable parameters"),
        dict(t="TWENTY-NINE POINT NINE THREE MILLION", c="red",
             at="twenty-nine point nine three million when all seven projections are targeted"),
    ],
    stats=[
        dict(v="3.69M", u="PARAMS", lab="RANK 16, QUERY AND VALUE ONLY",
             c="gold", at="for query and value alone"),
        dict(v="29.93M", u="PARAMS", lab="ALL SEVEN PROJECTIONS TARGETED",
             c="red", at="all seven projections are targeted"),
    ],
    tape="A SMALL RANK IS NOT A SPECIFICATION",
    tape_at="are targeted",
    source="derived &middot; rank 16 &middot; qwen2.5 3b instruct &middot; "
           "36 layers &middot; 2 kv heads &middot; head dim 128")

# =====================================================================
# THE PARADOX, PART TWO
# =====================================================================
win("rows",
    vo="The adapter file describes the changes you learned. It does not "
       "describe everything the machine needed while learning them. Loading a "
       "model and answering a question proves that an inference workload "
       "fits. Training that same model creates a different memory bill.",
    kicker="LoRA &middot; THE FILE AND THE JOB",
    title="THE FILE IS NOT THE JOB",
    art="memory_bank",
    art_caption="MEMORY BANK",
    header_at="The adapter file describes the changes you learned",
    art_at="The adapter file describes the changes you learned",
    rows=[
        dict(rank="01", name="THE MACHINE", val="NOT DESCRIBED",
             sub="WHAT WAS NEEDED", cls="",
             at="It does not describe everything the machine needed"),
        dict(rank="02", name="AN INFERENCE WORKLOAD", val="FITS",
             sub="PROVEN BY LOADING", cls="",
             at="Loading a model and answering a question"),
        dict(rank="03", name="A TRAINING RUN", val="DIFFERENT BILL",
             sub="NOT THE SAME WORK", cls="red",
             at="Training that same model"),
    ],
    closing=dict(c="gold", t="A DIFFERENT MEMORY BILL",
                 at="creates a different memory bill"),
    source="the QLoRA paper &middot; arxiv 2305.14314 &middot; training holds "
           "gradients and optimizer state that inference does not")

# =====================================================================
# THE THREE THINGS YOU NEED
# =====================================================================
win("strip",
    vo="Three separate problems, three separate parts of the machine, and "
       "every one of them is on this screen right now. Quantise it and the "
       "file shrinks. Load it into memory. And keep it on a drive that does "
       "not spin. Count them as three separate budgets.",
    kicker="LoRA &middot; THE THREE THINGS YOU NEED",
    title="QUANTISE, LOAD, STORE",
    header_at="Three separate problems",
    items=[
        dict(key="gguf_blocks", label="QUANTISE THE FILE",
             at="Quantise it and the file shrinks"),
        dict(key="ram_stick", label="LOAD IT INTO MEMORY",
             at="Load it into memory"),
        dict(key="nvme_ssd", label="KEEP IT ON A SOLID STATE DRIVE",
             at="a drive that does not spin"),
    ],
    closing=dict(c="gold", t="THREE BUDGETS, NOT ONE",
                 at="three separate budgets"),
    source="mechanism &middot; quantised weights, system memory, and a solid "
           "state drive are three separate budgets")

# =====================================================================
# WHERE SILICON COMES FROM
# =====================================================================
win("rows",
    vo="Training requires far more than the saved adapter. The base model "
       "stays frozen, but every forward pass stores temporary activations, "
       "and backpropagation calculates gradients for the trainable matrices. "
       "That execution state fills your memory.",
    kicker="LoRA &middot; TRAINING MEMORY MECHANISM",
    title="ACTIVATIONS, GRADIENTS, WEIGHTS",
    art="pipeline",
    art_caption="TRAINING PIPELINE",
    header_at="Training requires far more than the saved adapter",
    art_at="Training requires far more than the saved adapter",
    rows=[
        dict(rank="01", name="BASE WEIGHTS", val="FROZEN", sub="LOADED IN VRAM",
             cls="cyan", at="The base model stays frozen"),
        dict(rank="02", name="ACTIVATIONS", val="STORED", sub="EVERY FORWARD PASS",
             cls="gold", at="every forward pass stores temporary activations"),
        dict(rank="03", name="GRADIENTS & OPT", val="LIVE", sub="FOR TRAINABLE MATRICES",
             cls="red", at="backpropagation calculates gradients for the trainable matrices"),
    ],
    closing=dict(c="gold", t="EXECUTION STATE FILLS YOUR MEMORY",
                 at="That execution state fills your memory"),
    source="mechanism &middot; Hu et al. 2021 &middot; Dettmers et al. 2023 &middot; "
           "activation storage and optimizer state")

# =====================================================================
# HOW LoRA WORKS
# =====================================================================
win("hook",
    vo="LoRA freezes the original weight matrix and learns an additional "
       "update through two smaller matrices. Think of the frozen model as a "
       "machine whose controls you are adjusting. You do not rebuild every "
       "component. But the machine still runs during each training example.",
    kicker="LoRA &middot; HOW IT WORKS",
    title="TWO SMALL MATRICES",
    sub="the controls you are adjusting",
    art="two_die",
    art_caption="DIE A, DIE B",
    header_at="LoRA freezes the original",
    art_at="LoRA freezes the original",
    chips=[
        dict(t="THE ORIGINAL WEIGHTS STAY FROZEN", c="cyan",
             at="the original weight matrix"),
        dict(t="TWO SMALLER MATRICES ARE LEARNED", c="gold",
             at="Think of the frozen model as a machine"),
        dict(t="BUT THE MACHINE STILL RUNS", c="red",
             at="the machine still runs during each training example"),
    ],
    stats=[
        dict(v="2", u="MATRICES", lab="THE WHOLE UPDATE", c="gold",
             at="through two smaller matrices"),
        dict(v="0", u="REBUILT", lab="NOTHING IS REBUILT", c="cyan",
             at="You do not rebuild every component"),
    ],
    tape="FROZEN DOES NOT MEAN THE JOB DISAPPEARS",
    tape_at="during each training example",
    source="the LoRA paper &middot; arxiv 2106.09685")

# =====================================================================
# THE BACKWARD PASS
# =====================================================================
win("chain",
    vo="The error signal still travels backward through the computation so the "
       "adapter can learn. Intermediate tensors needed for that backward pass "
       "remain part of the job. Frozen weights are not permission to delete "
       "the learning process.",
    kicker="LoRA &middot; WHY THE MEMORY IS STILL THERE",
    title="THE BACKWARD PASS DOES NOT KNOW",
    art="chip",
    art_caption="THE PACKAGE",
    header_at="The error signal still travels",
    art_at="The error signal still travels",
    chain=[
        dict(t="BACKWARD", s="the error travels",
             at="backward through the computation"),
        dict(t="TENSORS", s="they stay live",
             at="Intermediate tensors needed for that backward pass"),
        dict(t="FROZEN", s="is not free",
             at="Frozen weights are not permission to delete"),
    ],
    compare=[
        dict(cls="hot", title="FROZEN",
             body="The weights do not change, so it is tempting to think the job is smaller.",
             at="so the adapter can learn"),
        dict(cls="good", title="THE ADAPTER",
             body="Only the small matrices learn, and the rest of the machine still runs.",
             at="remain part of the job"),
    ],
    closing=dict(c="gold", t="FROZEN IS NOT THE SAME AS FREE",
                 at="the learning process"),
    source="the LoRA paper &middot; arxiv 2106.09685 &middot; the gradient "
           "still flows through the frozen base")

# =====================================================================
# THE ARITHMETIC
# =====================================================================
win("rows",
    vo="The adapter arithmetic is concrete. For a projection with input width "
       "two thousand forty-eight and output width two thousand forty-eight, "
       "rank sixteen times their sum gives one hundred two thousand four "
       "hundred added values. One matrix maps the input into the rank, "
       "another maps the rank into the output.",
    kicker="LoRA &middot; THE ARITHMETIC",
    title="RANK TIMES THE SUM OF THE WIDTHS",
    art="die",
    art_caption="THE DIE",
    header_at="The adapter arithmetic is concrete",
    art_at="The adapter arithmetic is concrete",
    rows=[
        dict(rank="01", name="INPUT WIDTH", val="2,048", sub="RANK 16",
             cls="gold", at="input width two thousand forty-eight"),
        dict(rank="02", name="OUTPUT WIDTH", val="2,048", sub="RANK 16",
             cls="gold", at="output width two thousand forty-eight"),
        dict(rank="03", name="ADDED PER LAYER", val="102,400", sub="DERIVED",
             cls="", at="one hundred two thousand four hundred"),
        dict(rank="04", name="FIRST MATRIX", val="2048 TO 16",
             sub="INPUT TO RANK", cls="",
             at="One matrix maps the input into the rank"),
        dict(rank="05", name="SECOND MATRIX", val="16 TO 2048",
             sub="RANK TO OUTPUT", cls="",
             at="another maps the rank into the output"),
    ],
    closing=dict(c="gold", t="A COUNT OF TRAINABLE VALUES",
                 at="into the output"),
    source="derived &middot; rank 16 &middot; qwen2.5 3b instruct &middot; "
           "36 layers &middot; 2 kv heads &middot; head dim 128")

# =====================================================================
# A COUNT IS NOT A MEMORY PLAN
# =====================================================================
win("note",
    vo="Converting it into a memory prediction requires another question: what "
       "precision holds those values, their gradients, and the optimizer "
       "history? Then we still have to account for the rest of training.",
    kicker="LoRA &middot; COUNTING IS NOT THE SAME AS FITTING",
    title="A COUNT IS NOT A MEMORY PLAN",
    art="magnifier",
    art_caption="READ THE FINE PRINT",
    header_at="Converting it into a memory prediction",
    art_at="Converting it into a memory prediction",
    note_head="THREE THINGS THE COUNT DOES NOT TELL YOU",
    note_items=[
        dict(t="WHAT PRECISION HOLDS THE ADAPTER VALUES",
             at="what precision holds those values"),
        dict(t="WHAT HOLDS THEIR GRADIENTS AND THE OPTIMIZER HISTORY",
             at="their gradients, and the optimizer history"),
        dict(t="AND EVERYTHING ELSE THE TRAINING RUN KEEPS LIVE",
             at="we still have to account for the rest of training"),
    ],
    tape="THE COUNT IS NOT THE BUDGET",
    tape_at="the rest of training",
    source="the QLoRA paper &middot; arxiv 2305.14314 &middot; the frozen "
           "base, the gradients, and the optimizer state are separate budgets",
    source_at="the rest of training")

# =====================================================================
# THE ARCHITECTURE, PART ONE
# =====================================================================
win("rows",
    vo="Use an actual architecture. Qwen two point five, three billion, "
       "Instruct has thirty-six layers and a hidden width of two thousand "
       "forty-eight. Its sixteen query heads share only two key and value "
       "heads.",
    kicker="LoRA &middot; THE ARCHITECTURE, SPECIFICALLY",
    title="QWEN 2.5 3B INSTRUCT",
    art="superchip",
    art_caption="THE SUPERCHIP",
    header_at="Use an actual architecture",
    art_at="Use an actual architecture",
    rows=[
        dict(rank="01", name="LAYERS", val="36", sub="BLOCKS", cls="gold",
             at="thirty-six layers"),
        dict(rank="02", name="HIDDEN WIDTH", val="2,048", sub="WIDTH",
             cls="", at="a hidden width of two thousand forty-eight"),
        dict(rank="03", name="QUERY HEADS", val="16", sub="ATTENTION",
             cls="", at="Its sixteen query heads"),
        dict(rank="04", name="KV HEADS", val="2", sub="SHARED", cls="red",
             at="share only two key and value heads"),
    ],
    closing=dict(c="gold", t="TWO KV HEADS SERVE SIXTEEN",
                 at="two key and value heads"),
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; "
           "2 kv heads &middot; head dim 128")

# =====================================================================
# THE ARCHITECTURE, PART TWO
# =====================================================================
win("nodes",
    vo="Each attention head is one hundred twenty-eight values wide. Two key "
       "and value heads serve sixteen query heads, so the value projection "
       "produces two hundred fifty-six outputs, not two thousand forty-eight. "
       "The narrow projections are the smaller ones to train.",
    kicker="LoRA &middot; THE ARCHITECTURE, SPECIFICALLY",
    title="WHERE THE WIDTH GOES",
    art="two_die",
    art_caption="TWO KV HEADS",
    header_at="Each attention head is",
    art_at="Each attention head is",
    chain=[
        dict(t="HEAD DIM", s="128 VALUES",
             at="one hundred twenty-eight values wide"),
        dict(t="KV HEADS", s="TWO", at="Two key and value heads"),
        dict(t="VALUE OUTPUT", s="256, NOT 2,048",
             at="two hundred fifty-six outputs, not two thousand forty-eight"),
    ],
    closing=dict(c="gold", t="NARROW PROJECTIONS, SMALLER ADAPTERS",
                 at="the smaller ones to train"),
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers &middot; "
           "2 kv heads &middot; head dim 128")

# =====================================================================
# THE PARAMETER COUNT
# =====================================================================
win("rows",
    vo="Put rank sixteen adapters on query and value only. The query "
       "projection adds sixty-five thousand five hundred thirty-six values "
       "per layer and the value projection thirty-six thousand eight hundred "
       "sixty-four. That is the whole adapter.",
    kicker="LoRA &middot; RANK 16, QUERY AND VALUE ONLY",
    title="TWO PROJECTIONS, THAT IS ALL",
    art="die",
    art_caption="THE DIE",
    header_at="Put rank sixteen adapters on query and value only",
    art_at="Put rank sixteen adapters on query and value only",
    rows=[
        dict(rank="Q", name="QUERY", val="65,536", sub="PER LAYER",
             cls="gold",
             at="sixty-five thousand five hundred thirty-six values per layer"),
        dict(rank="V", name="VALUE", val="36,864", sub="PER LAYER",
             cls="gold", at="thirty-six thousand eight hundred sixty-four"),
    ],
    closing=dict(c="gold", t="TWO PROJECTIONS, THAT IS ALL",
                 at="That is the whole adapter"),
    source="derived &middot; rank 16 &middot; query and value only &middot; "
           "qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; "
           "head dim 128")

# =====================================================================
# THE TOTAL, DERIVED
# =====================================================================
win("note",
    vo="Multiply by thirty-six layers and the total is three million, six "
       "hundred eighty-six thousand, four hundred parameters, with no trained "
       "biases. That count is derived, not measured.",
    kicker="LoRA &middot; RANK 16, QUERY AND VALUE ONLY",
    title="3,686,400 TRAINABLE",
    art="chip",
    art_caption="ONE FORMULA",
    header_at="the total is three million, six hundred eighty-six thousand, "
              "four hundred parameters",
    art_at="the total is three million, six hundred eighty-six thousand, "
           "four hundred parameters",
    note_head="WHERE THE COUNT COMES FROM",
    note_items=[
        dict(t="36 LAYERS MULTIPLY EVERY PROJECTION", at="thirty-six layers"),
        dict(t="NO TRAINED BIASES", at="with no trained biases"),
    ],
    tape="DERIVED, NOT MEASURED",
    tape_at="That count is derived, not measured",
    source="derived &middot; 3,686,400 values &middot; 36 layers &middot; "
           "qwen2.5 3b instruct &middot; 2 kv heads &middot; head dim 128",
    source_at="not measured")

# =====================================================================
# THE SAME RANK, MORE TARGETS
# =====================================================================
win("chain",
    vo="Expand that same rank to query, key, value, attention output, and the "
       "three feed-forward projections. The exact total is twenty-nine "
       "million, nine hundred thirty-three thousand, five hundred sixty-eight "
       "trainable parameters. The rank stays at sixteen.",
    kicker="LoRA &middot; SAME RANK, MORE TARGETS",
    title="29,933,568 TRAINABLE",
    art="riser",
    art_caption="VERTICAL RISER",
    header_at="Expand that same rank",
    art_at="Expand that same rank",
    chain=[
        dict(t="QUERY", s="TARGETED", at="to query"),
        dict(t="KEY AND VALUE", s="TARGETED", at="key, value"),
        dict(t="ATTENTION OUTPUT", s="TARGETED", at="attention output"),
        dict(t="FEED FORWARD x3", s="TARGETED",
             at="the three feed-forward projections"),
        dict(t="TOTAL", s="29,933,568",
             at="twenty-nine million, nine hundred thirty-three thousand, five hundred sixty-eight"),
    ],
    compare=[
        dict(cls="hot", title="THE TOTAL",
             body="Twenty-nine point nine three million trainable values.",
             at="trainable parameters"),
        dict(cls="good", title="THE RANK",
             body="Still sixteen, on every projection.",
             at="The rank stays at sixteen"),
    ],
    source="derived &middot; rank 16 &middot; seven projections &middot; "
           "qwen2.5 3b instruct &middot; 36 layers &middot; 2 kv heads &middot; "
           "head dim 128")

# =====================================================================
# THE BASE MODEL DID NOT MOVE
# =====================================================================
win("rows",
    vo="The base architecture did not change, and the places you allowed it to "
       "adapt changed. That is the whole difference between the two counts you "
       "just computed.",
    kicker="LoRA &middot; SAME RANK, MORE TARGETS",
    title="MORE PLACES, SAME RANK",
    art="model_file",
    art_caption="MODEL FILE",
    header_at="The base architecture did not change",
    art_at="The base architecture did not change",
    rows=[
        dict(rank="01", name="THE PLACES TO ADAPT", val="SEVEN",
             sub="INSTEAD OF TWO", cls="gold",
             at="the places you allowed it to adapt changed"),
        dict(rank="02", name="THE WHOLE DIFFERENCE", val="THE TARGETS",
             sub="NOT THE RANK", cls="",
             at="the whole difference"),
    ],
    closing=dict(c="gold", t="MORE PLACES, SAME RANK",
                 at="the two counts you just computed"),
    source="derived &middot; rank 16 &middot; two projections against seven "
           "&middot; qwen2.5 3b instruct")

# =====================================================================
# WHAT TO ASK
# =====================================================================
win("note",
    vo="That is why somebody else saying rank sixteen is insufficient "
       "information. Ask which projections, which layers, whether embeddings "
       "or biases are trained, and what precision the implementation actually "
       "uses. A small rank is a setting. It is not a complete training "
       "specification.",
    kicker="LoRA &middot; WHAT TO ASK",
    title="RANK IS NOT A SPECIFICATION",
    art="question",
    art_caption="FOUR QUESTIONS",
    header_at="That is why somebody else saying rank sixteen",
    art_at="That is why somebody else saying rank sixteen",
    note_head="FOUR QUESTIONS THAT DECIDE THE BILL",
    note_items=[
        dict(t="WHICH PROJECTIONS ARE TARGETED", at="Ask which projections"),
        dict(t="WHICH LAYERS ARE TARGETED", at="which layers"),
        dict(t="ARE EMBEDDINGS OR BIASES TRAINED",
             at="whether embeddings or biases are trained"),
        dict(t="WHAT PRECISION THE IMPLEMENTATION USES",
             at="what precision the implementation actually uses"),
    ],
    tape="A SMALL RANK IS A SETTING",
    tape_at="A small rank is a setting",
    source="the LoRA paper &middot; arxiv 2106.09685 &middot; rank, target "
           "modules, and precision are separate choices",
    source_at="It is not a complete training specification")

# =====================================================================
# THE ORIGINAL LoRA PAPER
# =====================================================================
win("rows",
    vo="On GPT three with one hundred seventy-five billion parameters, full "
       "fine-tuning scored seventy-three point eight on Wiki SQL and "
       "eighty-nine point five on matched Multi N L I. A LoRA row with four "
       "point seven million scored seventy-three point four and ninety-one "
       "point seven. Those are the paper's own numbers.",
    kicker="THE ORIGINAL LoRA PAPER &middot; GPT-3 175B",
    title="TASK RESULTS, NOT A PROOF",
    art="scales",
    art_caption="TASK EVALUATION",
    header_at="On GPT three with one hundred seventy-five billion",
    art_at="On GPT three with one hundred seventy-five billion",
    rows=[
        dict(rank="FT", name="FULL FINE-TUNE", val="73.8", sub="WIKISQL",
             cls="", at="seventy-three point eight on Wiki SQL"),
        dict(rank="FT", name="FULL FINE-TUNE", val="89.5", sub="MNLI",
             cls="", at="eighty-nine point five on matched Multi N L I"),
        dict(rank="LR", name="LoRA 4.7M", val="73.4", sub="WIKISQL",
             cls="gold", at="A LoRA row with four point seven million"),
        dict(rank="LR", name="LoRA 4.7M", val="91.7", sub="MNLI",
             cls="gold", at="ninety-one point seven"),
    ],
    closing=dict(c="gold", t="THE PAPER'S OWN NUMBERS",
                 at="Those are the paper's own numbers"),
    source="the LoRA paper &middot; arxiv 2106.09685 &middot; WikiSQL and "
           "matched Multi N L I")

# =====================================================================
# WHOSE RESULT IS THIS
# =====================================================================
win("note",
    vo="Those are the original authors' task results, with task-specific "
       "variation, not measurements from this channel or promises for a "
       "desktop model. Now separate LoRA from quantized LoRA, because they "
       "are not the same method.",
    kicker="THE ORIGINAL LoRA PAPER &middot; READ THE ROW CORRECTLY",
    title="WHOSE RESULT IS THIS",
    art="magnifier",
    art_caption="READ THE FINE PRINT",
    header_at="Those are the original authors' task results",
    art_at="Those are the original authors' task results",
    note_head="THIS IS NOT YOUR MODEL AND NOT OUR HARDWARE",
    note_items=[
        dict(t="WITH TASK SPECIFIC VARIATION", at="with task-specific variation"),
        dict(t="NOT A MEASUREMENT FROM THIS CHANNEL",
             at="not measurements from this channel"),
        dict(t="NOT A PROMISE FOR A DESKTOP MODEL",
             at="or promises for a desktop model"),
    ],
    tape="SEPARATE LoRA FROM QUANTIZED LoRA",
    tape_at="Now separate LoRA from quantized LoRA",
    source="the LoRA paper &middot; arxiv 2106.09685 &middot; GPT-3 175B task "
           "results",
    source_at="not the same method")

# =====================================================================
# LoRA AND QUANTIZED LoRA
# =====================================================================
win("gallery",
    vo="Quantized LoRA keeps the small trainable matrices and changes how the "
       "frozen base is stored. The base sits in a reduced precision, and the "
       "adapters still train in a higher one. One method, two different "
       "memory bills.",
    kicker="LoRA &middot; TWO METHODS, TWO BILLS",
    title="LoRA AND QLoRA",
    art="gguf_blocks",
    art_caption="MIXED PRECISION",
    header_at="Quantized LoRA keeps the small trainable matrices",
    art_at="Quantized LoRA keeps the small trainable matrices",
    name="TWO DIFFERENT MEMORY BILLS",
    blurb="The base sits in a reduced precision, and the adapters still train in a higher one.",
    meta="one method, two different memory bills",
    name_at="changes how the frozen base is stored",
    blurb_at="The base sits in a reduced precision",
    meta_at="One method, two different memory bills",
    side="left",
    source="the QLoRA paper &middot; arxiv 2305.14314")

# =====================================================================
# THE FINAL QLoRA PAPER
# =====================================================================
win("rows",
    vo="In the final QLoRA paper, a Llama seven billion model tuned on "
       "Alpaca scored thirty-eight point four on five-shot M M L U using "
       "brain float sixteen adapter tuning. Normal float four with double "
       "quantization scored thirty-nine point zero.",
    kicker="THE FINAL QLoRA PAPER &middot; LLAMA 7B ON ALPACA",
    title="ADAPTER TRAINING PRECISIONS",
    art="gguf_blocks",
    art_caption="MIXED PRECISION",
    header_at="In the final QLoRA paper",
    art_at="In the final QLoRA paper",
    rows=[
        dict(rank="B16", name="BF16 ADAPTER", val="38.4", sub="5-SHOT MMLU",
             cls="", at="scored thirty-eight point four on five-shot"),
        dict(rank="N4Q", name="NF4 + DQ", val="39.0", sub="5-SHOT MMLU",
             cls="gold",
             at="Normal float four with double quantization scored thirty-nine point zero"),
    ],
    closing=dict(c="red", t="THESE ROWS COMPARE PRECISIONS",
                 at="scored thirty-nine point zero"),
    source="the QLoRA paper &middot; arxiv 2305.14314 &middot; Llama 7B on "
           "Alpaca, five-shot MMLU")

# =====================================================================
# THE MOVEMENT
# =====================================================================
win("bars",
    vo="On F L A N version two, the corresponding scores were forty-five point "
       "six for brain float sixteen and forty-four point five for normal "
       "float four. One dataset moved up zero point six points, the other "
       "down one point one. It has a boundary: the named model, datasets, "
       "methods, and evaluation.",
    kicker="THE FINAL QLoRA PAPER &middot; THE MOVEMENT",
    title="PLUS ZERO POINT SIX. MINUS ONE POINT ONE.",
    art="gauge",
    art_caption="THE DIAL",
    header_at="On F L A N version two",
    art_at="On F L A N version two",
    bars=[
        dict(lab="FLAN V2, BF16", val="45.6", unit="POINTS", pct=100.0,
             cls="", at="forty-five point six for brain float sixteen"),
        dict(lab="FLAN V2, NF4 + DQ", val="44.5", unit="POINTS", pct=97.6,
             cls="red", at="forty-four point five for normal float four"),
    ],
    mid=dict(c="", t="ONE UP 0.6 &middot; ONE DOWN 1.1",
             at="One dataset moved up zero point six points"),
    closing=dict(c="gold", t="IT HAS A BOUNDARY",
                 at="datasets, methods, and evaluation"),
    source="the QLoRA paper &middot; arxiv 2305.14314 &middot; FLAN v2 scores "
           "and the percentage point movement")

# =====================================================================
# WHERE THE RESULT STOPS
# =====================================================================
win("note",
    vo="It does not establish that four-bit training improves every task. It "
       "does not tell us whether our Qwen adapter follows an internal coding "
       "convention, or whether your data follows one.",
    kicker="THE FINAL QLoRA PAPER &middot; WHERE THE RESULT STOPS",
    title="THE ONLY NUMBER THAT ALWAYS IMPROVES",
    art="folder",
    art_caption="SAVED TO DISK",
    header_at="It does not establish that four-bit training",
    art_at="It does not establish that four-bit training",
    note_head="WHAT THESE ROWS DO NOT ESTABLISH",
    note_items=[
        dict(t="THAT FOUR BIT TRAINING IMPROVES EVERY TASK",
             at="four-bit training improves every task"),
        dict(t="WHETHER OUR QWEN ADAPTER FOLLOWS A CONVENTION",
             at="our Qwen adapter follows an internal coding convention"),
        dict(t="WHETHER YOUR DATA FOLLOWS ONE",
             at="whether your data follows one"),
    ],
    tape="THE BOUNDARY OF THE RESULT",
    tape_at="whether your data follows one",
    source="the QLoRA paper &middot; arxiv 2305.14314 &middot; results are "
           "scoped to the named model and datasets",
    source_at="whether your data follows one")

# =====================================================================
# WRITE THE TARGET DOWN FIRST
# =====================================================================
win("rows",
    vo="For that decision, write down the behavior you want to change and "
       "examples that test it before training begins. The only number "
       "guaranteed to improve is the number of checkpoints on disk.",
    kicker="THE FINAL QLoRA PAPER &middot; WHERE THE RESULT STOPS",
    title="THE ONLY NUMBER THAT ALWAYS IMPROVES",
    art="checklist",
    art_caption="THE CHECKLIST",
    header_at="For that decision, write down the behavior",
    art_at="For that decision, write down the behavior",
    rows=[
        dict(rank="01", name="THE BEHAVIOUR TO CHANGE", val="WRITE IT DOWN",
             sub="BEFORE YOU ALLOCATE", cls="gold",
             at="write down the behavior you want to change"),
        dict(rank="02", name="THE EXAMPLES THAT TEST IT",
             val="BEFORE TRAINING", sub="NOT AFTER", cls="",
             at="examples that test it before training begins"),
        dict(rank="03", name="THE CHECKPOINT COUNT", val="ALWAYS RISES",
             sub="AND NOTHING ELSE", cls="red",
             at="The only number guaranteed to improve"),
    ],
    closing=dict(c="red", t="THE NUMBER OF CHECKPOINTS ON DISK",
                 at="the number of checkpoints on disk"),
    source="mechanism &middot; write the target behaviour and the test cases "
           "before training begins")

# =====================================================================
# THE FAMOUS DEMONSTRATION
# =====================================================================
win("chain",
    vo="The famous sixty-five-billion model on a forty-eight-gigabyte GPU is "
       "also a scoped research demonstration. Keep the original recipe "
       "attached to that sentence. It is not a universal allowance for longer "
       "examples, a different architecture, or arbitrary batch sizes. The "
       "scope travels with the number.",
    kicker="THE FAMOUS DEMONSTRATION &middot; 65B ON A 48GB GPU",
    title="A SCOPED RESEARCH DEMONSTRATION",
    art="rack_server",
    art_caption="RACK SERVER",
    header_at="The famous sixty-five-billion model",
    art_at="The famous sixty-five-billion model",
    chain=[
        dict(t="MODEL", s="65B PARAMETERS",
             at="sixty-five-billion model on a forty-eight-gigabyte GPU"),
        dict(t="ONE DEVICE", s="48 GB",
             at="a forty-eight-gigabyte GPU"),
        dict(t="SCOPE", s="RESEARCH",
             at="a scoped research demonstration"),
        dict(t="NOT INCLUDED", s="LONGER EXAMPLES",
             at="longer examples"),
        dict(t="NOT INCLUDED", s="ARBITRARY BATCH SIZES",
             at="arbitrary batch sizes"),
    ],
    compare=[
        dict(cls="hot", title="A SCOPED DEMONSTRATION",
             body="Keep the original recipe attached to that sentence.",
             at="Keep the original recipe attached to that sentence"),
        dict(cls="good", title="NOT AN ALLOWANCE",
             body="It is not a universal allowance for other examples, architectures, or batch sizes.",
             at="not a universal allowance"),
    ],
    closing=dict(c="gold", t="ATTACH THE RECIPE TO THE NUMBER",
                 at="The scope travels with the number"),
    source="the QLoRA paper &middot; arxiv 2305.14314 &middot; the 65B and 48GB "
           "demonstration, with its recipe")

# =====================================================================
# HOW TO USE IT
# =====================================================================
win("note",
    vo="Treat it as evidence that quantized adapter training can make a "
       "previously inaccessible experiment possible. Then budget your own "
       "experiment. An engineering result becomes misleading when the "
       "equipment and settings disappear while the headline survives.",
    kicker="THE FAMOUS DEMONSTRATION &middot; HOW TO USE IT",
    title="EVIDENCE, NOT AN ALLOWANCE",
    art="cloud",
    art_caption="NOT THE CLOUD",
    header_at="Treat it as evidence that quantized adapter training",
    art_at="Treat it as evidence that quantized adapter training",
    note_head="WHAT THE DEMONSTRATION ESTABLISHES",
    note_items=[
        dict(t="IT CAN MAKE AN INACCESSIBLE EXPERIMENT POSSIBLE",
             at="can make a previously inaccessible experiment possible"),
        dict(t="THEN BUDGET YOUR OWN EXPERIMENT",
             at="Then budget your own experiment"),
        dict(t="KEEP THE EQUIPMENT AND THE SETTINGS WITH THE HEADLINE",
             at="the equipment and settings disappear while the headline survives"),
    ],
    tape="EVIDENCE, NOT AN ALLOWANCE",
    tape_at="while the headline survives",
    source="the QLoRA paper &middot; arxiv 2305.14314 &middot; a 65B model "
           "tuned on a single 48GB GPU",
    source_at="while the headline survives")

# =====================================================================
# FOUR BITS HIDES THINGS, PART ONE
# =====================================================================
win("rows",
    vo="Four-bit training does not mean every training tensor uses four bits. "
       "In the documented bits and bytes route, normal float four stores the "
       "converted base weights, and a separate compute setting selects the "
       "arithmetic precision. Our configuration uses brain float sixteen "
       "computation on compatible hardware.",
    kicker="THE RUNTIME MEMORY &middot; FOUR BITS HIDES THINGS",
    title="SEPARATE LINES IN A BUDGET",
    art="gguf_blocks",
    art_caption="MIXED PRECISION",
    header_at="Four-bit training does not mean every training tensor",
    art_at="Four-bit training does not mean every training tensor",
    rows=[
        dict(rank="01", name="BASE WEIGHTS", val="NF4", sub="STORED",
             cls="gold", at="normal float four stores the converted base weights"),
        dict(rank="02", name="COMPUTE", val="BF16", sub="ARITHMETIC",
             cls="gold",
             at="a separate compute setting selects the arithmetic precision"),
        dict(rank="03", name="OUR CONFIGURATION", val="BF16",
             sub="ON COMPATIBLE HARDWARE", cls="",
             at="brain float sixteen computation on compatible hardware"),
    ],
    closing=dict(c="red", t="FOUR BITS IS NOT EVERY TENSOR",
                 at="on compatible hardware"),
    source="mechanism &middot; the documented bits and bytes route &middot; a "
           "4-bit stored base with a 16-bit compute dtype")

# =====================================================================
# FOUR BITS HIDES THINGS, PART TWO
# =====================================================================
win("note",
    vo="The adapters are extra trainable tensors on top of the frozen base. "
       "Activations, gradients, and optimizer states have their own "
       "representations. Read those settings as separate lines in a budget, "
       "and name the precision for each one.",
    kicker="THE RUNTIME MEMORY &middot; FOUR BITS HIDES THINGS",
    title="SEPARATE LINES IN A BUDGET",
    art="scales",
    art_caption="THE SCALES",
    header_at="The adapters are extra trainable tensors",
    art_at="The adapters are extra trainable tensors",
    note_head="SEPARATE LINES IN A BUDGET",
    note_items=[
        dict(t="ACTIVATIONS, GRADIENTS, AND OPTIMIZER STATES",
             at="Activations, gradients, and optimizer states"),
        dict(t="EACH HAS ITS OWN REPRESENTATION",
             at="have their own representations"),
        dict(t="NAME THE PRECISION FOR EACH ONE",
             at="name the precision for each one"),
    ],
    tape="READ THE SETTINGS AS SEPARATE LINES",
    tape_at="separate lines in a budget",
    source="the QLoRA paper &middot; arxiv 2305.14314 &middot; a 4-bit base, a "
           "16-bit compute dtype, and adapter tensors",
    source_at="name the precision for each one")

# =====================================================================
# THE SCALES ARE NOT FREE
# =====================================================================
win("rows",
    vo="Multiplying the model's advertised parameter count by half a byte does "
       "not produce the peak. Even the converted weights need their scales: a "
       "scale stored in thirty-two bits for each block of sixty-four weights "
       "adds half a bit per weight. That is four and a half bits, before the "
       "scales shrink.",
    kicker="THE RUNTIME MEMORY &middot; THE SCALES ARE NOT FREE",
    title="FOUR AND A HALF, BEFORE THE SCALES SHRINK",
    art="cache_grid",
    art_caption="L2 / L3 CACHE",
    header_at="Multiplying the model's advertised parameter count",
    art_at="Multiplying the model's advertised parameter count",
    rows=[
        dict(rank="01", name="HALF A BYTE", val="NOT THE PEAK",
             sub="THE CONVERTED WEIGHTS NEED SCALES", cls="red",
             at="does not produce the peak"),
        dict(rank="02", name="SCALE WIDTH", val="32 BIT",
             sub="PER BLOCK OF 64", cls="gold",
             at="a scale stored in thirty-two bits"),
        dict(rank="03", name="SCALE OVERHEAD", val="+0.5 BIT",
             sub="PER WEIGHT", cls="red", at="adds half a bit per weight"),
        dict(rank="04", name="BEFORE THE SCALES SHRINK", val="4.5 BIT",
             sub="PER WEIGHT", cls="gold", at="four and a half bits"),
    ],
    closing=dict(c="gold", t="THAT IS NOT FOUR EITHER",
                 at="before the scales shrink"),
    source="mechanism &middot; a 32-bit scale for every block of 64 weights "
           "adds 0.5 bit per weight")

# =====================================================================
# THE SCALES SHRINK TOO
# =====================================================================
win("chain",
    vo="Nested quantization compresses the scales as well, taking back zero "
       "point three seven three of a bit. The large-tensor average becomes "
       "four point one two seven bits per weight. It is larger than four "
       "bits, and it says nothing about tensors the loader did not convert. "
       "Read it as an average.",
    kicker="THE RUNTIME MEMORY &middot; THE SCALES ARE NOT FREE",
    title="4.127 BITS, NOT FOUR",
    art="cache_grid",
    art_caption="L2 / L3 CACHE",
    header_at="Nested quantization",
    art_at="Nested quantization",
    chain=[
        dict(t="NESTED", s="the scales shrink too",
             at="compresses the scales as well"),
        dict(t="TAKEN BACK", s="0.373 BIT PER WEIGHT",
             at="zero point three seven three of a bit"),
        dict(t="AVERAGE", s="4.127 BITS PER WEIGHT",
             at="four point one two seven bits per weight"),
    ],
    compare=[
        dict(cls="good", title="REAL COMPRESSION",
             body="Nested quantization shrinks the scales as well.",
             at="the scales as well"),
        dict(cls="hot", title="NOT FOUR",
             body="It says nothing about the tensors the loader did not convert.",
             at="tensors the loader did not convert"),
    ],
    closing=dict(c="gold", t="READ IT AS AN AVERAGE, NOT A PROMISE",
                 at="Read it as an average"),
    source="mechanism &middot; nested quantization in the pinned implementation "
           "&middot; 4.127 bits per converted weight")

# =====================================================================
# THE QUIETER TRAP, PART ONE
# =====================================================================
win("rows",
    vo="Here is a quieter trap. The pinned P E F T preparation function "
       "freezes the base and promotes ordinary half-precision parameters to "
       "full precision, excluding the special four-bit parameters. That "
       "promotion is a full precision component you cannot see from the "
       "label.",
    kicker="THE RUNTIME MEMORY &middot; THE QUIETER TRAP",
    title="A FULL PRECISION COMPONENT",
    art="ram_stick",
    art_caption="SYSTEM MEMORY",
    header_at="Here is a quieter trap",
    art_at="Here is a quieter trap",
    rows=[
        dict(rank="01", name="PEFT PREPARATION", val="FREEZES THE BASE",
             sub="", cls="",
             at="The pinned P E F T preparation function"),
        dict(rank="02", name="HALF PRECISION", val="PROMOTED TO FP32",
             sub="", cls="gold", at="promotes ordinary half-precision parameters"),
        dict(rank="03", name="FOUR BIT PARAMS", val="EXCLUDED", sub="",
             cls="", at="excluding the special four-bit parameters"),
        dict(rank="04", name="WHAT THE LABEL HIDES", val="FP32 COMPONENT",
             sub="", cls="red",
             at="a full precision component you cannot see from the label"),
    ],
    closing=dict(c="red", t="A FOUR BIT LABEL IS NOT ALL FOUR BITS",
                 at="from the label"),
    source="mechanism &middot; the pinned P E F T preparation promotes half "
           "precision parameters to fp32")

# =====================================================================
# THE QUIETER TRAP, PART TWO
# =====================================================================
win("note",
    vo="Our Qwen model has a tied vocabulary embedding. That embedding "
       "contains about three hundred eleven million values, and at four bytes "
       "each it is about one point two four five decimal gigabytes. This is "
       "derived tensor arithmetic, not an allocation measurement.",
    kicker="THE RUNTIME MEMORY &middot; THE QUIETER TRAP",
    title="A FULL PRECISION COMPONENT",
    art="memory_bank",
    art_caption="MEMORY BANK",
    header_at="Our Qwen model has a tied vocabulary embedding",
    art_at="Our Qwen model has a tied vocabulary embedding",
    note_head="WHAT THE FOUR BIT LABEL HIDES",
    note_items=[
        dict(t="A TIED VOCABULARY EMBEDDING",
             at="That embedding contains"),
        dict(t="ABOUT 311M VALUES",
             at="about three hundred eleven million values"),
        dict(t="ABOUT 1.245 DECIMAL GIGABYTES AT FOUR BYTES EACH",
             at="about one point two four five decimal gigabytes"),
        dict(t="DERIVED, NOT AN ALLOCATION MEASUREMENT",
             at="derived tensor arithmetic, not an allocation measurement"),
    ],
    tape="A FOUR BIT LABEL IS NOT ALL FOUR BITS",
    tape_at="not an allocation measurement",
    source="derived &middot; qwen2.5 3b instruct &middot; tied vocabulary "
           "embedding &middot; fp32 at 4 bytes per value",
    source_at="not an allocation measurement")

# =====================================================================
# PLACEMENT
# =====================================================================
win("rows",
    vo="Placement is another separate decision. The pinned Transformers guide "
       "says automatic device mapping is for inference. It is not evidence "
       "that an inference offload layout is a valid training layout. Our "
       "inspection plan names one CUDA device explicitly and disables the "
       "inference cache. Neither choice manufactures memory.",
    kicker="THE RUNTIME MEMORY &middot; PLACEMENT",
    title="INFERENCE MAPPING IS NOT TRAINING MAPPING",
    art="mac_mini",
    art_caption="MINI PC",
    header_at="Placement is another separate decision",
    art_at="Placement is another separate decision",
    rows=[
        dict(rank="01", name="AUTOMATIC DEVICE MAPPING", val="INFERENCE",
             sub="NOT A TRAINING LAYOUT", cls="red",
             at="automatic device mapping is for inference"),
        dict(rank="02", name="OUR INSPECTION PLAN", val="ONE CUDA DEVICE",
             sub="NAMED EXPLICITLY", cls="gold",
             at="Our inspection plan names one CUDA device"),
        dict(rank="03", name="THE INFERENCE CACHE", val="DISABLED", sub="",
             cls="", at="disables the inference cache"),
        dict(rank="04", name="NEITHER CHOICE", val="MANUFACTURES MEMORY",
             sub="", cls="", at="Neither choice manufactures memory"),
    ],
    closing=dict(c="gold", t="PLACEMENT IS A SEPARATE DECISION",
                 at="manufactures memory"),
    source="mechanism &middot; the pinned Transformers guide &middot; device_map "
           "is documented for inference")

# =====================================================================
# THE CACHE IS NOT THE TRAINING TENSORS
# =====================================================================
win("chain",
    vo="Disabling the cache removes a mechanism for reusing past keys and "
       "values during generation. It does not remove the tensors needed to "
       "differentiate a training example. A successful loader is still only "
       "the beginning of the experiment, and the experiment is the expensive "
       "part.",
    kicker="THE RUNTIME MEMORY &middot; WHAT THE CACHE IS NOT",
    title="A LOADER IS NOT AN EXPERIMENT",
    art="switch",
    art_caption="NETWORK SWITCH",
    header_at="Disabling the cache removes a mechanism",
    art_at="Disabling the cache removes a mechanism",
    chain=[
        dict(t="CACHE", s="removes reuse of past keys and values",
             at="for reusing past keys and values"),
        dict(t="TRAINING TENSORS", s="still required",
             at="the tensors needed to differentiate a training example"),
        dict(t="LOADER", s="only the beginning",
             at="still only the beginning of the experiment"),
    ],
    compare=[
        dict(cls="hot", title="GENERATION ONLY",
             body="Reuse of past keys and values is an inference mechanism.",
             at="during generation"),
        dict(cls="good", title="TRAINING",
             body="The tensors needed to differentiate a training example remain.",
             at="differentiate a training example"),
    ],
    closing=dict(c="gold", t="THE TENSORS STILL HAVE TO FIT",
                 at="the experiment is the expensive part"),
    source="mechanism &middot; the pinned Transformers guide &middot; the "
           "inference cache is a generation mechanism")

# =====================================================================
# THE CONTROLS THAT DO SOMETHING, PART ONE
# =====================================================================
win("rows",
    vo="The useful controls change different parts of that experiment. "
       "Gradient checkpointing saves fewer intermediate tensors and recomputes "
       "them during backward, trading additional work for memory. A microbatch "
       "of one keeps fewer examples live together.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; THE CONTROLS THAT DO SOMETHING",
    title="TRADING WORK FOR MEMORY",
    art="fan",
    art_caption="THE FAN",
    header_at="The useful controls change different parts",
    art_at="The useful controls change different parts",
    rows=[
        dict(rank="01", name="GRADIENT CHECKPOINTING", val="FEWER",
             sub="TENSORS LIVE", cls="gold",
             at="Gradient checkpointing saves fewer intermediate tensors"),
        dict(rank="02", name="RECOMPUTED", val="ON BACKWARD",
             sub="TRADING WORK", cls="", at="recomputes them during backward"),
        dict(rank="03", name="MICROBATCH", val="1", sub="EXAMPLE AT A TIME",
             cls="gold", at="A microbatch of one keeps fewer examples"),
    ],
    closing=dict(c="cyan", t="TRADING WORK FOR MEMORY",
                 at="live together"),
    source="mechanism &middot; gradient checkpointing recomputes the graph, a "
           "microbatch of one keeps one example live")

# =====================================================================
# THE CONTROLS THAT DO SOMETHING, PART TWO
# =====================================================================
win("note",
    vo="Accumulating eight such microsteps builds an effective batch of eight "
       "on one device, without processing all eight simultaneously. Sequence "
       "length remains its own control, and these choices do not guarantee "
       "the same optimization behavior in every implementation.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; THE CONTROLS THAT DO SOMETHING",
    title="SPECIFIC VARIABLES, NOT GUARANTEES",
    art="meter",
    art_caption="THE METER",
    header_at="Accumulating eight such microsteps",
    art_at="Accumulating eight such microsteps",
    note_head="THE CONTROLS, AND THEIR LIMITS",
    note_items=[
        dict(t="AN EFFECTIVE BATCH OF EIGHT ON ONE DEVICE",
             at="builds an effective batch of eight on one device"),
        dict(t="WITHOUT PROCESSING ALL EIGHT SIMULTANEOUSLY",
             at="without processing all eight simultaneously"),
        dict(t="SEQUENCE LENGTH IS ITS OWN CONTROL",
             at="Sequence length remains its own control"),
        dict(t="THE SAME BEHAVIOUR IS NOT GUARANTEED EVERYWHERE",
             at="do not guarantee the same optimization behavior"),
    ],
    tape="SPECIFIC VARIABLES, NOT GUARANTEES",
    tape_at="in every implementation",
    source="mechanism &middot; gradient accumulation builds the effective batch "
           "without holding every microbatch",
    source_at="in every implementation")

# =====================================================================
# THE ADAPTER ARRAYS
# =====================================================================
win("rows",
    vo="Return to the twenty-nine point nine three million parameter adapter. Assume "
       "full-precision adapter weights at four bytes each, full-precision "
       "gradients at four bytes each, and two full-precision Adam moment "
       "buffers, eight bytes together. That is sixteen bytes per trainable "
       "value.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; THE ADAPTER ARRAYS",
    title="16 BYTES PER TRAINABLE VALUE",
    art="memory_bank",
    art_caption="MEMORY BANK",
    header_at="Return to the twenty-nine point nine three million parameter adapter",
    art_at="Return to the twenty-nine point nine three million parameter adapter",
    rows=[
        dict(rank="01", name="ADAPTER WEIGHTS", val="4 B", sub="FULL PRECISION",
             cls="", at="full-precision adapter weights at four bytes each"),
        dict(rank="02", name="GRADIENTS", val="4 B", sub="FULL PRECISION",
             cls="", at="full-precision gradients at four bytes each"),
        dict(rank="03", name="ADAM MOMENTS", val="8 B", sub="TWO BUFFERS",
             cls="", at="eight bytes together"),
        dict(rank="04", name="PER TRAINABLE VALUE", val="16 B", sub="DERIVED",
             cls="gold", at="sixteen bytes per trainable value"),
    ],
    closing=dict(c="red", t="THAT IS ONLY THE ADAPTER",
                 at="sixteen bytes per trainable value"),
    source="derived &middot; 16 bytes per trainable value &middot; fp32 weight, "
           "fp32 gradient, two fp32 Adam moments")

# =====================================================================
# THE ADAPTER SUBTOTAL
# =====================================================================
win("chain",
    vo="Our exact count is twenty-nine million, nine hundred thirty-three thousand, five "
       "hundred sixty-eight trainable values. Sixteen bytes per value yields "
       "four hundred fifty-six point seven five mebibytes for those four arrays. "
       "That is a theoretical adapter subtotal, not your full training footprint.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; THE ADAPTER SUBTOTAL",
    title="456.75 MiB THEORETICAL",
    art="gauge",
    art_caption="THE DIAL",
    header_at="Our exact count is twenty-nine million",
    art_at="Our exact count is twenty-nine million",
    chain=[
        dict(t="EXACT COUNT", s="29,933,568 VALUES",
             at="twenty-nine million, nine hundred thirty-three thousand, five hundred sixty-eight"),
        dict(t="PER VALUE", s="16 BYTES", at="Sixteen bytes per value yields"),
        dict(t="THE FOUR ARRAYS", s="456.75 MiB",
             at="four hundred fifty-six point seven five mebibytes"),
    ],
    compare=[
        dict(cls="good", title="456.75 MiB",
             body="The exact count times sixteen bytes, for the theoretical adapter state alone.",
             at="for those four arrays"),
        dict(cls="hot", title="SUBTOTAL ONLY",
             body="Excludes frozen base, activations, and runtime workspaces.",
             at="theoretical adapter subtotal"),
    ],
    closing=dict(c="gold", t="456.75 MiB ADAPTER ARRAYS ALONE", at="not your full training footprint"),
    source="derived &middot; 29,933,568 values x 16 bytes = 478,937,088 bytes "
           "= 456.75 MiB &middot; rank 16 &middot; qwen2.5 3b instruct")

# =====================================================================
# WHAT THE SUBTOTAL EXCLUDES
# =====================================================================
win("note",
    vo="That subtotal covers the adapter arrays only. The frozen base, the "
       "saved activations, and the temporary workspaces all sit outside it, "
       "and so does anything else the implementation keeps. Calling it the "
       "required video memory would erase most of the question we came here "
       "to answer.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; WHAT THE SUBTOTAL IS NOT",
    title="DO NOT CALL IT VIDEO MEMORY",
    art="magnifier",
    art_caption="READ THE FINE PRINT",
    header_at="That subtotal covers the adapter arrays only",
    art_at="That subtotal covers the adapter arrays only",
    note_head="WHAT THE SUBTOTAL EXCLUDES",
    note_items=[
        dict(t="THE FROZEN BASE", at="The frozen base"),
        dict(t="THE SAVED ACTIVATIONS", at="the saved activations"),
        dict(t="THE TEMPORARY WORKSPACES", at="the temporary workspaces"),
        dict(t="ANYTHING ELSE THE IMPLEMENTATION KEEPS",
             at="anything else the implementation keeps"),
    ],
    tape="THE SUBTOTAL IS NOT THE WHOLE BILL",
    tape_at="we came here to answer",
    source="mechanism &middot; the adapter arrays are one line of the budget, "
           "not the whole of it",
    source_at="we came here to answer")

# =====================================================================
# STARTING POINTS
# =====================================================================
win("rail",
    vo="On eight gigabytes, regard the three-billion family as a constrained "
       "experiment candidate. Start with short examples, perhaps five hundred "
       "twelve tokens, a microbatch of one, and checkpointing. Those are "
       "starting choices, not a tested fit claim, so on twelve gigabytes "
       "retain that controlled setup first.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; STARTING POINTS",
    title="EIGHT AND TWELVE GIGABYTES",
    art="mini_pc",
    art_caption="MINI PC",
    header_at="On eight gigabytes",
    art_at="On eight gigabytes",
    rails=[
        dict(lab="AT 8 GB", val="512 TOKENS", pct=41.0, cls="",
             at="Start with short examples, perhaps five hundred twelve"),
        dict(lab="MICROBATCH", val="1 EXAMPLE", pct=12.0, cls="",
             at="a microbatch of one"),
        dict(lab="AT 12 GB", val="SAME SETUP", pct=60.0, cls="red",
             at="so on twelve gigabytes retain that controlled setup"),
    ],
    closing=dict(c="gold", t="STARTING CHOICES, NOT A FIT CLAIM",
                 at="retain that controlled setup first"),
    source="mechanism &middot; a controlled starting setup of 512 tokens, a "
           "microbatch of one, and gradient checkpointing")

# =====================================================================
# MEASURE THE WHOLE THING
# =====================================================================
win("note",
    vo="Measure a complete training step: a forward pass, a backward pass, and "
       "an optimizer update. An optimizer can allocate state when the first "
       "update happens, so a forward-only demonstration can miss the failure "
       "that matters.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; MEASURE THE WHOLE THING",
    title="THE FIRST UPDATE IS WHERE IT BREAKS",
    art="warning",
    art_caption="WARNING",
    header_at="Measure a complete training step",
    art_at="Measure a complete training step",
    note_head="MEASURE ALL THREE PASSES",
    note_items=[
        dict(t="A COMPLETE FORWARD PASS", at="a forward pass"),
        dict(t="A COMPLETE BACKWARD PASS", at="a backward pass"),
        dict(t="A COMPLETE OPTIMIZER UPDATE", at="an optimizer update"),
        dict(t="A FORWARD ONLY DEMONSTRATION MISSES THE FAILURE",
             at="a forward-only demonstration can miss the failure that matters"),
    ],
    tape="THE FIRST UPDATE IS WHERE IT BREAKS",
    tape_at="can miss the failure that matters",
    source="mechanism &middot; the optimizer allocates its state on the first "
           "update",
    source_at="when the first update happens")

# =====================================================================
# MORE ROOM, MORE QUESTIONS
# =====================================================================
win("rail",
    vo="At sixteen gigabytes, you have more freedom to test broader adapter "
       "targets or longer examples, one change at a time. At twenty-four, a "
       "seven-billion experiment becomes another candidate to investigate "
       "after the smaller control works. Neither capacity guarantees full "
       "fine-tuning or a long-context run.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; MORE ROOM",
    title="SIXTEEN AND TWENTY FOUR",
    art="tower_pc",
    art_caption="TOWER PC",
    header_at="At sixteen gigabytes",
    art_at="At sixteen gigabytes",
    rails=[
        dict(lab="AT 16 GB", val="BROADER TARGETS", pct=66.0, cls="",
             at="broader adapter targets"),
        dict(lab="CHANGE AT A TIME", val="1 CHANGE", pct=12.0, cls="",
             at="one change at a time"),
        dict(lab="AT 24 GB", val="7B CANDIDATE", pct=100.0, cls="red",
             at="a seven-billion experiment"),
    ],
    closing=dict(c="red", t="NEITHER CAPACITY GUARANTEES A FIT",
                 at="Neither capacity guarantees full fine-tuning"),
    source="mechanism &middot; a smaller control first, then one change at a "
           "time")

# =====================================================================
# THE HARDWARE BEHIND THE CAPACITY
# =====================================================================
win("note",
    vo="Also check the hardware behind the capacity. Our pinned normal-float "
       "configuration requires a compatible CUDA stack and a device supporting "
       "its selected brain-float computation. Two cards with the same memory "
       "label can require different precision choices and different software "
       "support.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; THE HARDWARE",
    title="SAME MEMORY LABEL, DIFFERENT CARD",
    art="pcie_slot",
    art_caption="PCI EXPRESS SLOT",
    header_at="Also check the hardware behind the capacity",
    art_at="Also check the hardware behind the capacity",
    note_head="CHECK BEFORE YOU BUY",
    note_items=[
        dict(t="A COMPATIBLE CUDA STACK", at="requires a compatible CUDA stack"),
        dict(t="A DEVICE SUPPORTING BRAIN FLOAT COMPUTATION",
             at="a device supporting its selected brain-float computation"),
        dict(t="TWO CARDS, SAME LABEL, DIFFERENT PRECISION",
             at="Two cards with the same memory label can require different precision choices"),
    ],
    tape="DIFFERENT CARDS, DIFFERENT SUPPORT",
    tape_at="and different software support",
    source="mechanism &middot; the pinned normal float configuration &middot; a "
           "compatible CUDA stack and a brain float device",
    source_at="and different software support")

# =====================================================================
# UNIFIED MEMORY IS A DIFFERENT SYSTEM
# =====================================================================
win("gallery",
    vo="On an Apple machine with sixty-four or one hundred twenty-eight "
       "gigabytes of unified memory, the capacity number describes a "
       "different system. M L X L M has its own adapter training path for the "
       "Qwen two family. The CUDA configuration on screen is not a Mac "
       "recipe.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; UNIFIED MEMORY",
    title="A DIFFERENT SYSTEM",
    art="laptop_closed",
    art_caption="LAPTOP",
    header_at="On an Apple machine with sixty-four or one hundred twenty-eight",
    art_at="On an Apple machine with sixty-four or one hundred twenty-eight",
    name="A DIFFERENT SYSTEM",
    blurb="M L X L M has its own adapter training path for the Qwen two family.",
    meta="the CUDA configuration on screen is not a Mac recipe",
    name_at="the capacity number describes a different system",
    blurb_at="M L X L M has its own adapter training path for the Qwen two family",
    meta_at="is not a Mac recipe",
    side="right",
    source="mechanism &middot; MLX-LM has its own adapter training path for the "
           "Qwen two family")

# =====================================================================
# THE INFERENCE CACHE, CALCULATED SEPARATELY
# =====================================================================
win("rows",
    vo="For comparison, calculate this architecture's inference cache "
       "separately. One sequence at eight thousand one hundred ninety-two "
       "tokens needs two hundred eighty-eight mebibytes of logical key and "
       "value storage in sixteen-bit precision. That is about zero point "
       "three zero two decimal gigabytes.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; THE CACHE",
    title="AT 8,192 TOKENS",
    art="kv_cache",
    art_caption="KV CACHE",
    header_at="For comparison, calculate this architecture's inference cache",
    art_at="For comparison, calculate this architecture's inference cache",
    rows=[
        dict(rank="01", name="SEQUENCE", val="8,192", sub="TOKENS", cls="",
             at="eight thousand one hundred ninety-two tokens"),
        dict(rank="02", name="KV STORAGE, 16 BIT", val="288 MiB",
             sub="DERIVED", cls="gold", at="two hundred eighty-eight mebibytes"),
        dict(rank="03", name="THE SAME IN DECIMAL", val="0.302 GB",
             sub="DERIVED", cls="",
             at="zero point three zero two decimal gigabytes"),
    ],
    closing=dict(c="gold", t="CALCULATED SEPARATELY FROM TRAINING",
                 at="decimal gigabytes"),
    source="derived &middot; qwen2.5 3b instruct &middot; 2 kv heads &middot; "
           "head dim 128 &middot; 8192 tokens")

# =====================================================================
# THE SAME CACHE, QUANTIZED
# =====================================================================
win("bars",
    vo="An ideal Q eight zero payload is one hundred fifty-three mebibytes, "
       "because each thirty-two-value block carries thirty-four bytes, "
       "including its scale. two hundred eighty-eight mebibytes needs "
       "two hundred eighty-eight mebibytes. Both figures exclude runtime "
       "overhead, and neither is a training peak.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; THE CACHE",
    title="QUANTIZED AND NOT",
    art="gguf_blocks",
    art_caption="MIXED PRECISION",
    header_at="An ideal Q eight zero payload",
    art_at="An ideal Q eight zero payload",
    bars=[
        dict(lab="Q8_0 PAYLOAD", val="153", unit="MiB", pct=53.1, cls="",
             at="one hundred fifty-three mebibytes"),
        dict(lab="16-BIT KV STORAGE", val="288", unit="MiB", pct=100.0, cls="",
             at="two hundred eighty-eight mebibytes"),
    ],
    closing=dict(c="red", t="NEITHER FIGURE IS A TRAINING PEAK",
                 at="Both figures exclude runtime overhead"),
    source="derived &middot; qwen2.5 3b instruct &middot; 8192 tokens &middot; "
           "q8_0 block of 32 values at 34 bytes")

# =====================================================================
# WHAT MUST REMAIN LIVE
# =====================================================================
win("note",
    vo="During a training step, autograd, loss computation, batch shape, and "
       "the attention implementation decide what must remain live on the "
       "device. Checkpointing has a time cost worth counting, because it "
       "recomputes the graph.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; WHAT MUST REMAIN LIVE",
    title="WHAT MUST REMAIN LIVE",
    art="psu",
    art_caption="POWER SUPPLY",
    header_at="During a training step",
    art_at="During a training step",
    note_head="WHAT THE INFERENCE NUMBERS DO NOT CARRY OVER",
    note_items=[
        dict(t="AUTOGRAD AND LOSS COMPUTATION", at="autograd, loss computation"),
        dict(t="BATCH SHAPE", at="batch shape"),
        dict(t="THE ATTENTION IMPLEMENTATION", at="the attention implementation"),
        dict(t="CHECKPOINTING HAS A TIME COST", at="Checkpointing has a time cost"),
    ],
    tape="WHAT THE INFERENCE NUMBERS DO NOT CARRY OVER",
    tape_at="it recomputes the graph",
    source="mechanism &middot; autograd holds the training graph live, and "
           "checkpointing trades time for memory",
    source_at="it recomputes the graph")

# =====================================================================
# THE ENERGY COST
# =====================================================================
win("rows",
    vo="Suppose the whole system averages two hundred fifty watts for one "
       "hour. That is zero point two five kilowatt-hours. A configuration "
       "that uses less memory but takes longer can consume more total energy, "
       "depending on its power draw.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; THE ENERGY COST",
    title="250 WATTS FOR ONE HOUR",
    art="timer_flat",
    art_caption="TIMER",
    header_at="Suppose the whole system averages two hundred fifty watts",
    art_at="Suppose the whole system averages two hundred fifty watts",
    rows=[
        dict(rank="01", name="OVER ONE HOUR", val="0.25 kWh", sub="DERIVED",
             cls="gold", at="That is zero point two five kilowatt-hours"),
        dict(rank="02", name="LESS MEMORY, LONGER", val="MORE ENERGY",
             sub="DEPENDS ON DRAW", cls="red",
             at="A configuration that uses less memory"),
    ],
    closing=dict(c="red", t="LESS MEMORY CAN STILL COST MORE ENERGY",
                 at="its power draw"),
    source="mechanism &middot; whole system energy is average power times "
           "elapsed time &middot; no measured trace for this recipe")

# =====================================================================
# THE ENERGY WE CANNOT ANSWER
# =====================================================================
win("note",
    vo="We have no measured power trace for this recipe. Log wall time and "
       "whole-system energy if efficiency matters to your decision. A smaller "
       "checkpoint file cannot tell you how many watt-hours its training "
       "consumed.",
    kicker="BUDGET THE EXPERIMENT YOU OWN &middot; THE ENERGY",
    title="LOG IT YOURSELF",
    art="timer_flat",
    art_caption="TIMER",
    header_at="We have no measured power trace",
    art_at="We have no measured power trace",
    note_head="WHAT WE DO NOT HAVE",
    note_items=[
        dict(t="A MEASURED POWER TRACE FOR THIS RECIPE",
             at="for this recipe"),
        dict(t="LOG WALL TIME AND WHOLE SYSTEM ENERGY",
             at="Log wall time and whole-system energy"),
        dict(t="A CHECKPOINT FILE CANNOT TELL YOU THE WATT HOURS",
             at="A smaller checkpoint file cannot tell you"),
    ],
    tape="A SMALLER FILE IS NOT A SMALLER FOOTPRINT",
    tape_at="its training consumed",
    source="mechanism &middot; wall time and a whole system energy meter are "
           "the only honest measures",
    source_at="its training consumed")

# =====================================================================
# WHY TRAIN AT ALL, PART ONE
# =====================================================================
win("hook",
    vo="The useful reason to train an adapter is a behavior you can describe "
       "and test. Here are three cases: write your team's issue summaries "
       "consistently, apply a stable classification policy, or follow a "
       "domain-specific response pattern.",
    kicker="CHOOSE THE CHANGE, THEN THE HARDWARE",
    title="A BEHAVIOUR YOU CAN TEST",
    sub="describe it, then test it",
    art="checklist",
    art_caption="THE CHECKLIST",
    header_at="The useful reason to train an adapter",
    art_at="The useful reason to train an adapter",
    chips=[
        dict(t="ISSUE SUMMARIES, CONSISTENTLY", c="cyan",
             at="write your team's issue summaries consistently"),
        dict(t="A STABLE CLASSIFICATION POLICY", c="cyan",
             at="apply a stable classification policy"),
        dict(t="A DOMAIN SPECIFIC RESPONSE PATTERN", c="cyan",
             at="follow a domain-specific response pattern"),
    ],
    stats=[
        dict(v="1", u="BEHAVIOUR", lab="YOU CAN DESCRIBE AND TEST", c="gold",
             at="a behavior you can describe and test"),
        dict(v="3", u="CASES", lab="ONE BEHAVIOUR, THREE EXAMPLES", c="cyan",
             at="Here are three cases"),
    ],
    tape="DESCRIBE IT, THEN TEST IT",
    tape_at="a domain-specific response pattern",
    source="the LoRA paper &middot; arxiv 2106.09685 &middot; the target "
           "behaviour decides the training set")

# =====================================================================
# WHY TRAIN AT ALL, PART TWO
# =====================================================================
win("rows",
    vo="Build representative examples and keep a separate evaluation set. "
       "Compare the adapted result with the same base model, using the same "
       "prompt template and deployment precision. Check what improved and "
       "what regressed. If the underlying problem is simply a changing "
       "spreadsheet, first establish why changing the weights is necessary.",
    kicker="CHOOSE THE CHANGE, THEN THE HARDWARE",
    title="COMPARE LIKE WITH LIKE",
    art="checklist",
    art_caption="THE CHECKLIST",
    header_at="Build representative examples",
    art_at="Build representative examples",
    rows=[
        dict(rank="01", name="THE EVALUATION SET", val="SEPARATE",
             sub="NOT THE TRAINING DATA", cls="gold",
             at="keep a separate evaluation set"),
        dict(rank="02", name="THE COMPARISON", val="SAME BASE MODEL",
             sub="SAME PROMPT TEMPLATE", cls="",
             at="the same base model, using the same prompt template"),
        dict(rank="03", name="WHAT IMPROVED", val="CHECK",
             sub="AND WHAT REGRESSED", cls="",
             at="Check what improved and what regressed"),
        dict(rank="04", name="A CHANGING SPREADSHEET", val="FIX THE FILE",
             sub="NOT THE WEIGHTS", cls="red",
             at="first establish why changing the weights is necessary"),
    ],
    closing=dict(c="red", t="IF IT IS A SPREADSHEET, FIX THE SPREADSHEET",
                 at="changing the weights is necessary"),
    source="mechanism &middot; a separate evaluation set, the same prompt "
           "template, and the same deployment precision")

# =====================================================================
# A CONFIGURATION IS NOT A RUN
# =====================================================================
win("title",
    vo="The accompanying listing prints a configuration. It downloads no model "
       "and starts no training. A configuration is a proposal, and a proposal "
       "is not a run.",
    kicker="CHOOSE THE CHANGE, THEN THE HARDWARE &middot; BEFORE YOU ALLOCATE",
    title="A CONFIGURATION IS NOT A RUN",
    sub="the listing prints a proposal, not a result",
    art="nvme_ssd",
    art_caption="NVME SSD",
    head_at="The accompanying listing prints a configuration",
    closing=dict(c="red", t="NO MODEL, NO TRAINING, NO RESULT",
                 at="A configuration is a proposal"),
    source="mechanism &middot; the listing names revision, target modules, "
           "rank, precision, length, and microbatch")

# =====================================================================
# WHAT THE LISTING NAMES
# =====================================================================
win("rows",
    vo="The proposal is explicit. The revision, the target modules, the rank, "
       "the precision, the sequence length, and the microbatch are all named "
       "before any memory is allocated.",
    kicker="CHOOSE THE CHANGE, THEN THE HARDWARE &middot; BEFORE YOU ALLOCATE",
    title="REVIEW THE PROPOSAL",
    art="nvme_ssd",
    art_caption="NVME SSD",
    header_at="The proposal is explicit",
    art_at="The proposal is explicit",
    rows=[
        dict(rank="01", name="REVISION", val="EXPLICIT", sub="", cls="gold",
             at="The revision"),
        dict(rank="02", name="TARGET MODULES", val="EXPLICIT", sub="", cls="",
             at="the target modules"),
        dict(rank="03", name="RANK", val="EXPLICIT", sub="", cls="gold",
             at="the rank"),
        dict(rank="04", name="PRECISION", val="EXPLICIT", sub="", cls="",
             at="the precision"),
        dict(rank="05", name="SEQUENCE LENGTH", val="EXPLICIT", sub="",
             cls="", at="the sequence length"),
        dict(rank="06", name="MICROBATCH", val="EXPLICIT", sub="", cls="red",
             at="the microbatch"),
    ],
    closing=dict(c="red", t="REVIEW THE PROPOSAL BEFORE ALLOCATING MEMORY",
                 at="before any memory is allocated"),
    source="mechanism &middot; the listing names revision, target modules, "
           "rank, precision, length, and microbatch")

# =====================================================================
# WHAT A COMPLETE RUN NEEDS
# =====================================================================
win("note",
    vo="A complete run needs more than the listing. It needs tokenized data, "
       "a checked loss mask, an evaluation procedure, and full-step profiling "
       "on the machine you actually own, not on a paper configuration.",
    kicker="CHOOSE THE CHANGE, THEN THE HARDWARE &middot; BEFORE YOU ALLOCATE",
    title="A CONFIGURATION IS NOT A RUN",
    art="checklist",
    art_caption="THE CHECKLIST",
    header_at="A complete run needs more than the listing",
    art_at="A complete run needs more than the listing",
    note_head="WHAT THE LISTING DOES NOT DO",
    note_items=[
        dict(t="TOKENIZED DATA", at="tokenized data"),
        dict(t="A CHECKED LOSS MASK", at="a checked loss mask"),
        dict(t="AN EVALUATION PROCEDURE", at="an evaluation procedure"),
        dict(t="FULL STEP PROFILING ON YOUR MACHINE",
             at="full-step profiling on the machine you actually own"),
        dict(t="NOT A PAPER CONFIGURATION", at="not on a paper configuration"),
    ],
    tape="PROFILE THE STEP YOU WILL RUN",
    tape_at="not on a paper configuration",
    source="mechanism &middot; a run is data, a loss mask, an evaluation, and "
           "a profile on your own machine",
    source_at="not on a paper configuration")

# =====================================================================
# AFTER TRAINING
# =====================================================================
win("chain",
    vo="After training, two things must be preserved: the exact base revision "
       "and the adapter settings. Then check the deployed adapter too, because "
       "merging and quantized inference introduce another implementation "
       "choice that deserves its own validation on your own hardware.",
    kicker="CHOOSE THE CHANGE, THEN THE HARDWARE &middot; AFTER TRAINING",
    title="CHECK THE DEPLOYED ADAPTER",
    art="checklist",
    art_caption="THE CHECKLIST",
    header_at="After training, two things must be preserved",
    art_at="After training, two things must be preserved",
    chain=[
        dict(t="PRESERVE", s="the base revision", at="the exact base revision"),
        dict(t="PRESERVE", s="the adapter settings", at="the adapter settings"),
        dict(t="CHECK", s="the deployed adapter", at="check the deployed adapter too"),
        dict(t="VALIDATE", s="merging and quantized inference",
             at="merging and quantized inference introduce another implementation choice"),
    ],
    compare=[
        dict(cls="hot", title="A NEW CHOICE",
             body="Merging and quantized inference introduce another implementation choice.",
             at="another implementation choice"),
        dict(cls="good", title="YOUR OWN VALIDATION",
             body="It deserves its own validation on your hardware.",
             at="deserves its own validation"),
    ],
    closing=dict(c="gold", t="VALIDATE THE DEPLOYED ARTEFACT, NOT THE FILE",
                 at="on your own hardware"),
    source="mechanism &middot; the deployed adapter is a different artefact "
           "after merging or quantized inference")

# =====================================================================
# THE VERDICT, PART ONE
# =====================================================================
win("rows",
    vo="The verdict is simple. LoRA reduces what you update. Quantized LoRA "
       "also reduces how the frozen base is stored. Neither one removes the "
       "rest of the learning process.",
    kicker="THE VERDICT",
    title="THE ADAPTER IS THE CHANGE YOU KEEP",
    art="folder",
    art_caption="SAVED TO DISK",
    header_at="The verdict is simple",
    art_at="The verdict is simple",
    rows=[
        dict(rank="01", name="LoRA", val="REDUCES WHAT YOU UPDATE", sub="",
             cls="gold", at="LoRA reduces what you update"),
        dict(rank="02", name="QUANTIZED LoRA",
             val="REDUCES HOW THE BASE IS STORED", sub="", cls="",
             at="Quantized LoRA also reduces how the frozen base is stored"),
        dict(rank="03", name="NEITHER ONE",
             val="REMOVES THE LEARNING PROCESS", sub="", cls="red",
             at="removes the rest of the learning process"),
    ],
    closing=dict(c="red", t="NEITHER REMOVES THE REST OF THE LEARNING PROCESS",
                 at="the rest of the learning process"),
    source="the LoRA paper &middot; arxiv 2106.09685 &middot; the QLoRA paper "
           "&middot; arxiv 2305.14314")

# =====================================================================
# THE VERDICT, PART TWO
# =====================================================================
win("note",
    vo="Buy capacity around a measured training workload, or reduce the "
       "workload until it matches the hardware you already own. The adapter is "
       "the change you keep. Training memory is the work required to discover "
       "it.",
    kicker="THE VERDICT",
    title="THE ADAPTER IS THE CHANGE YOU KEEP",
    art="folder",
    art_caption="SAVED TO DISK",
    header_at="Buy capacity around a measured",
    art_at="Buy capacity around a measured",
    note_head="WHAT TO DO WITH THAT",
    note_items=[
        dict(t="BUY CAPACITY AROUND A MEASURED WORKLOAD",
             at="a measured training workload"),
        dict(t="OR REDUCE THE WORKLOAD TO THE HARDWARE YOU OWN",
             at="reduce the workload until it matches the hardware you already own"),
        dict(t="THE ADAPTER IS THE CHANGE YOU KEEP",
             at="The adapter is the change you keep"),
    ],
    tape="TRAINING MEMORY IS THE WORK REQUIRED TO DISCOVER IT",
    tape_at="the work required to discover it",
    source="derived &middot; Hu et al. 2021 (LoRA, arxiv 2106.09685) &middot; "
           "Dettmers et al. 2023 (QLoRA, arxiv 2305.14314) &middot; "
           "Qwen2.5-3B-Instruct config.json",
    source_at="the work required to discover it")
