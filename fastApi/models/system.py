from pydantic import BaseModel


class SystemModel(BaseModel):
    name: str
