document.documentElement.classList.remove("no-js");


window.EPISODE = {
  kicker: "Episode 03",
  title: "Two Users, Half the Speed",
  subtitle: "Concurrency · local AI",
  total: 31.20,
  vo: "audio/ep03_vo.mp3",
  sfxBase: "audio/",
  labels: ['01 HOOK', '02 WHY', '03 THE CACHE', '04 THE MATH', '05 THE FIX', '06 VERDICT'],
  scenes: [
  {s: 0.00,  e: 4.71},
  {s: 4.96,  e:12.42},
  {s:12.67,  e:16.93},
  {s:17.18,  e:21.76},
  {s:22.01,  e:27.25},
  {s:27.50,  e:30.50}
  ],
  wipes: [16.898, 27.215],
  wipeColors: ['blue', 'yellow'],
  sfx: [
  {t: 0.100, f:'tick'},
  {t: 1.956, f:'thud'},
  {t: 5.056, f:'tick'},
  {t:12.768, f:'tick'},
  {t:16.898, f:'whoosh'},
  {t:17.283, f:'tick'},
  {t:18.706, f:'tick'},
  {t:20.019, f:'tick'},
  {t:20.892, f:'tick'},
  {t:22.115, f:'tick'},
  {t:27.215, f:'whoosh'},
  {t:27.600, f:'thud'},
  ]
};



/* ============================================================
   KAI PLAYER — timeline engine
   Each episode sets:
     window.EPISODE = {
       title, kicker, subtitle,
       total: 42.72,
       scenes: [{s,e}, ...],
       wipes:  [20.355, 35.885],        // absolute; full cover lands at t+0.285
       sfx:    [{t, f:'tick'|'whoosh'|'thud'}, ...],
       labels: ['01 HOOK', '02 ...'],   // HUD cue text per scene
       vo:     'audio/vo.mp3',
       sfxBase:'../../audio/'           // where tick/whoosh/thud live
     }
   ============================================================ */
