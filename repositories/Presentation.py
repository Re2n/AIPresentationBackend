from sqlalchemy.ext.asyncio import AsyncSession

from models.Presentation import PresentationCreate


class PresentationRepository:
    pass

    # async def create_presentation(
    #     self, presentation_create: PresentationCreate, session: AsyncSession
    # ):
    #     # ...
    #     presentation = PresentationCreate(
    #         name="aboba",
    #     )
    #     file_path = "ananas.jpg"
    #     session.add(presentation)
    #     await session.commit()
    #     return file_path
