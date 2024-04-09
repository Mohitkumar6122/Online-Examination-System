from django.db import models
from django.contrib.auth.models import User
from admission.models import *
# from student.models import *

# Create your models here.
class StudentWallet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class WalletTransaction(models.Model):
    wallet = models.ForeignKey(StudentWallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10)  # 'credit' or 'debit'
    timestamp = models.DateTimeField(auto_now_add=True)

# Library Management System
class LibraryBook(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    is_borrowed = models.BooleanField(default=False)

class StudentInvolvement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity = models.CharField(max_length=100)
    is_cleared = models.BooleanField(default=False)

class ResultApproval(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
