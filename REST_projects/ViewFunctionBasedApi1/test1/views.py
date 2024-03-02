from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.decorators import api_view
# Create your views here.

@api_view(["POST","GET"])
def hello_world(req):
    # print("$$$$",dir(req))
    print(req._data,"!!!!!!!!!!!!")
    if req.method=="GET":
        return Response({'msg': 'GET Response'})
    if req.method  == "POST":
        print(req.data)
        return Response({'msg': 'Post Response'})
