# -*- coding: utf-8 -*-
"""
FUSION — EPISODE 08: "Why a Tiny LoRA Adapter Can Still Fill Your GPU"

The full script, split by ACT. Every window is a piece of the written script,
so the narration is the author's own and the pictures follow the argument
rather than decorating it.

Every figure on screen comes from the script. The script is careful about the
difference between a measurement, a derivation and a starting choice, and the
pictures keep that distinction:
  * a measured result is a plain number
  * a derivation is labelled DERIVED
  * a starting point is labelled A STARTING CHOICE
"""

import re

NAME = "BYTE-LORA"
TITLE = "WHY A TINY LoRA ADAPTER CAN STILL FILL YOUR GPU"
KICKER = "BYTE FORENSICS &middot; EPISODE 08"
SUBTITLE = "the adapter is small. the training job is not."
GLOBAL_PROGRESS = True

W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


def sents(vo):
    return [x.strip() for x in re.split(r"(?<=\.)\s+", vo) if x.strip()]


def S(p, i):
    """Sentence i, or the last one, if the paragraph is shorter."""
    return p[i] if i < len(p) else p[-1]


def act(no, title, sub, vo):
    win("title", vo=vo,
        kicker="BYTE FORENSICS &middot; EPISODE 08 &middot; ACT %s" % no,
        title=title, sub=sub, head_at=vo.split(".")[0] + ".")


def hero(vo, kicker, name, blurb, key, side="right", meta=None, blurb_at=None):
    p = sents(vo)
    first = S(p, 0) if S(p, 0).endswith(".") else S(p, 0) + "."
    second = S(p, 1) if len(p) > 1 else first
    win("gallery", vo=vo,
        kicker=kicker, name=name, blurb=blurb,
        meta=meta or ("asset: %s" % key),
        header_at=first, art_at=first, name_at=first, blurb_at=blurb_at or second,
        art=key, art_caption=key.replace("_", " ").upper(), side=side)


def row(vo, kicker, title, items):
    p = sents(vo)
    for it, s in zip(items, p):
        it["at"] = s if s.endswith(".") else s + "."
    win("strip", vo=vo, kicker=kicker, title=title,
        header_at=items[0]["at"], items=items)


# ===================================================================== ACT ONE
act("ONE", "THE TINY FILE", "and the large job",
    "Training a tiny adapter can exhaust your GPU. That is the first "
    "distinction to make before fine-tuning a local model.")

hero("The adapter file describes the changes you learned. It does not describe "
     "everything the machine needed while learning them. Loading a model and "
     "answering a question proves that an inference workload fits. Training "
     "that same model creates a different memory bill, even when most of its "
     "weights never change.",
     "ACT ONE &middot; FILE VERSUS JOB", "THE FILE IS NOT THE JOB",
     "A LoRA adapter is a small file. It describes the delta, and nothing "
     "about the machine that produced it.",
     "model_file", side="right")

hero("LoRA freezes the original weight matrix and learns an additional update "
     "through two smaller matrices. Think of the frozen model as a machine "
     "whose controls you are adjusting. You do not rebuild every component. But "
     "the machine still runs during each training example.",
     "ACT ONE &middot; HOW LoRA WORKS", "TWO SMALL MATRICES",
     "The original weights stay frozen. The adapter learns a low rank update "
     "on top of them.",
     "two_die", side="left")

chain_vo = ("The error signal still travels backward through the computation so "
            "the adapter can learn. Intermediate tensors needed for that backward "
            "pass remain part of the job. Frozen weights are not permission to "
            "delete the learning process.")
p = sents(chain_vo)
win("nodes", vo=chain_vo,
    kicker="ACT ONE &middot; WHY THE MEMORY IS STILL THERE",
    title="THE BACKWARD PASS DOES NOT KNOW",
    header_at=S(p, 0),
    art="two_die",
    art_caption="THE UPDATE",
    chain=[dict(t="BACKWARD", s="the error travels", sent=0),
           dict(t="TENSORS", s="they stay live", sent=1),
           dict(t="FROZEN", s="is not free", sent=2)])

arith = ("The adapter arithmetic is pleasantly concrete. For a projection with "
         "an input width and an output width, rank times their sum gives the "
         "added parameter count. One small matrix maps the input into the rank. "
         "The second maps the rank into the output.")
p = sents(arith)
win("rows", vo=arith,
    kicker="ACT ONE &middot; THE ARITHMETIC",
    title="RANK TIMES THE SUM OF THE WIDTHS",
    header_at=S(p, 0),
    art="chip",
    rows=[dict(rank="A", name="DOWN", val="2048 x 16", sub="INPUT INTO RANK", cls="gold", sent=1),
          dict(rank="B", name="UP", val="16 x 2048", sub="RANK INTO OUTPUT", cls="", sent=2),
          dict(rank="=", name="TOTAL", val="16 x SUM", sub="PER PROJECTION", cls="red", sent=3)])

budget = ("That is a count of trainable values. Converting it into a memory "
          "prediction requires another question: what precision holds those "
          "values, their gradients, and the optimizer history? Then we still "
          "have to account for the rest of training.")
p = sents(budget)
win("note", vo=budget,
    kicker="ACT ONE &middot; COUNTING IS NOT THE SAME AS FITTING",
    title="A COUNT IS NOT A MEMORY PLAN",
    header_at=S(p, 0),
    note_head="THREE THINGS THE COUNT DOES NOT TELL YOU",
    note_items=[
        dict(t="WHAT PRECISION HOLDS THE ADAPTER VALUES", sent=1),
        dict(t="WHAT HOLDS THEIR GRADIENTS AND THE OPTIMIZER HISTORY", sent=2),
        dict(t="AND EVERYTHING ELSE THE TRAINING RUN KEEPT LIVE", sent=3)])

