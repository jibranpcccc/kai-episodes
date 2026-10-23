from art_lib import (GPU, CHIP, LAPTOP, RAM, SLOT, CACHE, DIE, HEATSINK, TWODIE, PCB,
                     QUANT, TOWER, SYSRAM, PCIELINK, DUALBOARD, PSU, RISER, MINIPC,
                     LAPCUT, SODIMM, TWOGEN, GAUGE, WAFER)

NAME = "BYTE-06-A"
W = []

def win(layout, vo, cues, **data):
    W.append(dict(layout=layout, vo=vo, cues=cues, **data))

win("stat", "A newer model that runs slower than the one it replaced. Same card, same window, same quantization. This is the episode where the newer number is not the better number.",
    {"a": "runs slower", "b": "same window", "t": "not the better number"},
    art=TWOGEN, big=[("3.8", "", "var(--red)"), ("3.6", "", "var(--lime)")],
    labels=["the newer one", "the older one"], tape="newer is not faster")

win("callout", "Two chips, two generations. The die on the right is newer, and the benchmark says it processes fewer tokens per second at the context people actually use.",
    {"k": "Two chips", "a": "The die on the right", "b": "fewer tokens"},
    art=WAFER, marks=[("the wafer", "lt"), ("die grid", "rt"), ("one die", "lb")])

win("table", "The numbers, straight from the table. At four K, the older model does fifty-two tokens and the newer does forty. Close enough that you might not notice.",
    {"k": "The numbers", "r0": "At four K", "r1": "fifty-two tokens"},
    art=CHIP, rows=[("3.6 · 4K", "52.2", "older", "good"), ("3.8 · 4K", "40.3", "newer", "hot")],
    kicker="tokens per second, 3090")

win("quote", "Now watch the gap open as the context grows. At four K it is twenty-three percent. At sixty-four K it is more than double.",
    {"a": "watch the gap", "b": "more than double", "t": "twenty-three percent"},
    art=GAUGE, line="The gap grows with the window.", accent="var(--red)", tape="4K: 23% · 64K: 2.4x")

win("chart", "Sixty-four K on the same card. The older model does sixty-three tokens a second. The newer one does twenty-six. For a long conversation the older model is the faster model.",
    {"k": "Sixty-four K", "a": "sixty-three tokens", "b": "twenty-six", "c": "the faster model"},
    art=TWOGEN, bars=[("3.6 · 64K", "63.7", 100, "var(--lime)"), ("3.8 · 64K", "26.2", 41, "var(--red)")],
    kicker="tokens per second", note="measured")

win("stat", "Two point four times slower at the window this channel keeps telling you to use. That is not a rounding error, and it is not a different quantization.",
    {"a": "Two point four times", "b": "not a rounding error", "t": "this channel keeps telling you"},
    art=GAUGE, big=[("63.7", "t/s", "var(--lime)"), ("26.2", "t/s", "var(--red)")],
    labels=["3.6 at 64K", "3.8 at 64K"], tape="2.4x")

win("quote", "So the question is what the newer model bought with that speed. Usually it is quality, or a capability that did not exist before. It is never free.",
    {"a": "what the newer model bought", "b": "never free", "t": "that speed"},
    art=WAFER, line="Something was bought with it.", accent="var(--yellow)", tape="every speedup is paid for")

win("list", "Three things a newer model can spend speed on. Better answers at the same context. New abilities like tool use. Or a longer window that the older one cannot reach.",
    {"k": "Three things", "a": "Better answers", "b": "New abilities", "c": "a longer window"},
    art=CHIP, rows=[("01", "better answers", "good"), ("02", "new abilities", "good"),
                    ("03", "longer window", "good")],
    kicker="what you might be buying")

win("callout", "And this is where the clock matters. A model that is twice as slow halves how much you can do in an hour, which is a cost you feel every day rather than once at purchase.",
    {"k": "the clock matters", "a": "twice as slow", "b": "every day"},
    art=GAUGE, marks=[("the scale", "lt"), ("the needle", "rt"), ("tokens per second", "lb")])

win("quote", "A benchmark table hides that. A stopwatch does not. Time per useful answer is the number that decides whether you keep using a model.",
    {"a": "A benchmark table hides", "b": "A stopwatch", "t": "keep using"},
    art=GPU, line="Time per answer is the real score.", accent="var(--lime)", tape="stopwatch, not table")

