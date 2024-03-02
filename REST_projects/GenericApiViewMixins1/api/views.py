#GenericAPIView and Model Mixin

from .models import Student
from .serializers import StudentSerializer
from rest_framework.mixins import ListModelMixin,DestroyModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework.generics import GenericAPIView


class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,req,*args,**kwargs):
        return self.list(req,*args,**kwargs)

    def post(self,req,*args,**kwargs):
        return self.create(req,*args,**kwargs)

class RUDStudentAPI(GenericAPIView,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,req,*args,**kwargs):
        return self.retrieve(req,*args,**kwargs)
  
    def put(self,req,*args,**kwargs):
        return self.update(req,*args,**kwargs)
    
    def delete(self,req,*args,**kwargs):
        return self.destroy(req,*args,**kwargs)