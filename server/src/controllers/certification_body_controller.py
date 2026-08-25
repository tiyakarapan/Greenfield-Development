from ..app import App
from ..usecases.certification_body import get_all_certification_body, create_certification_body, update_certification_body, delete_certification_body

def init_certification_body_controller(app: App):
    @app.get("certification_body/")
    def get_all_certification_bodies_endpoint():
        return get_all_certification_body()

    @app.post("certification_body/")
    def create_certification_body_endpoint():
        values = app.get_request_body()
        return create_certification_body(values)

    @app.put("certification_body/<int:id>")
    def update_certification_body_endpoint(id):
        values = app.get_request_body()
        return update_certification_body(id, values)

    @app.delete("certification_body/<int:id>")
    def delete_certification_body_endpoint(id):
        return delete_certification_body(id)