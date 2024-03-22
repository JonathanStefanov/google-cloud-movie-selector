import streamlit as st
import pandas as pd
from google.cloud import bigquery
from big_query_client import get_movies_like, get_all_genres, get_all_languages
from grid import display_movies
from big_query_client import setup_bigquery_client


def main():
    """
    Main function to run the Streamlit app for movie title autocomplete with additional filters.
    """
    client = setup_bigquery_client()

    # Streamlit UI setup
    st.title("Google Cloud Movie Visualizer")

    # Input from the user for the movie title
    user_input = st.text_input("Type a movie title and press enter", "")

    # Additional filter options
    rating_filter = st.slider("Minimum rating", 0.0, 5.0, 3.0, 0.1)
    year_filter = st.slider("Release year after", 1891, 2023, [2010, 2020])
    language_filter = st.selectbox("Language", get_all_languages(client), index=0)
    genre_filter = st.multiselect("Genre", get_all_genres(client))

    # Display movies based on the filters
    user_input = user_input.lower()
    movies = get_movies_like(title=user_input, client=client, language=language_filter if language_filter else None, 
                                genre=genre_filter if genre_filter else [], min_rating=rating_filter if rating_filter else None, 
                                release_year=year_filter if year_filter else None)
    
    if not movies:
        st.write("No movies found.")
    else:
        display_movies(movies)
if __name__ == "__main__":
    main()