arch = ("Use an actual architecture. Qwen two point five, three billion, "
        "Instruct has thirty-six layers and a hidden width of two thousand "
        "forty-eight. Its sixteen query heads share only two key and value "
        "heads. Each head is one hundred twenty-eight values wide. So the value "
        "projection produces two hundred fifty-six outputs, not two thousand "
        "forty-eight.")
p = sents(arch)
win("rows", vo=arch,
    kicker="ACT ONE &middot; THE ARCHITECTURE, SPECIFICALLY",
    title="QWEN 2.5 3B INSTRUCT",
    header_at=S(p, 0),
    art="superchip",
    rows=[dict(rank="01", name="LAYERS", val="36", sub="blocks", cls="gold", sent=1),
          dict(rank="02", name="HIDDEN", val="2,048", sub="width", cls="", sent=2),
          dict(rank="03", name="QUERY HEADS", val="16", sub="attention", cls="", sent=3),
          dict(rank="04", name="KV HEADS", val="2", sub="shared", cls="red", sent=4),
          dict(rank="05", name="HEAD DIM", val="128", sub="values wide", cls="", sent=5)])

val = ("So the value projection produces two hundred fifty-six outputs, not two "
       "thousand forty-eight. Put rank sixteen adapters on query and value "
       "only, with no trained biases, and the total is three million, six "
       "hundred eighty-six thousand, four hundred parameters.")
p = sents(val)
win("rows", vo=val,
    kicker="ACT ONE &middot; RANK 16, QUERY AND VALUE ONLY",
    title="3,686,400 TRAINABLE",
    header_at=S(p, 0),
    art="die",
    rows=[dict(rank="Q", name="QUERY", val="65,536", sub="RANK 16", cls="gold", sent=1),
          dict(rank="V", name="VALUE", val="36,864", sub="RANK 16", cls="gold", sent=2),
          dict(rank="=", name="PER LAYER", val="102,400", sub="DERIVED", cls="", sent=3),
          dict(rank="x", name="36 LAYERS", val="3,686,400", sub="DERIVED", cls="red", sent=3)])

expand = ("Expand that same rank to query, key, value, attention output, and the "
          "three feed-forward projections. Now the total is just under thirty "
          "million trainable parameters. The base architecture did not change. The "
          "places you allowed it to adapt changed.")
p = sents(expand)
win("rows", vo=expand,
    kicker="ACT ONE &middot; SAME RANK, MORE TARGETS",
    title="JUST UNDER 30M TRAINABLE",
    header_at=S(p, 0),
    art="riser",
    rows=[dict(rank="01", name="QUERY", val="TARGETED", sub="", cls="gold", sent=1),
          dict(rank="02", name="KEY AND VALUE", val="TARGETED", sub="", cls="gold", sent=1),
          dict(rank="03", name="ATTENTION OUTPUT", val="TARGETED", sub="", cls="gold", sent=1),
          dict(rank="04", name="FEED FORWARD x3", val="TARGETED", sub="", cls="gold", sent=1)])

ask = ("That is why somebody else saying rank sixteen is insufficient "
       "information. Ask which projections, which layers, whether embeddings or "
       "biases are trained, and what precision the implementation actually uses. "
       "A small rank is a setting. It is not a complete training specification.")
p = sents(ask)
win("note", vo=ask,
    kicker="ACT ONE &middot; WHAT TO ASK",
    title="RANK IS NOT A SPECIFICATION",
    header_at=S(p, 0),
    note_head="FOUR QUESTIONS THAT DECIDE THE BILL",
    note_items=[
        dict(t="WHICH PROJECTIONS ARE TARGETED", sent=1),
        dict(t="WHICH LAYERS ARE TARGETED", sent=1),
        dict(t="ARE EMBEDDINGS OR BIASES TRAINED", sent=2),
        dict(t="WHAT PRECISION THE IMPLEMENTATION ACTUALLY USES", sent=2)])

# ===================================================================== ACT TWO
act("TWO", "WHAT THE ORIGINAL EXPERIMENTS ESTABLISH", "and what they do not",
    "Does learning so few parameters compromise quality? The original LoRA "
    "paper gives a useful comparison.")

paper = ("On GPT three with one hundred seventy-five billion parameters, full "
         "fine-tuning scored seventy-three point eight on Wiki SQL and "
         "eighty-nine point five on matched Multi N L I. A LoRA row with four "
         "point seven million trainable parameters scored seventy-three point "
         "four and ninety-one point seven.")
p = sents(paper)
win("rows", vo=paper,
    kicker="ACT TWO &middot; THE ORIGINAL LoRA PAPER",
    title="GPT-3 175B",
    header_at=S(p, 0),
    art="chip",
    rows=[dict(rank="FT", name="FULL FINE-TUNE", val="73.8", sub="WIKISQL", cls="", sent=1),
          dict(rank="LR", name="LoRA 4.7M", val="73.4", sub="WIKISQL", cls="gold", sent=2),
          dict(rank="FT", name="FULL FINE-TUNE", val="89.5", sub="MNLI", cls="", sent=1),
          dict(rank="LR", name="LoRA 4.7M", val="91.7", sub="MNLI", cls="gold", sent=2)])

