from app.models import Posts
from app.repositories.BaseRepository import BaseRepository
from app.schemas import (
    PostCreate,
    PostUpdate,
)


class PostRepository(BaseRepository[Posts, PostCreate, PostUpdate]):
    pass


post_repository = PostRepository(Posts)
