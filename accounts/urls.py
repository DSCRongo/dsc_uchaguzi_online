from django.urls import path
from . import views


urlpatterns =[
    path('login/', views.UsersLoginView.as_view(), name='login'),
    path('voter/registration/', views.VoterRegistrationView.as_view(), name='voter_registration'),
    path('user_profile', views.profileView, name='user_profile'),
    path('logout/', views.LogoutUsersView.as_view(), name='logout'),

]
