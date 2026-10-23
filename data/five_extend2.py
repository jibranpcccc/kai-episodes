"""Third pass: brings each episode to 15 scenes / ~1,250 words (7+ minutes)."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, "data", "specs")

MORE = {}

MORE["byte-03"] = [
 {"type": "bars", "head": "better cards do not fix vram",
  "vo": "Here is the part that surprises people. A five-oh-ninety does not have more VRAM than a three thousand ninety. Both are twenty-four gigabytes. What the five-oh-ninety buys you is speed, eighty-three tokens a second against forty-five, and it buys you nothing at all in capacity. If your problem is that the model does not fit, a faster card with the same memory does not solve it.",
  "items": [["3090 · 24 GB", "100", "45.3", "lime"],
            ["5090 · 24 GB", "100", "83.2", "cyan"]],
  "cues": {"h": "the part that surprises people", "0": "forty-five", "1": "eighty-three"}},

 {"type": "rows", "head": "the capacity is identical",
  "vo": "Read the spec sheets carefully and the two cards are the same size. Twenty-four gigabytes each. The difference is bandwidth, and bandwidth changes how fast you move through the window, not how much window you get. So the question what card do I need for one twenty-eight K has an answer that speed cannot buy: you need a model with a smaller cache, or you need a card with more memory, and there is no third answer.",
  "items": [["24 GB card", "same window, more speed", "good"],
            ["Bigger cache", "window shrinks", "hot"],
            ["No third option", "capacity or nothing", "dim"]],
  "cues": {"h": "Read the spec sheets", "0": "the same size", "1": "bandwidth changes", "2": "no third answer"}},

 {"type": "caveat", "head": "the one real escape",
  "vo": "There is one real escape, and it costs quality. Quantize harder. A four-bit model at sixteen point six eight gigabytes becomes a three-bit or two-bit model that is dramatically smaller, and the cache shrinks with it. You will fit more context on the same card. You will also get a measurably worse model, and the benchmark in front of us does not test how much worse, so do not let anyone tell you it is free.",
  "items": ["Lower quantization fits more context", "Quality cost is real and unmeasured here"],
  "tape": "nothing is free",
  "cues": {"h": "one real escape", "0": "Quantize harder", "1": "quality", "t": "nothing is free"}},
]

MORE["byte-04"] = [
 {"type": "bars", "head": "the 4090 sits in the middle",
  "vo": "There is a middle option people forget. An RTX four-oh-ninety does forty-six point one six tokens a second on Qwen three point eight at four K, against forty point three one on the three thousand ninety. That is a real gain, but it is fifteen percent, not double, and both cards are twenty-four gigabytes. You are buying speed again, not capacity, and you are paying a large premium for fifteen percent.",
  "items": [["3090 · 4K", "87", "40.31", "lime"],
            ["4090 · 4K", "100", "46.16", "cyan"],
            ["5090 · 4K", "100", "74.83", "orange"]],
  "cues": {"h": "a middle option", "0": "forty-six point one six", "1": "forty point three one", "2": "fifteen percent"}},

 {"type": "rows", "head": "if you must split",
  "vo": "If you must split, split a model that splits well. Dense models divide cleanly by layer, so a two-card split works and simply costs you the bus. Mixture of experts models route each token to a subset of experts, which means the split is uneven and the bus cost is unpredictable. If you are determined to run two cards, pick a dense model and accept the throughput you measured, rather than hoping it behaves like one card.",
  "items": [["Dense models", "split cleanly by layer", "good"],
            ["MoE models", "uneven routing, unpredictable cost", "hot"],
            ["Two cards", "always a bus in the middle", "dim"]],
  "cues": {"h": "If you must split", "0": "Dense models", "1": "Mixture of experts", "2": "a bus in the middle"}},

 {"type": "bars", "head": "the summarised comparison",
  "vo": "So here is the whole comparison in four bars. One three thousand ninety running Glimmer: forty-five point three at four K, thirty-eight point one at one twenty-eight K. Two fifty-sixty Ti cards running Qwen: twenty-two point four seven and fifteen point five five. Half the speed, at every length, for more money than one card.",
  "items": [["1 card · 4K", "100", "45.3", "lime"],
            ["2 cards · 4K", "50", "22.5", "orange"],
            ["1 card · 128K", "84", "38.1", "lime"],
            ["2 cards · 128K", "34", "15.6", "red"]],
  "cues": {"h": "the whole comparison", "0": "forty-five point three", "1": "twenty-two point four seven",
           "2": "thirty-eight point one", "3": "fifteen point five five"}},
]

MORE["byte-05"] = [
 {"type": "bars", "head": "a 5090 for scale",
  "vo": "For scale, a five-oh-ninety does eighty-three point two tokens a second on Glimmer at four K, and sixty-eight point nine eight at two hundred fifty-six K. That is not a subtle difference from twelve point seven on the GB10. It is roughly six and a half times faster, on a card that also costs less than the small box. Unified memory is a capacity purchase, and the numbers make that unavoidable.",
  "items": [["5090 · 4K", "100", "83.2", "lime"],
            ["GB10 · 4K", "15", "12.8", "red"],
            ["5090 · 256K", "83", "69.0", "lime"],
            ["GB10 · 256K", "12", "10.3", "red"]],
  "cues": {"h": "For scale", "0": "eighty-three point two", "1": "twelve point seven",
           "2": "sixty-eight point nine eight", "3": "six and a half times"}},

 {"type": "rows", "head": "the laptop case is different",
  "vo": "But the laptop case is genuinely different, and it deserves saying. A laptop with unified memory is the only way to run a large model on battery, quietly, with no external power supply. A three thousand ninety in a laptop does not exist. So if portability is the requirement, unified memory is not a compromise, it is the category. You are not choosing between fast and slow, you are choosing between possible and impossible.",
  "items": [["Desktop", "discrete card wins on speed", "good"],
            ["Laptop", "unified is the only option", "good"],
            ["Portability", "not a compromise, a category", "dim"]],
  "cues": {"h": "the laptop case", "0": "on battery", "1": "does not exist", "2": "the category"}},

 {"type": "caveat", "head": "what to measure before buying",
  "vo": "Before you buy either, measure two things. Tokens per second at the context you actually use, and time to first token at the prompt length you actually paste. Those two numbers describe the entire experience. Everything else on a spec sheet, including the memory figure that started this video, is a proxy that can mislead you in either direction.",
  "items": ["Tokens per second at your context", "Time to first token at your prompt length"],
  "tape": "two numbers, that is it",
  "cues": {"h": "measure two things", "0": "Tokens per second", "1": "time to first token", "t": "two numbers"}},
]

MORE["byte-06"] = [
 {"type": "bars", "head": "the 5090 at every length",
  "vo": "Here is three point eight across the whole range on a five-oh-ninety, so you can see where it stops being fine. Seventy-four point eight three at four K. Fifty-two point two three at sixteen K. Thirty-eight at thirty-two K. Twenty-eight point nine six at sixty-four K. Twenty-six point two two at one twenty-eight K. And twenty-two point seven nine at two hundred fifty-six K. The fall is steep and then it flattens.",
  "items": [["4K", "100", "74.83", "lime"],
            ["16K", "70", "52.23", "cyan"],
            ["32K", "51", "38.02", "yellow"],
            ["64K", "39", "28.96", "orange"],
            ["256K", "30", "22.79", "red"]],
  "cues": {"h": "across the whole range", "0": "seventy-four point eight three",
           "1": "fifty-two point two three", "2": "thirty-eight at thirty-two",
           "3": "twenty-eight point nine six", "4": "twenty-two point seven nine"}},

 {"type": "rows", "head": "how to read a benchmark like this",
  "vo": "Three questions turn a benchmark into something useful. What context length was tested. What quantization was used. And what hardware, because a result on a five-oh-ninety tells you nothing about a three thousand ninety at long context. A table that does not answer all three is decoration. The two articles behind this video answer all three, which is why the numbers are worth quoting at all.",
  "items": [["Context length", "was it short or long", "good"],
            ["Quantization", "same recipe or not", "good"],
            ["Hardware", "which card, exactly", "good"]],
  "cues": {"h": "Three questions", "0": "What context length", "1": "What quantization", "2": "what hardware"}},

 {"type": "bars", "head": "the prefill picture in one chart",
  "vo": "And prefill, same card, same context. Three point six processes a one twenty-eight K prompt at eleven hundred and eighty. Three point eight does four hundred and sixty-one. So the newer model is not just slower to write, it is slower to start, and the start is what you notice first because you are staring at a cursor.",
  "items": [["3.6 · 128K prefill", "100", "1,180", "lime"],
            ["3.8 · 128K prefill", "39", "461", "red"]],
  "cues": {"h": "And prefill", "0": "eleven hundred and eighty", "1": "four hundred and sixty-one"}},
]

MORE["byte-07"] = [
 {"type": "bars", "head": "generation vs prefill on one axis",
  "vo": "Put generation and prefill on the same axis and the point becomes obvious. On a five-oh-ninety with Glimmer at four K, prefill is four thousand six hundred and twenty-five and generation is eighty-three. Prefill is fifty-five times faster because it processes the whole prompt in one pass. But at one twenty-eight K, prefill has fallen to twenty-eight hundred while generation has only fallen to seventy-five. Prefill degrades faster than generation does.",
  "items": [["prefill · 4K", "100", "4,625", "cyan"],
            ["prefill · 128K", "61", "2,807", "cyan"],
            ["generation · 4K", "2", "83", "lime"],
            ["generation · 128K", "2", "76", "lime"]],
  "cues": {"h": "on the same axis", "0": "four thousand six hundred and twenty-five",
           "1": "twenty-eight hundred", "2": "eighty-three", "3": "seventy-five"}},

 {"type": "rows", "head": "why benchmarks hide it",
  "vo": "Benchmarks hide prefill for a boring reason. Tokens per second is one number and it is easy to publish, while time to first token depends on the prompt you personally paste, so it does not fit in a table. The result is that every comparison you have ever read is about the number you feel second, and almost none of them are about the number you feel first.",
  "items": [["Tokens per second", "easy to publish, easy to compare", "good"],
            ["Time to first token", "depends on your prompt, rarely published", "hot"],
            ["So everyone measures", "the wrong half", "dim"]],
  "cues": {"h": "Benchmarks hide prefill", "0": "Tokens per second", "1": "Time to first token", "2": "the wrong half"}},

 {"type": "bars", "head": "what to expect on your own machine",
  "vo": "On a three thousand ninety, expect prefill around fourteen hundred at short prompts, eleven hundred at sixty-four K, and eight hundred and fifty at one twenty-eight K. If you are seeing far below that, you are either spilling out of VRAM or you are not using the offload path you think you are. Those are the two things worth checking before you blame the model.",
  "items": [["3090 · 4K", "100", "1,477", "lime"],
            ["3090 · 64K", "74", "1,098", "yellow"],
            ["3090 · 128K", "58", "853", "orange"]],
  "cues": {"h": "On a three thousand ninety, expect", "0": "fourteen hundred", "1": "eleven hundred", "2": "eight hundred and fifty"}},
]

for key, extra in MORE.items():
    path = os.path.join(SPECS, key + ".json")
    ep = json.load(open(path, encoding="utf-8"))
    scenes = ep["scenes"]
    close = scenes.pop()
    scenes.extend(extra)
    scenes.append(close)
    ep["scenes"] = scenes
    json.dump(ep, open(path, "w", encoding="utf-8"), indent=1)
    words = sum(len(s["vo"].split()) for s in scenes)
    print(f"{key.upper()}: {len(scenes)} scenes, {words} words (~{words/175:.1f} min)")
