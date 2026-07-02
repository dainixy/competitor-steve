#!/usr/bin/env node
/**
 * Pairwise motion judge — forced A/B choice, both orders, 3 votes each order.
 * Port of judge_ears.py's pairwise recipe to video.
 *
 * Dimensions:
 *   aliveness   — overall motion: head drift, blinks, gaze saccades, micro-expression
 *   head-life   — head pose change (nod / tilt / turn) and gaze direction shifts only
 *   expression  — brow, cheek, lip-corner, chin micro-expressions and emotional warmth
 *
 * Usage:
 *   node judge_pairwise.mjs <clipA.mp4> <clipB.mp4> <dimension> [model]
 *
 * Returns JSON to stdout: { winner:"A"|"B"|"inconclusive", dimension, votes, reasons }
 * Exit 0 always (caller decides what to do with the result).
 *
 * API keys: source ../../alexis-voice-mvp/.env before running.
 */
import fs from 'fs';
import os from 'os';
import path from 'path';
import { execSync } from 'child_process';

const [,, CLIP_A, CLIP_B, DIMENSION, MODEL_ARG] = process.argv;
const MODEL = MODEL_ARG || 'openai/gpt-4.1';
const OPENROUTER_KEY = process.env.OPENROUTER_API_KEY;

if (!CLIP_A || !CLIP_B || !DIMENSION) {
  console.error('Usage: node judge_pairwise.mjs <clipA.mp4> <clipB.mp4> <dimension> [model]');
  process.exit(1);
}
if (!OPENROUTER_KEY) {
  console.error('OPENROUTER_API_KEY not set');
  process.exit(1);
}
for (const p of [CLIP_A, CLIP_B]) {
  if (!fs.existsSync(p)) { console.error('clip not found:', p); process.exit(1); }
}

const VALID_DIMENSIONS = ['aliveness', 'head-life', 'expression'];
if (!VALID_DIMENSIONS.includes(DIMENSION)) {
  console.error('dimension must be one of:', VALID_DIMENSIONS.join(', '));
  process.exit(1);
}

const FF = (() => {
  try { return execSync('command -v ffmpeg', { encoding: 'utf8' }).trim(); }
  catch { return '/Users/admin/.local/bin/ffmpeg'; }
})();
const FP = FF.replace(/ffmpeg$/, 'ffprobe');

function dur(clip) {
  return parseFloat(
    execSync(`${FP} -v error -show_entries format=duration -of default=nk=1:nw=1 "${clip}"`,
      { encoding: 'utf8' }).trim()
  );
}

/** Extract N chronological frames from a clip, return array of base64 PNG strings. */
function extractFrames(clip, n = 8) {
  const d = dur(clip);
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'pw_'));
  const frames = [];
  for (let i = 0; i < n; i++) {
    const t = 0.4 + (d - 0.8) * i / (n - 1);
    const out = path.join(tmp, `f${i}.png`);
    execSync(
      `${FF} -y -ss ${t.toFixed(3)} -i "${clip}" -frames:v 1 -vf "scale=460:-1" -q:v 2 "${out}"`,
      { stdio: 'ignore' }
    );
    frames.push({ t: +t.toFixed(2), b64: fs.readFileSync(out).toString('base64') });
  }
  return frames;
}

const RUBRICS = {
  aliveness: `You are judging which 3D avatar looks MORE ALIVE and naturally moving overall.
Judge: head pose change (nod/tilt/turn), gaze direction + blinks, eyebrows,
cheek micro-expression, breathing/shoulder rise, and overall posture sway.
IGNORE the lips/mouth entirely. Compare the two subjects on ALL these channels.`,
  'head-life': `You are judging which 3D avatar shows MORE head and gaze life.
Focus ONLY on: how much the head rotates/nods/tilts across frames, whether the
gaze direction shifts naturally, and whether blinks occur. Ignore mouth/lips,
body gestures, and overall expressiveness.`,
  expression: `You are judging which 3D avatar shows MORE facial expression and warmth.
Focus ONLY on: brow movement, cheek lift, lip-corner micro-expressions, chin
tucks, nose/cheek scrunches, and emotional warmth that shows on the face.
Ignore head rotation, body, and lip-sync.`,
};

/**
 * One pairwise vote: send frames of Subject A and Subject B, ask which looks better
 * on the given dimension.  Returns { winner: 'A'|'B'|'tie', reason: string }.
 */