scope1 = ("Those are the original authors' task results, with task-specific "
          "variation, not measurements from this channel or promises for a "
          "desktop model. Now separate LoRA from quantized LoRA.")
p = sents(scope1)
win("note", vo=scope1,
    kicker="ACT TWO &middot; READ THE ROW CORRECTLY",
    title="WHOSE RESULT IS THIS",
    header_at=S(p, 0),
    note_head="THIS IS NOT YOUR MODEL AND NOT OUR HARDWARE",
    note_items=[
        dict(t="THE ORIGINAL AUTHORS' TASK RESULTS", sent=0),
        dict(t="WITH TASK SPECIFIC VARIATION", at="with task-specific variation"),
        dict(t="NOT A MEASUREMENT FROM THIS CHANNEL", at="not measurements from this channel"),
        dict(t="NOT A PROMISE FOR A DESKTOP MODEL", at="or promises for a desktop model"),
        dict(t="NOW SEPARATE LoRA FROM QUANTIZED LoRA", sent=1)])

qlora = ("In the final QLoRA paper, a Llama seven billion model tuned on "
         "Alpaca scored thirty-eight point four on five-shot M M L U using "
         "brain float sixteen adapter tuning. Normal float four with double "
         "quantization scored thirty-nine point zero. On F L A N version two, the "
         "corresponding scores were forty-five point six and forty-four point "
         "five.")
p = sents(qlora)
win("rows", vo=qlora,
    kicker="ACT TWO &middot; THE FINAL QLoRA PAPER",
    title="LLAMA 7B, TUNED ON ALPACA",
    header_at=S(p, 0),
    art="gguf_blocks",
    rows=[dict(rank="B16", name="BF16 ADAPTER", val="38.4", sub="5-SHOT MMLU", cls="", sent=1),
          dict(rank="N4Q", name="NF4 + DQ", val="39.0", sub="5-SHOT MMLU", cls="gold", sent=2),
          dict(rank="B16", name="BF16 ADAPTER", val="45.6", sub="FLAN V2", cls="", sent=3),
          dict(rank="N4Q", name="NF4 + DQ", val="44.5", sub="FLAN V2", cls="gold", sent=3)])

move = ("One dataset moved up zero point six percentage points. The other moved "
        "down one point one. That is a useful result because it has a boundary: "
        "the named model, datasets, methods, and evaluation.")
p = sents(move)
win("bars", vo=move,
    kicker="ACT TWO &middot; THE MOVEMENT",
    title="PLUS ZERO POINT SIX. MINUS ONE POINT ONE.",
    header_at=S(p, 0),
    art="gauge",
    bars=[dict(lab="MMLU", val="+0.6", pct=54.0, cls="", sent=0),
          dict(lab="FLAN V2", val="-1.1", pct=40.0, cls="red", sent=1)])

bound = ("It does not establish that four-bit training improves every task. It "
         "does not tell us whether our Qwen adapter follows an internal coding "
         "convention. For that decision, write down the behavior you want to "
         "change and examples that test it before training begins. Otherwise the "
         "only number guaranteed to improve is the number of checkpoints on "
         "disk.")
p = sents(bound)
win("note", vo=bound,
    kicker="ACT TWO &middot; WHERE THE RESULT STOPS",
    title="THE ONLY NUMBER THAT ALWAYS IMPROVES",
    header_at=S(p, 0),
    note_head="WHAT THESE ROWS DO NOT ESTABLISH",
    note_items=[
        dict(t="THAT FOUR BIT TRAINING IMPROVES EVERY TASK", sent=0),
        dict(t="WHETHER OUR QWEN ADAPTER FOLLOWS AN INTERNAL CODING CONVENTION", sent=1),
        dict(t="WRITE DOWN THE BEHAVIOR YOU WANT TO CHANGE", sent=2),
        dict(t="AND THE EXAMPLES THAT TEST IT", at="examples that test it"),
        dict(t="THE NUMBER OF CHECKPOINTS ON DISK ALWAYS IMPROVES", sent=3)])

big = ("The famous sixty-five-billion model on a forty-eight-gigabyte GPU is "
       "also a scoped research demonstration. Keep the original recipe attached "
       "to that sentence. It is not a universal allowance for longer examples, a "
       "different architecture, arbitrary batch sizes, or another software "
       "stack.")
p = sents(big)
win("rows", vo=big,
    kicker="ACT TWO &middot; THE FAMOUS DEMONSTRATION",
    title="65B, ON A 48GB GPU",
    header_at=S(p, 0),
    art="rack_server",
    rows=[dict(rank="01", name="MODEL SIZE", val="65B", sub="PARAMETERS", cls="gold", sent=0),
          dict(rank="02", name="GPU MEMORY", val="48 GB", sub="ONE DEVICE", cls="", sent=0),
          dict(rank="03", name="SCOPE", val="RESEARCH", sub="NOT A RULE", cls="red", sent=2)])

big2 = ("Treat it as evidence that quantized adapter training can make a "
        "previously inaccessible experiment possible. Then budget your own "
        "experiment. An engineering result becomes misleading when the equipment "
        "and settings disappear while the headline survives.")
p = sents(big2)
win("note", vo=big2,
    kicker="ACT TWO &middot; HOW TO USE IT",
    title="EVIDENCE, NOT AN ALLOWANCE",
    header_at=S(p, 0),
    note_head="WHAT THE DEMONSTRATION ESTABLISHES",
    note_items=[
        dict(t="QUANTIZED ADAPTER TRAINING CAN MAKE AN INACCESSIBLE EXPERIMENT POSSIBLE", sent=0),
        dict(t="THEN BUDGET YOUR OWN EXPERIMENT", sent=1),
        dict(t="KEEP THE EQUIPMENT AND THE SETTINGS WITH THE HEADLINE", sent=2)])

