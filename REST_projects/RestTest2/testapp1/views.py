from django.shortcuts import render
from django.http import HttpRequest , HttpResponse,JsonResponse
import io

from .models import Student

from rest_framework.parsers import JSONParser

from .serializers import StudentSerializer

from rest_framework.renderers import JSONRenderer

from rest_framework.decorators import api_view
import json
#bypassing the csrf token
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def student_create(req):
    print("Hello")
    if req.method == 'POST':
        # json_data = req.body
        # print("BODY=================",dir(req._stream.getvalue()))
        # print("BODY=================",req._stream.getvalue())
        # stream = io.BytesIO(json_data)
        # print("STREAM =======", stream)
        # print(dir(stream),"#########################################")
        # # pythondata=JSONParser(stream)
        
         
        # pythondata =  json.loads(JSONParser().parse(stream))


        '''Advance way to extract data out of the request'''
        pythondata = JSONParser().parse(req._stream)
        print(pythondata,"Python data")
        print(type(pythondata))
        # print(dict(pythondata))

        python_dictionary=  json.loads(pythondata)
        print(python_dictionary)

        # now to convert the pythondata to complex data
        ## we'll pass this data to the serializer

        serializing = StudentSerializer(data = python_dictionary)
        print(serializing,"SERIALIZING")

        if serializing.is_valid():
            serializing.save()
            res= {'msg' : 'Data Created'}
            
            # sending back the response   in Json data
            return JsonResponse(res, safe=True )
        
        json_data= JSONRenderer().render(serializing._errors)
        return HttpResponse(json_data) 
    else:
        
        return HttpResponse("<h1> Nothing is here </h1>")
        



