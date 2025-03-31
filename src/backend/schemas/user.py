from datetime import date

from typing import Optional

from pydantic import BaseModel

# User Schema


class Base(BaseModel):
    username: str


class Register(Base):
    password: str


class Password(BaseModel):
    password: str

class UserID(Base):
    id: int

class User(Base):
    id: int
    create_time: Optional[date]
    last_login: Optional[date]

    class Config:
        orm_mode = True