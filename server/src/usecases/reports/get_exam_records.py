from ...gateways.exam_attempt_gateway import ExamAttemptGateway
from ...gateways.enrollment_gateway import EnrollmentGateway
from ...gateways.student_gateway import StudentGateway
from ...gateways.course_gateway import CourseGateway
from ...util.array_util import find

def get_exam_records():
    exam_attempt_gateway = ExamAttemptGateway()
    enrollment_gateway = EnrollmentGateway()
    student_gateway = StudentGateway()
    course_gateway = CourseGateway()

    exam_attempts = exam_attempt_gateway.list_all()
    enrollments = enrollment_gateway.list_all()
    students = student_gateway.list_all()
    courses = course_gateway.list_all()
    
    exam_records = []

    for exam_attempt in exam_attempts:
        enrollment = find(enrollments, lambda x: x["enrollment_id"] == exam_attempt["enrollment_id"])
        student = find(students, lambda x: x["student_id"] == enrollment["student_id"])
        course = find(courses, lambda x: x["course_id"] == enrollment["course_id"])

        exam_records.append({
            "first_name": student["first_name"],
            "last_name": student["last_name"],
            "course_name": course["course_name"],
            "attempt_number": exam_attempt["attempt_number"],
            "exam_date": exam_attempt["exam_date"],
            "score": exam_attempt["score"],
            "pass_fail": exam_attempt["pass_fail"]
        })

    return exam_records