from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.BaseRepository import BaseRepository
from app.repositories.VoteMixin import VoteMixin
from app.models.threads.threads import Threads
from app.models.threads.thread_votes import ThreadVotes
from app.schemas.threads.thread_votes import ThreadVotesCreate, ThreadVotesUpdate


class ThreadVotesRepository(
    BaseRepository[ThreadVotes, ThreadVotesCreate, ThreadVotesUpdate], VoteMixin
):
    async def toggle_vote(self, db: AsyncSession, thread_sid, user_sid, value):
        return await self._toggle_vote_logic(
            db=db,
            vote_model=ThreadVotes,  # <-- ТУТ ThreadVotes
            entity_model=Threads,  # <-- ТУТ Threads
            entity_fk_field="thread_sid",  # <-- И поле thread_sid
            entity_sid=thread_sid,
            user_sid=user_sid,
            value=value,
        )


thread_votes_repository = ThreadVotesRepository(ThreadVotes)
