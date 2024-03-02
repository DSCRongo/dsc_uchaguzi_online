from django.urls import path
from . import views


urlpatterns =[
    path('', views.LogIn, name='login'),
    path('home', views.Home, name='home'),
    path('logout', views.Logout, name='logout'),
    path('user_profile', views.profileView, name='user_profile'),
]
