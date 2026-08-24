from ...gateways.certification_body import CertificationBodyGateway

def update_certification_body(id, values):
    certification_body_gateway = CertificationBodyGateway()
    return certification_body_gateway.update(id, values)