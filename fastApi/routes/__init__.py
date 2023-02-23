from .game import Game
from .event import Event
from .match import Match
from .authentication import Authentication

from fastapi import APIRouter


class Routes:
    __router = None
    def __init__(self) -> None:
        self.__routers = {
            "/ews/v1": [Event, Game, Match],
            "/auth/v1": [Authentication]
        }

    @property
    def router(self):
        if self.__router is None:
            self.__router = APIRouter()
            self.__get_router()
        return self.__router

    def __get_router(self):
        for key in self.__routers.keys():
            routes = APIRouter(prefix=key)
            for __router in self.__routers[key]:
                service_obj = __router()
                routes.include_router(service_obj.router)
            self.__router.include_router(routes)
    