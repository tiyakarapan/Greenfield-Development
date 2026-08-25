from ...gateways.facilitator_qualification_gateway import FacilitatorQualificationGateway

def delete_facilitator_qualification(id):
    facilitator_qualification_gateway = FacilitatorQualificationGateway()
    facilitator_qualification_gateway.delete(id)
    return { "deleted": True }