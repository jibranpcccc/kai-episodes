# -*- coding: utf-8 -*-
"""FUSION ART LIBRARY — programmatic audit + full contact sheet."""
import io
import json
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, r"C:\Users\jibra\Desktop\1\KAI\data")
import fusion_art as A

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
FAIL = []
WARN = []

print("FUSION ART LIBRARY AUDIT — %d assets\n" % len(A.ART))

for name in sorted(A.ART):
    fn = A.ART[name]
    try:
        s = fn()
    except Exception as e:
        FAIL.append((name, "EXCEPTION %s" % e))
        continue
    if not s.startswith("<svg") or not s.endswith("</svg>"):
        FAIL.append((name, "not a bare svg element"))
        continue
    # exactly one viewBox, four numbers
    import re
    vbs = re.findall(r'viewBox="([^"]+)"', s)
    if len(vbs) != 1:
        FAIL.append((name, "%d viewBox attributes" % len(vbs)))
        continue
    parts = vbs[0].split()
    if len(parts) != 4:
        FAIL.append((name, "viewBox has %d numbers: %r" % (len(parts), vbs[0])))
        continue
    try:
        vx, vy, vw, vh = [float(x) for x in parts]
    except ValueError:
        FAIL.append((name, "viewBox not numeric"))
        continue
    if vw <= 0 or vh <= 0:
        FAIL.append((name, "viewBox has non-positive size"))
        continue
    # no transform on any <g>
    try:
        root = ET.fromstring(s)
    except ET.ParseError as e:
        FAIL.append((name, "not well-formed XML: %s" % e))
        continue
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag == "g" and el.get("transform"):
            FAIL.append((name, "<g> carries a transform attribute"))
    # well-formedness of the whole document
    # colour discipline: count accent usage
    g = s.count(GOLD) if (GOLD := "#F5C531") else 0
    c = s.count("#38D9E8")
    r = s.count("#E12A27")
    if g + c + r > 26:
        WARN.append((name, "heavy accent use: gold %d cyan %d red %d" % (g, c, r)))
    if "data-amb" in s and "data-draw-delay" in s:
        pass
    # ambient hook sanity
    if "data-amb" in s:
        for el in root.iter():
            if el.get("data-amb") in ("spin", "pulse", "blink", "float"):
                if el.get("data-amb-box") == "view-box" and not el.get("data-amb-origin"):
                    FAIL.append((name, "view-box spin without data-amb-origin"))
    print("  ok  %-16s viewBox=%-18s amb=%d" % (name, vbs[0], s.count("data-amb")))

print()
if FAIL:
    print("FAILURES (%d)" % len(FAIL))
    for n, m in FAIL:
        print("   [%s] %s" % (n, m))
if WARN:
    print("WARNINGS (%d)" % len(WARN))
    for n, m in WARN:
        print("   [%s] %s" % (n, m))
if not FAIL:
    print("all %d assets pass the structural audit" % len(A.ART))
