from django.urls import path
from .views.team_views import TeamsView, TeamsDetailView
from .views.player_views import PlayerView, PlayerDetailView

urlpatterns = [
    path('teams/', TeamsView.as_view(), name='teams'),
    path('teams/<int:pk>/', TeamsDetailView.as_view(), name='team'),
    path('players/', PlayerView.as_view(), name='players'),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name='player'),
]