from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class PostBase(CoreModel):
    content: Optional[str] = Field(None, description="Content of the post")


class PostCreate(PostBase):
    thread_sid: UUID = Field(..., description="Thread ID (FK to threads.threads.sid)")
    content: str
    pass


class PostUpdate(PostBase):
    content: Optional[str] = Field(None, description="Content of the post")


class PostInfo(PostBase):
    sid: UUID = Field(..., description="UUID of the post")
    score: Optional[int] = Field(None, description="Score of the post")
    created_at: datetime = Field(..., description="Created at timestamp")
    updated_at: datetime = Field(..., description="Updated at timestamp")
    thread_sid: UUID = Field(..., description="Thread ID")
    user_sid: UUID = Field(..., description="User ID")
