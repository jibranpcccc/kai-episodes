/* ============================================================
   FUSION — Byte Forensics runtime
   ------------------------------------------------------------
   The episode is DATA. This file never contains content; it only
   plays what core/fusion.css draws and what window.FUSION says.

   window.FUSION = {
     title, kicker, subtitle, total,
     words : [ {t, w} ],              // full word timeline (audit trail)
     scenes: [ {id, s, e, label} ],   // absolute seconds
     beats : [ {i,s,e,el,kind,dur,ease,group,anchor,nudge,
                count?,fill?,cdur?,fdur?} ],
     wipes : [ ... ], sfx: [ ... ], vo: '<base64 mp3>'
   }

   Design rules baked in here:
     * the AUDIO CLOCK is authoritative. Every animation is driven from
       audio.currentTime, so a stalled buffer can never desync the picture.
     * one easing curve drives the transform, the count-up and the bar fill,
       so they can never disagree.
     * renderAt(t) is the SAME code path as playback -> CI frames are exact.
     * motion only ever touches HTML wrappers. SVG art moves via its
       wrapper, stroke-dashoffset or opacity (never `transform` on an
       element that carries a transform attribute).
   ============================================================ */
(function () {
  'use strict';

  var F = window.FUSION;
  if (!F) { console.error('FUSION: window.FUSION missing'); return; }

  var stage = document.getElementById('stage');
  if (!stage) { console.error('FUSION: #stage missing'); return; }

  var SCENES = F.scenes || [];
  var BEATS  = F.beats  || [];
  var TOTAL  = F.total  || 0;

  /* ==========================================================
     1. EASING — one curve, shared by every channel
     ========================================================== */
  function bezier(cx1, cy1, cx2, cy2) {
    if (cx1 === cy1 && cx2 === cy2) return function (t) { return t; };
    var A = function (a, b) { return 1 - 3 * b + 3 * a; };
    var B = function (a, b) { return 3 * b - 6 * a; };
    var C = function (a) { return 3 * a; };
    var calc = function (t, a, b) { return ((A(a, b) * t + B(a, b)) * t + C(a)) * t; };
    var slope = function (t, a, b) { return 3 * A(a, b) * t * t + 2 * B(a, b) * t + C(a); };
    return function (x) {
      if (x <= 0) return 0;
      if (x >= 1) return 1;
      var t = x, e, d, i;
      for (i = 0; i < 8; i++) {
        d = slope(t, cx1, cx2);
        if (d === 0) break;
        e = calc(t, cx1, cx2) - x;
        if (Math.abs(e) < 1e-7) return calc(t, cy1, cy2);
        t -= e / d;
      }
      var lo = 0, hi = 1; t = x;
      for (i = 0; i < 24; i++) {
        e = calc(t, cx1, cx2) - x;
        if (Math.abs(e) < 1e-7) break;
        if (e > 0) hi = t; else lo = t;
        t = (lo + hi) / 2;
      }
      return calc(t, cy1, cy2);
    };
  }

  var EASE = {
    rise:  bezier(.20, .80, .20, 1),
    slam:  bezier(.16, 1.10, .30, 1),
    pop:   bezier(.34, 1.56, .64, 1),
    sticker: bezier(.20, 1.40, .40, 1),
    draw:  bezier(.42, .00, .24, 1),
    wipe:  bezier(.70, .00, .30, 1),
    fill:  bezier(.25, .80, .25, 1),
    count: bezier(.25, .80, .25, 1),
    push:  bezier(.30, .70, .30, 1),
    nudge: bezier(.34, 1.56, .64, 1),
    card:  bezier(.22, 1.20, .36, 1),
    edge:  bezier(.16, 1.00, .30, 1),
    linear: function (t) { return t; }
  };
  function easeFn(name) { return EASE[name] || EASE.rise; }

  /* ==========================================================
     2. MOTION VOCABULARY — keyframes per primitive
     ========================================================== */
  var KF = {
    rise: {
      d: 340,
      kf: [
        { o: 0, opacity: 0, visibility: 'hidden', transform: 'translateY(14px) scale(.975)' },
        { o: 1, opacity: 1, visibility: 'visible', transform: 'none' }
      ]
    },
    slam: {
      d: 460,
      kf: [
        { o: 0, opacity: 0, visibility: 'hidden', transform: 'translateY(-30px) scale(1.12)' },
        { o: 1, opacity: 1, visibility: 'visible', transform: 'none' }
      ]
    },
    pop: {
      d: 420,
      kf: [
        { o: 0,    opacity: 0, visibility: 'hidden', transform: 'scale(.80)' },
        { o: 0.62, opacity: 1, visibility: 'visible', transform: 'scale(1.07)' },
        { o: 1,    opacity: 1, visibility: 'visible', transform: 'scale(1)' }
      ]
    },
    sticker: {
      d: 380,
      kf: [
        { o: 0, opacity: 0, visibility: 'hidden', transform: 'rotate(-16deg) translateY(12px)' },
        { o: 1, opacity: 1, visibility: 'visible', transform: 'rotate(-5deg) translateY(0)' }
      ]
    },
    wipe: {
      d: 520,
      kf: [
        { o: 0, opacity: 1, visibility: 'visible', clipPath: 'inset(0 100% 0 0)' },
        { o: 1, opacity: 1, visibility: 'visible', clipPath: 'inset(0 0 0 0)' }
      ]
    },
    nudge: {
      d: 300,
      kf: [
        { o: 0, opacity: 0, visibility: 'hidden', transform: 'translateX(-14px)' },
        { o: 1, opacity: 1, visibility: 'visible', transform: 'none' }
      ]
    },
    /* 'count' fades the value in; the digits are driven by the runtime */
    count: {
      d: 340,
      kf: [
        { o: 0, opacity: 0, visibility: 'hidden', transform: 'translateY(8px)' },
        { o: 1, opacity: 1, visibility: 'visible', transform: 'none' }
      ]
    },
    /* 'sweep' fades the bar row in; the fill is driven by the runtime */
    sweep: {
      d: 340,
      kf: [
        { o: 0, opacity: 0, visibility: 'hidden', transform: 'translateX(-18px)' },
        { o: 1, opacity: 1, visibility: 'visible', transform: 'none' }
      ]
    },
    /* 'card' lands with a real spring overshoot */
    card: {
      d: 420,
      kf: [
        { o: 0, opacity: 0, visibility: 'hidden', transform: 'translateY(22px) scale(.95) rotate(-1deg)' },
        { o: 1, opacity: 1, visibility: 'visible', transform: 'none' }
      ]
    },
    /* 'edge' slides in from the left edge of its column */
    edge: {
      d: 380,
      kf: [
        { o: 0, opacity: 0, visibility: 'hidden', transform: 'translateX(-34px)' },
        { o: 1, opacity: 1, visibility: 'visible', transform: 'none' }
      ]
    },
    /* 'wipein' wipes the card on, border and content together */
    wipein: {
      d: 460,
      kf: [
        { o: 0, opacity: 1, visibility: 'visible', clipPath: 'inset(0 100% 0 0)' },
        { o: 1, opacity: 1, visibility: 'visible', clipPath: 'inset(0 0 0 0)' }
      ]
    }
  };

  /* ==========================================================
     3. AMBIENT — analytic, so frame N is always frame N
     ========================================================== */
  function applyAmbient(t) {
    var els = stage.querySelectorAll('[data-amb]');
    for (var i = 0; i < els.length; i++) {
      var el = els[i], m = el.getAttribute('data-amb');
      var kv = el.getAttribute('data-amb-k');
      var k = (kv === null) ? i : (+kv || 0);
      if (m === 'blink') {
        el.style.opacity = (Math.sin(t * 5.4) > -0.15) ? '1' : '0.12';
      } else if (m === 'pulse') {
        var pv = +el.getAttribute('data-amb-speed') || 1;
        el.style.opacity = (0.60 + 0.40 * (0.5 + 0.5 * Math.sin(t * 1.9 * pv + k))).toFixed(3);
      } else if (m === 'spin' || m === 'sway') {
        var sp = +el.getAttribute('data-amb-speed') || 1;
        var base = +el.getAttribute('data-amb-base') || 0;
        var ampAttr = el.getAttribute('data-amb-amp');
        var ang;
        if (ampAttr !== null) {
          /* A BOUNDED OSCILLATION. A needle that lives inside a dial must
             never sweep out of it: a full 360 spin carries the pointer
             below the arc and off the drawing. The amplitude is in degrees
             and swings around the drawn position. */
          ang = base + (+ampAttr) * Math.sin(t * sp + k);
        } else if (m === 'sway') {
          ang = base + 8 * Math.sin(t * sp + k);
        } else {
          ang = (t * 132 * sp + k * 40) % 360;
        }
        el.style.transform = 'rotate(' + ang.toFixed(2) + 'deg)';
        el.style.transformBox = el.getAttribute('data-amb-box') || 'fill-box';
        el.style.transformOrigin = el.getAttribute('data-amb-origin') || 'center';
      } else if (m === 'float') {
        el.style.transform = 'translateY(' + (Math.sin(t * 1.1 + k) * 8).toFixed(2) + 'px)';
      }
    }
  }

  /* ==========================================================
     4. BEATS -> ANIMATIONS
     ========================================================== */
  var anims = [];

  function buildAnimations() {
    for (var i = 0; i < BEATS.length; i++) {
      var b = BEATS[i];
      var el = document.querySelector(b.el);
      if (!el) { console.error('FUSION: beat target missing', b.el, b.i); continue; }
      b._el = el;
      b._ease = easeFn(b.ease || 'rise');

      if (b.kind === 'push') {
        /* a persistent camera move, not a one-shot reveal */
        b._push = true;
        continue;
      }
      if (b.kind === 'draw') {
        /* the line art sketches itself on: every stroke draws via
           stroke-dashoffset, staggered, and the filled shapes fade in
           alongside it. Filled-only shapes have no stroke, so they get
           the opacity fade instead of a dash.

           The stagger follows READING ORDER, not DOM order, so a marker
           never lands before the line that leads to it. A shape can
           override its own delay with data-draw-delay (seconds). */
        var shapes = el.querySelectorAll('path, rect, circle, line, polyline, polygon, ellipse, text');
        b._shapes = shapes;
        if (!shapes.length) { console.error('FUSION: draw target has no shapes', b.el); continue; }
        var STAG = 42;
        var SPREAD = 900;
        var frame = null;
        try { frame = el.getBBox(); } catch (e) { frame = null; }
        var fw = (frame && frame.width) ? frame.width : 1;
        var fh = (frame && frame.height) ? frame.height : 1;
        var fx = (frame && frame.width) ? frame.x : 0;
        var fy = (frame && frame.height) ? frame.y : 0;

        for (var j = 0; j < shapes.length; j++) {
          var p = shapes[j];
          var st = p.getAttribute('stroke');
          var hasStroke = !!(st && st !== 'none');

          /* where this shape starts, for reading order */
          var ax = null, ay = null;
          if (p.getPointAtLength) {
            try { var pt = p.getPointAtLength(0); ax = pt.x; ay = pt.y; } catch (e) { ax = null; }
          }
          if (ax === null && p.getBBox) {
            try { var bb = p.getBBox(); ax = bb.x + bb.width / 2; ay = bb.y + bb.height / 2; } catch (e) { ax = null; }
          }
          var delay;
          var od = p.getAttribute('data-draw-delay');
          if (od !== null) {
            delay = parseFloat(od) * 1000;
          } else if (ax !== null) {
            var nx = Math.max(0, Math.min(1, (ax - fx) / fw));
            var ny = Math.max(0, Math.min(1, (ay - fy) / fh));
            delay = (0.55 * nx + 0.45 * ny) * SPREAD + (j % 3) * 12;
          } else {
            delay = j * STAG;
          }
          delay = Math.max(0, Math.min(delay, SPREAD));

          if (hasStroke) {
            var len = 1000;
            if (p.getTotalLength) {
              try { len = Math.ceil(p.getTotalLength()) || 1000; } catch (e) { len = 1000; }
            }
            p.removeAttribute('pathLength');
            var dstr = (len + 2) + ' ' + (len * 2);
            p._dash = dstr;
            p.style.strokeDasharray = dstr;
            var a = p.animate(
              [{ strokeDashoffset: len + 2 }, { strokeDashoffset: 0 }],
              { duration: b.dur || 1500, easing: 'linear', fill: 'both', delay: delay }
            );
            a.pause();
            (b._anims = b._anims || []).push(a);
          }
          var a2 = p.animate(
            [{ opacity: 0 }, { opacity: 1 }],
            { duration: Math.round((b.dur || 1500) * 0.45), easing: 'linear', fill: 'both', delay: delay }
          );
          a2.pause();
          (b._anims = b._anims || []).push(a2);
        }
        continue;
      }

      var def = KF[b.kind] || KF.rise;
      var a2 = el.animate(def.kf, {
        duration: b.dur || def.d,
        easing: 'linear',        /* the curve is applied by the runtime */
        fill: 'both'
      });
      a2.pause();
      b._anim = a2;

      if (b.count) {
        b._countEl = document.querySelector(b.count.sel || (b.el + ' [data-count]'));
        if (b._countEl) {
          b._countEl.setAttribute('data-counted', '1');
          b._countFrom = b.count.from != null ? b.count.from : 0;
          b._countTo = b.count.to;
          b._countDec = b.count.dec || 0;
          b._countPrefix = b.count.prefix || '';
          b._countSuffix = b.count.suffix || '';
          b._countEl.textContent = b._countPrefix + fmt(b._countFrom, b._countDec) + b._countSuffix;
        }
      }
      if (b.fill) {
        b._fillEl = document.querySelector(b.fill.sel || (b.el + ' .bar__fill'));
        if (b._fillEl) b._fillEl.style.width = '0%';
      }
    }
  }

  function fmt(v, dec) {
    var s = dec > 0 ? v.toFixed(dec) : String(Math.round(v));
    var parts = s.split('.');
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return parts.join('.');
  }

  /* ==========================================================
     5. ONE STATE FUNCTION — playback and render share it
     ========================================================== */
  var sceneEls = [].slice.call(document.querySelectorAll('.scene'));
  var lastIdx = -1;

  function sceneAt(t) {
    var idx = 0;
    for (var i = 0; i < SCENES.length; i++) if (t >= SCENES[i].s) idx = i;
    return idx;
  }

  function dipOpacity(t) {
    var o = 0;
    for (var i = 1; i < SCENES.length; i++) {
      var B = SCENES[i].s;
      if (t >= B - 0.12 && t < B) o = Math.max(o, (t - (B - 0.12)) / 0.12);
      else if (t >= B && t < B + 0.22) o = Math.max(o, 1 - (t - B) / 0.22);
    }
    return o;
  }

  function renderState(t) {
    F.__t = t;
    /* --- scene --- */
    var idx = sceneAt(t);
    if (idx !== lastIdx) {
      for (var i = 0; i < sceneEls.length; i++) sceneEls[i].classList.toggle('on', i === idx);
      if (cueEl) cueEl.textContent = (SCENES[idx] && SCENES[idx].label) || '';
      lastIdx = idx;
    }

    /* --- beats ---
       beat.s / beat.e are SECONDS. beat.dur / cdur / fdur are MILLISECONDS.
       Everything below converts once, at the top, so the two can never mix. */
    for (var k = 0; k < BEATS.length; k++) {
      var b = BEATS[k];
      var durS = (b.dur || 340) / 1000;

      if (b._push) {
        /* the camera settles as the sketch completes */
        var pw = Math.max(0, Math.min(1, (t - b.s) / durS));
        var pe = b._ease(pw);
        var pfrom = b.from != null ? b.from : 0.97;
        var pto = b.to != null ? b.to : 1.03;
        b._el.style.transform = 'scale(' + (pfrom + (pto - pfrom) * pe).toFixed(4) + ')';
        b._el.style.transformOrigin = '50% 50%';
        continue;
      }

      if (b._anims) {
        var pd = Math.max(0, Math.min(1, (t - b.s) / durS));
        var ed = b._ease(pd);
        for (var m = 0; m < b._anims.length; m++) b._anims[m].currentTime = ed * (b.dur || 850);
        if (b._shapes) {
          if (pd >= 1.0) {
            for (var s = 0; s < b._shapes.length; s++) b._shapes[s].style.strokeDasharray = 'none';
          } else {
            for (var s = 0; s < b._shapes.length; s++) if (b._shapes[s]._dash) b._shapes[s].style.strokeDasharray = b._shapes[s]._dash;
          }
        }
      }
      if (b._anim) {
        var p = Math.max(0, Math.min(1, (t - b.s) / durS));
        b._anim.currentTime = b._ease(p) * (b.dur || 340);
      }

      if (b._countEl) {
        var cd = (b.cdur || 900) / 1000;
        var cp = Math.max(0, Math.min(1, (t - b.s) / cd));
        var ce = easeFn('count')(cp);
        var v = b._countFrom + (b._countTo - b._countFrom) * ce;
        b._countEl.textContent = b._countPrefix + fmt(v, b._countDec) + b._countSuffix;
      }
      if (b._fillEl) {
        /* the fill starts a beat after the row lands, so the number reads
           as the payoff rather than noise */
        var fd = (b.fdur || 900) / 1000;
        var fstart = b.s + (b.fd || 0);
        var fp = Math.max(0, Math.min(1, (t - fstart) / fd));
        var fe = easeFn('fill')(fp);
        b._fillEl.style.width = (b.fill.w * fe).toFixed(3) + '%';
      }
    }

    applyAmbient(t);

    if (dipEl) dipEl.style.opacity = dipOpacity(t).toFixed(3);
    if (barEl) barEl.style.width = (TOTAL ? (t / TOTAL * 100) : 0).toFixed(3) + '%';
    if (gprogEl) gprogEl.style.width = (TOTAL ? (t / TOTAL * 100) : 0).toFixed(3) + '%';
    if (tcEl) tcEl.textContent = t.toFixed(1) + ' / ' + TOTAL.toFixed(1);
  }

  /* ==========================================================
     6. CHROME
     ========================================================== */
  function mk(tag, attrs, html) {
    var el = document.createElement(tag);
    for (var k in attrs) el.setAttribute(k, attrs[k]);
    if (html != null) el.innerHTML = html;
    return el;
  }

  stage.appendChild(mk('div', { id: 'dip' }));
  if (F.progress) stage.appendChild(mk('div', { id: 'gprog' }));
  stage.appendChild(mk('div', { id: 'hud' }, '<div id="bar"></div>'));
  stage.appendChild(mk('div', { id: 'tc' }, '0.0 / ' + TOTAL.toFixed(1)));
  stage.appendChild(mk('div', { id: 'cue' }, ''));
  stage.appendChild(mk('div', { id: 'wm' }, F.watermark || 'Byte Forensics'));
  stage.appendChild(mk('div', { id: 'start' },
    '<div class="k">' + (F.kicker || '') + '</div>' +
    '<div class="t">' + (F.title || '') + '</div>' +
    '<div id="play"><svg width="46" height="52" viewBox="0 0 44 50"><path d="M0 0 L44 25 L0 50 Z" fill="#F5C531"/></svg></div>' +
    '<div class="s">' + (F.subtitle || '') + '</div>' +
    '<div class="meta">CLICK TO PLAY &middot; VOICE + SOUND</div>'));

  var audio = mk('audio', { id: 'vo', src: F.vo, preload: 'auto' });
  stage.appendChild(audio);
  (F.sfxBase ? [F.sfxBase] : []).forEach(function (base) {
    ['tick', 'whoosh', 'thud'].forEach(function (n) {
      stage.appendChild(mk('audio', { id: 'sfx-' + n, src: base + n + '.mp3', preload: 'auto' }));
    });
  });

  var dipEl = document.getElementById('dip');
  var gprogEl = document.getElementById('gprog');
  var barEl = document.getElementById('bar');
  var tcEl  = document.getElementById('tc');
  var cueEl = document.getElementById('cue');
  var startEl = document.getElementById('start');

  buildAnimations();

  /* ==========================================================
     7. PLAYBACK
     ========================================================== */
  var playing = false, raf = null, lastTick = 0, fired = {};

  function loop() {
    if (!playing) return;
    lastTick = performance.now();
    var t = audio.currentTime;
    renderState(t);

    if (F.sfx) {
      for (var i = 0; i < F.sfx.length; i++) {
        var c = F.sfx[i];
        if (t >= c.t && !fired['s' + i]) {
          fired['s' + i] = 1;
          var s = document.getElementById('sfx-' + c.f);
          if (s) { s.currentTime = 0; s.volume = c.f === 'tick' ? 0.20 : 0.28; s.play().catch(function () {}); }
        }
      }
    }

    if (t >= TOTAL - 0.02) { finish(); return; }
    raf = requestAnimationFrame(loop);
  }

  function begin() {
    lastIdx = -1; fired = {};
    startEl.classList.add('hide');
    audio.currentTime = 0;
    var p = audio.play();
    if (p && p.then) {
      p.then(function () { playing = true; loop(); })
       .catch(function () {
         startEl.classList.remove('hide');
         startEl.querySelector('.meta').textContent = 'CLICK AGAIN TO START AUDIO';
       });
    } else { playing = true; loop(); }
  }

  function finish() {
    playing = false; cancelAnimationFrame(raf);
    if (barEl) barEl.style.width = '100%';
    startEl.classList.remove('hide');
    startEl.querySelector('.s').textContent = 'End of segment';
    startEl.querySelector('.meta').textContent = 'REPLAY';
  }

  function togglePlay() {
    if (playing) {
      audio.pause(); playing = false; cancelAnimationFrame(raf);
      if (playBtn) playBtn.textContent = '\u25B6';
      startEl.classList.add('hide');
      return;
    }
    if (audio.currentTime >= TOTAL - 0.05) { audio.currentTime = 0; lastIdx = -1; }
    startEl.classList.add('hide');
    var pr = audio.play();
    var go = function () { playing = true; if (playBtn) playBtn.textContent = '\u2016'; loop(); };
    if (pr && pr.then) pr.then(go).catch(function () {});
    else go();
  }

  function stopPlayback() {
    audio.pause(); playing = false; cancelAnimationFrame(raf);
    audio.currentTime = 0; lastIdx = -1; fired = {};
    renderState(0);
    startEl.classList.remove('hide');
    if (playBtn) playBtn.textContent = '\u25B6';
    var meta = startEl.querySelector('.meta');
    if (meta) meta.textContent = 'CLICK TO START';
  }

  /* ==========================================================
     8. DETERMINISTIC RENDER — ?t=SECONDS
     ========================================================== */
  window.renderAt = function (t) {
    lastIdx = -1;
    F.__t = t;
    renderState(t);
    startEl.classList.add('hide');
  };

  var q = new URLSearchParams(location.search);
  if (q.has('t')) {
    document.body.classList.add('render');
    /* The 5 web fonts are ~1.4 MB of base64. Until they finish decoding the
       browser paints text with a fallback face, so a frame captured too early
       is not the frame you think it is. Wait for the fonts. */
    var go = function () {
      requestAnimationFrame(function () {
        requestAnimationFrame(function () {
          window.renderAt(parseFloat(q.get('t')) || 0);
        });
      });
    };
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(go);
    } else { go(); }
  }

  /* safety net: rAF stops when the tab is hidden, audio keeps going */
  setInterval(function () {
    if (!playing) return;
    if (performance.now() - lastTick > 400) { cancelAnimationFrame(raf); loop(); }
  }, 250);
  document.addEventListener('visibilitychange', function () {
    if (!document.hidden && playing) { cancelAnimationFrame(raf); loop(); }
  });

  /* ==========================================================
     9. REVIEW CONTROLS
     ========================================================== */
  var playBtn = null;
  var RATES = [1, 1.5, 2, 4];
  function setRate(r) {
    audio.playbackRate = r;
    var bs = document.querySelectorAll('#ctl .rate');
    for (var i = 0; i < bs.length; i++) bs[i].classList.toggle('on', parseFloat(bs[i].getAttribute('data-r')) === r);
  }
  if (!document.body.classList.contains('render')) {
    var ctl = document.createElement('div');
    ctl.id = 'ctl';
    ctl.innerHTML = '<button id="ctlPlay" title="Play / Pause (Space)">\u25B6</button>' +
      '<button id="ctlStop" title="Stop (S)">\u25A0</button><span class="sep"></span>' +
      RATES.map(function (r) { return '<button class="rate" data-r="' + r + '">' + r + '\u00D7</button>'; }).join('');
    document.body.appendChild(ctl);
    playBtn = ctl.querySelector('#ctlPlay');
    playBtn.addEventListener('click', togglePlay);
    ctl.querySelector('#ctlStop').addEventListener('click', stopPlayback);
    var rbs = ctl.querySelectorAll('.rate');
    for (var i = 0; i < rbs.length; i++) {
      (function (b) { b.addEventListener('click', function () { setRate(parseFloat(b.getAttribute('data-r'))); }); })(rbs[i]);
    }
    setRate(1);
  }

  addEventListener('keydown', function (e) {
    if (e.target && /INPUT|TEXTAREA/.test(e.target.tagName)) return;
    if (e.code === 'Space') { e.preventDefault(); togglePlay(); }
    else if (e.key === 's' || e.key === 'S') stopPlayback();
    else if (e.key >= '1' && e.key <= '4') setRate(RATES[+e.key - 1]);
    else if (e.code === 'ArrowRight') audio.currentTime = Math.min(TOTAL - 0.1, audio.currentTime + 5);
    else if (e.code === 'ArrowLeft') audio.currentTime = Math.max(0, audio.currentTime - 5);
  });

  startEl.addEventListener('click', function () { if (!playing) togglePlay(); });

  if (q.has('debug')) {
    var box = document.createElement('div');
    box.style.cssText = 'position:absolute;left:12px;top:12px;z-index:200;font:14px monospace;' +
      'color:#6f6;background:rgba(0,0,0,.75);padding:6px 10px;border:1px solid #333';
    stage.appendChild(box);
    setInterval(function () {
      box.textContent = 't=' + audio.currentTime.toFixed(1) + '  scene=' + (lastIdx + 1) +
        '  playing=' + playing + '  beats=' + BEATS.length;
    }, 200);
  }

  /* expose for the gate / tests */
  window.__FUSION__ = { F: F, renderState: renderState, sceneAt: sceneAt, dipOpacity: dipOpacity };
})();