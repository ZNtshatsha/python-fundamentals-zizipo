<<<<<<< HEAD
from typing import TypedDict, NamedTuple
from dataclasses import dataclass
from pydantic import BaseModel

=======
from dataclasses import dataclass
from typing import NamedTuple, TypedDict

from pydantic import BaseModel


>>>>>>> bfa5463 (Added new assignment files and updates)
# TypedDict
class UserTypedDict(TypedDict):
    id: int
    name: str
    email: str
    age: int

# NamedTuple
class UserNamedTuple(NamedTuple):
    id: int
    name: str
    email: str
    age: int

# Dataclass
@dataclass
class UserDataClass:
    id: int
    name: str
    email: str
    age: int

# Pydantic Model
class UserPydantic(BaseModel):
    id: int
    name: str
    email: str
    age: int
