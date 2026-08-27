from ...gateways.enrollment_gateway import EnrollmentGateway
from ...gateways.course_gateway import CourseGateway
from ...gateways.certification_body_gateway import CertificationBodyGateway

def get_transcript(student_id):
    enrollment_gateway = EnrollmentGateway()
    course_gateway = CourseGateway()
    certification_body_gateway = CertificationBodyGateway()

    enrollments = enrollment_gateway.list_all()
    courses = course_gateway.list_all()
    certification_bodies = certification_body_gateway.list_all()

    result = []

    for enrollment in enrollments:
        if str(enrollment["student_id"]) != str(student_id):
            continue

        course = next((c for c in courses if c["course_id"] == enrollment["course_id"]), None)
        if course is None:
            continue

        certification_body = next((cb for cb in certification_bodies if cb["cert_body_id"] == course["cert_body_id"]), None)

        result.append({
            "course_name": course["course_name"],
            "certification_body": certification_body["body_name"] if certification_body else None,
            "enrollment_date": enrollment["enrollment_date"],
            "enrollment_status": enrollment["enrollment_status"],
            "final_result": enrollment["final_result"]
        })

    return result