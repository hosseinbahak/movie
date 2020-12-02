from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def all_actors(request):
    data = Actor.objects.all()
    result = ActorsSerializer(data, many=True).data
    result.insert(0,{'number_of_actors':Actor.objects.count()})
    return Response(result)
    
@api_view(['GET'])
def all_genres(request):
    movies = Movie.objects.all()
    number_of_genres = 0
    data = []
    for movie in movies:
        for genre in movie.genres.split(','):
            for available_genre in data:
                if available_genre['name'] == genre:
                    available_genre['movie_ids'].append(movie.id)
                    break
            else:
                number_of_genres += 1
                dic = {'name':genre, 'movie_ids':[movie.id]}
                data.append(dic)
    result = GenresSerializer(data, many=True).data
    result.insert(0,{'number_of_genres':number_of_genres})
    return Response(result)

@api_view(['GET'])
def movie_details(request):
    movie_id = request.POST['movie_id']
    movie_info = Movie.objects.filter(id__id = movie_id).get()
    result = MovieSerializer(movie_info, many=True).data
    return Response(result)
    