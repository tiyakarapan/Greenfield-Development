from collections import defaultdict
from ...gateways.enrollment_gateway import EnrollmentGateway
from ...gateways.course_gateway import CourseGateway

def get_course_demand():
    enrollment_gateway = EnrollmentGateway()
    course_gateway = CourseGateway()

    enrollments = enrollment_gateway.list_all()
    courses = course_gateway.list_all()

    counts = defaultdict(int)

    for enrollment in enrollments:
        course = next((c for c in courses if c["course_id"] == enrollment["course_id"]), None)
        if course is None:
            continue

        enrollment_date = enrollment["enrollment_date"]
        intake_month = enrollment_date.strftime("%Y-%m")

        key = (course["course_name"], intake_month)
        counts[key] += 1

    result = []
    for (course_name, intake_month), enrollment_count in counts.items():
        result.append({
            "course_name": course_name,
            "intake_month": intake_month,
            "enrollment_count": enrollment_count
        })

    return result