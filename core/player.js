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

  /* numbers that count up when they land */
  function countUp(n) {
    const raw = n.dataset.count;
    const to = parseFloat(raw);
    if (!isFinite(to)) return;
    const dec = (raw.split('.')[1] || '').length;
    const suffix = n.dataset.suffix || '';
    const t0 = performance.now(), dur = 750;
    function step(t) {
      const k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      n.textContent = (to * e).toFixed(dec) + suffix;
      if (k < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  let lastTick = 0;

  function loop() {
    if (!playing) return;
    lastTick = performance.now();
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
      const d = parseFloat(n.dataset.in);
      // NaN guard: a malformed cue shows the element instead of hiding it forever
      if (!isFinite(d) || rel >= d) {
        if (!n.classList.contains('on')) {
          n.classList.add('on');
          if (n.dataset.count) countUp(n);
        }
      }
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
    const p = audio.play();
    if (p && p.then) {
      p.then(() => { playing = true; loop(); })
       .catch(() => { startEl.classList.remove('hide');
                      startEl.querySelector('.meta').textContent = 'CLICK AGAIN TO START AUDIO'; });
    } else { playing = true; loop(); }
  }

  function finish() {
    playing = false; cancelAnimationFrame(raf);
    barEl.style.width = '100%';
    startEl.classList.remove('hide');
    startEl.querySelector('.s').textContent = 'End of episode';
    startEl.querySelector('.meta').textContent = 'REPLAY';
  }

  /* ---------- deterministic frame renderer (used by CI) ---------- */
  const _q = new URLSearchParams(location.search);
  if (_q.has('t')) { document.body.classList.add('render'); }


  window.renderAt = function (t) {
    document.documentElement.style.setProperty('--anim-delay', (-t).toFixed(3) + 's');
    // deterministic ambient motion: state is a pure function of t
    document.querySelectorAll('.spin').forEach((el, k) => {
      el.style.transform = 'rotate(' + ((t * 132 + k * 40) % 360).toFixed(2) + 'deg)';
      el.style.transformBox = 'fill-box';
      el.style.transformOrigin = 'center';
    });
    document.querySelectorAll('.float').forEach((el, k) => {
      el.style.transform = 'translateY(' + (Math.sin(t * 1.1 + k) * 7).toFixed(2) + 'px)';
    });
    document.querySelectorAll('.pulse').forEach((el, k) => {
      el.style.opacity = (0.62 + 0.38 * (0.5 + 0.5 * Math.sin(t * 1.7 + k))).toFixed(3);
    });
    let idx = 0;
    for (let i = 0; i < SCENES.length; i++) if (t >= SCENES[i].s) idx = i;
    scenesEl.forEach((sc, k) => sc.classList.toggle('active', k === idx));
    const sc = SCENES[idx], rel = t - sc.s, el = scenesEl[idx];
    if (!el) return;
    el.querySelectorAll('[data-in]').forEach(n => {
      const d = parseFloat(n.dataset.in);
      if (!isFinite(d) || rel >= d) n.classList.add('on');
      else n.classList.remove('on');
    });
    document.getElementById('start').classList.add('hide');
    // colour wipe: replay it analytically so renders match playback
    const wp = (E.wipes || []).find(w => t >= w && t <= w + 0.62);
    if (wp) {
      const pr = (t - wp) / 0.62;
      wipeEl.style.display = 'flex';
      wipeEl.style.transform = 'translateX(' + (-103 + pr * 206) + '%)';
    } else {
      wipeEl.style.display = 'none';
    }
  };

  if (_q.has('t')) {
    const _t = parseFloat(_q.get('t')) || 0;
    requestAnimationFrame(() => window.renderAt(_t));
  }

  /* rAF stops when the tab is backgrounded or the window is occluded.
     Audio keeps playing, so the picture freezes. Poll audio time with a timer
     as a safety net, and resync the moment the page becomes visible again. */
  setInterval(() => {
    if (!playing) return;
    if (performance.now() - lastTick > 400) {
      cancelAnimationFrame(raf);
      loop();
    }
  }, 250);

  /* normalise art shapes so one dash animation draws any size of path */
  document.querySelectorAll('.art path,.art rect,.art circle,.art line,.art polyline')
    .forEach(el => { if (!el.hasAttribute('pathLength')) el.setAttribute('pathLength','100'); });

  document.addEventListener('visibilitychange', () => {
    if (!document.hidden && playing) { cancelAnimationFrame(raf); loop(); }
  });

  /* ?debug=1 shows a live readout so a freeze can be reported precisely */
  if (new URLSearchParams(location.search).has('debug')) {
    const box = document.createElement('div');
    box.style.cssText = 'position:absolute;left:12px;top:12px;z-index:200;font:14px monospace;' +
      'color:#6f6;background:rgba(0,0,0,.75);padding:6px 10px;border:1px solid #333';
    stage.appendChild(box);
    setInterval(() => {
      box.textContent = 't=' + audio.currentTime.toFixed(1) + '  scene=' + (last + 1) +
        '  playing=' + playing + '  hidden=' + document.hidden;
    }, 200);
  }

  startEl.addEventListener('click', () => { if (!playing) togglePlay(); });

  /* ---------- playback controls: play / stop / speed (hidden when rendering) ---------- */
  let playBtn = null;
  const RATES = [1, 1.5, 2, 4];

  function togglePlay() {
    if (playing) {
      audio.pause(); playing = false; cancelAnimationFrame(raf);
      if (playBtn) playBtn.textContent = '\u25B6';
      startEl.classList.add('hide');
      return;
    }
    if (audio.currentTime >= (E.total || 1e9) - 0.05) { reset(); audio.currentTime = 0; }
    startEl.classList.add('hide');
    const pr = audio.play();
    const go = () => { playing = true; if (playBtn) playBtn.textContent = '\u2016'; loop(); };
    if (pr && pr.then) pr.then(go).catch(() => { if (playBtn) playBtn.textContent = '\u25B6'; });
    else go();
  }

  function stopPlayback() {
    audio.pause(); playing = false; cancelAnimationFrame(raf);
    audio.currentTime = 0;
    reset();
    window.renderAt(0);
    startEl.classList.remove('hide');
    if (playBtn) playBtn.textContent = '\u25B6';
    const meta = startEl.querySelector('.meta');
    if (meta) meta.textContent = 'CLICK TO START';
  }

  function setRate(r) {
    audio.playbackRate = r;
    document.querySelectorAll('#ctl .rate').forEach(b =>
      b.classList.toggle('on', parseFloat(b.dataset.r) === r));
  }

  if (!document.body.classList.contains('render')) {
    const ctl = document.createElement('div');
    ctl.id = 'ctl';
    ctl.innerHTML = '<button id="ctlPlay" title="Play / Pause  (Space)">\u25B6</button>' +
      '<button id="ctlStop" title="Stop  (S)">\u25A0</button><span class="sep"></span>' +
      RATES.map(r => '<button class="rate" data-r="' + r + '">' + r + '\u00D7</button>').join('');
    document.body.appendChild(ctl);
    playBtn = ctl.querySelector('#ctlPlay');
    playBtn.addEventListener('click', togglePlay);
    ctl.querySelector('#ctlStop').addEventListener('click', stopPlayback);
    ctl.querySelectorAll('.rate').forEach(b =>
      b.addEventListener('click', () => setRate(parseFloat(b.dataset.r))));
    setRate(1);
  }

  addEventListener('keydown', e => {
    if (e.target && /INPUT|TEXTAREA/.test(e.target.tagName)) return;
    if (e.code === 'Space') { e.preventDefault(); togglePlay(); }
    else if (e.key === 's' || e.key === 'S') stopPlayback();
    else if (e.key >= '1' && e.key <= '4') setRate(RATES[+e.key - 1]);
    else if (e.code === 'ArrowRight') audio.currentTime = Math.min((E.total || 0) - 0.1, audio.currentTime + 5);
    else if (e.code === 'ArrowLeft') audio.currentTime = Math.max(0, audio.currentTime - 5);
  });
})();
