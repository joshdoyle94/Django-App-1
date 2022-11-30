from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from ..models.player import Player
from ..serializers import PlayerSerializer, PlayerReadSerializer

# def index(request):
#     players = Player.objects.all()
#     data = list(players.values())
#     return JsonResponse(data, safe=False)

class PlayerView(APIView):
    # View class for players/ for viewing all and creating
    serializer_class = PlayerSerializer
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerReadSerializer(players, many=True)
        return Response({'players': serializer.data})

    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerDetailView(APIView):
    #  View class for players/:pk
    serializer_class = PlayerSerializer
    def get(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        serializer = PlayerReadSerializer(player)
        return Response({'player': serializer.data})

    def patch(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)