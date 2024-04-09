from django.urls import path
from .views import student_results

urlpatterns = [
    path('student/<int:student_id>/results/', student_results, name='student_results'),
]
