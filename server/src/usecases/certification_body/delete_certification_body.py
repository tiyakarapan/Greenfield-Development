from ...gateways.certification_body import CertificationBodyGateway

def delete_certification_body(id):
    certification_body_gateway = CertificationBodyGateway()
    return certification_body_gateway.delete(id)