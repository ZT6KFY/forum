from app.models import BoardCategories
from app.repositories.BaseRepository import BaseRepository
from app.schemas import (
    BoardCategoryCreate,
    BoardCategoryUpdate,
)


class BoardCategoryRepository(
    BaseRepository[BoardCategories, BoardCategoryCreate, BoardCategoryUpdate]
):
    pass


board_category_repository = BoardCategoryRepository(BoardCategories)
