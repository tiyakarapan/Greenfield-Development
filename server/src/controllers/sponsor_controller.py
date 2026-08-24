from ..app import App
from ..usecases.sponsor import get_all_sponsors, create_sponsor, update_sponsor, delete_sponsor

def init_sponsor_controller(app: App):
    @app.get("sponsor/")
    def get_all_sponsors_endpoint():
        return get_all_sponsors()

    @app.post("sponsor/")
    def create_sponsor_endpoint():
        values = app.get_request_body()
        return create_sponsor(values)

    @app.put("sponsor/<int:id>")
    def update_sponsor_endpoint(id):
        values = app.get_request_body()
        return update_sponsor(id, values)

    @app.delete("sponsor/<int:id>")
    def delete_sponsor_endpoint(id):
        return delete_sponsor(id)