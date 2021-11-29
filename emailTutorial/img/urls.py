from django.urls import path
from . import views


urlpatterns = [
    path('imguplode/',views.SaveProfile,name='imguplode')
]