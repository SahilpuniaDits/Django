from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    

