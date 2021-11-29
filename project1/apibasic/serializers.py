from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import employee,student

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    phone = serializers.IntegerField()
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return employee.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.address = validated_data.get('address',instance.address)
        instance.phone = validated_data.get('phone',instance.phone)
        instance.email = validated_data.get('email',instance.email)
        instance.date = validated_data.get('',instance.date)
        instance.save()
        return instance


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        # fields = ['name','subject','roll_no']    
        fields = ('__all__')    

          