# app/models/__init__.py
from .posts.posts import Posts
from .posts.post_votes import PostVotes
from .threads.threads import Threads
from .threads.thread_votes import ThreadVotes
from .users.users import Users
from .boards.boards import Boards
from .boards.board_categories import BoardCategories
from .admin_logs.admin_logs import AdminLogs

__all__ = [
    "Posts",
    "PostVotes",
    "Threads",
    "ThreadVotes",
    "Users",
    "Boards",
    "BoardCategories",
    "AdminLogs",
]
