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

IMDbpY Integration:
    Optionally, An IMDb API can be used to retrieve certain information
    the advantage being that their information is always up to date.
    Several variables are used for this purpose in initObjects()
    The variables follow the naming scheme of [object_name]ID for the IMDb ID
    and [object_name]_imdb for the imdb movie object
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
    #imdb objects
    #you can use the imdb api to help grab information rather than looking it up
    #full documentation at imdbpy.sourceforge.net
    i = imdb.IMDb()
    toy_story_ID = '0114709'
    toy_story_imdb = i.get_movie(toy_story_ID)
    dDarko_ID = '0246578'
    dDarko_imdb = i.get_movie(dDarko_ID)
    bClub_ID = '0088847'
    bClub_imdb = i.get_movie(bClub_ID)
    dark_matter_ID = '4159076'
    dark_matter_imdb = i.get_movie(dark_matter_ID)
    seinfeld_ID = '0098904'
    seinfeld_imdb = i.get_movie(seinfeld_ID)
    game_of_thrones_ID = '0944947'
    game_of_thrones_imdb = i.get_movie(game_of_thrones_ID)
    #
    # End of IMDb objects 
    #

    toy_story = media.Movie(toy_story_imdb.get('title'),
                            6300,
                            toy_story_imdb.get('rating'),
                            "A story of a boy and his toys that come to life",
                            toy_story_imdb.get('cover url'),
                            "https://www.youtube.com/watch?v=vwyZH85NQC4")
    dDarko = media.Movie(dDarko_imdb.get('title'),
                        6285,
                        dDarko_imdb.get('rating'),
                        "A troubled youth and his imaginary friend",
                        dDarko_imdb.get('cover url'),
                        "https://www.youtube.com/watch?v=qdKbNuhXWvQ")
    bClub = media.Movie(bClub_imdb.get('title'),
                        6787,
                        bClub_imdb.get('rating'),
                        "Detention!",
                        bClub_imdb.get('cover url'),
                        "https://www.youtube.com/watch?v=ZXzlCpHK3-I")

    dark_matter = media.TV_Show(dark_matter_imdb.get('title'),
                            3600,
                            dark_matter_imdb.get('rating'),
                            "Six people aboard a spaceship have no idea who they are",
                            dark_matter_imdb.get('cover url'),
                            16)
    seinfeld = media.TV_Show(seinfeld_imdb.get('title'),
                        1800,
                        seinfeld_imdb.get('rating'),
                        "A show about nothing",
                        seinfeld_imdb.get('cover url'),
                        180)
    game_of_thrones = media.TV_Show(game_of_thrones_imdb.get('title'),
                        3600,
                        game_of_thrones_imdb.get('rating'),
                        "7 kings vying for a seat on the iron throne",
                        game_of_thrones_imdb.get('cover url'),
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
