from csv import DictReader
from django.core.management import BaseCommand
from movies.models import Movie


ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the Movie data from the CSV files,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = """
    Loads data from movies_metadata.csv into our Movie model
    And loads data from credits.csv into our Cast,Director model
    """

    def handle(self, *args, **options):
        if Movie.objects.exists():
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
            movie.save()

            