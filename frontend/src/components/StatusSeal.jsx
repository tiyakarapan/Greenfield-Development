// Renders any status-like value (student status, enrollment status,
// pass/fail, attendance) as a small stamped "seal" badge, colored by
// meaning rather than by table, so the same visual language holds
// across the whole app.
const TONE_MAP = {
  active: 'success', enrolled: 'success', pass: 'success', present: 'success', completed: 'success', graduated: 'success',
  at_risk: 'warn', late: 'warn',
  dropped: 'danger', fail: 'danger', failed: 'danger', absent: 'danger',
};

export default function StatusSeal({ value }) {
  if (!value) return <span className="seal seal-neutral">—</span>;
  const tone = TONE_MAP[value] || 'neutral';
  return <span className={`seal seal-${tone}`}>{String(value).replace('_', ' ')}</span>;
}
