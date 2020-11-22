from django.contrib import admin

from .models import Movie,Cast,Director

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'vote_average']

@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'movie_id']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'movie_id']