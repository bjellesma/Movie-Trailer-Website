#importing the module media
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        6300,
                        4,
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
dDarko = media.Movie("Donnie Darko",
                    6300,
                    4,
                    "Billy's favorite movie",
                    "https://cinefilles.files.wordpress.com/2013/03/donnie-darko-poster-1.jpg",
                    "https://www.youtube.com/watch?v=qdKbNuhXWvQ")
bClub = media.Movie("Breakfast Club",
                    6300,
                    5,
                    "Detention!",
                    "https://cauchonphotoclass.edublogs.org/files/2013/06/the-breakfast-club-movie-poster-1985-1020468204-tfrwg0.jpg",
                    "https://www.youtube.com/watch?v=n7wIEC4glrk")

movies = [toy_story, dDarko, bClub]
#fresh_tomatoes.open_movies_page(movies)
toy_story.print_duration()
toy_story.convert_duration()
toy_story.print_duration()
