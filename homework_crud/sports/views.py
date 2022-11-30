from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from sports.serializers import TeamSerializer

from .models import Team

# def index(request):
#     teams = Team.objects.all()
#     data = list(teams.values())
#     return JsonResponse(data, safe=False)

class TeamsView(APIView):
    # View class for teams/ for viewing all and creating
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response({'teams': serializer.data})

class TeamsDetailView(APIView):
    #  View class for teams/:pk
    def get(self, request, pk):
        team = get_object_or_404(Team, pk=pk)
        serializer = TeamSerializer(team)
        return Response({'team': serializer.data})
