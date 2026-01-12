from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import Field, EmailStr

from app.schemas.CoreModel import CoreModel


class UserBase(CoreModel):
    username: str = Field(..., description="Username")
    email: EmailStr = Field(..., description="Email address")


class UserCreate(UserBase):
    password: str = Field(..., description="Password")


class UserUpdate(CoreModel):
    username: Optional[str] = Field(None, description="Username")
    email: Optional[EmailStr] = Field(None, description="Email address")


class UserInfo(UserBase):
    sid: UUID = Field(..., description="UUID of the user")
    role: str = Field(..., description="Role")
    is_banned: bool = Field(False, description="Is user banned")
    created_at: datetime
    updated_at: datetime
