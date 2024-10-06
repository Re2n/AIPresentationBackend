from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.User import UserCreate
from repositories.User import UserRepository
from schemas.User import User


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(self, session: AsyncSession, user: UserCreate):
        stmt = select(User).where(User.senderId == user.senderId)
        result = await session.execute(stmt)
        if result.scalar():
            return {'User already exists'}
        new_user = await self.repository.create_user(session, user)
        return {'user': new_user, 'status': 200}

    async def check_balance(self, session: AsyncSession, senderId: int):
        res = await self.repository.check_balance(session, senderId)
        return res