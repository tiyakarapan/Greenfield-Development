from .query_runner import QueryRunner

class ExamAttemptGateway():
    def __init__(self):
        self.query_runner = QueryRunner("exam_attempt", "attempt_id")

    def list_all(self):
        return self.query_runner.list_all([
            "attempt_id",
            "enrollment_id",
            "attempt_number",
            "exam_date",
            "score",
            "pass_fail",
            "access_key"
        ])

    def create(self, values):
        return self.query_runner.insert(values)

    def update(self, id, values):
        return self.query_runner.update(id, values)

    def delete(self, id):
        return self.query_runner.delete(id)