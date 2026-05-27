Student Management System Backend
Project Overview

Student Management System Backend is a professional REST API application developed using Python FastAPI and MySQL. The project provides complete CRUD operations for managing student records with secure password hashing, layered architecture, JWT authentication foundation, and Swagger API documentation.

This project follows industry-level backend development practices similar to Spring Boot layered architecture.

Features
Student Management
Add Student
Get All Students
Get Student By ID
Update Student
Delete Student
Professional Backend Features
FastAPI REST APIs
MySQL Database Integration
SQLAlchemy ORM
Service Layer Architecture
Dependency Injection
Pydantic Request & Response Schemas
Exception Handling
Password Hashing using bcrypt
JWT Authentication Setup
Swagger API Documentation
Tech Stack
Backend
Python
FastAPI
Database
MySQL
ORM
SQLAlchemy
Authentication
JWT (python-jose)
bcrypt
passlib
API Testing
Swagger UI
Version Control
Git & GitHub
Project Structure
student-management-system/
│
├── app/
│   ├── auth/
│   │     ├── __init__.py
│   │     └── auth_handler.py
│   │
│   ├── models/
│   │     ├── __init__.py
│   │     └── student.py
│   │
│   ├── routers/
│   │     ├── __init__.py
│   │     └── student_router.py
│   │
│   ├── schemas/
│   │     ├── __init__.py
│   │     └── student_schema.py
│   │
│   ├── services/
│   │     ├── __init__.py
│   │     └── student_service.py
│   │
│   ├── __init__.py
│   ├── database.py
│   └── main.py
│
├── venv/
├── .gitignore
└── README.md
API Endpoints
Method	Endpoint	Description
GET	/students	Get all students
GET	/students/{id}	Get student by ID
POST	/students	Add student
PUT	/students/{id}	Update student
DELETE	/students/{id}	Delete student
Installation & Setup
Clone Repository
git clone https://github.com/your-username/student-management-system.git
Navigate to Project
cd student-management-system
Create Virtual Environment
python -m venv venv
Activate Virtual Environment
Windows
venv\Scripts\activate
Install Dependencies
pip install fastapi uvicorn sqlalchemy pymysql python-jose passlib bcrypt==4.0.1 python-multipart
MySQL Database Setup
Create Database
CREATE DATABASE studentdb;
Configure Database

Update database.py

DATABASE_URL = "mysql+pymysql://root:root@localhost/studentdb"

Replace:

username
password
according to your MySQL configuration.
Run Application
uvicorn app.main:app --reload
Swagger API Documentation

Open browser:

http://127.0.0.1:8000/docs
Example Request
Add Student
POST /students
{
  "name": "Narendra",
  "email": "narendra@gmail.com",
  "course": "MCA",
  "city": "Nellore",
  "password": "12345"
}
Example Response
{
  "id": 1,
  "name": "Narendra",
  "email": "narendra@gmail.com",
  "course": "MCA",
  "city": "Nellore"
}
Authentication Features
Passwords are encrypted using bcrypt hashing.
JWT token utility functions implemented.
Secure authentication architecture prepared for login system.
Professional Concepts Implemented
Layered Architecture
Router → Service → Database
Dependency Injection

Implemented using:

Depends(get_db)
Exception Handling

Implemented using:

HTTPException

with proper HTTP status codes.

Request & Response Validation

Implemented using Pydantic Schemas.

Future Enhancements
Login API
JWT Token Authentication
Protected APIs
Role-Based Access
React Frontend
Docker Deployment
Pagination & Search
Unit Testing
Author
Narendra Mediboina

Java Full Stack Developer | Python Backend Developer
