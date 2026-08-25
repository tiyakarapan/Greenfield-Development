from ...gateways.facilitator_gateway import FacilitatorGateway

def create_facilitator(values):
    facilitator_gateway = FacilitatorGateway()
    return facilitator_gateway.create(values)