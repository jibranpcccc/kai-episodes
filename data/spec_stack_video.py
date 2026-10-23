# -*- coding: utf-8 -*-
"""
FUSION — "FROM FILE TO FIRST TOKEN"

A three minute video that walks the whole stack and shows the library working
at three different scales:

  * gallery  - one hero asset, as big as the frame allows
  * strip   - three or four assets in a row, much smaller
  * title   - the bookends

No benchmark numbers are claimed here. The only figures on screen are the
quantisation format labels inside the drawings themselves (F32 / F16 / Q8 / Q4),
which are format names rather than results.
"""

import re

NAME = "BYTE-STACK"
TITLE = "FROM FILE TO FIRST TOKEN"
KICKER = "BYTE FORENSICS &middot; ONE LOOK"
SUBTITLE = "the whole stack, in one look"
GLOBAL_PROGRESS = True

W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


def sents(vo):
    return [x.strip() for x in re.split(r"(?<=\.)\s+", vo) if x.strip()]


def hero(vo, kicker, name, blurb, key, side="right", meta=None):
    """One asset, as large as the frame allows."""
    p = sents(vo)
    first = p[0] if p[0].endswith(".") else p[0] + "."
    second = p[1] if len(p) > 1 else first
    win("gallery", vo=vo,
        kicker=kicker, name=name, blurb=blurb,
        meta=meta or ("asset: %s" % key),
        header_at=first, art_at=first, name_at=first, blurb_at=second,
        art=key, art_caption=key.replace("_", " ").upper(), side=side)


def row(vo, kicker, title, items):
    """Several assets in a row, at a smaller scale. One sentence each."""
    p = sents(vo)
    for it, s in zip(items, p):
        it["at"] = s if s.endswith(".") else s + "."
    win("strip", vo=vo, kicker=kicker, title=title,
        header_at=items[0]["at"], items=items)


# ---------------------------------------------------------------- 1 open
win("title",
    vo="This is the whole stack, from one file sitting on a disk all the way "
       "to the first word coming back out of it. Every drawing in this video "
       "comes from one library, and every one of them is built to be used "
       "again in every episode that follows.",
    kicker="BYTE FORENSICS &middot; FUSION",
    title="FROM FILE TO FIRST TOKEN",
    sub="the whole stack &middot; one look &middot; fifty five drawings",
    head_at="This is the whole stack")

# ---------------------------------------------------------------- 2 the file
hero("It starts with one file. The weights, sitting on a disk, doing absolutely "
     "nothing. This is the part most people underestimate. A model is not a "
     "piece of software you install. It is a large collection of numbers, and "
     "until something reads them, they are just numbers.",
     "STEP ONE &middot; THE FILE", "THE MODEL FILE",
     "Every model you run locally is a file. Download it once, and everything "
     "else is hardware doing work on it.",
     "model_file", side="right")

# ---------------------------------------------------------------- 3 quantise / memory / disk
row("Quantise it and the file shrinks. Load it into memory. And keep it on a "
    "drive that does not spin. Three separate problems, three separate parts "
    "of the machine, and every one of them is on this screen right now.",
    "STEP TWO &middot; THE THREE THINGS YOU NEED",
    "QUANTISE, LOAD, STORE",
    [dict(key="gguf_blocks", label="QUANTISED WEIGHTS"),
     dict(key="ram_stick", label="SYSTEM MEMORY"),
     dict(key="nvme_ssd", label="SOLID STATE DRIVE")])

# ---------------------------------------------------------------- 4 where silicon comes from
row("The chip is cut from a wafer. The die is a slice of silicon. And the package "
    "is what you actually solder down. Three steps, and the last one is the "
    "only one most people ever see.",
    "STEP THREE &middot; WHERE SILICON COMES FROM",
    "WAFER, DIE, PACKAGE",
    [dict(key="wafer", label="THE WAFER"),
     dict(key="die", label="THE DIE"),
     dict(key="chip", label="THE PACKAGE")])

# ---------------------------------------------------------------- 5 silicon
hero("Underneath it is silicon. A graphics die and a processor die, on one "
     "board, joined by the interconnect. Everything the model does eventually "
     "becomes arithmetic on a die like this one, and the speed of the whole "
     "machine comes down to how fast that arithmetic happens.",
     "STEP FOUR &middot; THE SILICON", "THE SUPERCHIP",
     "One package, two dies, and a bar of gold between them that moves data "
     "faster than anything else on the board.",
     "superchip", side="left")

