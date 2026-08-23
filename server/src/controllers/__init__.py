from ..app import App
from .student_controller import init as init_student_controller

def init(app: App):
    init_student_controller(app)