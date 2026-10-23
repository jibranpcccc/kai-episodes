from art_lib import (GPU, CHIP, LAPTOP, RAM, SLOT, CACHE, DIE, HEATSINK, TWODIE, PCB,
                     QUANT, TOWER, SYSRAM, PCIELINK, DUALBOARD, PSU, RISER, MINIPC,
                     LAPCUT, SODIMM, GAUGE, WAFER, SUPERCHIP, ROUTER2)

NAME = "BYTE-08-A"
W = []

def win(layout, vo, cues, **data):
    W.append(dict(layout=layout, vo=vo, cues=cues, **data))

win("stat", "Two thousand five hundred and ninety-nine dollars. One hundred and twenty-eight gigabytes of memory. And a claim that this laptop replaces the desktop you were going to build.",
    {"a": "Two thousand five hundred", "b": "One hundred and twenty-eight", "t": "replaces the desktop"},
    art=LAPCUT, big=[("$2,599", "", "var(--lime)"), ("128", "GB", "var(--cyan)")],
    labels=["starting price", "unified memory"], tape="announced october 16")

win("callout", "The part that matters is one package. An RTX graphics chip on the left, a Grace processor on the right, and memory that both of them can reach directly.",
    {"k": "one package", "a": "An RTX graphics chip", "b": "memory"},
    art=SUPERCHIP, marks=[("the gpu", "lt"), ("the cpu", "rt"), ("unified memory", "lb")])

win("stat", "NVIDIA's number for it is up to one petaflop of FP4 compute. That is the company's figure, from the announcement, and it is not an independent measurement.",
    {"a": "one petaflop", "b": "not an independent measurement", "t": "the company's figure"},
    art=CHIP, big=[("1", "PFLOPS", "var(--cyan)"), ("FP4", "", "var(--dim)")],
    labels=["the claim", "the precision"], tape="vendor figure")

win("callout", "And the memory is the reason this laptop is interesting. It is not soldered to the graphics chip alone. Both processors share one pool, which is what makes the number useful.",
    {"k": "the memory", "a": "one pool", "b": "the number useful"},
    art=MINIPC, marks=[("one board", "lt"), ("shared pool", "rt"), ("soldered", "lb")])

win("table", "Now do the arithmetic nobody in the press release does. A seventy-four billion parameter model at four-bit needs roughly forty gigabytes. A twenty-seven billion model needs roughly seventeen.",
    {"k": "the arithmetic", "r0": "seventy-four billion", "r1": "twenty-seven billion"},
    art=RAM, rows=[("74B · 4-bit", "~40 GB", "fits easily", "good"), ("27B · 4-bit", "~17 GB", "fits easily", "good")],
    kicker="parameters to memory")

win("chart", "So the memory is not the limit any more. On a twenty-four gigabyte card, a seventy-four billion model does not fit at all. Here it fits with eighty gigabytes still free.",
    {"k": "not the limit", "a": "does not fit at all", "b": "eighty gigabytes still free"},
    art=RAM, bars=[("RTX 5090", "24 GB", 19, "var(--red)"), ("RTX Spark", "128 GB", 100, "var(--lime)")],
    kicker="memory available", note="24 GB card vs the claim")

win("quote", "Which means the question changes. It is no longer whether the model fits. It is how fast it answers, and how long the battery lasts while it does.",
    {"a": "the question changes", "b": "how fast it answers", "t": "whether the model fits"},
    art=GAUGE, line="Capacity solved. Speed is next.", accent="var(--lime)", tape="the new question")

win("list", "Three things NVIDIA says it runs on day one. A seventy-four billion parameter Nemotron model tuned for tool calls. Local agents including Hermes and OpenClaw. And Adobe Photoshop and Premiere in beta.",
    {"k": "day one", "a": "Nemotron", "b": "Local agents", "c": "Adobe"},
    art=CHIP, rows=[("01", "nemotron 74b local", "good"), ("02", "hermes, openclaw agents", "good"),
                    ("03", "photoshop, premiere beta", "good")],
    kicker="what ships with it")

win("callout", "And there is a router feature. One of these laptops can serve models to the other computers in your house, so the desktop does not need its own graphics card to use them.",
    {"k": "a router feature", "a": "serve models", "b": "does not need its own"},
    art=ROUTER2, marks=[("the laptop", "lt"), ("other machines", "rt"), ("over the network", "lb")])

win("table", "The machines, as announced. ASUS ProArt, Dell XPS 16, HP OmniBook, Lenovo Yoga Pro, and Microsoft Surface Laptop Ultra.",
    {"k": "The machines", "r0": "ASUS ProArt", "r1": "Dell XPS 16", "r2": "Surface Laptop Ultra"},
    art=LAPTOP, rows=[("ASUS / Dell / HP", "available", "today", "good"),
                      ("Lenovo / MSI", "available", "today", "good"),
                      ("Surface Ultra", "available", "today", "good")],
    kicker="the launch lineup")

win("stat", "Six manufacturers, ten models, all on shelves now. The cheapest configuration is two thousand five hundred and ninety-nine dollars.",
    {"a": "Six manufacturers", "b": "two thousand five hundred", "t": "all on shelves"},
    art=SODIMM, big=[("6", "OEMs", "var(--cyan)"), ("10", "models", "var(--lime)")],
    labels=["manufacturers", "configurations"], tape="shipping today")

