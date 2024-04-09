from django.db import models
# from admission import models, views 
from admission.models import *

from django.db import models

class Session(models.Model):
    name = models.CharField(max_length=250)

# Allow Only Admitted Students to Pay Acceptance Fees:

# Create a model for students with field to track their admission status.
# Implement a view where admitted students can pay acceptance fees.
# Allow Only Cleared Students to Register Courses:

# Add a field in the student model to track fee clearance status.
# Implement a view for students to register courses,
# checking if the student has cleared fees before allowing course selection.
# Allocate Credit Units for Freshers and Returning Students:

# Create models for courses and student course registrations.
# Define credit units for each course and set credit limits for each student
# based on their program and semester.
# Implement logic to allocate credit units to students based on their status
# (freshers or returning) and the courses they select.


class Grade(models.Model):
    name = models.CharField(max_length=50)
    points = models.FloatField()


class StudentAcceptance(models.Model):
    name = models.CharField(max_length=250)
    matrix_No = models.ForeignKey(Student, on_delete=models.CASCADE)
    has_paid_acceptance_fee = models.BooleanField(default=False)
    has_paid_school_fees = models.BooleanField(default=False)
    credit_units_limit = models.IntegerField(default=0)
    probation_years = models.IntegerField(default=0)
    grade_points = models.FloatField(default=0.0)

class Course(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    course_Code = models.CharField(max_length=10)
    credit_units = models.IntegerField()

class CourseRegistration(models.Model):
    student = models.ForeignKey(StudentAcceptance, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)










