from ...gateways.attendance_gateway import AttendanceGateway

def get_all_attendance():
    attendance_gateway = AttendanceGateway()
    return attendance_gateway.list_all()