from ...gateways.attendance_gateway import AttendanceGateway

def update_attendance(id, values):
    attendance_gateway = AttendanceGateway()
    return attendance_gateway.update(id, values)