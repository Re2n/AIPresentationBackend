from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.User import UserCreate
from schemas.Action import Action
from schemas.User import User


class UserRepository:
    async def create_user(self, session: AsyncSession, user: UserCreate):
        new_user = User(**user.model_dump())
        new_action = Action(senderId=user.senderId)
        session.add(new_user)
        await session.commit()
        session.add(new_action)
        await session.commit()
        await session.refresh(new_user)
        return user

    async def check_balance(self, session: AsyncSession, senderId: int):
        stmt = select(User.balanceRub).where(User.senderId == senderId)
        result = await session.execute(stmt)
        return result.scalar()
