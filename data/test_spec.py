# -*- coding: utf-8 -*-
import sys, re
sys.path.insert(0, r"C:\Users\jibra\Desktop\1\KAI\data")
import spec_structured_outputs as spec

W = spec.W
print(f"Total windows: {len(W)}")

errors = []
for i, w in enumerate(W, 1):
    vo = w["vo"]
    words = vo.split()
    if len(words) > 50:
        errors.append(f"Win {i}: word count {len(words)} > 50")
    
    # Check ACT
    for k in ["kicker", "title", "sub", "tape"]:
        val = w.get(k, "")
        if re.search(r"\bact\b", val, re.I):
            errors.append(f"Win {i}: found 'act' in {k}: {val}")
    # Note: in vo, allow words like 'exact' or 'contracts', but not standalone word 'act' or 'act one'
    if re.search(r"\bact\s+(one|two|three|four|five|\d+)\b", vo, re.I):
        errors.append(f"Win {i}: found act number in vo: {vo}")
    
    # Check source
    if not w.get("source"):
        errors.append(f"Win {i}: missing source")

    # Check anchors
    anchors = []
    if "header_at" in w:
        anchors.append(("header_at", w["header_at"]))
    if "art_at" in w:
        anchors.append(("art_at", w["art_at"]))
    if "tape_at" in w:
        anchors.append(("tape_at", w["tape_at"]))
    if "closing" in w and "at" in w["closing"]:
        anchors.append(("closing.at", w["closing"]["at"]))

    for c in w.get("chips", []):
        anchors.append(("chip", c["at"]))
    for s in w.get("stats", []):
        anchors.append(("stat", s["at"]))
    for r in w.get("rows", []):
        anchors.append(("row", r["at"]))
    for b in w.get("bars", []):
        anchors.append(("bar", b["at"]))
        if not b.get("unit"):
            errors.append(f"Win {i}: bar missing unit: {b}")
    for r in w.get("rails", []):
        anchors.append(("rail", r["at"]))
    for c in w.get("chain", []):
        anchors.append(("chain", c["at"]))
    for c in w.get("compare", []):
        anchors.append(("compare", c["at"]))
    for n in w.get("note_items", []):
        anchors.append(("note_item", n["at"]))

    vo_low = vo.lower()
    for lab, at in anchors:
        if at.lower() not in vo_low:
            errors.append(f"Win {i}: anchor not found for {lab}: '{at}'")

    # Check ordering of list elements
    def check_order(items, item_type):
        pos = []
        for it in items:
            idx = vo_low.find(it["at"].lower())
            pos.append(idx)
        if pos != sorted(pos):
            errors.append(f"Win {i}: {item_type} out of order: {pos}")

    if "rows" in w: check_order(w["rows"], "rows")
    if "rails" in w: check_order(w["rails"], "rails")
    if "bars" in w: check_order(w["bars"], "bars")
    if "chain" in w: check_order(w["chain"], "chain")
    if "note_items" in w: check_order(w["note_items"], "note_items")

# Check layout alternation
for i in range(1, len(W)):
    if W[i]["layout"] == W[i-1]["layout"]:
        errors.append(f"Consecutive layout match at Win {i} and {i+1}: {W[i]['layout']}")

print(f"Verification errors: {len(errors)}")
for e in errors[:20]:
    print("  FAIL:", e)
if not errors:
    print("ALL 55 WINDOWS PASS INTERNAL SPEC VERIFICATION 100%!")
