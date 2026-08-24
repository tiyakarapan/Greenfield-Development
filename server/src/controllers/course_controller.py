from ..app import App
from ..usecases.course import get_all_courses, create_course, update_course, delete_course

def init_course_controller(app: App):
    @app.get("course/")
    def get_all_courses_endpoint():
        return get_all_courses()

    @app.post("course/")
    def create_course_endpoint():
        values = app.get_request_body()
        return create_course(values)

    @app.put("course/<int:id>")
    def update_course_endpoint(id):
        values = app.get_request_body()
        return update_course(id, values)

    @app.delete("course/<int:id>")
    def delete_course_endpoint(id):
        return delete_course(id)