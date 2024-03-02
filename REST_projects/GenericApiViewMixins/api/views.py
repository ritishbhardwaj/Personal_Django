# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status
# from rest_framework.views import APIView
# Create your views here.

#GenericAPIView and Model Mixin

from .models import Student
from .serializers import StudentSerializer
from rest_framework.mixins import ListModelMixin,DestroyModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework.generics import GenericAPIView


class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,req,*args,**kwargs):
        return self.list(req,*args,**kwargs)
    

class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,req,*args,**kwargs):
        return self.retrieve(req,*args,**kwargs)

class StudentPost(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self,req,*args,**kwargs):
        return self.create(req,*args,**kwargs)
    

class StudentUpdate(GenericAPIView,UpdateModelMixin,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self,req,*args,**kwargs):
        return self.update(req,*args,**kwargs)

    def get(self,req,*args,**kwargs):
        return self.retrieve(req,*args,**kwargs)
    
class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self,req,*args,**kwargs):
        return self.destroy(req,*args,**kwargs)