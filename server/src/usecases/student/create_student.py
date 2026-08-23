from ...gateways.student_gateway import StudentGateway

def create_student(values):
    student_gateway = StudentGateway()
    return student_gateway.create(values)