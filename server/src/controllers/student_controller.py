from ..app import App
from ..usecases.student import get_all_students, create_student, update_student, delete_student

def init_student_controller(app: App):
    @app.get("student/")
    def get_all_students_endpoint():
        return get_all_students()

    @app.post("student/")
    def create_student_endpoint():
        values = app.get_request_body()
        return create_student(values)

    @app.put("student/<int:id>")
    def update_student_endpoint(id):
        values = app.get_request_body()
        return update_student(id, values)

    @app.delete("student/<int:id>")
    def delete_student_endpoint(id):
        return delete_student(id)