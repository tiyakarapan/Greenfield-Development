from ..app import App
from ..usecases.attendance import get_all_attendance, create_attendance, update_attendance, delete_attendance

def init_attendance_controller(app: App):
    @app.get("attendance/")
    def get_all_attendance_endpoint():
        return get_all_attendance()

    @app.post("attendance/")
    def create_attendance_endpoint():
        values = app.get_request_body()
        return create_attendance(values)

    @app.put("attendance/<int:id>")
    def update_attendance_endpoint(id):
        values = app.get_request_body()
        return update_attendance(id, values)

    @app.delete("attendance/<int:id>")
    def delete_attendance_endpoint(id):
        return delete_attendance(id)