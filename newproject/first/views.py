from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
# Create your views here.
from rest_framework import generics

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
from django.http import HttpResponse
# from rest_framework.decorators import list_route

from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    forgotPasswordSerializer,
    verification_otpSerializer,
    ChangePasswordSerializer,
    taskSerializer
    # forgetpasswordSerializer,

)
# from utils import res_codes
import jwt
from .models import User, verification_otp,task

# otp_send = random.randint(100000,999999)
# val_otp = None

class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
    def post(self, request):
        otp_send = random.randint(100000, 999999)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print("<<<<<<<<<<<", serializer.data['email'])

            u_obj = User.objects.get(email=serializer.data['email'])
            print(">>>>>>>>>>>>", u_obj)
            user_obj = verification_otp()
            user_obj.user = u_obj
            user_obj.otp = otp_send
            user_obj.save()
            # if valid:
            #     serializer.save()
            email = EmailMultiAlternatives('Confirmation mail.', f'verification otp is {otp_send}',
                                           'sahilpuniawins@gmail.com', [
                                               serializer.data['email']])
            email.send()
            print("<<<<<<<<<<<<<<", otp_send)
            # if otp_send is is_verified:
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)



class verification_otpAPIView(APIView):
    def post(self, request):
        serializer = verification_otpSerializer(data=request.data)
        # user_otp = verification_otp.objects.get(user =serializer.data['otp'])
        # user_otp = serializer.data['otp']
        if serializer.is_valid(raise_exception=True):
            print("***************", serializer)
            # serializer.save()
            user_otp = verification_otp.objects.get(user__email=serializer.data['email'])
            print("****************", user_otp)
            if serializer.data['otp'] == user_otp.otp:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'successfully verified email matched ',
                    'user': serializer.data
                }
                return Response(response, otpforgot(serializer.data['email']))
            else:
                status_code = status.HTTP_400_BAD_REQUEST

                response = {
                    'success': False,
                    'statusCode': status_code,
                    'message': 'otp did not match',
                    'user': serializer.data
                }
                return Response(response)

        # return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

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
                # 'authenticatedUser': {
                #     'email': serializer.data['email'],
                #     # 'role': serializer.data['role']
                # }
            }

            return Response(response, status=status_code)

def otpforgot(email):

    print('email---', email)
    aa = User.objects.get(email=email)
    aa.is_active = True
    aa.save()


class forgotPasswordView(APIView):
    def post(self, request):
        otp_send = random.randint(100000, 999999)
        serializer=forgotPasswordSerializer(data=request.data)
        alldatas={}
        if serializer.is_valid(raise_exception=True):
            mname=serializer.save()
            usr_obj = User.objects.get(email=serializer.data['email'])
            print(">>>>>>>>>>>>", usr_obj.id)
            # user_obj = verification_otp()
            user_obj = verification_otp.objects.get(user=usr_obj)
            user_obj.otp = otp_send
            user_obj.save()

            email = EmailMultiAlternatives('forgot password.', f'verification otp is {otp_send}', 'sahilpuniawins@gmail.com', [
                serializer.data['email']])
            email.send()
            pf = User.objects.get(email=serializer.data['email'])
            # for item in pf:
            pf.is_active = False
            pf.save()
            alldatas['data']='successfully registered'
            print(alldatas)
            return Response(alldatas)
        return Response('failed retry after some time')


class forgotverification_otp(APIView):
    def post(self, request):
        serializer = verification_otpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            usr_otp = verification_otp.objects.get(user__email=serializer.data['email'])
            if serializer.data['otp'] == usr_otp.otp:
                print("<<<<<<<<<<<<mateched otp", usr_otp)
                status_code = status.HTTP_201_CREATED

                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'successfully verified email matched ',
                    'user': serializer.data
                }
                return Response(response, otpforgot(serializer.data['email']))
            else:
                status_code = status.HTTP_400_BAD_REQUEST

                response = {
                    'success': False,
                    'statusCode': status_code,
                    'message': 'otp did not match',
                    'user': serializer.data
                }
                return Response(response)

 # change password
# class ChangePasswordView(generics.UpdateAPIView):
#     # permission_classes = (AllowAny, )
#     queryset = User.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ChangePasswordSerializer
#     print("helooooooooooooooooooo<<<<<<<<<<<<<<<<<<<<<")
#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj

class ChangePasswordView(APIView):
    def put(self,request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                'success':True,
                'massage':'you successfully change password',
                'user':serializer.data
            }
            return Response(response,status=status.HTTP_200_OK)
        else:
            response = {
                'success':False,
                'massage':'some error',
                'user':serializer.data
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

class taskapi(APIView):
    def post(self,request):
        serializer = taskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response={
                'success':True,
                'massage':"successfully created",
                'user':serializer.data
            }
            return Response(response,status=status.HTTP_200_OK)
        else:
            response={
                'success':False,
                'massage':"not created",
                'user':serializer.data
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        getdata = task.objects.all()
        serializer = taskSerializer(getdata,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class updatetaskapi(APIView):
    def get_object(self,id):
        return task.objects.get(id=id)
    def put(self,request,id):
        getbyid = self.get_object(id)
        serializer = taskSerializer(getbyid,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

class deletetaskapi(APIView):
    def get_object(self, id):
        return task.objects.get(id=id)
    def delete(self,request,id):
        deletetask = self.get_object(id)
        deletetask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


