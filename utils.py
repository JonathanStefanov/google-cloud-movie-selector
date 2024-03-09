import streamlit as st
from movie import Movie  # Ensure this import is correctly pointing to your Movie class file
import math

def create_grid(total_tiles, movies, height_per_tile=300):
    """
    Create a grid layout with a specified number of tiles, displaying movie posters, titles, and ratings using star emojis.

    Parameters:
    - total_tiles: int, the total number of tiles to create.
    - movies: list, a list of Movie objects. This list should have at least 'total_tiles' elements.
    - height_per_tile: int, height of each tile in pixels.
    """
    rows_needed = total_tiles // 3  # Number of full rows
    extra_tiles = total_tiles % 3  # Tiles in the last row, if any

    tile_index = 0  # Keep track of which tile we're on, to match with the corresponding movie

    # Generate full rows
    for _ in range(rows_needed):
        row = st.columns(3)  # Create a row with 3 columns
        for col in row:
            if movies and tile_index < len(movies):
                movie = movies[tile_index]
                rating_stars = "⭐️" * math.floor(movie.rating)  # Convert rating to floor integer and then to stars
                tile = col.container()
                tile.image(movie.posterUrl, caption=f"{movie.title} ({rating_stars})", width=200)  # Adjust width as needed
                tile_index += 1

    # Generate the last row, if there are extra tiles
    if extra_tiles > 0:
        last_row = st.columns(extra_tiles)  # Create a row for the remaining tiles
        for col in last_row:
            if movies and tile_index < len(movies):
                movie = movies[tile_index]
                rating_stars = "⭐️" * math.floor(movie.rating)  # Convert rating to floor integer and then to stars
                tile = col.container()
                tile.image(movie.posterUrl, caption=f"{movie.title} ({rating_stars})", width=200)  # Adjust width as needed
                tile_index += 1
