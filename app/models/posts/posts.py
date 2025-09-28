from uuid import UUID

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database.base_model import Base

POST_SCHEMA = "posts"


class Posts(Base):
    __tablename__ = "posts"
    __table_args__ = {"schema": POST_SCHEMA, "comment": "Post table"}

    content: Mapped[str] = mapped_column(
        String, nullable=True, unique=False, comment="Content of the post"
    )

    thread_sid: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("threads.threads.sid", ondelete="CASCADE"),
        nullable=False,
        comment="Thread ID",
    )
    thread = relationship("Threads", back_populates="posts", lazy="select")

    user_sid: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.users.sid", ondelete="CASCADE"),
        nullable=False,
        comment="User ID",
    )
    user = relationship("Users", back_populates="posts", lazy="joined")

    post_votes = relationship(
        "PostVotes", back_populates="post", cascade="all, delete-orphan", lazy="joined"
    )
