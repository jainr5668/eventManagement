import uuid
from utills.common import Common
from models.authentication import userLogin

model = {
    "email" : "ronak.jain@mail.com",
    "password": '12345678'
}
class Authentication:
    def __init__(self, common: Common):
        self.__common = common
    
    def signup(self,data: userLogin):
        print(self.__common.database)
        if data.email == model['email'] and data.password == model['password']:
            return {"token": uuid.uuid1()}
        return [data.email, data.password,self.__common.database]

    def login(self,data: userLogin):
        if data.email == model['email'] and data.password == model['password']:
            return {"token": uuid.uuid1()}
        return [data.email, data.password]

    def logout(self,data: userLogin):
        if data.email == model['email'] and data.password == model['password']:
            return {"token": uuid.uuid1()}
        return [data.email, data.password]
