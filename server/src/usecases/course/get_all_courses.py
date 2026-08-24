from ...gateways.course_gateway import CourseGateway

def get_all_courses():
    course_gateway = CourseGateway()
    return course_gateway.list_all()