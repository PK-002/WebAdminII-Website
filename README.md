## WebAdminII Project

# RANK THAT

### By Edward Emanuel and Paul Kranker

## Description

Rank That is a website that allows users to upload their own personal image files and create tier lists, which are ways to graphically rank images based on a user’s personal opinion. Users are able to customize the rows in their tier lists. They can share tier lists by downloading an image of them or publishing them to the site and sharing the link.

The frontend is built with plain html and csss. The backend is built with Django.

## Setup

### Clone the repo

```
    git clone https://github.com/PK-002/WebAdminII-Website.git
    cd WebAdminII-Website
```

### Setup the virtual environment

```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install the dependencies

```
    pip install -r requirements.txt
```

### Setup the database

This will set up all the tables in the database.

```
    python manage.py migrate
```

### Run the website locally

```
    python manage.py runserver
```