win("table", "Here is the same comparison as time per answer. A five hundred token answer takes roughly eight seconds on the older model and twenty on the newer, at sixty-four K.",
    {"k": "time per answer", "r0": "eight seconds", "r1": "twenty"},
    art=GAUGE, rows=[("3.6 · 64K", "8 s", "500 tokens", "good"), ("3.8 · 64K", "19 s", "500 tokens", "hot")],
    kicker="seconds per 500 tokens")

win("quote", "That is the trade in one line. You did not get a slower model by accident. You got a model that spends its budget somewhere other than tokens per second.",
    {"a": "not by accident", "b": "somewhere other", "t": "one line"},
    art=TWOGEN, line="Spent elsewhere, not lost.", accent="var(--yellow)", tape="the budget moved")

win("list", "Three ways to decide for yourself. Run both at the context you actually use. Measure time to a useful answer, not tokens. And check whether the new abilities matter to your work.",
    {"k": "decide for yourself", "a": "Run both", "b": "time to a useful answer", "c": "new abilities"},
    art=SYSRAM, rows=[("01", "test your real context", "good"), ("02", "time a useful answer", "good"),
                       ("03", "do the new abilities matter", "good")],
    kicker="the three tests")

win("stat", "And the number that keeps this honest. Sixty-three against twenty-six. If your work is long conversations, the older model is the one that respects your time.",
    {"a": "Sixty-three against twenty-six", "b": "respects your time", "t": "long conversations"},
    art=DIE, big=[("63.7", "", "var(--lime)"), ("26.2", "", "var(--red)")],
    labels=["older", "newer"], tape="at 64K")

win("quote", "None of this means the newer model is bad. It means the newer model is not automatically the faster one, and the table will not tell you that for free.",
    {"a": "not automatically the faster", "b": "not tell you", "t": "not bad"},
    art=CHIP, line="Newer is a version, not a speed.", accent="var(--cyan)", tape="read the table carefully")

win("table", "The full comparison, both contexts. Four K and sixty-four K, older and newer. Two rows where the newer model is slower, and one where it is dramatically slower.",
    {"k": "The full comparison", "r0": "Four K", "r1": "sixty-four K"},
    art=PCB, rows=[("3.6 · 4K", "52.2", "faster", "good"), ("3.8 · 4K", "40.3", "slower", "hot"),
                      ("3.6 · 64K", "63.7", "faster", "good"), ("3.8 · 64K", "26.2", "much slower", "hot")],
    kicker="all four rows")

win("callout", "And the wafer is why this keeps happening. Two generations made on different processes, different cache sizes, different priorities. The model number hides all of it.",
    {"k": "the wafer", "a": "different processes", "b": "The model number hides"},
    art=WAFER, marks=[("one wafer", "lt"), ("many dies", "rt"), ("yield varies", "lb")])

win("stat", "So read the table twice. Once for the number in the name, and once for the number in the row that matches your context.",
    {"a": "read the table twice", "b": "your context", "t": "the number in the name"},
    art=TOWER, big=[("2", "rows", "var(--yellow)"), ("1", "context", "var(--lime)")],
    labels=["read both", "yours"], tape="context decides")

win("list", "Three caveats. These are single-card measurements from one build. The quantization recipe differs between generations. And quality was not measured here at all.",
    {"k": "Three caveats", "a": "single-card", "b": "recipe differs", "c": "quality was not measured"},
    art=CHIP, rows=[("01", "single card, one build", "hot"), ("02", "recipes differ", "hot"),
                    ("03", "quality not measured", "hot")],
    kicker="read these")

win("quote", "That is the whole lesson. A newer model is a trade, and the trade is only visible if you measure at the context you actually use.",
    {"a": "a trade", "b": "at the context you actually use", "t": "the whole lesson"},
    art=TWOGEN, line="Measure at your context.", accent="var(--lime)", tape="the lesson")

win("stat", "Full tables in the description. That is seven episodes of measurements. If this series saved you a bad purchase, the next one starts with the card you already own.",
    {"a": "Full tables", "b": "a bad purchase", "c": "the card you already own"},
    art=GPU, big=[("7", "", "var(--lime)"), ("END", "", "var(--dim)")],
    labels=["episodes", "of measurements"], tape="byte forensics")
