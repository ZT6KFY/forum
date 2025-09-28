from uuid import UUID

from sqlalchemy import ForeignKey, String, Boolean
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database.base_model import Base

THREAD_SCHEMA = "threads"


class Threads(Base):
    __tablename__ = THREAD_SCHEMA
    __table_args__ = {"schema": THREAD_SCHEMA, "comment": "Threads table"}

    title: Mapped[str] = mapped_column(String, nullable=False, comment="Thread title")

    is_locked: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False, comment="Thread is locked"
    )

    is_pinned: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False, comment="Thread is pinned"
    )

    board_sid: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("boards.boards.sid", ondelete="CASCADE"),
        nullable=False,
        comment="Board ID",
    )
    board = relationship("Boards", back_populates="threads", lazy="joined")

    user_sid: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.users.sid", ondelete="CASCADE"),
        nullable=False,
        comment="User ID",
    )
    user = relationship("Users", back_populates="threads", lazy="joined")

    posts = relationship(
        "Posts", back_populates="thread"
    )  # select coz posts - collection
