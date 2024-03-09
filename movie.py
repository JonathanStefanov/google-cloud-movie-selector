class Movie:
    def __init__(self, title, rating, posterUrl, genres, overview, runtime):
        self.title = title
        self.rating = rating
        self.genres = genres
        self.posterUrl = posterUrl
        self.overview = overview
        self.runtime = runtime

    def __str__(self):
        return f"{self.title}"