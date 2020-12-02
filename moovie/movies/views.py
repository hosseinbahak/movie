from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Actor
from .serializers import ActorsSerializer

@api_view(['GET'])
def all_actors(requst):
    data = Actor.objects.all()
    result = ActorsSerializer(data, many=True).data
    return Response(result)
    