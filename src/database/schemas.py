"""Schemas"""

import datetime

from pydantic import BaseModel


class User(BaseModel):
    """Schema for create new user"""
    user_id: int
    f_name: str | None
    s_name: str | None
    user_name: str
    phone_number: str | None
    date: datetime.datetime
