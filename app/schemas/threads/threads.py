from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class ThreadBase(CoreModel):
    title: str = Field(..., description="Thread title")
    board_sid: UUID = Field(..., description="Board ID")


class ThreadCreate(ThreadBase):
    pass


class ThreadUpdate(CoreModel):
    title: Optional[str] = Field(None, description="Thread title")
    is_locked: Optional[bool] = Field(None, description="Thread is locked")
    is_pinned: Optional[bool] = Field(None, description="Thread is pinned")
    board_sid: Optional[UUID] = Field(None, description="Board ID")


class ThreadInfo(ThreadBase):
    sid: UUID = Field(..., description="UUID of the thread")
    is_locked: bool = Field(False, description="Thread is locked")
    is_pinned: bool = Field(False, description="Thread is pinned")
    user_sid: UUID = Field(..., description="User ID")
    score: int = Field(0, description="Thread score")
    created_at: datetime
    updated_at: datetime
