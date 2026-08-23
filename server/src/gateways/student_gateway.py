from .query_runner import QueryRunner

class StudentGateway():
    def __init__(self):
        self.query_runner = QueryRunner("student", "student_id")

    def list_all(self):
        return self.query_runner.list_all([
            "student_id",
            "first_name",
            "last_name",
            "national_id_number",
            "email",
            "address",
            "date_of_birth",
            "enrollment_date",
            "status",
            "medical_needs",
            "medical_aid_provider",
            "medical_aid_number"
        ])

    def create(self, values):
        return self.query_runner.insert(values)

    def update(self, id, values):
        return self.query_runner.update(id, values)

    def delete(self, id):
        return self.query_runner.delete(id)