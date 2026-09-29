# ⚡ FastAPI Learning Lab

> A hands-on learning repository for mastering backend development with Python and FastAPI, from HTTP and REST fundamentals to databases, authentication, testing, Docker, deployment, and AI/ML APIs.

## Table of Contents

- [About](#about)
- [Learning Roadmap](#learning-roadmap)
- [Topics](#topics)
  - [Web & API Fundamentals](#web--api-fundamentals)
  - [Python](#python)
  - [FastAPI](#fastapi)
  - [Pydantic](#pydantic)
  - [Postman](#postman)
  - [Databases](#databases)
  - [Authentication & Security](#authentication--security)
  - [Testing](#testing)
  - [Docker & Deployment](#docker--deployment)
  - [AI/ML + FastAPI](#aiml--fastapi)
- [Repository Structure](#repository-structure)
- [Technology Stack](#technology-stack)
- [Learning Approach](#learning-approach)
- [Resources](#resources)
- [Long-Term Direction](#long-term-direction)
- [Repository Status](#repository-status)
- [Author](#author)

## About

**FastAPI Learning Lab** is a personal, hands-on repository for learning backend development with Python and FastAPI.

The repository focuses on understanding how backend systems work rather than only learning framework syntax. The learning path covers API fundamentals, data validation, databases, authentication, testing, containerization, deployment, and the foundations needed to serve AI/ML applications through APIs.

Each topic is organized as a self-contained learning area with explanations, examples, experiments, and notes.

## Learning Roadmap

The learning path progresses from core programming and API concepts toward complete backend systems:

```text
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
   ├──────────────┬──────────────┐
   ▼              ▼              ▼
🧪 Testing   🗄️ Database   🔐 Authentication
   │              │              │
   └──────────────┼──────────────┘
                  ▼
             🐳 Docker
                  │
                  ▼
             🚀 Deployment
                  │
                  ▼
             🤖 AI / ML APIs

The long-term objective is to understand how to build systems that can serve, secure, test, and deploy AI/ML applications—not just train individual models.

Topics
Web & API Fundamentals
The foundation for understanding how applications communicate over the web.

Topics include:

HTTP

REST

Client/server architecture

Requests and responses

HTTP methods

HTTP status codes

Headers

Query parameters

Path parameters

JSON

API design

Basic request flow:

Client
  │
  │ HTTP Request
  ▼
Backend / API
  │
  │ HTTP Response
  ▼
Client

Python
Python concepts required for backend development and FastAPI.

Topics include:

Functions

Modules and packages

Virtual environments

Type hints

Exception handling

Classes and object-oriented programming

Decorators

async / await

JSON handling

File handling

Package management

FastAPI
FastAPI is the primary focus of this repository.

Topics include:

FastAPI fundamentals

Routes and endpoints

HTTP methods: GET, POST, PUT, PATCH, DELETE

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

A typical API flow:

HTTP Request
     │
     ▼
  FastAPI
     │
 ┌───┴─────────────┐
 ▼                 ▼
Validation     Business Logic
 │                 │
 └────────┬────────┘
          ▼
      Database
          │
          ▼
    JSON Response

Pydantic
Pydantic provides structured data models and validation used throughout FastAPI applications.

Topics include:

Base models

Type validation

Required fields

Optional fields

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

The model defines the expected structure and types of valid data.

Postman
Postman is used as part of the API development and testing workflow.

Topics include:

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

Typical workflow:

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
 ▼         ▼
Works     Fails
 │         │
 ▼         ▼
Keep     Debug
           │
           └──────► Test Again

Databases
The database learning path covers both relational database fundamentals and their integration with FastAPI.

Topics include:

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

The intended progression is:

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

Authentication & Security
The repository explores the fundamentals required to protect API resources and manage users.

Topics include:

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

Basic authentication flow:

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

Testing
Testing is introduced to move beyond manually checking whether an API works.

Topics include:

Pytest

Unit testing

API testing

FastAPI TestClient

Endpoint testing

Authentication testing

Database testing

Edge cases

Error handling

Docker & Deployment
The deployment section focuses on moving from local development toward reproducible application environments.

Topics include:

Environment variables

Docker

Docker Compose

Containers

Production configuration

CI/CD fundamentals

Cloud deployment

API deployment

Deployment direction:

Local Development
       │
       ▼
    🐳 Docker
       │
       ▼
 ☁️ Cloud / Server
       │
       ▼
   🌐 Public API

AI/ML + FastAPI
A major long-term purpose of learning FastAPI is connecting backend development with AI/ML applications.

The intended architecture is:

Client
  │
  ▼
FastAPI
  │
  ├───────────────┐
  ▼               ▼
Database        AI / ML
                  │
           ┌──────┴──────┐
           ▼             ▼
         Model          LLM
           │             │
           └──────┬──────┘
                  ▼
            JSON Response

Potential application areas include:

Machine learning prediction APIs

Deep learning APIs

NLP APIs

Recommendation systems

LLM applications

RAG applications

AI-powered services

Repository Structure
The repository is organized around learning topics rather than individual production projects.

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
└── 10-docker/
    ├── README.md
    └── examples/

Each topic can contain:

README.md
   │
   ├── Concepts
   ├── Examples
   ├── Experiments
   └── Notes

The root README provides the overall learning path, while individual directories contain the detailed material for each topic.

Projects are intended to live in their own repositories rather than inside this learning repository.

Technology Stack
Technology	Purpose
Python	Programming language
FastAPI	Backend and API framework
Pydantic	Data validation and structured data
Uvicorn	ASGI server
Postman	API testing
SQL	Database language
PostgreSQL	Relational database
SQLAlchemy	ORM
Pytest	Testing
Docker	Containerization
Git	Version control
GitHub	Code hosting

Learning Approach
This repository is intended to be a hands-on laboratory rather than a collection of code copied from tutorials.

The learning cycle is:

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

The goal is to understand concepts deeply enough to apply them independently instead of following a tutorial step by step.

Resources
The repository uses the following documentation and learning resources as references:

FastAPI Documentation

Python Documentation

Pydantic Documentation

PostgreSQL Documentation

SQLAlchemy Documentation

Postman Learning Center

Long-Term Direction
The broader learning direction combines backend development with AI/ML:

                 🐍 Python
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      📊 Data / ML        🌐 Backend
          │                   │
          ▼                   ▼
       🤖 AI / ML          ⚡ FastAPI
          │                   │
          └─────────┬─────────┘
                    ▼
             🏗️ Complete Systems
                    │
                    ▼
               ☁️ Deployment

The goal is to become capable of building complete applications and systems rather than only individual models or isolated pieces of code.

Repository Status
🟢 Active Learning

This repository will continue to evolve as new concepts are learned, experiments are added, mistakes are debugged, and existing implementations are improved.

Learn → Build → Break → Debug → Understand → Repeat.

Author
Vedant

Python • AI/ML • Backend Development

GitHub: @jvedant1001-ship-it
