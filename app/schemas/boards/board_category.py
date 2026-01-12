from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class BoardCategoryBase(CoreModel):
    title: str = Field(..., description="Title of the board category")


class BoardCategoryCreate(BoardCategoryBase):
    pass


class BoardCategoryUpdate(CoreModel):
    title: Optional[str] = Field(None, description="Title of the board category")


class BoardCategoryInfo(BoardCategoryBase):
    sid: UUID = Field(..., description="UUID of the board category")
    created_at: datetime
    updated_at: datetime
