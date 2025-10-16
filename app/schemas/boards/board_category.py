from typing import Optional
from uuid import UUID

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class BoardCategoryBase(CoreModel):
    title: str = Field(..., description="Title of the board category")


class BoardCategoryCreate(BoardCategoryBase):
    pass


class BoardCategoryUpdate(BoardCategoryBase):
    title: Optional[str] = Field(None, description="Title of the board category")
    board_sid: Optional[UUID] = Field(None, description="UUID of the related board")


class BoardCategoryInfo(BoardCategoryBase):
    sid: UUID = Field(..., description="UUID of the board category")
