from ..app import App
from .student_controller import init_student_controller
from .next_of_kin_controller import init_next_of_kin_controller
from .sponsor_controller import init_sponsor_controller
from .certification_body import init_certification_body_controller
from. facilitator_controller import init_facilitator_controller
from .facilitator_qualification_controller import init_facilitator_qualification_controller

def init_controllers(app: App):
    init_student_controller(app)
    init_next_of_kin_controller(app)
    init_sponsor_controller(app)
    init_certification_body_controller(app)
    init_facilitator_controller(app)
    init_facilitator_qualification_controller(app)