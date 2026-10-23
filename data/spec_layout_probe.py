# -*- coding: utf-8 -*-
"""
LAYOUT PROBE
============
A four window smoke test that exercises the four layouts which carry a source
footer of their own -- gallery, title, strip and nodes -- so a regression in
the builder shows up as a gate failure instead of a silent missing footer.

    FUSION_SPEC=spec_layout_probe python data/fusion_build.py
    python data/fusion_gate.py BYTE-LAYOUT-PROBE spec_layout_probe

It is a test fixture, not an episode. It is never shipped.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

NAME = "BYTE-LAYOUT-PROBE"
TITLE = "LAYOUT PROBE"
DOC_TITLE = "LAYOUT PROBE &middot; BYTE FORENSICS"
KICKER = "BYTE FORENSICS &middot; LAYOUT PROBE"
SUBTITLE = "a test fixture, not an episode"
GLOBAL_PROGRESS = False

W = []


def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))


win("gallery",
    vo="Three different things are called memory on a local machine. The weights "
       "sit on the disk. The weights sit on the card. The cache sits in between, "
       "and it is the only one that grows while you talk.",
    kicker="PROBE &middot; GALLERY",
    title="THREE THINGS CALLED MEMORY",
    art="cache_grid", art_caption="ONE GRID",
    header_at="Three different things are called memory",
    art_at="The weights sit on the disk",
    name="THREE THINGS CALLED MEMORY",
    blurb="the weights on the disk, the weights on the card, and the cache in "
          "between",
    meta="only the cache grows while you talk",
    name_at="The weights sit on the card",
    blurb_at="The cache sits in between",
    meta_at="the only one that grows while you talk",
    side="left",
    source="derived &middot; qwen2.5 3b instruct &middot; 36 layers")

win("title",
    vo="Now the part people quote wrong. A longer context is not only slower. "
       "It also changes what the machine has to hold while it answers. That is "
       "a memory bill, not a speed number.",
    kicker="PROBE &middot; TITLE",
    title="THE PART PEOPLE QUOTE WRONG",
    sub="a longer context is not only slower",
    art="token_blocks",
    head_at="Now the part people quote wrong",
    closing=dict(t="NOT ONLY SLOWER", c="gold",
                 at="It also changes what the machine has to hold"),
    tape="A MEMORY BILL, NOT A SPEED NUMBER",
    tape_at="That is a memory bill, not a speed number",
    source="mechanism &middot; the kv cache grows with the context length")

win("strip",
    vo="A cache is in one of three states. Empty, before the prompt lands. "
       "Filling, while the prefill pass writes it. Full, and still growing with "
       "every token you send.",
    kicker="PROBE &middot; STRIP",
    title="THREE STATES OF A CACHE",
    header_at="A cache is in one of three states",
    items=[
        dict(key="token_blocks", label="EMPTY",
             at="Empty, before the prompt lands"),
        dict(key="context_window", label="FILLING",
             at="Filling, while the prefill pass writes it"),
        dict(key="collapse", label="FULL",
             at="Full, and still growing with every token you send"),
    ],
    closing=dict(t="THREE STATES, ONE CACHE", c="gold",
                 at="Full, and still growing with every token you send"),
    source="mechanism &middot; prefill writes the cache, decode extends it")

win("nodes",
    vo="Every new token pays for the whole cache again. It reads the keys and "
       "values for every layer, attends over them, and then writes one more "
       "entry at the end. That is the cost of the next token.",
    kicker="PROBE &middot; NODES",
    title="THE COST OF THE NEXT TOKEN",
    header_at="Every new token pays for the whole cache again",
    art="pipeline", art_caption="THE PASS",
    art_at="It reads the keys and values for every layer",
    chain=[
        dict(t="READ", s="every layer",
             at="It reads the keys and values for every layer"),
        dict(t="ATTEND", s="over them", at="attends over them"),
        dict(t="WRITE", s="one more entry", at="writes one more entry at the end"),
    ],
    closing=dict(t="THAT IS THE COST", c="gold",
                 at="That is the cost of the next token"),
    source="mechanism &middot; one forward pass reads the cache and extends it")


if __name__ == "__main__":
    print("LAYOUT PROBE -- %d windows" % len(W))
    for i, w in enumerate(W):
        print("  %d  %-8s %3d words  source=%s"
              % (i + 1, w["layout"], len(w["vo"].split()), bool(w.get("source"))))
