# Bookstore API

Bookstore API developed during the Backend Python course at EBAC using Django REST Framework.

This project provides an API for managing bookstore resources, including products, categories, and orders.

## Technologies

- Python 3.10+
- Django 5.2
- Django REST Framework
- PostgreSQL
- Poetry
- Docker & Docker Compose
- Gunicorn
- WhiteNoise
- GitHub Actions
- Render (Deployment)

## Prerequisites

Before running this project, make sure you have installed:


Python 3.10+
Poetry
Docker
Docker Compose


## Quickstart

### 1. Clone this project

```shell
git clone https://github.com/lucas-mcd/bookstore.git
2. Access the project folder
cd bookstore
3. Install dependencies
poetry install
4. Apply database migrations
poetry run python manage.py migrate
5. Run local development server
poetry run python manage.py runserver

The application will be available at:

http://127.0.0.1:8000/
Running with Docker

Build and start the containers:

docker-compose up -d --build

Run migrations inside the container:

docker-compose exec web python manage.py migrate
Running Tests

Run tests locally:

poetry run pytest

Or inside Docker:

docker-compose exec web pytest
Deployment

The application is configured for continuous deployment using Render.

Every update merged into the main branch triggers a new deployment automatically.

Static files are handled using WhiteNoise and collected during the build process.

Continuous Integration

This project uses GitHub Actions to validate changes before deployment.

The workflow automatically:

Installs project dependencies
Checks Django configuration
Runs automated tests