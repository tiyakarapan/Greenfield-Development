// src/config/entities.js
//
// One entry per table. This single file decides:
//  - what shows up in the sidebar
//  - what columns the table shows
//  - what fields the add/edit form renders, and how (text, date,
//    select, or a foreign-key dropdown pulling live data from another
//    entity)
//
// To add a new manageable table later: add one object here. No new
// components needed.

const STATUS_OPTIONS = ['active', 'at_risk', 'dropped', 'graduated'];
const ENROLLMENT_STATUS_OPTIONS = ['enrolled', 'completed', 'dropped', 'failed'];
const RESULT_OPTIONS = ['pass', 'fail'];
const ATTENDANCE_OPTIONS = ['present', 'absent', 'late'];
const SPONSOR_TYPE_OPTIONS = ['self', 'parent', 'guardian', 'company', 'bursary'];

export const entities = {
  student: {
    key: 'student',
    label: 'Students',
    singular: 'Student',
    pk: ['student_id'],
    displayField: (row) => `${row.first_name} ${row.last_name}`,
    tableColumns: ['student_id', 'first_name', 'last_name', 'email', 'status', 'enrollment_date'],
    statusField: 'status',
    fields: [
      { name: 'first_name', label: 'First name', type: 'text', required: true },
      { name: 'last_name', label: 'Last name', type: 'text', required: true },
      { name: 'national_id_number', label: 'National ID number', type: 'text', required: true },
      { name: 'email', label: 'Email', type: 'email', required: true },
      { name: 'address', label: 'Address', type: 'textarea', required: true },
      { name: 'date_of_birth', label: 'Date of birth', type: 'date', required: true },
      { name: 'enrollment_date', label: 'Enrollment date', type: 'date' },
      { name: 'status', label: 'Status', type: 'select', options: STATUS_OPTIONS, required: true },
      { name: 'medical_needs', label: 'Medical needs', type: 'textarea' },
      { name: 'medical_aid_provider', label: 'Medical aid provider', type: 'text' },
      { name: 'medical_aid_number', label: 'Medical aid number', type: 'text' },
    ],
  },

  next_of_kin: {
    key: 'next_of_kin',
    label: 'Next of Kin',
    singular: 'Next of Kin',
    pk: ['next_of_kin_id'],
    displayField: (row) => row.full_name,
    tableColumns: ['next_of_kin_id', 'full_name', 'relationship', 'phone_number', 'student_id'],
    fields: [
      { name: 'student_id', label: 'Student', type: 'fk', fk: 'student', required: true },
      { name: 'full_name', label: 'Full name', type: 'text', required: true },
      { name: 'national_id_number', label: 'National ID number', type: 'text', required: true },
      { name: 'phone_number', label: 'Phone number', type: 'text', required: true },
      { name: 'relationship', label: 'Relationship', type: 'text' },
      { name: 'address', label: 'Address', type: 'textarea', required: true },
    ],
  },

  sponsor: {
    key: 'sponsor',
    label: 'Sponsors',
    singular: 'Sponsor',
    pk: ['sponsor_id'],
    displayField: (row) => row.sponsor_name,
    tableColumns: ['sponsor_id', 'sponsor_name', 'sponsor_type', 'contact_email', 'contact_phone'],
    fields: [
      { name: 'sponsor_name', label: 'Sponsor name', type: 'text', required: true },
      { name: 'sponsor_type', label: 'Sponsor type', type: 'select', options: SPONSOR_TYPE_OPTIONS, required: true },
      { name: 'contact_email', label: 'Contact email', type: 'email' },
      { name: 'contact_phone', label: 'Contact phone', type: 'text' },
    ],
  },

  certification_body: {
    key: 'certification_body',
    label: 'Certification Bodies',
    singular: 'Certification Body',
    pk: ['cert_body_id'],
    displayField: (row) => row.body_name,
    tableColumns: ['cert_body_id', 'body_name'],
    fields: [
      { name: 'body_name', label: 'Body name', type: 'text', required: true },
    ],
  },

  course: {
    key: 'course',
    label: 'Courses',
    singular: 'Course',
    pk: ['course_id'],
    displayField: (row) => row.course_name,
    tableColumns: ['course_id', 'course_name', 'duration_weeks', 'cert_body_id', 'prerequisite_course_id'],
    fields: [
      { name: 'course_name', label: 'Course name', type: 'text', required: true },
      { name: 'duration_weeks', label: 'Duration (weeks)', type: 'number', required: true },
      { name: 'cert_body_id', label: 'Certification body', type: 'fk', fk: 'certification_body' },
      { name: 'prerequisite_course_id', label: 'Prerequisite course', type: 'fk', fk: 'course' },
    ],
  },

  facilitator: {
    key: 'facilitator',
    label: 'Facilitators',
    singular: 'Facilitator',
    pk: ['facilitator_id'],
    displayField: (row) => `${row.first_name} ${row.last_name}`,
    tableColumns: ['facilitator_id', 'first_name', 'last_name', 'email', 'phone_number'],
    fields: [
      { name: 'first_name', label: 'First name', type: 'text', required: true },
      { name: 'last_name', label: 'Last name', type: 'text', required: true },
      { name: 'email', label: 'Email', type: 'email', required: true },
      { name: 'phone_number', label: 'Phone number', type: 'text' },
    ],
  },

  facilitator_qualification: {
    key: 'facilitator_qualification',
    label: 'Qualifications',
    singular: 'Qualification',
    pk: ['facilitator_id', 'course_id'],
    displayField: (row) => `#${row.facilitator_id} → #${row.course_id}`,
    tableColumns: ['facilitator_id', 'course_id', 'qualified_date'],
    fields: [
      { name: 'facilitator_id', label: 'Facilitator', type: 'fk', fk: 'facilitator', required: true },
      { name: 'course_id', label: 'Course', type: 'fk', fk: 'course', required: true },
      { name: 'qualified_date', label: 'Qualified date', type: 'date' },
    ],
  },

  enrollment: {
    key: 'enrollment',
    label: 'Enrollments',
    singular: 'Enrollment',
    pk: ['enrollment_id'],
    displayField: (row) => `Enrollment #${row.enrollment_id}`,
    tableColumns: ['enrollment_id', 'student_id', 'course_id', 'facilitator_id', 'enrollment_status', 'final_result'],
    statusField: 'enrollment_status',
    fields: [
      { name: 'student_id', label: 'Student', type: 'fk', fk: 'student', required: true },
      { name: 'course_id', label: 'Course', type: 'fk', fk: 'course', required: true },
      { name: 'facilitator_id', label: 'Facilitator', type: 'fk', fk: 'facilitator' },
      { name: 'sponsor_id', label: 'Sponsor', type: 'fk', fk: 'sponsor' },
      { name: 'enrollment_date', label: 'Enrollment date', type: 'date' },
      { name: 'enrollment_status', label: 'Status', type: 'select', options: ENROLLMENT_STATUS_OPTIONS, required: true },
      { name: 'final_result', label: 'Final result', type: 'select', options: RESULT_OPTIONS },
    ],
  },

  exam_attempt: {
    key: 'exam_attempt',
    label: 'Exam Attempts',
    singular: 'Exam Attempt',
    pk: ['attempt_id'],
    displayField: (row) => `Attempt #${row.attempt_number}`,
    tableColumns: ['attempt_id', 'enrollment_id', 'attempt_number', 'exam_date', 'score', 'pass_fail'],
    statusField: 'pass_fail',
    fields: [
      { name: 'enrollment_id', label: 'Enrollment', type: 'fk', fk: 'enrollment', required: true },
      { name: 'attempt_number', label: 'Attempt number', type: 'number', required: true },
      { name: 'exam_date', label: 'Exam date', type: 'date', required: true },
      { name: 'score', label: 'Score (0-100)', type: 'number' },
      { name: 'pass_fail', label: 'Result', type: 'select', options: RESULT_OPTIONS },
      { name: 'access_key', label: 'Access key', type: 'text' },
    ],
  },

  attendance: {
    key: 'attendance',
    label: 'Attendance',
    singular: 'Attendance Record',
    pk: ['attendance_id'],
    displayField: (row) => `${row.attendance_date}`,
    tableColumns: ['attendance_id', 'enrollment_id', 'attendance_date', 'status', 'notes'],
    statusField: 'status',
    fields: [
      { name: 'enrollment_id', label: 'Enrollment', type: 'fk', fk: 'enrollment', required: true },
      { name: 'attendance_date', label: 'Date', type: 'date', required: true },
      { name: 'status', label: 'Status', type: 'select', options: ATTENDANCE_OPTIONS, required: true },
      { name: 'notes', label: 'Notes', type: 'textarea' },
    ],
  },
};

export const navGroups = [
  { title: 'People', items: ['student', 'next_of_kin', 'facilitator', 'sponsor'] },
  { title: 'Academics', items: ['course', 'certification_body', 'facilitator_qualification'] },
  { title: 'Records', items: ['enrollment', 'attendance', 'exam_attempt'] },
];
