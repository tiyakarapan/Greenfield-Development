from ...gateways.sponsor_gateway import SponsorGateway

def create_sponsor(values):
    sponsor_gateway = SponsorGateway()
    return sponsor_gateway.create(values)