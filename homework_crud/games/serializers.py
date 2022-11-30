from rest_framework import serializers

from .models import VideoGame

class VideoGameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = VideoGame