from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from models.recipes import Ingredient, Recipe
import schemas.recipes as ingredient_schema

class ingredientCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session

    async def get_ingredient_by_title(self, title: str):
        stmt = select(Ingredient).where(Ingredient.title == title)
        result = await self.db_session.execute(stmt)
        ingredient = result.scalars().first()
        return ingredient

    async def get_ingredients(self) -> List[ingredient_schema.ingredientBase]:
        stmt = select(Ingredient)
        result = await self.db_session.execute(stmt)
        ingredients = result.scalars().all()
        return ingredients

    async def create_ingredient(self, ingredient: ingredient_schema.IngredientCreate) -> ingredient_schema.ingredientBase:
        db_ingredient = Ingredient(
            name=ingredient.name,
            quantity=ingredient.quantity,
            recipes=[
                Recipe(title=recipe.title, description=recipe.description, instructions=recipe.instructions)
                for recipe in ingredient.recipes
            ]
        )
        self.db_session.add(db_ingredient)
        await self.db_session.commit()
        return db_ingredient

    async def update_quantity(self, name: str, quantity: str):
        stmt = (
            update(Ingredient)
            .where(Ingredient.name == name)
            .values(quantity=quantity)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_ingredient(self, name: str):
        stmt = delete(Ingredient).where(Ingredient.name == name)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)