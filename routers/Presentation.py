import asyncio

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from starlette.responses import FileResponse

from config.Database import db
from depends import presentation_service
from models.Presentation import PresentationCreate


presentation_router = APIRouter(tags=["Presentation"])


# @presentation_router.post("/create", response_class=FileResponse)
# async def create_presentation(
#     session: Annotated[AsyncSession, Depends(db.session_getter)],
#     presentation: PresentationCreate,
# ):
#     file_path = await presentation_service.create_presentation(presentation, session)
#     return file_path


@presentation_router.get("/test", response_class=FileResponse)
async def test_presentation():
    file_path = "123.pdf"
    await asyncio.sleep(5)
    return FileResponse(file_path, media_type="application/pdf", filename="test.pdf")
