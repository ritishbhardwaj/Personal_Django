from django.urls import path

from .views import StudentAPI


urlpatterns = [
    
    path('apis',StudentAPI.as_view()),

]