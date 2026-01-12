from typing import Literal
from uuid import UUID
from datetime import datetime

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class PostVotesBase(CoreModel):
    value: Literal[1, -1] = Field(
        ..., description="Vote value: 1 (upvote) or -1 (downvote)"
    )


class PostVotesCreate(PostVotesBase):
    post_sid: UUID = Field(..., description="Target Post UUID")


class PostVotesUpdate(CoreModel):
    value: Literal[1, -1] = Field(..., description="New vote value")


class PostVotesInfo(PostVotesBase):
    sid: UUID = Field(..., description="Vote UUID")
    post_sid: UUID = Field(..., description="Post UUID")
    user_sid: UUID = Field(..., description="User UUID")
    created_at: datetime
    updated_at: datetime
