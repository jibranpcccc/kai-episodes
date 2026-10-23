# -*- coding: utf-8 -*-
"""
FUSION SHOWCASE — every asset in the library, one window each.

This is a real episode built with the real engine: real TTS, real word
timings, real beat scheduling. Its job is to put all 55 drawings on screen
so they can be judged in motion, and to document what each one is for.

The script below is the documentation. Every line says what the drawing is
FOR in a video, not what it looks like.
"""

NAME = "BYTE-LIB"
import re
TITLE = "THE ART LIBRARY"
KICKER = "BYTE FORENSICS &middot; DESIGN SYSTEM"
SUBTITLE = "fifty five drawings, one look"
GLOBAL_PROGRESS = True

W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


def asset(cat, idx, total, key, name, blurb, vo, side):
    """One window per asset.

    The art and the name land on the FIRST sentence, so the drawing is the
    visual event of the window. The blurb follows on the second sentence.
    """
    parts = [x.strip() for x in re.split(r"(?<=\.)\s+", vo) if x.strip()]
    first = parts[0] + "." if not parts[0].endswith(".") else parts[0]
    second = parts[1] if len(parts) > 1 else first
    win("gallery", vo=vo,
        kicker="%s &middot; %02d / %d" % (cat.upper(), idx, total),
        name=name,
        blurb=blurb,
        meta="asset: %s" % key,
        header_at=first,
        art_at=first,
        name_at=first,
        blurb_at=second,
        art=key,
        art_caption=key.replace("_", " ").upper(),
        side=side)


# ------------------------------------------------------------------ intro
win("title",
    vo="Every drawing in this library. Flat line art, one accent colour, and "
       "built so it drops straight into an episode.",
    kicker="BYTE FORENSICS &middot; FUSION DESIGN SYSTEM",
    title="THE ART LIBRARY",
    sub="fifty five drawings &middot; one look &middot; built to be reused",
    head_at="Every drawing in this library")

# ============================================================== COMPUTE
asset("compute", 1, 55, "chip", "PROCESSOR PACKAGE",
      "A CPU seen from directly above. The gold corner is pin one, so the "
      "viewer can tell which way round it is.",
      "A processor package seen from directly above. The gold corner is pin one.",
      "right")
asset("compute", 2, 55, "die", "SILICON DIE",
      "The die up close, its core block subdivided, and the memory strip "
      "running down one side.",
      "The die up close, its core block subdivided, and the memory strip down one side.",
      "left")
asset("compute", 3, 55, "wafer", "WAFER",
      "A wafer with the flat cut marked. The gold dies are the ones that "
      "passed, the grey ones did not.",
      "A wafer with the flat cut marked, and the gold dies are the ones that passed.",
      "right")
asset("compute", 4, 55, "two_die", "TWO DIES",
      "Two dies in one package, joined by a gold trace. This is what chiplets "
      "actually look like.",
      "Two dies in one package, joined by a gold trace. This is what chiplets look like.",
      "left")
asset("compute", 5, 55, "superchip", "SUPERCHIP",
      "A graphics die and a processor die on one board, joined by the gold "
      "interconnect bar.",
      "A graphics die and a processor die on one board, joined by the gold interconnect.",
      "right")

# =============================================================== MEMORY
asset("memory", 6, 55, "ram_stick", "MEMORY MODULE",
      "A desktop memory stick. The gold edge is where the notch tells you "
      "which way it goes in.",
      "A desktop memory stick. The gold edge is where the notch tells you which way it goes.",
      "left")
asset("memory", 7, 55, "sodimm", "LAPTOP MEMORY",
      "A laptop module. Shorter, and with one notch instead of two.",
      "A laptop memory module. Shorter, and with one notch instead of two.",
      "right")
asset("memory", 8, 55, "vram_module", "STACKED VRAM",
      "Two boards stacked and bridged. This is what thirty gigabytes of video "
      "memory looks like.",
      "Two boards stacked and bridged. This is what thirty gigabytes of video memory looks like.",
      "left")
