from uuid import UUID
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.post_votes.post_votes import PostVotes
from app.models.posts.posts import Posts
from app.repositories.BaseRepository import BaseRepository
from app.schemas import PostVotesCreate, PostVotesUpdate


class PostVotesRepository(BaseRepository[PostVotes, PostVotesCreate, PostVotesUpdate]):
    async def toggle_vote(
        self, db: AsyncSession, post_sid: UUID, user_sid: UUID, value: int
    ):
        # поиск существующего голоса
        stmt = select(PostVotes).where(
            PostVotes.post_sid == post_sid, PostVotes.user_sid == user_sid
        )
        result = await db.execute(stmt)
        existing_vote = result.scalar_one_or_none()

        score_delta = 0
        current_vote_value = value

        if existing_vote:
            if existing_vote.value == value:
                # голос существовал и он такой же (удаление голоса)
                await db.delete(existing_vote)
                score_delta = -value
                current_vote_value = None
            else:
                # голос существовал, смена на противоположный
                score_delta = value - existing_vote.value
                existing_vote.value = value
        else:
            # если голоса ранее не существовало
            new_vote = PostVotes(post_sid=post_sid, user_sid=user_sid, value=value)
            db.add(new_vote)
            score_delta = value
        # обновление счетчика
        stmt_post = (
            update(Posts)
            .where(Posts.sid == post_sid)
            .values(score=Posts.score + score_delta)
            .returning(Posts.score)
        )
        result_post = await db.execute(stmt_post)
        new_score = result_post.scalar_one()

        await db.commit()
        return new_score, current_vote_value


post_votes_repository = PostVotesRepository(PostVotes)
