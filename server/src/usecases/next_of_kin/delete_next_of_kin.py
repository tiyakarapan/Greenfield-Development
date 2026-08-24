from ...gateways.next_of_kin_gateway import NextOfKinGateway

def delete_next_of_kin(id):
    next_of_kin_gateway = NextOfKinGateway()
    next_of_kin_gateway.delete(id)
    return { "deleted": True }