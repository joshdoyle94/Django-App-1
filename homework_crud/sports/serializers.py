from rest_framework import serializers

from .models.team import Team
from .models.player import Player

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Team

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Player

class PlayerReadSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Player