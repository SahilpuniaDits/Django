from os import access, write
# from typing_extensions import Required
from django.db import models
# from typing_extensions import Required
from rest_framework import status, validators
from rest_framework import response
from rest_framework.response import Response



from .models import User ,verification_otp,task
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, Token
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password
# from utils import res_codes
import jwt
from rest_framework.permissions import IsAuthenticated
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )
    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    # role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid login credentials")
        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            # update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                # 'role': user.role,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
class verification_otpSerializer(serializers.ModelSerializer):
    class Meta:
        model =verification_otp
        fields = "__all__"


class forgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = '__all__'
    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            # then set the new password for your username
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'error': 'please enter valid crendentials'})


# change password
class ChangePasswordSerializer(serializers.ModelSerializer):
    New_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    Confirm_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'New_password', 'Confirm_password')  # ,'access')

    def validate(self, attrs):
        if attrs['New_password'] != attrs['Confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user

        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['New_password'])
        instance.save()

        return instance


class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model=task
        fields = "__all__"
