from csv import DictReader
from django.core.management import BaseCommand
from movies.models import Movie, Actor, Director, Writer
import requests
import os
from dotenv import load_dotenv
load_dotenv()

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the Movie data from the CSV files,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = """
    Loads data from movies_metadata.csv into our Movie model
    And loads data from credits.csv into our Actor,Director model
    """

    def handle(self, *args, **options):
        if Movie.objects.exists() or Actor.objects.exists() or Director.objects.exists() or Writer.objects.exists():
            print('Movie data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading Movie data for Movies available in movies_metadata.csv")
        for row in DictReader(open('./movies_metadata.csv')):
            movie = Movie()
            movie.id = row['id']
            movie.title = row['title']
            movie.budget = row['budget']
            # genres is a list of dictionaries
            genres_raw = row['genres']
            genres_list = eval(genres_raw)
            genres_name_list = list()
            for genre in genres_list:
                genres_name_list.append(genre['name'])
            movie.genres = ','.join(genres_name_list)
            movie.language = row['original_language']
            movie.overview = row['overview']
            # companies is a list of dictionaries
            companies_raw = row['production_companies']
            companies_list = eval(companies_raw)
            companies_name_list = list()
            for companie in companies_list:
                companies_name_list.append(companie['name'])
            movie.companies = ','.join(companies_name_list)
            # countries is a list of dictionaries
            countries_raw = row['production_countries']
            countries_list = eval(countries_raw)
            countries_name_list = list()
            for country in countries_list:
                countries_name_list.append(country['name'])
            movie.countries = ','.join(countries_name_list)
            movie.release_date = row['release_date']
            movie.revenue = row['revenue']
            movie.runtime = row['runtime']
            movie.vote_average = row['vote_average']
            movie.vote_count = row['vote_count']
            try:
                # get the right picture for movie
                api_req = requests.get("https://api.themoviedb.org/3/movie/" + 
                str(row['id']) + "?api_key=" + str(os.getenv('API_KEY')) + "&language=en-US")
                movie.poster = str(api_req.json()['poster_path'])
            except:
                movie.poster = row['poster_path']
            movie.save()
        print("Loading Actor, Director, Writer data for Credits available in credits.csv")
        SEX_CHOICES = {1:'F', 2:'M', 0:''}
        for row in DictReader(open('./credits.csv')):
            # import Actors
            actors_raw = row['cast']
            actors_list = eval(actors_raw)
            for each_actor in actors_list[:5]:
                # if we have the actor just add movie id to it
                try:
                    actor = Actor.objects.get(actor_id=each_actor['id'])
                    actor.movie_ids = actor.movie_ids + ',' + row['id']
                except:
                    actor = Actor()
                    actor.actor_id = each_actor['id']
                    actor.name = each_actor['name']
                    gender_raw = each_actor['gender']
                    actor.gender = SEX_CHOICES[gender_raw]
                    actor.movie_ids = row['id']
                    if each_actor['profile_path']: actor.pic = each_actor['profile_path']
                actor.save()
            # import Directors, Writers from crew
            crews_raw = row['crew']
            crews_list = eval(crews_raw)
            # get only 1 writer
            flag_one_writer = False
            # get only 1 director
            flag_one_director = False
            for crew in crews_list:
                # import Director
                if flag_one_director == False and crew['job'] == 'Director' :
                    try:
                        director = Director.objects.get(actor_id=crew['id'])
                        director.movie_ids = director.movie_ids + ',' + row['id']
                    except:
                        director = Director()
                        director.director_id = crew['id']
                        director.name = crew['name']
                        gender_raw = crew['gender']
                        director.gender = SEX_CHOICES[gender_raw]
                        director.movie_ids = row['id']
                    director.save()
                    flag_one_director = True
                # import Writer
                elif flag_one_writer == False and crew['department'] == 'Writing' :
                    try:
                        writer = Writer.objects.get(actor_id=crew['id'])
                        writer.movie_ids = writer.movie_ids + ',' + row['id']
                    except:
                        writer = Writer()
                        writer.writer_id = crew['id']
                        writer.name = crew['name']
                        gender_raw = crew['gender']
                        writer.gender = SEX_CHOICES[gender_raw]
                        writer.movie_ids = row['id']
                    writer.save()
                    flag_one_writer = True
                if flag_one_writer == True and flag_one_director == True:
                    break
            