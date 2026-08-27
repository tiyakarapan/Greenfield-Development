# ITCA API Contract

This is the interface the frontend expects. As long as your backend
matches this — whatever language/framework you build it in — the
frontend will work against it without changes.

Base path: everything is under `/api`.

## Conventions

- All responses are JSON.
- Dates: `YYYY-MM-DD` or ISO timestamps (frontend truncates to date on display).
- On error, respond with a non-2xx status and a JSON body: `{ "error": "human-readable message" }`.
  The frontend displays this message directly to the user, so make it
  readable (e.g. "Facilitator is not qualified to teach this course" not
  a raw stack trace).
- Empty/optional fields: `null`.

## Entity endpoints (CRUD)

The frontend calls the same 5 endpoints for every table below. Replace
`:entity` with the table name and `:id` with its primary key value.
For tables with a **composite primary key** (only `facilitator_qualification`),
`:id` is the key parts joined with `_`, e.g. `3_7` for facilitator_id=3, course_id=7.

| Method | Path | Behavior |
|---|---|---|
| GET | `/api/:entity` | Return array of all rows |
| GET | `/api/:entity/:id` | Return single row, 404 if missing |
| POST | `/api/:entity` | Create row from JSON body, return the created row (201) |
| PUT | `/api/:entity/:id` | Update row from JSON body, return updated row |
| DELETE | `/api/:entity/:id` | Delete row, return `{ "deleted": true }` |

Entities (table name = URL segment = JSON keys, matching `schema.sql` columns):

- `student` — pk `student_id`
- `next_of_kin` — pk `next_of_kin_id`
- `sponsor` — pk `sponsor_id`
- `certification_body` — pk `cert_body_id`
- `course` — pk `course_id`
- `facilitator` — pk `facilitator_id`
- `facilitator_qualification` — pk `facilitator_id` + `course_id` (composite)
- `enrollment` — pk `enrollment_id`
- `exam_attempt` — pk `attempt_id`
- `attendance` — pk `attendance_id`

Full column lists live in `frontend/src/config/entities.js` (`fields` array
per entity) — that's the source of truth for what a create/update payload
should contain.

## Report endpoints

| Method | Path | Query params | Returns |
|---|---|---|---|
| GET | `/api/reports/at-risk-students` | — | Students with 3+ consecutive absences |
| GET | `/api/reports/facilitator-mismatches` | — | Enrollments where facilitator isn't qualified for the course |
| GET | `/api/reports/exam-records` | — | All exam attempts with student/course names |
| GET | `/api/reports/intake` | `from`, `to` (dates) | Students enrolled in that date range |
| GET | `/api/reports/course-demand` | — | Enrollment counts per course per intake month |
| GET | `/api/reports/roster` | — | All enrollments grouped by course |
| GET | `/api/reports/transcript/:studentId` | — | One student's enrollment + result history |
| GET | `/api/reports/export/students` | — | Full student export (backs `student_export` view) |
| GET | `/api/reports/prerequisite-check` | `studentId`, `courseId` | `{ prerequisite_met, required_prerequisite, target_course }` |

Exact response field names each report expects are visible in
`frontend/src/pages/Dashboard.jsx` (the `columns` arrays reference the
field names directly).

## CORS

The backend needs to allow requests from the frontend's origin (or just
enable permissive CORS for development, e.g. Express's `cors()` middleware).
