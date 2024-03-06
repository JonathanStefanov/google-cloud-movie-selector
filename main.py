import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from big_query_client import get_movies_like
from utils import create_grid

# Authentication and setting up BigQuery client
credentials = service_account.Credentials.from_service_account_file('./key.json')
project_id = 'assignment1-416415'
client = bigquery.Client(credentials=credentials, project=project_id)

# Streamlit UI
st.title("Movie Title Autocomplete")
st.session_state.theme = "light"
# Text input for the user to type the movie title
user_input = st.text_input("Type a movie title", "")

# Only run the query if there is user input to avoid unnecessary costs and errors
if user_input:
    df = get_movies_like(user_input, client)
    # Display the results in the app
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("No movies found.")


# Example usage:
total_tiles = 12  # Total number of tiles you want to display
create_grid(total_tiles)