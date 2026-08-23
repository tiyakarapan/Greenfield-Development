from ..app import App
from ..usecases.student import get_all_students, create_student, update_student, delete_student

def init(app: App):
    @app.get("student/")
    def get_all():
        return get_all_students()

    @app.post("student/")
    def create():
        values = app.get_request_body()
        return create_student(values)

    @app.put("student/<int:id>")
    def update(id):
        values = app.get_request_body()
        return update_student(id, values)

    @app.delete("student/<int:id>")
    def delete(id):
        return delete_student(id)