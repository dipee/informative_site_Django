from django.urls import path
from django import urls 
from .views import index  
urlpatterns=[
    path("", index, name="index"),
]