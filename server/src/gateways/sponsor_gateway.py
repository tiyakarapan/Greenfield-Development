from .query_runner import QueryRunner


class SponsorGateway(QueryRunner):
    def __init__(self):
        super().__init__("sponsor", "sponsor_id")