from ...gateways.attendance_gateway import AttendanceGateway

def create_attendance(values):
    attendance_gateway = AttendanceGateway()
    return attendance_gateway.create(values)