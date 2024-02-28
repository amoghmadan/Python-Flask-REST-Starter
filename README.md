# Python Flask REST Starter

Kick-starter to your REST application.

## Setup Project

- Create a virtual environment: -
  ```bash
  python -m venv venv
  ```
- Activte: -
  - Windows: `venv\Scripts\activate`
  - Unix-like: `. venv\bin\activate`
- Run: -
  ```bash
  pip install .
  ```

## Run project (in development mode)

- Activte: -
  - Windows: `venv\Scripts\activate`
  - Unix-like: `. venv\bin\activate`
- Change directory: -
  ```bash
  cd src
  ```
- Create a new user: -
  ```bash
  flask run createsuperuser
  ```
- Run: -
  ```bash
  python wsgi.py
  ```

## How to run in production?

```bash
gunicorn -b 0.0.0.0:8000 --chdir=src -w 4 -t 10 wsgi:application
```