# ---------------------------------------------------------------- 5 the board
row("That board is a motherboard. The card plugs into a long slot. And the board "
    "itself is just board. It is tempting to ignore this layer, but the trace "
    "lengths on it are the reason the card has to sit where it sits.",
    "STEP FOUR &middot; THE BOARD",
    "BOARD, SLOT, BOARD",
    [dict(key="motherboard", label="THE MOTHERBOARD"),
     dict(key="pcie_slot", label="THE PCI EXPRESS SLOT"),
     dict(key="pcb", label="THE BOARD ITSELF")])

# ---------------------------------------------------------------- 6 power
hero("And all of it runs on a power supply. This is the part everybody forgets "
     "to check. A card that wants more power than the supply can cleanly "
     "deliver will throttle itself, and then you spend an afternoon "
     "wondering why the numbers changed.",
     "STEP FIVE &middot; THE POWER", "POWER SUPPLY",
     "A power supply is a box of cables and a fan. Get the wrong one and "
     "nothing else on this list matters.",
     "psu", side="right")

# ---------------------------------------------------------------- 7 power / heat / fan
row("The power splits into rails of different thickness. The heat comes off the "
    "die. Into a heatsink. And then into a fan that never stops turning. None "
    "of this is glamorous, and all of it decides what you actually measure.",
    "STEP SIX &middot; HEAT",
    "POWER, PASSIVE, AIR",
    [dict(key="power_rails", label="THE RAILS"),
     dict(key="heat_sink", label="THE HEATSINK"),
     dict(key="cooler", label="THE COOLER"),
     dict(key="fan", label="THE FAN")])

# ---------------------------------------------------------------- 8 the box
hero("All of that fits in a box this small. Or in a tower. Or in a rack, if you "
     "are doing this properly. The box is the easy part. Everything that makes "
     "it fast is inside, and everything that makes it slow is also inside.",
     "STEP SEVEN &middot; THE BOX", "MINI PC",
     "The box is the easy part. Everything that makes it fast is inside, and "
     "everything that makes it slow is also inside.",
     "mini_pc", side="left")

# ---------------------------------------------------------------- 9 the card
hero("And the card itself. Two fans, and they never stop turning. This is the "
     "only part of the stack that was actually designed for the job. "
     "Everything else is plumbing, and plumbing is where the surprises come "
     "from.",
     "STEP EIGHT &middot; THE CARD", "GRAPHICS CARD",
     "The card is the only part of this stack that is actually designed for "
     "the job. The rest is plumbing.",
     "gpu", side="right")

# ---------------------------------------------------------------- 10 network
row("All of it runs on your network. Between the box and the machine. And the "
    "cloud is the alternative, which is the thing this whole channel keeps "
    "arguing against, for a very simple reason.",
    "STEP NINE &middot; THE NETWORK",
    "LOCAL, NOT REMOTE",
    [dict(key="router", label="THE ROUTER"),
     dict(key="lan_link", label="THE LINK"),
     dict(key="cloud", label="NOT THE CLOUD")])

# ---------------------------------------------------------------- 11 the work
row("Then you type a prompt. It becomes tokens. And all of it has to fit inside "
    "the context window, which is the part that decides how long you wait "
    "before the first word appears.",
    "STEP TEN &middot; THE WORK",
    "PROMPT, TOKENS, WINDOW",
    [dict(key="prompt_stream", label="THE PROMPT"),
     dict(key="token_blocks", label="THE TOKENS"),
     dict(key="context_window", label="THE WINDOW")])

# ---------------------------------------------------------------- 13 where you actually use it
hero("And the place you will actually run it. A laptop, with a document on "
     "screen and a caret that will not stop blinking, because the model is "
     "still working through everything you pasted into it.",
     "STEP TWELVE &middot; WHERE YOU USE IT", "THE LAPTOP",
     "The last piece of the stack is the one you are already looking at. "
     "Everything else exists to feed it.",
     "laptop", side="right")

# ---------------------------------------------------------------- 14 the result
hero("And then it runs. This is what speed looks like while you are waiting "
     "for it. Everything upstream of this point exists to move exactly one "
     "number, and that number is how fast the first word arrives.",
     "STEP THIRTEEN &middot; THE RESULT", "THE DIAL",
     "Everything upstream of this point exists to move one number: how fast "
     "the first word arrives.",
     "gauge", side="left")

# ---------------------------------------------------------------- 13 close
win("title",
    vo="One library. One look. Every drawing built to be used again, in every "
       "episode, with no exceptions.",
    kicker="BYTE FORENSICS &middot; FUSION",
    title="ONE LOOK",
    sub="every drawing &middot; every episode &middot; no exceptions",
    head_at="One library")
