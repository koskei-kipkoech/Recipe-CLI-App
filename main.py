import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Recipe, Ingredient, Category
import random

DATABASE_URL = 'sqlite:///recipes.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    #initialize the database incase its not there already
    Base.metadata.create_all(engine)
    print("Database Initialized")

#Add category
def add_category():
    name = input("Enter category name: ").strip()
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category Name: '{name}' added successfully.")

#View category 
def view_category():
    categories = session.query(Category).all()
    if not categories:
        print("No categories found.")
    else:
        for category in categories:
            print(f"Category ID: {category.id} and Name: '{category.name}' ")

#update categories
def update_category():
    view_category()
    category_id = int(input("Enter category ID to update: "))

    #check if category exists 
    category = session.query(Category).filter_by(id=category_id).first()
    if not category:
        print("Invalid category ID.")
    else:
        new_name = input(f'Enter New Name for the category "{category.name}": ').strip()
        category.name = new_name
        session.commit()
        print(f"Category ID: {category_id} updated successfully.")

#Add recipe
def add_recipe():
    name = input("Name of recipe: ").strip()
    description = input("Description of recipe (optional): ").strip()
    view_category()
    category_id = int(input("Enter category id: "))

    #check if category exists 
    category = session.query(Category).filter_by(id=category_id).first()
    if not category:
        print("Invalid category ID.")
        return

    recipe = Recipe(name=name, description=description, category=category)
    session.add(recipe)
    session.commit()
    print(f"Recipe Name: '{name}' added successfully.")

# view recipe 
def view_recipe():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
    else:
        for recipe in recipes:
            print(f"Recipe ID: {recipe.id}  Name: '{recipe.name}' Description: '{recipe.description}'  || CategoryID: {recipe.category_id}")

#update recipe
def update_recipe():
    view_recipe()
    recipe_id = int(input("Enter recipe ID to update: "))

    #check if recipe exists 
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe:
        print("Invalid recipe ID.")
        return

    new_name = input("Enter New Name: ").strip()
    new_description = input("Enter New Description: ").strip()
    view_category()
    new_category_id = int(input("Enter new category ID: "))

    recipe.name = new_name
    recipe.description = new_description
    recipe.category_id = new_category_id
    session.commit()
    print(f"Recipe ID: {recipe_id} updated successfully.")

# delete recipe
def delete_recipe():
    view_recipe()
    recipe_id = int(input("Enter recipe ID to delete: "))

    #check if recipe exists 
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe:
        print("Invalid recipe ID.")
        return

    session.delete(recipe)
    session.commit()
    print(f"Recipe ID ' {recipe_id} ' deleted successfully.")

def add_ingredient():
    view_recipe()
    recipe_id = int(input("Enter recipe ID to add ingredient: "))

    #check if recipe exists 
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe:
        print("Invalid recipe ID.")
        return

    name = input("Ingredient name: ").strip()
    quantity = float(input("Ingredient quantity: "))
    unit = input("Ingredient unit of measurment: ").strip()

    ingredient = Ingredient(name=name, quantity=quantity, unit=unit, recipe=recipe)
    session.add(ingredient)
    session.commit()
    print(f"Ingredient Name: '{name}' added successfully to recipe ID: {recipe_id} .")

def view_ingredients():
    ingredients = session.query(Ingredient).all()
    if not ingredients:
        print("No ingredients found.")
    else:
        for ingredient in ingredients:
            print(f"Ingredient ID: {ingredient.id}  Name: '{ingredient.name}'  Quantity/Unit: '{ingredient.quantity}{ingredient.unit}'   RecipeID: {ingredient.recipe_id}")

def update_ingredients():
    view_ingredients()
    ingredient_id = int(input("Enter ingredient ID to update: "))

    #check if ingredient exists 
    ingredient = session.query(Ingredient).filter_by(id=ingredient_id).first()
    if not ingredient:
        print("Invalid ingredient ID.")
        return

    new_name = input("Enter New Name: ").strip()
    new_quantity = float(input("Enter New Quantity: "))
    new_unit = input("Enter New Unit: ").strip()

    ingredient.name = new_name
    ingredient.quantity = new_quantity
    ingredient.unit = new_unit
    session.commit()
    print(f"Ingredient ID: {ingredient_id} updated successfully.")


def delete_ingredients():
    view_ingredients()
    ingredient_id = int(input("Enter ingredient ID to delete: "))

    #check if ingredient exists 
    ingredient = session.query(Ingredient).filter_by(id=ingredient_id).first()
    if not ingredient:
        print("Invalid ingredient ID.")
        return

    session.delete(ingredient)
    session.commit()
    print(f"Ingredient ID: '{ingredient_id}' deleted successfully.")

def get_recipes_by_category():
    view_category()
    category_id = int(input("Enter category ID to view recipes: "))

    #check if category exists 
    category = session.query(Category).filter_by(id=category_id).first()
    if not category:
        print("Invalid category ID.")
        return

    recipes = session.query(Recipe).filter_by(category=category).all()
    if not recipes:
        print("No recipes found in this category.")
    else:
        print(f'Recipes Found for category  "{category.name}" ')
        for recipe in recipes:
            print(f"Recipe ID: {recipe.id}  Name: '{recipe.name}' Description: '{recipe.description}'  || CategoryID: {recipe.category_id}")

