#!/usr/bin/env
"""
This is the main file of the program that will open a webpage with a list of favorited movies

Adding Objects:
    The format for adding objects is to assign a variable name to media.Movie or media.TV_Show
    and to use the proper argument list listed below.

Arg List for media.Movie:
    Movie Title: string
    Movie Duration (in seconds): integer
    Movie Rating (out of 10): integer
    Movie Storyline: String
    Movie Poster URL: string
    Movie Trailer: string

Arg List for media.TV_Show:
    TV Show Title: string
    TV Show Runtime (in seconds): integer
    TV Show Rating (out of 10): integer
    TV Show Storyline: String
    TV Show Poster URL: string
    TV Show Episodes: integer
"""
import media
import fresh_tomatoes
import imdb

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
    i = imdb.IMDb()
    toyStoryID = '0114709'
    dDarkoID = '0246578'
    bClubID = '0088847'
    #dark_matter_ID = '0159076'
    #seinfeld_ID = '0098904'
    #game_of_Thrones_ID = '0944947'
    #print(i.get_movie(dark_matter_ID))
    toy_story = media.Movie(i.get_movie(toyStoryID).get('title'),
                            6300,
                            i.get_movie(toyStoryID).get('rating'),
                            "A story of a boy and his toys that come to life",
                            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=vwyZH85NQC4")
    dDarko = media.Movie(i.get_movie(dDarkoID).get('title'),
                        6285,
                        i.get_movie(dDarkoID).get('rating'),
                        "Billy's favorite movie",
                        "https://cinefilles.files.wordpress.com/2013/03/donnie-darko-poster-1.jpg",
                        "https://www.youtube.com/watch?v=qdKbNuhXWvQ")
    bClub = media.Movie(i.get_movie(bClubID).get('title'),
                        6787,
                        i.get_movie(bClubID).get('rating'),
                        "Detention!",
                        "https://cauchonphotoclass.edublogs.org/files/2013/06/the-breakfast-club-movie-poster-1985-1020468204-tfrwg0.jpg",
                        "https://www.youtube.com/watch?v=ZXzlCpHK3-I")

    dark_matter = media.TV_Show("Dark Matter",
                            3600,
                            4,
                            "A story of six people aboard a spaceship who have no idea who they are",
                            "http://sharingseries.com/wp-content/uploads/2015/05/Dark-Matter-poster-SyFy-season-1-2015.jpg",
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
                        "http://coppergoose.com/static/uploaded/eggs/game-of-thrones-book-1.png",
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
