from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register),
    path('home',views.home),
    path('login',views.login)
]

