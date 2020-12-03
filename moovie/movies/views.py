from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from random import randint
from .models import *
from .serializers import *

@api_view(['GET'])
def all_actors(request, actor_id):
    # returns only one Actor
    if actor_id:
        # if the actor_id is valid
        try:
            data = Actor.objects.get(actor_id=actor_id)
            result = ActorsSerializer(data).data
            return Response(result)
        except Actor.DoesNotExist:
            raise Http404('actor not found')
    # returns all the Actors
    else:
        data = Actor.objects.all()
        result = ActorsSerializer(data, many=True).data
        # add url to each Actor
        for actor in result:
            # reverse create full link to each actor
            actor['url'] = reverse('all_actors', args=[str(actor['actor_id'])], request=request)
        return Response(result)

@api_view(['GET'])
def all_genres(request, which_genre):
    if not which_genre:
        # returns all genres
        movies = Movie.objects.all()
        data = []
        for movie in movies:
            for genre in movie.genres.split(','):
                for available_genre in data:
                    # if we had the genre before just add the movie id
                    if available_genre['name'] == genre:
                        available_genre['movie_ids'].append(movie.id)
                        break
                else:
                    # if we don't have that genre create a new one
                    dic = {'name':genre, 'movie_ids':[movie.id], 'url':reverse('all_genres', args=[genre], request=request)}
                    data.append(dic)
        result = GenresSerializer(data, many=True).data
        return Response(result)
    else:
        # return only one genre
        movies = Movie.objects.all()
        data = {'name':which_genre, 'movie_ids':[], 'url':reverse('all_genres', args=[which_genre], request=request)}
        # if which_genre is valid then: flag_which_genre == True
        flag_which_genre = False
        # search for which_genre
        for movie in movies:
            for genre in movie.genres.split(','):
                if genre == which_genre:
                    # if genre is valid then add movie_id to the list
                    data['movie_ids'].append(movie.id)
                    flag_which_genre = True
        if flag_which_genre == True:
            result = GenresSerializer(data).data
            return Response(result)
        else:
            raise Http404('genre not found')

@api_view(['GET', 'POST'])
def movie_details(request):
    movie_id = request.POST['movie_id']
    movie_info = Movie.objects.filter(id = movie_id)
    result = MovieSerializer(movie_info, many=True).data
    return Response(result)
    
@api_view(['GET'])
def random(request):
    # bring all ids from movies DB
    all_ids = Movie.objects.raw('SELECT id from movies_movie')
    data = {'movie_ids':[]}
    # select 10 of them by random
    for _ in range(10):
        data['movie_ids'].append(all_ids[randint(0, len(all_ids) - 1)].id)
    result = RandomSerializer(data).data
    return Response(result)
