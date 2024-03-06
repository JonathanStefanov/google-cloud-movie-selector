import streamlit as st

def create_grid(total_tiles, height_per_tile=300):
    # Calculate the number of full rows needed and the number of tiles in the last row
    rows_needed = total_tiles // 5  # Number of full rows
    extra_tiles = total_tiles % 5  # Tiles in the last row, if any

    # Generate full rows
    for _ in range(rows_needed):
        row = st.columns(5)  # Create a row with 5 columns
        for col in row:
            tile = col.container()  # Create a container for each tile
            tile.title(":balloon:")  # Example content, you can customize it
            tile.write("Content goes here")  # Additional example content

    # Generate the last row, if there are extra tiles
    if extra_tiles > 0:
        last_row = st.columns(extra_tiles)  # Create a row for the remaining tiles
        for col in last_row:
            tile = col.container()
            tile.title(":balloon:")
            tile.write("Content goes here")