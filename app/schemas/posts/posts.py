from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class PostBase(CoreModel):
    content: Optional[str] = Field(
        None, description="Content of the post"
    )  # nullable в БД
    thread_sid: UUID = Field(..., description="Thread ID (FK to threads.threads.sid)")
    user_sid: UUID = Field(..., description="User ID (FK to users.users.sid)")


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    content: Optional[str] = Field(None, description="Content of the post")
    thread_sid: Optional[UUID] = Field(
        None, description="Thread ID (FK to threads.threads.sid)"
    )
    user_sid: Optional[UUID] = Field(
        None, description="User ID (FK to users.users.sid)"
    )


class PostInfo(PostBase):
    sid: UUID = Field(..., description="UUID of the post")
    created_at: datetime = Field(..., description="Created at timestamp")
    updated_at: datetime = Field(..., description="Updated at timestamp")
