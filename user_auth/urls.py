from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "user_auth"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('oauth/', views.oauth, name='oauth'),
]