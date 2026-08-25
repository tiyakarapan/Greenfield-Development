from ...gateways.course_gateway import CourseGateway

def delete_course(id):
    course_gateway = CourseGateway()
    course_gateway.delete(id)
    return { "deleted": True }