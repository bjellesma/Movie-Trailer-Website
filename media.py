import webbrowser

class Video():
    def __init__(self, title, duration=200):
        self.title = title
        self.duration = duration

    def show_title(self):
        print("Title: "+self.title)

class Movie(Video):
    """
    This class is designed to be used in conjunction with the fresh_tomatoes module
    This contains the schema for creating a new movie object
    """
    #the following is an example of a class variable
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #the init function will create space in memory
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
