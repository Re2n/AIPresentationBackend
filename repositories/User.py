from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update

from models.ActionModel import ActionModel
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
        stmt1 = select(User.balanceGeneration).where(User.senderId == senderId)
        result1 = await session.execute(stmt1)
        return result.scalar(), result1.scalar()

    async def add_action(self, session: AsyncSession, senderId: int, action: ActionModel):
        match action:
            case 'actionStart':
                stmt_first = select(Action.actionStart).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionStart = number.scalar() + 1)
                await session.execute(stmt)
                await session.commit()
                return True
            case 'actionPayment':
                stmt_first = select(Action.actionPayment).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionPayment = number.scalar() + 1)
                await session.execute(stmt)
                await  session.commit()
                return True
            case 'actionGeneration':
                stmt_first = select(Action.actionGeneration).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionGeneration = number.scalar() + 1)
                await session.execute(stmt)
                await  session.commit(stmt)
                return True
            case 'actionLowGeneration':
                stmt_first = select(Action.actionLowGeneration).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionLowGeneration=number.scalar() + 1)
                await session.execute(stmt)
                await  session.commit()
                return True
            case 'actionHighGeneration':
                stmt_first = select(Action.actionHighGeneration).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionHighGeneration=number.scalar() + 1)
                await session.execute(stmt)
                await  session.commit()
                return True
            case 'actionSendUrl':
                stmt_first = select(Action.actionSendUrl).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionSendUrl=number.scalar() + 1)
                await session.execute(stmt)
                await  session.commit()
                return True
            case 'actionSendPictures':
                stmt_first = select(Action.actionSendPictures).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionSendPictures=number.scalar() + 1)
                await session.execute(stmt)
                await  session.commit()
                return True
            case 'actionSendDescription':
                stmt_first = select(Action.actionSendDescription).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionSendDescription=number.scalar() + 1)
                await session.execute(stmt)
                await  session.commit()
                return True
            case 'actionSendType':
                stmt_first = select(Action.actionSendType).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionSendType=number.scalar() + 1)
                await session.execute(stmt)
                await  session.commit()
                return True
            case 'actionCheckBalance':
                stmt_first = select(Action.actionCheckBalance).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionCheckBalance=number.scalar() + 1)
                await session.execute(stmt)
                await  session.commit()
                return True
            case 'actionSuccessGeneration':
                stmt_first = select(Action.actionSuccessGeneration).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionSuccessGeneration=number.scalar() + 1)
                await session.execute(stmt)
                await  session.commit()
                return True
            case 'actionSuccessPayment':
                stmt_first = select(Action.actionSuccessPayment).where(Action.senderId == senderId)
                number = await session.execute(stmt_first)
                stmt = update(Action).where(Action.senderId == senderId).values(actionSuccessPayment=number.scalar() + 1)
                await session.execute(stmt)
                await  session.commit()
                return True
