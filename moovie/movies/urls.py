from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/Actors/(\d*)', views.all_actors, name='all_actors'),
    url(r'^api/Genres/(\w*)', views.all_genres, name='all_genres'),
    url(r'^api/Movie/(\d*)', views.movie_details, name='movie_detail'),
    url(r'^api/TopRated/', views.top_rated, name='top_rated'),
    url(r'^api/ReleaseDate/', views.release_date, name='release_date'),
    url(r'^api/Random/', views.random, name='random'),
    url(r'^api/Search/', views.search, name='search'),
    url(r'^genres/', views.genres_page, name='genres'),
    url(r'^movie_list/', views.movie_list, name='movie_list'),
    url(r'^(?P<movie_id>[\w-]+)/$', views.movie_detail, name='movie_detail'),
    url(r'', views.home, name='home'),
]
