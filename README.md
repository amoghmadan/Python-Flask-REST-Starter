# Python-Flask-REST-Starter
Kick-starter to your REST application.

## Setup Project
    Create a virtual environment.
    Run pip install -r requirements.txt

## Run Project
    cd src
    python main.py

## Project Structure
    .
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    ├── resources
    │   ├── development.ini
    │   └── production.ini
    └── src
        ├── app.py
        ├── controllers
        │   ├── __init__.py
        │   ├── person.py
        │   └── root.py
        ├── main.py
        ├── models
        │   ├── __init__.py
        │   └── person.py
        ├── routes
        │   ├── __init__.py
        │   ├── person.py
        │   └── root.py
        ├── serializers
        │   ├── __init__.py
        │   └── person.py
        └── utils
            ├── database.py
            ├── __init__.py
            └── migrate.py

## How to run in production?
    cd src
    gunicorn -b 0.0.0.0:8000 -w 4 main:app -e ENV=production
    
## Migrate Database
    cd src
    export FLASK_APP=main.py
    flask db init
    flask db upgrade
