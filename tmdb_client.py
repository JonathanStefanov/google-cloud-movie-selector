import os
import requests
import json  # Import json module for parsing JSON response

API_KEY = os.environ.get('TMDB_API_KEY', '')
base_url = "https://api.themoviedb.org/3/movie/{}?language=en-US"

def get_info_from_id(movie_id: int):
    url = base_url.format(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }

    response = requests.get(url, headers=headers)
    movie_data = json.loads(response.text)
    full_poster_url = ""


    if 'poster_path' in movie_data and movie_data['poster_path']:
        poster_path = movie_data['poster_path']
        full_poster_url = "https://image.tmdb.org/t/p/original" + poster_path
    elif 'backdrop_path' in movie_data and movie_data['backdrop_path']:
        poster_path = movie_data['backdrop_path']
        full_poster_url = "https://image.tmdb.org/t/p/original" + poster_path
    else:
        full_poster_url = "https://cdn-icons-png.flaticon.com/512/2748/2748558.png"
    
    return full_poster_url, movie_data['overview'], movie_data['runtime']

def get_video_from_id(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }

    response = requests.get(url, headers=headers)
    video_data = json.loads(response.text)

    if 'results' in video_data and video_data['results']:
        key = video_data['results'][0]['key']
        return f"https://www.youtube.com/watch?v={key}"
    
    return None
