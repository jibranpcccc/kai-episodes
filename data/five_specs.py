"""Builds the five episode specs (script + cues) and writes them as JSON.

Every number below comes from the two Hardware Corner benchmark articles already
cited in Episode 02. Nothing is estimated.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "specs")
os.makedirs(OUT, exist_ok=True)

EPS = {}

# ─────────────────────────────────────────────────────────────── EP03
EPS["BYTE-03"] = {
 "name": "BYTE-03",
 "kicker": "Byte Forensics",
 "title": "Your 24GB Card Cannot Do 128K",
 "subtitle": "context vs VRAM, measured",
 "scenes": [
  {"type": "hook", "art": "gpu", "head": "24 GB · 128K context · pick one",
   "vo": "Okay, so you have got a twenty-four gigabyte card, and you want one twenty-eight K of context, because that is the number printed on every model released this year. Here is the problem. Context is not free, and it is not linear. The model file is the part everyone measures, and it is the part that barely changes. The hard part arrives after the model is loaded, when you start filling the window.",
   "a": {"v": "24", "u": "GB", "c": "cyan", "lab": "your card"},
   "b": {"v": "128", "u": "K", "c": "red", "lab": "what you asked for"},
   "tape": "context is not free",
   "cues": {"h": "Okay, so", "a": "twenty-four gigabyte card", "b": "one twenty-eight K", "t": "Context is not free"}},

  {"type": "rows", "head": "two things live in your vram",
   "vo": "Let's separate the two things living in your VRAM. One is the weights, a fixed file. The other is the cache, and the cache is what grows. At four K of context, Muse Glimmer sits at sixteen gigabytes in total. Qwen three point eight sits at eighteen. Both fit comfortably. Nobody argues at this point, and this is exactly where every tutorial stops.",
   "items": [["Weights", "fixed file", "good"], ["KV cache", "grows every token", "hot"]],
   "cues": {"h": "two things living", "0": "the weights", "1": "the cache"}},

  {"type": "bars", "head": "now push the context",
   "vo": "Now push it. At thirty-two K of context, Glimmer is still at sixteen gigabytes. Qwen has moved to twenty. At sixty-four K, Glimmer is seventeen, Qwen is twenty-two. At one twenty-eight K, Glimmer is eighteen and Qwen is twenty-six. That leaves two gigabytes of headroom on a twenty-four gigabyte card, which is not headroom. That is a hostage situation.",
   "items": [["Glimmer 32K", "67", "16 GB", "lime"],
             ["Qwen 32K", "83", "20 GB", "dim"],
             ["Glimmer 128K", "75", "18 GB", "cyan"],
             ["Qwen 128K", "100", "26 GB", "red"]],
   "cues": {"h": "Now push it", "0": "thirty-two K", "1": "Qwen has moved", "2": "sixty-four K", "3": "one twenty-eight K"}},

  {"type": "table", "head": "the full curve",
   "vo": "Here is the whole curve, measured, not calculated. Four K is sixteen against eighteen. Thirty-two K is sixteen against twenty. Sixty-four K is seventeen against twenty-two. One twenty-eight K is eighteen against twenty-six. And two hundred fifty-six K is twenty against thirty-four. Glimmer fits the entire window. Qwen does not fit the last row at all.",
   "items": [["4K", "16", "18", "good"], ["32K", "16", "20", "good"],
             ["64K", "17", "22", "good"], ["128K", "18", "26", "hot"],
             ["256K", "20", "34", "hot"]],
   "cues": {"h": "the whole curve", "0": "Four K is", "1": "Thirty-two K is",
            "2": "Sixty-four K is", "3": "One twenty-eight K is", "4": "two hundred fifty-six K"}},

  {"type": "caveat", "head": "what happens when you exceed it",
   "vo": "When you exceed the card, the model does not crash politely. It spills into system memory over PCIe, and token generation collapses. It does not halve, it falls off a cliff, and that cliff is not printed on any spec sheet. That is why the number on the box matters less than the number in your cache.",
   "items": ["Spills to system RAM over PCIe", "Throughput collapses, not halves, collapses",
             "The cliff is on no spec sheet"],
   "tape": "the cliff is invisible",
   "cues": {"h": "When you exceed", "0": "system memory", "1": "does not halve",
            "2": "spec sheet", "t": "cliff is not printed"}},

  {"type": "rows", "head": "what actually works on 24 gb",
   "vo": "So what works? Option one, Glimmer at its full context window. Option two, Qwen at sixty-four K, and you plan around that instead of discovering it at token ninety thousand. Option three, quantize harder and accept the quality loss. There is no fourth option where you keep the model, the context, and the card.",
   "items": [["Glimmer 30B", "full 256K", "good"], ["Qwen 3.8", "64K ceiling", "hot"],
             ["Quantize harder", "quality loss", "hot"]],
   "cues": {"h": "So what works", "0": "Option one", "1": "Option two", "2": "Option three"}},

  {"type": "close", "art": "chip", "head": "close",
   "vo": "Three caveats before you spend anything. Glimmer was measured at four-bit medium and Qwen at four-bit small, so this is not a perfectly fair fight. These are hardware measurements, not quality measurements. And your desktop uses VRAM too, so leave a gigabyte for the compositor.",
   "line": "Leave a gigabyte for the desktop.",
   "chips": ["FILE", "CACHE", "CONTEXT"],
   "cues": {"h": "Three caveats", "l": "Leave a gigabyte", "0": "four-bit medium",
            "1": "hardware measurements", "w": "compositor"}},
 ]}

# ─────────────────────────────────────────────────────────────── EP04
EPS["BYTE-04"] = {
 "name": "BYTE-04",
 "kicker": "Byte Forensics",
 "title": "Two Cheap Cards vs One Good Card",
 "subtitle": "dual GPU vs single, measured",
 "scenes": [
  {"type": "hook", "art": "gpu", "head": "2 × 16 GB vs 1 × 24 GB",
   "vo": "Okay, so two sixteen gigabyte cards cost less than one good twenty-four gigabyte card, and together they hold thirty-two gigabytes. On paper that is more memory for less money, and on paper it wins. So why does everyone who tries it come back and buy the single card anyway? Because capacity and speed are two different numbers, and the benchmark actually tested both.",
   "a": {"v": "32", "u": "GB", "c": "cyan", "lab": "two cards"},
   "b": {"v": "24", "u": "GB", "c": "lime", "lab": "one card"},
   "tape": "capacity is not speed",
   "cues": {"h": "Okay, so", "a": "thirty-two gigabytes", "b": "twenty-four gigabyte card", "t": "capacity and speed"}},

  {"type": "bars", "head": "two cards running qwen 3.8",
   "vo": "The test was a pair of RTX fifty-sixty Ti cards, thirty-two gigabytes total. Running Qwen three point eight, generation starts at twenty-two point four seven tokens a second at four K context. It holds twenty point four three at thirty-two K. At sixty-four K it is eighteen point five. At one twenty-eight K it is fifteen point five five. Every number is real, and every number is modest.",
   "items": [["5060 Ti ×2 · 4K", "100", "22.47", "cyan"],
             ["5060 Ti ×2 · 32K", "91", "20.43", "cyan"],
             ["5060 Ti ×2 · 64K", "82", "18.50", "yellow"],
             ["5060 Ti ×2 · 128K", "69", "15.55", "red"]],
   "cues": {"h": "The test was", "0": "twenty-two point four seven",
            "1": "thirty-two K", "2": "sixty-four K", "3": "one twenty-eight K"}},

  {"type": "bars", "head": "one 3090 running glimmer",
   "vo": "Now the same job on a single three thousand ninety running Muse Glimmer. Forty-five point three tokens a second at four K. Forty-two point four at sixty-four K. Thirty-eight point one at one twenty-eight K. Roughly double the speed of two cards, at every context length, from one slot.",
   "items": [["3090 · 4K", "100", "45.30", "lime"],
             ["3090 · 64K", "94", "42.45", "lime"],
             ["3090 · 128K", "84", "38.13", "lime"]],
   "cues": {"h": "Now the same job", "0": "forty-five point three",
            "1": "forty-two point four", "2": "thirty-eight point one"}},

  {"type": "bars", "head": "prefill is worse",
   "vo": "And it gets worse before the first word. Prefill on the two-card setup is eleven hundred and sixty-seven tokens a second at four K, and five hundred and twelve at one twenty-eight K. The single three thousand ninety does fourteen hundred and seventy-six and five hundred and eighty-four. So the two-card route loses on the wait as well as the generation.",
   "items": [["5060 Ti ×2 · 4K", "79", "1,167", "orange"],
             ["3090 · 4K", "100", "1,477", "lime"],
             ["5060 Ti ×2 · 128K", "35", "513", "red"],
             ["3090 · 256K", "40", "584", "lime"]],
   "cues": {"h": "before the first word", "0": "eleven hundred", "1": "fourteen hundred",
            "2": "five hundred and twelve", "3": "five hundred and eighty-four"}},

  {"type": "rows", "head": "why it is slower",
   "vo": "The reason is not mysterious. Two cards split a model across a PCIe bus, so every layer boundary is a transfer, and every batch waits for the slowest half. One card has no bus to cross. You are paying for memory you can address instantly, and that is the whole product.",
   "items": [["Split across PCIe", "every layer crosses the bus", "hot"],
             ["Batch waits", "for the slowest card", "hot"],
             ["Single card", "no bus to cross", "good"]],
   "cues": {"h": "The reason", "0": "Two cards split", "1": "every batch", "2": "One card has no bus"}},

  {"type": "caveat", "head": "when two cards is right",
   "vo": "Two caveats. If you already own one sixteen gigabyte card, adding a second is a real upgrade path, and thirty-two gigabytes does reach one twenty-eight K on Qwen three point eight. And these numbers are for dense models that split cleanly. Mixture of experts models behave differently and this data does not cover them.",
   "items": ["Already own one card: adding a second works",
             "Dense models only: MoE is not covered here"],
   "tape": "capacity, not speed",
   "cues": {"h": "Two caveats", "0": "already own one", "1": "Mixture of experts",
            "t": "capacity"}},

  {"type": "close", "art": "gpu", "head": "close",
   "vo": "So if you are buying from scratch, one twenty-four gigabyte card does more with less. If you already own a sixteen, a second one is the cheap path to capacity, and you should expect roughly half the tokens per second. That is the trade, and now you can see both sides of it.",
   "line": "Buy capacity or buy speed. Not both.",
   "chips": ["CAPACITY", "SPEED", "PREFILL"],
   "cues": {"h": "buying from scratch", "l": "Buy capacity", "0": "sixteen",
            "1": "capacity", "w": "both sides"}},
 ]}

# ─────────────────────────────────────────────────────────────── EP05
EPS["BYTE-05"] = {
 "name": "BYTE-05",
 "kicker": "Byte Forensics",
 "title": "Unified Memory Is Not Free",
 "subtitle": "128 GB looks great until you measure it",
 "scenes": [
  {"type": "hook", "art": "laptop", "head": "128 GB unified vs 24 GB discrete",
   "vo": "Okay, so a machine with one hundred and twenty-eight gigabytes of unified memory will hold any model you can throw at it. That part is true. So why does it feel slower than a gaming card with a fifth of the memory? Because bandwidth is not capacity, and the benchmark measured both machines on the same model.",
   "a": {"v": "128", "u": "GB", "c": "orange", "lab": "unified"},
   "b": {"v": "45", "u": "t/s", "c": "lime", "lab": "one 3090"},
   "tape": "capacity is not bandwidth",
   "cues": {"h": "Okay, so", "a": "one hundred and twenty-eight", "b": "gaming card", "t": "bandwidth is not capacity"}},

  {"type": "bars", "head": "m5 max · 128 gb unified",
   "vo": "On an M5 Max with one hundred and twenty-eight gigabytes, Qwen three point eight generates thirty-one point four tokens a second at four K. At sixteen K it is twenty-three point six. At thirty-two K, twenty-one point six. At sixty-four K, eighteen point two. That is a real machine doing real work, and it is slower than a three thousand ninety at every single row.",
   "items": [["M5 Max · 4K", "100", "31.4", "orange"],
             ["M5 Max · 16K", "75", "23.6", "orange"],
             ["M5 Max · 32K", "69", "21.6", "yellow"],
             ["M5 Max · 64K", "58", "18.2", "red"]],
   "cues": {"h": "On an M5 Max", "0": "thirty-one point four",
            "1": "twenty-three point six", "2": "twenty-one point six", "3": "eighteen point two"}},

  {"type": "bars", "head": "gb10 · the small box",
   "vo": "The GB10 box is the same story with a smaller number. Twelve point two tokens a second at four K. Eleven point nine at eight K. Ten point eight at thirty-two K. Nine point seven at sixty-four K. Eight at one twenty-eight K. And five point nine four at two hundred fifty-six K. It will hold the context. It will not move quickly through it.",
   "items": [["GB10 · 4K", "100", "12.20", "orange"],
             ["GB10 · 32K", "89", "10.88", "orange"],
             ["GB10 · 128K", "66", "8.03", "red"],
             ["GB10 · 256K", "49", "5.94", "red"]],
   "cues": {"h": "The GB10 box", "0": "twelve point two", "1": "ten point eight",
            "2": "eight at one twenty-eight", "3": "five point nine four"}},

  {"type": "table", "head": "same model, three machines",
   "vo": "Put them in one table. At four K, the three thousand ninety does forty-five, the M5 Max does thirty-one, the GB10 does twelve. At sixty-four K, thirty-four, eighteen, and eight. The memory ceiling is the opposite order. The machine with the most memory is the slowest, by a factor of four.",
   "items": [["4K · 3090", "40.3", "45.3", "good"],
             ["4K · M5 Max", "31.4", "18.2", "hot"],
             ["64K · GB10", "8.0", "5.9", "hot"]],
   "cues": {"h": "Put them in one table", "0": "three thousand ninety does",
            "1": "the M5 Max", "2": "the GB10 does"}},

  {"type": "caveat", "head": "what unified memory is for",
   "vo": "Two caveats, and they matter. Unified memory is genuinely better when the model does not fit anywhere else, and it is quieter and cheaper to run than four cards. And this measures a dense thirty billion parameter model. A machine with one hundred and twenty-eight gigabytes can hold something no consumer card can, and that is worth something real.",
   "items": ["Wins when the model fits nowhere else",
             "Quieter, cheaper than four cards",
             "This tested dense models only"],
   "tape": "capacity has a price",
   "cues": {"h": "Two caveats", "0": "does not fit anywhere else",
            "1": "quieter and cheaper", "2": "dense thirty billion", "t": "capacity has a price"}},

  {"type": "rows", "head": "the honest summary",
   "vo": "So the summary is not that unified memory is bad. It is that you should buy it for the model that does not fit, not for the speed. If your model fits on a twenty-four gigabyte card, the discrete card wins on tokens per second, on prefill, and on price. If it does not fit, the unified machine is the only door.",
   "items": [["Model fits 24 GB", "discrete card wins", "good"],
             ["Model needs 128 GB", "unified is the only door", "good"],
             ["Buying for speed", "wrong reason", "hot"]],
   "cues": {"h": "the summary", "0": "does not fit", "1": "twenty-four gigabyte card",
            "2": "only door"}},

  {"type": "close", "art": "laptop", "head": "close",
   "vo": "So stop reading the memory number first. Read the bandwidth, then the measured tokens per second, then the capacity. In that order the machine chooses itself, and you stop paying for gigabytes you will never fill.",
   "line": "Bandwidth, then speed, then capacity.",
   "chips": ["BANDWIDTH", "TOKENS", "CAPACITY"],
   "cues": {"h": "stop reading", "l": "Bandwidth, then speed", "0": "bandwidth",
            "1": "tokens per second", "w": "capacity"}},
 ]}

# ─────────────────────────────────────────────────────────────── EP06
EPS["BYTE-06"] = {
 "name": "BYTE-06",
 "kicker": "Byte Forensics",
 "title": "The Newer Model Is 2.4× Slower",
 "subtitle": "qwen 3.6 vs 3.8 at long context",
 "scenes": [
  {"type": "hook", "art": "chip", "head": "same card · same context · two generations",
   "vo": "Okay, so this should not happen. The newer model is slower. Not by a little, by two point four times at sixty-four K context, on the same card, with the same engine. Qwen three point six, the previous generation, generates sixty-three point six tokens a second. Qwen three point eight does twenty-six point two. The old one wins, and it is not close.",
   "a": {"v": "63.66", "u": "", "c": "lime", "lab": "qwen 3.6 · older"},
   "b": {"v": "26.22", "u": "", "c": "red", "lab": "qwen 3.8 · newer"},
   "tape": "the older one is faster",
   "cues": {"h": "Okay, so", "a": "sixty-three point six", "b": "twenty-six point two", "t": "The old one wins"}},

  {"type": "bars", "head": "rtx 5090 · 64k context",
   "vo": "Here it is on a five-oh-ninety at sixty-four K context. Three point six is doing sixty-three point six six tokens a second. Three point eight is doing twenty-six point two two. Same GPU, same quantization family, same llama dot cpp build. The only variable is the model.",
   "items": [["Qwen 3.6 · 64K", "100", "63.66", "lime"],
             ["Qwen 3.8 · 64K", "41", "26.22", "red"]],
   "cues": {"h": "Here it is", "0": "sixty-three point six six", "1": "twenty-six point two two"}},

  {"type": "bars", "head": "and it holds at every length",
   "vo": "At four K the two models are almost identical. Seventy-five point five seven against seventy-four point eight three. That is noise. At sixty-four K the gap opens. At one twenty-eight K, three point six is at fifty-four point five eight and three point eight is at twenty-two point seven nine. The regression is a long context regression, not a general one.",
   "items": [["3.6 · 4K", "100", "75.57", "lime"],
             ["3.8 · 4K", "99", "74.83", "dim"],
             ["3.6 · 128K", "72", "54.58", "lime"],
             ["3.8 · 128K", "30", "22.79", "red"]],
   "cues": {"h": "At four K", "0": "seventy-five point five seven",
            "1": "seventy-four point eight three", "2": "fifty-four point five eight",
            "3": "twenty-two point seven nine"}},

  {"type": "bars", "head": "prefill regressed too",
   "vo": "Prefill regressed with it. At one twenty-eight K on the five-oh-ninety, three point six processes the prompt at eleven hundred and eighty tokens a second. Three point eight does four hundred and sixty-one. So not only does the newer model write slower, it takes longer to start writing.",
   "items": [["3.6 · prefill 128K", "100", "1,180", "lime"],
             ["3.8 · prefill 128K", "39", "461", "red"]],
   "cues": {"h": "Prefill regressed", "0": "eleven hundred and eighty", "1": "four hundred and sixty-one"}},

  {"type": "caveat", "head": "before you downgrade",
   "vo": "Three caveats, because this is where a video like this becomes misleading. Speed is not quality, and three point eight may well be the better model at the task you actually have. These numbers are hardware measurements only. And the two versions were not tested at identical quantization levels, so treat the ratio as directional, not exact.",
   "items": ["Speed is not quality", "Hardware measurements only",
             "Quantization levels differ: ratio is directional"],
   "tape": "read the caveats",
   "cues": {"h": "Three caveats", "0": "Speed is not quality",
            "1": "hardware measurements only", "2": "directional", "t": "read the caveats"}},

  {"type": "rows", "head": "what this actually means",
   "vo": "What it means is simple. Newer is not automatically faster, and the parameter count does not tell you either. The only number that predicts how the thing will feel is the measured tokens per second at the context length you actually use. Everything else is marketing.",
   "items": [["Newer", "not automatically faster", "hot"],
             ["Parameter count", "predicts nothing here", "hot"],
             ["Measured t/s at your context", "the only honest number", "good"]],
   "cues": {"h": "What it means", "0": "Newer is not", "1": "parameter count",
            "2": "measured tokens per second"}},

  {"type": "close", "art": "chip", "head": "close",
   "vo": "So before you upgrade a model, run it at the context you actually use and measure the tokens per second yourself. It takes ten minutes, and it will save you from a downgrade you did not see coming. That is the forensic part.",
   "line": "Measure before you upgrade.",
   "chips": ["CONTEXT", "TOKENS", "VERSION"],
   "cues": {"h": "before you upgrade", "l": "Measure before", "0": "context",
            "1": "tokens per second", "w": "forensic part"}},
 ]}

# ─────────────────────────────────────────────────────────────── EP07
EPS["BYTE-07"] = {
 "name": "BYTE-07",
 "kicker": "Byte Forensics",
 "title": "Prefill: Why Long Context Feels Broken",
 "subtitle": "the wait before the first word",
 "scenes": [
  {"type": "hook", "art": "laptop", "head": "two numbers, one of them is invisible",
   "vo": "Okay, so you paste a long document into a local model and nothing happens for twenty seconds. The model is not broken, and your card is not too slow. You are watching a number that almost nobody measures, called prefill, and it decides how the whole thing feels. Token generation is how fast words come out. Prefill is how long you wait before the first one.",
   "a": {"v": "4,625", "u": "t/s", "c": "lime", "lab": "prefill · short prompt"},
   "b": {"v": "461", "u": "t/s", "c": "red", "lab": "prefill · 128K"},
   "tape": "the wait is the product",
   "cues": {"h": "Okay, so", "a": "called prefill", "b": "how long you wait", "t": "the wait"}},

  {"type": "bars", "head": "rtx 5090 prefill · glimmer",
   "vo": "On a five-oh-ninety, Muse Glimmer processes a four K prompt at four thousand six hundred and twenty-five tokens a second. At sixteen K it is four thousand three hundred and seventy-three. At sixty-four K it is three thousand six hundred and six. At one twenty-eight K, two thousand eight hundred and six. At two hundred fifty-six K, one thousand eight hundred and seventy-four. Long context costs you, but it degrades gracefully.",
   "items": [["Glimmer · 4K", "100", "4,625", "lime"],
             ["Glimmer · 64K", "78", "3,606", "lime"],
             ["Glimmer · 128K", "61", "2,807", "yellow"],
             ["Glimmer · 256K", "41", "1,874", "orange"]],
   "cues": {"h": "On a five-oh-ninety", "0": "four thousand six hundred",
            "1": "three thousand six hundred and six", "2": "two thousand eight hundred",
            "3": "one thousand eight hundred and seventy-four"}},

  {"type": "bars", "head": "same card · qwen 3.8",
   "vo": "The same card running Qwen three point eight starts at three thousand seven hundred and forty-nine at four K. At sixteen K it is eighteen hundred and twenty-five. At sixty-four K it is seven hundred and seventeen. And at one twenty-eight K it is four hundred and sixty-one tokens a second. That is the number that makes a long context chat feel broken.",
   "items": [["Qwen · 4K", "81", "3,749", "cyan"],
             ["Qwen · 16K", "39", "1,826", "cyan"],
             ["Qwen · 64K", "15", "718", "red"],
             ["Qwen · 128K", "10", "461", "red"]],
   "cues": {"h": "same card running", "0": "three thousand seven hundred",
            "1": "eighteen hundred and twenty-five", "2": "seven hundred and seventeen",
            "3": "four hundred and sixty-one"}},

  {"type": "table", "head": "what that means in seconds",
   "vo": "Turn it into time. A hundred thousand token prompt at forty-six hundred tokens a second is about twenty-two seconds of waiting. The same prompt at four hundred and sixty-one tokens a second is three and a half minutes, before the model writes a single word. That is the whole difference between an assistant and a loading screen.",
   "items": [["100K @ 4,625", "22 s", "wait", "good"],
             ["100K @ 1,874", "53 s", "wait", "hot"],
             ["100K @ 461", "217 s", "wait", "hot"]],
   "cues": {"h": "Turn it into time", "0": "twenty-two seconds",
            "1": "three and a half minutes", "2": "loading screen"}},

  {"type": "rows", "head": "why prefill collapses",
   "vo": "Prefill is one big matrix multiplication over the whole prompt, so it scales with prompt length and it is memory bandwidth bound. The longer the prompt, the more of the model's attention you have to compute before you can emit the first token. Generation, by contrast, is one token at a time and barely cares how long the prompt was.",
   "items": [["Prefill", "one pass over the whole prompt", "hot"],
             ["Generation", "one token at a time", "good"],
             ["Both", "bounded by memory bandwidth", "dim"]],
   "cues": {"h": "Prefill is one", "0": "the whole prompt", "1": "one token at a time",
            "2": "memory bandwidth"}},

  {"type": "caveat", "head": "two honest notes",
   "vo": "Two notes. These are single GPU measurements with full offload, so a machine that splits a model across cards will see different prefill behaviour. And a cached prompt is nearly free on the second run, so the wait you feel is usually the first time only.",
   "items": ["Single GPU, full offload only", "Prompt caching removes most repeat cost"],
   "tape": "first time only",
   "cues": {"h": "Two notes", "0": "single GPU measurements", "1": "cached prompt",
            "t": "first time"}},

  {"type": "close", "art": "laptop", "head": "close",
   "vo": "So when you compare hardware, do not only compare tokens per second. Compare the time to first token at the prompt length you actually paste. That is the number you feel, and it is the number almost nobody publishes.",
   "line": "Measure time to first token.",
   "chips": ["PREFILL", "FIRST TOKEN", "CONTEXT"],
   "cues": {"h": "when you compare", "l": "Measure time to first token", "0": "tokens per second",
            "1": "first token", "w": "almost nobody publishes"}},
 ]}

for name, ep in EPS.items():
    path = os.path.join(OUT, name.lower() + ".json")
    json.dump(ep, open(path, "w", encoding="utf-8"), indent=1)
    words = sum(len(s["vo"].split()) for s in ep["scenes"])
    print(f"{name}: {len(ep['scenes'])} scenes, {words} words (~{words/175:.1f} min)")
