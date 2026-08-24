from ..app import App
from .student_controller import init_student_controller
from .next_of_kin_controller import init_next_of_kin_controller
from .sponsor_controller import init_sponsor_controller

def init_controllers(app: App):
    init_student_controller(app)
    init_next_of_kin_controller(app)
    init_sponsor_controller