## Recipe Management CLI Application

A Command-Line Interface (CLI) application for managing recipes, categories, and ingredients. This project uses Python and SQLAlchemy to perform CRUD operations on a SQLite database and also alembic for migrations, along with **click** for user interaction.

## Features

- **Category Management**:

  - Add, view, and update categories.
  - Delete categories along with their associated recipes.

- **Recipe Management**:

  - Add, view, update, and delete recipes.
  - Search for recipes by name or category.
  - Get random recipe suggestions.

- **Ingredient Management**:

  - Add, view, update, and delete ingredients.
  - Link ingredients to recipes.
  - View all ingredients associated with a recipe.

- **Statistics Dashboard**:

  - Display insights about the database, such as the number of recipes and categories.

- **Database Initialization**:

  - Setup and initialize the SQLite database schema.

- **User-Friendly CLI**:
  -Interactive CLI commands with **click** to guide you through the operations.

### Prerequisites

- Python 3.8+
- `pipenv` (Python package manager)
- click (for CLI welcome message)

### Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd recipe-management-cli
   ```

2. Install dependencies:

   ```bash
   pipenv install
   ```

3. Initialize the database:
   ```bash
   python main.py
   ```
   Select the option to initialize the database.

## Usage

Run the application:

```bash
python main.py
```

Follow the menu prompts to perform various operations:

- Add categories, recipes, or ingredients.
- View, update, or delete data.
- Search for recipes or get a random suggestion.
- View statistics or recent searches.

## Dependencies

- [SQLAlchemy] - ORM for database interaction.
- [SQLite] - Lightweight database.
- [alembic] - helps in migrations.
- [click] - for CLI interaction.

Install dependencies using:

```bash
pipenv install
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

## Acknowledgements

- Inspired by the need to simplify recipe and ingredient management.
- Built with Python, SQLAlchemyand, Alembic and Click.
