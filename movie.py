import requests
import os
from typing import Union

class Movie:
    """
    A class to represent a movie with attributes from The Movie Database (TMDB).
    
    Attributes:
        title (str): The title of the movie.
        tmdbId (int): The TMDB identifier for the movie.
        rating (float): The movie's rating.
        posterUrl (str): URL to the movie's poster image.
        genres (list): List of genres associated with the movie.
        overview (str): A brief overview of the movie.
        runtime (int): The runtime of the movie in minutes.
        api_key (str): TMDB API key for making requests.
    """
    
    def __init__(self, title, tmdbId, rating, posterUrl, genres, overview, runtime):
        """
        Initializes the Movie object with title, TMDB ID, rating, poster URL, genres, overview, and runtime.
        """
        self.title = title
        self.tmdbId = tmdbId
        self.rating = rating
        self.genres = genres
        self.posterUrl = posterUrl
        self.overview = overview
        self.runtime = runtime
        self.api_key = os.environ.get('TMDB_API_KEY', '')

    def __str__(self):
        """
        Returns the string representation of the Movie object.
        """
        return self.title
    
    def get_video_url(self) -> Union[str, None]:
        """
        Fetches the URL for the movie's first video (e.g., a trailer) on YouTube.
        
        Returns:
            str or None: The URL of the video if available; otherwise, None.
        """
        # Define the URL for the movie's videos endpoint
        url = f"https://api.themoviedb.org/3/movie/{self.tmdbId}/videos?language=en-US"
        # Prepare the header with authorization
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + self.api_key,
        }
        # Make the request and parse the JSON response directly
        response = requests.get(url, headers=headers)
        video_data = response.json()

        # Extract and return the first video URL if available
        if video_data.get('results'):
            key = video_data['results'][0]['key']  # Get the key of the first video
            return f"https://www.youtube.com/watch?v={key}"
        
        return None
