from ...gateways.attendance_gateway import AttendanceGateway

def delete_attendance(id):
    attendance_gateway = AttendanceGateway()
    return attendance_gateway.delete(id)