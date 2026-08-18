// mock-server/server.js
//
// A throwaway API that matches API_CONTRACT.md, backed by in-memory
// arrays instead of Postgres. Lets the frontend run standalone while
// the real backend is being built. Swap it out later by pointing
// vite.config.js's proxy target at the real backend's port instead of
// this one - no frontend code changes needed.
//
// Run: npm install && npm start   (defaults to http://localhost:4000)

const express = require('express');
const cors = require('cors');
const { db, nextId } = require('./data');

const app = express();
app.use(cors());
app.use(express.json());

const PK = {
  student: ['student_id'], next_of_kin: ['next_of_kin_id'], sponsor: ['sponsor_id'],
  certification_body: ['cert_body_id'], course: ['course_id'], facilitator: ['facilitator_id'],
  facilitator_qualification: ['facilitator_id', 'course_id'], enrollment: ['enrollment_id'],
  exam_attempt: ['attempt_id'], attendance: ['attendance_id'],
};

function matchesId(row, pk, idParts) {
  return pk.every((col, i) => String(row[col]) === idParts[i]);
}

Object.keys(PK).forEach((entity) => {
  const pk = PK[entity];

  app.get(`/api/${entity}`, (req, res) => res.json(db[entity]));

  app.get(`/api/${entity}/:id`, (req, res) => {
    const idParts = req.params.id.split('_');
    const row = db[entity].find((r) => matchesId(r, pk, idParts));
    if (!row) return res.status(404).json({ error: 'Not found' });
    res.json(row);
  });

  app.post(`/api/${entity}`, (req, res) => {
    const row = { ...req.body };
    if (pk.length === 1 && !row[pk[0]]) {
      row[pk[0]] = nextId[entity] ?? (Math.max(0, ...db[entity].map((r) => r[pk[0]])) + 1);
      nextId[entity] = row[pk[0]] + 1;
    }
    db[entity].push(row);
    res.status(201).json(row);
  });

  app.put(`/api/${entity}/:id`, (req, res) => {
    const idParts = req.params.id.split('_');
    const row = db[entity].find((r) => matchesId(r, pk, idParts));
    if (!row) return res.status(404).json({ error: 'Not found' });
    Object.assign(row, req.body);
    res.json(row);
  });

  app.delete(`/api/${entity}/:id`, (req, res) => {
    const idParts = req.params.id.split('_');
    const idx = db[entity].findIndex((r) => matchesId(r, pk, idParts));
    if (idx === -1) return res.status(404).json({ error: 'Not found' });
    db[entity].splice(idx, 1);
    res.json({ deleted: true });
  });
});

// ---- reports (simplified logic, real enough to demo the UI) ----

app.get('/api/reports/at-risk-students', (req, res) => {
  const byEnrollment = {};
  db.attendance.forEach((a) => {
    (byEnrollment[a.enrollment_id] = byEnrollment[a.enrollment_id] || []).push(a);
  });
  const results = [];
  Object.entries(byEnrollment).forEach(([enrollmentId, rows]) => {
    rows.sort((a, b) => a.attendance_date.localeCompare(b.attendance_date));
    let streak = 0, start = null;
    rows.forEach((r, i) => {
      if (r.status === 'absent') {
        if (streak === 0) start = r.attendance_date;
        streak += 1;
      }
      const isLast = i === rows.length - 1;
      if ((r.status !== 'absent' || isLast) && streak >= 3) {
        const enrollment = db.enrollment.find((e) => e.enrollment_id == enrollmentId);
        const student = db.student.find((s) => s.student_id === enrollment.student_id);
        const course = db.course.find((c) => c.course_id === enrollment.course_id);
        results.push({
          student_id: student.student_id, first_name: student.first_name, last_name: student.last_name,
          course_name: course.course_name, consecutive_absences: streak,
          streak_start: start, streak_end: r.status === 'absent' ? r.attendance_date : rows[i - 1].attendance_date,
        });
      }
      if (r.status !== 'absent') streak = 0;
    });
  });
  res.json(results);
});

