"""Init DB connection and making session"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from settings import REAL_DATABASE_URL

engine = create_async_engine(
    REAL_DATABASE_URL,
    echo=True
)

async_session_maker = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class Base(DeclarativeBase):
    """Base class ORM"""
