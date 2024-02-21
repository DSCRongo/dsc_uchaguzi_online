from django.urls import path
from . import views


urlpatterns =[
    path('', views.LogIn, name='login'),
    path('home', views.Home, name='home'),
]
