"""
module: media
TODO insert licence boiler plate code
"""
import webbrowser

class Video():
    """
    The Video class is designed as the parent class that will define initials attributes
    and methods that will be common to all subclasses of Video

    Attributes:
        title: A string containing the title of the Video
        duration: An integer (in seconds) of the duration of the Video
        stars: An integer (from 0 to 5) of the rating that you've given the Video
    """
    def __init__(self, title, duration, stars, storyline, poster_image):
        self.title = title
        self.duration = duration
        self.stars = stars
        self.storyline = storyline
        self.poster_image_url = poster_image

    def print_title(self):
        print("Title: "+self.title)

    def print_stars(self):
        print("Stars: "+str(self.stars))

    def print_duration(self):
        print("Duration: "+str(self.duration))

    def convert_duration(self):
        seconds=self.duration
        minutes=seconds/60
        seconds=seconds%60
        hours=minutes/60
        minutes=minutes%60
        self.duration="Runtime: "+str(hours) + "H " + str(minutes) + "M " + str(seconds) + "S"

    def print_storyline(self):
        print("Storyline: "+self.storyline)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)

class Movie(Video):
    """
    This class is designed to be used in conjunction with the fresh_tomatoes module
    This contains the schema for creating a new movie object
    """
    #the following is an example of a class variable
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #the init function will create space in memory
    def __init__(self, movie_title, movie_duration, movie_stars,
                movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, movie_duration, movie_stars, movie_storyline, poster_image)
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)





class TV_Show(Video):
    """
    Class for creating TV shows
    Inherits the Video class
    """
    def __init__(self, tv_show_title, tv_show_runtime, tv_show_stars,
                tv_show_storyline, poster_image, episodes):
        Video.__init__(self, tv_show_title, tv_show_runtime, tv_show_stars,
                    tv_show_storyline, poster_image)
        self.episodes = episodes

    def print_episodes(self):
        print("Episodes: "+self.episodes)
