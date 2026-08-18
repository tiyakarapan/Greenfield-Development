import StatusSeal from './StatusSeal';

const DATE_COLS = new Set(['enrollment_date', 'date_of_birth', 'exam_date', 'attendance_date', 'qualified_date']);
const MONO_COLS = new Set(['access_key']);

function formatCell(col, value) {
  if (value === null || value === undefined || value === '') return <span style={{ color: 'var(--line)' }}>—</span>;
  if (DATE_COLS.has(col)) return String(value).split('T')[0];
  return String(value);
}

export default function DataTable({ config, rows, onEdit, onDelete }) {
  if (rows.length === 0) {
    return (
      <div className="panel">
        <div className="empty-state">
          <h3>No {config.label.toLowerCase()} yet</h3>
          <p>Add the first record using the button above.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="panel">
      <table>
        <thead>
          <tr>
            {config.tableColumns.map((col) => (
              <th key={col}>{col.replace(/_/g, ' ')}</th>
            ))}
            <th style={{ textAlign: 'right' }}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => {
            const pkVal = config.pk.map((p) => row[p]).join('_');
            return (
              <tr key={pkVal}>
                {config.tableColumns.map((col) => {
                  const isId = col.endsWith('_id');
                  const isStatus = col === config.statusField;
                  return (
                    <td key={col} className={isId || MONO_COLS.has(col) ? 'mono' : ''}>
                      {isStatus ? <StatusSeal value={row[col]} /> : formatCell(col, row[col])}
                    </td>
                  );
                })}
                <td className="actions">
                  <button className="btn-ghost" onClick={() => onEdit(row)}>Edit</button>
                  <button className="btn-ghost" style={{ color: 'var(--danger)' }} onClick={() => onDelete(row)}>Delete</button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
