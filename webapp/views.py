from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webapp import getdata
class smartAPI(APIView):

    def get(self, request, id = None, param = None):
        data = getdata.callGmAPI(id, param)
        return Response(data)
        #return Response(param)

    def post(self, request, id = None, param = None):
        data = getdata.callGmAPIPost(id, request)
        return Response(data)