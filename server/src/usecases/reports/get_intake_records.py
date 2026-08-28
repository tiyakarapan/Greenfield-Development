from datetime import date
from ...gateways.student_gateway import StudentGateway
from ...gateways.enrollment_gateway import EnrollmentGateway


def get_intake_records(from_date_str: str, to_date_str: str):
    student_gateway = StudentGateway()
    enrollment_gateway = EnrollmentGateway()

    students = student_gateway.list_all()
    enrollments = enrollment_gateway.list_all()


    # Convert the query strings into Python date objects
    try:
        from_date = date.fromisoformat(from_date_str) if from_date_str is not None else date(1950, 1, 1)
        to_date = date.fromisoformat(to_date_str) if to_date_str is not None else date(2050, 12, 31)
    except ValueError as e:
        raise ValueError(
            f"Invalid date format, expected ISO format (YYYY-MM-DD): {e}"
        )

    # Find all student IDs who enrolled within the date range
    enrollment_dates = {}

    for enrollment in enrollments:
        try:
            enroll_date = enrollment["enrollment_date"]
            student_id = enrollment["student_id"]
        except KeyError:
            continue

        if from_date <= enroll_date <= to_date:
            enrollment_dates[student_id] = enroll_date

    # Extract and format the student profiles for those IDs
    intake_records = []

    for student in students:
        student_id = student.get("student_id")

        if student_id in enrollment_dates:
            intake_records.append({
                "student_id": student_id,
                "first_name": student.get("first_name"),
                "last_name": student.get("last_name"),
                "email": student.get("email"),
                "enrollment_date": enrollment_dates[student_id],
                "status": student.get("status"),
            })

    return intake_records
