from typing import Annotated

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Depends

from config.Database import db
from depends import user_service
from models.User import UserCreate



user_router = APIRouter(tags=["User"])

@user_router.post("/register")
async def register_user(session: Annotated[AsyncSession, Depends(db.session_getter)],
                        create_user: UserCreate,
):
    res = await user_service.create_user(session, create_user)
    return res

@user_router.post("/checkBalance/{senderId}")
async def check_balance(senderId: int, session: AsyncSession = Depends(db.session_getter)):
    res = await user_service.check_balance(session, senderId)
    return res
