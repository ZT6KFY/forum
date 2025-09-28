from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database.base_model import Base

BOARDS_SCHEMA = "boards"


class Boards(Base):
    __tablename__ = "boards"
    __table_args__ = {"schema": BOARDS_SCHEMA, "comment": "Boards table"}

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
        comment="Name of the board",
    )
    description: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Description of the board",
    )

    threads = relationship(
        "Threads", back_populates="board", cascade="all, delete-orphan", lazy="select"
    )
