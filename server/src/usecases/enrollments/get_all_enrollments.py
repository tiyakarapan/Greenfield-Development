from ...gateways.enrollment_gateway import EnrollmentGateway

def get_all_enrollments():
    enrollment_gateway = EnrollmentGateway()
    return enrollment_gateway.list_all()