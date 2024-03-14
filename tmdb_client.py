import os
import requests
import json

# Retrieve TMDB API key from environment variables
API_KEY = os.environ.get('TMDB_API_KEY', '')
# Base URL for fetching movie details from TMDB
base_url = "https://api.themoviedb.org/3/movie/{}?language=en-US"

def get_info_from_id(movie_id: int) -> tuple:
    """
    Fetches movie information by ID from The Movie Database (TMDB).
    
    Parameters:
        movie_id (int): The unique identifier for the movie in TMDB.
        
    Returns:
        tuple: A tuple containing the full poster URL, movie overview, and runtime.
    """
    # Format the URL with the specified movie ID
    url = base_url.format(movie_id)
    # Set the request headers with authorization
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + API_KEY,
    }
    # Perform the HTTP request to TMDB API
    response = requests.get(url, headers=headers)
    # Parse the JSON response into a dictionary
    movie_data = json.loads(response.text)
    
    # Determine the full poster URL based on available paths
    if 'poster_path' in movie_data and movie_data['poster_path']:
        poster_path = movie_data['poster_path']
        full_poster_url = "https://image.tmdb.org/t/p/original" + poster_path
    elif 'backdrop_path' in movie_data and movie_data['backdrop_path']:
        poster_path = movie_data['backdrop_path']
        full_poster_url = "https://image.tmdb.org/t/p/original" + poster_path
    else:
        # Default poster if no image path is available
        full_poster_url = "https://cdn-icons-png.flaticon.com/512/2748/2748558.png"
    
    # Return the movie details
    return full_poster_url, movie_data.get('overview', ''), movie_data.get('runtime', 0)
