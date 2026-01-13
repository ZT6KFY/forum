from app.models import BoardCategories, ThreadVotes
from app.repositories.BaseRepository import BaseRepository
from app.schemas import (
    BoardCategoryCreate,
    BoardCategoryUpdate,
)


class BoardCategoryRepository(
    BaseRepository[BoardCategories, BoardCategoryCreate, BoardCategoryUpdate]
):
    pass


thread_votes_repository = BoardCategoryRepository(ThreadVotes)
