from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/<int:pk>/', views.student_profile, name='student_profile'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
]