(function () {
  const E = window.EPISODE;
  const stage = document.getElementById('stage');

  /* ---------- inject chrome so episode files stay small ---------- */
  const mk = (tag, attrs, html) => {
    const el = document.createElement(tag);
    for (const k in attrs) el.setAttribute(k, attrs[k]);
    if (html != null) el.innerHTML = html;
    return el;
  };
  stage.appendChild(mk('div', {id: 'wipe'}, '<span></span><span></span><span></span><span></span><span></span><span></span><span></span>'));
  stage.appendChild(mk('div', {id: 'hud'}, '<div id="bar"></div>'));
  stage.appendChild(mk('div', {id: 'tc'}, '0.0 / ' + E.total.toFixed(1)));
  stage.appendChild(mk('div', {id: 'cue'}, ''));
  stage.appendChild(mk('div', {id: 'start'},
    '<div class="k">' + (E.kicker || '') + '</div>' +
    '<div class="t">' + (E.title || '') + '</div>' +
    '<div id="play"><svg width="44" height="50" viewBox="0 0 44 50"><path d="M0 0 L44 25 L0 50 Z" fill="#F6F6F4"/></svg></div>' +
    '<div class="s">' + (E.subtitle || '') + '</div>' +
    '<div class="meta">CLICK TO PLAY · VOICE + SOUND</div>'));

  const audio = mk('audio', {id: 'vo', src: E.vo || 'audio/vo.mp3', preload: 'auto'});
  stage.appendChild(audio);
  const base = E.sfxBase || '../../audio/';
  ['tick', 'whoosh', 'thud'].forEach(n => {
    stage.appendChild(mk('audio', {id: 'sfx-' + n, src: base + n + '.mp3', preload: 'auto'}));
  });

  /* ---------- refs ---------- */
  const scenesEl = [...document.querySelectorAll('.scene')];
  const startEl = document.getElementById('start');
  const barEl = document.getElementById('bar');
  const tcEl = document.getElementById('tc');
  const cueEl = document.getElementById('cue');
  const wipeEl = document.getElementById('wipe');
  const sfxEl = {tick: document.getElementById('sfx-tick'),
                 whoosh: document.getElementById('sfx-whoosh'),
                 thud: document.getElementById('sfx-thud')};
  const SCENES = E.scenes, TOTAL = E.total, LABELS = E.labels || [];

  /* ---------- fit 1920x1080 into any window ---------- */
  const fit = () => {};   /* scaling is pure CSS now */
  addEventListener('resize', fit); fit();

  let playing = false, raf = null, last = -1, fired = new Set(), wiped = new Set();

  function reset() {
    fired.clear(); wiped.clear(); last = -1;
    scenesEl.forEach(s => s.classList.remove('active'));
    document.querySelectorAll('[data-in]').forEach(el => el.classList.remove('on'));
    document.querySelectorAll('.grow').forEach(el => el.classList.remove('on'));
    wipeEl.classList.remove('go');
    barEl.style.width = '0%';
  }

  /* number tween driven by the audio clock is not needed — values are set by hooks */
  window.epTween = function (from, to, ms, cb) {
    const t0 = performance.now();
    (function step() {
      const k = Math.min((performance.now() - t0) / ms, 1);
      cb(Math.round(from + (to - from) * (1 - Math.pow(1 - k, 2))));
      if (k < 1) requestAnimationFrame(step);
    })();
  };

  function loop() {
    if (!playing) return;
    const t = audio.currentTime;

    /* scene index — clamp to the last scene that has started (no gap flash) */
    let idx = 0;
    for (let i = 0; i < SCENES.length; i++) if (t >= SCENES[i].s) idx = i;

    if (idx !== last) {
      scenesEl.forEach((sc, k) => sc.classList.toggle('active', k === idx));
      last = idx;
      cueEl.textContent = LABELS[idx] || '';
    }

    const sc = SCENES[idx], rel = t - sc.s;
    const el = scenesEl[idx];
    if (el) el.querySelectorAll('[data-in]').forEach(n => {
      if (rel >= parseFloat(n.dataset.in)) n.classList.add('on');
    });

    /* per-episode hooks: window.epScene(idx, rel, fired) */
    if (window.epScene) window.epScene(idx, rel, fired);

    E.wipes.forEach((w, k) => {
      if (t >= w && !wiped.has(k)) {
        wiped.add(k);
        wipeEl.classList.toggle('blue', !!(E.wipeColors && E.wipeColors[k] === 'blue'));
        wipeEl.classList.remove('go'); void wipeEl.offsetWidth; wipeEl.classList.add('go');
      }
    });

    E.sfx.forEach((c, k) => {
      if (t >= c.t && !fired.has('s' + k)) {
        fired.add('s' + k);
        const s = sfxEl[c.f];
        if (s) { s.currentTime = 0; s.volume = c.f === 'tick' ? 0.22 : 0.30; s.play().catch(() => {}); }
      }
    });

    barEl.style.width = (t / TOTAL * 100) + '%';
    tcEl.textContent = t.toFixed(1) + ' / ' + TOTAL.toFixed(1);

    if (t >= TOTAL - 0.02) { finish(); return; }
    raf = requestAnimationFrame(loop);
  }

  function begin() {
    reset();
    startEl.classList.add('hide');
    audio.currentTime = 0;
    audio.play().then(() => { playing = true; loop(); })
         .catch(() => { cueEl.textContent = 'AUDIO BLOCKED — click again'; });
  }

  function finish() {
    playing = false; cancelAnimationFrame(raf);
    barEl.style.width = '100%';
    startEl.classList.remove('hide');
    startEl.querySelector('.s').textContent = 'End of episode';
    startEl.querySelector('.meta').textContent = 'REPLAY';
  }

  startEl.addEventListener('click', () => { if (!playing) begin(); });
  addEventListener('keydown', e => {
    if (e.code === 'Space') {
      e.preventDefault();
      if (!playing) begin();
      else { audio.pause(); playing = false; cancelAnimationFrame(raf); }
    }
  });
})();


