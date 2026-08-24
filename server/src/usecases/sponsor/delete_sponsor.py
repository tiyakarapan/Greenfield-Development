from ...gateways.sponsor_gateway import SponsorGateway

def delete_sponsor(id):
    sponsor_gateway = SponsorGateway()
    sponsor_gateway.delete(id)
    return { "deleted": True }