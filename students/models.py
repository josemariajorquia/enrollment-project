from django.db import models


class Student(models.Model):
    # Personal Info
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    # Background Info
    guardian_name = models.CharField(max_length=100, blank=True)
    guardian_contact = models.CharField(max_length=20, blank=True)
    previous_school = models.CharField(max_length=150, blank=True)
    year_graduated = models.PositiveIntegerField(null=True, blank=True)

    # Academic Info
    course = models.CharField(max_length=100)
    year_level = models.PositiveSmallIntegerField(default=1)
    section = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, default='Enrolled')

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"