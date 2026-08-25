from ...gateways.facilitator_gateway import FacilitatorGateway

def delete_facilitator(id):
    facilitator_gateway = FacilitatorGateway()
    facilitator_gateway.delete(id)
    return { "deleted": True }