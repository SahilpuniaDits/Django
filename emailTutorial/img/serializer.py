from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        Model=Profile
        fields="__all__"