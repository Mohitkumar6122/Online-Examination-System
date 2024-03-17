from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# https://workik.com/django-code-generator

class Programme(models.Model):
    name = models.CharField(max_length=50)


class Country(models.Model):
    name = models.CharField(max_length=150)


class State(models.Model):
    name = models.CharField(max_length=150)


class LGA(models.Model):
    name = models.CharField(max_length=150)


class ChoiceOne(models.Model):
    name = models.CharField(max_length=2)


class ChoiceTwo(models.Model):
    name = models.CharField(max_length=2)


class ChoiceThree(models.Model):
    name = models.CharField(max_length=2)


class Applicant_Registration(models.Model):
    name = models.CharField(max_length=150)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_Origin = models.ForeignKey(State, on_delete=models.CASCADE)
    lga_Origin = models.ForeignKey(LGA, on_delete=models.CASCADE)
    email = models.EmailField(
        default="example@example.com", unique=True)
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
    
    
    
