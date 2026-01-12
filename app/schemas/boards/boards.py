from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class BoardBase(CoreModel):
    name: str = Field(..., description="Name of the board")
    description: str = Field(..., description="Description of the board")
    board_category_sid: Optional[UUID] = Field(None, description="Board category ID")


class BoardCreate(BoardBase):
    board_category_sid: Optional[UUID] = Field(None, description="Board category ID")


class BoardUpdate(CoreModel):
    name: Optional[str] = Field(None, description="Name of the board")
    description: Optional[str] = Field(None, description="Description of the board")
    board_category_sid: Optional[UUID] = Field(None, description="Board category ID")


class BoardInfo(BoardBase):
    sid: UUID = Field(..., description="UUID of the board")
    created_at: datetime
    updated_at: datetime
