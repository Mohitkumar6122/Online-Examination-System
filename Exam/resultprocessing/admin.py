from django.contrib import admin
from course.models import *
from resultprocessing.models import *
# Register your models here.


admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Score)

