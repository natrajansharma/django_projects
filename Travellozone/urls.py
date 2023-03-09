from django.contrib import admin
from django.urls import path
from Travellozone import views

urlpatterns = [
    path("",views.index, name='index'),
    path("base",views.base, name='base'),
    path("login",views.loginusers, name='login'),
    path("logout",views.logoutusers, name='logout'),
    path("signup",views.signupusers, name='signup'),
]