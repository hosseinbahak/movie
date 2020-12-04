from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/Actors/(\d*)', views.all_actors, name='all_actors'),
    url(r'^api/Genres/(\w*)', views.all_genres, name='all_genres'),
    url(r'^api/Movie/', views.movie_details, name='movie_detail'),
<<<<<<< HEAD
    url(r'^api/TopRated/', views.top_rated, name='top_rated'),
    url(r'^api/ReleaseDate/', views.release_date, name='release_date'),
=======
    url(r'^api/Random/', views.random, name='random'),
>>>>>>> 7a20713b774d6722ff70574930d2ecf211ddeb2c
    
]
