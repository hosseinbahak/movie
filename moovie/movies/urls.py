from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/Actors/', views.all_actors),
    url(r'^api/Genres/', views.all_genres),
    url(r'^api/Movie/', views.movie_details, name='movie_detail'),
    
]
