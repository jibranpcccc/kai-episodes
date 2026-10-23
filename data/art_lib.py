"""Shared hardware drawing library."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GPU = open(os.path.join(ROOT, "data", "art_gpu.svg"), encoding="utf-8").read()
CHIP = ('<svg viewBox="0 0 240 240" class="art"><rect x="58" y="58" width="124" height="124" rx="14" '
        'fill="rgba(255,255,255,.025)" stroke="rgba(237,234,227,.85)" stroke-width="2"/>'
        '<rect x="88" y="88" width="64" height="64" rx="8" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.4)" stroke-width="1.5"/>'
        '<g class="spin"><rect x="106" y="106" width="28" height="28" rx="5" fill="rgba(180,227,61,.9)"/></g>'
        '<g stroke="rgba(237,234,227,.45)" stroke-width="1.5"><path d="M78 58V34M98 58V34M118 58V34M138 58V34M158 58V34"/>'
        '<path d="M78 182v24M98 182v24M118 182v24M138 182v24M158 182v24"/>'
        '<path d="M58 78H34M58 98H34M58 118H34M58 138H34M58 158H34"/>'
        '<path d="M182 78h24M182 98h24M182 118h24M182 138h24M182 158h24"/></g></svg>')
LAPTOP = ('<svg viewBox="0 0 380 250" class="art"><rect x="54" y="24" width="272" height="170" rx="12" '
          'fill="rgba(255,255,255,.025)" stroke="rgba(237,234,227,.85)" stroke-width="2"/>'
          '<path d="M20 212H360L334 190H46Z" fill="rgba(255,255,255,.02)" stroke="rgba(237,234,227,.85)" stroke-width="2"/>'
          '<rect x="78" y="50" width="146" height="14" rx="4" fill="rgba(180,227,61,.85)"/>'
          '<rect x="78" y="80" width="216" height="9" rx="4" fill="rgba(237,234,227,.22)"/>'
          '<rect x="78" y="99" width="188" height="9" rx="4" fill="rgba(237,234,227,.22)"/>'
          '<rect x="78" y="118" width="204" height="9" rx="4" fill="rgba(237,234,227,.22)"/>'
          '<rect x="78" y="144" width="118" height="10" rx="4" fill="rgba(245,213,71,.8)"/></svg>')


RAM = ('<svg viewBox="0 0 460 140" class="art">'
       '<rect x="10" y="30" width="440" height="80" rx="8" fill="rgba(255,255,255,.025)" '
       'stroke="rgba(237,234,227,.85)" stroke-width="2"/>'
       '<rect x="30" y="46" width="56" height="48" rx="4" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.45)" stroke-width="1.2"/>'
       '<rect x="96" y="46" width="56" height="48" rx="4" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.45)" stroke-width="1.2"/>'
       '<rect x="162" y="46" width="56" height="48" rx="4" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.45)" stroke-width="1.2"/>'
       '<rect x="228" y="46" width="56" height="48" rx="4" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.45)" stroke-width="1.2"/>'
       '<rect x="294" y="46" width="56" height="48" rx="4" fill="rgba(180,227,61,.85)"/>'
       '<rect x="360" y="46" width="56" height="48" rx="4" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.45)" stroke-width="1.2"/>'
       '<rect x="24" y="104" width="196" height="10" rx="3" fill="rgba(245,213,71,.7)"/>'
       '<rect x="46" y="104" width="7" height="10" fill="rgba(0,0,0,.65)"/>'
       '<rect x="72" y="104" width="7" height="10" fill="rgba(0,0,0,.65)"/>'
       '<rect x="98" y="104" width="7" height="10" fill="rgba(0,0,0,.65)"/>'
       '<rect x="124" y="104" width="7" height="10" fill="rgba(0,0,0,.65)"/>'
       '</svg>')

SLOT = ('<svg viewBox="0 0 480 200" class="art">'
        '<rect x="20" y="30" width="440" height="140" rx="10" fill="rgba(255,255,255,.02)" '
        'stroke="rgba(237,234,227,.55)" stroke-width="2"/>'
        '<rect x="44" y="86" width="392" height="34" rx="6" fill="rgba(0,0,0,.4)" '
        'stroke="rgba(237,234,227,.7)" stroke-width="2"/>'
        '<g fill="rgba(245,213,71,.8)">'
        '<rect x="60" y="96" width="14" height="14" rx="2"/><rect x="88" y="96" width="14" height="14" rx="2"/>'
        '<rect x="116" y="96" width="14" height="14" rx="2"/><rect x="144" y="96" width="14" height="14" rx="2"/>'
        '<rect x="172" y="96" width="14" height="14" rx="2"/><rect x="200" y="96" width="14" height="14" rx="2"/>'
        '<rect x="228" y="96" width="14" height="14" rx="2"/><rect x="256" y="96" width="14" height="14" rx="2"/></g>'
        '<rect x="300" y="96" width="120" height="14" rx="4" fill="rgba(237,234,227,.25)"/>'
        '<rect x="60" y="46" width="150" height="10" rx="3" fill="rgba(56,217,232,.75)"/>'
        '<rect x="240" y="46" width="90" height="10" rx="3" fill="rgba(237,234,227,.2)"/>'
        '<text x="60" y="152" class="small">PCIE &middot; 16 LANES</text>'
        '</svg>')

CACHE = ('<svg viewBox="0 0 420 260" class="art">'
         '<rect x="20" y="20" width="380" height="220" rx="10" fill="rgba(255,255,255,.02)" '
         'stroke="rgba(237,234,227,.5)" stroke-width="1.5"/>'
         '<text x="34" y="46" class="small">KEY</text><text x="200" y="46" class="small">VALUE</text>'
         + "".join(
             f'<rect x="{34+j*86}" y="{62+k*44}" width="34" height="30" rx="4" '
             f'fill="{"rgba(245,213,71,.85)" if (j+k)%3==0 else "rgba(237,234,227,.10)"}"/>'
             f'<rect x="{200+j*48}" y="{62+k*44}" width="34" height="30" rx="4" '
             f'fill="{"rgba(180,227,61,.85)" if (j+k)%2==0 else "rgba(237,234,227,.10)"}"/>'
             for k in range(4) for j in range(2))
         + '</svg>')



DIE = ('<svg viewBox="0 0 300 300" class="art">'
       '<rect x="30" y="30" width="240" height="240" rx="6" fill="rgba(255,255,255,.02)" '
       'stroke="rgba(237,234,227,.8)" stroke-width="2"/>'
       '<g fill="rgba(237,234,227,.10)" stroke="rgba(237,234,227,.25)" stroke-width="1">'
       + "".join(f'<rect x="{52+ j*44}" y="{52+k*44}" width="38" height="38" rx="3"/>'
                 for k in range(5) for j in range(5))
       + '</g><rect x="96" y="96" width="108" height="108" rx="4" fill="rgba(180,227,61,.85)"/>'
       '<text x="30" y="292" class="small">ONE DIE &middot; 27B</text></svg>')

HEATSINK = ('<svg viewBox="0 0 420 200" class="art">'
            '<rect x="16" y="40" width="388" height="34" rx="6" fill="rgba(255,255,255,.03)" '
            'stroke="rgba(237,234,227,.7)" stroke-width="2"/>'
            + "".join(f'<rect x="{28+i*34}" y="{74}" width="20" height="{i*6+70}" rx="4" '
                      f'fill="rgba(237,234,227,.08)" stroke="rgba(237,234,227,.35)" stroke-width="1.5"/>'
                      for i in range(11))
            + '<g class="spin"><circle cx="120" cy="26" r="14" fill="none" stroke="rgba(237,234,227,.7)" stroke-width="1.5"/><path d="M120 14a12 12 0 0 1 0 24" fill="none" stroke="rgba(237,234,227,.4)" stroke-width="4"/></g>'  # fan circle
              '<circle cx="300" cy="26" r="10" fill="rgba(245,213,71,.85)"/>'
              '<text x="16" y="192" class="small">HEAT SINK &middot; PASSIVE</text></svg>')


TWODIE = ('<svg viewBox="0 0 520 240" class="art">'
          '<rect x="24" y="40" width="190" height="150" rx="8" fill="rgba(255,255,255,.02)" '
          'stroke="rgba(237,234,227,.75)" stroke-width="2"/>'
          '<rect x="56" y="70" width="126" height="90" rx="4" fill="rgba(237,234,227,.10)" stroke="rgba(237,234,227,.3)" stroke-width="1"/>'
          '<text x="24" y="216" class="small">27.32B</text>'
          '<rect x="300" y="40" width="196" height="150" rx="8" fill="rgba(255,255,255,.03)" '
          'stroke="rgba(180,227,61,.85)" stroke-width="2"/>'
          '<rect x="336" y="70" width="124" height="90" rx="4" fill="rgba(180,227,61,.85)"/>'
          '<text x="300" y="216" class="small">27.85B</text></svg>')

PCB = ('<svg viewBox="0 0 460 240" class="art">'
       '<rect x="16" y="20" width="428" height="200" rx="10" fill="rgba(255,255,255,.02)" '
       'stroke="rgba(237,234,227,.55)" stroke-width="2"/>'
       '<g stroke="rgba(245,213,71,.45)" stroke-width="2" fill="none">'
       '<path d="M120 90H300V150H380"/><path d="M120 120H250V180H380"/><path d="M80 150H200"/></g>'
       '<rect x="56" y="66" width="70" height="60" rx="4" fill="rgba(237,234,227,.14)" stroke="rgba(237,234,227,.7)" stroke-width="1.5"/>'
       '<rect x="300" y="120" width="86" height="46" rx="4" fill="rgba(180,227,61,.75)"/>'
       '<text x="16" y="236" class="small">RECIPE &middot; NOT PARAMETERS</text></svg>')

QUANT = ('<svg viewBox="0 0 420 160" class="art">'
         '<rect x="24" y="46" width="110" height="70" rx="6" fill="rgba(245,213,71,.8)"/>'
         '<text x="24" y="140" class="small">4-BIT</text>'
         '<rect x="156" y="46" width="86" height="70" rx="6" fill="rgba(56,217,232,.75)"/>'
         '<text x="156" y="140" class="small">3-BIT</text>'
         '<rect x="264" y="46" width="64" height="70" rx="6" fill="rgba(232,72,61,.8)"/>'
         '<text x="264" y="140" class="small">2-BIT</text></svg>')


TOWER = ('<svg viewBox="0 0 300 380" class="art">'
         '<rect x="40" y="16" width="220" height="348" rx="12" fill="rgba(255,255,255,.02)" '
         'stroke="rgba(237,234,227,.75)" stroke-width="2"/>'
         '<rect x="62" y="40" width="176" height="26" rx="4" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.35)" stroke-width="1.5"/>'
         '<rect x="62" y="86" width="176" height="96" rx="6" fill="rgba(0,0,0,.35)" stroke="rgba(180,227,61,.8)" stroke-width="2"/>'
         '<rect x="80" y="104" width="60" height="60" rx="4" fill="rgba(180,227,61,.75)"/>'
         '<rect x="152" y="104" width="66" height="60" rx="4" fill="rgba(237,234,227,.12)" stroke="rgba(237,234,227,.3)" stroke-width="1"/>'
         '<rect x="62" y="200" width="176" height="18" rx="3" fill="rgba(56,217,232,.75)"/>'
         '<rect x="62" y="230" width="176" height="18" rx="3" fill="rgba(56,217,232,.45)"/>'
         '<rect x="62" y="274" width="176" height="62" rx="6" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.35)" stroke-width="1.5"/>'
         '<text x="40" y="376" class="small">THE MACHINE</text></svg>')

SYSRAM = ('<svg viewBox="0 0 460 220" class="art">'
          '<rect x="20" y="30" width="420" height="160" rx="10" fill="rgba(255,255,255,.02)" '
          'stroke="rgba(237,234,227,.5)" stroke-width="2"/>'
          '<rect x="46" y="60" width="368" height="26" rx="4" fill="rgba(0,0,0,.4)" stroke="rgba(237,234,227,.5)" stroke-width="1.5"/>'
          '<rect x="46" y="100" width="368" height="26" rx="4" fill="rgba(56,217,232,.55)" stroke="rgba(56,217,232,.9)" stroke-width="1.5"/>'
          '<rect x="46" y="140" width="368" height="26" rx="4" fill="rgba(0,0,0,.4)" stroke="rgba(237,234,227,.5)" stroke-width="1.5"/>'
          '<text x="20" y="212" class="small">SYSTEM RAM</text></svg>')

PCIELINK = ('<svg viewBox="0 0 520 200" class="art">'
            '<rect x="16" y="40" width="150" height="120" rx="8" fill="rgba(255,255,255,.03)" '
            'stroke="rgba(180,227,61,.85)" stroke-width="2"/>'
            '<text x="16" y="186" class="small">VRAM</text>'
            '<rect x="354" y="40" width="150" height="120" rx="8" fill="rgba(255,255,255,.02)" '
            'stroke="rgba(237,234,227,.5)" stroke-width="2"/>'
            '<text x="354" y="186" class="small">SYSTEM RAM</text>'
            '<g stroke="rgba(232,72,61,.9)" stroke-width="2.5" fill="none">'
            '<path d="M176 78H344"/><path d="M336 70l10 8-10 8"/>'
            '<path d="M344 122H176"/><path d="M184 114l-10 8 10 8"/></g>'
            '<text x="214" y="66" class="small">PCIE</text></svg>')


DUALBOARD = ('<svg viewBox="0 0 480 260" class="art">'
             '<rect x="14" y="16" width="452" height="228" rx="10" fill="rgba(255,255,255,.02)" '
             'stroke="rgba(237,234,227,.5)" stroke-width="2"/>'
             '<rect x="40" y="52" width="400" height="30" rx="5" fill="rgba(180,227,61,.7)" stroke="rgba(180,227,61,.9)" stroke-width="1.5"/>'
             '<rect x="40" y="104" width="400" height="30" rx="5" fill="rgba(56,217,232,.65)" stroke="rgba(56,217,232,.9)" stroke-width="1.5"/>'
             '<rect x="40" y="160" width="180" height="56" rx="5" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.4)" stroke-width="1.5"/>'
             '<rect x="250" y="160" width="190" height="56" rx="5" fill="rgba(0,0,0,.35)" stroke="rgba(237,234,227,.4)" stroke-width="1.5"/>'
             '<text x="14" y="256" class="small">TWO SLOTS</text></svg>')

PSU = ('<svg viewBox="0 0 440 210" class="art">'
       '<rect x="16" y="26" width="408" height="148" rx="10" fill="rgba(255,255,255,.02)" '
       'stroke="rgba(237,234,227,.7)" stroke-width="2"/>'
       '<g class="spin"><circle cx="122" cy="100" r="46" fill="none" stroke="rgba(237,234,227,.55)" stroke-width="1.5"/>'
       '<path d="M122 60a40 40 0 0 1 0 80" fill="none" stroke="rgba(237,234,227,.3)" stroke-width="6"/>'
       '<circle cx="122" cy="100" r="8" fill="rgba(245,213,71,.9)"/></g>'
       '<rect x="212" y="56" width="176" height="16" rx="8" fill="rgba(245,213,71,.75)"/>'
       '<rect x="212" y="86" width="176" height="16" rx="8" fill="rgba(245,213,71,.55)"/>'
       '<rect x="212" y="116" width="120" height="16" rx="8" fill="rgba(232,72,61,.7)"/>'
       '<text x="16" y="196" class="small">POWER &middot; TWO CARDS</text></svg>')

RISER = ('<svg viewBox="0 0 480 180" class="art">'
          '<rect x="20" y="60" width="150" height="56" rx="6" fill="rgba(255,255,255,.04)" '
          'stroke="rgba(237,234,227,.7)" stroke-width="2"/>'
          '<path d="M176 74c60 -30 120 30 180 0" fill="none" stroke="rgba(245,213,71,.85)" stroke-width="10" stroke-linecap="round"/>'
          '<rect x="352" y="60" width="108" height="56" rx="6" fill="rgba(180,227,61,.6)" stroke="rgba(180,227,61,.9)" stroke-width="2"/>'
          '<text x="20" y="168" class="small">RISER &middot; ANOTHER BUS</text></svg>')

MINIPC = ('<svg viewBox="0 0 448 200" class="art">'
          '<rect x="60" y="40" width="320" height="120" rx="12" fill="rgba(255,255,255,.03)" '
          'stroke="rgba(237,234,227,.8)" stroke-width="2"/>'
          '<circle cx="120" cy="100" r="26" fill="none" stroke="rgba(237,234,227,.4)" stroke-width="1.5"/>'
          '<circle cx="120" cy="100" r="7" fill="rgba(245,213,71,.85)"/>'
          '<rect x="180" y="72" width="170" height="12" rx="6" fill="rgba(56,217,232,.8)"/>'
          '<rect x="180" y="96" width="130" height="10" rx="5" fill="rgba(237,234,227,.25)"/>'
          '<rect x="180" y="118" width="150" height="10" rx="5" fill="rgba(237,234,227,.25)"/>'
          '<text x="60" y="192" class="small">UNIFIED BOX</text></svg>')

LAPCUT = ('<svg viewBox="0 0 470 240" class="art">'
          '<rect x="60" y="30" width="340" height="150" rx="10" fill="rgba(255,255,255,.02)" '
          'stroke="rgba(237,234,227,.8)" stroke-width="2"/>'
          '<rect x="86" y="58" width="120" height="94" rx="6" fill="rgba(180,227,61,.55)" stroke="rgba(180,227,61,.9)" stroke-width="1.5"/>'
          '<rect x="220" y="58" width="154" height="94" rx="6" fill="rgba(56,217,232,.45)" stroke="rgba(56,217,232,.9)" stroke-width="1.5"/>'
          '<path d="M150 152h28" stroke="rgba(237,234,227,.6)" stroke-width="3"/>'
          '<text x="86" y="176" class="small">CPU</text>'
          '<text x="220" y="176" class="small">SHARED MEMORY</text>'
          '<path d="M30 208H430L400 190H60Z" fill="none" stroke="rgba(237,234,227,.8)" stroke-width="2"/>'
          '</svg>')

SODIMM = ('<svg viewBox="0 0 380 120" class="art">'
          '<rect x="10" y="24" width="360" height="64" rx="6" fill="rgba(255,255,255,.085)" '
          'stroke="rgba(237,234,227,.8)" stroke-width="2"/>'
          '<rect x="26" y="38" width="44" height="36" rx="3" fill="rgba(0,0,0,.4)" stroke="rgba(237,234,227,.4)" stroke-width="1"/>'
          '<rect x="80" y="38" width="44" height="36" rx="3" fill="rgba(0,0,0,.4)" stroke="rgba(237,234,227,.4)" stroke-width="1"/>'
          '<rect x="134" y="38" width="44" height="36" rx="3" fill="rgba(56,217,232,.75)"/>'
          '<rect x="188" y="38" width="44" height="36" rx="3" fill="rgba(0,0,0,.4)" stroke="rgba(237,234,227,.4)" stroke-width="1"/>'
          '<rect x="242" y="38" width="44" height="36" rx="3" fill="rgba(0,0,0,.4)" stroke="rgba(237,234,227,.4)" stroke-width="1"/>'
          '<rect x="296" y="38" width="58" height="36" rx="3" fill="rgba(245,213,71,.7)"/>'
          '<text x="10" y="112" class="small">SODIMM &middot; LAPTOP</text></svg>')

TWOGEN = ('<svg viewBox="0 0 530 240" class="art">'
          '<rect x="24" y="46" width="200" height="140" rx="10" fill="rgba(255,255,255,.02)" '
          'stroke="rgba(237,234,227,.6)" stroke-width="2"/>'
          '<rect x="70" y="86" width="108" height="62" rx="4" fill="rgba(237,234,227,.15)" stroke="rgba(237,234,227,.35)" stroke-width="1"/>'
          '<text x="24" y="216" class="small">3.6 &middot; OLDER</text>'
          '<rect x="296" y="46" width="200" height="140" rx="10" fill="rgba(255,255,255,.02)" '
          'stroke="rgba(232,72,61,.8)" stroke-width="2"/>'
          '<rect x="342" y="86" width="108" height="62" rx="4" fill="rgba(232,72,61,.55)"/>'
          '<text x="296" y="216" class="small">3.8 &middot; NEWER</text></svg>')

CLOCK = ('<svg viewBox="0 0 320 320" class="art">'
         '<circle cx="160" cy="160" r="118" fill="rgba(56,217,232,.09)" stroke="rgba(237,234,227,.65)" stroke-width="2"/>'
         '<circle cx="160" cy="160" r="6" fill="rgba(245,213,71,.95)"/>'
         '<g class="spin"><path d="M160 160V72" stroke="rgba(245,213,71,.9)" stroke-width="4" stroke-linecap="round"/></g>'
         '<path d="M160 160l62 34" stroke="rgba(237,234,227,.5)" stroke-width="3" stroke-linecap="round"/>'
         '<text x="30" y="308" class="small">TOKENS / SECOND</text></svg>')

WAFER = ('<svg viewBox="0 0 310 300" class="art">'
         '<circle cx="150" cy="150" r="126" fill="rgba(255,255,255,.06)" stroke="rgba(237,234,227,.7)" stroke-width="2"/>'
         + "".join(f'<rect x="{52+c*44}" y="{52+r*44}" width="34" height="34" rx="2" '
                   f'fill="{"rgba(180,227,61,.8)" if (r+c)%4==0 else "rgba(237,234,227,.08)"}" '
                   f'stroke="rgba(237,234,227,.2)" stroke-width="1"/>'
                   for r in range(4) for c in range(4))
         + '<text x="20" y="292" class="small">WAFER &middot; YIELD</text></svg>')

GAUGE = ('<svg viewBox="0 0 384 250" class="art">''<path d="M40 190 A150 150 0 0 1 340 190" fill="rgba(56,217,232,.10)" stroke="rgba(237,234,227,.6)" stroke-width="3"/>''<line x1="40.0" y1="190.0" x2="62.0" y2="190.0" stroke="rgba(237,234,227,.45)" stroke-width="3"/><line x1="47.3" y1="143.6" x2="68.3" y2="150.4" stroke="rgba(237,234,227,.45)" stroke-width="3"/><line x1="68.6" y1="101.8" x2="86.4" y2="114.8" stroke="rgba(237,234,227,.45)" stroke-width="3"/><line x1="101.8" y1="68.6" x2="114.8" y2="86.4" stroke="rgba(237,234,227,.45)" stroke-width="3"/><line x1="143.6" y1="47.3" x2="150.4" y2="68.3" stroke="rgba(237,234,227,.45)" stroke-width="3"/><line x1="190.0" y1="40.0" x2="190.0" y2="62.0" stroke="rgba(237,234,227,.45)" stroke-width="3"/><line x1="236.4" y1="47.3" x2="229.6" y2="68.3" stroke="rgba(237,234,227,.45)" stroke-width="3"/><line x1="278.2" y1="68.6" x2="265.2" y2="86.4" stroke="rgba(237,234,227,.45)" stroke-width="3"/><line x1="311.4" y1="101.8" x2="293.6" y2="114.8" stroke="rgba(237,234,227,.45)" stroke-width="3"/><line x1="332.7" y1="143.6" x2="311.7" y2="150.4" stroke="rgba(237,234,227,.45)" stroke-width="3"/><line x1="340.0" y1="190.0" x2="318.0" y2="190.0" stroke="rgba(237,234,227,.45)" stroke-width="3"/>''<line x1="190" y1="190" x2="254.7" y2="86.5" stroke="rgba(180,227,61,.95)" stroke-width="5" stroke-linecap="round"/>''<circle cx="190" cy="190" r="9" fill="rgba(245,213,71,.95)"/>''<text x="40" y="242" class="small">TOKENS PER SECOND</text></svg>')


SUPERCHIP = ('<svg viewBox="0 0 490 270" class="art">'
             '<rect x="18" y="24" width="454" height="200" rx="12" fill="rgba(255,255,255,.03)" '
             'stroke="rgba(237,234,227,.7)" stroke-width="2"/>'
             '<rect x="46" y="58" width="180" height="132" rx="6" fill="rgba(180,227,61,.75)" stroke="rgba(180,227,61,.95)" stroke-width="2"/>'
             '<text x="46" y="212" class="small">GPU</text>'
             '<rect x="252" y="58" width="188" height="60" rx="6" fill="rgba(56,217,232,.7)" stroke="rgba(56,217,232,.95)" stroke-width="2"/>'
             '<text x="252" y="212" class="small">CPU</text>'
             '<rect x="252" y="130" width="188" height="60" rx="6" fill="rgba(245,213,71,.55)" stroke="rgba(245,213,71,.9)" stroke-width="2"/>'
             '<text x="252" y="246" class="small">UNIFIED MEMORY</text>'
             '<path d="M232 124H248" stroke="rgba(237,234,227,.8)" stroke-width="4"/>'
             '<path d="M232 160H248" stroke="rgba(237,234,227,.8)" stroke-width="4"/></svg>')

# ---- v2 (layered, realistic) replaces the flat originals ----
from art2_lib import GPU2, RAM2, LAPTOP2, TOWER2, DIE2, WAFER2, ROUTER2
GPU, RAM, LAPTOP, TOWER, DIE, WAFER = GPU2, RAM2, LAPTOP2, TOWER2, DIE2, WAFER2
