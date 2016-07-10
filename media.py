"""
module: media
author: William Jellesma

This module provides the three classes necessary to rendered the movie webpage
"""
import webbrowser

class Video():
    """
    The Video class is designed as the parent class that will define initials attributes
    and methods that will be common to all subclasses of Video

    Attributes:
        title: A string containing the title of the Video
        duration: An integer (in seconds) of the duration of the Video
        stars: A float (from 0 to 10) of the rating that you've given the Video
        storyline: A string containing the main story summation
        poster_image: A string containing a url of an image
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
        print("IMDb Rating: "+str(self.stars))

    def print_duration(self):
        print("Duration: "+str(self.duration))

    def print_storyline(self):
        print("Storyline: "+self.storyline)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)


    def convert_duration(self):
        """
        Function to convert raw seconds to H-M-S Format
        """
        seconds=self.duration
        minutes=seconds/60
        seconds=seconds%60
        hours=minutes/60
        minutes=minutes%60
        self.duration="Runtime: "+str(hours) + "H " + str(minutes) + "M " + str(seconds) + "S"


class Movie(Video):
    """
    This class is designed to be used in conjunction with the fresh_tomatoes module
    This contains the schema for creating a new movie object

    Inherits:
        Video

    Attributes:
        title: A string containing the title of the Video
        duration: An integer (in seconds) of the duration of the Video
        stars: A float (from 0 to 10) of the rating that you've given the Video
        storyline: A string containing the main story summation
        poster_image: A string containing a url of an image
        trailer_youtube: A string containing a link to the youtube trailer
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

    Inherits:
        Video

    Attributes:
        title: A string containing the title of the Video
        duration: An integer (in seconds) of the duration of the Video
        stars: A float (from 0 to 10) of the rating that you've given the Video
        storyline: A string containing the main story summation
        poster_image: A string containing a url of an image
        trailer_youtube: A string containing a link to the youtube trailer
    """
    def __init__(self, tv_show_title, tv_show_runtime, tv_show_stars,
                tv_show_storyline, poster_image, episodes):
        Video.__init__(self, tv_show_title, tv_show_runtime, tv_show_stars,
                    tv_show_storyline, poster_image)
        self.episodes = episodes

    def print_episodes(self):
        print("Episodes: "+self.episodes)
