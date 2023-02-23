from services import Services
from fastapi import APIRouter


class Team:
    __router = None

    def __init__(self):
        self.__services = Services()

    @property
    def router(self):
        if self.__router is None:
            self.__router = self.__get_routes()
        return self.__router

    def __get_routes(self):
        routes = APIRouter(prefix="/teams", tags=["Team"])

        # Teams
        @routes.get("")
        def teams():
            return self.__services.team.demo()

        # Teams
        @routes.post("")
        def teams():
            return self.__services.team.demo()

        # Event detail GET
        @routes.get("/{teamId}")
        def teams(teamId: int):
            return self.__services.team.demo()

        # Event detail PATCH
        @routes.patch("/{teamId}")
        def teams(teamId: int):
            return self.__services.team.demo()

        return routes
