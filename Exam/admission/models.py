from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# https://workik.com/django-code-generator

class Programme(models.Model):
    name = models.CharField(max_length=50)
class Department(models.Model):
    name = models.CharField(max_length=50)

class Nationality(models.Model):
    name = models.CharField(max_length=50)

class Country(models.Model):
    name = models.CharField(max_length=150)

class State(models.Model):
    name = models.CharField(max_length=150)

class Village(models.Model):
    name = models.CharField(max_length=150)

class LGA(models.Model):
    name = models.CharField(max_length=150)

class ChoiceOne(models.Model):
    name = models.CharField(max_length=2)

class ChoiceTwo(models.Model):
    name = models.CharField(max_length=2)

class ChoiceThree(models.Model):
    name = models.CharField(max_length=2)


# After having passed JAMB Examination, Candidate must apply to the school for admission

# To do so, candidate must fill and submit form to the Admissions Department
class Applicant_Registration(models.Model):
    surname = models.CharField(max_length=150, default="select")
    first_Name = models.CharField(max_length=150, default="select")
    other_Name = models.CharField(max_length=150, default="select")
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_Origin = models.ForeignKey(State, on_delete=models.CASCADE)
    lga_Origin = models.ForeignKey(LGA, on_delete=models.CASCADE)
    email = models.EmailField(
        default="example@example.com", unique=True)
    gender_choice = (
            ("male", "Male"),
            ("Female", "Female"),
        )
    gender = models.CharField(max_length=10, choices=gender_choice, default="Male")
    reg_No = models.CharField(max_length=20, default="23u764", unique=True)
    phone = models.CharField(max_length=25, default="234", unique=True)
    choice_One = models.ForeignKey(
    ChoiceOne, on_delete=models.CASCADE, default="1", unique=True)
    choice_Two = models.ForeignKey(ChoiceTwo, on_delete=models.CASCADE, default="2", unique=True)
    choice_Three = models.ForeignKey(ChoiceThree, on_delete=models.CASCADE, default="3", unique=True)
    
    class Meta:        
            # verbose_name = ("")
            verbose_name_plural = ("Candidate Application")
    
    def __str__(self):
            return self.name

    def get_absolute_url(self):
            return reverse("_detail", kwargs={"pk": self.pk})
class Result(models.Model):
    jamb_Result = models.FileField(upload_to='media/jamb_result')   

    def __str__(self):
        return self.jamb_Result    

    class Meta:
        verbose_name_plural = 'JAMB Result Upload'


# When admitted, the candidate officially becomes a student of the school

# The student is now assigned a Matriculation No. no longer Reg No

# The student journey begins here. We can now perform various checks, fees, admission status, etc

# We can now register the student and capture necessary student details
def jls_extract_def():
    return ('default', 'accepted')

class Student(models.Model):
    PROGRAMTYPE = [
        ('phd', 'PHD'),
        ('masters', 'Masters'),
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('diploma', 'Diploma'),
        ('pre_degree', 'Pre Degree'),
        ('default', 'Full Time'),
    ]
    OFFER = [
        ('accepted', 'Admitted and Accepted'),
        ('rejected', 'Admitted but Rejected'),
        ('denied', 'Not Admitted'),
        ('differed', 'Admission is Deferred'),
        jls_extract_def(), 
    ]
    surname = models.CharField(max_length=150, default="select")
    first_Name = models.CharField(max_length=150, default="select")
    other_Name = models.CharField(max_length=150, default="select")
    # nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    # state_Origin = models.ForeignKey(State, on_delete=models.CASCADE)
    # lga_Origin = models.ForeignKey(LGA, on_delete=models.CASCADE)
    email = models.EmailField(default="example@example.com", unique=True)
    gender_choice = (
            ("male", "Male"),
            ("Female", "Female"),
        )
    gender = models.CharField(max_length=10, choices=gender_choice, default="Male")
    reg_No = models.CharField(max_length=20, default="23u764", unique=True)
    phone = models.CharField(max_length=25, default="234", unique=True)    
    admitted_programme = models.ForeignKey(Programme, on_delete=models.CASCADE, default='Not Admitted')
    admitted_Department = models.ForeignKey(Department, on_delete=models.CASCADE, default='Computer Science')
    fee_status = models.BooleanField(default=False)  # True if fees are cleared
    profile_pic = models.ImageField(default = 'avatar', upload_to='profile_pic/Student/', blank=True)
    home_Address = models.CharField(max_length=40)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    local_Government = models.ForeignKey(LGA, on_delete=models.CASCADE)
    village_Name = models.ForeignKey(Village, on_delete=models.CASCADE)
    mother_Maiden_name = models.CharField(max_length=200)
    matrix_No = models.CharField(max_length=20, default="2003/csc-0001")
    admission_status = models.BooleanField(default=False)  # True if admitted    
    start_class = models.DateField(auto_now_add=True)  # Date when the student started class
    semester = models.IntegerField(default=1)
    academic_session = models.CharField(max_length=20, default='2022/2023')
    programme_duration = models.IntegerField(default=4)  # Default duration in years
    graduation_year = models.IntegerField(default=2026)  # Default graduation year

    def __str__(self):
        return f"{self.first_Name}  {self.surname}  {self.other_Name} ‖ {self.email}" 
    class Meta:
            verbose_name_plural = 'Students Personal Information'



    # When all necessary checks are passed, the student can register courses in the course App 