async function oneVote(framesA, framesB, dimension) {
  const rubric = RUBRICS[dimension];
  const n = framesA.length;

  const content = [
    {
      type: 'text',
      text: `${rubric}

You are given ${n} frames in CHRONOLOGICAL ORDER (frame 1 earliest → frame ${n} latest),
sampled evenly across each clip. Compare across frames to infer motion over time.

SUBJECT A — ${n} frames:`,
    },
  ];
  framesA.forEach((f, i) => {
    content.push({ type: 'text', text: `A frame ${i + 1} (t=${f.t}s):` });
    content.push({ type: 'image_url', image_url: { url: `data:image/png;base64,${f.b64}`, detail: 'high' } });
  });
  content.push({ type: 'text', text: `SUBJECT B — ${n} frames:` });
  framesB.forEach((f, i) => {
    content.push({ type: 'text', text: `B frame ${i + 1} (t=${f.t}s):` });
    content.push({ type: 'image_url', image_url: { url: `data:image/png;base64,${f.b64}`, detail: 'high' } });
  });
  content.push({
    type: 'text',
    text: `Which subject looks MORE ${dimension === 'head-life' ? 'alive in head/gaze motion' : dimension === 'expression' ? 'expressively warm and lively in facial expression' : 'alive overall (all motion channels except lips)'}?
Answer ONLY: {"winner":"A","reason":"<= 20 words"} or {"winner":"B","reason":"<= 20 words"} or {"winner":"tie","reason":"<= 20 words"}.
No preamble. JSON only.`,
  });

  const body = {
    model: MODEL,
    messages: [{ role: 'user', content }],
    max_tokens: 80,
    temperature: 0.1,
  };

  for (let attempt = 0; attempt < 3; attempt++) {
    const r = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: { Authorization: `Bearer ${OPENROUTER_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
    const j = await r.json();
    if (!j.choices) {
      if (attempt < 2) continue;
      return { winner: 'err', reason: JSON.stringify(j).slice(0, 120) };
    }
    const rawTxt = j.choices[0].message.content || '';
    // Strip markdown code fences (```json ... ``` or ``` ... ```) before parsing
    const txt = rawTxt.replace(/^```(?:json)?\s*/i, '').replace(/\s*```\s*$/, '').trim();
    const m = txt.match(/\{[^}]+\}/);
    try {
      if (m) return JSON.parse(m[0]);
    } catch { /* fall through */ }
    // Try to extract just the letter
    const letter = txt.match(/\b(A|B|tie)\b/);
    if (letter) return { winner: letter[1], reason: txt.slice(0, 80) };
    if (attempt < 2) continue;
    return { winner: 'parse_err', reason: txt.slice(0, 80) };
  }
  return { winner: 'err', reason: 'exhausted retries' };
}

/**
 * Full pairwise duel: both orders × VOTES_PER_ORDER votes.
 * Consistent winner = wins in BOTH orders (majority per order).
 * Order flip or tie → inconclusive.
 */
const VOTES_PER_ORDER = 3;

async function duel(clipA, clipB, dimension) {
  process.stderr.write(`Extracting frames from A and B...\n`);
  const framesA = extractFrames(clipA);
  const framesB = extractFrames(clipB);

  process.stderr.write(`Running ${VOTES_PER_ORDER} votes in order A→B...\n`);
  const order1_votes = [];
  for (let i = 0; i < VOTES_PER_ORDER; i++) {
    const v = await oneVote(framesA, framesB, dimension);
    order1_votes.push(v);
    process.stderr.write(`  vote ${i + 1}: ${v.winner} — ${v.reason}\n`);
  }

  process.stderr.write(`Running ${VOTES_PER_ORDER} votes in order B→A...\n`);
  const order2_votes = [];
  for (let i = 0; i < VOTES_PER_ORDER; i++) {
    // In reversed order: A is presented as B, B as A → flip the winner label
    const v = await oneVote(framesB, framesA, dimension);
    // Remap back to A/B from original clips perspective
    const remapped = { ...v };
    if (v.winner === 'A') remapped.winner = 'B'; // model picked "A" but that was our B
    else if (v.winner === 'B') remapped.winner = 'A';
    order2_votes.push(remapped);
    process.stderr.write(`  vote ${i + 1}: ${remapped.winner} (raw:${v.winner}) — ${v.reason}\n`);
  }

  // Majority within each order
  function majority(votes) {
    const counts = { A: 0, B: 0, tie: 0, err: 0, parse_err: 0 };
    for (const v of votes) counts[v.winner] = (counts[v.winner] || 0) + 1;
    if (counts.A > counts.B && counts.A > counts.tie) return 'A';
    if (counts.B > counts.A && counts.B > counts.tie) return 'B';
    return 'tie';
  }

  const m1 = majority(order1_votes);
  const m2 = majority(order2_votes);

  let winner;
  if (m1 === 'A' && m2 === 'A') winner = 'A';
  else if (m1 === 'B' && m2 === 'B') winner = 'B';
  else winner = 'inconclusive'; // order flip or genuine tie → conservative no-win

  return {
    winner,
    dimension,
    model: MODEL,
    order1: { votes: order1_votes, majority: m1 },
    order2: { votes: order2_votes, majority: m2 },
    summary: `order1→${m1} order2→${m2} => ${winner}`,
  };
}

const result = await duel(CLIP_A, CLIP_B, DIMENSION);
process.stderr.write(`\nResult: ${result.summary}\n`);
console.log(JSON.stringify(result, null, 2));
