from django.urls import path, include
from .views import index, audio


urlpatterns = [
    path('', index),
    path('audioAPI', audio)
]