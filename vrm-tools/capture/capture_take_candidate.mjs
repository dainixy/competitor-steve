#!/usr/bin/env node
// capture_take_candidate.mjs — same as capture_take.mjs but writes to a
// candidate dir (set via CANDIDATE_LEDGER env var) instead of the baseline ledger.
//
// Uses canvas captureStream (same as capture_take.mjs) — this works reliably
// on this machine with --use-angle=metal enabling GPU in headless Chromium.
//
// Usage:
//   CANDIDATE_LEDGER=<dir> node capture_take_candidate.mjs <idle|speak> <label> [question]
//
// Extra vs capture_take.mjs:
//   - Writes to CANDIDATE_LEDGER/<label>/ instead of baseline ledger
//   - Waits for VRM to actually load (headRotX > 0) not just for probe to register
//   - Probes headRotX/Y/Z in addition to standard fields
//   - Forces useReplayTTS via WS intercept for deterministic speaking takes
//   - Pins nadia-v2.vrm requests to nadia.vrm

import pwPkg from '/Users/admin/Documents/claude/alexis/node_modules/playwright/index.js';
const { chromium } = pwPkg;
import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const FFMPEG = '/Users/admin/.local/bin/ffmpeg';
const BASE_PORT = 3000;
const BASE_URL = `http://localhost:${BASE_PORT}`;
const LOGIN_EMAIL = 'graverisd@gmail.com';
const LOGIN_PASSWORD = 'NadiaLive2026!';
const LEDGER = process.env.CANDIDATE_LEDGER;
if (!LEDGER) {
  console.error('CANDIDATE_LEDGER env var is required');
  process.exit(1);
}

const mode = process.argv[2]; // 'idle' | 'speak'
const label = process.argv[3] || `take_${Date.now()}`;
const question = process.argv[4] || 'Tell me about the book you couldn\'t put down last winter.';

if (!mode || !['idle', 'speak'].includes(mode)) {
  console.error('Usage: CANDIDATE_LEDGER=<dir> node capture_take_candidate.mjs <idle|speak> <label> [question]');
  process.exit(1);
}

const OUT = path.join(LEDGER, label);
fs.mkdirSync(OUT, { recursive: true });
console.log(`[capture] mode=${mode} label=${label} out=${OUT}`);

// --- Boot browser (same flags as capture_take.mjs — metal GPU for captureStream) ---
const browser = await chromium.launch({
  headless: true,
  args: [
    '--use-angle=metal',
    '--enable-gpu',
    '--ignore-gpu-blocklist',
    '--no-sandbox',
    '--autoplay-policy=no-user-gesture-required',
    '--disable-web-security',
  ],
});
const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
const page = await ctx.newPage();

const errors = [];
page.on('pageerror', (e) => errors.push(String(e).slice(0, 200)));
page.on('console', (m) => {
  const t = m.text();
  if (/__cap|__rec|MediaRecorder|captureStream|nadiaProbe/.test(t)) {
    console.log('  [page]', t.slice(0, 150));
  }
});

