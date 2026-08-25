from .query_runner import QueryRunner

class FacilitatorGateway():
    def __init__(self):
        self.query_runner = QueryRunner("facilitator", "facilitator_id")

    def list_all(self):
        return self.query_runner.list_all()

    def create(self, values):
        return self.query_runner.insert(values)

    def update(self, id, values):
        return self.query_runner.update(id, values)

    def delete(self, id):
        return self.query_runner.delete(id)