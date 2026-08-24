from .query_runner import QueryRunner

class SponsorGateway():
    def __init__(self):
        self.query_runner = QueryRunner("sponsor", "sponsor_id")

    def list_all(self):
        return self.query_runner.list_all([
            "sponsor_name",
            "sponsor_type",
            "contact_email",
            "contact_phone",
            "sponsor_id"
        ])

    def create(self, values):
        return self.query_runner.insert(values)

    def update(self, id, values):
        return self.query_runner.update(id, values)

    def delete(self, id):
        return self.query_runner.delete(id)