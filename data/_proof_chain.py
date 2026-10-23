# -*- coding: utf-8 -*-
"""Literal proof-of-detection for check 2b.

Builds a minimal episode whose only content is the ORIGINAL defect shape:
    <div class="chain__arrow">&rarr;</div>
- no id, no data-fx, no beat - inside a <section class="scene">.
The checker must FAIL 2b on it.  A control copy where the arrow sits under a
data-fx="1" ancestor must PASS.
"""
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _check_open as co  # noqa: E402

TPL = """<!DOCTYPE html><html><head><style>
:root { --gold:#F5C531; }
.chain__arrow { color: var(--gold); font-size: 40px; }
</style></head><body>
<div class="stage">
  <section class="scene" data-scene="0">
    <div class="scene__inner">
      %s
    </div>
  </section>
</div>
<script>
window.FUSION = {"scenes": [{"id":0,"s":0.0,"e":2.0,"label":"A"}],
 "beats": [{"el":"#w0_01","kind":"rise","dur":400,"ease":"rise","s":0.0,"e":0.4,"group":0}]};
</script>
</body></html>"""

CASES = [
    ("BUG", '<div class="chain__arrow">&rarr;</div>'),
    ("CONTROL", '<div id="w0_01" data-fx="1"><div class="chain__arrow">&rarr;</div></div>'),
]

tmp = tempfile.mkdtemp(prefix="checkopen_proof_")
for label, body in CASES:
    with open(os.path.join(tmp, "PROOF.html"), "w", encoding="utf-8") as fh:
        fh.write(TPL % body)
    co.ROOT = tmp
    print("=" * 70)
    print("CASE:", label, "->", body)
    co.main(["_check_open.py", "PROOF"])
print("tmp:", tmp)
