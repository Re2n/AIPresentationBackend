from typing import Annotated

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Depends

from config.Database import db
from depends import user_service
from models.ActionModel import ActionModel
from models.User import UserCreate


user_router = APIRouter(tags=["User"])


@user_router.post("/register")
async def register_user(
    session: Annotated[AsyncSession, Depends(db.session_getter)],
    create_user: UserCreate,
):
    res = await user_service.create_user(session, create_user)
    return res

@user_router.get("/{senderId}/checkBalance")
async def check_balance(
    senderId: int, session: AsyncSession = Depends(db.session_getter)
):
    res = await user_service.check_balance(session, senderId)
    return {'status': 200, 'balanceRub': res[0], 'balanceGeneration': res[1]}

@user_router.put("/add_action")
async def add_action(senderId: int, action: ActionModel, session: AsyncSession = Depends(db.session_getter)):
    res = await user_service.add_action(session, senderId, action)
    return res
