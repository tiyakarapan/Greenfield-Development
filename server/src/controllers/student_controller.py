from .api import api_get, api_post, api_put, api_delete, get_request_body
from ..usecases.student import get_all_students, create_student, update_student, delete_student

def init():
    @api_get("student/")
    def get_all():
        return get_all_students()

    @api_post("student/")
    def create():
        values = get_request_body()
        return create_student(values)

    @api_put("student/<int:id>")
    def update(id):
        values = get_request_body()
        return update_student(id, values)

    @api_delete("student/<int:id>")
    def delete(id):
        return delete_student(id)