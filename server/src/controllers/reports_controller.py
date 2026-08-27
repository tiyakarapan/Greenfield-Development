from ..app import App
from ..usecases.reports.get_exam_records import get_exam_records
from ..usecases.reports.get_roster import get_roster
from ..usecases.reports.get_transcript import get_transcript

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