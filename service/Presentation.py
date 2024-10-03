from sqlalchemy.ext.asyncio import AsyncSession

from models.Presentation import PresentationCreate
from repositories.Presentation import PresentationRepository


class PresentationService:
    def __init__(self, repository: PresentationRepository):
        self.repository = repository

    async def create_presentation(
        self, presentation: PresentationCreate, session: AsyncSession
    ):
        presentation_path = await self.repository.create_presentation(
            presentation, session
        )
        return presentation_path
