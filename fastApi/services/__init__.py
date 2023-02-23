from .game import Game
from .event import Event
from .match import Match
from .authentication import Authentication

from utills.common import Common


class Services:
    __authentication = None
    __event = None
    __game = None
    __match = None
    
    def __init__(self):
        self.__common = Common()
    
    
    @property
    def authentication(self):
        if self.__authentication is None:
            self.__authentication = Authentication(self.__common)
        return self.__authentication
    
    @property
    def event(self):
        if self.__event is None:
            self.__event = Event(self.__common)
        return self.__event
    
    @property
    def game(self):
        if self.__game is None:
            self.__game = Game(self.__common)
        return self.__game
    
    @property
    def match(self):
        if self.__match is None:
            self.__match = Match(self.__common)
        return self.__match