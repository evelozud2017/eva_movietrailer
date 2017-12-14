import webbrowser


class Movie():
    """This class provides a way to store movie information and show trailer"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Constructor that sets movie title, storyline, poster and trailer"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Method that opens browser and play the movie trailer"""
        webbrowser.open(self.trailer_youtube_url)
