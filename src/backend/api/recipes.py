from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from crud.recipes import RecipeCRUD
from crud.dependencies import get_recipe_crud
import schemas.recipes as recipe_schema

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("", response_model=List[recipe_schema.Recipe])
async def get_recipes(
    db: RecipeCRUD = Depends(get_recipe_crud),
):
    recipes = await db.get_recipes()
    return recipes


@router.post(
    "", response_model=recipe_schema.Recipe, status_code=status.HTTP_201_CREATED
)
async def create_recipe(
    new_recipe: recipe_schema.RecipeCreate,
    db: RecipeCRUD = Depends(get_recipe_crud),
):
    recipe = await db.create_recipe(new_recipe)
    return recipe


@router.get("/{recipe_id}", response_model=recipe_schema.Recipe)
async def get_recipe(
    recipe_id: int,
    db: RecipeCRUD = Depends(get_recipe_crud),
):
    recipe = await db.get_recipe(recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@router.put("/{recipe_id}", response_model=recipe_schema.Recipe)
async def update_recipe(
    recipe_id: int,
    new_recipe: recipe_schema.RecipeCreate,
    db: RecipeCRUD = Depends(get_recipe_crud),
):
    recipe = await db.get_recipe(recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    updated_recipe = await db.update_recipe(recipe_id, new_recipe)
    return updated_recipe


@router.get("/search/{title}", response_model=List[recipe_schema.Recipe])
async def get_recipes_by_title(
    title: str,
    db: RecipeCRUD = Depends(get_recipe_crud),
):
    recipes = await db.get_recipes_by_title(f"%{title}%")
    return recipes


@router.get("/user/{user_id}", response_model=List[recipe_schema.Recipe])
async def get_recipe_by_user_id(
    user_id: str,
    db: RecipeCRUD = Depends(get_recipe_crud),
):
    recipes = await db.get_recipes_by_user_id(user_id)
    return recipes


@router.delete("/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_recipe(
    recipe_id: int,
    db: RecipeCRUD = Depends(get_recipe_crud),
):
    recipe = await db.get_recipe(recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    await db.delete_recipe(recipe_id)
    return
