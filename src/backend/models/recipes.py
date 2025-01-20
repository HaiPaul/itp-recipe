from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.config import Base

# Association table for many-to-many relationship between Recipe and Ingredient
recipe_ingredient_association = Table(
    'recipe_ingredient', Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id', ondelete="CASCADE")),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id', ondelete="CASCADE"))
)

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    instructions = Column(Text)
    ingredients = relationship("Ingredient", secondary=recipe_ingredient_association, back_populates="recipes")
    created_by = Column(Integer, ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"<Recipe(title={self.title}, description={self.description}, instructions={self.instructions}, created_by={self.created_by})>"

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(String)
    recipes = relationship("Recipe", secondary=recipe_ingredient_association, back_populates="ingredients")

    def __repr__(self) -> str:
        return f"<Ingredient(name={self.name}, quantity={self.quantity})>"