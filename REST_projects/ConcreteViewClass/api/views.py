
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView




class Student_LC(ListCreateAPIView):
    queryset= Student.objects.all()
    serializer_class=StudentSerializer



class Student_RUD(RetrieveUpdateDestroyAPIView):
    queryset= Student.objects.all()
    serializer_class=StudentSerializer