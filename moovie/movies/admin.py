from django.contrib import admin

from .models import Movie, Actor, Director

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'vote_average',
     'genres', 'release_date', 'revenue', 'runtime']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'movie_id']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'movie_id']