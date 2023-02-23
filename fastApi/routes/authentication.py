from services import Services
from fastapi import APIRouter
from models.authentication import userLogin



class Authentication:
    __router = None
    def __init__(self):
        self.__services = Services()
    
    @property
    def router(self):
        if self.__router is None:
            self.__router = self.__get_routes()
        return self.__router
            
    def __get_routes(self):
        routes = APIRouter(prefix="/auth", tags=["Authentication"])
        
        # signup Rout
        @routes.post("/signup/")
        async def signup(userData: userLogin):
            return self.__services.authentication.signup(userData)
        
        # Login Route
        @routes.post("/login/")
        async def login(userData: userLogin):
            return self.__services.authentication.login(userData)
        
        # Logout Route
        @routes.post("/logout/")
        async def logout(userData: userLogin):
            return self.__services.authentication.logout(userData)

        return routes