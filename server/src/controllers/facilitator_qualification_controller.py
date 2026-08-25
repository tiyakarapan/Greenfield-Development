from ..app import App
from ..usecases.facilitator_qualification import get_all_facilitator_qualifications, create_facilitator_qualification, update_facilitator_qualification, delete_facilitator_qualification

def init_facilitator_qualification_controller(app: App):
    @app.get("facilitator_qualification/")
    def get_all_facilitator_qualifications_endpoint():
        return get_all_facilitator_qualifications()

    @app.post("facilitator_qualification/")
    def create_facilitator_qualification_endpoint():
        values = app.get_request_body()
        return create_facilitator_qualification(values)

    @app.put("facilitator_qualification/<int:id>")
    def update_facilitator_qualification_endpoint(id):
        values = app.get_request_body()
        return update_facilitator_qualification(id, values)

    @app.delete("facilitator_qualification/<int:id>")
    def delete_facilitator_qualification_endpoint(id):
        return delete_facilitator_qualification(id)