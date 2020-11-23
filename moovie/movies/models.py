from django.db import models

class Movie(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    budget = models.PositiveIntegerField()
    genres = models.TextField()
    language = models.CharField(max_length=2)
    overview = models.TextField()
    companies = models.TextField()
    countries = models.TextField()
    release_date = models.DateField()
    revenue = models.PositiveIntegerField()
    runtime = models.FloatField()
    vote_average = models.FloatField()
    vote_count = models.PositiveIntegerField()

class Actor(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    gender = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    movie_id = models.PositiveIntegerField()

class Director(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    gender = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    movie_id = models.PositiveIntegerField()
