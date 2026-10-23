from art_lib import (GPU, CHIP, LAPTOP, RAM, SLOT, CACHE, DIE, HEATSINK, TWODIE, PCB,
                     QUANT, TOWER, SYSRAM, PCIELINK, DUALBOARD, PSU, RISER, MINIPC,
                     LAPCUT, SODIMM)

NAME = "BYTE-05-A"
W = []

def win(layout, vo, cues, **data):
    W.append(dict(layout=layout, vo=vo, cues=cues, **data))

win("stat", "One hundred and twenty-eight gigabytes of memory, no graphics card, and a model that fits entirely. Unified memory sounds like the answer to every problem in this series.",
    {"a": "One hundred and twenty-eight", "b": "no graphics card", "t": "every problem"},
    art=LAPCUT, big=[("128", "GB", "var(--cyan)"), ("0", "cards", "var(--dim)")],
    labels=["shared pool", "discrete GPU"], tape="the unified promise")

win("callout", "Start with the package. A small box, one fan, and memory soldered beside the processor. There is no slot, no card, and nothing to upgrade later.",
    {"k": "the package", "a": "memory soldered", "b": "nothing to upgrade"},
    art=MINIPC, marks=[("the fan", "lt"), ("the board", "rt"), ("soldered memory", "lb")])

win("callout", "Inside a laptop it is even clearer. The processor and the memory sit on the same board, sharing one pool. Nothing has to cross a slot to reach the model.",
    {"k": "Inside a laptop", "a": "sharing one pool", "b": "cross a slot"},
    art=LAPCUT, marks=[("the cpu", "lt"), ("shared memory", "rt"), ("the hinge", "lb")])

win("callout", "The memory itself looks like laptop memory. Small modules, soldered down, and a fixed quantity you choose once at purchase.",
    {"k": "laptop memory", "a": "Small modules", "b": "choose once"},
    art=SODIMM, marks=[("one module", "lt"), ("soldered", "rt"), ("fixed at purchase", "lb")])

win("quote", "And that is the trade. You get capacity no consumer card can match, and you give up the ability to change any of it afterwards.",
    {"a": "the trade", "b": "change any of it", "t": "capacity"},
    art=LAPCUT, line="Capacity now, forever.", accent="var(--cyan)", tape="soldered means final")

win("table", "Three machines, the same model, the same four K context. A three thousand ninety at forty-five tokens. An M5 Max at thirty-one. A small unified box at twelve.",
    {"k": "Three machines", "r0": "three thousand ninety", "r1": "M5 Max", "r2": "unified box"},
    art=LAPTOP, rows=[("3090", "45.3", "24 GB", "good"), ("M5 Max", "31.4", "128 GB", "hot"),
                      ("GB10", "12.2", "128 GB", "hot")],
    kicker="same model, same 4k")

win("chart", "Put those numbers on one axis and the pattern is obvious. The card with the least memory is the fastest, and the box with the most memory is the slowest.",
    {"k": "one axis", "a": "least memory is the fastest", "b": "most memory is the slowest"},
    art=CHIP, bars=[("3090", "45.3", 100, "var(--lime)"), ("M5 Max", "31.4", 69, "var(--yellow)"),
                    ("GB10", "12.2", 27, "var(--red)")],
    kicker="tokens per second", note="measured, 4K context")

win("stat", "Three point seven times slower than the card. That is the honest size of the gap, and it does not disappear when the model gets bigger.",
    {"a": "Three point seven times", "b": "does not disappear", "t": "the gap"},
    art=CHIP, big=[("45.3", "t/s", "var(--lime)"), ("12.2", "t/s", "var(--red)")],
    labels=["RTX 3090", "GB10"], tape="3.7x")

win("quote", "Unified memory is not free. You are paying for capacity with bandwidth, and the exchange rate is roughly three to four times.",
    {"a": "not free", "b": "three to four times", "t": "capacity with bandwidth"},
    art=CHIP, line="You pay for capacity in speed.", accent="var(--yellow)", tape="3-4x slower")