asset("memory", 9, 55, "memory_bank", "MEMORY BANK",
      "Eight slots, one of them highlighted. This is the frame you use to "
      "explain capacity.",
      "Eight slots with one of them highlighted. This is the frame you use to explain capacity.",
      "right")
asset("memory", 10, 55, "cache_grid", "CACHE",
      "A cache as a grid of cells, with a diagonal band. It shows what "
      "actually gets hit.",
      "A cache as a grid of cells with a diagonal band. It shows what actually gets hit.",
      "left")

# ================================================================ BOARDS
asset("boards", 11, 55, "pcb", "CIRCUIT BOARD",
      "A board from above, with vias, footprints, and one traced route in "
      "gold.",
      "A circuit board from above, with vias, footprints, and one traced route in gold.",
      "right")
asset("boards", 12, 55, "motherboard", "MOTHERBOARD",
      "A full board. Socket, memory slots, the PCIe slot, and the ports "
      "along the edge.",
      "A full board. Socket, memory slots, the PCIe slot, and the ports along the edge.",
      "left")
asset("boards", 13, 55, "pcie_slot", "PCI EXPRESS",
      "A long slot seen from the side, gold contacts in the floor, and a "
      "latch at the end.",
      "A long slot seen from the side, gold contacts in the floor, and a latch at the end.",
      "right")
asset("boards", 14, 55, "dual_slot", "TWO CARDS",
      "Two cards in one board with a gap between them. That gap is airflow, "
      "and it is thermal.",
      "Two cards in one board with a gap between them. That gap is airflow, and it is thermal.",
      "left")
asset("boards", 15, 55, "riser", "RISER CABLE",
      "A vertical riser, because the graphics card does not always have to "
      "sit flat.",
      "A vertical riser, because the graphics card does not always have to sit flat.",
      "right")

# ================================================================= POWER
asset("power", 16, 55, "psu", "POWER SUPPLY",
      "A power supply with its fan grille, and the bundle of cables that "
      "comes out of it.",
      "A power supply with its fan grille, and the bundle of cables that comes out of it.",
      "left")
asset("power", 17, 55, "heat_sink", "HEATSINK",
      "Finned fins, with the vapour chamber showing in the gaps between "
      "them.",
      "Finned fins, with the vapour chamber showing in the gaps between them.",
      "right")
asset("power", 18, 55, "fan", "COOLING FAN",
      "One big fan. It spins, so it can sit on screen the entire time and "
      "still be alive.",
      "One big fan. It spins, so it can sit on screen the whole time and still be alive.",
      "left")
asset("power", 19, 55, "cooler", "TOWER COOLER",
      "A stack of angled plates on four heat pipes, with the fan clipped to "
      "the front.",
      "A stack of angled plates on four heat pipes, with the fan clipped to the front.",
      "right")
asset("power", 20, 55, "power_rails", "POWER RAILS",
      "Power splitting into three rails of different thickness. The thick gold "
      "one feeds the card.",
      "Power splitting into three rails of different thickness. The thick gold one feeds the card.",
      "left")

# =============================================================== MACHINES
asset("machines", 21, 55, "mini_pc", "MINI PC",
      "A small box with front ports and a vent you can point at when you "
      "talk about noise.",
      "A mini PC. A small box with front ports and a vent you can point at when you talk about noise.",
      "right")
asset("machines", 22, 55, "tower_pc", "MID TOWER",
      "A tower with a glass panel, so the card inside stays visible while "
      "you talk about it.",
      "A mid tower with a glass panel, so the card inside stays visible while you talk about it.",
      "left")
asset("machines", 23, 55, "rack_server", "RACK SERVER",
      "A two unit server. Eight drive bays, four status lights, and one of "
      "them gold.",
      "A two unit server. Eight drive bays, four status lights, and one of them gold.",
      "right")
