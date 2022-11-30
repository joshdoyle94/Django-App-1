from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from games.serializers import VideoGameSerializer

from .models import VideoGame

# Create your views here.
class VideoGamesView(APIView):
    def get(self, request):
        video_games = VideoGame.objects.all()
        serializer = VideoGameSerializer(video_games, many=True)
        return Response({'video_games': serializer.data})

    def post(self, request):
        serializer = VideoGameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoGamesDetailView(APIView):
    def get(self, request, pk):
        video_game = get_object_or_404(VideoGame, pk=pk)
        serializer = VideoGameSerializer(video_game)
        return Response({'team': serializer.data})

    def patch(self, request, pk):
        video_game = get_object_or_404(VideoGame, pk=pk)
        serializer = VideoGameSerializer(video_game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        video_game = get_object_or_404(VideoGame, pk=pk)
        video_game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        