// --- Inject helpers before page load ---
await page.addInitScript(() => {
  // age gate
  try { localStorage.setItem('age-verification-consent', JSON.stringify({ verified: true, timestamp: Date.now() })); } catch {}

  // Force Replay TTS on the WS transport
  const __origWsSend = WebSocket.prototype.send;
  WebSocket.prototype.send = function (data) {
    try {
      if (typeof data === 'string' && data.includes('useReplayTTS')) {
        const obj = JSON.parse(data);
        const patch = (o) => {
          if (o && typeof o === 'object') {
            if ('useReplayTTS' in o) o.useReplayTTS = true;
            for (const v of Object.values(o)) patch(v);
          }
        };
        patch(obj);
        data = JSON.stringify(obj);
        console.log('__cap patched WS useReplayTTS=true');
      }
    } catch (e) {}
    return __origWsSend.call(this, data);
  };

  // TTS element tracking (to capture audio stream for speaking takes)
  window.__ttsEl = null;
  window.__audioEvents = [];
  const origPlay = HTMLMediaElement.prototype.play;
  HTMLMediaElement.prototype.play = function () {
    try {
      if (this instanceof HTMLAudioElement) {
        window.__audioEvents.push({ t: Math.round(performance.now()), vol: +this.volume.toFixed(2), muted: this.muted });
        if (this.volume > 0 && !this.muted) window.__ttsEl = this;
      }
    } catch (e) {}
    return origPlay.apply(this, arguments);
  };

  // Probe timeseries — polls __nadiaProbe every animation frame
  window.__probeTS = [];
  (function poll() {
    try {
      if (typeof window.__nadiaProbe === 'function') {
        const p = window.__nadiaProbe();
        window.__probeTS.push({
          t: Math.round(performance.now()),
          jaw: p.jawOpen,
          bl: p.eyeBlinkLeft,
          br: p.eyeBlinkRight,
          sm: p.mouthSmileLeft,
          lip: p.lipsync,
          bi: p.browInnerUp,
          headX: p.headX, headY: p.headY, headZ: p.headZ,
          camX: p.camX, camY: p.camY, camZ: p.camZ,
          camFov: p.camFov,
          chestRotX: p.chestRotX,
          headRotX: p.headRotX, headRotY: p.headRotY, headRotZ: p.headRotZ,
        });
        if (window.__probeTS.length > 12000) window.__probeTS.shift();
      }
    } catch (e) {}
    requestAnimationFrame(poll);
  })();

  // MediaRecorder helpers (captureStream approach — works with metal GPU)
  const u8ToB64 = (bytes) => {
    let bin = ''; const c = 0x8000;
    for (let i = 0; i < bytes.length; i += c)
      bin += String.fromCharCode.apply(null, bytes.subarray(i, i + c));
    return btoa(bin);
  };

  window.__startRec = async () => {
    const canvas = document.querySelector('canvas');
    if (!canvas) throw new Error('No canvas found');
    const vstream = canvas.captureStream(30);
    let aTracks = [];
    if (window.__ttsEl && window.__ttsEl.captureStream) {
      try {
        const as = window.__ttsEl.captureStream();
        for (let i = 0; i < 30 && as.getAudioTracks().length === 0; i++)
          await new Promise(r => setTimeout(r, 50));
        aTracks = as.getAudioTracks();
      } catch (e) { window.__capErr = String(e); }
    }
    window.__capAudioTracks = aTracks.length;
    const mixed = new MediaStream([...vstream.getVideoTracks(), ...aTracks]);
    window.__chunks = [];
    const mime = MediaRecorder.isTypeSupported('video/webm;codecs=vp8,opus')
      ? 'video/webm;codecs=vp8,opus' : 'video/webm';
    const mr = new MediaRecorder(mixed, { mimeType: mime });
    mr.ondataavailable = (e) => { if (e.data.size > 0) window.__chunks.push(e.data); };
    window.__mr = mr;
    window.__recStart = Math.round(performance.now());
    mr.start(100);
    console.log('__rec started mime=' + mime + ' aTracks=' + aTracks.length);
    return { audioTracks: aTracks.length, mime };
  };

  window.__stopRec = () => new Promise((res) => {
    const mr = window.__mr;
    if (!mr) { res(null); return; }
    mr.onstop = async () => {
      const blob = new Blob(window.__chunks, { type: 'video/webm' });
      res(u8ToB64(new Uint8Array(await blob.arrayBuffer())));
    };
    mr.stop();
  });
});

// Pin the avatar model to the ORIGINAL nadia.vrm
await page.route('**/models/nadia-v2.vrm*', (route) => {
  const u = new URL(route.request().url());
  console.log('[capture] pinned model request to /models/nadia.vrm (was ' + u.pathname + ')');
  route.continue({ url: `${u.origin}/models/nadia.vrm` });
});

// --- Login ---
await page.goto(BASE_URL, { waitUntil: 'domcontentloaded' });
await page.evaluate(async ({ email, password }) => {
  return fetch('/api/auth/sign-in/email/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({ email, password, turnstileToken: 'XXXX.DUMMY.TOKEN.XXXX' }),
  });
}, { email: LOGIN_EMAIL, password: LOGIN_PASSWORD });

await ctx.addCookies([{ name: 'age-verified', value: 'true', url: BASE_URL }]);
console.log('[capture] logged in, navigating to 3d-demo...');

// --- Navigate to 3d-demo ---
await page.goto(`${BASE_URL}/3d-demo`, { waitUntil: 'domcontentloaded' });
try { await page.click('button:has-text("I am 18 or older")', { timeout: 5000 }); } catch {}

