from ..app import App
from ..usecases.enrollments import get_all_enrollments, create_enrollment, update_enrollment, delete_enrollment

def init_enrollment_controller(app: App):
    @app.get("enrollment/")
    def get_all_enrollments_endpoint():
        return get_all_enrollments()

    @app.post("enrollment/")
    def create_enrollment_endpoint():
        values = app.get_request_body()
        return create_enrollment(values)

    @app.put("enrollment/<int:id>")
    def update_enrollment_endpoint(id):
        values = app.get_request_body()
        return update_enrollment(id, values)

    @app.delete("enrollment/<int:id>")
    def delete_enrollment_endpoint(id):
        return delete_enrollment(id)