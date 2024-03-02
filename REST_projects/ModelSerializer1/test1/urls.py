from django.urls import path,include

from .views import student_api


urlpatterns = [
    path('apis',student_api),
]