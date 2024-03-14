from django.urls import path
from . import views


urlpatterns = [
    path('<str:user_id>/view/', views.ElectionResultsView.as_view(), name='election_results'),
]