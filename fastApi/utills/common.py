from database import Database


class Common:
    __database = None

    @property
    def database(self):
        if self.__database is None:
            self.__database = Database()
        return self.__database
