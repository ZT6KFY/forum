from sqlalchemy import String
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

    boards = relationship(
        "Boards",
        back_populates="board_category",
        cascade="all, delete-orphan",
        lazy="select",
    )
