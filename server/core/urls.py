from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .reports import (
    at_risk_students,
    course_demand,
    export_students,
    exam_records,
    facilitator_mismatches,
    intake_report,
    prerequisite_check,
    roster,
    transcript,
)
from .views import (
    AttendanceViewSet,
    CertificationBodyViewSet,
    CourseViewSet,
    EnrollmentViewSet,
    ExamAttemptViewSet,
    FacilitatorQualificationViewSet,
    FacilitatorViewSet,
    NextOfKinViewSet,
    SponsorViewSet,
    StudentViewSet,
)

router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
router.register(r'next_of_kin', NextOfKinViewSet, basename='next_of_kin')
router.register(r'sponsor', SponsorViewSet, basename='sponsor')
router.register(r'certification_body', CertificationBodyViewSet, basename='certification_body')
router.register(r'course', CourseViewSet, basename='course')
router.register(r'facilitator', FacilitatorViewSet, basename='facilitator')
router.register(r'facilitator_qualification', FacilitatorQualificationViewSet, basename='facilitator_qualification')
router.register(r'enrollment', EnrollmentViewSet, basename='enrollment')
router.register(r'exam_attempt', ExamAttemptViewSet, basename='exam_attempt')
router.register(r'attendance', AttendanceViewSet, basename='attendance')

urlpatterns = [
    path('', include(router.urls)),
    path('reports/at-risk-students', at_risk_students),
    path('reports/facilitator-mismatches', facilitator_mismatches),
    path('reports/exam-records', exam_records),
    path('reports/intake', intake_report),
    path('reports/course-demand', course_demand),
    path('reports/roster', roster),
    path('reports/transcript/<int:student_id>', transcript),
    path('reports/export/students', export_students),
    path('reports/prerequisite-check', prerequisite_check),
]
