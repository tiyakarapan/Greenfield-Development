from ...gateways.enrollment_gateway import EnrollmentGateway

def delete_enrollment(id):
    enrollment_gateway = EnrollmentGateway()
    enrollment_gateway.delete(id)
    return { "deleted": True }