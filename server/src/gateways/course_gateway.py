from .query_runner import QueryRunner

class CourseGateway(QueryRunner):
    def __init__(self):
        super().__init__("course", "course_id")    