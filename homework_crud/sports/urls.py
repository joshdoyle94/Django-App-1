from django.urls import path
from .views import TeamsDetailView, TeamsView

urlpatterns = [
    path('', TeamsView.as_view(), name='teams'),
    path('<int:pk>/', TeamsDetailView.as_view(), name='team')
]