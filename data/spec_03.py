from art_lib import (GPU, CHIP, LAPTOP, RAM, SLOT, CACHE, DIE, HEATSINK, TWODIE, PCB,
                     QUANT, TOWER, SYSRAM, PCIELINK)

NAME = "BYTE-03-A"
W = []

def win(layout, vo, cues, **data):
    W.append(dict(layout=layout, vo=vo, cues=cues, **data))

win("stat", "Every video about VRAM tells you what fits. This one is about what happens when it does not. One model, one card, and a window that is two gigabytes too big.",
    {"a": "what happens", "b": "two gigabytes too big", "t": "what fits"},
    art=GPU, big=[("26", "GB", "var(--red)"), ("24", "GB", "var(--cyan)")],
    labels=["needed at 128K", "on your card"], tape="the failure case")

win("table", "Start with the exact numbers. At sixty-four K this model wants twenty-two gigabytes. At one twenty-eight K it wants twenty-six. Twenty-four is the card, so the last row does not fit.",
    {"k": "the exact numbers", "r0": "sixty-four K", "r1": "one twenty-eight K", "r2": "Twenty-four is the card"},
    art=RAM, rows=[("64K", "22 GB", "fits", "good"), ("128K", "26 GB", "2 over", "hot"),
                   ("256K", "34 GB", "10 over", "hot")],
    kicker="qwen 3.8 on 24 gb")

win("stat", "Two gigabytes over is not a small overshoot. It is the difference between a model that runs and a model that starts moving pieces of itself somewhere else.",
    {"a": "not a small overshoot", "b": "somewhere else", "t": "starts moving"},
    art=GPU, big=[("2", "GB", "var(--red)"), ("?", "", "var(--yellow)")],
    labels=["over budget", "where does it go"], tape="it has to go somewhere")

win("callout", "The machine has two kinds of memory. The card has the fast memory the model was loaded into. The motherboard has system memory, which is larger and far slower for this job.",
    {"k": "two kinds of memory", "a": "The card has the fast memory", "b": "system memory"},
    art=SYSRAM, marks=[("system ram", "lt"), ("slots", "rt"), ("slow for this", "lb")])

win("callout", "So the model spills. Layers that no longer fit are pushed across the PCIe bus into system memory, and every token has to pull them back across that bus to compute.",
    {"k": "spills", "a": "PCIe bus", "b": "pull them back"},
    art=PCIELINK, marks=[("vram", "lt"), ("system ram", "rt"), ("the bus", "lb")])

win("quote", "That is the cliff. It is not a gradual slowdown. Throughput falls off a wall, and the wall is on no spec sheet you have ever read.",
    {"a": "the cliff", "b": "no spec sheet", "t": "gradual slowdown"},
    art=TOWER, line="It does not slow down. It falls.", accent="var(--red)", tape="the cliff")

win("chart", "Here is the measured fall on a five-oh-ninety. Seventy-five tokens a second at four K. Fifty-two at sixteen. Thirty-eight at thirty-two. Twenty-eight at sixty-four. And twenty-two at one twenty-eight.",
    {"k": "the measured fall", "a": "Seventy-five tokens", "b": "thirty-eight", "c": "twenty-two"},
    art=GPU, bars=[("4K", "74.8", 100, "var(--lime)"), ("16K", "52.2", 70, "var(--cyan)"),
                   ("32K", "38.0", 51, "var(--yellow)"), ("128K", "22.8", 30, "var(--red)")],
    kicker="tokens per second, 5090", note="measured")

win("chart", "And prefill, which is worse. Four K prompts process at three thousand seven hundred tokens a second. At one twenty-eight K it is four hundred and sixty-one. Prepare to wait.",
    {"k": "prefill, which is worse", "a": "three thousand seven hundred", "b": "four hundred and sixty-one"},
    art=CHIP, bars=[("4K prompt", "3,749", 100, "var(--cyan)"), ("128K prompt", "461", 12, "var(--red)")],
    kicker="prefill, tokens per second", note="measured")

win("stat", "Four hundred and sixty-one tokens a second means a hundred thousand token prompt takes about three and a half minutes before the first word appears. That is the failure, made visible.",
    {"a": "three and a half minutes", "b": "before the first word", "t": "made visible"},
    art=CHIP, big=[("217", "s", "var(--red)"), ("22", "s", "var(--lime)")],
    labels=["100K at 461 t/s", "100K at 4,625 t/s"], tape="time to first token")

win("quote", "The benchmark says it plainly: at one twenty-eight K on a twenty-four gigabyte card, this model is not practical. That is their wording, not mine.",
    {"a": "not practical", "b": "their wording", "t": "one twenty-eight K"},
    art=GPU, line="Not practical on this card.", accent="var(--red)", tape="the benchmark's wording")

win("list", "Three ways you meet this in real life. You paste a long document and the model stalls. You load a bigger model and it never fully fits. Or you open a second monitor and lose the headroom you had.",
    {"k": "Three ways", "a": "paste a long document", "b": "load a bigger model", "c": "second monitor"},
    art=TOWER, rows=[("01", "long document stalls", "hot"), ("02", "model never fits", "hot"),
                     ("03", "second monitor steals it", "hot")],
    kicker="how it shows up")

