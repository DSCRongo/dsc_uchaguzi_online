from django.urls import path
from . import views


urlpatterns = [
    path('feedback/', views.SubmitFeedbackView.as_view(), name='feedback')
]