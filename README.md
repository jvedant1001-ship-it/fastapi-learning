⚡ FastAPI Learning Lab
🐍 Python • ⚡ FastAPI • 🗄️ Databases • 🔐 Security • 🐳 Deployment • 🤖 AI/ML

A hands-on journey into backend development with Python and FastAPI.

This repository is my personal FastAPI learning laboratory — a place to understand backend concepts, experiment with code, document what I learn, and gradually develop the skills required to build production-ready APIs.

The focus is not just learning syntax.

The goal is to understand how backend systems work and eventually use that knowledge to build and serve AI/ML applications.

🧭 Learning Roadmap
                        🐍 Python
                           │
                           ▼
                    🌐 HTTP & REST
                           │
                           ▼
                         📦 JSON
                           │
                           ▼
                      🧩 Pydantic
                           │
                           ▼
                       ⚡ FastAPI
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        🧪 Testing    🗄️ Database    🔐 Authentication
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                       🐳 Docker
                           │
                           ▼
                    🚀 Deployment
                           │
                           ▼
                     🤖 AI / ML APIs

📑 Contents

🎯 Why FastAPI?

🌐 Web & API Fundamentals

🐍 Python

⚡ FastAPI

🧩 Pydantic

🧪 Postman

🗄️ Databases

🔐 Authentication & Security

🧪 Testing

🐳 Docker & Deployment

🤖 AI/ML + FastAPI

📂 Repository Structure

🛠️ Technology Stack

🧠 Learning Approach

📚 Resources

🧭 Long-Term Direction

🎯 Why FastAPI?

My broader goal is to become comfortable working across both AI/ML and backend development.

FastAPI is an important part of that journey because it allows me to connect models and applications with real backend systems.

                  🤖 AI / ML
                      │
                      │
                      ▼
                ⚡ FastAPI
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      🗄️ Database   🔐 Auth    🧪 Testing
          │           │           │
          └───────────┼───────────┘
                      ▼
                 🌐 API
                      │
                      ▼
               👨‍💻 Application


The long-term goal is to understand not only how to train a model, but also how to serve, secure, test, and deploy it.

🌐 Web & API Fundamentals

Before going deep into FastAPI, I'm learning the fundamentals behind APIs.

Topics

HTTP

REST

Client / Server architecture

Requests and responses

HTTP methods

HTTP status codes

Headers

Query parameters

Path parameters

JSON

API design

The basic idea
Client
  │
  │ HTTP Request
  ▼
Backend / API
  │
  │ HTTP Response
  ▼
Client

🐍 Python

FastAPI is built around Python, so I'm strengthening the Python concepts required for backend development.

Topics

Functions

Modules and packages

Virtual environments

Type hints

Exception handling

Classes and OOP

Decorators

async / await

JSON handling

File handling

Package management

⚡ FastAPI

The main focus of this repository.

Core Concepts

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

Typical API flow
             HTTP Request
                  │
                  ▼
             ⚡ FastAPI
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   Validation           Business Logic
        │                   │
        └─────────┬─────────┘
                  ▼
             Database
                  │
                  ▼
             JSON Response

🧩 Pydantic

Pydantic is used heavily with FastAPI for data validation and structured data.

Topics

Base models

Type validation

Required fields

Optional fields

Nested models

Lists and dictionaries

Serialization

Deserialization

Custom validation

Example
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str


The model describes what valid data should look like.

🧪 Postman

Postman will be used to test the APIs I build.

Topics

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

Collections

Development cycle
       Build Endpoint
             │
             ▼
        Start FastAPI
             │
             ▼
          Postman
             │
             ▼
       Send Request
             │
             ▼
        Check Response
             │
        ┌────┴────┐
        │         │
      Works     Fails
        │         │
        ▼         ▼
      Keep      Debug
                  │
                  └──────► Test Again

🗄️ Databases

A backend needs somewhere to store and retrieve data.

Topics

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

Learning direction
SQL
 │
 ▼
SQLite
 │
 ▼
PostgreSQL
 │
 ▼
SQLAlchemy
 │
 ▼
FastAPI + Database

🔐 Authentication & Security

As I move beyond basic APIs, I'll learn how applications handle users and protect resources.

Topics

User registration

Login

Password hashing

JWT

Access tokens

Authentication

Authorization

Roles and permissions

Environment variables

Security fundamentals

Basic flow
User
 │
 │ Login
 ▼
FastAPI
 │
 ▼
Verify Credentials
 │
 ▼
Generate Token
 │
 ▼
JWT
 │
 ▼
Authenticated Requests

🧪 Testing

Learning how to make APIs reliable instead of only checking whether they work manually.

Topics

Pytest

Unit testing

API testing

FastAPI TestClient

Endpoint testing

Authentication testing

Database testing

