from app.models import PostVotes
from app.repositories.BaseRepository import BaseRepository
from app.schemas import (
    PostVotesCreate,
    PostVotesUpdate,
)


class PostVotesRepository(BaseRepository[PostVotes, PostVotesCreate, PostVotesUpdate]):
    pass


post_votes_repository = PostVotesRepository(PostVotes)
