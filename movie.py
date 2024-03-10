import requests
import os

class Movie:
    def __init__(self, title, tmdbId, rating, posterUrl, genres, overview, runtime):
        self.title = title
        self.tmdbId = tmdbId
        self.rating = rating
        self.genres = genres
        self.posterUrl = posterUrl
        self.overview = overview
        self.runtime = runtime
        self.api_key = os.environ.get('TMDB_API_KEY', '')

    def __str__(self):
        return f"{self.title}"
    
    def get_video_url(self):
        # Define the URL for the movie's videos endpoint
        url = f"https://api.themoviedb.org/3/movie/{self.tmdbId}/videos?language=en-US"
        # Prepare the header with authorization
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + self.api_key,
        }
        # Make the request
        response = requests.get(url, headers=headers)
        video_data = response.json()  # Directly parse the JSON response

        # Check if there are any videos available
        if 'results' in video_data and video_data['results']:
            key = video_data['results'][0]['key']  # Get the key of the first video
            return f"https://www.youtube.com/watch?v={key}"
        
        # Return None if no videos are found
        return None