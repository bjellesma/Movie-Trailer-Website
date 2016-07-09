#importing the module media
import media
import fresh_tomatoes



toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
dDarko = media.Movie("Donnie Darko",
                    "Billy's favorite movie",
                    "https://cinefilles.files.wordpress.com/2013/03/donnie-darko-poster-1.jpg",
                    "https://www.youtube.com/watch?v=qdKbNuhXWvQ")
bClub = media.Movie("Breakfast Club",
                    "Detention!",
                    "https://cauchonphotoclass.edublogs.org/files/2013/06/the-breakfast-club-movie-poster-1985-1020468204-tfrwg0.jpg",
                    "https://www.youtube.com/watch?v=n7wIEC4glrk")

movies = [toy_story, dDarko, bClub]
fresh_tomatoes.open_movies_page(movies)
print("The following is the documentation for the Movie class: \n" + media.Movie.__doc__)
print("The following is the name of the class: \n" + media.Movie.__name__)
print("The following is the name of the module: \n" + media.Movie.__module__)
dDarko.show_title()
