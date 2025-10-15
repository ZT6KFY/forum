from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = "16ced7899727"
down_revision: Union[str, Sequence[str], None] = "f34a5d703adc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS votes;")
    op.create_table(
        "thread_votes",
        sa.Column("thread_sid", sa.UUID(), nullable=False, comment="Thread ID"),
        sa.Column("user_sid", sa.UUID(), nullable=False, comment="User ID"),
        sa.Column(
            "value", sa.Integer(), nullable=False, comment="Value of thread votes"
        ),
        sa.Column("sid", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["thread_sid"], ["threads.threads.sid"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["user_sid"], ["users.users.sid"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("sid"),
        sa.UniqueConstraint("sid"),
        schema="votes",
        comment="Thread Votes table",
    )


def downgrade() -> None:
    op.drop_table("thread_votes", schema="votes")
