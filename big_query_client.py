import pandas as pd

# Function to query BigQuery and return results
def get_movies_like(title, client):
    safe_title = title.replace("'", "\\'")  # Basic attempt to sanitize title for safety
    query = f"""
        SELECT title, genres
        FROM `assignment1-416415.moviesdata.movies`
        WHERE title LIKE '{safe_title}%'
        LIMIT 50
    """
    query_job = client.query(query)
    results = query_job.result()  # Wait for the job to complete.
    
    # Collecting results into a dataframe
    movies = []
    for row in results:
        movies.append({'Title': row.title, 'Genres': row.genres})
    return pd.DataFrame(movies)