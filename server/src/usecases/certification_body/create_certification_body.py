from ...gateways.certification_body_gateway import CertificationBodyGateway

def create_certification_body(values):
    certification_body_gateway = CertificationBodyGateway()
    return certification_body_gateway.create(values)