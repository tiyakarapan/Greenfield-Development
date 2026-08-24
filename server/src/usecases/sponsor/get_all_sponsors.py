from ...gateways.sponsor_gateway import SponsorGateway

def get_all_sponsors():
    sponsor_gateway = SponsorGateway()
    return sponsor_gateway.list_all()