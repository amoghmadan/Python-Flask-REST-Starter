# Python Flask REST Starter

Kick-starter to your REST application.

## How to setup project for development?

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

## How to setup project for deployment?

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