app.get('/api/reports/facilitator-mismatches', (req, res) => {
  const results = db.enrollment.filter((e) => e.facilitator_id && !db.facilitator_qualification.some(
    (fq) => fq.facilitator_id === e.facilitator_id && fq.course_id === e.course_id
  )).map((e) => {
    const f = db.facilitator.find((x) => x.facilitator_id === e.facilitator_id);
    const c = db.course.find((x) => x.course_id === e.course_id);
    return { enrollment_id: e.enrollment_id, facilitator_first_name: f.first_name, facilitator_last_name: f.last_name, course_name: c.course_name };
  });
  res.json(results);
});

app.get('/api/reports/exam-records', (req, res) => {
  const results = db.exam_attempt.map((ea) => {
    const e = db.enrollment.find((x) => x.enrollment_id === ea.enrollment_id);
    const s = db.student.find((x) => x.student_id === e.student_id);
    const c = db.course.find((x) => x.course_id === e.course_id);
    return { first_name: s.first_name, last_name: s.last_name, course_name: c.course_name, ...ea };
  });
  res.json(results);
});

app.get('/api/reports/intake', (req, res) => {
  const { from = '1900-01-01', to = '2999-12-31' } = req.query;
  res.json(db.student.filter((s) => s.enrollment_date >= from && s.enrollment_date <= to));
});

app.get('/api/reports/course-demand', (req, res) => {
  const counts = {};
  db.enrollment.forEach((e) => {
    const course = db.course.find((c) => c.course_id === e.course_id);
    const month = e.enrollment_date.slice(0, 7) + '-01';
    const key = `${course.course_name}|${month}`;
    counts[key] = (counts[key] || 0) + 1;
  });
  res.json(Object.entries(counts).map(([key, count]) => {
    const [course_name, intake_month] = key.split('|');
    return { course_name, intake_month, enrollment_count: count };
  }));
});

app.get('/api/reports/roster', (req, res) => {
  res.json(db.enrollment.map((e) => {
    const s = db.student.find((x) => x.student_id === e.student_id);
    const c = db.course.find((x) => x.course_id === e.course_id);
    const f = db.facilitator.find((x) => x.facilitator_id === e.facilitator_id);
    return {
      course_name: c.course_name, student_id: s.student_id, first_name: s.first_name, last_name: s.last_name,
      enrollment_status: e.enrollment_status,
      facilitator_first_name: f?.first_name || null, facilitator_last_name: f?.last_name || null,
    };
  }));
});

app.get('/api/reports/transcript/:studentId', (req, res) => {
  const studentId = Number(req.params.studentId);
  const results = db.enrollment.filter((e) => e.student_id === studentId).map((e) => {
    const c = db.course.find((x) => x.course_id === e.course_id);
    const cb = db.certification_body.find((x) => x.cert_body_id === c.cert_body_id);
    return {
      course_name: c.course_name, certification_body: cb?.body_name || null,
      enrollment_date: e.enrollment_date, enrollment_status: e.enrollment_status, final_result: e.final_result,
    };
  });
  res.json(results);
});

app.get('/api/reports/export/students', (req, res) => {
  res.json(db.student.map((s) => {
    const nk = db.next_of_kin.find((n) => n.student_id === s.student_id);
    return {
      ...s,
      next_of_kin_name: nk?.full_name || null, next_of_kin_national_id: nk?.national_id_number || null,
      next_of_kin_address: nk?.address || null, next_of_kin_phone: nk?.phone_number || null,
      next_of_kin_relationship: nk?.relationship || null,
    };
  }));
});

app.get('/api/reports/prerequisite-check', (req, res) => {
  const { studentId, courseId } = req.query;
  const course = db.course.find((c) => c.course_id === Number(courseId));
  if (!course) return res.json({ prerequisite_met: true, required_prerequisite: null });
  const prereq = db.course.find((c) => c.course_id === course.prerequisite_course_id);
  const met = !prereq || db.enrollment.some((e) => e.student_id === Number(studentId) && e.course_id === prereq.course_id && e.final_result === 'pass');
  res.json({ target_course: course.course_name, required_prerequisite: prereq?.course_name || null, prerequisite_met: met });
});

app.get('/api/health', (req, res) => res.json({ status: 'ok', mode: 'mock' }));

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => console.log(`Mock ITCA API (in-memory) listening on http://localhost:${PORT}`));
