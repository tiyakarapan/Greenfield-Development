from .query_runner import QueryRunner

class EnrollmentGateway(QueryRunner):
    def __init__(self):
        super().__init__("enrollment", "enrollment_id")