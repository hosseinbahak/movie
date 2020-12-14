from django.test import TestCase, Client
from .models import *


class MovieWithoutDBTestCase(TestCase):
    def test_all_actors_api_without_data(self):
        response = self.client.get('/api/Actors/')
        self.assertEqual(response.status_code, 500)

    def test_all_actors_api_with_one_actor_without_data(self):
        response = self.client.get('/api/Actors/5')
        self.assertEqual(response.status_code, 404)

    def test_all_genres_api_without_data(self):
        response = self.client.get('/api/Genres/')
        self.assertEqual(response.status_code, 500)

    def test_all_genres_api_with_one_genre_without_data(self):
        response = self.client.get('/api/Genres/Animation')
        self.assertEqual(response.status_code, 404)

    def test_random_api_without_data(self):
        response = self.client.get('/api/Random/')
        self.assertEqual(response.status_code, 500)

    def test_search_api_without_data(self):
        response = self.client.get('/api/Search/', data={'search': 'toy'})
        self.assertEqual(response.status_code, 500)


class MovieTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.actor = Actor.objects.create(
            actor_id=1,
            name='Tom',
            gender='M',
            movie_ids='1',
            pic='/pQFoyx7rp09CJTAb932F2g8Nlho.jpg'
        )
        self.movie = Movie.objects.create(
            id=1,
            title='toy story',
            budget=30000,
            genres='Animation,Family',
            language='En',
            overview='hi this is only for test',
            companies='Pixar',
            countries='USA',
            release_date='1995-10-30',
            revenue=3000000,
            runtime=120,
            vote_average=8.0,
            vote_count=1000,
            poster='/rhIRbceoE9lR4veEXuwCC2wARtG.jpg'
        )
        self.director = Director.objects.create(
            name='John Lasseter',
            gender='M',
            movie_ids='1',
            director_id=1
        )
        self.writer = Writer.objects.create(
            name='Joss Whedon',
            gender='M',
            movie_ids='1',
            writer_id=1
        )

    def test_all_actors_api_with_loaded_data(self):
        response = self.client.get('/api/Actors/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], 'Tom')
        self.assertEqual(response.json()[0]['actor_id'], 1)
        self.assertEqual(response.json()[0]['gender'], 'M')
        self.assertEqual(response.json()[0]['movie_ids'], '1')
        self.assertEqual(
            response.json()[0]['pic'], '/pQFoyx7rp09CJTAb932F2g8Nlho.jpg')
        self.assertEqual(
            response.json()[0]['url'], 'http://testserver/api/Actors/1')

    def test_all_actors_api_with_one_actor_with_loaded_data(self):
        response = self.client.get('/api/Actors/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {'actor_id': 1, 'name': 'Tom', 'gender': 'M',
             'pic': '/pQFoyx7rp09CJTAb932F2g8Nlho.jpg', 'movie_ids': '1'}
        )
        response = self.client.get('/api/Actors/3')
        self.assertEqual(response.status_code, 404)

    def test_all_genres_api_with_loaded_data(self):
        response = self.client.get('/api/Genres/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['name'], 'Animation')
        self.assertEqual(response.json()[0]['movie_ids'], [1])
        self.assertEqual(
            response.json()[0]['url'], 'http://testserver/api/Genres/Animation')
        self.assertEqual(response.json()[1]['name'], 'Family')
        self.assertEqual(response.json()[1]['movie_ids'], [1])
        self.assertEqual(
            response.json()[1]['url'], 'http://testserver/api/Genres/Family')

    def test_all_genres_api_with_one_genre_with_loaded_data(self):
        response = self.client.get('/api/Genres/Animation')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"name": "Animation",
                "movie_ids": [1],
                "url": "http://testserver/api/Genres/Animation"
             }
        )
        response = self.client.get('/api/Genres/Ani')
        self.assertEqual(response.status_code, 404)

    def test_random_api_with_loaded_data(self):
        response = self.client.get('/api/Random/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {"movie_ids": [1]}
                         )

    def test_search_api_with_loaded_data(self):
        data = {'search': 'to'}
        response = self.client.get('/api/Search/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        self.assertEqual(response.json(),
                         {"movie_ids": [{"id": 1}],
                          "acotr_ids": [{"actor_id": 1}],
                          "director_ids": [],
                          "writers_ids": []}
                         )
        data = {'search': 'somethingthatcannotbefound'}
        response = self.client.get('/api/Search/', data=data)
        self.assertEqual(response.status_code, 404)

    def test_home_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
