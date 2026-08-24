from ...gateways.next_of_kin_gateway import NextOfKinGateway

def create_next_of_kin(values):
    next_of_kin_gateway = NextOfKinGateway()
    return next_of_kin_gateway.create(values)