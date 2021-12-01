from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
# from PIL import Image
# from io import BytesIO
from django.utils.deconstruct import deconstructible
# from sorl.thumbnail import  get_thumbnail
from uuid import uuid4
from django.core.validators import FileExtensionValidator
# Create your models here.
import os
def image_size(image):
    picture_size = image.size 

    if picture_size > 200000:
        raise ValidationError("Max size of file is 2 MB")

def path_and_rename(instance, filename):
    upload_to = 'Profile'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)



class profile(models.Model):
   
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=path_and_rename,null=True, blank=True,validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg']),image_size])

    # def save(self, *args, **kwargs):
    #     if self.image:
    #         self.image = get_thumbnail(self.image, '500x600', quality=99)
    #     super(profile, self).save(*args, **kwargs)

    def delete(self,*args, **kwargs):
        # self.png.delete()
        self.image.delete()
        super().delete(*args, **kwargs)
    
    