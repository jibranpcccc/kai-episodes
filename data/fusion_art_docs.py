# -*- coding: utf-8 -*-
"""Write a markdown index of the asset library."""
import io
import os
import re
import sys

sys.path.insert(0, r"C:\Users\jibra\Desktop\1\KAI\data")
import fusion_art as A

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
CATS = [
    ("compute", ["chip", "die", "wafer", "two_die", "superchip"]),
    ("memory", ["ram_stick", "sodimm", "vram_module", "memory_bank", "cache_grid"]),
    ("boards", ["pcb", "motherboard", "pcie_slot", "dual_slot", "riser"]),
    ("power", ["psu", "heat_sink", "fan", "cooler", "power_rails"]),
    ("machines", ["mini_pc", "tower_pc", "rack_server", "mac_mini", "laptop_closed",
                  "laptop", "gpu"]),
    ("storage", ["nvme_ssd", "hdd", "model_file", "gguf_blocks", "folder"]),
    ("network", ["router", "switch", "cloud", "lan_link"]),
    ("meters", ["gauge", "tok_speed_dial", "cost_dial", "timer_flat", "clock", "meter"]),
    ("dataflow", ["prompt_stream", "token_blocks", "context_window", "kv_cache", "pipeline"]),
    ("symbols", ["magnifier", "warning", "checklist", "price_tag", "scales", "question",
                 "caveat", "collapse"]),
]

lines = [
    "# FUSION ART LIBRARY",
    "",
    "**%d reusable drawings** for the Byte Forensics fusion look. Flat line art on" % len(A.ART),
    "near-black, one accent colour per drawing, every one with a tight viewBox so it",
    "fills whatever panel it is dropped into.",
    "",
    "Browse them: open **`ART-LIBRARY.html`** in a browser.",
    "",
    "Use them in a spec by name:",
    "",
    "```python",
    'win("bars", vo="...", art="chip", art_caption="SILICON DIE", ...)',
    "```",
    "",
    "The style contract these obey is `data/fusion_art_spec.md`.",
    "",
]
seen = set()
for cat, names in CATS:
    rows = []
    for n in names:
        if n not in A.ART or n in seen:
            continue
        seen.add(n)
        s = A.ART[n]()
        vb = re.search(r'viewBox="([^"]+)"', s)
        amb = sorted(set(re.findall(r'data-amb="(\w+)"', s)))
        rows.append("| `%s` | %s | %s |" % (n, vb.group(1) if vb else "?",
                                             ", ".join(amb) if amb else "static"))
    if rows:
        lines += ["## %s (%d)" % (cat.upper(), len(rows)),
                  "", "| asset | viewBox | motion |", "|---|---|---|"] + rows + [""]

rest = sorted(set(A.ART) - seen)
if rest:
    lines += ["## OTHER (%d)" % len(rest), "", "| asset | viewBox | motion |", "|---|---|---|"]
    for n in rest:
        s = A.ART[n]()
        vb = re.search(r'viewBox="([^"]+)"', s)
        amb = sorted(set(re.findall(r'data-amb="(\w+)"', s)))
        lines.append("| `%s` | %s | %s |" % (n, vb.group(1) if vb else "?",
                                             ", ".join(amb) if amb else "static"))
    lines.append("")

lines += [
    "## Motion hooks",
    "",
    "| hook | does |",
    "|---|---|",
    "| `data-amb=\"spin\"` | rotates. `data-amb-speed` scales 132 deg/s (0.1 slow, 0.3 a fan). `data-amb-k` offsets the start angle. If the part pivots off its own bbox, add `data-amb-box=\"view-box\"` and `data-amb-origin=\"<x>px <y>px\"`. |",
    "| `data-amb=\"pulse\"` | opacity 0.60 to 1.00. `data-amb-k` sets the phase so a row of markers breathes in sequence. |",
    "| `data-amb=\"blink\"` | a cursor waiting. |",
    "",
    "A shape can pin its own place in the sketch-on order with",
    "`data-draw-delay=\"0.42\"` (seconds) — use it for a marker that must not appear",
    "before the line that leads to it.",
    "",
    "## Rules that are not negotiable",
    "",
    "1. A `<g>` NEVER carries a `transform` attribute. Animating `style.transform` on",
    "   an element that HAS one collapses it to the top-left.",
    "2. The viewBox string is used verbatim. Never prefix it with `0 0`.",
    "3. Nothing overlaps a label, a line, or another label.",
    "4. One accent per drawing, used sparingly.",
    "5. Every drawing reads at thumbnail size.",
    "",
    "## Checks",
    "",
    "```",
    "python data/fusion_art_audit.py     # structural: viewBox, XML, transform, accents",
    "python data/fusion_art_sheet.py     # renders proof/_library.png, the contact sheet",
    "python data/fusion_art_index.py     # rebuilds ART-LIBRARY.html and this file",
    "```",
    "",
]

out = os.path.join(ROOT, "docs", "ART-LIBRARY.md")
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, "w", encoding="utf-8").write("\n".join(lines))
print("wrote", out, "-", len(A.ART), "assets")
