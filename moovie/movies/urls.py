from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/Actors/(\d*)', views.all_actors, name='all_actors'),
    url(r'^api/Genres/(\w*)', views.all_genres, name='all_genres'),
    url(r'^api/Movie/', views.movie_details, name='movie_detail'),
    url(r'^api/Random/', views.random, name='random'),
    
]
