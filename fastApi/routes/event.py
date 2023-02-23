from services import Services
from fastapi import APIRouter


class Event:
    __router = None

    def __init__(self):
        self.__services = Services()

    @property
    def router(self):
        if self.__router is None:
            self.__router = self.__get_routes()
        return self.__router

    def __get_routes(self):
        routes = APIRouter(prefix="/events", tags=["Event"])

        # Events
        @routes.get("")
        def events():
            return self.__services.event.demo()

        # Events
        @routes.post("")
        def events():
            return self.__services.event.demo()

        # Event detail GET
        @routes.get("/{eventId}")
        def events(eventId: int):
            return self.__services.event.demo()

        # Event detail PATCH
        @routes.patch("/{eventId}")
        def events(eventId: int):
            return self.__services.event.demo()

        return routes
