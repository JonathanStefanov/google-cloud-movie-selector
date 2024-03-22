import pandas as pd
from movie import Movie
from tmdb_client import get_info_from_id
import streamlit as st
from google.cloud import bigquery
from typing import List
from google.oauth2 import service_account


# Initializes BigQuery client with credentials
def setup_bigquery_client() -> bigquery.Client:
    """
    Sets up and returns a BigQuery client using credentials from a service account file.
    """
    credentials = service_account.Credentials.from_service_account_file('./key.json')
    project_id = 'assignment1-416415'
    return bigquery.Client(credentials=credentials, project=project_id)


# lambda function so that the bigquery client alwars returns 1, this way even if it changes id somehow it will still return the same hash and the cache will still work
@st.cache_data(hash_funcs={bigquery.client.Client: lambda _: 1}, ttl=24*60*60)
def get_movies_like(client: bigquery.Client, title = None, language=None, genre=[], min_rating=None, release_year=None) -> List[Movie]:
    # Sanitizing title for safety. This is a very basic form of sanitization.
    safe_title = title.replace("'", "\\'")

    if language == "Any":
        language = None
    if genre == "None":
        genre = None

    
    # Base query
    query_parts = [
        "SELECT m.title, m.tmdbId, m.genres, AVG(r.rating) as average_rating",
        "FROM `assignment1-416415.moviesdata.movies` m",
        "INNER JOIN `assignment1-416415.moviesdata.ratings` r ON m.movieId = r.movieId",
    ]
    # TODO: Make sure %{safe_title}% or just {safe_title}% search/autocomplete
    
    # Adding filters
    if title:
        query_parts.append(f"WHERE LOWER(m.title) LIKE '{safe_title}%'")
    if language:
        query_parts.append(f"AND m.language = '{language}'")
    if genre:
        genres_condition = " OR ".join(f"m.genres LIKE '%{g}%'" for g in genre)
        query_parts.append(f"AND ({genres_condition})")
    if release_year:
        query_parts.append(f"AND m.release_year > {release_year[0]} AND m.release_year < {release_year[1]}")
    # Include m.genres in GROUP BY clause
    query_parts.append("GROUP BY m.title, m.tmdbId, m.genres")
    if min_rating:
        query_parts.append(f"HAVING AVG(r.rating) > {min_rating}")
    query_parts.append("ORDER BY average_rating DESC")
    query_parts.append("LIMIT 30;")
    
    query = " ".join(query_parts)
    
    query_job = client.query(query)
    results = query_job.result()  # Wait for the job to complete.
    
    # Collecting results into a dataframe and a list of Movie objects
    movies = []
    for row in results:
        # Assuming genres are stored as a delimited string, we split them here for the Movie object
        genres = row.genres.split('|') if row.genres else []
        poster_url, overview, runtime = get_info_from_id(row.tmdbId)
        movies.append(Movie(row.title, row.tmdbId,row.average_rating, poster_url, genres, overview, runtime))
    return movies

@st.cache_data(hash_funcs={bigquery.client.Client: lambda _: 1}, ttl=24*60*60)
def get_all_languages(client: bigquery.Client) -> List[str]:
    query = "SELECT DISTINCT language FROM `assignment1-416415.moviesdata.movies`"
    query_job = client.query(query)
    results = query_job.result()  # Wait for the job to complete.
    languages = ["Any"]  # Prepend "None" to the list of languages
    languages.extend(row.language for row in results if row.language)
    return languages

@st.cache_data(hash_funcs={bigquery.client.Client: lambda _: 1}, ttl=24*60*60)
def get_all_genres(client: bigquery.Client) -> List[str]:
    query = "SELECT DISTINCT genres FROM `assignment1-416415.moviesdata.movies`"
    query_job = client.query(query)
    results = query_job.result()
    genres = set()
    for row in results:
        if row.genres:
            genres.update(row.genres.split('|'))

    return genres

