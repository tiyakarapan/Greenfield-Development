from ...gateways.enrollment_gateway import EnrollmentGateway
from ...gateways.facilitator_gateway import FacilitatorGateway
from ...gateways.course_gateway import CourseGateway
from ...gateways.facilitator_qualification_gateway import FacilitatorQualificationGateway

def get_facilitator_mismatches():
    enrollment_gateway = EnrollmentGateway()
    facilitator_gateway = FacilitatorGateway()
    course_gateway = CourseGateway()
    facilitator_qualification_gateway = FacilitatorQualificationGateway()

    enrollments = enrollment_gateway.list_all()
    facilitators = facilitator_gateway.list_all()
    courses = course_gateway.list_all()
    qualifications = facilitator_qualification_gateway.list_all()

    result = []

    for enrollment in enrollments:
        facilitator = next((f for f in facilitators if f["facilitator_id"] == enrollment["facilitator"]), None)
        course = next((c for c in courses if c["course_id"] == enrollment["course_id"]), None)

        if facilitator is None or course is None:
            continue

        is_qualified = any(
            q["facilitator_id"] == facilitator["facilitator_id"] and q["course_id"] == course["course_id"]
            for q in qualifications
        )

        if is_qualified:
            continue

        result.append({
            "enrollment_id": enrollment["enrollment_id"],
            "facilitator_first_name": facilitator["first_name"],
            "facilitator_last_name": facilitator["last_name"],
            "course_name": course["course_name"]
        })

    return result