# -*- coding: utf-8 -*-
"""Build ART-LIBRARY.html - a browsable index of every asset in the library."""
import io
import os
import sys

sys.path.insert(0, r"C:\Users\jibra\Desktop\1\KAI\data")
import fusion_art as A

ROOT = r"C:\Users\jibra\Desktop\1\KAI"

CATS = {
    "compute": ["chip", "die", "wafer", "two_die", "superchip"],
    "memory": ["ram_stick", "sodimm", "vram_module", "memory_bank", "cache_grid"],
    "boards": ["pcb", "motherboard", "pcie_slot", "dual_slot", "riser"],
    "power": ["psu", "heat_sink", "fan", "cooler", "power_rails"],
    "machines": ["mini_pc", "tower_pc", "rack_server", "mac_mini", "laptop_closed",
                 "laptop", "gpu"],
    "storage": ["nvme_ssd", "hdd", "model_file", "gguf_blocks", "folder"],
    "network": ["router", "switch", "cloud", "lan_link"],
    "meters": ["gauge", "tok_speed_dial", "cost_dial", "timer_flat", "clock", "meter"],
    "dataflow": ["prompt_stream", "token_blocks", "context_window", "kv_cache", "pipeline"],
    "symbols": ["magnifier", "warning", "checklist", "price_tag", "scales", "question",
                "caveat", "collapse"],
}
seen = set()
sections = []
for cat, names in CATS.items():
    cells = []
    for n in names:
        if n not in A.ART or n in seen:
            continue
        seen.add(n)
        cells.append('<div class="c"><div class="lab">%s</div>%s</div>' % (n, A.ART[n]()))
    if cells:
        sections.append('<h2>%s <span>%d</span></h2><div class="row">%s</div>'
                        % (cat.upper(), len(cells), "".join(cells)))
missing = sorted(set(A.ART) - seen)
if missing:
    sections.append('<h2>UNCATEGORISED <span>%d</span></h2><div class="row">%s</div>'
                    % (len(missing), "".join(
                        '<div class="c"><div class="lab">%s</div>%s</div>' % (n, A.ART[n]())
                        for n in missing)))

html = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Byte Forensics &middot; ART LIBRARY</title><style>
@font-face{font-family:"FuseMono";src:url("file:///C:/Users/jibra/Desktop/1/KAI/core/fonts/JetBrainsMono-Regular.ttf");font-weight:400}
@font-face{font-family:"FuseMono";src:url("file:///C:/Users/jibra/Desktop/1/KAI/core/fonts/JetBrainsMono-Bold.ttf");font-weight:700}
@font-face{font-family:"FuseBlack";src:url("file:///C:/Users/jibra/Desktop/1/KAI/core/fonts/ArchivoBlack-Regular.ttf");font-weight:400}
html,body{margin:0;background:#0D1110;color:#F6F6F4;font-family:FuseMono,monospace}
header{padding:56px 60px 30px;border-bottom:1px solid #1b2321}
h1{font-family:FuseBlack,Impact,sans-serif;font-size:64px;letter-spacing:-.03em;margin:0}
header p{color:#6E7270;letter-spacing:.2em;font-size:14px;text-transform:uppercase;margin:14px 0 0}
h2{font-size:17px;letter-spacing:.26em;color:#F5C531;margin:54px 60px 22px;font-weight:700}
h2 span{color:#4C514E;letter-spacing:.1em}
.row{display:flex;flex-wrap:wrap;padding:0 44px}
.c{width:420px;height:300px;position:relative;display:flex;align-items:center;
   justify-content:center;border:1px solid #1b2321;box-sizing:border-box;background:#0b0f0e}
.c svg{width:390px;height:270px;overflow:visible}
.lab{position:absolute;left:10px;top:8px;color:#F5C531;font-size:11px;letter-spacing:.2em;
     text-transform:uppercase;z-index:9}
</style></head><body>
<header><h1>ART LIBRARY</h1><p>%d assets &middot; byte forensics &middot; fusion look</p></header>
%s
</body></html>""" % (len(A.ART), "\n".join(sections))

out = os.path.join(ROOT, "ART-LIBRARY.html")
open(out, "w", encoding="utf-8").write(html)
print("wrote", out, "-", len(A.ART), "assets")
