class Video(object):
    # Parent class for both movies and tv-shows

    """This class is a parent class to Movie and TvShow.
    Use media.Movie() or media.TvShow() instead
    """

    def __init__(self, title, storyline, poster, trailer, duration, rating):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer
        self.duration = duration
        self.rating = rating


class Movie(Video):
    # The class to create a movie

    """media.Movie(title, storyline, poster, trailer, duration, rating)
    title = Title of the Movie
    storyline = Storyline of the movie
    poster = url to the poster of the movie (image file)
    trailer = url to the youtube trailer of the movie
    duration = duration of the movie in hours and minutes
    rating = IMDB rating of the movie
    """

    def __init__(self, title, storyline, poster, trailer, duration, rating):
        super(Movie, self).__init__(
            title, storyline, poster, trailer, duration, rating)


class TvShow(Video):
    # The class to create a tv-show. Added episodes and seasons.

    """media.Movie(
    title, storyline, poster, trailer, duration, rating, episodes, seasons
    )
    title = Title of the tv-show
    storyline = Storyline of the tv-show
    poster = url to the poster of the tv-show (image file)
    trailer = url to the youtube trailer of the tv-show
    duration = duration of the tv-show in hours and minutes
    rating = IMDB rating of the tv-show
    """

    def __init__(
            self, title, storyline, poster, trailer,
            duration, rating, episodes, seasons):
        super(TvShow, self).__init__(
            title, storyline, poster, trailer, duration, rating)
        self.episodes = episodes
        self.seasons = seasons
