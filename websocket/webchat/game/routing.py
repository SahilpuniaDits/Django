# from django.urls import re_path

from . import consumer

# websocket_urlpatterns = [
#     re_path(r'ws/game/(?P<room_name>\w+)/$', consumer.ChatConsumer.as_asgi()),
# ]
from django.urls import re_path 

websocket_urlpatterns = [
  re_path('ws/(?P<room_name>\w+)/', consumer.ChatConsumer.as_asgi()), # Using asgi
]