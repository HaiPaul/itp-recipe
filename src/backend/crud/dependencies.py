from typing import Generator

from database.config import async_session
from crud.user import UserCRUD
from crud.recipes import RecipeCRUD

async def get_db() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield session


async def get_user_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield UserCRUD(session)

async def get_recipe_crud() -> Generator:
    async with async_session() as session:
        async with session.begin():
            yield RecipeCRUD(session)
