"""SETTINGS APP"""

from envparse import Env
from loguru import logger

env = Env()
LOGER = logger


def info_only(record):
    """filter level loguru"""
    return record["level"].name == "INFO"


LOGER.add(
    "logs/errors.log",
    rotation="10 KB",
    format="{time} {level} {message}",
    level="ERROR"
)

LOGER.add(
    "logs/info.log",
    rotation="10 KB",
    format="{time} {level} {message}",
    level="INFO",
    filter=info_only
)

env.read_envfile(".env")

API_ID = env.int("API_ID")
API_HASH = env.str("API_HASH")
FTIME = env.float("FTIME")
STIME = env.float("STIME")
TTIME = env.float("TTIME")
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default=f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
)
