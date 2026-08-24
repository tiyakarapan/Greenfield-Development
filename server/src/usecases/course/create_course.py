from ...gateways.course_gateway import CourseGateway

def create_course(values):
    course_gateway = CourseGateway()
    return course_gateway.create(values)