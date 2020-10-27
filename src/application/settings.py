import os
import configparser
from contextlib import suppress
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler

ENV: str = os.environ.get("ENV", "development")

BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR: str = os.path.dirname(BASE_DIR)
LOG_DIR: str = os.path.join(ROOT_DIR, "logs")
with suppress(FileExistsError):
    os.makedirs(LOG_DIR)
LOG_FILE: str = os.path.join(LOG_DIR, "debug.log")

CONFIG: configparser.ConfigParser = configparser.ConfigParser()
CONFIG.read(os.path.join(ROOT_DIR, "resources", f"{ENV}.ini"))

DEBUG: bool = CONFIG.getboolean("DEFAULT", "DEBUG")
PORT: int = CONFIG.getint("DEFAULT", "PORT")

SQLALCHEMY_DATABASE_URI: str = CONFIG.get("DEFAULT", "SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS: bool = CONFIG.getboolean(
    "DEFAULT", "SQLALCHEMY_TRACK_MODIFICATIONS"
)

FORMATTER: Formatter = Formatter(
    "%(asctime)s  %(levelname)s  %(process)d  %(pathname)s  %(funcName)s  %(lineno)d  %(message)s"
)
LOGGING_HANDLER: TimedRotatingFileHandler = TimedRotatingFileHandler(
    LOG_FILE, interval=1, when="midnight", backupCount=7
)
LOGGING_HANDLER.setFormatter(FORMATTER)
