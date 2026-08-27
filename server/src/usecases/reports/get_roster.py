from ...gateways.student_gateway import StudentGateway
from ...gateways.enrollment_gateway import EnrollmentGateway
from ...gateways.facilitator_gateway import FacilitatorGateway
from ...gateways.course_gateway import CourseGateway

def get_roster():
    student_gateway = StudentGateway()
    enrollment_gateway = EnrollmentGateway()
    facilitator_gateway = FacilitatorGateway()
    course_gateway = CourseGateway()

    students = student_gateway.list_all()
    enrollments = enrollment_gateway.list_all()
    facilitators = facilitator_gateway.list_all()
    courses = course_gateway.list_all()

    result = []

    

    for enrollment in enrollments:
        student_for_enrollment = None
        for student in students:
            if student["student_id"] == enrollment["student_id"]:
                student_for_enrollment = student
        course_for_enrollment = None
        for course in courses:
            if course["course_id"] == enrollment["course_id"]:
                course_for_enrollment = course   
        facilitator_for_enrollment = None
        for facilitator in facilitators:
            if facilitator["facilitator_id"] == enrollment["facilitator_id"]:
                facilitator_for_enrollment = facilitator    

        result.append({
            "student_id" : enrollment["student_id"],
            "first_name" : student_for_enrollment["first_name"],
            "last_name" : student_for_enrollment["last_name"],
            "course_name" : course_for_enrollment["course_name"],
            "enrollment_status" : enrollment["enrollment_status"],
            "facilitator_first_name" : facilitator_for_enrollment["first_name"],
            "facilitator_last_name" : facilitator_for_enrollment["last_name"]
        })
    
    return result