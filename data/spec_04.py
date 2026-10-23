from art_lib import (GPU, CHIP, LAPTOP, RAM, SLOT, CACHE, DIE, HEATSINK, TWODIE, PCB,
                     QUANT, TOWER, SYSRAM, PCIELINK, DUALBOARD, PSU, RISER)

NAME = "BYTE-04-A"
W = []

def win(layout, vo, cues, **data):
    W.append(dict(layout=layout, vo=vo, cues=cues, **data))

win("stat", "Two cheap cards against one expensive one. On paper the pair wins by eight gigabytes. Tonight we find out what that eight gigabytes actually costs.",
    {"a": "Two cheap cards", "b": "eight gigabytes", "t": "actually costs"},
    art=DUALBOARD, big=[("32", "GB", "var(--orange)"), ("24", "GB", "var(--lime)")],
    labels=["two cards", "one card"], tape="the two-card route")

win("callout", "Start with the board, because the board is the argument. Two slots, two cards, and one bus between them and the processor. Everything else follows from that single wire.",
    {"k": "the board", "a": "Two slots", "b": "one bus"},
    art=DUALBOARD, marks=[("slot one", "lt"), ("slot two", "rt"), ("the chipset", "lb")])

win("pair", "Two sixteen gigabyte cards hold thirty-two gigabytes. One three thousand ninety holds twenty-four. Four gigabytes per card is not much memory, but the total is larger.",
    {"l": "Two sixteen", "a": "thirty-two gigabytes", "b": "twenty-four", "t": "the total is larger"},
    art=SLOT, pair=[("2 x 5060 Ti", "32 GB", "var(--orange)"), ("1 x 3090", "24 GB", "var(--lime)")],
    tape="32 vs 24")

win("callout", "The power supply has to feed both cards. Two connectors, two cables, and a rating that covers both at once, not one after the other.",
    {"k": "The power supply", "a": "Two connectors", "b": "both at once"},
    art=PSU, marks=[("the fan", "lt"), ("rail one", "rt"), ("rail two", "lb")])

win("callout", "And the second card needs a riser, because it will not physically fit beside the first. The riser is another length of copper between the model and the memory it lives in.",
    {"k": "needs a riser", "a": "another length of copper", "b": "the memory"},
    art=RISER, marks=[("the board", "lt"), ("the ribbon", "rt"), ("the card", "lb")])

win("quote", "So the pair is not one machine with thirty-two gigabytes. It is two machines passing layers across a wire, and every layer boundary is a delay.",
    {"a": "not one machine", "b": "a delay", "t": "thirty-two gigabytes"},
    art=DUALBOARD, line="Two machines, one wire.", accent="var(--orange)", tape="the cost is the bus")

win("chart", "Measured on one long request, not a queue. At four K the pair does twenty-two tokens a second. The single three thousand ninety does forty. At the same window the pair is half the speed.",
    {"k": "one long request", "a": "twenty-two tokens", "b": "forty", "c": "half the speed"},
    art=SLOT, bars=[("2 cards 4K", "22.5", 50, "var(--orange)"), ("1 card 4K", "40.3", 90, "var(--lime)")],
    kicker="tokens per second", note="one request, not a queue")

win("stat", "At one twenty-eight K the pair still runs, at fifteen tokens a second, because thirty-two gigabytes is enough. The single card does thirty-eight, and needs no explanation.",
    {"a": "fifteen tokens", "b": "thirty-eight", "t": "still runs"},
    art=SLOT, big=[("15.6", "t/s", "var(--orange)"), ("38.1", "t/s", "var(--lime)")],
    labels=["2 cards", "1 card"], tape="capacity bought, speed lost")

win("quote", "Two cards buy capacity. They never buy speed. That sentence is the whole episode, and every number after it is just evidence.",
    {"a": "buy capacity", "t": "just evidence"},
    art=CHIP, line="Capacity, not speed.", accent="var(--orange)", tape="the thesis")

win("chart", "Here is the shape of the loss. One card, one request, throughput against context. The pair follows the same curve, shifted down by roughly half at every point.",
    {"k": "the shape of the loss", "a": "shifted down", "b": "half at every point"},
    art=GPU, bars=[("4K", "22.5", 50, "var(--orange)"), ("32K", "19.8", 44, "var(--yellow)"),
                   ("128K", "15.6", 35, "var(--red)")],
    kicker="the pair, by context", note="measured")

win("list", "Three things the pair genuinely gives you. A window a single card cannot hold. Two cards bought over time instead of one large purchase. And redundancy if one card fails.",
    {"k": "Three things", "a": "A window", "b": "bought over time", "c": "redundancy"},
    art=DUALBOARD, rows=[("01", "a bigger window", "good"), ("02", "buy over time", "good"),
                         ("03", "redundancy", "good")],
    kicker="what you actually gain")

