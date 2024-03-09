import pandas as pd
from movie import Movie
from tmdb_client import get_poster_url_from_id

# Function to query BigQuery and return results
def get_movies_like(title, client):
    # Basic attempt to sanitize title for safety. Be aware this is a very basic form of sanitization.
    # For production code, consider using parameterized queries to prevent SQL injection.
    safe_title = title.replace("'", "\\'")
    query = f"""
        SELECT m.title, m.tmdbId, AVG(r.rating) as average_rating
        FROM `assignment1-416415.moviesdata.movies` m
        INNER JOIN `assignment1-416415.moviesdata.ratings` r ON m.movieId = r.movieId
        WHERE m.title LIKE '{safe_title}%'
        GROUP BY m.title, m.tmdbId
        ORDER BY average_rating DESC
        LIMIT 50;
    """
    query_job = client.query(query)
    results = query_job.result()  # Wait for the job to complete.
    
    # Collecting results into a dataframe
    movies_df = []
    movies = []
    for row in results:
        movies.append(Movie(row.title, row.average_rating, get_poster_url_from_id(row.tmdbId)))
        movies_df.append({'Title': row.title, 'MovieId': row.tmdbId, 'Rating': row.average_rating})
    return pd.DataFrame(movies_df), movies
