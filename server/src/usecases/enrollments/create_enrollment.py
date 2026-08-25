from ...gateways.enrollment_gateway import EnrollmentGateway

def create_enrollment(values):
    enrollment_gateway = EnrollmentGateway()
    return enrollment_gateway.create(values)