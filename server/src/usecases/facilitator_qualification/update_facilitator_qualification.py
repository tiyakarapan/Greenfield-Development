from ...gateways.facilitator_qualification_gateway import FacilitatorQualificationGateway

def update_facilitator_qualification(id, values):
    facilitator_qualification_gateway = FacilitatorQualificationGateway()
    return facilitator_qualification_gateway.update(id, values)