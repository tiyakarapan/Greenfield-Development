from ...gateways.student_gateway import StudentGateway

def get_all_students():
    student_gateway = StudentGateway()
    return student_gateway.list_all()