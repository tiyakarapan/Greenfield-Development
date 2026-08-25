from ...gateways.exam_attempt_gateway import ExamAttemptGateway

def update_exam_attempt(id, values):
    exam_attempt_gateway = ExamAttemptGateway()
    return exam_attempt_gateway.update(id, values)