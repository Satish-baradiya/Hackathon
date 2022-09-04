from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('master',views.master),
    path('institue',views.institue),
    path('order',views.order),
]