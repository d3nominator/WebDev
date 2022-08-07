import imp
from django import views
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path("hi" , views.greet , name="greet")
]   