from datetime import date

from pydantic import BaseModel

# User Schema


class Base(BaseModel):
    id: int
    username: str


class Register(Base):
    password: str


class Password(BaseModel):
    password: str
