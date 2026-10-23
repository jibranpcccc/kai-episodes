"""Episode 02 — The 30B That Uses Less VRAM Than The 27B

Angle: THE PARADOX. A bigger model ships in a smaller file, and the reason is the
quantization recipe plus a leaner cache — not magic, and not fewer parameters.
Measurement methodology belongs to episode 01; spilling belongs to 03.
"""
from art_lib import GPU, CHIP, LAPTOP, RAM, SLOT, CACHE, DIE, HEATSINK, TWODIE, PCB, QUANT

NAME = "BYTE-02-A"
W = []


def win(layout, vo, cues, **data):
    W.append(dict(layout=layout, vo=vo, cues=cues, **data))


win("stat", "A thirty billion parameter model that ships smaller than a twenty-seven billion one. Same card, same window, less memory. That is the whole video.",
    {"a": "thirty billion", "b": "twenty-seven billion", "t": "whole video"},
    art=TWODIE, big=[("30", "B", "var(--lime)"), ("27", "B", "var(--dim)")],
    labels=["Glimmer", "Qwen 3.8"], tape="the bigger model is smaller")

win("pair", "Two files, measured on disk. Qwen three point eight twenty-seven B is sixteen point six eight gigabytes. Glimmer thirty B is fourteen point seven eight. The larger model is almost two gigabytes smaller.",
    {"l": "Two files", "a": "sixteen point six eight", "b": "fourteen point seven eight", "t": "two gigabytes smaller"},
    art=RAM, pair=[("Qwen 3.8 27B", "16.68 GiB", "var(--dim)"), ("Glimmer 30B", "14.78 GiB", "var(--lime)")],
    tape="16.68 vs 14.78")

win("table", "Put the two spec sheets side by side. Glimmer: twenty-seven point eight five billion active parameters. Qwen: twenty-seven point three two. Two percent apart, before either file is quantized.",
    {"k": "the two spec sheets", "r0": "twenty-seven point eight five", "r1": "twenty-seven point three two"},
    art=TWODIE, rows=[("Glimmer 30B", "27.85 B", "dense", "good"), ("Qwen 3.8 27B", "27.32 B", "dense", "good")],
    kicker="parameters, not files")

win("callout", "The reason is not compression magic. The reason is the recipe. Glimmer was measured at four-bit medium. Qwen was measured at four-bit small. Different recipes, different file sizes.",
    {"k": "The reason", "a": "four-bit medium", "b": "four-bit small"},
    art=QUANT, marks=[("4-bit medium", "lt"), ("4-bit small", "rt"), ("the recipe decides", "lb")])

win("chart", "Only two file sizes were actually measured, and they are the two that matter. Sixteen point six eight gigabytes for Qwen at four-bit small. Fourteen point seven eight for Glimmer at four-bit medium.",
    {"k": "Only two file sizes", "a": "Sixteen point six eight", "b": "Fourteen point seven eight"},
    art=QUANT, bars=[("Qwen · 4-bit small", "16.68 GiB", 100, "var(--cyan)"),
                     ("Glimmer · 4-bit medium", "14.78 GiB", 89, "var(--lime)")],
    kicker="the two measured files", note="harder recipes were not measured here")

win("callout", "Now the part the recipe does not explain. At the same quantization the two files were still not the same size. So the model itself, its shape, its attention, is buying you the rest.",
    {"k": "the recipe does not explain", "a": "its shape", "b": "its attention"},
    art=PCB, marks=[("the board", "lt"), ("the modules", "rt"), ("traces carry it", "lb")])

win("stat", "The file difference is two gigabytes. The cache difference, at two fifty-six K, is fourteen. That is the number that decides whether this model runs on your card.",
    {"a": "two gigabytes", "b": "fourteen", "t": "whether this model runs"},
    art=RAM, big=[("2", "GB", "var(--dim)"), ("14", "GB", "var(--red)")],
    labels=["file", "cache at 256K"], tape="the cache decides")

win("list", "Two things load into your VRAM. The weights, a file whose size is fixed at download. And the cache, whose size is decided by how long you talk to it.",
    {"k": "Two things load", "a": "The weights", "b": "the cache"},
    art=RAM, rows=[("WEIGHTS", "fixed at download", "good"), ("KV CACHE", "decided by context", "hot")],
    kicker="what loads")

win("chart", "Measured on one twenty-four gigabyte card. Glimmer needs sixteen gigabytes at four K and peaks at twenty at two fifty-six. Qwen starts at eighteen and ends at thirty-four.",
    {"k": "Measured on one", "a": "sixteen gigabytes", "b": "twenty at two fifty-six", "c": "thirty-four"},
    art=GPU, bars=[("Glimmer · 4K", "16 GB", 47, "var(--lime)"), ("Glimmer · 256K", "20 GB", 59, "var(--lime)"),
                   ("Qwen · 4K", "18 GB", 53, "var(--cyan)"), ("Qwen · 256K", "34 GB", 100, "var(--red)")],
    kicker="vram by context", note="measured")

