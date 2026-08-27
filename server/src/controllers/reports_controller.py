from ..app import App
from ..usecases.reports.get_exam_records import get_exam_records
from ..usecases.reports.get_roster import get_roster
def init_reports_controller(app: App):
    @app.get("reports/exam-records")
    def get_exam_records_endpoint():
        return get_exam_records()

    @app.get("reports/roster")
    def get_roster_endpoint():
            return get_roster()