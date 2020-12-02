from django.urls import path, include
from . import views

urlpatterns = [
    path('api/Actors/', views.all_actors),
    path('api/Genres/', views.all_genres),
]