win("list", "And three things it costs. Half the throughput. Twice the power and heat. And a driver stack that has to split one model across two devices without getting it wrong.",
    {"k": "And three things it costs", "a": "Half the throughput", "b": "Twice the power", "c": "a driver stack"},
    art=PSU, rows=[("01", "half the throughput", "hot"), ("02", "twice the power", "hot"),
                   ("03", "split-model drivers", "hot")],
    kicker="what it costs")

win("callout", "There is a third option people forget. Buy one card with more memory instead of two with less. Thirty-two gigabytes on a single card exists, and it has no bus in the middle.",
    {"k": "a third option", "a": "more memory", "b": "no bus in the middle"},
    art=GPU, marks=[("one card", "lt"), ("more memory", "rt"), ("no bus", "lb")])

win("table", "Three routes, one table. Two cards: thirty-two gigabytes, twenty-two tokens. One thirty-two gigabyte card: thirty-two gigabytes, and no inter-card traffic at all. One twenty-four: the baseline.",
    {"k": "Three routes", "r0": "Two cards", "r1": "One thirty-two", "r2": "One twenty-four"},
    art=PSU, rows=[("2 x 16 GB", "32 GB", "22.5 t/s", "hot"), ("1 x 32 GB", "32 GB", "single bus", "good"),
                         ("1 x 24 GB", "24 GB", "40.3 t/s", "good")],
    kicker="the three routes")

win("quote", "The single card wins on everything except price. That is not a benchmark result, that is what a bus does when you put a model across it.",
    {"a": "wins on everything except price", "b": "what a bus does", "t": "single card"},
    art=GPU, line="One card, one bus, no waiting.", accent="var(--lime)", tape="the bus decides")

win("callout", "And the machine has to hold it. Two cards need airflow between them, a board with spacing, and a case that does not turn the second card into an oven.",
    {"k": "the machine", "a": "airflow", "b": "an oven"},
    art=RISER, marks=[("the board", "lt"), ("the gap", "rt"), ("airflow", "lb")])

win("stat", "The honest summary is arithmetic. Thirty-two gigabytes for two cards, at half the speed of one card with twenty-four. You are trading throughput for capacity, at a fixed exchange rate.",
    {"a": "Thirty-two gigabytes", "b": "half the speed", "t": "fixed exchange rate"},
    art=SLOT, big=[("32", "GB", "var(--orange)"), ("1/2", "speed", "var(--red)")],
    labels=["capacity", "throughput"], tape="the exchange rate")

win("list", "Who should actually buy the pair. People running one long document that must fit. People who already own one card. And people who cannot buy a single large card at all.",
    {"k": "Who should", "a": "one long document", "b": "already own one card", "c": "cannot buy"},
    art=TOWER, rows=[("01", "one long document", "good"), ("02", "already own one", "good"),
                         ("03", "single card unavailable", "good")],
    kicker="the honest answer")

win("table", "And the numbers that matter when you decide. Memory, throughput at four K, throughput at one twenty-eight, and whether the model fits at all.",
    {"k": "the numbers that matter", "r0": "Memory", "r1": "throughput at four K", "r2": "one twenty-eight"},
    art=RAM, rows=[("2 x 16 GB", "32 GB", "22.5", "hot"), ("1 x 32 GB", "32 GB", "single device", "good"),
                   ("1 x 24 GB", "24 GB", "40.3", "good")],
    kicker="decide with this")

win("quote", "So the pair is not a mistake. It is a specific purchase for a specific problem, and the problem is memory, not speed.",
    {"a": "not a mistake", "b": "memory, not speed", "t": "specific purchase"},
    art=GPU, line="Buy it for memory, not speed.", accent="var(--orange)", tape="the only reason")

win("list", "Three caveats. These are single-request measurements, not a batch server. Riser quality varies and can cost more than the card. And dual-card drivers are not all equal.",
    {"k": "Three caveats", "a": "single-request", "b": "Riser quality", "c": "drivers"},
    art=RISER, rows=[("01", "single request only", "hot"), ("02", "riser quality varies", "hot"),
                     ("03", "drivers differ", "hot")],
    kicker="read these")

win("stat", "Full tables in the description. Next episode is the one that sounds like it solves everything: unified memory, where the processor and the memory share one pool.",
    {"a": "Full tables", "b": "unified memory", "c": "one pool"},
    art=GPU, big=[("NEXT", "", "var(--lime)")], labels=["unified memory"], tape="byte forensics")
