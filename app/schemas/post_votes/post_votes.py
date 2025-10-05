from typing import Optional
from uuid import UUID

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class PostVotesBase(CoreModel):
    post_id: UUID = Field(..., description="UUID of the post")
    user_id: UUID = Field(..., description="UUID of the user who voted")
    value: int = Field(..., description="Vote value (e.g., +1 or -1)")


class PostVotesCreate(PostVotesBase):
    pass


class PostVotesUpdate(PostVotesBase):
    post_id: Optional[UUID] = Field(None, description="UUID of the post")
    user_id: Optional[UUID] = Field(None, description="UUID of the user who voted")
    value: Optional[int] = Field(None, description="Vote value (e.g., +1 or -1)")


class PostVotesInfo(PostVotesBase):
    sid: UUID = Field(..., description="UUID of the post vote")
    post_id: UUID = Field(..., description="UUID of the post")
    user_id: UUID = Field(..., description="UUID of the user who voted")
    value: int = Field(..., description="Vote value (e.g., +1 or -1)")
