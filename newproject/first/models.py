import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
# from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

  # Roles created here
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('Email',unique=True)
    phone = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField('active', default=False)
    # is_superuser = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email


class verification_otp(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    otp = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

# CHOICES = (
#     (pending=1,"pending"),
#     Completed=2,"Completed"
#     failed=3,"failed",
#     Processing=4,"Processing"
# )
class task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    due_to = models.DateField()
    status = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
