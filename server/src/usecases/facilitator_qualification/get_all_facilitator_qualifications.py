from ...gateways.facilitator_qualification_gateway import FacilitatorQualificationGateway

def get_all_facilitator_qualifications():
    facilitator_qualification_gateway = FacilitatorQualificationGateway()
    return facilitator_qualification_gateway.list_all()