# from os import name
from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return str(self.name)

