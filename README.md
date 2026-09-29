⚡ FastAPI Learning Lab

My hands-on journey into backend development, APIs, databases, authentication, deployment, and AI/ML systems using Python and FastAPI.

This repository is my FastAPI learning lab — a place to learn concepts, write experiments, build APIs, document what I learn, and gradually turn those concepts into real-world projects.

The goal is not just to learn FastAPI syntax.

The goal is to understand how backend systems work and eventually use that knowledge to build and serve AI/ML applications.

🎯 Why FastAPI?

My broader goal is to become comfortable working across both AI/ML and backend development.

FastAPI provides a way to connect those two areas:

                    Python
                      │
          ┌───────────┴───────────┐
          │                       │
        AI / ML               Backend
          │                       │
    ML Models / LLMs           FastAPI
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
                Production APIs


Eventually, I want to be able to take a model or AI application and build the backend around it — including APIs, databases, authentication, testing, and deployment.

🧠 What I'm Learning
🌐 Web & API Fundamentals

Before going deep into FastAPI, I'm learning the fundamentals behind APIs:

HTTP

REST

Client / Server architecture

Requests and responses

HTTP methods

Status codes

Headers

Query parameters

Path parameters

JSON

API design

🐍 Python

FastAPI is built around Python, so I'm strengthening the Python concepts needed for backend development:

Functions

Modules and packages

Virtual environments

Type hints

Exception handling

Classes and OOP

Decorators

async / await

Working with JSON

Working with files

Package management

⚡ FastAPI

The main focus of this repository:

FastAPI fundamentals

Routes and endpoints

GET / POST / PUT / PATCH / DELETE

Path parameters

Query parameters

Request bodies

Response models

Pydantic integration

Dependency injection

Error handling

Middleware

Background tasks

Automatic API documentation

📦 Pydantic

Learning how FastAPI validates and structures data:

Base models

Type validation

Required and optional fields

Nested models

Lists and dictionaries

Serialization

Deserialization

Custom validation

Example:

from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str

🧪 Postman

Using Postman to understand and test APIs:

GET requests

POST requests

PUT / PATCH requests

DELETE requests

Request bodies

Query parameters

Path parameters

Headers

Authentication

Status codes

API collections

The idea is to understand what is actually happening when a client communicates with a backend.

🗄️ Databases

The backend isn't complete without understanding data persistence.

I'm learning:

SQL fundamentals

Tables

Rows and columns

Primary keys

Foreign keys

Relationships

CRUD operations

SQLite

PostgreSQL

SQLAlchemy

Database migrations

🔐 Authentication & Security

As the projects become more advanced, I'll work with:

User registration

Login

Password hashing

JWT

Access tokens

Authentication

Authorization

Roles and permissions

Environment variables

API security fundamentals

🧪 Testing

Learning how to make APIs reliable:

Pytest

Unit testing

API testing

FastAPI TestClient

Testing endpoints

Testing authentication

Testing database operations

Handling edge cases

🐳 Deployment & Production

Eventually moving from:

"It works on my computer."


to:

"It is actually deployed."


Topics include:

Environment variables

Docker

Docker Compose

Production configuration

CI/CD fundamentals

Cloud deployment

API monitoring fundamentals

🤖 AI / ML + FastAPI

One of the main reasons I'm learning FastAPI is to connect backend development with my AI/ML work.

The long-term goal:

        Client / Frontend
                │
                ▼
             FastAPI
                │
        ┌───────┴────────┐
        │                │
    Database         AI / ML Model
        │                │
        └───────┬────────┘
                │
                ▼
           JSON Response


Possible future applications:

Machine learning prediction APIs

Deep learning APIs

NLP APIs

Recommendation systems

LLM applications

RAG applications

AI-powered services

📂 Repository Structure

The repository is divided into two main parts:

fastapi-learning/
│
├── README.md
│
├── 01-http-rest/
│   ├── README.md
│   └── examples/
│
├── 02-json/
│   ├── README.md
│   └── examples/
│
├── 03-pydantic/
│   ├── README.md
│   └── examples/
│
├── 04-fastapi-basics/
│   ├── README.md
│   └── examples/
│
├── 05-postman/
│   ├── README.md
│   └── collections/
│
├── 06-databases/
│   ├── README.md
│   └── examples/
│
├── 07-sqlalchemy/
│   ├── README.md
│   └── examples/
│
├── 08-authentication/
│   ├── README.md
│   └── examples/
│
├── 09-testing/
│   ├── README.md
│   └── examples/
│
├── 10-docker/
│   ├── README.md
│   └── examples/
│
└── projects/
    ├── todo-api/
    ├── blog-api/
    ├── expense-tracker-api/
    ├── ecommerce-api/
    └── ai-ml-api/

01–10

These folders contain my learning notes, experiments, examples, and exercises.

projects/

This contains larger applications where multiple concepts are combined into something closer to a real backend system.

🚀 Projects

The concepts learned here will eventually be applied to larger projects.

📝 Todo API

A simple CRUD API to understand the fundamentals.

Topics:

FastAPI

Pydantic

CRUD

HTTP methods

Request / response

Postman

📰 Blog API

A multi-user backend for creating and managing blog posts.

Topics:

FastAPI

PostgreSQL

SQLAlchemy

Authentication

JWT

Users

Posts

Comments

Permissions

💰 Expense Tracker API

A backend for managing personal income and expenses.

Topics:

Authentication

PostgreSQL

CRUD

Categories

Transactions

Filtering

Pagination

Data validation

🛒 E-Commerce API

A larger backend combining multiple systems.

Possible features:

Users

Authentication

Products

Categories

Cart

Orders

Inventory

Permissions

Database relationships

🤖 AI / ML API

A project connecting FastAPI with AI/ML.

Possible applications:

ML prediction API

Image classification API

Recommendation API

NLP API

LLM API

RAG API

🧩 Learning Approach

I'm using this repository as a hands-on laboratory, not just a collection of tutorial code.

The learning cycle:

Learn
  ↓
Understand
  ↓
Code
  ↓
Test
  ↓
Break
  ↓
Debug
  ↓
Improve
  ↓
Build


Whenever possible, concepts will be followed by practical implementations.

🛠️ Technology Stack
Technology	Purpose
Python	Programming language
FastAPI	Backend/API framework
Pydantic	Data validation
Uvicorn	ASGI server
Postman	API testing
SQL	Database language
PostgreSQL	Relational database
SQLAlchemy	ORM
Pytest	Testing
Docker	Containerization
Git	Version control
GitHub	Code hosting & collaboration
📚 Resources
FastAPI

https://fastapi.tiangolo.com/

Python

https://docs.python.org/3/

Pydantic

https://docs.pydantic.dev/

PostgreSQL

https://www.postgresql.org/docs/

SQLAlchemy

https://docs.sqlalchemy.org/

Postman

https://learning.postman.com/

🔗 More of My Work

This repository is part of my broader journey through Python, AI/ML, and software development.

GitHub:

https://github.com/jvedant1001-ship-it


The objective is to become capable of building complete applications, not just individual models or isolated pieces of code.

🚧 Status

This repository is continuously evolving as I learn, experiment, build projects, and improve my understanding of backend development.

Learn the fundamentals. Build the projects. Understand the system.
