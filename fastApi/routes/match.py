from services import Services
from fastapi import APIRouter



class Match:
    __router = None
    def __init__(self):
        self.__services = Services()
    
    @property
    def router(self):
        if self.__router is None:
            self.__router = self.__get_routes()
        return self.__router
            
    def __get_routes(self):
        routes = APIRouter(prefix="/matches", tags=["Match"])
        
        # Matches
        @routes.get('')
        def matches():
            return {"api":"matches"}
        
        # Matches
        @routes.post('')
        def matches():
            return {"api":"matches","method":"POST"}
        
        # Event detail GET
        @routes.get('/{matchId}')
        def matches(matchId:int):
            return {"api":"matches", "matchId":matchId}
        
        # Event detail PATCH
        @routes.patch('/{matchId}')
        def matches(matchId:int):
            return {"api":"matches", "matchId":matchId}
        
        return routes