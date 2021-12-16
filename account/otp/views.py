from django.shortcuts import render
from rest_framework import permissions, serializers

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views import View
from .models import User
#djnago imports
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login as django_login, logout as django_logout
from django.utils import timezone

# from otp.registerotp.serializers import UserRegistrationSerializer

from .serializers import (
	UserRegistrationSerializer, 
	UserLoginSerializer,
	# ChangePasswordSerializer,
)

# from utils import res_codes
from django.core.mail import send_mail
from .models import AccountSettings, key_expire

User = get_user_model()


class SignUpView(APIView):
    seralizer_class = UserRegistrationSerializer
    # permission_classes =(AllowAny,)
    def post(self,request):
        serializer = self.seralizer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            user_obj = serializer.save(is_active=False)
            host_name = 'http://127.0.0.1:8000'
            subject = 'verify email'
            conformations_email = '{}/api/email-conformations/{}/'.\
                format(
                    host_name,
                    user_obj.User.activation_key
                    )
            send_mail(subject,conformations_email,'sahilpuniawins@gmail.com',[user_obj.email],)

            return Response(serializer.data,status=status.HTTP_201_CREATED,)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class EmailConformationView(View):
    def post(self,request,*args, **kwargs):
        activation_key = kwargs.get('activation_key')


        activation = User.objects.filter(activation_key=activation_key)
        # for item in activation:
        activation.is_active = True
        activation.save()   
    # def post(self,request,*args, **kwargs):
        # activation_key = kwargs.get('activation_key')
        # account_setting_obj = AccountSettings.objects.get(
        #     activation_key=activation_key
        # )
        # key_expire = account_setting_obj.key_expire
        # if key_expire > timezone.now():
            # return Response(status=status.HTTP_201_CREATED)
        # return Response(status=status.HTTP_400_BAD_REQUEST)
        #     return Response({
        #         'status':'User not register',
        #         'massage': "key_expire",
               
        #     })
        # else:
        #     account_setting_obj.user.delete()
        #     return Response({
        #         'status':'User not register',
        #         'massage': "key_expire"
        #     })


            
           
       
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




	