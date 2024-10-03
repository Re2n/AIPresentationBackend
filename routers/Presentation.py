from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from starlette.responses import FileResponse

from config.Database import db
from depends import presentation_service
from models.Presentation import PresentationCreate


router = APIRouter(tags=["Presentation"])


@router.post("/create", response_class=FileResponse)
async def create_presentation(
    session: Annotated[AsyncSession, Depends(db.session_getter)],
    presentation: PresentationCreate,
):
    file_path = await presentation_service.create_presentation(presentation, session)
    return file_path
