from ...gateways.facilitator_gateway import FacilitatorGateway

def update_facilitator(id, values):
    facilitator_gateway = FacilitatorGateway()
    return facilitator_gateway.update(id, values)