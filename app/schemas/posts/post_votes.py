from uuid import UUID
from typing import Optional, Literal
from pydantic import BaseModel, Field
from app.schemas.CoreModel import CoreModel


class PostVotesBase(CoreModel):
    value: Literal[1, -1] = Field(
        ..., description="Vote value: 1 (upvote) or -1 (downvote)"
    )


class PostVotesCreate(PostVotesBase):
    user_sid: UUID = Field(..., description="User UUID (TEMPORARY FOR TESTING)")


class PostVotesUpdate(CoreModel):
    value: Literal[1, -1] = Field(..., description="New vote value")


class VoteResponse(BaseModel):
    post_sid: UUID
    new_score: int
    current_vote: Optional[int]
