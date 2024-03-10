import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from big_query_client import get_movies_like, get_all_genres, get_all_languages
from utils import create_grid

# Authentication and setting up BigQuery client
credentials = service_account.Credentials.from_service_account_file('./key.json')
project_id = 'assignment1-416415'
client = bigquery.Client(credentials=credentials, project=project_id)

# Streamlit UI
st.title("Movie Title Autocomplete")
st.session_state.theme = "light"

# Text input for the user to type the movie title
user_input = st.text_input("Type a movie title and press enter", "")

# Additional filters
rating_filter = st.slider("Minimum rating", 0.0, 5.0, 3.0, 0.1)
year_filter = st.slider("Release year after", 1900, 2023, 2000)
language_filter = st.selectbox("Language", get_all_languages(client), index=0)
genre_filter = st.selectbox("Genre", get_all_genres(client), index=0)

# Load and display movies based on the user's input and additional filters
if user_input:
    # Fetch movies like the user input with additional filters
    movies = get_movies_like(title=user_input, client=client, language=language_filter if language_filter else None, 
                                 genre=genre_filter if genre_filter else None, min_rating=rating_filter if rating_filter else None, 
                                 release_year=year_filter if year_filter else None)
    
    # Display the results in the app
    if len(movies) == 0:
        st.write("No movies found.")
    else:
        # Create a grid layout with the posters
        create_grid(len(movies), movies)
