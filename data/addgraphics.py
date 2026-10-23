import re, os

p = r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
s = open(p, encoding="utf-8").read().replace("\r\n", "\n")

# ---------------------------------------------------------------- CSS
CSS_ADD = r'''  /* ---- graph furniture ---- */
  .scene::before{{content:"";position:absolute;inset:0;pointer-events:none;opacity:.5;
    background-image:radial-gradient(#1A2422 1px,transparent 1px);background-size:30px 30px}}
  .ruler{{position:absolute;left:50%;transform:translateX(-50%);bottom:64px;width:1100px;height:74px}}
  .ruler__line{{position:absolute;left:0;right:0;top:36px;height:2px;background:#3C4241}}
  .ruler__tick{{position:absolute;top:29px;width:2px;height:16px;background:#3C4241;transform:translateX(-50%)}}
  .ruler__tick span{{position:absolute;top:20px;left:50%;transform:translateX(-50%);font-family:var(--mono);
    font-weight:700;font-size:13px;letter-spacing:.14em;color:#6E7270;white-space:nowrap}}
  .ruler__dot{{position:absolute;top:31px;width:12px;height:12px;border-radius:50%;background:var(--yellow);
    transform:translateX(-50%);box-shadow:0 0 0 4px rgba(248,207,51,.18)}}
  .ruler__lab{{position:absolute;top:0;transform:translateX(-50%);font-family:var(--mono);font-weight:800;
    font-size:17px;color:var(--yellow);letter-spacing:.04em}}
  .ring{{position:absolute;right:120px;top:50%;transform:translateY(-50%);width:200px;height:200px}}
  .spark{{position:absolute;left:50%;transform:translateX(-50%);bottom:52px;width:520px;height:220px}}
'''

anchor = """              background:rgba(4,94,239,.08)}}"""
assert anchor in s, "style anchor not found"
if ".ruler{{" not in s:
    s = s.replace(anchor, anchor + "\n" + CSS_ADD, 1)

# ---------------------------------------------------------------- EP02 : price ruler
EP02_ANCHOR = '      <div class="cap">What it actually costs, per year</div>'
RULER = '''
      <div class="ruler" data-in="@row3@">
        <div class="ruler__line"></div>
        <div class="ruler__tick" style="left:0%"><span>$0</span></div>
        <div class="ruler__tick" style="left:100%"><span>$700</span></div>
        <div class="ruler__dot" style="left:30%"></div><div class="ruler__lab" style="left:30%">$210</div>
        <div class="ruler__dot" style="left:42%"></div><div class="ruler__lab" style="left:42%">$294</div>
        <div class="ruler__dot" style="left:90%"></div><div class="ruler__lab" style="left:90%">$631</div>
      </div>'''
assert EP02_ANCHOR in s, "ep02 cap not found"
if 'class="ruler"' not in s:
    s = s.replace(EP02_ANCHOR, EP02_ANCHOR + "\n" + RULER, 1)

# ---------------------------------------------------------------- EP03 : ring + sparkline
EP03_RING_ANCHOR = '      <div class="cap" data-in="@kv@">The KV cache doubles</div>'
RING = '''
      <svg class="ring" data-in="@fits@" viewBox="0 0 120 120">
        <circle cx="60" cy="60" r="52" fill="none" stroke="#1B2422" stroke-width="9"/>
        <circle cx="60" cy="60" r="52" fill="none" stroke="#F8CF33" stroke-width="9" stroke-linecap="round"
                stroke-dasharray="326.7" stroke-dashoffset="55.5" transform="rotate(-90 60 60)"/>
        <text x="60" y="57" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800"
              font-size="25" fill="#F6F6F4">83%</text>
        <text x="60" y="74" text-anchor="middle" font-family="monospace" font-size="8.5"
              fill="#6E7270" letter-spacing="1.2">VRAM USED</text>
      </svg>'''
assert EP03_RING_ANCHOR in s, "ep03 kv cap not found"
if 'class="ring"' not in s:
    s = s.replace(EP03_RING_ANCHOR, EP03_RING_ANCHOR + "\n" + RING, 1)

EP03_SPARK_ANCHOR = '      <div class="cap">Tokens per second, per user</div>'
SPARK = '''
      <svg class="spark" data-in="@r4@" viewBox="0 0 260 110">
        <line x1="10" y1="100" x2="250" y2="100" stroke="#24302D" stroke-width="1.5"/>
        <polyline points="10,28.9 89.2,60.9 168.4,84 250,92.9" fill="none" stroke="#2294D6"
                  stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="10" cy="28.9" r="4" fill="#2294D6"/>
        <circle cx="89.2" cy="60.9" r="4" fill="#2294D6"/>
        <circle cx="168.4" cy="84" r="4" fill="#2294D6"/>
        <circle cx="250" cy="92.9" r="4" fill="#E12A27"/>
      </svg>'''
assert EP03_SPARK_ANCHOR in s, "ep03 table cap not found"
if 'class="spark"' not in s:
    s = s.replace(EP03_SPARK_ANCHOR, EP03_SPARK_ANCHOR + "\n" + SPARK, 1)

open(p, "w", encoding="utf-8", newline="\n").write(s)
print("added: dot grid (all scenes), price ruler (EP02), ring + sparkline (EP03)")
