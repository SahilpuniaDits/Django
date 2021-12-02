from django.db.models import fields
from rest_framework import serializers
from .models import emailApi,Sendemail



class emailApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=emailApi
        fields="__all__"


class SendemailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sendemail
        fields="__all__"

    # def create(self, validated_data):
    #     return emailApi(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance