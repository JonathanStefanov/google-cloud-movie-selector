# Movie Visualiser App 🎬🔍

Welcome to the Movie Visualiser app, the ultimate tool for movie enthusiasts! Dive into a vast ocean of films and find your next favorite flick in just a few clicks.

[Access App](https://movie-visualizer-bz4aqyjydq-oa.a.run.app/)


## Features

- **Auto-complete Functionality**: Just start typing, and our app will suggest movie titles instantly. 🧠💡
- **Advanced Filters**: Search movies by minimum rating, release year, language, and genre to find the perfect match for your movie night. 🔍
- **Detailed Information**: Get in-depth details about the movies, including ratings, genres, summaries, and more. 🎥📖
- **Caching System**: Enjoy faster searches with our smart caching system that reduces load times and improves your experience. ⚡🗃️

## How It Works

1. **Enter a Movie Title**: Start typing the name of the movie you're interested in.
2. **Refine Your Search**: Use the sliders and dropdowns to set your preferences for rating, year, language, and genre.
3. **Explore Results**: View a list of movies that match your criteria, complete with ratings and an option to get more information.
4. **Get the Details**: Click on 'More info' to learn more about the movie, including a synopsis and a preview if available.

## Technologies Used

- **Google BigQuery**: Our backend is powered by BigQuery for handling massive datasets with ease. 🗄️🚀
- **Google Cloud Run**: The app is hosted on Google Cloud Run for a fully managed, serverless experience. ☁️✨
- **The Movie Database (TMDB) API**: We enrich our movie data with additional details fetched from the TMDB API. 🎞️📊

## File Explanation
- **streamlit_app.py**: The main script that uses Streamlit to create the web interface. It integrates all other components, handling user input and displaying search results and detailed movie pages.

- **movie.py**: Defines the `Movie` class, representing a movie with attributes like title, TMDB ID, rating, poster URL, genres, overview, and runtime. It also includes a method to fetch video URLs (e.g., trailers) from TMDB.

- **tmdb_client.py**: Contains functions to interact with The Movie Database (TMDB) API. It fetches additional movie details like poster URLs, overviews, and runtimes using the TMDB API, enriching the data obtained from BigQuery.

- **grid.py**: Utilizes Streamlit to display search results in a grid layout. Each grid tile shows a movie's poster, title, rating in stars, and includes a "More info" button for accessing detailed information.

- **movie_page.py**: Renders a detailed view of a selected movie. This page displays the movie's title, rating, genres, summary, runtime, and a video preview (if available) using information fetched from TMDB.

- **utils.py**: Provides additional utility functions for the app, like creating a grid layout for movie tiles. This file might contain common functions used across different parts of the app to avoid code duplication.

- **big_query_client.py**: Handles communication with Google Cloud's BigQuery. It includes functions for setting up the BigQuery client, querying movies based on user input and selected filters, and fetching lists of available languages and genres from the dataset.
