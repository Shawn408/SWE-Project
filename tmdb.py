import requests
import os
from dotenv import find_dotenv,load_dotenv

load_dotenv(find_dotenv())

BASE_URL = 'https://api.themoviedb.org/3/movie'
IMAGE_URL = 'https://api.themoviedb.org/3/configuration'

def get_movie_info(movie_id):
    
    params = {
        'movie_id' : movie_id,
        'api_key': os.getenv('API_KEY')
    }

    response = requests.get(f'{BASE_URL}/{movie_id}', params=params)

    def get_title(film):
        film = response.json()['title']
        return film

    def get_tagline(film):
        film = response.json()['tagline']
        return film
    
    def get_genre(film):
        film = response.json()['genres']
        genre = []
        for i in range(len(film)):
            genre.append(film[i]['name'])
        return ", ".join(genre)
    
    def get_similar(film):
        response_video = requests.get(f'{BASE_URL}/{movie_id}/similar', params=params)
        data = response_video.json()
        film = data['results']
        site = []
        for i in range(len(film)):
            site.append(film[i]['id'])
        return site
    
    image = response.json()['poster_path']
    params2 = {
        'api_key': os.getenv('API_KEY')
    }
    response2 = requests.get(f'{IMAGE_URL}', params=params2)
    data = response2.json()
    baseurl = data['images']['base_url']
        
    movie_id=response.json()['id']
    title = get_title(response)
    tagline = get_tagline(response)
    genre = get_genre(response)
    site = get_similar(response)
    
    
    return{
        'movie_id': movie_id,
        'title': title,
        'tagline': tagline,
        'genre': genre,
        'site': site,
        'image': image,
        'baseurl': baseurl
    }
