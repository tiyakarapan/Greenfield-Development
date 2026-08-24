from ...gateways.student_gateway import StudentGateway

def update_student(id, values):
    student_gateway = StudentGateway()
    return student_gateway.update(id, values)