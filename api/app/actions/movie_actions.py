from random import randint

from ..schemas.movie import Movie

movies = [Movie(1, "Toy Story (1995)", "Adventure|Animation|Children|Comedy|Fantasy")]
# TODO: request movies from logstash


class MovieActions:
    def get_random(self) -> Movie:
        return Movie(**movies[randint(0, (len(movies)) - 1)])


movie = MovieActions()
