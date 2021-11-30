from django.shortcuts import render
from rest_framework.compat import apply_markdown
from .serializers import profileSerializer
# from fileuplode.uplode_api.serializer import profileSerializer
from .models import profile
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
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
        serializer= profileSerializer(data,many=True)
        return Response(serializer.data)
