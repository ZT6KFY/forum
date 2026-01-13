from uuid import UUID

from sqlalchemy import ForeignKey, Integer, UniqueConstraint, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database.base_model import Base

POST_SCHEMA = "posts"


class PostVotes(Base):
    __tablename__ = "post_votes"
    __table_args__ = (
        UniqueConstraint("post_sid", "user_sid", name="uq_post_vote_user"),
        CheckConstraint(
            "value IN (-1, 1)", name="check_vote_value_valid"
        ),  # <-- Только -1 или 1
        {"schema": POST_SCHEMA, "comment": "Post Votes table"},
    )

    post_sid: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("posts.posts.sid", ondelete="CASCADE"),
        nullable=False,
        comment="Post ID",
    )
    post = relationship("Posts", back_populates="post_votes", lazy="joined")

    user_sid: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.users.sid", ondelete="CASCADE"),
        nullable=False,
        comment="User ID",
    )
    user = relationship("Users", back_populates="post_votes", lazy="joined")

    value: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="Value of post votes"
    )
