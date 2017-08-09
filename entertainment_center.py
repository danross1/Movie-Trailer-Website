import media
import fresh_tomatoes

# define the instances of class "movie"
clue = media.Movie("Clue",
                   "Six guests are invited to a strange house and must cooperate with the staff to solve a murder mystery",
                   "https://dfep0xlbws1ys.cloudfront.net/thumbs1b/37/1b3768db2a5ca1b5c652e934cab43a28.jpg?response-cache-control=max-age=2628000",
                   "https://www.youtube.com/watch?v=nkwqw4lPz64")

wet_hot = media.Movie("Wet Hot American Summer",
                     "Set on the last day of camp, in the hot summer of 1981, a group of counselors try to complete their unfinished business before the day ends",
                     "https://upload.wikimedia.org/wikipedia/en/5/59/Wet_hot_american_summer.jpg",
                     "https://www.youtube.com/watch?v=tIvN94hkB1A")

rocky_horror = media.Movie("Rocky Horror Picture Show",
                          "A newly engaged couple have a breakdown in an isolated area and must pay a call to the bizarre residence of Dr. Frank-N-Furter", 
                          "https://upload.wikimedia.org/wikipedia/en/c/c2/Original_Rocky_Horror_Picture_Show_poster.jpg",
                          "https://www.youtube.com/watch?v=Pgx1QZFNMz8",)

prisoner = media.Movie("Harry Potter and the Prisoner of Azkaban",
                       "It's Harry's third year at Hogwarts; not only does he have a new Defense Against the Dark Arts teacher, but there is also trouble brewing. Convicted murderer Sirius Black has escaped the Wizards' Prison and is coming after Harry",
                       "https://upload.wikimedia.org/wikipedia/en/b/bc/Prisoner_of_azkaban_UK_poster.jpg",
                       "https://www.youtube.com/watch?v=lAxgztbYDbs")

room = media.Movie("The Room",
                   "Johnny is a successful banker who lives happily in a San Francisco townhouse with his fiance, Lisa. One day, inexplicably, she gets bored with him and decides to seduce his best friend, Mark. From there, nothing will be the same again",
                   "https://upload.wikimedia.org/wikipedia/en/e/e1/TheRoomMovie.jpg",
                   "https://www.youtube.com/watch?v=tfMTHIwTUXA")

angry_men = media.Movie("12 Angry Men",
                       "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence",
                       "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",
                       "https://youtu.be/EqDd06GW76o?list=PLZbXA4lyCtqoKE2fbNgzoaRkpMSHnzE60")

# choose which instances will be displayed in variable "movies"
movies = [clue, wet_hot, rocky_horror, prisoner, room, angry_men]

# run function open_movies_page from the fresh_tomatoes file
# using the instances chosen above
fresh_tomatoes.open_movies_page(movies)
