from ..app import App
from ..usecases.next_of_kin import get_all_next_of_kin, create_next_of_kin, update_next_of_kin, delete_next_of_kin

def init(app: App):
    @app.get("next_of_kin/")
    def get_all_next_of_kin_endpoint():
        return get_all_next_of_kin()

    @app.post("next_of_kin/")
    def create_next_of_kin_endpoint():
        values = app.get_request_body()
        return create_next_of_kin(values)

    @app.put("next_of_kin/<int:id>")
    def update_next_of_kin_endpoint(id):
        values = app.get_request_body()
        return update_next_of_kin(id, values)

    @app.delete("next_of_kin/<int:id>")
    def delete_next_of_kin_endpoint(id):
        return delete_next_of_kin(id)