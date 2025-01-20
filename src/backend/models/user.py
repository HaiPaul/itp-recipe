from datetime import datetime

from sqlalchemy import Column, VARCHAR, DATE, DateTime, INTEGER

from database.config import Base


# Create User class
class UserModels(Base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True)
    username = Column(VARCHAR, unique=True)
    password = Column(VARCHAR)
    create_time = Column(DateTime, default=datetime.utcnow())
    last_login = Column(DateTime, default=datetime.utcnow())

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f"<UserModels(username={self.username}, password={self.password})>"
