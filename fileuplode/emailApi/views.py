import os
from django.core import mail
from django.shortcuts import render

from .models import emailApi
from .seralizers import emailApiSerializer
from rest_framework import serializers
from rest_framework.views import APIView
import datetime
import smtplib  
from email.mime.text import MIMEText
from django.template.loader import render_to_string, get_template
from email.mime.multipart import MIMEMultipart
from email.message import Message
import json
from django.core.mail import EmailMessage,send_mail
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from mimetypes import guess_type
from os.path import basename
from email.mime.base import MIMEBase
from email import encoders
# Create your views here.

class Sendemail(APIView):
    def post(self,request):
        serializer = emailApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer,'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            #for 
            email = EmailMultiAlternatives(serializer.data['subject'], serializer.data['content'],
             'sahilpuniawins@gmail.com', [
                serializer.data['send_to']], 
                )

           
            print("READ",os.path.join(os.path.realpath('.'),serializer.data['attechment'].lstrip("/")))
            attachment = open(os.path.join(os.path.realpath('.'),serializer.data['attechment'].lstrip("/")), 'rb')
            email.attach(serializer.data['attechment'].lstrip("/media/"), attachment.read())
           
            email.send()
           

           
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SendemailApi(APIView):
#     def post(self,request):
#         serializer = emailApiSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             send_mail(serializer.data['subject'], serializer.data['massage'], 'sahilpuniawins@gmail.com', [
#                 serializer.data['send_to']], fail_silently=False)
            
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       