from uuid import UUID
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession


class VoteMixin:
    async def _toggle_vote_logic(
        self,
        db: AsyncSession,
        vote_model,
        entity_model,
        entity_fk_field: str,
        entity_sid: UUID,
        user_sid: UUID,
        value: int,
    ):
        vote_filter = (getattr(vote_model, entity_fk_field) == entity_sid) & (
            vote_model.user_sid == user_sid
        )

        stmt = select(vote_model).where(vote_filter)
        result = await db.execute(stmt)
        existing_vote = result.scalar_one_or_none()

        score_delta = 0
        current_vote_value = value

        if existing_vote:
            if existing_vote.value == value:
                # то же голос => убирает голос
                await db.delete(existing_vote)
                score_delta = -value
                current_vote_value = None
            else:
                # смена голоса на противоположный
                score_delta = value - existing_vote.value
                existing_vote.value = value
        else:
            # новый голос
            create_kwargs = {
                entity_fk_field: entity_sid,
                "user_sid": user_sid,
                "value": value,
            }
            new_vote = vote_model(**create_kwargs)
            db.add(new_vote)
            score_delta = value

        # обновление счетчика
        stmt_entity = (
            update(entity_model)
            .where(entity_model.sid == entity_sid)
            .values(score=entity_model.score + score_delta)
            .returning(entity_model.score)
        )
        result_entity = await db.execute(stmt_entity)
        new_score = result_entity.scalar_one()

        await db.commit()

        return new_score, current_vote_value
