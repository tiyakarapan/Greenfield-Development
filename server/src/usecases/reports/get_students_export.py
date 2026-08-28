from ...gateways.student_gateway import StudentGateway
from ...gateways.next_of_kin_gateway import NextOfKinGateway

def get_students_export():
    student_gateway = StudentGateway()
    next_of_kin_gateway = NextOfKinGateway()

    students = student_gateway.list_all()
    next_of_kins = next_of_kin_gateway.list_all()

    result = []

    for student in students:
        next_of_kin_for_student = {}
        for next_of_kin in next_of_kins:
            if student["student_id"] == next_of_kin["student_id"]:
                next_of_kin_for_student = next_of_kin

        result.append({
            "student_id" : student["student_id"],
            "first_name" : student["first_name"],
            "last_name" : student["last_name"],
            "national_id_number" : student["national_id_number"],
            "address" : student["address"],
            "date_of_birth" : student["date_of_birth"],
            "medical_needs" : student["medical_needs"],
            "medical_aid_provider" : student["medical_aid_provider"],
            "medical_aid_number" : student["medical_aid_number"],
            "enrollment_date" : student["enrollment_date"],
            "status" : student["status"],
            "next_of_kin_name" : next_of_kin_for_student.get("full_name"),
            "next_of_kin_national_id" : next_of_kin_for_student.get("national_id_number"),
            "next_of_kin_address" : next_of_kin_for_student.get("address"),
            "next_of_kin_phone" : next_of_kin_for_student.get("phone_number"),
            "next_of_kin_relationship" : next_of_kin_for_student.get("relationship")
        })
    
    return result