Edge cases

Error handling

🐳 Docker & Deployment

Moving from:

"It works on my computer."

to:

"It can run consistently anywhere."

Topics

Environment variables

Docker

Docker Compose

Containers

Production configuration

CI/CD fundamentals

Cloud deployment

API deployment

Deployment direction
💻 Local Development
        │
        ▼
     🐳 Docker
        │
        ▼
   ☁️ Cloud / Server
        │
        ▼
   🌐 Public API

🤖 AI/ML + FastAPI

One of the main reasons I'm learning FastAPI is to connect backend development with my AI/ML work.

The long-term idea:

              👨‍💻 Client
                  │
                  ▼
              ⚡ FastAPI
                  │
          ┌───────┴────────┐
          ▼                ▼
      🗄️ Database      🤖 AI / ML
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                  Model          LLM
                    │             │
                    └──────┬──────┘
                           ▼
                     📦 JSON Response


Potential applications include:

Machine learning prediction APIs

Deep learning APIs

NLP APIs

Recommendation systems

LLM applications

RAG applications

AI-powered services

📂 Repository Structure

The repository is organized around learning topics, rather than individual projects.

fastapi-learning/
│
├── 📄 README.md
│
├── 01-http-rest/
│   ├── 📄 README.md
│   └── examples/
│       ├── ...
│       └── ...
│
├── 02-json/
│   ├── 📄 README.md
│   └── examples/
│       ├── ...
│       └── ...
│
├── 03-pydantic/
│   ├── 📄 README.md
│   └── examples/
│       ├── ...
│       └── ...
│
├── 04-fastapi-basics/
│   ├── 📄 README.md
│   └── examples/
│       ├── ...
│       └── ...
│
├── 05-postman/
│   ├── 📄 README.md
│   └── collections/
│
├── 06-databases/
│   ├── 📄 README.md
│   └── examples/
│
├── 07-sqlalchemy/
│   ├── 📄 README.md
│   └── examples/
│
├── 08-authentication/
│   ├── 📄 README.md
│   └── examples/
│
├── 09-testing/
│   ├── 📄 README.md
│   └── examples/
│
└── 10-docker/
    ├── 📄 README.md
    └── examples/

📌 Structure Philosophy

Each topic can contain:

README.md
   │
   ├── 📖 Concepts
   ├── 💻 Examples
   ├── 🧪 Experiments
   └── 📝 Notes


The root README explains the overall journey.

Individual folders contain the actual learning material.

Projects will live in their own repositories rather than inside this learning repository.

🛠️ Technology Stack
Technology	Purpose
🐍 Python	Programming language
⚡ FastAPI	Backend / API framework
🧩 Pydantic	Data validation
🚀 Uvicorn	ASGI server
🧪 Postman	API testing
🗄️ SQL	Database language
🐘 PostgreSQL	Relational database
🔗 SQLAlchemy	ORM
🧪 Pytest	Testing
🐳 Docker	Containerization
🌿 Git	Version control
🐙 GitHub	Code hosting
🧠 Learning Approach

This repository is a hands-on laboratory, not just a collection of tutorial code.

My learning cycle:

       📖 Learn
          │
          ▼
      🧠 Understand
          │
          ▼
        💻 Code
          │
          ▼
        🧪 Test
          │
          ▼
        💥 Break
          │
          ▼
       🐛 Debug
          │
          ▼
       🔧 Improve
          │
          ▼
        🚀 Build


The idea is to learn concepts deeply enough that I can use them without following a tutorial step-by-step.

📚 Resources
⚡ FastAPI

https://fastapi.tiangolo.com/

🐍 Python

https://docs.python.org/3/

🧩 Pydantic

https://docs.pydantic.dev/

🐘 PostgreSQL

https://www.postgresql.org/docs/

🔗 SQLAlchemy

https://docs.sqlalchemy.org/

🧪 Postman

https://learning.postman.com/

🧭 Long-Term Direction

The bigger picture:

                         🐍 Python
                            │
             ┌──────────────┴──────────────┐
             ▼                             ▼
       📊 Data / ML                  🌐 Backend
             │                             │
             ▼                             ▼
       🤖 AI / ML                      ⚡ FastAPI
             │                             │
             └──────────────┬──────────────┘
                            ▼
                    🏗️ Complete Systems
                            │
                            ▼
                       ☁️ Deployment


The goal is to become capable of building complete applications and systems, rather than only individual models or isolated pieces of code.

🚧 Repository Status

🟢 Active Learning

This repository will continuously evolve as I learn, experiment, make mistakes, build, and improve.

Learn → Build → Break → Debug → Understand → Repeat.

👨‍💻 Author

Vedant

Python • AI/ML • Backend Development

🔗 GitHub:
https://github.com/jvedant1001-ship-it
