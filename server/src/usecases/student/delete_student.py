from ...gateways.student_gateway import StudentGateway

def delete_student(id):
    student_gateway = StudentGateway()
    student_gateway.delete(id)
    return { "deleted": True }