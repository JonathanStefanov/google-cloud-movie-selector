import streamlit as st
from movie import Movie

def movie_page(movie: Movie):
    st.markdown("<h1 style='text-align: center;'>More Details</h1>", unsafe_allow_html=True)
    st.write(f"Title: {movie.title}")
    st.write(f"Rating: {round(movie.rating, 2)}")
    st.write(f"Genres: {', '.join(movie.genres)}")
    st.write(f"Overview: {movie.overview}")
    st.write(f"Runtime: {movie.runtime} minutes")
    video_url = movie.get_video_url()

    if video_url:
        st.video(video_url)
    else:
        st.write("Video unavailable.")