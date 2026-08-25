from ...gateways.exam_attempt_gateway import ExamAttemptGateway

def get_all_exam_attempts():
    exam_attempt_gateway = ExamAttemptGateway()
    return exam_attempt_gateway.list_all()