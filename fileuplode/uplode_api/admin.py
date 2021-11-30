from django.contrib import admin
from .models import profile
# Register your models here.
class profileAdmin(admin.ModelAdmin):
    list_display=['id','name','picture']
admin.site.register(profile)    

