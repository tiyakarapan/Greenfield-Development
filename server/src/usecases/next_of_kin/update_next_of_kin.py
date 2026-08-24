from ...gateways.next_of_kin_gateway import NextOfKinGateway

def update_next_of_kin(id, values):
    next_of_kin_gateway = NextOfKinGateway()
    return next_of_kin_gateway.update(id, values)