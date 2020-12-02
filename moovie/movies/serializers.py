from rest_framework import serializers
from .models import Actor

class ActorsSerializer(serializers.Serializer):
    actor_id = serializers.IntegerField()
    name = serializers.CharField(max_length=70)
    gender = serializers.CharField(max_length=1)
    pic = serializers.CharField(max_length=50)
    movie_ids = serializers.CharField(max_length=50)

