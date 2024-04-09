from django.urls import path
from .views import course_list, CourseRegistrationListView, course_registration

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('registrations/', CourseRegistrationListView.as_view(), name='registration_list'),
    path('register/', course_registration, name='course_registration'),
]
