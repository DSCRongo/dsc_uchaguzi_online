from django.urls import path
from . import views
from . import validators


urlpatterns =[
    path('login/', views.UsersLoginView.as_view(), name='login'),
    path('user_profile', views.profileView, name='user_profile'),
    path('logout/', views.LogoutUsersView.as_view(), name='logout'),

]

htmx_urlpatterns = [
    path('validate/registration-number/', validators.check_registration_number_exists, name='validate_registration_num'),
]

urlpatterns += htmx_urlpatterns