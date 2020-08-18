from django.contrib import admin
from django.urls import path
from  . import views



urlpatterns = [
         
         path('index',views.index,name='index'),
         path('login',views.login,name='index'),
         
         path('',views.signup,name='signup'),
         path('signup',views.signup,name='signup'),
         ]
