from dataclasses import dataclass
from typing import NamedTuple, TypedDict

from pydantic import BaseModel  # Must be correct


class UserTypedDict(TypedDict):
    id: int
    name: str
    email: str
    age: int

class UserNamedTuple(NamedTuple):
    id: int
    name: str
    email: str
    age: int

@dataclass
class UserDataClass:
    id: int
    name: str
    email: str
    age: int

class UserPydantic(BaseModel):
    id: int
    name: str
    email: str
    age: int
