from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_excel, name='upload_excel'),
    path('grant-admission/', views.grant_admission, name='grant_admission'),
]