# =================================================================== ACT THREE
act("THREE", "THE RUNTIME MEMORY THAT FOUR BITS HIDES", "every line is separate",
    "Four-bit training does not mean every training tensor uses four bits. In "
    "the documented bits and bytes route, normal float four stores the "
    "converted base weights.")

separate = ("A separate compute setting selects the arithmetic precision. Our "
            "configuration uses brain float sixteen computation on compatible "
            "hardware. The adapters are extra trainable tensors. Activations, "
            "gradients, and optimizer states have their own representations. "
            "Read those settings as separate lines in a budget.")
p = sents(separate)
win("rows", vo=separate,
    kicker="ACT THREE &middot; READ THE SETTINGS AS LINES",
    title="SEPARATE LINES IN A BUDGET",
    header_at=S(p, 0),
    art="gguf_blocks",
    rows=[dict(rank="01", name="BASE WEIGHTS", val="NF4", sub="STORED", cls="gold", sent=0),
          dict(rank="02", name="COMPUTE", val="BF16", sub="ARITHMETIC", cls="gold", sent=1),
          dict(rank="03", name="ADAPTERS", val="EXTRA", sub="TRAINABLE", cls="", sent=2),
          dict(rank="04", name="ACTIVATIONS", val="OWN", sub="REPRESENTATION", cls="", sent=3),
          dict(rank="05", name="GRADIENTS AND OPTIMIZER", val="OWN", sub="REPRESENTATION", cls="", sent=3)])

trap = ("Multiplying the model's advertised parameter count by half a byte does "
        "not produce the peak. Even the converted weights need their scales. "
        "With a scale stored in thirty-two bits for each block of sixty-four "
        "weights, those scales add half a bit per weight.")
p = sents(trap)
win("rows", vo=trap,
    kicker="ACT THREE &middot; THE SCALES ARE NOT FREE",
    title="HALF A BIT PER WEIGHT",
    header_at=S(p, 0),
    art="cache_grid",
    rows=[dict(rank="01", name="HALF A BYTE", val="NOT A PEAK", sub="", cls="red", sent=0),
          dict(rank="02", name="CONVERTED WEIGHTS", val="NEED SCALES", sub="", cls="", sent=1),
          dict(rank="03", name="SCALE WIDTH", val="32 BIT", sub="PER BLOCK", cls="gold", sent=2),
          dict(rank="04", name="BLOCK SIZE", val="64", sub="WEIGHTS", cls="", sent=2),
          dict(rank="05", name="SCALE OVERHEAD", val="+0.5 BIT", sub="PER WEIGHT", cls="red", sent=2)])

nest = ("Nested quantization compresses the scales too. In the pinned "
        "implementation, the large-tensor average becomes about four point one "
        "two seven bits per converted weight, before small metadata and "
        "rounding. That is useful compression. It is still larger than exactly "
        "four bits, and it says nothing about tensors the loader did not "
        "convert.")
p = sents(nest)
win("rows", vo=nest,
    kicker="ACT THREE &middot; AFTER NESTED QUANTIZATION",
    title="4.127 BITS, NOT FOUR",
    header_at=S(p, 0),
    art="die",
    rows=[dict(rank="01", name="NESTED QUANT", val="SCALES SHRINK", sub="", cls="", sent=0),
          dict(rank="02", name="LARGE TENSOR AVERAGE", val="4.127", sub="BITS PER WEIGHT", cls="gold", sent=1),
          dict(rank="03", name="METADATA", val="EXCLUDED", sub="", cls="",
               at="before small metadata and rounding"),
          dict(rank="04", name="USEFUL COMPRESSION", val="YES", sub="", cls="", sent=2),
          dict(rank="05", name="EXACTLY FOUR BITS", val="NO", sub="NOT WHAT YOU GET", cls="red", sent=3),
          dict(rank="06", name="UNCONVERTED TENSORS", val="?", sub="SAYS NOTHING", cls="", sent=3)])

embed = ("Here is a quieter trap. The pinned P E F T preparation function "
         "freezes the base and promotes ordinary half-precision parameters to "
         "full precision, excluding the special four-bit parameters. Our Qwen "
         "model has a tied vocabulary embedding containing about three hundred "
         "eleven million values. At four bytes each, that embedding alone is "
         "about one point two four five decimal gigabytes.")
p = sents(embed)
win("rows", vo=embed,
    kicker="ACT THREE &middot; THE QUIETER TRAP",
    title="A FULL PRECISION COMPONENT",
    header_at=S(p, 0),
    art="ram_stick",
    rows=[dict(rank="01", name="PEFT PREP", val="FREEZES BASE", sub="", cls="", sent=1),
          dict(rank="02", name="HALF PRECISION", val="PROMOTED TO FP32", sub="", cls="gold",
               at="promotes ordinary half-precision parameters"),
          dict(rank="03", name="FOUR BIT PARAMS", val="EXCLUDED", sub="", cls="",
               at="excluding the special four-bit parameters"),
          dict(rank="04", name="TIED EMBEDDING", val="311M", sub="VALUES", cls="gold", sent=2),
          dict(rank="05", name="AT FOUR BYTES", val="1.245 GB", sub="DERIVED", cls="red", sent=3)])

place = ("This is derived tensor arithmetic, not an allocation measurement. But "
         "it explains why a model with a four-bit label can retain a substantial "
         "full-precision component. Placement is another separate decision.")
