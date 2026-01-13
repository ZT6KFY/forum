from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.BaseRepository import BaseRepository
from app.repositories.VoteMixin import VoteMixin
from app.models.posts.posts import Posts
from app.models.posts.post_votes import PostVotes
from app.schemas import PostVotesCreate, PostVotesUpdate


class PostVotesRepository(
    BaseRepository[PostVotes, PostVotesCreate, PostVotesUpdate], VoteMixin
):
    async def toggle_vote(self, db: AsyncSession, post_sid, user_sid, value):
        return await self._toggle_vote_logic(
            db=db,
            vote_model=PostVotes,
            entity_model=Posts,
            entity_fk_field="post_sid",
            entity_sid=post_sid,
            user_sid=user_sid,
            value=value,
        )


post_votes_repository = PostVotesRepository(PostVotes)
