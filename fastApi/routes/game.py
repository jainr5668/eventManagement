from services import Services
from fastapi import APIRouter



class Game:
    __router = None
    def __init__(self):
        self.__services = Services()
    
    @property
    def router(self):
        if self.__router is None:
            self.__router = self.__get_routes()
        return self.__router
            
    def __get_routes(self):
        routes = APIRouter(prefix="/games", tags=["Game"])
        
        # Games
        @routes.get('')
        def games():
            return self.__services.game.demo()
        
        # Games
        @routes.post('')
        def games():
            return self.__services.game.demo()
        
        # Event detail GET
        @routes.get('/{gameId}')
        def games(gameId:int):
            return self.__services.game.demo()
        
        # Event detail PATCH
        @routes.patch('/{gameId}')
        def games(gameId:int):
            return self.__services.game.demo()
        
        return routes