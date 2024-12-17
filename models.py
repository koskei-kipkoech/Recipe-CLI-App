from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    recipes = relationship('Recipe', back_populates='category')

    def __repr__(self):
        return f'Category( id={self.id},  name="{self.name}" )'
class Recipe(Base):
    __tablename__ ='recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Category', back_populates='recipes')
    ingredients = relationship('Ingredient', back_populates='recipes')

    def __repr__(self):
        return f'Recipe( id={self.id},  name="{self.name}",  description="{self.description}",  category_id={self.category_id} )'

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String(10), nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    recipes = relationship('Recipe', back_populates='ingredients')

    def __repr__(self):
        return f'Ingredient( id={self.id},  name="{self.name}",  quantity={self.quantity},  unit="{self.unit}",  recipe_id={self.recipe_id} )'
