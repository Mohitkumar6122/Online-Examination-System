from django.urls import path
from .views import view_results, borrow_book, return_book, manage_clearance

urlpatterns = [
    path('results/<int:student_id>/', view_results, name='view_results'),
    path('borrow/<int:student_id>/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return/<int:student_id>/<int:book_id>/', return_book, name='return_book'),
    path('clearance/<int:student_id>/', manage_clearance, name='manage_clearance'),
]
