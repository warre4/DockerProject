from fastapi import APIRouter, Depends, HTTPException
from .. import actions
from ..schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get("/", response_model=Movie, tags=["movie"])
def get_movie() -> Movie:
    return actions.movie.get_random()