p = sents(place)
win("note", vo=place,
    kicker="ACT THREE &middot; PLACEMENT",
    title="A SEPARATE DECISION",
    header_at=S(p, 0),
    note_head="KEEP THE DISTINCTIONS",
    note_items=[
        dict(t="DERIVED TENSOR ARITHMETIC, NOT AN ALLOCATION MEASUREMENT", sent=0),
        dict(t="IT EXPLAINS A SUBSTANTIAL FULL PRECISION COMPONENT", sent=1),
        dict(t="PLACEMENT IS ANOTHER SEPARATE DECISION", sent=2)])

auto = ("The pinned Transformers guide says automatic device mapping is for "
        "inference. It is not evidence that an inference offload layout is a "
        "valid training layout. Our inspection plan names one CUDA device "
        "explicitly and disables the inference cache.")
p = sents(auto)
win("note", vo=auto,
    kicker="ACT THREE &middot; DEVICE PLACEMENT",
    title="INFERENCE MAPPING IS NOT TRAINING MAPPING",
    header_at=S(p, 0),
    note_head="WHAT OUR INSPECTION PLAN DOES",
    note_items=[
        dict(t="AUTOMATIC DEVICE MAPPING IS FOR INFERENCE", sent=0),
        dict(t="AND AN INFERENCE OFFLOAD LAYOUT IS NOT A TRAINING LAYOUT", sent=1),
        dict(t="NAMES ONE CUDA DEVICE EXPLICITLY", sent=2),
        dict(t="DISABLES THE INFERENCE CACHE", sent=2),
        dict(t="NEITHER CHOICE MANUFACTURES MEMORY", sent=2)])

nocache = ("Disabling the cache removes a mechanism for reusing past keys and "
           "values during generation. It does not remove the tensors needed to "
           "differentiate a training example. A successful loader is still only "
           "the beginning of the experiment.")
p = sents(nocache)
win("note", vo=nocache,
    kicker="ACT THREE &middot; WHAT DISABLING THE CACHE DOES",
    title="A LOADER IS NOT AN EXPERIMENT",
    header_at=S(p, 0),
    note_head="THE CACHE IS NOT THE TRAINING TENSORS",
    note_items=[
        dict(t="DISABLING IT REMOVES REUSE OF PAST KEYS AND VALUES DURING GENERATION", sent=0),
        dict(t="IT DOES NOT REMOVE THE TENSORS NEEDED TO DIFFERENTIATE", sent=1),
        dict(t="A SUCCESSFUL LOADER IS STILL ONLY THE BEGINNING", sent=2)])

controls = ("The useful controls change different parts of that experiment. "
            "Gradient checkpointing saves fewer intermediate tensors and "
            "recomputes them during backward, trading additional work for "
            "memory. A microbatch of one keeps fewer examples live together.")
p = sents(controls)
win("rows", vo=controls,
    kicker="ACT THREE &middot; THE CONTROLS THAT DO SOMETHING",
    title="TRADING WORK FOR MEMORY",
    header_at=S(p, 0),
    art="clock",
    rows=[dict(rank="01", name="GRADIENT CHECKPOINTING", val="FEWER", sub="TENSORS LIVE", cls="gold", sent=1),
          dict(rank="02", name="RECOMPUTED", val="ON BACKWARD", sub="TRADING WORK", cls="",
               at="recomputes them during backward"),
          dict(rank="03", name="MICROBATCH", val="1", sub="EXAMPLE AT A TIME", cls="gold", sent=2)])

accum = ("Accumulating eight such microsteps builds an effective batch of eight "
         "on one device without processing all eight simultaneously. Sequence "
         "length remains its own control. These choices do not guarantee the "
         "same optimization behavior in every implementation.")
p = sents(accum)
win("rows", vo=accum,
    kicker="ACT THREE &middot; THE CONTROLS THAT DO SOMETHING",
    title="EFFECTIVE BATCH WITHOUT THE MEMORY",
    header_at=S(p, 0),
    art="token_blocks",
    rows=[dict(rank="01", name="MICROBATCH", val="1", sub="AT A TIME", cls="", sent=0),
          dict(rank="02", name="ACCUMULATION STEPS", val="8", sub="EFFECTIVE BATCH", cls="gold", sent=0),
          dict(rank="03", name="SEQUENCE LENGTH", val="OWN", sub="CONTROL", cls="", sent=1)])

vars = ("They give you specific variables to change when you investigate a "
        "peak.")
p = sents(vars)
win("gallery", vo=vars,
    kicker="ACT THREE &middot; WHAT YOU ACTUALLY GET",
    name="SPECIFIC VARIABLES",
    blurb="Not a guarantee. A set of named levers you can turn one at a time "
           "when a peak turns up.",
    meta="asset: gauge",
    header_at=S(p, 0), art_at=S(p, 0), name_at=S(p, 0), blurb_at=S(p, 0),
    art="gauge", art_caption="GAUGE", side="left")

# ==================================================================== ACT FOUR
act("FOUR", "BUDGET THE EXPERIMENT YOU ACTUALLY OWN", "not the one in the paper",
    "Return to the thirty-million-parameter adapter. Assume full-precision "
    "adapter weights, full-precision gradients, and two full-precision Adam "
    "moment buffers.")

arrays = ("That is sixteen bytes per trainable value. Our exact parameter count "
          "then gives about four hundred fifty-seven mebibytes for those four "
          "arrays. It excludes the frozen base, saved activations, temporary "
          "workspaces, and anything else the implementation keeps.")
