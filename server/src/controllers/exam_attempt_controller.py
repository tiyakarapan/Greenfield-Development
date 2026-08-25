from ..app import App
from ..usecases.exam_attempt import get_all_exam_attempts, create_exam_attempt, update_exam_attempt, delete_exam_attempt

def init_exam_attempt_controller(app: App):
    @app.get("exam-attempt/")
    def get_all_exam_attempts_endpoint():
        return get_all_exam_attempts()

    @app.post("exam-attempt/")
    def create_exam_attempt_endpoint():
        values = app.get_request_body()
        return create_exam_attempt(values)

    @app.put("exam-attempt/<int:id>")
    def update_exam_attempt_endpoint(id):
        values = app.get_request_body()
        return update_exam_attempt(id, values)

    @app.delete("exam-attempt/<int:id>")
    def delete_exam_attempt_endpoint(id):
        return delete_exam_attempt(id)