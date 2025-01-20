from sqlalchemy import update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from typing import List

from models.recipes import Recipe, Ingredient
from auth.dependencies import protected
import schemas.recipes as recipe_schema
import schemas.user as UserSchema

class RecipeCRUD:
    db_session = None

    def __init__(self, db_session: AsyncSession = None):
        self.db_session = db_session
    
    async def get_recipe(self, recipe_id: int) -> recipe_schema.RecipeBase:
        stmt = select(Recipe).where(Recipe.id == recipe_id).options(joinedload(Recipe.ingredients))
        result = await self.db_session.execute(stmt)
        recipe = result.scalars().unique().first()
        return recipe

    async def get_recipes_by_title(self, title: str) -> List[recipe_schema.Recipe]:
        stmt = select(Recipe).where(Recipe.title.like(title)).options(joinedload(Recipe.ingredients))
        result = await self.db_session.execute(stmt)
        recipes = result.scalars().unique().all()
        return recipes

    async def get_recipes(self) -> List[recipe_schema.Recipe]:
        stmt = select(Recipe).options(joinedload(Recipe.ingredients))
        result = await self.db_session.execute(stmt)
        recipes = result.scalars().unique().all()
        return recipes
    
    async def get_recipes_by_user_id(self, user_id: str) -> List[recipe_schema.RecipeBase]:
        stmt = select(Recipe).where(Recipe.created_by == user_id).options(joinedload(Recipe.ingredients))
        result = await self.db_session.execute(stmt)
        recipes = result.scalars().all()
        return recipes
    
    async def get_recipes_from_current_user(self) -> List[recipe_schema.RecipeBase]:
        current_user: UserSchema.Base = await protected()
        stmt = select(Recipe).where(Recipe.created_by == current_user.id).options(joinedload(Recipe.ingredients))
        result = await self.db_session.execute(stmt)
        recipes = result.scalars().all()
        return recipes

    async def create_recipe(self, recipe: recipe_schema.RecipeCreate) -> recipe_schema.Recipe:
        db_recipe = Recipe(
            title=recipe.title,
            description=recipe.description,
            instructions=recipe.instructions,
            ingredients=[
                Ingredient(name=ingredient.name, quantity=ingredient.quantity)
                for ingredient in recipe.ingredients
            ]
        )
        self.db_session.add(db_recipe)
        await self.db_session.commit()
        return db_recipe

    async def update_recipe(self, recipe_id: int, recipe: recipe_schema.RecipeCreate):
        stmt = (
            update(Recipe)
            .where(Recipe.id == recipe_id)
            .values(
                title=recipe.title,
                description=recipe.description,
                instructions=recipe.instructions
            )
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)
        await self.db_session.commit()

    async def update_description(self, title: str, description: str):
        stmt = (
            update(Recipe)
            .where(Recipe.title.like(title))
            .values(description=description)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def update_instructions(self, title: str, instructions: str):
        stmt = (
            update(Recipe)
            .where(Recipe.title.like(title))
            .values(instructions=instructions)
        )
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)

    async def delete_recipe(self, recipe_id: str):
        stmt = delete(Recipe).where(Recipe.id == recipe_id)
        stmt.execution_options(synchronize_session="fetch")
        await self.db_session.execute(stmt)