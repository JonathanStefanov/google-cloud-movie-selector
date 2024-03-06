import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Authentication and setting up BigQuery client
credentials = service_account.Credentials.from_service_account_file('./key.json')
project_id = 'assignment1-416415'
client = bigquery.Client(credentials=credentials, project=project_id)

# Streamlit UI
st.title("Movie Title Autocomplete")

# Text input for the user to type the movie title
user_input = st.text_input("Type a movie title", "")

# Function to query BigQuery and return results
def get_movies_like(title):
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

# Only run the query if there is user input to avoid unnecessary costs and errors
if user_input:
    df = get_movies_like(user_input)
    # Display the results in the app
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("No movies found.")
