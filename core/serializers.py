from rest_framework import serializers

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


class CertificationBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationBody
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin
        fields = '__all__'


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class FacilitatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilitator
        fields = '__all__'


class FacilitatorQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilitatorQualification
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class ExamAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamAttempt
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
