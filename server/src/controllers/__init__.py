from ..app import App
from .student_controller import init_student_controller
from .next_of_kin_controller import init_next_of_kin_controller
from .sponsor_controller import init_sponsor_controller
from .certification_body_controller import init_certification_body_controller
from. facilitator_controller import init_facilitator_controller
from .facilitator_qualification_controller import init_facilitator_qualification_controller
from .enrollment_controller import init_enrollment_controller
from .attendance_controller import init_attendance_controller
from .course_controller import init_course_controller

def init_controllers(app: App):
    init_student_controller(app)
    init_next_of_kin_controller(app)
    init_sponsor_controller(app)
    init_certification_body_controller(app)
    init_facilitator_controller(app)
    init_facilitator_qualification_controller(app)
    init_enrollment_controller(app)
    init_attendance_controller(app)
    init_course_controller(app)