from app.models import Boards
from app.repositories.BaseRepository import BaseRepository
from app.schemas import (
    BoardCreate,
    BoardUpdate,
)


class BoardRepository(BaseRepository[Boards, BoardCreate, BoardUpdate]):
    pass


board_repository = BoardRepository(Boards)
