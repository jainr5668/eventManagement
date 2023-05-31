from models.system import SystemModel
from services import Services
from fastapi import APIRouter


class System:
    __router = None

    def __init__(self):
        self.__services = Services()

    @property
    def router(self):
        if self.__router is None:
            self.__router = self.__get_routes()
        return self.__router

    def __get_routes(self):
        routes = APIRouter(prefix="/system", tags=["System"])

        @routes.get("")
        def systemDetails() -> SystemModel:
            return SystemModel(name='EventManager')
        return routes
