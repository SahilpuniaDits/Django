from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework import serializers
from rest_framework import response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMultiAlternatives
import random
# from rest_framework.decorators import list_route

from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    verification_otpSerializer,
    # ChangePasswordSerializer
    # UserListSerializer
)
# from utils import res_codes
import jwt
from .models import User

# otp_send = random.randint(100000,999999)
val_otp = None

class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        otp_send = random.randint(100000, 999999)
        global val_otp
        def val_otp():
            return otp_send
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            print("<<<<<<<<<<<<<<",otp_send)
            # if otp_send is is_verified:       
            email = EmailMultiAlternatives('Confirmation mail.', f'verification otp is {otp_send}', 'sahilpuniawins@gmail.com', [
                serializer.data['email']])
            email.send()
            status_code = status.HTTP_201_CREATED
            

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)

class verification_otpAPIView(APIView):
    def post(self ,request):
        ok = val_otp()
        serializer = verification_otpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer.data['otp'] == ok:
                print("<<<<<<<<<<<<mateched otp")
                status_code = status.HTTP_201_CREATED
            
                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'successfully verified email matched ',
                    'user': serializer.data
                }
                return Response(response,tiv())
            else:
                print(">>>>>>>>>>>>>>>>>>>>not macthed")
                # status_code = status.HTTP_400_BAD_REQUEST
                # response = {
                #     'success': False,
                #     'message': 'email otp is not matched',
                #     'user': serializer.data
                # }
                return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


def tiv():

    pf = User.objects.filter()
    for item in pf:
        item.is_active = True
        item.save()    




class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    # 'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)


# class idView(APIView):
#     serializer_class = UserLoginSerializer
#     permission_classes = (AllowAny, )

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)
#         decode = jwt.decode(serializer.data['access'], options={
#                             "verify_signature": False})
#         print(">>>>>>>>>>>>>>>>>", decode)
#         id = decode.get("user_id")

#         if valid:
#             status_code = status.HTTP_200_OK

#             response = {
#                'id':id,
#                 }
            

#             return Response(response, status=status_code)


