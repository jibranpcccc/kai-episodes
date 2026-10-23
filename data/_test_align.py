# -*- coding: utf-8 -*-
"""Unit test for the caption alignment: script words onto synthesiser tokens."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from fusion_build import _align_tokens, _groups

CASES = [
    # (script words, synthesiser tokens, expected token index per script word)
    (["llama", ".", "cpp", "runs"], ["llama", ".", "cpp", "runs"], [0, 1, 2, 3]),
    (["llama.cpp", "runs"], ["llama", ".", "cpp", "runs"], [0, 3]),
    (["two", "hundred", "and", "eighty-eight", "mebibytes"],
     ["two", "hundred", "eighty-eight", "mebibytes"], [0, 1, 2, 2, 3]),
    (["afford."], ["afford"], [0]),
    (["a", "b"], ["a", "b", "c"], [0, 1]),
    (["MiB", "per", "token"], ["mee", "bee", "per", "token"], [0, 2, 3]),
]

bad = 0
for vw, tw, want in CASES:
    ws = [(0.0 * i, t) for i, t in enumerate(tw)]
    got = _align_tokens(vw, ws)
    ok = got == want
    print("%-4s script=%-46s tokens=%-34s -> %s (want %s)"
          % ("PASS" if ok else "FAIL", vw, tw, got, want))
    if not ok:
        bad += 1

print()
print("groups of 8 over 50 words:", _groups(50, 8))
print("groups of 8 over 51 words:", _groups(51, 8))
print("groups of 8 over 9  words:", _groups(9, 8))
print()
print("PROBLEMS: %d" % bad)
sys.exit(1 if bad else 0)
