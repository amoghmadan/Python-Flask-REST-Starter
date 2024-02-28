from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DEBUG = True

SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR / "db.sqlite3"}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
