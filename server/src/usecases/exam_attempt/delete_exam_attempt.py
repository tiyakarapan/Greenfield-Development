from ...gateways.exam_attempt_gateway import ExamAttemptGateway

def delete_exam_attempt(id):
    exam_attempt_gateway = ExamAttemptGateway()
    return exam_attempt_gateway.delete(id)