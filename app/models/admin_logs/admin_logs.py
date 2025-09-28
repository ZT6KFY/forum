from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database.base_model import Base

ADMIN_LOGS_SCHEMA = "admin_logs"


class AdminLogs(Base):
    __tablename__ = ADMIN_LOGS_SCHEMA
    __table_args__ = {"schema": ADMIN_LOGS_SCHEMA, "comment": "Admin logs table"}

    admin_sid: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.users.sid", ondelete="SET NULL"),
        nullable=True,
        comment="Admin ID",
    )
    user = relationship("Users", back_populates="admin_logs")

    action: Mapped[str] = mapped_column(String, nullable=False, comment="Action")
    target_type: Mapped[str] = mapped_column(
        String, nullable=False, comment="Target type"
    )
    target_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), nullable=False, comment="Target ID"
    )
