from django.db import models

# Create your models here.


class emailApi(models.Model):
    subject =models.CharField(max_length=100)
    send_to =models.EmailField(max_length=100)
    content =models.CharField(max_length=100)
    attechment =models.FileField()

class Sendemail(models.Model):
    send_to =models.EmailField(max_length=100)
    subject =models.CharField(max_length=100)
    massage =models.CharField(max_length=100)


