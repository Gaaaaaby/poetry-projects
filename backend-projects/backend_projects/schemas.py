
from datetime import date
from typing import List, Union
from pydantic import BaseModel

class ITeam(BaseModel):
    name:str
    members: int
    date_created: Union[str,date]
    status: str
    list_tasks: List[str]

class IUser(BaseModel):
    id: int
    name:str
    lastname: str
    age: int
    email: str
    address: str 
    number: int 
    status: str
    position: str