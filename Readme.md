# FastAPI Student CRUD API

A simple FastAPI project demonstrating **CRUD operations with SQLite and SQLAlchemy**.

## Features
- Create student
- Read all students
- Read single student
- Update student
- Delete student
- SQLite database integration
- Auto API docs with Swagger UI

## Project Structure
```text
Fast_API/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── students.db
````

## Installation

```bash
pip install fastapi uvicorn sqlalchemy
```

## Run the Project

```bash
uvicorn main:app --reload
```

## API Documentation

Open in browser:

```text
http://127.0.0.1:8000/docs
```

## Example Request Body

```json
{
  "name": "Mehrab",
  "age": 24,
  "department": "CSE"
}
```

## CRUD Endpoints

* `POST /students/` → Create student
* `GET /students/` → Get all students
* `GET /students/{id}` → Get one student
* `PUT /students/{id}` → Update student
* `DELETE /students/{id}` → Delete student

## Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn
