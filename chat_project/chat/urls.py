# chat/urls.py
from django.urls import path
from .views import message_list, create_message

urlpatterns = [
    path('', message_list, name='message_list'),
    path('create/', create_message, name='create_message'),
]
