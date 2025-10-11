from uuid import UUID


from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database.base_model import Base

BOARDS_SCHEMA = "boards"


class BoardCategories(Base):
    __tablename__ = "board_categories"
    __table_args__ = {"schema": BOARDS_SCHEMA, "comment": "Board categories table"}

    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Title of the board category",
    )

    board_sid: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("boards.boards.sid", ondelete="SET NULL"),
        nullable=True,
        comment="Board ID",
    )

    boards = relationship(
        "Boards",
        back_populates="board_category",
        lazy="select",
    )
