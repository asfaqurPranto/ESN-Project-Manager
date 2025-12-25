# ESN Project Manager

[![Django](https://img.shields.io/badge/Django-4.x-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/Database-SQLite3-lightgrey)](https://www.sqlite.org/)

A **RESTful web application** built with the Django framework, designed as an **Enterprise Social Network (ESN)** focused on **project management**. It enables users to create profiles, search for professionals, discover team members across projects, and allows admins to create and manage projects.

This project demonstrates advanced user authentication, search functionality, profile management, and an admin panel for project creation.

## Features

### User Features
- **Registration & Authentication**
  - Register new users with personal and professional details.
  - Secure login.
- **Profile Management**
  - View your own profile.
  - Edit personal information (name, profession, location, bio, etc.).
- **Discovery & Search**
  - Discover all team members working on projects.
  - Search users by name, profession, or role.

### Admin Features
- **Project Creation**
  - Create new projects with title, description, tags, and deadlines.

## API Endpoints

| Method | Endpoint                  | Description                              | Body/Example |
|--------|---------------------------|------------------------------------------|--------------|
| POST   | `/login`                  | User login                               | `{ "email": "abc@gmail.com", "password": "xxxxx" }` |
| POST   | `/register`               | Create new user                          | `{ "firstname": "xyz", "lastname": "xyz", "email": "xyz@gmail.com", "profession": "Python dev", "country": "Bangladesh", "city": "dhaka", "bio": "..." }` |
| POST   | `/create-project` (Admin) | Create a new project                     | `{ "title": "todo", "description": "...", "tags": "go, redis, mysql", "deadlines": 20 }` |
| GET    | `/discover-people`        | List all team members in projects        | - |
| POST   | `/search-result/?q=query` | Search by name, profession, or role      | Query in body or params |
| GET    | `/view-profile`           | View own profile                         | - |
| PUT    | `/edit-profile`           | Update user information                  | Updated fields |

## Technologies Used

- **Backend**: Python, Django
- **Database**: SQLite3
- **Frontend**: HTML, CSS
- **Other**: Django REST framework (implied for RESTful design), Django's built-in authentication

## Installation & Setup


```bash
git clone https://github.com/asfaqurPranto/esn-project-manager.git
cd esn-project-manager

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```
project will be running on: http://127.0.0.1:8000/