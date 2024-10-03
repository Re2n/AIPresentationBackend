from sqlalchemy.ext.asyncio import AsyncSession

from models.Presentation import PresentationCreate
from schemas.Presentation import Presentation


class PresentationRepository:

    async def create_presentation(
        self, presentation_create: PresentationCreate, session: AsyncSession
    ):
        # ...
        presentation = Presentation(
            name="aboba",
        )
        file_path = "ananas.jpg"
        session.add(presentation)
        await session.commit()
        return file_path
