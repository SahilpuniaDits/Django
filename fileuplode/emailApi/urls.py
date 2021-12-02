from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import Sendemail
urlpatterns = [
   
    path('emailsend',Sendemail.as_view()),
    # path('sendemailAPi',SendemailApi.as_view()),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
