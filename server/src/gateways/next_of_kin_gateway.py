from .query_runner import QueryRunner

class NextOfKinGateway():
    def __init__(self):
        self.query_runner = QueryRunner("next_of_kin", "next_of_kin_id")

    def list_all(self):
        return self.query_runner.list_all([
            "next_of_kin_id",
            "student_id",
            "full_name",
            "national_id_number",
            "address",
            "phone_number",
            "relationship",
        ])

    def create(self, values):
        return self.query_runner.insert(values)

    def update(self, id, values):
        return self.query_runner.update(id, values)

    def delete(self, id):
        return self.query_runner.delete(id)