def get_ingredients_by_recipe():
    view_recipe()
    recipe_id = int(input("Enter recipe ID to view ingredients: "))

    #check if recipe exists 
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe:
        print("Invalid recipe ID.")
        return

    ingredients = session.query(Ingredient).filter_by(recipe=recipe).all()
    if not ingredients:
        print("No ingredients found for this recipe.")
    else:
        print(f'Ingredients Found for recipe  "{recipe.name}" ')
        for ingredient in ingredients:
            print(f"Ingredient ID: {ingredient.id}  Name: '{ingredient.name}'  Quantity/Unit: '{ingredient.quantity}{ingredient.unit}'")

def search_recipe():
    print("Search by:")
    print("1. Recipe Name")
    print("2. Category Name")
    print("3. Ingredient Name")
    search_choice = input("Enter your choice (1/2/3): ")

    if search_choice == "1":
        # Search by recipe name
        recipe_name = input("Enter recipe name to search: ").strip()
        recipes = session.query(Recipe).filter(Recipe.name.ilike(f"%{recipe_name}%")).all()

        if not recipes:
            print(f"No recipes found with the name '{recipe_name}'.")
        else:
            for recipe in recipes:
                print(f"\nRecipe Name: {recipe.name}")
                print(f"Category: {recipe.category.name}")
                print("Ingredients:")
                for ingredient in recipe.ingredients:
                    print(f" -> {ingredient.name} ({ingredient.quantity} {ingredient.unit})")
    
    elif search_choice == "2":
        # Search by category name
        category_name = input("Enter category name to search: ").strip()
        category = session.query(Category).filter(Category.name.ilike(f"%{category_name}%")).first()

        if not category:
            print(f"No category found with the name '{category_name}'.")
        else:
            print(f"\nCategory: {category.name}")
            print("Recipes:")
            for recipe in category.recipes:
                print(f" - {recipe.name}")
                print(" Ingredients:")
                for ingredient in recipe.ingredients:
                    print(f"   -> {ingredient.name} ({ingredient.quantity} {ingredient.unit})")
    
    elif search_choice == "3":
        # Search by ingredient name
        ingredient_name = input("Enter ingredient name to search: ").strip()
        ingredients = session.query(Ingredient).filter(Ingredient.name.ilike(f"%{ingredient_name}%")).all()

        if not ingredients:
            print(f"No ingredients found with the name '{ingredient_name}'.")
        else:
            for ingredient in ingredients:
                recipe = ingredient.recipe
                print(f"\nRecipe Name: {recipe.name}")
                print(f"Category: {recipe.category.name}")
                print(f"Ingredient: {ingredient.name} ({ingredient.quantity} {ingredient.unit})")
    
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")

def random_recipe_suggestion(session):
    recipes = session.query(Recipe).all()
    if recipes:
        recipe = random.choice(recipes)
        print(f"Today's Random Suggestion:")
        print(f"Recipe: {recipe.name}")
        print(f"Description: {recipe.description}")
        print(f"Category: {recipe.category.name}")
        print("Ingredients:")
        for ingredient in recipe.ingredients:
            print(f"- {ingredient.name} ({ingredient.quantity} {ingredient.unit})")
    else:
        print("No recipes available.")

def statistics_dashboard(session):
    total_categories = session.query(Category).count()
    total_recipes = session.query(Recipe).count()
    total_ingredients = session.query(Ingredient).count()

    print("Statistics Dashboard:")
    print(f"- Total Categories: {total_categories}")
    print(f"- Total Recipes: {total_recipes}")
    print(f"- Total Ingredients: {total_ingredients}")

def delete_category_with_recipes(session):
    view_category()
    category_name = input("Enter the category name: ")
    category = session.query(Category).filter_by(name=category_name).first()

    if category:
        confirmation = input(f"Are you sure you want to delete '{category.name}' and all associated recipes? (yes/no): ")
        if confirmation.lower() == 'yes':
            session.delete(category)
            session.commit()
            print(f"Category '{category.name}' and its recipes were deleted successfully.")
        else:
            print("Operation canceled.")
    else:
        print(f"Category '{category_name}' not found.")

def main_menu():
    while True:
        print("\n========  RECIPE   APPLICSTION   CLI  ==========")
        print("1. Add Category")
        print("2. View Categories")
        print("3. Add Recipe")
        print("4. View Recipes")
        print("5. Update Recipe")
        print("6. Delete Recipe")
        print("7. Add Ingredient")
        print("8. View Ingredients")
        print("9. Update Categories")
        print("10. Update Ingreients")
        print("11. Delete Ingredients")
        print("12. Get Recipes with the Same Category")
        print("13. Get Ingredients for a specific Recipe")
        print("14. Search Recipe by Name, Category, and Recipe")
        print("15. Random Recipe Suggestion")
        print("16. Delete category and Recipe")
        print("17. View Statistics Dashboard")
        print("18. Exit ")
        print("\n==============================================")
        choice = input("Enter your Choice: ")
        if choice == "1":
            add_category()
        elif choice == "2":
            view_category()
        elif choice == "3":
            add_recipe()
        elif choice == "4":
            view_recipe()
        elif choice == "5":
            update_recipe()
        elif choice == "6":
            delete_recipe()
        elif choice == "7":
            add_ingredient()
        elif choice == "8":
            view_ingredients()
        elif choice == "9":
            update_category()
        elif choice == "10":
            update_ingredients()
        elif choice == "11":
            delete_ingredients()
        elif choice == "12":
            get_recipes_by_category()
        elif choice == "13":
            get_ingredients_by_recipe()
        elif choice == "14":
            search_recipe()
        elif choice == "15":
            random_recipe_suggestion(session)
        elif choice == "16":
            delete_category_with_recipes(session)
        elif choice == "17":
            statistics_dashboard(session)
        elif choice == "18":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid Choice! Please try again.")



if __name__ == "__main__":
    init_db()
    main_menu()