asset("machines", 24, 55, "mac_mini", "MAC MINI",
      "Flat, quiet, and it still takes twenty four gigabytes of memory. That "
      "surprises people.",
      "A Mac mini. Flat, quiet, and it still takes twenty four gigabytes of memory.",
      "left")
asset("machines", 25, 55, "laptop_closed", "CLOSED LAPTOP",
      "The shape people recognise before anything else has been said.",
      "A closed laptop. The shape people recognise before anything else has been said.",
      "right")
asset("machines", 26, 55, "laptop", "LAPTOP, WAITING",
      "A long document on screen, and a caret that will not stop blinking "
      "because the model is still reading.",
      "A laptop with a long document on screen, and a caret that will not stop blinking.",
      "left")
asset("machines", 27, 55, "gpu", "GRAPHICS CARD",
      "A card with two fans that never stop turning. The most alive object "
      "in the whole library.",
      "A graphics card with two fans that never stop turning. The most alive object in the library.",
      "right")

# =============================================================== STORAGE
asset("storage", 28, 55, "nvme_ssd", "NVME DRIVE",
      "An M.2 drive. The controller sits on one end and the memory in the "
      "middle.",
      "An M.2 drive. The controller sits on one end and the memory in the middle.",
      "left")
asset("storage", 29, 55, "hdd", "HARD DRIVE",
      "A spinning drive, with the arm and the platter. This is the reason "
      "it is slow.",
      "A spinning hard drive, with the arm and the platter. This is the reason it is slow.",
      "right")
asset("storage", 30, 55, "model_file", "MODEL FILE",
      "The model itself. Four gigabytes, and it is the only download in this "
      "whole channel that matters.",
      "The model file. Four gigabytes, and it is the only download in this channel that matters.",
      "left")
asset("storage", 31, 55, "gguf_blocks", "QUANTISATION",
      "The same file quantised. The big gold blocks are more bits, and they "
      "are also more size.",
      "The same file quantised. The big gold blocks are more bits, and they are also more size.",
      "right")
asset("storage", 32, 55, "folder", "SAVED TO DISK",
      "A folder with the model in it, and the arrow that put it there.",
      "A folder with the model saved to disk, and the arrow that put it there.",
      "left")

# ================================================================ NETWORK
asset("network", 33, 55, "router", "HOME ROUTER",
      "A router, with the address you actually type into a browser when the "
      "thing will not connect.",
      "A home router, with the address you actually type into a browser when the thing will not connect.",
      "right")
asset("network", 34, 55, "switch", "NETWORK SWITCH",
      "Eight ports. Port one is the uplink, and it is the one that is gold.",
      "An eight port switch. Port one is the uplink, and it is the one that is gold.",
      "left")
asset("network", 35, 55, "cloud", "NOT THE CLOUD",
      "A cloud with a cross straight through it. Because this channel is "
      "about not using one.",
      "A cloud with a cross straight through it. Because this channel is about not using one.",
      "right")
asset("network", 36, 55, "lan_link", "LOCAL LINK",
      "Two boxes on your own network. This is the alternative to a monthly "
      "subscription.",
      "Two boxes on your own network. This is the alternative to a monthly subscription.",
      "left")

# ================================================================= METERS
asset("meters", 37, 55, "gauge", "SPEEDOMETER",
      "A dial with a danger zone, and a needle that sweeps. It reads as "
      "live rather than printed.",
      "A speedometer with a danger zone, and a needle that sweeps. It reads as live rather than printed.",
      "right")
asset("meters", 38, 55, "tok_speed_dial", "TOKENS PER SECOND",
      "The number every comparison in this channel starts with, on a dial.",
      "Tokens per second, on a dial. The number every comparison in this channel starts with.",
      "left")
asset("meters", 39, 55, "cost_dial", "COST PER HOUR",
      "Cost split into quarters, with one of them gold. That is the part "
      "that hurts.",
      "Cost per hour, split into quarters, with one of them gold. That is the part that hurts.",
      "right")
