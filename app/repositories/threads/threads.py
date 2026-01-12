from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Threads
from app.repositories.BaseRepository import BaseRepository
from app.schemas import (
    ThreadCreate,
    ThreadUpdate,
)


class ThreadRepository(BaseRepository[Threads, ThreadCreate, ThreadUpdate]):
    async def get_by_board(self, db: AsyncSession, board_sid: UUID):
        stmt = select(Threads).where(Threads.board_sid == board_sid)
        result = await db.execute(stmt)
        return result.scalars().all()

    async def get_by_user(self, db: AsyncSession, user_sid: UUID):
        stmt = select(Threads).where(Threads.user_sid == user_sid)
        result = await db.execute(stmt)
        return result.scalars().all()


thread_repository = ThreadRepository(Threads)
