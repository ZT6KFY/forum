from uuid import UUID

from sqlalchemy import ForeignKey, String, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database.base_model import Base

THREAD_SCHEMA = "threads"


class Threads(Base):
    __tablename__ = THREAD_SCHEMA
    __table_args__ = {"schema": THREAD_SCHEMA, "comment": "Threads table"}

    title: Mapped[str] = mapped_column(String, nullable=False, comment="Thread title")

    score: Mapped[int] = mapped_column(
        Integer,
        default=0,
        server_default="0",
        nullable=False,
        unique=False,
        comment="Score of the thread",
    )

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

    thread_votes = relationship(
        "ThreadVotes",
        back_populates="thread",
        cascade="all, delete-orphan",
        lazy="select",
    )