p = sents(arrays)
win("rows", vo=arrays,
    kicker="ACT FOUR &middot; THE ADAPTER ARRAYS",
    title="16 BYTES PER TRAINABLE VALUE",
    header_at=S(p, 0),
    art="ram_stick",
    rows=[dict(rank="01", name="ADAPTER WEIGHTS", val="4 B", sub="FULL PRECISION", cls="", sent=0),
          dict(rank="02", name="GRADIENTS", val="4 B", sub="FULL PRECISION", cls="", sent=0),
          dict(rank="03", name="ADAM MOMENTS", val="8 B", sub="TWO BUFFERS", cls="", sent=0),
          dict(rank="=", name="30M VALUES", val="457 MiB", sub="DERIVED", cls="gold", sent=1)])

excl = ("The arithmetic is useful precisely because its assumptions are "
        "visible. Calling that subtotal the required video memory would erase "
        "most of the question we came here to answer.")
p = sents(excl)
win("note", vo=excl,
    kicker="ACT FOUR &middot; WHAT THE SUBTOTAL IS NOT",
    title="DO NOT CALL IT VIDEO MEMORY",
    header_at=S(p, 0),
    note_head="457 MiB EXCLUDES",
    note_items=[
        dict(t="THE FROZEN BASE", sent=1),
        dict(t="SAVED ACTIVATIONS", sent=1),
        dict(t="TEMPORARY WORKSPACES", sent=1),
        dict(t="AND ANYTHING ELSE THE IMPLEMENTATION KEEPS", sent=1)])

tiers = ("On eight gigabytes, regard the three-billion family as a constrained "
         "experiment candidate. Start with short examples, perhaps five hundred "
         "twelve tokens, a microbatch of one, and checkpointing. Those are "
         "starting choices, not a tested fit claim. On twelve gigabytes, retain "
         "that controlled setup before spending the extra room on length or more "
         "examples at once.")
p = sents(tiers)
win("rail", vo=tiers,
    kicker="ACT FOUR &middot; STARTING POINTS, NOT FIT CLAIMS",
    title="EIGHT AND TWELVE GIGABYTES",
    header_at=S(p, 0),
    art="mini_pc",
    rails=[dict(lab="AT 8 GB", val="512 TOKENS", pct=41.0, cls="", sent=1),
           dict(lab="MICROBATCH", val="1", pct=12.0, cls="", sent=2),
           dict(lab="AT 12 GB", val="SAME SETUP", pct=60.0, cls="red", sent=3)])

meas = ("Measure a complete forward pass, backward pass, and optimizer update. "
        "An optimizer can allocate state when the first update happens. A "
        "forward-only demonstration can miss the failure that matters.")
p = sents(meas)
win("note", vo=meas,
    kicker="ACT FOUR &middot; MEASURE THE WHOLE THING",
    title="THE FIRST UPDATE IS WHERE IT BREAKS",
    header_at=S(p, 0),
    note_head="MEASURE ALL THREE PASSES",
    note_items=[
        dict(t="A COMPLETE FORWARD PASS", sent=0),
        dict(t="A COMPLETE BACKWARD PASS", sent=0),
        dict(t="A COMPLETE OPTIMIZER UPDATE", sent=0),
        dict(t="A FORWARD ONLY DEMONSTRATION CAN MISS THE FAILURE THAT MATTERS", sent=2)])

more = ("At sixteen gigabytes, you have more freedom to test broader adapter "
        "targets or longer examples, one change at a time. At twenty-four, a "
        "seven-billion experiment becomes another candidate to investigate after "
        "the smaller control works. Neither capacity guarantees full fine-tuning "
        "or a long-context run.")
p = sents(more)
win("rail", vo=more,
    kicker="ACT FOUR &middot; MORE ROOM, MORE QUESTIONS",
    title="SIXTEEN AND TWENTY FOUR",
    header_at=S(p, 0),
    art="tower_pc",
    rails=[dict(lab="AT 16 GB", val="BROADER", pct=66.0, cls="", sent=0),
           dict(lab="CHANGE AT A TIME", val="1", pct=12.0, cls="", sent=0),
           dict(lab="AT 24 GB", val="7B CANDIDATE", pct=100.0, cls="red", sent=1)])

hw = ("Also check the hardware behind the capacity. Our pinned normal-float "
      "configuration requires a compatible CUDA stack and a device supporting "
      "its selected brain-float computation. Two cards with the same memory "
      "label can require different precision choices and different software "
      "support.")
p = sents(hw)
win("note", vo=hw,
    kicker="ACT FOUR &middot; THE HARDWARE BEHIND THE CAPACITY",
    title="SAME MEMORY LABEL, DIFFERENT CARD",
    header_at=S(p, 0),
    note_head="CHECK BEFORE YOU BUY",
    note_items=[
        dict(t="A COMPATIBLE CUDA STACK", sent=1),
        dict(t="A DEVICE SUPPORTING THE SELECTED BRAIN FLOAT COMPUTATION",
             at="a device supporting its selected brain-float computation"),
        dict(t="TWO CARDS WITH THE SAME LABEL CAN REQUIRE DIFFERENT PRECISION CHOICES", sent=2)])

mac = ("On an Apple machine with sixty-four or one hundred twenty-eight "
       "gigabytes of unified memory, the capacity number describes a "
       "different system. Applications and the operating system share that "
       "pool. The CUDA configuration on screen is not a Mac recipe.")
