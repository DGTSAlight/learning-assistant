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

const VALID_STATUS = new Set(['mastered', 'shaky', 'not-learned', 'skipped', 'unverified']);

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
const mastered = points.filter((p) => p && p.status === 'mastered');
const weakEvidence = mastered.filter((p) => (p.checks ?? 0) < 2 || p.unpromptedRecall !== true);
const badStatus = points.filter((p) => p && !VALID_STATUS.has(p.status));

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
    ? `${weakEvidence.length} mastered point(s) lack two independent checks or unprompted recall`
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
    ? `${badStatus.length} point(s) have an unknown status`
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
