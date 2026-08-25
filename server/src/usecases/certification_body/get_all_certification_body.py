from ...gateways.certification_body_gateway import CertificationBodyGateway

def get_all_certification_body():
    certification_body_gateway = CertificationBodyGateway()
    return certification_body_gateway.list_all()