p = sents(mac)
win("rows", vo=mac,
    kicker="ACT FOUR &middot; UNIFIED MEMORY IS A DIFFERENT SYSTEM",
    title="THE NUMBER DESCRIBES A DIFFERENT MACHINE",
    header_at=S(p, 0),
    art="mac_mini",
    rows=[dict(rank="01", name="UNIFIED MEMORY", val="64 / 128 GB", sub="SHARED POOL", cls="gold", sent=0),
          dict(rank="02", name="THE CAPACITY NUMBER", val="A DIFFERENT SYSTEM", sub="", cls="",
               at="the capacity number describes a different system"),
          dict(rank="03", name="THE OS AND APPS", val="SHARE IT", sub="NOT YOURS", cls="red", sent=1),
          dict(rank="04", name="THE CUDA CONFIG", val="NOT A MAC RECIPE", sub="DIFFERENT BACKEND", cls="", sent=2)])

mlx = ("M L X L M has its own adapter training path, including quantized models "
       "and the Qwen two family. Use that backend's model conversion, targets, "
       "and memory controls. More shared memory can widen the experiments "
       "available; it cannot establish compatibility with another backend's "
       "quantization format or predict the time to finish.")
p = sents(mlx)
win("note", vo=mlx,
    kicker="ACT FOUR &middot; THE OTHER BACKEND",
    title="MLX-LM HAS ITS OWN PATH",
    header_at=S(p, 0),
    note_head="USE THAT BACKEND'S OWN CONTROLS",
    note_items=[
        dict(t="ITS MODEL CONVERSION", sent=1),
        dict(t="ITS TARGETS", sent=1),
        dict(t="ITS MEMORY CONTROLS", sent=1),
        dict(t="MORE SHARED MEMORY CANNOT ESTABLISH COMPATIBILITY", sent=2)])

cache = ("For comparison, calculate this architecture's inference cache "
         "separately. One sequence at eight thousand one hundred ninety-two "
         "tokens needs two hundred eighty-eight mebibytes of logical key and "
         "value storage in sixteen-bit precision. That is about zero point "
         "three zero two decimal gigabytes.")
p = sents(cache)
win("rows", vo=cache,
    kicker="ACT FOUR &middot; THE INFERENCE CACHE, SEPARATELY",
    title="AT 8,192 TOKENS",
    header_at=S(p, 0),
    art="kv_cache",
    rows=[dict(rank="01", name="SEQUENCE", val="8,192", sub="TOKENS", cls="", sent=1),
          dict(rank="02", name="KV STORAGE, 16 BIT", val="288 MiB", sub="DERIVED", cls="gold",
               at="needs two hundred eighty-eight mebibytes"),
          dict(rank="03", name="THE SAME IN DECIMAL", val="0.302 GB", sub="DERIVED", cls="",
               sent=3)])

q8 = ("An ideal Q eight zero payload is one hundred fifty-three mebibytes "
      "because each thirty-two-value block carries thirty-four bytes, "
      "including its scale. Both figures exclude runtime overhead. Neither is a "
      "training peak.")
p = sents(q8)
win("rows", vo=q8,
    kicker="ACT FOUR &middot; THE SAME CACHE, QUANTIZED",
    title="153 MiB, AND STILL NOT A PEAK",
    header_at=S(p, 0),
    art="gguf_blocks",
    rows=[dict(rank="01", name="Q8_0 PAYLOAD", val="153 MiB", sub="IDEAL", cls="gold", sent=0),
          dict(rank="02", name="BLOCK", val="34 BYTES", sub="PER 32 VALUES", cls="",
               at="each thirty-two-value block carries"),
          dict(rank="03", name="SCALE", val="INCLUDED", sub="", cls="", at="including its scale"),
          dict(rank="04", name="RUNTIME OVERHEAD", val="EXCLUDED", sub="NEITHER FIGURE", cls="red", sent=1),
          dict(rank="05", name="TRAINING PEAK", val="NEITHER", sub="NOT THIS", cls="red", sent=2)])

during = ("During training, autograd, loss computation, batch shape, and the "
          "attention implementation change what must remain live. And "
          "checkpointing has a time cost worth counting.")
p = sents(during)
win("note", vo=during,
    kicker="ACT FOUR &middot; DURING TRAINING",
    title="WHAT MUST REMAIN LIVE CHANGES",
    header_at=S(p, 0),
    note_head="THE INFERENCE NUMBERS DO NOT CARRY OVER",
    note_items=[
        dict(t="AUTOGRAD", sent=0),
        dict(t="LOSS COMPUTATION", sent=0),
        dict(t="BATCH SHAPE", sent=0),
        dict(t="THE ATTENTION IMPLEMENTATION", sent=0)])

energy = ("Suppose, purely hypothetically, the whole system averages two hundred "
          "fifty watts for one hour. That is zero point two five "
          "kilowatt-hours. A configuration that uses less memory but takes "
          "longer can consume more total energy, depending on its power draw.")
p = sents(energy)
win("rows", vo=energy,
    kicker="ACT FOUR &middot; THE ENERGY COST",
    title="250 WATTS FOR ONE HOUR",
    header_at=S(p, 0),
    art="psu",
    rows=[dict(rank="01", name="SYSTEM AVERAGE", val="250 W", sub="HYPOTHETICAL", cls="gold", sent=0),
          dict(rank="02", name="OVER ONE HOUR", val="0.25 kWh", sub="DERIVED", cls="", sent=1),
          dict(rank="03", name="LESS MEMORY, LONGER TIME", val="MORE ENERGY", sub="DEPENDS ON DRAW", cls="red", sent=2)])

