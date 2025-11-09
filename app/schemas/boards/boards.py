from typing import Optional
from uuid import UUID

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class BoardBase(CoreModel):
    name: str = Field(..., description="Name of the board")
    description: str = Field(..., description="Description of the board")
    board_category_sid: UUID = Field(
        ..., description="Board_category ID (FK to board.board_category.sid)"
    )


class BoardCreate(BoardBase):
    pass


class BoardUpdate(BoardBase):
    name: Optional[str] = Field(None, description="Name of the board")
    description: Optional[str] = Field(None, description="Description of the board")


class BoardInfo(BoardBase):
    sid: UUID = Field(..., description="UUID of the board")
    name: str = Field(..., description="Name of the board")
    description: str = Field(..., description="Description of the board")