asset("meters", 40, 55, "timer_flat", "TIMER",
      "A flat timer, for the frames where the thing you are measuring is a "
      "wait.",
      "A flat timer, for the frames where the thing you are measuring is a wait.",
      "left")
asset("meters", 41, 55, "clock", "STOPWATCH",
      "A stopwatch with a sweeping hand and a prompt that never finishes "
      "loading.",
      "A stopwatch with a sweeping hand and a prompt that never finishes loading.",
      "right")
asset("meters", 42, 55, "meter", "BANDWIDTH",
      "The bus, with the limit marked in gold. This is the wall prefill "
      "runs into.",
      "The memory bus, with the limit marked in gold. This is the wall prefill runs into.",
      "left")

# ================================================================ DATAFLOW
asset("dataflow", 43, 55, "prompt_stream", "YOUR PROMPT",
      "Your prompt arriving line by line, with the caret at the end of it.",
      "Your prompt arriving line by line, with the caret at the end of it.",
      "right")
asset("dataflow", 44, 55, "token_blocks", "TOKENS",
      "Tokens in a row, and a count underneath. This is what context length "
      "actually is.",
      "Tokens in a row, and a count underneath. This is what context length actually is.",
      "left")
asset("dataflow", 45, 55, "context_window", "CONTEXT WINDOW",
      "The window filling up on one side, and the half you have not used "
      "yet on the other.",
      "The context window filling up on one side, and the half you have not used yet on the other.",
      "right")
asset("dataflow", 46, 55, "kv_cache", "THE CACHE",
      "The cache, read and written on every token. This is why long context "
      "is slow.",
      "The cache, read and written on every token. This is why long context is slow.",
      "left")
asset("dataflow", 47, 55, "pipeline", "THE PIPELINE",
      "Prompt, prefill, decode, stream. The whole path, in four boxes.",
      "Prompt, prefill, decode, stream. The whole path, in four boxes.",
      "right")

# ================================================================= SYMBOLS
asset("symbols", 48, 55, "magnifier", "MAGNIFIER",
      "For the frames where you are about to check something.",
      "A magnifying glass, for the frames where you are about to check something.",
      "left")
asset("symbols", 49, 55, "warning", "WARNING",
      "For the claim that is about to fall apart.",
      "A warning triangle, for the claim that is about to fall apart.",
      "right")
asset("symbols", 50, 55, "checklist", "CHECKLIST",
      "For the fine print that nobody reads but everybody should.",
      "A checklist, for the fine print that nobody reads but everybody should.",
      "left")
asset("symbols", 51, 55, "price_tag", "PRICE TAG",
      "Because every single number in this channel has a cost attached to "
      "it.",
      "A price tag, because every number in this channel has a cost attached to it.",
      "right")
asset("symbols", 52, 55, "scales", "SCALES",
      "For the comparison that is not as even as it looks.",
      "A set of scales, for the comparison that is not as even as it looks.",
      "left")
asset("symbols", 53, 55, "question", "THE QUESTION",
      "For the part of the video you do not know the answer to yet.",
      "A question mark, for the part of the video you do not know the answer to yet.",
      "right")
asset("symbols", 54, 55, "caveat", "THE FINE PRINT",
      "A document under a lens. Every episode owes the viewer one of these.",
      "A document under a lens. Every episode owes the viewer one of these.",
      "left")
asset("symbols", 55, 55, "collapse", "THE COLLAPSE",
      "Two curves on one chart. One falls off a cliff, and one barely moves.",
      "Two curves on one chart. One falls off a cliff, and one barely moves.",
      "right")

# ------------------------------------------------------------------ outro
win("title",
    vo="Fifty five drawings, one accent colour, and every one of them built "
       "to be used again.",
    kicker="BYTE FORENSICS &middot; FUSION DESIGN SYSTEM",
    title="ONE LOOK",
    sub="every drawing &middot; every episode &middot; no exceptions",
    head_at="Fifty five drawings")
