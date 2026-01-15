from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Users
from app.repositories.BaseRepository import BaseRepository
from app.schemas import (
    UserCreate,
    UserUpdate,
)


class UserRepository(BaseRepository[Users, UserCreate, UserUpdate]):
    async def get_by_email(self, db: AsyncSession, email: str) -> Users | None:
        stmt = select(Users).where(Users.email == email)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_username(self, db: AsyncSession, username: str):
        stmt = select(self.model).where(self.model.username == username)
        result = await db.execute(stmt)
        return result.unique().scalar_one_or_none()


user_repository = UserRepository(Users)
