📝 Todo API

A simple REST API built with FastAPI as part of my backend development learning journey.

🚀 Features

Create, read, update, and delete todos

Path parameters

Request body handling

Automatic API documentation with Swagger

In-memory data storage

🛠️ Tech Stack

Python

FastAPI

Uvicorn

▶️ Run Locally

Create and activate a virtual environment:

python -m venv .venv

.venv\Scripts\Activate.ps1


Install dependencies:

pip install fastapi uvicorn


Start the server:

uvicorn main:app --reload


API:

http://127.0.0.1:8000


Interactive API documentation:

http://127.0.0.1:8000/docs

📌 API Endpoints
Method	Endpoint	Description
GET	/	API status
GET	/todos	Get all todos
GET	/todos/{id}	Get a todo
POST	/todos	Create a todo
PUT	/todos/{id}	Update a todo
DELETE	/todos/{id}	Delete a todo
📚 About

This is a beginner FastAPI project focused on understanding REST APIs, CRUD operations, routing, path parameters, and how FastAPI connects HTTP requests to Python functions.

More advanced features such as databases, authentication, testing, and deployment will be explored in future projects.