# In Employee/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list),
    path('employees/<int:pk>/', views.employee_detail),
    path('projects/', views.project_list),
    path('projects/<int:pk>/', views.project_detail),
    # Define similar URLs for Project model
]
