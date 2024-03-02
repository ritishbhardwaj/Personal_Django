from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
 
#  Processing Single student data 
def studentDetail(req,pk):
    stu=Student.objects.get(id=pk)
    serializer= StudentSerializers(stu)   #pyton ntive object is created 
    
    # # print('11111',serializer.data)
    # json_data=JSONRenderer().render(serializer.data)  #now from python native object json data is formed using JSONRenderer from rest_frameworks.renderers

    # # print('22222',json_data)

    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data, safe=True)

# Processing all student data (QuerySet)
def studentDetail_all(req):
    stu=Student.objects.all()
    serializer= StudentSerializers(stu,many=True)   #pyton ntive object is created   #it is important to mention '''many = True ''' 
    
    print('11111',serializer.data)
    json_data=JSONRenderer().render(serializer.data)  #now from python native object json data is formed using JSONRenderer from rest_frameworks.renderers

    print('22222',json_data)

    return HttpResponse(json_data,content_type='application/json')



