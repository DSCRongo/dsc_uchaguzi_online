from django.urls import path
from . import views
from accounts import validators


urlpatterns = [
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    path('<str:voter_id>/vote/', views.VotingView.as_view(), name='cast_vote'),
    
]

htmx_urlpatterns = [
    path('validate/registration-number/', validators.check_registration_number_exists, name='validate_registration_num'),
]

urlpatterns += htmx_urlpatterns