"""Episode 01 — How Much VRAM Does Qwen 3.8 27B Really Need?

Angle: THE MEASUREMENT. What the numbers are, how they were taken, and where
the card runs out. The file-size paradox belongs to episode 02; spilling and
the cliff belong to 03.
"""
from art_lib import GPU, CHIP, LAPTOP, RAM, SLOT, CACHE, DIE, HEATSINK

NAME = "BYTE-01-A"
W = []


def win(layout, vo, cues, **data):
    W.append(dict(layout=layout, vo=vo, cues=cues, **data))


win("stat", "Twenty-four gigabytes of VRAM, one model, and a question nobody answers with measurements. Tonight the answer is a table, not an opinion.",
    {"a": "Twenty-four gigabytes", "b": "a table", "t": "not an opinion"},
    art=GPU, big=[("24", "GB", "var(--cyan)"), ("27", "B", "var(--lime)")],
    labels=["your card", "the model"], tape="measured, not estimated")

win("callout", "Here is the rig. One card, full offload, Flash Attention on, a stock build of llama dot cpp. No CPU spill, no sharding, nothing clever that would flatter the numbers.",
    {"k": "the rig", "a": "full offload", "b": "nothing clever"},
    art=GPU, marks=[("the card", "lt"), ("memory · loaded", "rt"), ("slot · one card", "lb")])

win("stat", "The model is twenty-seven point three two billion parameters. At four-bit it lands at sixteen point six eight gigabytes on disk, and that file is what loads into memory first.",
    {"a": "twenty-seven point three two", "b": "sixteen point six eight", "t": "loads into memory"},
    art=DIE, big=[("27.32", "B", "var(--lime)"), ("16.68", "GiB", "var(--cyan)")],
    labels=["parameters", "file on disk"], tape="one die, one file")

win("list", "Three things were recorded at every context length. Total VRAM in use. Prefill, which is the wait before the first token. And generation, which is how fast words arrive after that.",
    {"k": "Three things", "a": "Total VRAM", "b": "Prefill", "c": "generation"},
    art=CHIP, rows=[("VRAM", "measured directly", "good"), ("PREFILL", "time to first token", "good"),
                    ("GENERATION", "tokens per second", "good")],
    kicker="what the test recorded")

win("chart", "First half of the curve. Eighteen gigabytes at four K. Eighteen again at eight K. Nineteen at sixteen K. Twenty at thirty-two. The file is not moving, the cache is.",
    {"k": "First half", "a": "Eighteen gigabytes", "b": "Nineteen at sixteen", "c": "Twenty at thirty-two"},
    art=RAM, bars=[("4K", "18 GB", 53, "var(--lime)"), ("8K", "18 GB", 53, "var(--lime)"),
                   ("16K", "19 GB", 56, "var(--cyan)"), ("32K", "20 GB", 59, "var(--cyan)")],
    kicker="vram by context · part one", note="measured")

win("chart", "Second half. Twenty-two gigabytes at sixty-four K. Twenty-six at one twenty-eight. And thirty-four at two fifty-six, which does not fit on a twenty-four gigabyte card at all.",
    {"k": "Second half", "a": "Twenty-two gigabytes", "b": "Twenty-six", "c": "thirty-four"},
    art=RAM, bars=[("64K", "22 GB", 65, "var(--yellow)"), ("128K", "26 GB", 76, "var(--orange)"),
                   ("256K", "34 GB", 100, "var(--red)")],
    kicker="vram by context · part two", note="the last row does not fit")

win("quote", "The curve is not linear. It is flat for the first thirty-two K, then it bends, and the bend is where your card stops being enough.",
    {"a": "not linear", "t": "stops being enough"},
    art=RAM, line="The bend is the answer.", accent="var(--yellow)", tape="flat, then it bends")