win("list", "Three things unified memory genuinely wins. A model that would never fit on a card. A machine that fits in a bag. And a power draw a laptop charger can cover.",
    {"k": "Three things", "a": "A model that would never fit", "b": "fits in a bag", "c": "power draw"},
    art=MINIPC, rows=[("01", "models no card can hold", "good"), ("02", "portable", "good"),
                      ("03", "low power", "good")],
    kicker="what it wins")

win("list", "And three it loses. Throughput, upgradeability, and the ability to run two of them cheaply when you need more speed rather than more memory.",
    {"k": "And three it loses", "a": "Throughput", "b": "upgradeability", "c": "two of them"},
    art=SODIMM, rows=[("01", "throughput", "hot"), ("02", "no upgrades", "hot"),
                      ("03", "scaling is expensive", "hot")],
    kicker="what it loses")

win("stat", "The numbers again, from the table. Forty-five tokens on the card at four K. Thirty-one on the M5 Max. Twelve on the small box. Capacity and speed pull in opposite directions.",
    {"a": "Forty-five tokens", "b": "Thirty-one", "c": "Twelve"},
    art=LAPTOP, big=[("45.3", "", "var(--lime)"), ("12.2", "", "var(--red)")],
    labels=["card", "unified box"], tape="capacity vs speed")

win("quote", "So the question is not which is better. It is which one you are short of: memory, or time.",
    {"a": "not which is better", "b": "memory, or time", "t": "short of"},
    art=CHIP, line="Memory, or time.", accent="var(--cyan)", tape="pick your shortage")

win("table", "The decision table. If the model fits on a card, buy the card. If it does not, buy the memory and accept the speed. There is no row where you get both.",
    {"k": "The decision table", "r0": "fits on a card", "r1": "does not"},
    art=RAM, rows=[("Fits on a card", "buy the card", "fast", "good"),
                   ("Does not fit", "buy memory", "slow", "hot")],
    kicker="the whole decision")

win("callout", "And remember what the box is. One fan, one board, soldered memory. When it is too slow in two years, you replace the entire machine, not one part of it.",
    {"k": "what the box is", "a": "soldered memory", "b": "replace the entire machine"},
    art=MINIPC, marks=[("one fan", "lt"), ("one board", "rt"), ("no upgrades", "lb")])

win("quote", "That is the real cost of unified memory. Not the purchase price, the replacement price, because nothing inside it can be improved.",
    {"a": "the replacement price", "b": "nothing inside it", "t": "real cost"},
    art=SODIMM, line="Nothing inside it can be upgraded.", accent="var(--red)", tape="the real cost")

win("list", "Three caveats. These are one build on three very different machines. Memory bandwidth figures are not directly comparable. And a larger model changes the ranking entirely.",
    {"k": "Three caveats", "a": "one build", "b": "not directly comparable", "c": "larger model"},
    art=CHIP, rows=[("01", "one build, three machines", "hot"), ("02", "bandwidth not compared", "hot"),
                    ("03", "bigger models reorder this", "hot")],
    kicker="read these")

win("stat", "So unified memory is a capacity answer, not a speed answer. If your model does not fit, it is the only door. If it does fit, it is the slow door.",
    {"a": "capacity answer", "b": "the slow door", "t": "does not fit"},
    art=MINIPC, big=[("128", "GB", "var(--cyan)"), ("12.2", "t/s", "var(--red)")],
    labels=["capacity", "throughput"], tape="one door, one cost")

win("quote", "Full tables in the description. Next episode is a strange one: a newer model that runs slower than the one it replaced, on the same card and the same window.",
    {"a": "Full tables", "b": "a newer model", "c": "the same window"},
    art=CHIP, line="Newer, and slower.", accent="var(--yellow)", tape="next: the regression")
