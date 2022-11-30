from django.urls import path
from .views import VideoGamesDetailView, VideoGamesView

urlpatterns = [
    path('', VideoGamesView.as_view(), name='video_games'),
    path('<int:pk>/', VideoGamesDetailView.as_view(), name='video_game')
]