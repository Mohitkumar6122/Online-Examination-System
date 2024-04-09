from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Grade)
admin.site.register(StudentAcceptance)
admin.site.register(Course)
admin.site.register(CourseRegistration)
admin.site.register(Session)
