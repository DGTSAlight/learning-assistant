// Optional deterministic gate check for learning-assistant.
//
// Level 2 of the degradation ladder in references/gates.md: voluntary, not automatic.
// Reads a session state JSON from stdin or a file argument and checks the five gates.
// Pure Node, no dependencies, no network, no writes outside stdout/stderr.
//
// Usage:
//   node scripts/check-gates.mjs < state.json
//   node scripts/check-gates.mjs state.json
//
// Exit codes: 0 all gates pass (or no state supplied) / 1 some gate failed / 2 bad input.

import fs from 'node:fs';

// Canonical set: mastered | shaky | not-learned | skipped | unknown | unverified.
// The references spell these differently ("not learned", "unverified"), so statuses are
// normalised before comparison instead of trusting one spelling.
const VALID_STATUS = new Set(['mastered', 'shaky', 'not-learned', 'skipped', 'unknown', 'unverified']);
const normStatus = (point) => String(point?.status ?? '').trim().toLowerCase().replace(/[\s_]+/g, '-');

function readInput() {
  const file = process.argv[2];
  if (file && file !== '-') {
    try { return fs.readFileSync(file, 'utf8').trim(); }
    catch (error) {
      console.error(`[check-gates] cannot read ${file}: ${error?.message ?? error}`);
      process.exit(2);
    }
  }
  try { return fs.readFileSync(0, 'utf8').trim(); } catch { return ''; }
}

const raw = readInput();
if (!raw) {
  console.log('[check-gates] no state supplied; use the document self-check in references/gates.md');
  process.exit(0);
}

let state;
try { state = JSON.parse(raw); }
catch (error) {
  console.error(`[check-gates] invalid JSON: ${error?.message ?? error}`);
  process.exit(2);
}
if (typeof state !== 'object' || state === null || Array.isArray(state)) {
  console.error('[check-gates] state must be a JSON object');
  process.exit(2);
}

const points = Array.isArray(state.points) ? state.points : [];
const graded = points.filter((p) => p && typeof p === 'object')
  .map((p) => ({ point: p, status: normStatus(p) }));
const mastered = graded.filter((g) => g.status === 'mastered').map((g) => g.point);

// A check count must be a number. "two" is not evidence, and a string comparison would
// silently pass: ("two" < 2) is false, which is exactly how this gate used to be bypassed.
function weakReason(point) {
  const n = point.checks;
  if (typeof n !== 'number' || !Number.isFinite(n)) { return 'checks is not a number'; }
  if (n < 2) { return 'fewer than two checks'; }
  if (point.unpromptedRecall !== true) { return 'no unprompted recall'; }
  return '';
}
const weakEvidence = mastered
  .map((p) => ({ point: p, reason: weakReason(p) }))
  .filter((w) => w.reason);
const badStatus = graded.filter((g) => !VALID_STATUS.has(g.status));

const results = [];
const add = (name, ok, detail) => results.push({ name, ok, detail });

add(
  'goal set',
  Boolean(state.goal && String(state.goal).trim()) && Boolean(state.depth),
  state.goal && state.depth ? 'goal and depth tier present' : 'missing goal or depth tier',
);

add(
  'mastery evidence',
  weakEvidence.length === 0,
  weakEvidence.length
    ? `${weakEvidence.length} mastered point(s) have no usable evidence — ` +
      weakEvidence.map((w) => `${w.point.name ?? w.point.title ?? '(unnamed)'}: ${w.reason}`).join('; ')
    : `${mastered.length} mastered point(s) checked`,
);

add(
  'prep verification',
  state.prepVerified === true,
  state.prepVerified === true
    ? 'commands/code were run or checked'
    : 'prepVerified is not true; label shown material as unverified',
);

add(
  'notes landed',
  state.notesWritten === true,
  state.notesWritten === true ? 'notes written or updated' : 'notesWritten is not true',
);

const honest = badStatus.length === 0 && !(state.claimsTested === true && state.executed !== true);
add(
  'honest status',
  honest,
  badStatus.length
    ? `${badStatus.length} point(s) have a status outside the allowed set`
    : state.claimsTested === true && state.executed !== true
      ? 'claims tested but no execution evidence'
      : 'status labels are consistent',
);

let failed = 0;
for (const r of results) {
  console.log(`[check-gates] ${r.ok ? 'PASS' : 'FAIL'}  ${r.name} — ${r.detail}`);
  if (!r.ok) failed += 1;
}
console.log(`[check-gates] ${results.length - failed}/${results.length} gates passed`);
if (failed) {
  console.log('[check-gates] fix the failed gates, or state explicitly that they were skipped');
  process.exitCode = 1;
}
