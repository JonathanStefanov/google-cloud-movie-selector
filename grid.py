import streamlit as st
from movie import Movie  # Ensure this import is correctly pointing to your Movie class file
from movie_page import movie_page
import math

def display_movies(movies: Movie, height_per_tile=300):
    """
    Create a grid layout with a specified number of tiles, displaying movie posters, titles, and ratings using star emojis.

    Parameters:
    - total_tiles: int, the total number of tiles to create.
    - movies: list, a list of Movie objects. This list should have at least 'total_tiles' elements.
    - height_per_tile: int, height of each tile in pixels.
    """
    
    def create_tile(movie, col):
        """Create a tile for a movie."""
        rating_stars = "⭐️" * math.floor(movie.rating)  # Convert rating to floor integer and then to stars
        tile = col.container()
        tile.image(movie.posterUrl, caption=f"{movie.title} ({rating_stars})", width=200)  # Adjust width as needed
        click = tile.button("More info", key=movie.title)
        if click:
            movie_page(movie)


    total_tiles = len(movies)
    tiles_per_row = 3
    total_rows = (total_tiles + tiles_per_row - 1) // tiles_per_row  # Calculates the total number of rows needed, rounding up

    tile_index = 0  # Keep track of which tile we're on

    # Generate rows and tiles
    for _ in range(total_rows):
        # Determine the number of columns for the current row (it may be less than tiles_per_row for the last row)
        cols_in_row = tiles_per_row if (total_tiles - tile_index) >= tiles_per_row else (total_tiles - tile_index) % tiles_per_row
        row = st.columns(cols_in_row)
        
        for col in row:
            if tile_index < len(movies):
                create_tile(movies[tile_index], col)
                tile_index += 1

