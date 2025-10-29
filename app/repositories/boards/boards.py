from uuid import UUID
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Boards
from app.repositories.BaseRepository import BaseRepository
from app.schemas import (
    BoardCreate,
    BoardUpdate,
)


class BoardRepository(BaseRepository[Boards, BoardCreate, BoardUpdate]):
    async def get_by_board_category(self, db: AsyncSession, board_category_sid: UUID):
        stmt = select(Boards).where(Boards.board_category_sid == board_category_sid)
        result = await db.execute(stmt)
        return result.scalars().all()


board_repository = BoardRepository(Boards)
