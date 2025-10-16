from uuid import UUID


from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database.base_model import Base

BOARDS_SCHEMA = "boards"


class Boards(Base):
    __tablename__ = "boards"
    __table_args__ = {"schema": BOARDS_SCHEMA, "comment": "Boards table"}

    board_category_sid: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("boards.board_categories.sid", ondelete="SET NULL"),
        nullable=True,
        comment="Board category ID",
    )

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

    board_category = relationship(
        "BoardCategories",
        back_populates="boards",
        lazy="select",
    )