win("callout", "Your desktop is part of the budget. The compositor, the browser, and a second monitor all take memory before the model has loaded a single layer.",
    {"k": "part of the budget", "a": "The compositor", "b": "a second monitor"},
    art=LAPTOP, marks=[("compositor", "lt"), ("browser", "rt"), ("second monitor", "lb")])

win("stat", "So the usable number is twenty-two, not twenty-four. Every table in every review is two gigabytes optimistic, and that two gigabytes is exactly where this model goes wrong.",
    {"a": "twenty-two, not twenty-four", "b": "two gigabytes optimistic", "t": "goes wrong"},
    art=GPU, big=[("24", "GB", "var(--dim)"), ("22", "GB", "var(--lime)")],
    labels=["on the box", "usable"], tape="plan for 22")

win("pair", "There are two ways out. Buy thirty-two gigabytes instead of twenty-four, or pick a model with a smaller cache so the same window fits.",
    {"l": "two ways out", "a": "thirty-two gigabytes", "b": "smaller cache"},
    art=SLOT, pair=[("32 GB card", "128K fits", "var(--cyan)"), ("24 GB + leaner cache", "256K fits", "var(--lime)")],
    tape="capacity or efficiency")

win("chart", "Two sixteen gigabyte cards give you thirty-two gigabytes and they do reach one twenty-eight K. The cost is throughput: twenty-two tokens at four K, and fifteen at one twenty-eight.",
    {"k": "Two sixteen gigabyte cards", "a": "twenty-two tokens", "b": "fifteen"},
    art=SLOT, bars=[("2 cards 4K", "22.5", 50, "var(--orange)"), ("2 cards 128K", "15.6", 35, "var(--red)"),
                    ("1 card 128K", "38.1", 84, "var(--lime)")],
    kicker="tokens per second", note="capacity, not speed")

win("quote", "So the escape from the cliff is either more memory or a smaller cache. There is no third door where you keep the model, the window, and the card.",
    {"a": "more memory or a smaller cache", "t": "no third door"},
    art=SLOT, line="More memory, or a smaller cache.", accent="var(--yellow)", tape="no third option")

win("list", "How to tell which side of the cliff you are on. Watch VRAM as the context grows. Watch prefill, not just generation. And test at the length you actually paste, not a benchmark prompt.",
    {"k": "How to tell", "a": "Watch VRAM", "b": "Watch prefill", "c": "test at the length"},
    art=GPU, rows=[("01", "watch vram as context grows", "good"), ("02", "watch prefill too", "good"),
                   ("03", "test your real length", "good")],
    kicker="the three signals")

win("table", "The three outcomes, side by side. Glimmer at twenty-four gigabytes: fits. Qwen at sixty-four K: fits. Qwen at one twenty-eight: two gigabytes over, and that is the failure.",
    {"k": "three outcomes", "r0": "Glimmer", "r1": "Qwen at sixty-four", "r2": "Qwen at one twenty-eight"},
    art=RAM, rows=[("Glimmer 256K", "20 GB", "fits", "good"), ("Qwen 64K", "22 GB", "fits", "good"),
                   ("Qwen 128K", "26 GB", "2 over", "hot")],
    kicker="same card, three outcomes")

win("quote", "And the model does not warn you. There is no error message that says you crossed the line. You just watch the tokens per second collapse and wonder what broke.",
    {"a": "does not warn you", "b": "tokens per second collapse", "t": "what broke"},
    art=GPU, line="There is no error message.", accent="var(--red)", tape="the silent failure")

win("list", "Three caveats. These are single GPU measurements with full offload. Spill behaviour depends on your driver and your motherboard. And a cached prompt hides the worst of it, on the second run only.",
    {"k": "Three caveats", "a": "single GPU measurements", "b": "your motherboard", "c": "cached prompt"},
    art=CHIP, rows=[("01", "single gpu, full offload", "hot"), ("02", "driver and board vary", "hot"),
                    ("03", "caching hides run two", "hot")],
    kicker="read these")

win("callout", "The machine is the same machine in every case. Card, system memory, and the bus between them. The only variable is how much of the model you force across that bus.",
    {"k": "The machine", "a": "the bus between them", "b": "how much of the model"},
    art=TOWER, marks=[("the card", "lt"), ("system memory", "rt"), ("the bus", "lb")])

win("stat", "Two gigabytes is the whole story. Two gigabytes is the difference between twenty-two tokens a second and three and a half minutes of waiting.",
    {"a": "Two gigabytes", "b": "three and a half minutes", "t": "the whole story"},
    art=GPU, big=[("2", "GB", "var(--red)"), ("3.5", "min", "var(--yellow)")],
    labels=["over budget", "the wait"], tape="two gigabytes is everything")

win("quote", "So measure the window before you buy the card. And if you already own the card, measure the window before you load the model.",
    {"a": "measure the window", "b": "before you load the model", "t": "already own"},
    art=RAM, line="Measure the window first.", accent="var(--lime)", tape="file . cache . context")

win("stat", "Full tables in the description. Next episode: two cheap cards against one good one, and why the pair loses on the bus.",
    {"a": "Full tables", "b": "Next episode", "c": "loses on the bus"},
    art=SLOT, big=[("NEXT", "", "var(--lime)")], labels=["two cards vs one"], tape="byte forensics")
