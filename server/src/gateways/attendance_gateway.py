from .query_runner import QueryRunner

class AttendanceGateway(QueryRunner):
    def __init__(self):
        super().__init__("attendance", "attendance_id")