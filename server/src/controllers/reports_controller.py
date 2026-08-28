from ..app import App
from ..usecases.reports.get_exam_records import get_exam_records
from ..usecases.reports.get_roster import get_roster
from ..usecases.reports.get_transcript import get_transcript
from ..usecases.reports.get_students_export import get_students_export
from ..usecases.reports.get_at_risk_students import get_at_risk_students
from ..usecases.reports.get_course_demand import get_course_demand
from ..usecases.reports.get_facilitator_mismatches import get_facilitator_mismatches
from ..usecases.reports.get_intake_records import get_intake_records

def init_reports_controller(app: App):
    @app.get("reports/exam-records")
    def get_exam_records_endpoint():
        return get_exam_records()

    @app.get("reports/roster")
    def get_roster_endpoint():
        return get_roster()

    @app.get("reports/transcript/<studentId>")
    def get_transcript_endpoint(studentId):
        return get_transcript(studentId)

    @app.get("reports/export/students")
    def get_students_export_endpoint():
        return get_students_export()

    @app.get("reports/at-risk-students")
    def get_at_risk_students_endpoint():
        return get_at_risk_students()

    @app.get("reports/course-demand")
    def get_course_demand_endpoint():
        return get_course_demand()

    @app.get("reports/facilitator-mismatches")
    def get_facilitator_mismatches_endpoint():
        return get_facilitator_mismatches()

    @app.get("reports/intake") 
    def get_intake_records_endpoint(): 
        params = app.get_request_query_params()

        from_date = params.get("from")
        to_date = params.get("to") 
        return get_intake_records(from_date, to_date)