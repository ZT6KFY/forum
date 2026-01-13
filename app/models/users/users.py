from sqlalchemy import String, Boolean

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database.base_model import Base

USER_SCHEMA = "users"


class Users(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": USER_SCHEMA, "comment": "User table"}

    username: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True,
        comment="Username",  # null for anonymous
    )
    email: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
        comment="Email address",  # null for anonymous
    )
    password_hash: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
        comment="Password hash",  # null for anonymous
    )
    role: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="user",  # admin/user/anonymous
    )
    is_banned: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    posts = relationship(
        "Posts", back_populates="user", cascade="all, delete-orphan", lazy="select"
    )
    post_votes = relationship(
        "PostVotes",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="select",
    )

    thread_votes = relationship(
        "ThreadVotes",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="select",
    )
    admin_logs = relationship(
        "AdminLogs", back_populates="user", cascade="all, delete-orphan", lazy="select"
    )
    threads = relationship("Threads", back_populates="user", lazy="select")