logit = ("We have no measured power trace for this recipe. Log wall time and "
         "whole-system energy if efficiency matters to your decision. A smaller "
         "checkpoint file cannot tell you how many watt-hours its training "
         "consumed.")
p = sents(logit)
win("note", vo=logit,
    kicker="ACT FOUR &middot; MEASURE THE ENERGY",
    title="LOG IT YOURSELF",
    header_at=S(p, 0),
    note_head="WHAT WE DO NOT HAVE",
    note_items=[
        dict(t="A MEASURED POWER TRACE FOR THIS RECIPE", sent=0),
        dict(t="LOG WALL TIME AND WHOLE SYSTEM ENERGY", sent=1),
        dict(t="A CHECKPOINT FILE CANNOT TELL YOU THE WATT HOURS", sent=2)])

# =================================================================== ACT FIVE
act("FIVE", "CHOOSE THE CHANGE, THEN THE HARDWARE", "in that order",
    "The useful reason to train an adapter is a behavior you can describe and "
    "test.")

hero("Perhaps the model needs to write your team's issue summaries "
     "consistently, apply a stable classification policy, or follow a "
     "domain-specific response pattern. Build representative examples and keep "
     "a separate evaluation set. Compare the adapted result with the same base "
     "model, using the same prompt template and deployment precision. Check "
     "what improved and what regressed.",
     "ACT FIVE &middot; THE REASON TO TRAIN AT ALL", "A BEHAVIOUR YOU CAN TEST",
     "If the problem is a changing spreadsheet, first establish why changing "
     "the weights is necessary.",
     "checklist", side="right",
     blurb_at="apply a stable classification policy")

proced = ("The accompanying Python listing prints an inspectable configuration "
          "only. It downloads no model and starts no training. Its revision, "
          "target modules, rank, precision, length, and microbatch are explicit "
          "so you can review the actual proposal before allocating memory.")
p = sents(proced)
win("rows", vo=proced,
    kicker="ACT FIVE &middot; WHAT THE LISTING DOES",
    title="A CONFIGURATION, NOT A RUN",
    header_at=S(p, 0),
    art="model_file",
    rows=[dict(rank="01", name="REVISION", val="EXPLICIT", sub="", cls="", sent=2),
          dict(rank="02", name="TARGET MODULES", val="EXPLICIT", sub="", cls="", sent=2),
          dict(rank="03", name="RANK AND PRECISION", val="EXPLICIT", sub="", cls="gold", sent=2),
          dict(rank="04", name="LENGTH AND MICROBATCH", val="EXPLICIT", sub="", cls="", sent=2),
          dict(rank="05", name="MODEL DOWNLOADED", val="NO", sub="NO TRAINING", cls="red", sent=1)])

still = ("A complete run still needs tokenized data, a checked loss mask, an "
         "evaluation procedure, and full-step profiling on your machine. After "
         "training, preserve the exact base revision and adapter settings.")
p = sents(still)
win("note", vo=still,
    kicker="ACT FIVE &middot; WHAT A COMPLETE RUN STILL NEEDS",
    title="THE CONFIGURATION IS NOT THE EXPERIMENT",
    header_at=S(p, 0),
    note_head="STILL TO DO",
    note_items=[
        dict(t="TOKENIZED DATA", sent=0),
        dict(t="A CHECKED LOSS MASK", sent=0),
        dict(t="AN EVALUATION PROCEDURE", sent=0),
        dict(t="FULL STEP PROFILING ON YOUR MACHINE", sent=0),
        dict(t="AND PRESERVE THE EXACT BASE REVISION AND ADAPTER SETTINGS", sent=1)])

deploy = ("Check the deployed adapter too: merging and quantized inference "
          "introduce another implementation choice that deserves its own "
          "validation.")
p = sents(deploy)
win("note", vo=deploy,
    kicker="ACT FIVE &middot; AFTER TRAINING",
    title="CHECK THE DEPLOYED ADAPTER",
    header_at=S(p, 0),
    note_head="ANOTHER IMPLEMENTATION CHOICE",
    note_items=[
        dict(t="MERGING INTRODUCES ITS OWN BEHAVIOUR", sent=0),
        dict(t="QUANTIZED INFERENCE INTRODUCES ITS OWN BEHAVIOUR", sent=0),
        dict(t="BOTH DESERVE THEIR OWN VALIDATION", sent=1)])

verdict = ("The verdict is simple. LoRA reduces what you update. Quantized "
           "LoRA also reduces how the frozen base is stored. Neither removes "
           "the rest of the learning process. Buy capacity around a measured "
           "training workload, or reduce the workload until it matches the "
           "hardware you already own.")
p = sents(verdict)
win("title", vo=verdict,
    kicker="BYTE FORENSICS &middot; EPISODE 08 &middot; THE VERDICT",
    title="THE ADAPTER IS SMALL. THE JOB IS NOT.",
    sub="buy capacity around a measured training workload",
    head_at=S(p, 0))

sign = ("The adapter is the change you keep. Training memory is the work "
        "required to discover it. If this saved you a download and a weekend, "
        "subscribe. Byte Forensics breaks down local AI hardware with real "
        "numbers. No hype. See you in the next breakdown.")
p = sents(sign)
win("title", vo=sign,
    kicker="BYTE FORENSICS",
    title="SEE YOU IN THE NEXT BREAKDOWN",
    sub="local AI hardware &middot; real numbers &middot; no hype",
    head_at=S(p, 0))
