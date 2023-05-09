from django.contrib import admin
from django.urls import path

from .views import EmployeeAPIView
from .views import EmployeeDetialAPIView


urlpatterns = [
    path('employees', EmployeeAPIView.as_view()),
    path('employees/<int:pk>', EmployeeDetialAPIView.as_view()),
]
