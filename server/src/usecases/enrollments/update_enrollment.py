from ...gateways.enrollment_gateway import EnrollmentGateway

def update_enrollment(id, values):
    enrollment_gateway = EnrollmentGateway()
    return enrollment_gateway.update(id, values)