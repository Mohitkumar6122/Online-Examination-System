from django.db import models
from django.contrib.auth.models import User
from student.models import *
from admission.models import *
from course.models import *
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=250)
    # Add other student-related fields

class Course(models.Model):
    name = models.CharField(max_length=250)
    credit_units = models.IntegerField()

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_score = models.FloatField()
    test_score = models.FloatField()
    exam_score = models.FloatField()

    @property
    def total_score(self):
        return self.assignment_score + self.test_score + self.exam_score

    # Add other relevant fields and methods for GPA and CGPA calculations

# Views, logic for GPA, CGPA calculations, and updating student profiles would be implemented in views.py
