"""move post votes to posts schema

Revision ID: fdddacb790a5
Revises: a1d4515c3b31
Create Date: 2026-01-13 18:50:38.724220

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "fdddacb790a5"
down_revision: Union[str, Sequence[str], None] = "a1d4515c3b31"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS posts")

    op.execute("ALTER TABLE post_votes.post_votes SET SCHEMA posts")

    op.execute("DROP SCHEMA IF EXISTS post_votes CASCADE")


def downgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS post_votes")
    op.execute("ALTER TABLE posts.post_votes SET SCHEMA post_votes")
