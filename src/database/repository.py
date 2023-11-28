"""Users repository"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Sequence

from src.database import async_session_maker
from src.database.models import User as ORMUser
from src.database.schemas import User as SchemaUser


class RepoUsers:
    """Repository USERS"""
    def __init__(self):
        self.session: AsyncSession = async_session_maker()

    async def add_user(self, data: SchemaUser) -> int:
        """Added new user in DB"""
        new_user = ORMUser(**data.model_dump())
        async with self.session as s:
            s.add(new_user)
            await s.commit()
            await s.close()
        return new_user.id

    async def get_user_by_user_id(self, user_id) -> ORMUser | None:
        """Returning user if user_id in DB"""
        async with self.session as s:
            query = select(ORMUser.id).where(ORMUser.user_id == user_id)
            res = await s.scalar(query)
            await s.close()
        return res

    async def get_all_new_users(self, date) -> Sequence:
        """Returning users filtering by date"""
        async with self.session as s:
            query = select(ORMUser.id).where(ORMUser.date >= date)
            res = await s.scalars(query)
            await s.close()
        return res.all()
