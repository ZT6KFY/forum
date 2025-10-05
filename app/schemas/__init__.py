# app/schemas/__init__.py

from .users.users import (
    UserBase as UserBase,
    UserCreate as UserCreate,
    UserUpdate as UserUpdate,
    UserInfo as UserInfo,
)

from .boards.boards import (
    BoardBase as BoardBase,
    BoardCreate as BoardCreate,
    BoardUpdate as BoardUpdate,
    BoardInfo as BoardInfo,
)

from .post_votes.post_votes import (
    PostVotesBase as PostVotesBase,
    PostVotesCreate as PostVotesCreate,
    PostVotesUpdate as PostVotesUpdate,
    PostVotesInfo as PostVotesInfo,
)

__all__ = [
    # Users
    "UserBase",
    "UserCreate",
    "UserUpdate",
    "UserInfo",
    # Boards
    "BoardBase",
    "BoardCreate",
    "BoardUpdate",
    "BoardInfo",
    # PostVotes
    "PostVotesBase",
    "PostVotesCreate",
    "PostVotesUpdate",
    "PostVotesnfo",
]
