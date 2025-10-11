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

from .boards.board_category import (
    BoardCategoryBase as BoardCategoryBase,
    BoardCategoryCreate as BoardCategoryCreate,
    BoardCategoryUpdate as BoardCategoryUpdate,
    BoardCategoryInfo as BoardCategoryInfo,
)


from .post_votes.post_votes import (
    PostVotesBase as PostVotesBase,
    PostVotesCreate as PostVotesCreate,
    PostVotesUpdate as PostVotesUpdate,
    PostVotesInfo as PostVotesInfo,
)

from .posts.posts import (
    PostBase as PostBase,
    PostCreate as PostCreate,
    PostUpdate as PostUpdate,
    PostInfo as PostInfo,
)

from .threads.threads import (
    ThreadBase as ThreadBase,
    ThreadCreate as ThreadCreate,
    ThreadUpdate as ThreadUpdate,
    ThreadInfo as ThreadInfo,
)

from .admin_logs.admin_logs import (
    AdminLogBase as AdminLogBase,
    AdminLogCreate as AdminLogCreate,
    AdminLogUpdate as AdminLogUpdate,
    AdminLogInfo as AdminLogInfo,
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
    # BoardCategory
    "BoardCategoryBase",
    "BoardCategoryCreate",
    "BoardCategoryUpdate",
    "BoardCategoryInfo",
    # PostVotes
    "PostVotesBase",
    "PostVotesCreate",
    "PostVotesUpdate",
    "PostVotesInfo",
    # Posts
    "PostBase",
    "PostCreate",
    "PostUpdate",
    "PostInfo",
    # Threads
    "ThreadBase",
    "ThreadCreate",
    "ThreadUpdate",
    "ThreadInfo",
    # AdminLogs
    "AdminLogBase",
    "AdminLogCreate",
    "AdminLogUpdate",
    "AdminLogInfo",
]
