import streamlit as st
from movie import Movie
from tmdb_client import get_video_from_id

def movie_page(movie: Movie):
    st.markdown("<h1 style='text-align: center;'>More Details</h1>", unsafe_allow_html=True)
    st.write(f"Title: {movie.title}")
    st.write(f"Rating: {movie.rating}")
    st.write(f"Genres: {', '.join(movie.genres)}")
    st.write(f"Overview: {movie.overview}")
    st.write(f"Runtime: {movie.runtime} minutes")
    video_url = get_video_from_id(movie.tmdbId) 

    if video_url:
        st.video(video_url)
    else:
        st.write("Video unavailable.")