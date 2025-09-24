# week8_db

# Products & Orders FastAPI CRUD App

This project is a FastAPI application that implements full CRUD (Create, Read, Update, Delete) operations for two entities: **Products** and **Orders**. It uses SQLAlchemy for ORM and SQLite as the database backend.

## Features
- CRUD endpoints for Products
- CRUD endpoints for Orders
- Relational mapping between Products and Orders
- Pydantic schemas for data validation

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation
1. Clone this repository or copy the project files to your local machine.
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

### Running the App
Start the FastAPI server with Uvicorn:
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### API Documentation
Interactive docs are available at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure
- `main.py` - FastAPI app and API endpoints
- `crud.py` - CRUD logic for Products and Orders
- `models.py` - SQLAlchemy models
- `schemas.py` - Pydantic schemas
- `database.py` - Database connection and session

## Example Endpoints
- `POST /products/` - Create a product
- `GET /products/` - List products
- `POST /orders/` - Create an order
- `GET /orders/` - List orders