win("quote", "Two thousand six hundred dollars is not a laptop price. It is a workstation price, and it should be judged like one.",
    {"a": "not a laptop price", "b": "a workstation price", "t": "judged like one"},
    art=LAPCUT, line="$2,599 is workstation money.", accent="var(--yellow)", tape="judge it as one")

win("stat", "For comparison, the card in most of these videos has twenty-four gigabytes and no battery. This has five times the memory, one fifth of the power budget, and a screen attached.",
    {"a": "five times the memory", "b": "one fifth of the power", "t": "a screen attached"},
    art=SUPERCHIP, big=[("128", "GB", "var(--cyan)"), ("24", "GB", "var(--dim)")],
    labels=["unified", "the card"], tape="memory vs power")

win("list", "Three things the announcement does not tell you. What the tokens per second actually are. What happens when the battery is not plugged in. And how much of that memory the operating system keeps.",
    {"k": "does not tell you", "a": "tokens per second", "b": "the battery", "c": "the operating system"},
    art=LAPTOP, rows=[("01", "no tokens per second", "hot"), ("02", "no battery-loaded number", "hot"),
                      ("03", "os keeps some memory", "hot")],
    kicker="the missing numbers")

win("quote", "A petaflop is a peak number at a precision nobody runs their model in. It is not the number you will feel when you press enter.",
    {"a": "a peak number", "b": "when you press enter", "t": "nobody runs their model in"},
    art=CHIP, line="Peak is not throughput.", accent="var(--red)", tape="fp4 vs real work")

win("table", "Here is what is claimed and what is checkable today. Memory: checkable, it is a spec. Price: checkable. Petaflops: a vendor figure. Tokens per second: not published yet.",
    {"k": "claimed and checkable", "r0": "Memory", "r1": "Price", "r2": "Petaflops"},
    art=PCB, rows=[("128 GB memory", "spec sheet", "checkable", "good"), ("$2,599", "announced", "checkable", "good"),
                   ("1 PFLOPS FP4", "vendor", "unverified", "hot")],
    kicker="claims vs evidence")

win("callout", "The ecosystem is the other half of the story. This is Windows on Arm, and NVIDIA says it now has a native PyTorch CUDA build, a native Python, and support for ninety-seven percent of the top fifteen thousand packages.",
    {"k": "The ecosystem", "a": "Windows on Arm", "b": "ninety-seven percent"},
    art=WAFER, marks=[("the silicon", "lt"), ("many dies", "rt"), ("yield varies", "lb")])

win("list", "Three questions to ask before you buy one. Does your software run on Arm. Do you need the memory or the speed. And would a desktop card plus a cheap laptop cost less.",
    {"k": "Three questions", "a": "run on Arm", "b": "memory or the speed", "c": "cost less"},
    art=TOWER, rows=[("01", "does your software run on arm", "good"), ("02", "memory or speed", "good"),
                     ("03", "card plus laptop cheaper", "good")],
    kicker="before you buy")

win("stat", "NVIDIA also says there are one hundred and fifty million RTX AI PCs already out there. That is a claim about install base, and it is the reason software will follow this thing.",
    {"a": "one hundred and fifty million", "b": "install base", "t": "software will follow"},
    art=GPU, big=[("150", "M", "var(--cyan)"), ("RTX", "", "var(--dim)")],
    labels=["ai pcs", "the platform"], tape="vendor figure")

win("quote", "So this is the first laptop where the memory argument is settled and the speed argument is not. That is a real change, and it is not the same as a fast machine.",
    {"a": "memory argument is settled", "b": "speed argument is not", "t": "a real change"},
    art=SUPERCHIP, line="Capacity solved, speed unproven.", accent="var(--lime)", tape="the honest summary")

win("list", "Three caveats. Every performance number here is from NVIDIA's own announcement. No independent benchmark of this chip exists yet. And availability, configuration and price vary by region.",
    {"k": "Three caveats", "a": "NVIDIA's own announcement", "b": "No independent benchmark", "c": "vary by region"},
    art=CHIP, rows=[("01", "vendor numbers only", "hot"), ("02", "no independent test", "hot"),
                    ("03", "region pricing varies", "hot")],
    kicker="read these")

win("quote", "When independent tokens per second land, this channel will measure them the same way it measured every card in the last six videos. Until then, treat the petaflop as marketing.",
    {"a": "independent tokens per second", "b": "treat the petaflop as marketing", "t": "the same way"},
    art=GAUGE, line="Wait for the measurement.", accent="var(--yellow)", tape="our rule")

win("stat", "Full source link in the description. Two thousand five hundred ninety-nine dollars, one hundred and twenty-eight gigabytes, and a question nobody has answered yet: how many tokens per second.",
    {"a": "Full source link", "b": "how many tokens per second", "t": "nobody has answered"},
    art=LAPCUT, big=[("$2,599", "", "var(--lime)"), ("?", "t/s", "var(--red)")],
    labels=["the price", "the unknown"], tape="byte forensics")
