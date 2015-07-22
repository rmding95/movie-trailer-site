import media
import fresh_tomatoes

# The Good, the Bad and the Ugly
the_gbu = media.Movie("The Good, the Bad and the Ugly (1966)",
                      "A bounty hunting scam joins two men in an uneasy \
                       alliance against a third in a race to find a fortune in \
                       gold buried in a remote cemetery",
                      "http://ia.media-imdb.com/images/M/MV5BOTQ5NDI3MTI4MF5BMl5BanBnXkFtZTgwNDQ4ODE5MDE@._V1_SX640_SY720_.jpg", # noqa
                      "https://www.youtube.com/watch?v=WCN5JJY_wiA",
                      "Directed by: Sergio Leone")

interstellar = media.Movie("Interstellar (2014)",
                           "A team of explorers travel through a wormhole in \
                            space in an attempt to ensure humanity's survival",
                           "http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar2.jpg", #noqa
                           "https://www.youtube.com/watch?v=2LqzF5WauAw",
                           "Directed by: Christopher Nolan")

spirited_away = media.Movie("Spirited Away (2001)",
                            "During her family's move to the suburbs, a sullen \
                             10-year-old girl wanders into a world ruled by \
                             gods, witches, and spirits, and where humans are \
                             changed into beasts",
                            "http://www.nausicaa.net/miyazaki/sen/poster_images/USA_full.jpg", # noqa
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk",
                            "Directed by: Hayao Miyazaki")

mad_max = media.Movie("Mad Max: Fury Road (2015)",
                      "In a stark desert landscape where humanity is broken, \
                       two rebels just might be able to restore order: Max, a \
                       man of action and of few words, and Furiosa, a woman of \
                       action who is looking to make it back to her childhood \
                       homeland",
                      "http://ia.media-imdb.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_SX640_SY720_.jpg", # noqa
                      "https://www.youtube.com/watch?v=SIpVReh6tvE",
                      "Directed by: George Miller")

blade_runner = media.Movie("Blade Runner (1982)",
                           "A blade runner must pursue and try to terminate \
                            four replicants who stole a ship in space and have \
                            returned to Earth to find their creator",
                           "https://bookpeopleblog.files.wordpress.com/2013/06/blade-runner-poster.jpg", # noqa
                           "https://www.youtube.com/watch?v=eogpIG53Cis",
                           "Directed by: Ridley Scott")

commando = media.Movie("Commando (1985)",
                       "A retired elite Black Ops Commando launches a one man \
                        war against a group of South American criminals who \
                        have kidnapped his daughter to blackmail him into \
                        starting a revolution and getting an exiled dictator \
                        back into power",
                       "https://d12vb6dvkz909q.cloudfront.net/uploads/galleries/3446/ap_commando_poster.jpg", # noqa
                       "https://www.youtube.com/watch?v=pPhISgw3I2w",
                       "Directed by: Mark L. Lester")

# A list to store the movies in
movies = [interstellar, spirited_away, mad_max, blade_runner, commando, the_gbu]
# Passing the list of movies to fresh_tomatoes.py to create the webpage
fresh_tomatoes.open_movies_page(movies)
