from ...gateways.certification_body_gateway import CertificationBodyGateway

def delete_certification_body(id):
    certification_body_gateway = CertificationBodyGateway()
    certification_body_gateway.delete(id)
    return { "deleted": True }