import media
import fresh_tomatoes


# define the instances of class "movie"
clue = media.Movie("Clue",
                   "https://dfep0xlbws1ys.cloudfront.net/thumbs1b/37/1b3768db2a5ca1b5c652e934cab43a28.jpg?response-cache-control=max-age=2628000",  # NOQA
                   "https://www.youtube.com/watch?v=nkwqw4lPz64")

wet_hot = media.Movie("Wet Hot American Summer",
                     "https://upload.wikimedia.org/wikipedia/en/5/59/Wet_hot_american_summer.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=tIvN94hkB1A")

rocky_horror = media.Movie("Rocky Horror Picture Show",
                          "https://upload.wikimedia.org/wikipedia/en/c/c2/Original_Rocky_Horror_Picture_Show_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=Pgx1QZFNMz8",)

prisoner = media.Movie("Harry Potter and the Prisoner of Azkaban",
                       "https://upload.wikimedia.org/wikipedia/en/b/bc/Prisoner_of_azkaban_UK_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=lAxgztbYDbs")

room = media.Movie("The Room",
                   "https://upload.wikimedia.org/wikipedia/en/e/e1/TheRoomMovie.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=tfMTHIwTUXA")

angry_men = media.Movie("12 Angry Men",
                       "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",  # NOQA
                       "https://youtu.be/EqDd06GW76o?list=PLZbXA4lyCtqoKE2fbNgzoaRkpMSHnzE60")  # NOQA

# choose which instances will be displayed in variable "movies"
movies = [clue, wet_hot, rocky_horror, prisoner, room, angry_men]

# run function open_movies_page from the fresh_tomatoes file
# using the instances chosen above
fresh_tomatoes.open_movies_page(movies)
