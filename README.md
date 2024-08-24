# Python Flask REST Starter

Kick-starter to your REST application.

## How to set up environment variables?

- Fill the .env file with the following values, they might need adjustment.
  ```dotenv
  DEBUG=<BOOLEAN>                   # Dev: True
  SECRET_KEY=<TOKEN>                # Dev: a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p16q
  SQLALCHEMY_DATABASE_URI=<SQLITE>  # Dev: sqlite:///db.sqlite3
  ```

## How to set up project for development?

- Create a virtual environment: -
  ```bash
  python -m venv venv
  ```
- Activate: -
    - Windows: `venv\Scripts\activate`
    - Unix-like: `. venv\bin\activate`
- Install dependencies: -
  ```bash
  pip install . -e '.[all]'
  ```
- Set environment variable: -
    - Windows: `SET FLASK_APP=app.wsgi`
    - Unix-like: `export FLASK_APP=app.wsgi`
- Create a new user: -
  ```bash
  flask manage createsuperuser
  ```
- Run: -
  ```bash
  flask run --debug
  ```

## How to set up project for deployment?

- Create a virtual environment: -
  ```bash
  python -m venv venv
  ```
- Activate: -
    - Windows: `venv\Scripts\activate`
    - Unix-like: `. venv\bin\activate`
- Install dependencies: -
  ```bash
  pip install -e '.[deployment]'
  ```
- Set environment variable: -
    - Windows: `SET FLASK_APP=app.wsgi`
    - Unix-like: `export FLASK_APP=app.wsgi`
- Create a new user: -
  ```bash
  flask manage createsuperuser
  ```
- Run: -
  ```bash
  gunicorn -b 0.0.0.0:8000 app.wsgi:application -w 4 -t 9
  ```
