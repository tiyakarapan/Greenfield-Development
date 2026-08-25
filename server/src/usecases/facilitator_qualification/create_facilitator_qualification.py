from ...gateways.facilitator_qualification_gateway import FacilitatorQualificationGateway

def create_facilitator_qualification(values):
    facilitator_qualification_gateway = FacilitatorQualificationGateway()
    return facilitator_qualification_gateway.create(values)