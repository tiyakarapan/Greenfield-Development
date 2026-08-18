import { useState } from 'react';
import { entities } from '../config/entities';

// fkOptions: { [entityKey]: rows[] } — preloaded lists used to populate
// foreign-key dropdowns (e.g. the "Student" select on the Enrollment form).
export default function EntityForm({ config, initial, fkOptions, onSubmit, onCancel, submitLabel }) {
  const isEditing = Boolean(initial);
  const [values, setValues] = useState(() => {
    const base = {};
    config.fields.forEach((f) => { base[f.name] = initial?.[f.name] ?? ''; });
    return base;
  });
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);

  function setField(name, val) {
    setValues((v) => ({ ...v, [name]: val }));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setSaving(true);
    setError(null);
    try {
      // Dates come back from <input type=date> as "YYYY-MM-DD" already;
      // strip any trailing time component if it was pre-filled from the DB.
      const payload = {};
      config.fields.forEach((f) => {
        let v = values[f.name];
        if (f.type === 'date' && typeof v === 'string' && v.includes('T')) v = v.split('T')[0];
        if (v === '') {
          // On create, leave the key out entirely so columns with a DB
          // default (e.g. enrollment_date DEFAULT CURRENT_DATE) get
          // that default instead of an explicit NULL, which would
          // violate NOT NULL. On edit, send null to actually clear an
          // optional field the user emptied out.
          if (isEditing) payload[f.name] = null;
        } else {
          payload[f.name] = v;
        }
      });
      await onSubmit(payload);
    } catch (err) {
      setError(err?.response?.data?.error || err.message || 'Save failed.');
    } finally {
      setSaving(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <div className="modal-body">
        {error && <div className="error-banner">{error}</div>}
        {config.fields.map((f) => (
          <div className="field" key={f.name}>
            <label>
              {f.label}
              {f.required && <span className="req">*</span>}
            </label>
            {f.type === 'select' && (
              <select
                required={f.required}
                value={values[f.name] || ''}
                onChange={(e) => setField(f.name, e.target.value)}
              >
                <option value="">— Select —</option>
                {f.options.map((opt) => (
                  <option key={opt} value={opt}>{opt.replace('_', ' ')}</option>
                ))}
              </select>
            )}
            {f.type === 'fk' && (
              <select
                required={f.required}
                value={values[f.name] || ''}
                onChange={(e) => setField(f.name, e.target.value)}
              >
                <option value="">— None —</option>
                {(fkOptions[f.fk] || []).map((row) => {
                  const pkCol = entities[f.fk].pk[0];
                  const display = entities[f.fk].displayField(row);
                  return (
                    <option key={row[pkCol]} value={row[pkCol]}>
                      #{row[pkCol]} — {display}
                    </option>
                  );
                })}
              </select>
            )}
            {f.type === 'textarea' && (
              <textarea
                required={f.required}
                value={values[f.name] || ''}
                onChange={(e) => setField(f.name, e.target.value)}
              />
            )}
            {['text', 'email', 'date', 'number'].includes(f.type) && (
              <input
                type={f.type}
                step={f.type === 'number' ? '0.01' : undefined}
                required={f.required}
                value={values[f.name] || ''}
                onChange={(e) => setField(f.name, e.target.value)}
              />
            )}
          </div>
        ))}
      </div>
      <div className="modal-footer">
        <button type="button" className="btn btn-secondary" onClick={onCancel}>Cancel</button>
        <button type="submit" className="btn btn-primary" disabled={saving}>
          {saving ? 'Saving…' : submitLabel}
        </button>
      </div>
    </form>
  );
}
