from typing import Optional
from uuid import UUID
from datetime import datetime

from pydantic import Field

from app.schemas.CoreModel import CoreModel


class AdminLogBase(CoreModel):
    admin_sid: Optional[UUID] = Field(
        None, description="Admin ID (nullable, FK to users.users.sid)"
    )
    action: str = Field(..., description="Action")
    target_type: str = Field(..., description="Target type")
    target_id: UUID = Field(..., description="Target ID")


class AdminLogCreate(AdminLogBase):
    pass


class AdminLogUpdate(CoreModel):
    admin_sid: Optional[UUID] = Field(
        None, description="Admin ID (nullable, FK to users.users.sid)"
    )
    action: Optional[str] = Field(None, description="Action")
    target_type: Optional[str] = Field(None, description="Target type")
    target_id: Optional[UUID] = Field(None, description="Target ID")


class AdminLogInfo(AdminLogBase):
    sid: UUID = Field(..., description="UUID of the admin log record")
    created_at: datetime = Field(..., description="Created at timestamp")
    updated_at: datetime = Field(..., description="Updated at timestamp")
