from django.contrib import admin

from .models import Movie, Actor, Director, Writer

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'vote_average',
     'genres', 'release_date', 'revenue', 'runtime']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'movie_ids']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'movie_ids']

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ['name', 'movie_ids']