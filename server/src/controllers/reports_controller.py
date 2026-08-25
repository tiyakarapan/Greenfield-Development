from ..app import App
from ..usecases.reports.get_exam_records import get_exam_records
def init_reports_controller(app: App):
    @app.get("reports/exam-records")
    def get_exam_records_endpoint():
        return get_exam_records()