// Step 1: wait for probe + run_demo_1 to register (component mounted)
console.log('[capture] waiting for probe registration...');
await page.waitForFunction(
  () => {
    try { return typeof window.__nadiaProbe === 'function' && typeof window.run_demo_1 === 'function'; }
    catch { return false; }
  },
  null,
  { timeout: 180000 }
);
console.log('[capture] probe registered, waiting for VRM to load into scene...');

// Step 2: wait for VRM humanoid bones to be populated (headRotX becomes non-zero)
await page.waitForFunction(
  () => {
    try {
      const p = window.__nadiaProbe();
      return typeof p.headRotX === 'number' && Math.abs(p.headRotX) > 0.0001;
    } catch { return false; }
  },
  null,
  { timeout: 240000 }
);
console.log('[capture] VRM scene loaded (head bone reporting)');

// Extra settle so idle animations fully initialize and first blink cycle starts
await page.waitForTimeout(6000);

// --- Start recording ---
const recInfo = await page.evaluate(() => window.__startRec());
console.log('[capture] rec started:', JSON.stringify(recInfo));
const recT0 = Date.now();

if (mode === 'idle') {
  console.log('[capture] idle mode — recording 20s');
  await page.waitForTimeout(20000);
} else {
  console.log(`[capture] speak mode — question: ${question.slice(0, 60)}`);

  // useReplayTTS via URL param as backup
  await page.route('**/api/3d-engine*', (route) => {
    const u = new URL(route.request().url());
    u.searchParams.set('useReplayTTS', 'true');
    console.log('[capture] rewrote 3d-engine request with useReplayTTS=true');
    route.continue({ url: u.toString() });
  });

  let dialogHandled = false;
  page.on('dialog', async (d) => {
    if (!dialogHandled) {
      dialogHandled = true;
      await d.accept(question);
      console.log('[capture] dialog accepted with question');
    }
  });

  await page.evaluate(() => {
    if (window.run_demo_1) window.run_demo_1();
  });

  let sawLip = false, lipEnd = null;
  while (Date.now() - recT0 < 90000) {
    await page.waitForTimeout(150);
    let lip = 0;
    try { lip = await page.evaluate(() => { const p = window.__nadiaProbe(); return p.lipsync; }); } catch {}
    if (lip === 1) { sawLip = true; lipEnd = Date.now(); }
    if (sawLip && lipEnd && Date.now() - lipEnd > 2000) break;
    if (!sawLip && Date.now() - recT0 > 60000) {
      console.log('[capture] WARN: no lipsync detected within 60s, stopping anyway');
      break;
    }
  }
  await page.waitForTimeout(500);
}

// --- Stop recording ---
const b64 = await page.evaluate(() => window.__stopRec());
const probeTS = await page.evaluate(() => ({
  recStart: window.__recStart,
  samples: window.__probeTS,
}));
const meta = await page.evaluate(() => ({
  events: window.__audioEvents,
  capAudioTracks: window.__capAudioTracks,
  capErr: window.__capErr,
}));

await browser.close();

console.log(`[capture] probe samples: ${probeTS.samples?.length}`);

// --- Save files ---
const rawWebm = path.join(OUT, 'raw.webm');
if (b64) {
  const buf = Buffer.from(b64, 'base64');
  fs.writeFileSync(rawWebm, buf);
  console.log(`[capture] saved probe_ts=${probeTS.samples?.length} samples, webm=${buf.length} bytes`);
} else {
  console.log('[capture] WARN: no video data captured (captureStream returned null)');
  fs.writeFileSync(rawWebm, Buffer.alloc(0));
}

fs.writeFileSync(path.join(OUT, 'probe_ts.json'), JSON.stringify(probeTS));
fs.writeFileSync(path.join(OUT, 'meta.json'), JSON.stringify({
  mode, label, question: mode === 'speak' ? question : null,
  recInfo, meta, errors,
  probeCount: probeTS.samples?.length ?? 0,
  captureMethod: 'canvas-captureStream',
}, null, 2));

// --- Transcode to mp4 ---
const mp4 = path.join(OUT, 'clip.mp4');
try {
  execSync(`"${FFMPEG}" -y -fflags +genpts -i "${rawWebm}" -c:v libx264 -preset fast -crf 23 -an "${mp4}"`,
    { stdio: 'inherit' });
  console.log(`[capture] mp4 saved: ${mp4}`);
} catch (e) {
  console.error('[capture] ffmpeg error:', e.message.slice(0, 200));
}
