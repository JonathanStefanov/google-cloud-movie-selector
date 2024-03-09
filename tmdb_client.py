import os
import requests
import json  # Import json module for parsing JSON response

API_KEY = os.environ.get('TMDB_API_KEY', '')
base_url = "https://api.themoviedb.org/3/movie/{}?language=en-US"

def get_poster_url_from_id(movie_id):
    url = base_url.format(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }

    response = requests.get(url, headers=headers)
    movie_data = json.loads(response.text)


    if 'poster_path' in movie_data and movie_data['poster_path']:
        poster_path = movie_data['poster_path']
        full_poster_url = "https://image.tmdb.org/t/p/original" + poster_path
        return full_poster_url
    elif 'backdrop_path' in movie_data and movie_data['backdrop_path']:
        poster_path = movie_data['backdrop_path']
        full_poster_url = "https://image.tmdb.org/t/p/original" + poster_path
        return full_poster_url
    else:
        return "https://cdn-icons-png.flaticon.com/512/2748/2748558.png"