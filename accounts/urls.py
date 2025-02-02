from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import register_request, login_request, logout_request

app_name = "main"   


urlpatterns = [

    path("register/", register_request, name="register"),
    path('login/',  login_request, name='login'),
    path('logout/', logout_request, name='logout')
]