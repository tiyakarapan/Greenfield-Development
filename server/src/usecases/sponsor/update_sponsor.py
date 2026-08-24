from ...gateways.sponsor_gateway import SponsorGateway

def update_sponsor(id, values):
    sponsor_gateway = SponsorGateway()
    return sponsor_gateway.update(id, values)