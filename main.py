import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from big_query_client import get_movies_like
from utils import create_grid
from tmdb_client import get_poster_url_from_id
import time

# Authentication and setting up BigQuery client
credentials = service_account.Credentials.from_service_account_file('./key.json')
project_id = 'assignment1-416415'
client = bigquery.Client(credentials=credentials, project=project_id)

# Streamlit UI
st.title("Movie Title Autocomplete")
st.session_state.theme = "light"

# Initialize session state for debounce
if 'last_query_time' not in st.session_state:
    st.session_state['last_query_time'] = time.time()

# Function to load movies based on input
def load_movies():
    user_input = st.session_state.user_input
    current_time = time.time()
    # Simple debounce mechanism: Only run if certain time has passed since last query
    if user_input and (current_time - st.session_state['last_query_time']) > 0.5:  # 0.5 seconds debounce
        df, movies = get_movies_like(user_input, client)
        # Display the results in the app
        if df.empty:
            st.write("No movies found.")
        else:
            st.dataframe(df)

            # Create a grid layout with the posters
            create_grid(len(movies), movies)
        st.session_state['last_query_time'] = time.time()

# Text input for the user to type the movie title with callback
user_input = st.text_input("Type a movie title", "", key="user_input", on_change=load_movies)
