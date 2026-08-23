from .query_runner import QueryRunner

class CertificationBodyGateway(QueryRunner):
    def __init__(self):
        super().__init__("certification_body", "cert_body_id")