from datetime import timedelta
from ...gateways.student_gateway import StudentGateway
from ...gateways.enrollment_gateway import EnrollmentGateway
from ...gateways.course_gateway import CourseGateway
from ...gateways.attendance_gateway import AttendanceGateway

def get_at_risk_students():
    student_gateway = StudentGateway()
    enrollment_gateway = EnrollmentGateway()
    course_gateway = CourseGateway()
    attendance_gateway = AttendanceGateway()

    students = student_gateway.list_all()
    enrollments = enrollment_gateway.list_all()
    courses = course_gateway.list_all()
    attendance_records = attendance_gateway.list_all()

    result = []

    for enrollment in enrollments:
        student = next((s for s in students if s["student_id"] == enrollment["student_id"]), None)
        course = next((c for c in courses if c["course_id"] == enrollment["course_id"]), None)

        if student is None or course is None:
            continue

        enrollment_attendance = [
            a for a in attendance_records
            if a["enrollment_id"] == enrollment["enrollment_id"] and a["status"] == "absent"
        ]
        enrollment_attendance.sort(key=lambda a: a["attendance_date"])

        streak_start = None
        previous_date = None
        streak_length = 0

        def close_streak(end_date):
            if streak_length >= 3:
                result.append({
                    "student_id": student["student_id"],
                    "first_name": student["first_name"],
                    "last_name": student["last_name"],
                    "course_name": course["course_name"],
                    "consecutive_absences": streak_length,
                    "streak_start": streak_start,
                    "streak_end": end_date
                })

        for record in enrollment_attendance:
            current_date = record["attendance_date"]

            if previous_date is not None and (current_date - previous_date) == timedelta(days=1):
                streak_length += 1
            else:
                close_streak(previous_date)
                streak_start = current_date
                streak_length = 1

            previous_date = current_date

        close_streak(previous_date)

    return result