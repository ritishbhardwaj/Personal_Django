from django.shortcuts import render

from django.http import JsonResponse,HttpResponse

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json

from  .models import Student

from .serializers import StudentSerializers

from django.views.decorators.csrf import csrf_exempt

import io


# Create your views here.

@csrf_exempt
def student_api(req):
    

    #GET Method
    if req.method  == 'GET' :
 
        '''json_data =req.body
        stream = io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)'''

        pythondata= JSONParser().parse(req._stream)
        id=pythondata.get('id', None)

        if id is not None:
            '''getting the object from database from using the models'''
            stu = Student.objects.get(id=id)

            ''' Now convert this object to python native data type'''
            serializer = StudentSerializers(stu)

            '''Now coverting this python native data into the json_data'''
            return JsonResponse(serializer.data)

        stu = Student.objects.all()
        serailizer = StudentSerializers(stu,many=True)
        '''since list is returned by the serializer hence we will set safe to false'''
        return JsonResponse(serailizer.data,safe=False)
    
    # POST Method
    if req.method =="POST":
        
        pythondata = JSONParser().parse(req._stream)
        print(pythondata,"$$$$$$$$$$$$$$$$$$")
        serializer = StudentSerializers(data=pythondata)

        if serializer.is_valid():
            serializer.save()

            res = {"msg" : "data added"}

            return JsonResponse(res,safe=True)

        json_data= JSONRenderer().render(serializer.errors)
        print(json_data)
        return JsonResponse(serializer.errors,safe=False)
    

    if req.method  ==  "PUT":
        
        # print(dir(req))
        pythondata : dict= JSONParser().parse(req._stream)
        print(len(pythondata.items()))
        id = pythondata.get('id')

        stu=Student.objects.get(id=id)

        serializer=StudentSerializers(stu,data=pythondata,partial = True)

        if serializer.is_valid():
            serializer.save()

            res= {'msg':'Data Updated'} 
            return JsonResponse(res,safe=True)      
        
        return JsonResponse(serializer.errors , safe=False)
    
    if req.method == "DELETE":
        
        pythondata_dict : dict = JSONParser().parse(req._stream)
        id= pythondata_dict.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res={'msg':  'Data is deleted'}
        return JsonResponse(res,safe=True)