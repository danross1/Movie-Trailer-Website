import webbrowser


# define class Movie
class Movie():
    # initialize class Movie
    # with inputs movie_title et al from instances
    # defined in entertainment_center.py
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # define function to show trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
