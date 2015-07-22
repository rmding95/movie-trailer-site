# The movie class stores the title, storyline, poster, trailer and director
# of a movie
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        
