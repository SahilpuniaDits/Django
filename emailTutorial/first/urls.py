
from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login,name='login')
]
# from django.conf.urls import patterns, url
# from django.views.generic import TemplateView

# urlpatterns = patterns('views',
#    url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
#    url(r'^login/', 'login', name = 'login'))