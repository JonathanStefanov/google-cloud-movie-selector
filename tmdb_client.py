import os
import requests

API_KEY = os.environ.get('TMDB_API_KEY', '')

def get_poster_from_id(movie_id):
    