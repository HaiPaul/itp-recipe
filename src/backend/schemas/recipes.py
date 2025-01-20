from pydantic import BaseModel
from typing import List, Optional

class IngredientBase(BaseModel):
    name: str
    quantity: str

class IngredientCreate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: int

    class Config:
        orm_mode: True

class RecipeBase(BaseModel):
    title: str
    description: Optional[str] = None
    instructions: Optional[str] = None

class RecipeCreate(RecipeBase):
    ingredients: List[IngredientCreate]

class Recipe(RecipeBase):
    id: int
    ingredients: List[Ingredient]
    created_by: Optional[int] = None

    class Config:
        orm_mode: True