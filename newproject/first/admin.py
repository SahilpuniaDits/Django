from django.contrib import admin
from .models import User,verification_otp,task
# Register your models here.
admin.site.register(User)
admin.site.register(verification_otp)
admin.site.register(task)