win("callout", "The die is where those parameters live. Everything in the middle is compute. The cache does not grow on the die, it grows beside the model, in the memory you are actually buying.",
    {"k": "The die", "a": "compute", "b": "memory you are buying"},
    art=DIE, marks=[("the die", "lt"), ("compute block", "rt"), ("one package", "lb")])

win("table", "Here is the whole table in one place. Four K, eighteen. Sixteen K, nineteen. Thirty-two K, twenty. Sixty-four K, twenty-two. And two fifty-six K, thirty-four.",
    {"k": "the whole table", "r0": "Four K", "r1": "Sixteen K", "r2": "Thirty-two K", "r3": "Sixty-four K", "r4": "two fifty-six K"},
    art=RAM, rows=[("4K", "18", "fit", "good"), ("16K", "19", "fit", "good"), ("32K", "20", "fit", "good"),
                   ("64K", "22", "fit", "hot"), ("256K", "34", "no", "hot")],
    kicker="qwen 3.8 27b · measured")

win("stat", "At sixty-four K you are using twenty-two of twenty-four gigabytes. Two gigabytes left. That is not headroom, that is the minimum your desktop needs to keep drawing the screen.",
    {"a": "twenty-two of twenty-four", "b": "Two gigabytes", "t": "keep drawing the screen"},
    art=GPU, big=[("22", "GB", "var(--yellow)"), ("2", "GB", "var(--red)")],
    labels=["used", "left"], tape="64K is the ceiling")

win("quote", "So sixty-four K is the honest ceiling on this card, and every number after that is a measurement of something you cannot actually run.",
    {"a": "sixty-four K", "t": "cannot actually run"},
    art=GPU, line="64K is the ceiling.", accent="var(--yellow)", tape="24 GB · 64K")

win("callout", "Cooling is not your limit. The heat sink and the fan decide how fast the card can run for a long time, not how much memory it has. That number was fixed when you bought it.",
    {"k": "Cooling is not", "a": "heat sink", "b": "how much memory"},
    art=HEATSINK, marks=[("heat sink", "lt"), ("fins", "rt"), ("fixed at purchase", "lb")])

win("chart", "Now generation on a three thousand ninety. Forty tokens a second at four K. Thirty-seven at thirty-two K. Thirty-four at sixty-four K. And thirty-three at one twenty-eight, which the card runs, but barely fits.",
    {"k": "generation on a three thousand ninety", "a": "Forty tokens", "b": "thirty-four", "c": "thirty-three"},
    art=GPU, bars=[("4K", "40.3", 100, "var(--lime)"), ("32K", "37.0", 92, "var(--lime)"),
                   ("64K", "33.9", 84, "var(--yellow)"), ("128K", "33.9*", 84, "var(--red)")],
    kicker="tokens per second, 3090", note="* VRAM does not fit at 128K")

win("chart", "The five-oh-ninety has the same twenty-four gigabytes and much higher throughput. Seventy-four tokens a second at four K, fifty-two at sixteen, and it falls to twenty-two by one twenty-eight because the cache outgrows the card.",
    {"k": "five-oh-ninety", "a": "Seventy-four tokens", "b": "fifty-two", "c": "twenty-two"},
    art=GPU, bars=[("4K", "74.8", 100, "var(--cyan)"), ("16K", "52.2", 70, "var(--cyan)"),
                   ("32K", "38.0", 51, "var(--yellow)"), ("128K", "22.8", 30, "var(--red)")],
    kicker="tokens per second, 5090", note="throughput falls as the cache grows")

win("quote", "A faster card buys throughput at short context. It does not buy the window, because the window is set by memory and both cards have exactly the same amount.",
    {"a": "buys throughput", "t": "the same amount"},
    art=GPU, line="Faster is not more memory.", accent="var(--cyan)", tape="both cards: 24 GB")

