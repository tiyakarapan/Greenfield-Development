// mock-server/data.js
// In-memory fake data, shaped exactly like the real API's rows, so the
// frontend can run against this with zero setup. Not the real backend —
// swap for your teammates' API once it's ready (see README.md).

let nextId = { student: 6, next_of_kin: 4, sponsor: 4, certification_body: 3,
  course: 5, facilitator: 4, enrollment: 6, exam_attempt: 5, attendance: 9 };

const db = {
  student: [
    { student_id: 1, first_name: 'Lindiwe', last_name: 'Khumalo', national_id_number: '0001015800083', address: '1 Main Rd, Durban', email: 'lindiwe.khumalo@student.itca.ac.za', date_of_birth: '2000-01-01', medical_needs: null, medical_aid_provider: null, medical_aid_number: null, enrollment_date: '2024-01-15', status: 'active' },
    { student_id: 2, first_name: 'Thabo', last_name: 'Mahlangu', national_id_number: '0002015800084', address: '2 Church St, Pinetown', email: 'thabo.mahlangu@student.itca.ac.za', date_of_birth: '2001-02-02', medical_needs: null, medical_aid_provider: null, medical_aid_number: null, enrollment_date: '2024-01-15', status: 'active' },
    { student_id: 3, first_name: 'Aisha', last_name: 'Patel', national_id_number: '0003015800085', address: '3 Ridge Rd, Westville', email: 'aisha.patel@student.itca.ac.za', date_of_birth: '2002-03-03', medical_needs: null, medical_aid_provider: null, medical_aid_number: null, enrollment_date: '2024-01-15', status: 'active' },
    { student_id: 4, first_name: 'Sipho', last_name: 'Dlamini', national_id_number: '0004015800086', address: '4 Berea Rd, Durban', email: 'sipho.dlamini@student.itca.ac.za', date_of_birth: '2000-04-04', medical_needs: null, medical_aid_provider: null, medical_aid_number: null, enrollment_date: '2024-01-15', status: 'at_risk' },
    { student_id: 5, first_name: 'Naledi', last_name: 'Botha', national_id_number: '0005015800087', address: '3 Kloof St, Kloof', email: 'naledi.botha@student.itca.ac.za', date_of_birth: '2002-07-22', medical_needs: null, medical_aid_provider: null, medical_aid_number: null, enrollment_date: '2024-07-01', status: 'active' },
  ],
  next_of_kin: [
    { next_of_kin_id: 1, student_id: 1, full_name: 'Nomsa Khumalo', national_id_number: '7001015800081', address: '1 Main Rd, Durban', phone_number: '0821112222', relationship: 'mother' },
    { next_of_kin_id: 2, student_id: 2, full_name: 'John Mahlangu', national_id_number: '7002015800082', address: '2 Church St, Pinetown', phone_number: '0823334444', relationship: 'father' },
    { next_of_kin_id: 3, student_id: 3, full_name: 'Farah Patel', national_id_number: '7003015800083', address: '3 Ridge Rd, Westville', phone_number: '0825556666', relationship: 'mother' },
  ],
  sponsor: [
    { sponsor_id: 1, sponsor_name: 'Self-funded', sponsor_type: 'self', contact_email: null, contact_phone: null },
    { sponsor_id: 2, sponsor_name: 'MTN Bursary Fund', sponsor_type: 'bursary', contact_email: 'bursary@mtn.co.za', contact_phone: '0111234567' },
    { sponsor_id: 3, sponsor_name: 'Dlamini Family', sponsor_type: 'parent', contact_email: null, contact_phone: '0834445555' },
  ],
  certification_body: [
    { cert_body_id: 1, body_name: 'CompTIA' },
    { cert_body_id: 2, body_name: 'Cisco' },
    { cert_body_id: 3, body_name: 'Microsoft' },
  ],
  course: [
    { course_id: 1, course_name: 'IT Fundamentals', duration_weeks: 8, cert_body_id: 1, prerequisite_course_id: null },
    { course_id: 2, course_name: 'CompTIA A+', duration_weeks: 12, cert_body_id: 1, prerequisite_course_id: 1 },
    { course_id: 3, course_name: 'Cisco CCNA', duration_weeks: 16, cert_body_id: 2, prerequisite_course_id: 1 },
    { course_id: 4, course_name: 'Microsoft Azure Fundamentals (AZ-900)', duration_weeks: 6, cert_body_id: 3, prerequisite_course_id: null },
  ],
  facilitator: [
    { facilitator_id: 1, first_name: 'Sihle', last_name: 'Ndlovu', email: 'sihle.ndlovu@itca.ac.za', phone_number: '0831110000' },
    { facilitator_id: 2, first_name: 'Tiya', last_name: 'Mokoena', email: 'tiya.mokoena@itca.ac.za', phone_number: '0831110001' },
    { facilitator_id: 3, first_name: 'Siphelele', last_name: 'Zulu', email: 'siphelele.zulu@itca.ac.za', phone_number: '0831110002' },
  ],
  facilitator_qualification: [
    { facilitator_id: 1, course_id: 1, qualified_date: '2023-06-01' },
    { facilitator_id: 1, course_id: 2, qualified_date: '2023-06-01' },
    { facilitator_id: 2, course_id: 1, qualified_date: '2023-06-01' },
    { facilitator_id: 2, course_id: 3, qualified_date: '2023-08-01' },
    { facilitator_id: 3, course_id: 4, qualified_date: '2024-01-10' },
  ],
  enrollment: [
    { enrollment_id: 1, student_id: 1, course_id: 1, facilitator_id: 1, sponsor_id: 1, enrollment_date: '2024-01-15', enrollment_status: 'completed', final_result: 'pass' },
    { enrollment_id: 2, student_id: 2, course_id: 1, facilitator_id: 2, sponsor_id: 1, enrollment_date: '2024-01-15', enrollment_status: 'completed', final_result: 'pass' },
    { enrollment_id: 3, student_id: 3, course_id: 4, facilitator_id: 3, sponsor_id: 2, enrollment_date: '2024-01-15', enrollment_status: 'completed', final_result: 'pass' },
    { enrollment_id: 4, student_id: 4, course_id: 1, facilitator_id: 1, sponsor_id: 3, enrollment_date: '2024-01-15', enrollment_status: 'enrolled', final_result: null },
    { enrollment_id: 5, student_id: 1, course_id: 2, facilitator_id: 1, sponsor_id: 1, enrollment_date: '2024-07-01', enrollment_status: 'enrolled', final_result: null },
  ],
  exam_attempt: [
    { attempt_id: 1, enrollment_id: 1, attempt_number: 1, exam_date: '2024-03-08', score: 78.5, pass_fail: 'pass', access_key: 'AK-1001' },
    { attempt_id: 2, enrollment_id: 2, attempt_number: 1, exam_date: '2024-03-08', score: 65.0, pass_fail: 'pass', access_key: 'AK-1002' },
    { attempt_id: 3, enrollment_id: 4, attempt_number: 1, exam_date: '2024-03-08', score: 41.0, pass_fail: 'fail', access_key: 'AK-1003' },
    { attempt_id: 4, enrollment_id: 4, attempt_number: 2, exam_date: '2024-04-12', score: 55.5, pass_fail: 'fail', access_key: 'AK-1004' },
  ],
  attendance: [
    { attendance_id: 1, enrollment_id: 4, attendance_date: '2024-07-01', status: 'present', notes: null },
    { attendance_id: 2, enrollment_id: 4, attendance_date: '2024-07-02', status: 'absent', notes: null },
    { attendance_id: 3, enrollment_id: 4, attendance_date: '2024-07-03', status: 'absent', notes: null },
    { attendance_id: 4, enrollment_id: 4, attendance_date: '2024-07-04', status: 'absent', notes: 'no message from guardian' },
    { attendance_id: 5, enrollment_id: 1, attendance_date: '2024-01-16', status: 'present', notes: null },
  ],
};

module.exports = { db, nextId };
