from ...gateways.course_gateway import CourseGateway

def delete_course(id):
    course_gateway = CourseGateway()
    return course_gateway.delete(id)