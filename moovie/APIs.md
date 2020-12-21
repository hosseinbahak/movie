# Readme for all APIs

This is a readme for APIs.

## /api/Actors/

- GET : returns a json
- Output : List of all actors
- Example :

```json
[
  {
    "actor_id": 31,
    "name": "Tom Hanks",
    "gender": "M",
    "pic": "/pQFoyx7rp09CJTAb932F2g8Nlho.jpg",
    "movie_ids": "862,345,1778",
    "url": "http://127.0.0.1:8000/api/Actors/31"
  },
  {
    "actor_id": 12898,
    "name": "Tim Allen",
    "gender": "M",
    "pic": "/uX2xVf6pMmPepxnvFWyBtjexzgY.jpg",
    "movie_ids": "862,654,124,875",
    "url": "http://127.0.0.1:8000/api/Actors/12898"
  }
]
```

if 'gender' == 'M' then : actor is Male

if 'gender' == 'F' then : actor is Female

'movie_ids' : all movie ids from that Actor

'url' : a link to actor api with 'actor_id'

### /api/Actors/2157

Example :

```json
{
  "actor_id": 2157,
  "name": "Robin Williams",
  "gender": "M",
  "pic": "/sojtJyIV3lkUeThD7A2oHNm8183.jpg",
  "movie_ids": "8844"
}
```

## /api/Genres/

- GET : returns a json
- Output : List of all genres
- Example :

```json
[
  {
    "name": "Animation",
    "movie_ids": [862, 21032, 10530],
    "url": "http://127.0.0.1:8000/api/Genres/Animation"
  },
  {
    "name": "Comedy",
    "movie_ids": [862, 15602, 31357],
    "url": "http://127.0.0.1:8000/api/Genres/Comedy"
  }
]
```

'url' : a link to genre api with 'name' of genre

### /api/Genres/Drama

- Example :

```json
{
  "name": "Drama",
  "movie_ids": [31357, 949, 45325],
  "url": "http://127.0.0.1:8000/api/Genres/Drama"
}
```

## /api/Random

- GET : returns a json
- Input : num (optional)
- Output : List of 10 random movie ids if num hasn't been sent, if you send num=5 the 5 movie ids will be sent
- Example :

```json
{
  "movie_ids": [9691, 12110, 35196, 1408, 9312, 11517, 11443, 577, 1710, 10530]
}
```

### /api/Random/?num=3

- This api request will send only 3 random movie ids
- Example :

```json
{
  "movie_ids": [9087, 687, 8391]
}
```

## /api/Movie/862

- GET : returns a json
- Input: movie_id
- Output : movie details
- Example :

```json
[
  {
    "id": 862,
    "title": "Toy Story",
    "budget": 30000000,
    "genres": "Animation,Comedy,Family",
    "language": "en",
    "overview": "Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",
    "companies": "Pixar Animation Studios",
    "countries": "United States of America",
    "release_date": "1995-10-30",
    "revenue": 373554033,
    "runtime": 81.0,
    "vote_average": 7.7,
    "vote_count": 5415,
    "poster": "/rhIRbceoE9lR4veEXuwCC2wARtG.jpg"
  }
]
```

## /api/Search/?search=

- GET : returns a json
- Input: search
- Output : movie, actor, director, writer ids
- Example :

```json
{
  "movie_ids": [
    {
      "id": 45325
    }
  ],
  "acotr_ids": [
    {
      "actor_id": 31
    },
    {
      "actor_id": 3197
    },
    {
      "actor_id": 119232
    }
  ],
  "director_ids": [],
  "writers_ids": []
}
```

## /api/ReleaseDate/

- GET : returns a json
- Input: -
- Output : movie details of top 20 movies sorted by last release

## /api/TopRated/

- GET : returns a json
- Input: -
- Output : movie details of top 20 movies sorted by most rate
