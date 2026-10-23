"""Extends the five episode specs to full length (7+ minutes each).

Inserts extra scenes before the closing scene. All figures still come from the
two Hardware Corner benchmark articles.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, "data", "specs")

EXTRA = {}

# ─────────────────────────────────────────────────────────── EP03
EXTRA["byte-03"] = [
 {"type": "rows", "head": "the mistake everyone makes",
  "vo": "The mistake is comparing model file sizes and calling it a memory comparison. Sixteen point six eight gigabytes against fourteen point seven eight looks like a two gigabyte difference, so people assume the smaller file wins by two gigabytes everywhere. It does not work like that. The file is a constant. The cache is a variable, and the variable is the thing that decides whether you get one twenty-eight K or sixty-four K.",
  "items": [["File size", "constant, known before you load", "good"],
            ["KV cache", "variable, grows with every token", "hot"],
            ["The decision", "made by the variable", "dim"]],
  "cues": {"h": "The mistake is", "0": "the file is a constant", "1": "the cache is a variable", "2": "the variable"}},

 {"type": "bars", "head": "the cache is the whole story",
  "vo": "Watch what happens to the gap as context grows. At four K the two models are two gigabytes apart. At thirty-two K they are four apart. At one twenty-eight K they are eight apart. At two hundred fifty-six K they are fourteen apart. The file difference was two gigabytes. The cache difference becomes fourteen. That is the entire argument, in four numbers.",
  "items": [["gap at 4K", "11", "2 GB", "lime"],
            ["gap at 32K", "24", "4 GB", "cyan"],
            ["gap at 128K", "47", "8 GB", "orange"],
            ["gap at 256K", "82", "14 GB", "red"]],
  "cues": {"h": "Watch what happens", "0": "two gigabytes apart", "1": "four apart",
           "2": "eight apart", "3": "fourteen apart"}},

 {"type": "caveat", "head": "the desktop tax",
  "vo": "One thing the benchmarks never include is your desktop. A twenty-four gigabyte card does not give twenty-four gigabytes to the model. The compositor wants memory, the browser wants memory, and if you are driving two monitors the display engine takes a slice before you load anything. Leave a gigabyte, ideally two, and treat twenty-four as twenty-two.",
  "items": ["Compositor and browser take VRAM", "Two monitors take more",
            "Plan for 22 GB usable, not 24"],
  "tape": "twenty-four is twenty-two",
  "cues": {"h": "One thing the benchmarks", "0": "the compositor", "1": "two monitors", "2": "twenty-two", "t": "twenty-four as twenty-two"}},

 {"type": "rows", "head": "how to check your own card",
  "vo": "You can check this yourself in about five minutes. Load the model at the context you intend to use, then look at the reported VRAM before you type anything. Then keep doubling the context and watch the number climb. When it stops climbing and starts spilling, you have found your ceiling. It is always lower than the box says, and it is always specific to your machine.",
  "items": [["Load at target context", "read VRAM before typing", "good"],
            ["Double the context", "watch the number climb", "good"],
            ["Spilling begins", "that is your real ceiling", "hot"]],
  "cues": {"h": "check this yourself", "0": "Load the model", "1": "keep doubling", "2": "spilling"}},

 {"type": "bars", "head": "what you actually get",
  "vo": "So on a twenty-four gigabyte card, with two gigabytes reserved for the desktop, here is what you actually get. Glimmer holds its full two hundred fifty-six K window at twenty gigabytes. Qwen three point eight holds one twenty-eight K at twenty-six, which does not fit, so realistically sixty-four K. That is the honest table, and it is the one nobody prints on the box.",
  "items": [["Glimmer · 256K", "83", "20 GB", "lime"],
            ["Qwen · 128K", "100", "26 GB", "red"],
            ["Qwen · 64K", "85", "22 GB", "yellow"]],
  "cues": {"h": "here is what you actually get", "0": "twenty gigabytes", "1": "twenty-six",
           "2": "sixty-four K"}},
]

# ─────────────────────────────────────────────────────────── EP04
EXTRA["byte-04"] = [
 {"type": "rows", "head": "what the bus actually costs",
  "vo": "Splitting a model across two cards means every layer boundary becomes a transfer over PCIe. On a consumer board that is sixteen lanes shared with your storage and your chipset. The cards cannot compute a layer until the previous layer has crossed the bus and landed. So you are not running two GPUs, you are running one slow GPU with extra steps.",
  "items": [["Layer boundary", "a PCIe transfer", "hot"],
            ["16 lanes", "shared with storage", "hot"],
            ["Result", "one slow GPU with extra steps", "hot"]],
  "cues": {"h": "Splitting a model", "0": "every layer boundary", "1": "sixteen lanes", "2": "extra steps"}},

 {"type": "bars", "head": "the gap widens with context",
  "vo": "The gap is not constant, it widens. At four K the two-card setup is at twenty-two point four seven and the three thousand ninety is at forty-five point three. That is roughly double. At one twenty-eight K the two-card setup is at fifteen point five five and the single card is at thirty-eight point one three. That is nearly two and a half times. The longer the context, the worse the split gets.",
  "items": [["2 cards · 4K", "50", "22.47", "orange"],
            ["1 card · 4K", "100", "45.30", "lime"],
            ["2 cards · 128K", "41", "15.55", "red"],
            ["1 card · 128K", "84", "38.13", "lime"]],
  "cues": {"h": "The gap is not constant", "0": "twenty-two point four seven",
           "1": "forty-five point three", "2": "fifteen point five five", "3": "thirty-eight point one three"}},

 {"type": "rows", "head": "the costs nobody budgets",
  "vo": "Then there are the costs that never appear in a token per second table. Two cards need two sets of power cables, two slots of cooling, and a motherboard with enough lanes to feed both. Your case airflow has to handle double the heat in half the space. And when one card is idle during a split workload, you are paying for silicon that is doing nothing.",
  "items": [["Power", "two sets of cables", "hot"],
            ["Cooling", "double the heat, same case", "hot"],
            ["Idle half", "paying for unused silicon", "hot"]],
  "cues": {"h": "the costs that never appear", "0": "two sets of power", "1": "double the heat", "2": "idle"}},

 {"type": "bars", "head": "prefill tells the same story",
  "vo": "Prefill agrees. The two-card setup processes a four K prompt at eleven hundred and sixty-seven tokens a second. The three thousand ninety does fourteen hundred and seventy-six. At one twenty-eight K the two-card setup is at five hundred and twelve, and the single card running Glimmer is at five hundred and eighty-four at two hundred fifty-six K, with four times the context. It is not close in either direction.",
  "items": [["2 cards · 4K prefill", "79", "1,167", "orange"],
            ["1 card · 4K prefill", "100", "1,477", "lime"],
            ["2 cards · 128K prefill", "35", "513", "red"],
            ["1 card · 256K prefill", "40", "584", "lime"]],
  "cues": {"h": "Prefill agrees", "0": "eleven hundred and sixty-seven", "1": "fourteen hundred and seventy-six",
           "2": "five hundred and twelve", "3": "five hundred and eighty-four"}},

 {"type": "caveat", "head": "when the two-card route wins",
  "vo": "Two honest cases where two cards win. If you already own one, the second card is the cheapest capacity you will ever buy, and thirty-two gigabytes genuinely reaches one twenty-eight K on Qwen three point eight. And if your workload is throughput across many small requests rather than one long context, splitting can pay off, because each card can serve independently. This benchmark tested one long request, not a queue.",
  "items": ["You already own one card", "Many small requests, not one long one"],
  "tape": "it depends on the workload",
  "cues": {"h": "Two honest cases", "0": "already own one", "1": "many small requests", "t": "depends on the workload"}},
]

# ─────────────────────────────────────────────────────────── EP05
EXTRA["byte-05"] = [
 {"type": "bars", "head": "m5 max prefill",
  "vo": "Prefill on the M5 Max tells the same story. Eight hundred and thirty-four tokens a second at a short prompt, falling to four hundred and twenty-four at longer context. On the three thousand ninety, Glimmer does fourteen hundred and seventy-six and still holds five hundred and eighty-four at two hundred fifty-six K. The unified machine is not slow because it is badly built. It is slow because it is feeding a very wide model from memory that is not a graphics card.",
  "items": [["M5 Max · short", "56", "834", "orange"],
            ["3090 · short", "100", "1,477", "lime"],
            ["M5 Max · long", "29", "425", "red"],
            ["3090 · 256K", "40", "584", "lime"]],
  "cues": {"h": "Prefill on the M5 Max", "0": "eight hundred and thirty-four", "1": "fourteen hundred and seventy-six",
           "2": "four hundred and twenty-four", "3": "five hundred and eighty-four"}},

 {"type": "bars", "head": "gb10 prefill",
  "vo": "The GB10 is lower again. Eight hundred and twelve tokens a second at four K, falling to two hundred and twenty-eight at two hundred fifty-six K. That is a machine that will hold the context and then take minutes to read it. For an agent that re-reads a large codebase on every step, that is the difference between usable and unusable.",
  "items": [["GB10 · 4K", "100", "813", "orange"],
            ["GB10 · 64K", "52", "426", "orange"],
            ["GB10 · 256K", "28", "228", "red"]],
  "cues": {"h": "The GB10 is lower", "0": "eight hundred and twelve", "1": "two hundred and twenty-eight", "2": "two hundred and twenty-eight at two hundred"}},

 {"type": "rows", "head": "what unified memory is genuinely for",
  "vo": "So be fair to it. Unified memory is the only way to hold a model that does not fit on any consumer card, and it does that at a fraction of the power and noise of a four card rig. It is also the only option on a laptop, where a discrete card with that much memory does not exist. The mistake is buying it for speed, because speed is the one thing it does not sell.",
  "items": [["Holds models nothing else can", "genuine win", "good"],
            ["Quiet, low power", "genuine win", "good"],
            ["Speed", "not what you are buying", "hot"]],
  "cues": {"h": "So be fair to it", "0": "the only way", "1": "quiet", "2": "not what you are buying"}},

 {"type": "table", "head": "the full comparison",
  "vo": "Here is everything in one place. At four K, the three thousand ninety does forty-five point three, the M5 Max does thirty-one point four, the GB10 does twelve point two, and the two-card setup does twenty-two point four seven. At sixty-four K it is thirty-four, eighteen, eight, and eighteen point five. Sort by memory and you get one order. Sort by speed and you get the exact opposite.",
  "items": [["3090 · 4K", "45.3", "45.3", "good"],
            ["M5 Max · 4K", "31.4", "31.4", "hot"],
            ["2x 5060 Ti · 4K", "22.5", "22.5", "hot"],
            ["GB10 · 4K", "12.2", "12.2", "hot"]],
  "cues": {"h": "everything in one place", "0": "forty-five point three", "1": "thirty-one point four",
           "2": "twenty-two point four seven", "3": "twelve point two"}},

 {"type": "caveat", "head": "the honest limits of this test",
  "vo": "Two limits. These are dense models, and a mixture of experts model activates a fraction of its parameters per token, so the bandwidth penalty shrinks and unified memory looks much better. And this is one benchmark on one software build. Treat the ratio as a shape, not a law, and measure your own model before you spend four figures on a machine.",
  "items": ["Dense models only: MoE behaves differently", "One build, one benchmark: shape, not law"],
  "tape": "shape, not law",
  "cues": {"h": "Two limits", "0": "dense models", "1": "one benchmark", "t": "shape, not law"}},
]

# ─────────────────────────────────────────────────────────── EP06
EXTRA["byte-06"] = [
 {"type": "bars", "head": "prefill at short context is fine",
  "vo": "At short context the two generations are indistinguishable. Prefill at four K is thirty-eight hundred and seventy-three for three point six against thirty-seven hundred and forty-nine for three point eight. That is a three percent difference, well inside noise. So the regression is not that three point eight is a slower model. It is that three point eight is a slower model specifically when the context gets long.",
  "items": [["3.6 · prefill 4K", "100", "3,874", "lime"],
            ["3.8 · prefill 4K", "97", "3,750", "dim"]],
  "cues": {"h": "At short context", "0": "thirty-eight hundred and seventy-three", "1": "thirty-seven hundred and forty-nine"}},

 {"type": "bars", "head": "the regression has a shape",
  "vo": "Follow the shape. At four K the gap is one percent. At sixty-four K it is two point four times. At one twenty-eight K it is two point four times again. So whatever changed between the versions costs you almost nothing on short prompts and a great deal on long ones. That is the signature of an attention or cache change, not a general slowdown.",
  "items": [["4K · 3.6 vs 3.8", "99", "~1%", "dim"],
            ["64K · 3.6 vs 3.8", "41", "2.4x", "red"],
            ["128K · 3.6 vs 3.8", "42", "2.4x", "red"]],
  "cues": {"h": "Follow the shape", "0": "one percent", "1": "two point four times", "2": "two point four times again"}},

 {"type": "rows", "head": "why this matters more than it looks",
  "vo": "This matters because the entire pitch of long context is that you can hand a model a large codebase or a long document. If the newer model is two point four times slower exactly in that regime, then the feature you paid for is the feature that got worse. Benchmarks that only test short prompts would never catch it, which is why almost nobody noticed.",
  "items": [["Long context is the selling point", "the regime that regressed", "hot"],
            ["Short prompt benchmarks", "would never catch it", "hot"],
            ["Nobody noticed", "because nobody measured", "dim"]],
  "cues": {"h": "This matters because", "0": "large codebase", "1": "short prompts", "2": "nobody noticed"}},

 {"type": "rows", "head": "how to check before you switch",
  "vo": "Before you switch models, do this. Run both at the context length you actually use, with the same quantization, on the same machine. Time the first token and the tokens per second after it. Ten minutes of work tells you more than any leaderboard, because leaderboards almost never publish tokens per second at long context on consumer hardware.",
  "items": [["Same context", "the length you actually use", "good"],
            ["Same quantization", "otherwise the ratio is meaningless", "good"],
            ["Time first token", "and tokens per second", "good"]],
  "cues": {"h": "Before you switch", "0": "the context length", "1": "same quantization", "2": "first token"}},

 {"type": "caveat", "head": "the other side of the ledger",
  "vo": "And be fair to three point eight. It may be better at reasoning, at code, at following instructions, and none of that is measured here. A model that is two point four times slower and noticeably smarter can still be the right purchase. Speed is a cost, not a verdict. The point is that you should know the cost before you pay it, not after.",
  "items": ["Quality is not measured here", "Faster is not automatically better"],
  "tape": "speed is a cost",
  "cues": {"h": "be fair to three point eight", "0": "reasoning", "1": "not a verdict", "t": "speed is a cost"}},
]

# ─────────────────────────────────────────────────────────── EP07
EXTRA["byte-07"] = [
 {"type": "bars", "head": "rtx 3090 prefill",
  "vo": "On a three thousand ninety the numbers are lower but the shape is identical. Glimmer prefills a four K prompt at fourteen hundred and seventy-seven tokens a second. Sixty-four K is eleven hundred. One twenty-eight K is eight hundred and fifty-three. Two hundred fifty-six K is five hundred and eighty-four. Even the old card degrades gracefully on the better optimised model.",
  "items": [["Glimmer · 4K", "100", "1,477", "lime"],
            ["Glimmer · 64K", "74", "1,098", "lime"],
            ["Glimmer · 128K", "58", "853", "yellow"],
            ["Glimmer · 256K", "40", "584", "orange"]],
  "cues": {"h": "On a three thousand ninety", "0": "fourteen hundred and seventy-seven",
           "1": "eleven hundred", "2": "eight hundred and fifty-three", "3": "five hundred and eighty-four"}},

 {"type": "bars", "head": "qwen 3.8 on the same 3090",
  "vo": "Qwen three point eight on the same card starts at thirteen hundred and eight at four K, which is close enough to Glimmer that you would not notice. By sixty-four K it is seven hundred and seventeen, and that is where the two diverge. Same card, same engine, one model holds its prefill and the other halves it.",
  "items": [["Qwen · 4K", "89", "1,308", "cyan"],
            ["Qwen · 64K", "49", "767", "red"]],
  "cues": {"h": "Qwen three point eight on the same card", "0": "thirteen hundred and eight", "1": "seven hundred and seventeen"}},

 {"type": "rows", "head": "prompt caching changes everything",
  "vo": "There is one honest escape hatch. If you send the same long document repeatedly, a cached prompt is nearly free on the second pass, because the prefill work is already done. So the twenty seconds you feel is a first-time cost, not a per-message cost. Agents that re-read the same codebase over and over are exactly the case where caching turns an unusable wait into a normal one.",
  "items": [["First pass", "full prefill cost", "hot"],
            ["Cached prompt", "nearly free", "good"],
            ["Agent loops", "where caching saves you", "good"]],
  "cues": {"h": "one honest escape hatch", "0": "a cached prompt", "1": "nearly free", "2": "Agent loops"}},

 {"type": "table", "head": "time to first token at 100k",
  "vo": "Put the three machines side by side at a hundred thousand token prompt. Twenty-two seconds on a five-oh-ninety running Glimmer. Fifty-four seconds on a three thousand ninety. Two hundred and seventeen seconds on the same five-oh-ninety running Qwen three point eight. Same document, same question, a wait that ranges from tolerable to abandoned.",
  "items": [["5090 · Glimmer", "22 s", "22 s", "good"],
            ["3090 · Glimmer", "54 s", "54 s", "hot"],
            ["5090 · Qwen 3.8", "217 s", "217 s", "hot"]],
  "cues": {"h": "side by side", "0": "twenty-two seconds", "1": "fifty-four seconds", "2": "two hundred and seventeen seconds"}},

 {"type": "rows", "head": "how to measure it yourself",
  "vo": "Measurement is easy and almost nobody does it. Send the longest prompt you realistically use, and time from pressing enter to the first character appearing. That single number predicts whether the tool feels fast, better than any tokens per second figure on a leaderboard. Write it down for two machines and the purchase decision makes itself.",
  "items": [["Paste your real longest prompt", "not a benchmark prompt", "good"],
            ["Time to first character", "the number you feel", "good"],
            ["Do it on both machines", "then decide", "good"]],
  "cues": {"h": "Measurement is easy", "0": "the longest prompt", "1": "first character", "2": "both machines"}},
]

for key, extra in EXTRA.items():
    path = os.path.join(SPECS, key + ".json")
    ep = json.load(open(path, encoding="utf-8"))
    scenes = ep["scenes"]
    close = scenes.pop()                      # keep the closing scene last
    scenes.extend(extra)
    scenes.append(close)
    ep["scenes"] = scenes
    json.dump(ep, open(path, "w", encoding="utf-8"), indent=1)
    words = sum(len(s["vo"].split()) for s in scenes)
    print(f"{key.upper()}: {len(scenes)} scenes, {words} words (~{words/175:.1f} min)")
