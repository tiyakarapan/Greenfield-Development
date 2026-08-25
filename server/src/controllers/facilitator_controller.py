from ..app import App
from ..usecases.facilitator import get_all_facilitator, create_facilitator, update_facilitator, delete_facilitator

def init_facilitator_controller(app: App):
    @app.get("facilitator/")
    def get_all_facilitators_endpoint():
        return get_all_facilitators()

    @app.post("facilitator/")
    def create_facilitator_endpoint():
        values = app.get_request_body()
        return create_facilitator(values)

    @app.put("facilitator/<int:id>")
    def update_facilitator_endpoint(id):
        values = app.get_request_body()
        return update_facilitator(id, values)

    @app.delete("facilitator/<int:id>")
    def delete_facilitator_endpoint(id):
        return delete_facilitator(id)