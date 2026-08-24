from ...gateways.next_of_kin_gateway import NextOfKinGateway

def get_all_next_of_kin():
    next_of_kin_gateway = NextOfKinGateway()
    return next_of_kin_gateway.list_all()