win("table", "The full curve for both. Four K, sixteen against eighteen. Thirty-two K, sixteen against twenty. Sixty-four K, seventeen against twenty-two. Two fifty-six K, twenty against thirty-four.",
    {"k": "The full curve", "r0": "Four K", "r1": "Thirty-two K", "r2": "Sixty-four K", "r3": "Two fifty-six K"},
    art=RAM, rows=[("4K", "16", "18", "good"), ("32K", "16", "20", "good"),
                   ("64K", "17", "22", "hot"), ("256K", "20", "34", "hot")],
    kicker="glimmer vs qwen")

win("quote", "So on twenty-four gigabytes, one model holds its entire window and the other one has to be planned around. Same card, four times the context.",
    {"a": "entire window", "t": "four times the context"},
    art=GPU, line="Same card. Four times the context.", accent="var(--lime)", tape="24 GB")

win("callout", "The mechanism is the cache. Every token writes a key matrix and a value matrix. Those matrices scale with context length, and they do not care how many parameters the model has.",
    {"k": "The mechanism", "a": "key matrix", "b": "context length"},
    art=CACHE, marks=[("key matrix", "lt"), ("value matrix", "rt"), ("context length", "lb")])

win("list", "Three things that are not true, and all three get repeated. More parameters means more memory. A bigger number on the box means a better experience. A faster card fixes capacity.",
    {"k": "Three things", "a": "More parameters", "b": "A bigger number", "c": "A faster card"},
    art=CHIP, rows=[("PARAMETERS", "not memory", "hot"), ("BOX NUMBERS", "not experience", "hot"),
                    ("SPEED", "not capacity", "hot")],
    kicker="all three are false")

win("chart", "On a three thousand ninety, Glimmer generates forty-five tokens a second at four K and forty-two at sixty-four K. Qwen does forty and thirty-four. Close at short context, apart at long.",
    {"k": "three thousand ninety", "a": "forty-five tokens", "b": "forty-two", "c": "thirty-four"},
    art=GPU, bars=[("Glimmer · 4K", "45.3", 100, "var(--lime)"), ("Qwen · 4K", "40.3", 89, "var(--cyan)"),
                   ("Glimmer · 64K", "42.5", 94, "var(--lime)"), ("Qwen · 64K", "33.9", 75, "var(--yellow)")],
    kicker="tokens per second, 3090", note="measured")

win("chart", "On a five-oh-ninety the gap opens. Eighty-three against seventy-four at four K. At one twenty-eight K, seventy-five against twenty-two, and that gap is the cache, not the silicon.",
    {"k": "five-oh-ninety", "a": "Eighty-three", "b": "seventy-four", "c": "twenty-two"},
    art=GPU, bars=[("Glimmer · 4K", "83.2", 100, "var(--lime)"), ("Qwen · 4K", "74.8", 90, "var(--cyan)"),
                   ("Glimmer · 128K", "75.8", 91, "var(--lime)"), ("Qwen · 128K", "22.8", 27, "var(--red)")],
    kicker="tokens per second, 5090", note="measured")

win("chart", "At sixty-four K the measured difference is five gigabytes. Seventeen for Glimmer, twenty-two for Qwen. At two fifty-six K it is twenty against thirty-four, a fourteen gigabyte gap on the same card.",
    {"k": "sixty-four K", "a": "Seventeen for Glimmer", "b": "twenty-two for Qwen", "c": "twenty against thirty-four"},
    art=CACHE, bars=[("64K · Glimmer", "17 GB", 50, "var(--lime)"), ("64K · Qwen", "22 GB", 65, "var(--yellow)"),
                     ("256K · Glimmer", "20 GB", 59, "var(--lime)"), ("256K · Qwen", "34 GB", 100, "var(--red)")],
    kicker="the measured gap", note="same card, same context")

win("quote", "So stop shopping by parameter count. Shop by the file, the cache, and the context you actually use. Those three numbers are printed on the page.",
    {"a": "stop shopping", "b": "the file, the cache", "t": "printed on the page"},
    art=RAM, line="Shop by the window, not the model.", accent="var(--lime)", tape="file · cache · context")

win("stat", "Full tables in the description. Next episode is the failure case: what actually happens at one twenty-eight K when the card runs out of room.",
    {"a": "Full tables", "b": "Next episode", "c": "runs out of room"},
    art=GPU, big=[("→", "", "var(--lime)")], labels=["next: the failure case"], tape="byte forensics")
