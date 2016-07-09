#!/usr/bin/env
"""
This is the main file of the program that will open a webpage with a list of favorited movies
"""
import media
import fresh_tomatoes

def prep_movies(movies):
    """
    This function will prepare the movies for proper rendering
    """
    for movie in movies:
        movie.convert_duration()

def prep_shows(shows):
    """
    This function will prepare the movies for proper rendering
    """
    for show in shows:
        show.convert_duration()

def initObjects():
    """
    Function to initialize sample objects
    """
    toy_story = media.Movie("Toy Story",
                            6300,
                            4,
                            "A story of a boy and his toys that come to life",
                            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=vwyZH85NQC4")
    dDarko = media.Movie("Donnie Darko",
                        6285,
                        4,
                        "Billy's favorite movie",
                        "https://cinefilles.files.wordpress.com/2013/03/donnie-darko-poster-1.jpg",
                        "https://www.youtube.com/watch?v=qdKbNuhXWvQ")
    bClub = media.Movie("Breakfast Club",
                        6787,
                        5,
                        "Detention!",
                        "https://cauchonphotoclass.edublogs.org/files/2013/06/the-breakfast-club-movie-poster-1985-1020468204-tfrwg0.jpg",
                        "https://www.youtube.com/watch?v=n7wIEC4glrk")

    dark_matter = media.TV_Show("Dark Matter",
                            3600,
                            4,
                            "A story of six people aboard a spaceship who have no idea who they are",
                            "http://nerdystuff.com/wp-content/uploads/2015/07/DarkMatter1.jpg",
                            15)
    seinfeld = media.TV_Show("Seinfeld",
                        1800,
                        4,
                        "A show about nothing",
                        "http://www.sonypictures.com/tv/seinfeld/assets/images/onesheet.jpg",
                        180)
    game_of_thrones = media.TV_Show("Game of Thrones",
                        3600,
                        5,
                        "A story of 7 kings vying for a seat on the iron throne",
                        "http://i.lv3.hbo.com/custom-assets/img/free-episodes/game-of-thrones-1349.jpg",
                        60)

    #Simply add movies to the movie list and tv shows to the tv shows list
    movies = [toy_story, dDarko, bClub]
    tv_shows = [dark_matter, seinfeld, game_of_thrones]
    #prepare tv shows and movies to work with backend classes
    prep_movies(movies)
    prep_shows(tv_shows)
    #create webpage
    fresh_tomatoes.open_movies_and_tv_page(movies, tv_shows)

initObjects()
