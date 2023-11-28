"""Response messages and command messages"""

from enum import Enum


class ResponseMSG(Enum):
    """Messages response"""
    GREETINGS = "Добрый день!"
    STUFF = "Подготовила для вас материал"
    AFTER_STUFF = "Скоро вернусь с новым материалом!"
    COMMAND1 = "Новых пользователей "


class Commands(Enum):
    """Command messages"""
    GET_ALL_NEW_USERS = "/users_today"
