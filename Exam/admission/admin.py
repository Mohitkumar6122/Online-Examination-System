from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Programme)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(LGA)
admin.site.register(Applicant_Registration)
admin.site.register(Result)
