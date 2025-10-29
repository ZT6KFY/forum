from sqlalchemy import select
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Posts
from app.repositories.BaseRepository import BaseRepository
from app.schemas import (
    PostCreate,
    PostUpdate,
)


class PostRepository(BaseRepository[Posts, PostCreate, PostUpdate]):
    async def get_by_thread(self, db: AsyncSession, thread_sid: UUID):
        stmt = select(Posts).where(Posts.thread_sid == thread_sid)
        result = await db.execute(stmt)
        return result.scalars().all()


post_repository = PostRepository(Posts)
