from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    path('<str:voter_id>/vote/', views.VotingView.as_view(), name='cast_vote'),
    
]