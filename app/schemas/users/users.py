from typing import Optional
from uuid import UUID

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class UserBase(CoreModel):
    username: str = Field(..., description="Username")
    email: str = Field(..., description="Email address")


class UserCreate(UserBase):
    password: str = Field(..., description="Password")
    # username, email, password


class UserUpdate(UserBase):
    username: Optional[str] = Field(None, description="Username")
    email: Optional[str] = Field(None, description="Email address")
    role: Optional[str] = Field(None, description="Role")
    # username, email, password


class UserInfo(UserBase):
    sid: UUID = Field(..., description="UUID of the user")
    username: str = Field(..., description="Username")
