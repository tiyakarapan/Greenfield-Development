from ...gateways.course_gateway import CourseGateway

def update_course(id, values):
    course_gateway = CourseGateway()
    return course_gateway.update(id, values)