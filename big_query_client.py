import pandas as pd
from movie import Movie
from tmdb_client import get_info_from_id

def get_movies_like(title, client, language=None, genre=None, min_rating=None, release_year=None):
    # Sanitizing title for safety. This is a very basic form of sanitization.
    safe_title = title.replace("'", "\\'")
    
    # Base query
    query_parts = [
        "SELECT m.title, m.tmdbId, m.genres, AVG(r.rating) as average_rating",
        "FROM `assignment1-416415.moviesdata.movies` m",
        "INNER JOIN `assignment1-416415.moviesdata.ratings` r ON m.movieId = r.movieId",
        f"WHERE m.title LIKE '{safe_title}%'"
    ]
    
    # Adding filters
    if language:
        query_parts.append(f"AND m.language = '{language}'")
    if genre:
        query_parts.append(f"AND m.genres LIKE '%{genre}%'")
    if release_year:
        query_parts.append(f"AND m.release_year > {release_year}")
    # Include m.genres in GROUP BY clause
    query_parts.append("GROUP BY m.title, m.tmdbId, m.genres")
    if min_rating:
        query_parts.append(f"HAVING AVG(r.rating) > {min_rating}")
    query_parts.append("ORDER BY average_rating DESC")
    query_parts.append("LIMIT 50;")
    
    query = " ".join(query_parts)
    
    query_job = client.query(query)
    results = query_job.result()  # Wait for the job to complete.
    
    # Collecting results into a dataframe and a list of Movie objects
    movies_df = []
    movies = []
    for row in results:
        # Assuming genres are stored as a delimited string, we split them here for the Movie object
        genres = row.genres.split('|') if row.genres else []
        poster_url, overview, runtime = get_info_from_id(row.tmdbId)
        movies.append(Movie(row.title, row.average_rating, poster_url, genres, overview, runtime))
        movies_df.append({'Title': row.title, 'MovieId': row.tmdbId, 'Rating': row.average_rating, 'Genres': row.genres})
    return pd.DataFrame(movies_df), movies
