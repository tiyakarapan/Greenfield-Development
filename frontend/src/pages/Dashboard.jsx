import { useEffect, useState } from 'react';
import { api, apiErrorMessage } from '../api';
import StatusSeal from '../components/StatusSeal';

function Section({ title, desc, children }) {
  return (
    <div className="report-section">
      <h2>{title}</h2>
      <p className="desc">{desc}</p>
      {children}
    </div>
  );
}

function SimpleTable({ rows, columns, empty }) {
  if (!rows || rows.length === 0) {
    return <div className="panel"><div className="empty-state"><h3>{empty || 'Nothing to show'}</h3></div></div>;
  }
  return (
    <div className="panel">
      <table>
        <thead>
          <tr>{columns.map((c) => <th key={c.key}>{c.label}</th>)}</tr>
        </thead>
        <tbody>
          {rows.map((row, i) => (
            <tr key={i}>
              {columns.map((c) => (
                <td key={c.key} className={c.mono ? 'mono' : ''}>
                  {c.render ? c.render(row) : (row[c.key] ?? '—')}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default function Dashboard({ counts }) {
  const [atRisk, setAtRisk] = useState([]);
  const [mismatches, setMismatches] = useState([]);
  const [roster, setRoster] = useState([]);
  const [examRecords, setExamRecords] = useState([]);
  const [demand, setDemand] = useState([]);
  const [intake, setIntake] = useState([]);
  const [intakeFrom, setIntakeFrom] = useState('1900-01-01');
  const [intakeTo, setIntakeTo] = useState('2999-12-31');
  const [transcriptId, setTranscriptId] = useState('');
  const [transcript, setTranscript] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    (async () => {
      try {
        const [ar, mm, r, ex, dm, ik] = await Promise.all([
          api.report('at-risk-students'),
          api.report('facilitator-mismatches'),
          api.report('roster'),
          api.report('exam-records'),
          api.report('course-demand'),
          api.report('intake'),
        ]);
        setAtRisk(ar); setMismatches(mm); setRoster(r); setExamRecords(ex); setDemand(dm); setIntake(ik);
      } catch (err) {
        setError(apiErrorMessage(err));
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  async function runIntakeFilter() {
    try {
      const rows = await api.report('intake', { from: intakeFrom, to: intakeTo });
      setIntake(rows);
    } catch (err) { setError(apiErrorMessage(err)); }
  }

  async function lookupTranscript() {
    if (!transcriptId) return;
    try {
      const rows = await api.report(`transcript/${transcriptId}`);
      setTranscript(rows);
    } catch (err) { setError(apiErrorMessage(err)); }
  }

  function exportStudentsCsv() {
    api.report('export/students').then((rows) => {
      if (rows.length === 0) return;
      const cols = Object.keys(rows[0]);
      const csv = [cols.join(','), ...rows.map((r) => cols.map((c) => JSON.stringify(r[c] ?? '')).join(','))].join('\n');
      const blob = new Blob([csv], { type: 'text/csv' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url; a.download = 'itca_students_export.csv'; a.click();
      URL.revokeObjectURL(url);
    }).catch((err) => setError(apiErrorMessage(err)));
  }

  return (
    <div>
      <div className="page-header">
        <div>
          <h1 className="page-title">Dashboard</h1>
          <div className="page-subtitle">Operational reports for Andre &amp; campus staff</div>
        </div>
        <button className="btn btn-secondary" onClick={exportStudentsCsv}>Export students to CSV</button>
      </div>

      {error && <div className="error-banner">{error}</div>}

      <div className="stat-grid">
        <div className="stat-card"><div className="num">{counts?.student ?? '–'}</div><div className="label">Total students</div></div>
        <div className="stat-card"><div className="num">{counts?.enrollment ?? '–'}</div><div className="label">Total enrollments</div></div>
        <div className="stat-card"><div className="num">{atRisk.length}</div><div className="label">At-risk (3+ absences)</div></div>
        <div className="stat-card"><div className="num">{counts?.course ?? '–'}</div><div className="label">Courses offered</div></div>
      </div>

      {loading ? <div className="loading">Loading reports…</div> : (
        <>
          <Section
            title="At-risk students"
            desc="Students with 3 or more consecutive absences on a course — flagged so parents/sponsors can be contacted."
          >
            <SimpleTable
              rows={atRisk}
              empty="No students currently at risk — nice."
              columns={[
                { key: 'student_id', label: 'ID', mono: true },
                { key: 'name', label: 'Student', render: (r) => `${r.first_name} ${r.last_name}` },
                { key: 'course_name', label: 'Course' },
                { key: 'consecutive_absences', label: 'Consecutive absences' },
                { key: 'streak_start', label: 'From', mono: true, render: (r) => String(r.streak_start).split('T')[0] },
                { key: 'streak_end', label: 'To', mono: true, render: (r) => String(r.streak_end).split('T')[0] },
              ]}
            />
          </Section>

          <Section
            title="Facilitator qualification audit"
            desc="Enrollments where the assigned facilitator is not on record as qualified for that course. The database trigger blocks new bad assignments, so this should stay empty."
          >
            <SimpleTable
              rows={mismatches}
              empty="No mismatches found — the qualification trigger is holding."
              columns={[
                { key: 'enrollment_id', label: 'Enrollment', mono: true },
                { key: 'facilitator', label: 'Facilitator', render: (r) => `${r.facilitator_first_name} ${r.facilitator_last_name}` },
                { key: 'course_name', label: 'Course' },
              ]}
            />
          </Section>

          <Section title="Class rosters" desc="Every current enrollment, grouped by course, with the assigned facilitator.">
            <SimpleTable
              rows={roster}
              columns={[
                { key: 'course_name', label: 'Course' },
                { key: 'student_id', label: 'Student ID', mono: true },
                { key: 'student', label: 'Student', render: (r) => `${r.first_name} ${r.last_name}` },
                { key: 'enrollment_status', label: 'Status', render: (r) => <StatusSeal value={r.enrollment_status} /> },
                { key: 'facilitator', label: 'Facilitator', render: (r) => r.facilitator_first_name ? `${r.facilitator_first_name} ${r.facilitator_last_name}` : '—' },
              ]}
            />
          </Section>

          <Section title="Exam attempts" desc="Full pass/fail history across all exam attempts, including retakes.">
            <SimpleTable
              rows={examRecords}
              columns={[
                { key: 'student', label: 'Student', render: (r) => `${r.first_name} ${r.last_name}` },
                { key: 'course_name', label: 'Course' },
                { key: 'attempt_number', label: 'Attempt #' },
                { key: 'exam_date', label: 'Date', mono: true, render: (r) => String(r.exam_date).split('T')[0] },
                { key: 'score', label: 'Score' },
                { key: 'pass_fail', label: 'Result', render: (r) => <StatusSeal value={r.pass_fail} /> },
              ]}
            />
          </Section>

          <Section title="Course demand" desc="Enrollment counts per course by intake month — for tracking industry demand trends.">
            <SimpleTable
              rows={demand}
              columns={[
                { key: 'course_name', label: 'Course' },
                { key: 'intake_month', label: 'Intake month', mono: true, render: (r) => String(r.intake_month).split('T')[0] },
                { key: 'enrollment_count', label: 'Enrollments' },
              ]}
            />
          </Section>

          <Section title="New student intake" desc="Students enrolled within a date range — the beginning-of-year intake workflow.">
            <div className="report-toolbar">
              <div className="field">
                <label>From</label>
                <input type="date" value={intakeFrom} onChange={(e) => setIntakeFrom(e.target.value)} />
              </div>
              <div className="field">
                <label>To</label>
                <input type="date" value={intakeTo} onChange={(e) => setIntakeTo(e.target.value)} />
              </div>
              <button className="btn btn-secondary" onClick={runIntakeFilter}>Filter</button>
            </div>
            <SimpleTable
              rows={intake}
              columns={[
                { key: 'student_id', label: 'ID', mono: true },
                { key: 'name', label: 'Student', render: (r) => `${r.first_name} ${r.last_name}` },
                { key: 'email', label: 'Email' },
                { key: 'enrollment_date', label: 'Enrolled', mono: true, render: (r) => String(r.enrollment_date).split('T')[0] },
                { key: 'status', label: 'Status', render: (r) => <StatusSeal value={r.status} /> },
              ]}
            />
          </Section>

          <Section title="Academic transcript lookup" desc="Full course + result history for one student — for transcript requests from students or sponsors.">
            <div className="report-toolbar">
              <div className="field">
                <label>Student ID</label>
                <input type="number" value={transcriptId} onChange={(e) => setTranscriptId(e.target.value)} placeholder="e.g. 1" />
              </div>
              <button className="btn btn-secondary" onClick={lookupTranscript}>Look up</button>
            </div>
            {transcript && (
              <SimpleTable
                rows={transcript}
                empty="No enrollment history for this student."
                columns={[
                  { key: 'course_name', label: 'Course' },
                  { key: 'certification_body', label: 'Cert body' },
                  { key: 'enrollment_date', label: 'Enrolled', mono: true, render: (r) => String(r.enrollment_date).split('T')[0] },
                  { key: 'enrollment_status', label: 'Status', render: (r) => <StatusSeal value={r.enrollment_status} /> },
                  { key: 'final_result', label: 'Result', render: (r) => <StatusSeal value={r.final_result} /> },
                ]}
              />
            )}
          </Section>
        </>
      )}
    </div>
  );
}
