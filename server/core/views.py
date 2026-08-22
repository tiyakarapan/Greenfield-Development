from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import (
    Attendance,
    CertificationBody,
    Course,
    Enrollment,
    ExamAttempt,
    Facilitator,
    FacilitatorQualification,
    NextOfKin,
    Sponsor,
    Student,
)
from .serializers import (
    AttendanceSerializer,
    CertificationBodySerializer,
    CourseSerializer,
    EnrollmentSerializer,
    ExamAttemptSerializer,
    FacilitatorQualificationSerializer,
    FacilitatorSerializer,
    NextOfKinSerializer,
    SponsorSerializer,
    StudentSerializer,
)


class BaseDestroyMixin:
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'deleted': True}, status=status.HTTP_200_OK)


class StudentViewSet(BaseDestroyMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class NextOfKinViewSet(BaseDestroyMixin, viewsets.ModelViewSet):
    queryset = NextOfKin.objects.all()
    serializer_class = NextOfKinSerializer


class SponsorViewSet(BaseDestroyMixin, viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class CertificationBodyViewSet(BaseDestroyMixin, viewsets.ModelViewSet):
    queryset = CertificationBody.objects.all()
    serializer_class = CertificationBodySerializer


class CourseViewSet(BaseDestroyMixin, viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class FacilitatorViewSet(BaseDestroyMixin, viewsets.ModelViewSet):
    queryset = Facilitator.objects.all()
    serializer_class = FacilitatorSerializer


class EnrollmentViewSet(BaseDestroyMixin, viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class ExamAttemptViewSet(BaseDestroyMixin, viewsets.ModelViewSet):
    queryset = ExamAttempt.objects.all()
    serializer_class = ExamAttemptSerializer


class AttendanceViewSet(BaseDestroyMixin, viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class FacilitatorQualificationViewSet(BaseDestroyMixin, viewsets.ModelViewSet):
    queryset = FacilitatorQualification.objects.all()
    serializer_class = FacilitatorQualificationSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            return super().get_object()

        parts = str(pk).split('_')
        if len(parts) != 2:
            raise ValueError('Composite key must be in the format facilitator_id_course_id')

        facilitator_id, course_id = parts
        return get_object_or_404(
            FacilitatorQualification,
            facilitator_id=facilitator_id,
            course_id=course_id,
        )
