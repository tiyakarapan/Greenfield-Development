from .student_controller import init as init_student_controller
from .api import app

def init():
    init_student_controller()