from django.shortcuts import render
from rest_framework.compat import apply_markdown
from .serializers import profileSerializer
# from fileuplode.uplode_api.serializer import profileSerializer
from .models import profile
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
import os
# Create your views here.


class uplodefile(APIView):
    def post(self,request):
        serializer = profileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"massage":'success'})
        return Response(serializer.errors)

    def get(self,request):
        data = profile.objects.all()
        serializer= profileSerializer(data ,many=True)
        return Response(serializer.data)

class fileuploadcrud(APIView):
    
    def get_object(self,id):
        try:
            return profile.objects.get(id=id)

        except profile.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        students = self.get_object(id)
        serializer = profileSerializer(students)
        return Response(serializer.data)

    def put(self,request,id):
        students = self.get_object(id)
        serializer = profileSerializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        students = self.get_object(id)
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#  if request.method == 'POST':
#                 if len(request.image)!=0:
#                     if len(students.image) >0:
#                         os.remove(students.image.path)