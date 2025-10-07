from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class ThreadBase(CoreModel):
    title: str = Field(..., description="Thread title")
    is_locked: bool = Field(..., description="Thread is locked")
    is_pinned: bool = Field(..., description="Thread is pinned")
    board_sid: UUID = Field(..., description="Board ID (FK to boards.boards.sid)")
    user_sid: UUID = Field(..., description="User ID (FK to users.users.sid)")


class ThreadCreate(ThreadBase):
    # sid/created_at/updated_at выставляются на уровне сервиса/БД
    pass


class ThreadUpdate(CoreModel):
    title: Optional[str] = Field(None, description="Thread title")
    is_locked: Optional[bool] = Field(None, description="Thread is locked")
    is_pinned: Optional[bool] = Field(None, description="Thread is pinned")
    board_sid: Optional[UUID] = Field(
        None, description="Board ID (FK to boards.boards.sid)"
    )
    user_sid: Optional[UUID] = Field(
        None, description="User ID (FK to users.users.sid)"
    )


class ThreadInfo(ThreadBase):
    sid: UUID = Field(..., description="UUID of the thread")
    created_at: datetime = Field(..., description="Created at timestamp")
    updated_at: datetime = Field(..., description="Updated at timestamp")
