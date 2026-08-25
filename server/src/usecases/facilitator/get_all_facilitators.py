from ...gateways.facilitator_gateway import FacilitatorGateway

def get_all_facilitators():
    facilitator_gateway = FacilitatorGateway()
    return facilitator_gateway.list_all()