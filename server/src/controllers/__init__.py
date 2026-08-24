from ..app import App
from .student_controller import init as init_student_controller
from .next_of_kin_controller import init as init_next_of_kin_controller

def init(app: App):
    init_student_controller(app)
    init_next_of_kin_controller(app)