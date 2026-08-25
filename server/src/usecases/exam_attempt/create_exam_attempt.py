from ...gateways.exam_attempt_gateway import ExamAttemptGateway

def create_exam_attempt(values):
    exam_attempt_gateway = ExamAttemptGateway()
    return exam_attempt_gateway.create(values)