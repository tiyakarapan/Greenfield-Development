from .query_runner import QueryRunner

class CourseGateway():
    def __init__(self):
        self.query_runner = QueryRunner("course", "course_id")

    def list_all(self):
        return self.query_runner.list_all([
            "course_id",
            "course_name",
            "duration_weeks",
            "cert_body_id",
            "prerequisite_course_id"
        ])

    def create(self, values):
        return self.query_runner.insert(values)

    def update(self, id, values):
        return self.query_runner.update(id, values)

    def delete(self, id):
        return self.query_runner.delete(id)