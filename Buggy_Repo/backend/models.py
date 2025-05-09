from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str

class User(BaseModel):
    username: str
    bio: str