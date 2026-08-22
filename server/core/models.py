from django.db import models


class CertificationBody(models.Model):
    cert_body_id = models.AutoField(primary_key=True)
    body_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'certification_body'

    def __str__(self):
        return self.body_name


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    duration_weeks = models.IntegerField()
    cert_body = models.ForeignKey(
        CertificationBody,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='cert_body_id',
        related_name='courses',
    )
    prerequisite_course = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='prerequisite_course_id',
        related_name='dependent_courses',
    )

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.course_name


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    national_id_number = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    medical_needs = models.TextField(null=True, blank=True)
    medical_aid_provider = models.CharField(max_length=255, null=True, blank=True)
    medical_aid_number = models.CharField(max_length=100, null=True, blank=True)
    enrollment_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='active')

    class Meta:
        db_table = 'student'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class NextOfKin(models.Model):
    next_of_kin_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        db_column='student_id',
        related_name='next_of_kins',
    )
    full_name = models.CharField(max_length=255)
    national_id_number = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=50)
    relationship = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'next_of_kin'

    def __str__(self):
        return self.full_name


class Sponsor(models.Model):
    sponsor_id = models.AutoField(primary_key=True)
    sponsor_name = models.CharField(max_length=255)
    sponsor_type = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=255, null=True, blank=True)
    contact_phone = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'sponsor'

    def __str__(self):
        return self.sponsor_name


class Facilitator(models.Model):
    facilitator_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'facilitator'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class FacilitatorQualification(models.Model):
    facilitator = models.ForeignKey(
        Facilitator,
        on_delete=models.CASCADE,
        db_column='facilitator_id',
        related_name='qualifications',
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        db_column='course_id',
        related_name='qualifications',
    )
    qualified_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'facilitator_qualification'
        constraints = [
            models.UniqueConstraint(fields=['facilitator', 'course'], name='uq_facilitator_course'),
        ]

    def __str__(self):
        return f'{self.facilitator_id} -> {self.course_id}'


class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        db_column='student_id',
        related_name='enrollments',
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        db_column='course_id',
        related_name='enrollments',
    )
    facilitator = models.ForeignKey(
        Facilitator,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='facilitator_id',
        related_name='enrollments',
    )
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='sponsor_id',
        related_name='enrollments',
    )
    enrollment_date = models.DateField(null=True, blank=True)
    enrollment_status = models.CharField(max_length=50, default='enrolled')
    final_result = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'enrollment'

    def __str__(self):
        return f'Enrollment #{self.enrollment_id}'


class ExamAttempt(models.Model):
    attempt_id = models.AutoField(primary_key=True)
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        db_column='enrollment_id',
        related_name='exam_attempts',
    )
    attempt_number = models.IntegerField()
    exam_date = models.DateField()
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pass_fail = models.CharField(max_length=10, null=True, blank=True)
    access_key = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'exam_attempt'

    def __str__(self):
        return f'Attempt #{self.attempt_id}'


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        db_column='enrollment_id',
        related_name='attendance_records',
    )
    attendance_date = models.DateField()
    status = models.CharField(max_length=20)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'attendance'

    def __str__(self):
        return f'Attendance {self.attendance_id}'
