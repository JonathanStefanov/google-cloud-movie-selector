class Movie:
    def __init__(self, title, rating, posterUrl):
        self.title = title
        self.rating = rating
        self.posterUrl = posterUrl

    def __str__(self):
        return f"{self.title}"