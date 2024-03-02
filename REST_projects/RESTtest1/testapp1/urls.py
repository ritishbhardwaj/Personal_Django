
from django.urls import path

from .views import studentDetail,studentDetail_all


urlpatterns=[
    path('stuinfo/<int:pk>',  studentDetail),
    path('stuinfo/',studentDetail_all),
]