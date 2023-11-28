"""Models for ORM SQLAlchemy"""

import datetime

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    """User model ORM"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        Integer, nullable=False,
        unique=True, name="ID to telegram"
    )
    f_name: Mapped[str] = mapped_column(
        String(50), nullable=True, name="First name"
    )
    s_name: Mapped[str] = mapped_column(
        String(50), nullable=True, name="Second name"
    )
    user_name: Mapped[str] = mapped_column(
        String(50), nullable=False, name="Username"
    )
    phone_number: Mapped[str] = mapped_column(
        String(18), nullable=True, name="Phone number"
    )
    date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