win("table", "There is a middle card people forget. The four-oh-ninety does forty-six tokens a second at four K against forty on the three thousand ninety. Fifteen percent more, for a much higher price.",
    {"k": "a middle card", "r0": "forty-six", "r1": "forty on the three thousand ninety"},
    art=GPU, rows=[("3090 · 4K", "40.3", "24 GB", "good"), ("4090 · 4K", "46.2", "24 GB", "hot"),
                   ("5090 · 4K", "74.8", "24 GB", "good")],
    kicker="same memory, different speed")

win("stat", "Prefill is the number you feel first. Thirteen hundred tokens a second at four K, on the three thousand ninety. At sixty-four K it is seven hundred and sixty-seven, and at that point you are watching a cursor.",
    {"a": "Prefill", "b": "Thirteen hundred", "c": "seven hundred and sixty-seven"},
    art=CHIP, big=[("1308", "t/s", "var(--lime)"), ("767", "t/s", "var(--red)")],
    labels=["4K prompt", "64K prompt"], tape="time to first token")

win("chart", "Turn that into seconds for a hundred thousand token prompt. Forty-six hundred tokens a second is twenty-two seconds. Seven hundred and sixty is two minutes and eleven. Same document, same card.",
    {"k": "turn that into seconds", "a": "twenty-two seconds", "b": "two minutes and eleven"},
    art=CHIP, bars=[("100K @ 4,625", "22 s", 18, "var(--lime)"), ("100K @ 767", "131 s", 100, "var(--red)")],
    kicker="time to first token", note="lower is better")

win("quote", "That is the difference between an assistant and a loading screen, and it is not a model quality question. It is a measurement you can take in ten minutes.",
    {"a": "assistant and a loading screen", "t": "ten minutes"},
    art=LAPTOP, line="Measure it yourself in ten minutes.", accent="var(--lime)", tape="the wait is measurable")

win("list", "How to measure your own card. Load the model at the context you actually use. Read VRAM before you type anything. Then double the context and watch where the number stops climbing.",
    {"k": "How to measure", "a": "Load the model", "b": "Read VRAM", "c": "double the context"},
    art=GPU, rows=[("01", "load at your context", "good"), ("02", "read vram before typing", "good"),
                   ("03", "double and watch the bend", "good")],
    kicker="the ten minute test")

win("callout", "And leave room for the desktop. The compositor, the browser, and a second monitor all take memory before the model has loaded a single layer.",
    {"k": "leave room", "a": "The compositor", "b": "a second monitor"},
    art=LAPTOP, marks=[("compositor", "lt"), ("browser", "rt"), ("second monitor", "lb")])

win("stat", "Which is why twenty-four is really twenty-two. Every number in this video holds at twenty-two, and none of them hold at twenty-four with two monitors attached.",
    {"a": "twenty-two", "b": "none of them hold", "t": "two monitors"},
    art=GPU, big=[("24", "GB", "var(--dim)"), ("22", "GB", "var(--lime)")],
    labels=["on the box", "usable"], tape="plan for 22")

win("table", "So here is the measured answer, in one table you can screenshot. Four K to sixty-four K fits. One twenty-eight does not. Two fifty-six is not a conversation about this card.",
    {"k": "the measured answer", "r0": "Four K to sixty-four", "r1": "One twenty-eight", "r2": "Two fifty-six"},
    art=RAM, rows=[("4K–64K", "18–22", "fits", "good"), ("128K", "26", "no", "hot"), ("256K", "34", "no", "hot")],
    kicker="screenshot this")

win("quote", "Every number in this video was measured on one card with one build. That is the standard I am holding this channel to, and it is the reason you can check me.",
    {"a": "measured on one card", "t": "check me"},
    art=DIE, line="Measured, or it didn't happen.", accent="var(--lime)", tape="one card · one build")

win("stat", "Full tables in the description. Next episode is the one that should not be possible: a thirty billion parameter model that uses less memory than a twenty-seven billion one.",
    {"a": "Full tables", "b": "Next episode", "c": "less memory"},
    art=GPU, big=[("→", "", "var(--lime)")], labels=["next: 30B vs 27B"], tape="byte forensics")
